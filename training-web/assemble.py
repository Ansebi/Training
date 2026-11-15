#!/usr/bin/env python3
"""Assemble the modular Training CMD project into dist/training.html."""

from pathlib import Path
import json
import re

ROOT = Path(__file__).resolve().parent
SRC = ROOT / "src"


def enabled_exercises():
    """Return (configs, module_sources) for every enabled exercise."""
    configs = []
    modules = []
    for config_path in sorted((SRC / "config").glob("*.json")):
        config = json.loads(config_path.read_text(encoding="utf-8"))
        if not config.get("enabled", False):
            continue
        exercise_id = config["id"]
        module_path = SRC / "exercises" / f"{exercise_id}.js"
        if not module_path.is_file():
            raise FileNotFoundError(
                f"Enabled exercise {exercise_id!r} has no module: {module_path}"
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
        modules.append(module_path.read_text(encoding="utf-8").rstrip())
    return configs, modules


def core_modules():
    """Return the sources of src/core/*.js, ordered by file name."""
    paths = sorted((SRC / "core").glob("*.js"))
    if not paths:
        raise FileNotFoundError(f"No core modules found in {SRC / 'core'}")
    return [p.read_text(encoding="utf-8").rstrip() for p in paths]


def main():
    template = (SRC / "template.html").read_text(encoding="utf-8")
    configs, modules = enabled_exercises()

    # "</" is escaped so the JSON can never close the surrounding <script>.
    config_json = json.dumps(configs, ensure_ascii=False).replace("</", "<\\/")
    core = (SRC / "core.js").read_text(encoding="utf-8").rstrip()
    core = core.replace("{{CORE_MODULES}}", "\n\n".join(core_modules()))
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
