# Training CMD

Build the standalone HTML file from the project root:

```bash
python assemble.py
```

The result is `dist/training.html`. It contains the CSS, enabled exercise modules, and core JavaScript inline, so it can be opened directly in a browser.

## Project structure

- `src/template.html` — HTML document shell and assembly placeholders.
- `src/style.css` — terminal styling.
- `src/core.js` — terminal, menus, training flow, scoring, and history.
- `src/config/*.json` — exercise metadata and enabled flags.
- `src/exercises/*.js` — exercise implementations.
- `dist/training.html` — generated standalone page.

## Adding an exercise

Create a config JSON and a matching `src/exercises/<id>.js` file. The exercise module registers a function on `window.TrainingExercises` using the config ID. The function receives `difficulty` and returns an object containing `right_answers`, `input_message`, and `prompt`.
