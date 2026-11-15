(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function logs(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    let power, right_answer;
    const mode = P.randint(1, 3);
    const base = P.randint(2, 13);
    if (mode < 3) {
        // proper powers
        if (base === 2) {
            power = P.randint(0, 14);
        } else if (base < 6) {
            power = P.randint(0, 9 - base);
        } else if (base < 9) {
            power = P.randint(0, 3);
        } else {
            power = P.randint(0, 2);
        }
        // end(proper powers)
    } else {
        if (base === 2) {
            power = P.randint(1, 14);
        } else if (base < 6) {
            power = P.randint(1, 9 - base);
        } else if (base < 9) {
            power = P.randint(1, 3);
        } else {
            power = P.randint(1, 2);
        }
    }

    const number = base ** power;

    if (mode === 1) {
        // log a (b) = x
        right_answer = power;
        input_message = "log " + String(base) + " (" + String(number) + ") = ";
    } else if (mode === 2) {
        // log a (x) = c
        right_answer = number;
        input_message = "log " + String(base) + " (x) = " + String(power) + "\nx = ";
    } else {
        // log x (b) = c
        right_answer = base;
        input_message = "log x (" + String(number) + ") = " + String(power) + "\nx = ";
    }

    right_answer = String(right_answer);
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.logs = logs;
})();
