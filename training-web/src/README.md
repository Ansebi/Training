# Training

A modular, offline-capable, CMD-style training application.

## Requirements

- Python 3.8+
- A modern web browser
- No external libraries

## Build

From the project root:

    python assemble.py

The assembler creates:

    dist/training.html

Open this HTML file in a browser.

## Architecture

Every exercise consists of two files:

    src/exercises/example.js
    src/config/example.json

The filenames and IDs must match.

## Adding an exercise

1. Create a JavaScript module in src/exercises/.
2. Create its JSON configuration in src/config/.
3. Give both files the same ID.
4. Register the module using Training.registerExercise().
5. Run python assemble.py.

No existing file needs to be modified.

## Exercise module API

    Training.registerExercise({
      id: "example",

      generate(rand, difficulty, settings) {
        return {
          prompt: "Question?",
          answer: 42
        };
      },

      check(question, userInput, settings) {
        return Number(userInput) === question.answer;
      }
    });

The custom check function is optional.

## Configuration fields

- id: unique exercise ID
- name: displayed exercise name
- subjects: array of subjects
- enabled: whether the exercise is available
- default_difficulty: initial difficulty
- min_difficulty: minimum difficulty
- max_difficulty: maximum difficulty
- increase_on_correct: increase difficulty after a correct answer
- decrease_on_wrong: decrease difficulty after an incorrect answer
- standard_completion_time_sec: reference time for the exercise
- settings: exercise-specific parameters

Optional:
- sort_order: controls position in the subject menu

## Multiple subjects

An exercise can belong to multiple subjects:

    "subjects": ["maths", "english"]

It appears in both menus but has only one implementation.

## Important rules

- Never use exercise numbers as IDs.
- Never depend on file order.
- Never hardcode configurable values in exercise logic.
- Never edit core.js just to add an exercise.
- Keep exercise logic independent of the interface.
- Keep each exercise's settings in its own JSON file.