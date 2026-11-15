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
    """Return (configs, module_sources) for enabled exercise scripts."""
    configs = []
    modules = []

    config_dir = SRC / "config"
    default_path = config_dir / "default.json"

    default_config = None
    if default_path.is_file():
        default_config = json.loads(default_path.read_text(encoding="utf-8"))

    for module_path in sorted((SRC / "exercises").glob("*.js")):
        exercise_id = module_path.stem

        if not EXERCISE_ID_RE.match(exercise_id):
            print(f"warning: invalid exercise ID: {module_path.name}")
            continue

        config_path = config_dir / f"{exercise_id}.json"

        if config_path.is_file():
            config = json.loads(config_path.read_text(encoding="utf-8"))
        elif default_config is not None:
            print(
                f"warning: {config_path.name} missing; "
                "using default.json"
            )
            config = default_config
        else:
            print(
                f"warning: {config_path.name} and default.json missing; "
                "skipping"
            )
            continue

        if not config.get("enabled", False):
            continue

        source = module_path.read_text(encoding="utf-8").rstrip()

        if not re.search(
            rf"window\.TrainingExercises\.{re.escape(exercise_id)}\s*=",
            source
        ):
            print(f"warning: {module_path.name} does not register its exercise")
            continue

        subjects = config.get("subjects")
        if not isinstance(subjects, list) or not subjects:
            print(f"warning: {exercise_id} has no valid subjects; skipping")
            continue

        configs.append({
            "id": exercise_id,
            "name": config.get("name", exercise_id),
            "subjects": [str(s).strip().lower() for s in subjects],
        })
        modules.append(source)

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