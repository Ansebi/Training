(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function multiply_two_digits(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // n * m
    const n = P.randint(10, 100);
    const m = P.randint(2, 11);
    const right_answer = n * m;
    right_answers = [String(right_answer)];
    input_message = String(n) + " * " + String(m) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.multiply_two_digits = multiply_two_digits;
})();
