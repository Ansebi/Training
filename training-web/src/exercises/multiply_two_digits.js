(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function multiply_two_digits(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // NOTE: this is the LATER of two definitions in the Python file, so it is the one that wins there
    let n1, n2;
    if (P.randint(0, 1) === 1) {
        n1 = P.randint(3, 13);
        n2 = P.randint(3, 13);
    } else {
        n1 = P.int(P.round(P.triangular(1, 99, 25), 0));
        n2 = P.randint(0, 10);
    }

    const right_answer = String(n1 * n2);
    right_answers = [right_answer];
    input_message = String(n1) + " * " + String(n2) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.multiply_two_digits = multiply_two_digits;
})();
