#!/usr/bin/env python3
"""Assemble the modular Training CMD project into dist/training.html."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"
CORE_DIR = SRC / "core"

EXERCISE_ID_RE = re.compile(r"^[A-Za-z_][A-Za-z0-9_]*$")
# A line consisting only of:  // @include name
INCLUDE_RE = re.compile(
    r"^[ \t]*//[ \t]*@include[ \t]+([A-Za-z0-9_-]+)[ \t]*$", re.MULTILINE
)


def enabled_exercises():
    """Return (configs, module_sources) for every enabled exercise.

    An exercise is identified by its file stem: config/<id>.json pairs with
    exercises/<id>.js, and the module must register window.TrainingExercises.<id>.
    """
    configs = []
    modules = []
    config_ids = set()

    for config_path in sorted((SRC / "config").glob("*.json")):
        exercise_id = config_path.stem
        config_ids.add(exercise_id)
        config = json.loads(config_path.read_text(encoding="utf-8"))

        if "id" in config and config["id"] != exercise_id:
            raise ValueError(
                f"{config_path.name}: 'id' {config['id']!r} does not match "
                f"filename; remove the 'id' field"
            )

        if not config.get("enabled", False):
            continue

        if not EXERCISE_ID_RE.match(exercise_id):
            raise ValueError(
                f"{config_path.name}: filename must be a valid identifier "
                f"(letters, digits, underscores; not starting with a digit)"
            )

        module_path = SRC / "exercises" / f"{exercise_id}.js"
        if not module_path.is_file():
            raise FileNotFoundError(
                f"Enabled exercise {exercise_id!r} has no module: {module_path}"
            )
        source = module_path.read_text(encoding="utf-8").rstrip()
        if not re.search(
            rf"window\.TrainingExercises\.{re.escape(exercise_id)}\s*=", source
        ):
            raise ValueError(
                f"{module_path.name} never assigns "
                f"window.TrainingExercises.{exercise_id}"
            )

        subjects = config.get("subjects")
        if not isinstance(subjects, list) or not subjects:
            raise ValueError(
                f"Exercise {exercise_id!r} needs a non-empty 'subjects' list"
            )

        configs.append({
            "id": exercise_id,
            "name": config.get("name", exercise_id),
            "subjects": [str(s).strip().lower() for s in subjects],
        })
        modules.append(source)

    for module_path in sorted((SRC / "exercises").glob("*.js")):
        if module_path.stem not in config_ids:
            print(f"warning: {module_path.name} has no config/{module_path.stem}.json")

    return configs, modules


def expand_core_includes(core_source):
    """Replace each '// @include name' line in core.js with core/name.js.

    core.js is the manifest: it fixes both which modules exist and their
    load order. Missing, duplicate and unlisted modules are build errors.
    """
    included = []

    def replace(match):
        name = match.group(1)
        path = CORE_DIR / f"{name}.js"
        if not path.is_file():
            raise FileNotFoundError(
                f"core.js includes {name!r} but {path} does not exist"
            )
        if name in included:
            raise ValueError(f"core.js includes {name!r} more than once")
        included.append(name)
        body = path.read_text(encoding="utf-8").rstrip()
        return f"// ---- core/{name}.js ----\n{body}\n"

    expanded = INCLUDE_RE.sub(replace, core_source)

    if not included:
        raise ValueError("core.js has no '// @include <module>' lines")

    unlisted = sorted({p.stem for p in CORE_DIR.glob("*.js")} - set(included))
    if unlisted:
        raise ValueError(
            "core modules not listed in core.js: "
            + ", ".join(f"{n}.js" for n in unlisted)
        )
    return expanded


def main():
    template = (SRC / "template.html").read_text(encoding="utf-8")
    configs, modules = enabled_exercises()

    # "</" is escaped so the JSON can never close the surrounding <script>.
    config_json = json.dumps(configs, ensure_ascii=False).replace("</", "<\\/")
    core = (SRC / "core.js").read_text(encoding="utf-8").rstrip()
    core = expand_core_includes(core)
    core = core.replace("{{EXERCISE_CONFIG}}", config_json)

    replacements = {
        "{{STYLE}}": (SRC / "style.css").read_text(encoding="utf-8").rstrip(),
        "{{EXERCISES}}": "\n\n".join(modules),
        "{{CORE}}": core,
    }
    html = template
    for marker, content in replacements.items():
        html = html.replace(marker, content)
    unresolved = re.findall(r"\{\{[A-Z_]+\}\}", html)
    if unresolved:
        raise ValueError(f"Unresolved template markers: {unresolved}")
    destination = ROOT / "dist" / "training.html"
    destination.parent.mkdir(parents=True, exist_ok=True)
    destination.write_text(html, encoding="utf-8")
    print(f"Built {destination.relative_to(ROOT)}")


if __name__ == "__main__":
    main()