
import json
import re
from pathlib import Path


ROOT = Path(__file__).resolve().parent

SRC = ROOT / "src"
CONFIG_DIR = SRC / "config"
EXERCISES_DIR = SRC / "exercises"

TEMPLATE_FILE = SRC / "template.html"
CSS_FILE = SRC / "style.css"
CORE_FILE = SRC / "core.js"

DIST_DIR = ROOT / "dist"
OUTPUT_FILE = DIST_DIR / "training.html"

# This marker separates the registration API from the rest of core.js.
# Exercise modules must be inserted between these two sections.
CORE_INSERTION_MARKER = "// CONFIGURATION"


def read_text(path):
    if not path.is_file():
        raise FileNotFoundError(f"Missing file: {path}")

    return path.read_text(encoding="utf-8")


def load_config(path):
    try:
        data = json.loads(read_text(path))
    except json.JSONDecodeError as error:
        raise ValueError(
            f"Invalid JSON in {path.name}: {error}"
        )

    if not isinstance(data, dict):
        raise ValueError(
            f"{path.name} must contain a JSON object."
        )

    return data


def discover_configs():
    if not CONFIG_DIR.is_dir():
        raise FileNotFoundError(
            f"Configuration folder not found: {CONFIG_DIR}"
        )

    files = sorted(CONFIG_DIR.rglob("*.json"))

    if not files:
        raise RuntimeError("No configuration files found.")

    configs = []

    for path in files:
        config = load_config(path)

        exercise_id = config.get("id")

        if not isinstance(exercise_id, str) or not exercise_id:
            raise ValueError(
                f"{path.name}: missing or invalid 'id'."
            )

        if not re.fullmatch(r"[a-zA-Z0-9_-]+", exercise_id):
            raise ValueError(
                f"{path.name}: invalid exercise ID '{exercise_id}'."
            )

        if path.stem != exercise_id:
            raise ValueError(
                f"{path.name}: filename must match ID "
                f"'{exercise_id}'."
            )

        if not isinstance(config.get("name"), str):
            raise ValueError(
                f"{path.name}: missing exercise name."
            )

        subjects = config.get("subjects")

        if (
            not isinstance(subjects, list)
            or not subjects
            or not all(
                isinstance(subject, str) and subject.strip()
                for subject in subjects
            )
        ):
            raise ValueError(
                f"{path.name}: subjects must be a non-empty "
                f"array of strings."
            )

        if len(set(subjects)) != len(subjects):
            raise ValueError(
                f"{path.name}: duplicate subject entries."
            )

        configs.append(config)

    return configs


def discover_exercises():
    if not EXERCISES_DIR.is_dir():
        raise FileNotFoundError(
            f"Exercise folder not found: {EXERCISES_DIR}"
        )

    files = sorted(EXERCISES_DIR.rglob("*.js"))

    if not files:
        raise RuntimeError("No exercise modules found.")

    return files


def validate_pairing(configs, exercise_files):
    config_ids = {config["id"] for config in configs}
    module_ids = {path.stem for path in exercise_files}

    missing_modules = config_ids - module_ids
    missing_configs = module_ids - config_ids

    if missing_modules:
        raise RuntimeError(
            "Missing JavaScript modules for: "
            + ", ".join(sorted(missing_modules))
        )

    if missing_configs:
        raise RuntimeError(
            "Missing JSON configurations for: "
            + ", ".join(sorted(missing_configs))
        )

    if len(module_ids) != len(exercise_files):
        raise RuntimeError(
            "Duplicate exercise IDs found in module filenames."
        )

    if len(config_ids) != len(configs):
        raise RuntimeError(
            "Duplicate exercise IDs found in configurations."
        )


def split_core(core):
    """
    Split core.js into two sections:

    1. Registration API:
       Defines Training.registerExercise() and the registry.

    2. Game core:
       Loads configurations and starts the game.

    Exercise modules are inserted between these sections.
    """

    if core.count(CORE_INSERTION_MARKER) != 1:
        raise RuntimeError(
            "core.js must contain exactly one "
            f"'{CORE_INSERTION_MARKER}' marker."
        )

    core_prefix, marker, core_suffix = core.partition(
        CORE_INSERTION_MARKER
    )

    if not marker:
        raise RuntimeError(
            "Could not find the core insertion marker."
        )

    return core_prefix, marker + core_suffix


def embed_config(configs):
    # Prevent JSON strings from accidentally terminating
    # the surrounding HTML script element.
    serialized = json.dumps(
        configs,
        ensure_ascii=False,
        separators=(",", ":")
    )

    serialized = (
        serialized
        .replace("<", "\\u003c")
        .replace(">", "\\u003e")
        .replace("&", "\\u0026")
    )

    return f"window.TRAINING_CONFIG = {serialized};"


def build_scripts(core, exercise_files):
    core_prefix, core_suffix = split_core(core)

    scripts = []

    # 1. Start the core and define the Training API.
    scripts.append(core_prefix)

    # 2. Register every discovered exercise.
    for path in exercise_files:
        print(f"Adding module: {path.relative_to(ROOT)}")
        scripts.append(read_text(path))

    # 3. Continue the core: load configurations and start the game.
    scripts.append(core_suffix)

    return "\n\n".join(scripts)


def assemble():
    print("TRAINING BUILD")
    print("-------------")

    template = read_text(TEMPLATE_FILE)
    css = read_text(CSS_FILE)
    core = read_text(CORE_FILE)

    configs = discover_configs()
    exercise_files = discover_exercises()

    validate_pairing(configs, exercise_files)

    print(f"Configurations found: {len(configs)}")
    print(f"Exercise modules found: {len(exercise_files)}")

    # Build JavaScript in the correct execution order.
    script_content = build_scripts(core, exercise_files)

    replacements = {
        "/*__CSS__*/": css,
        "/*__CONFIG__*/": embed_config(configs),
        "/*__SCRIPTS__*/": script_content
    }

    html = template

    for placeholder, content in replacements.items():
        if placeholder not in html:
            raise RuntimeError(
                f"Template placeholder missing: {placeholder}"
            )

        html = html.replace(placeholder, content, 1)

    # Ensure no placeholder was accidentally left behind.
    for placeholder in replacements:
        if placeholder in html:
            raise RuntimeError(
                f"Unresolved placeholder: {placeholder}"
            )

    DIST_DIR.mkdir(parents=True, exist_ok=True)

    OUTPUT_FILE.write_text(html, encoding="utf-8")

    print("")
    print("BUILD SUCCESSFUL")
    print(f"Output: {OUTPUT_FILE}")
    print(f"Exercises: {len(configs)}")


if __name__ == "__main__":
    try:
        assemble()
    except Exception as error:
        print("")
        print("BUILD FAILED")
        print(error)
        raise SystemExit(1)
