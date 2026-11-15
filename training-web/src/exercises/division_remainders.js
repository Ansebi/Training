(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function division_remainders(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const divisor = P.randint(1, 11);
    const remainder = P.randint(0, divisor - 1);
    const quotient = P.randint(0, 9);
    const divident = divisor * quotient + remainder;
    let right_answer;
    if (remainder > 0) {
        if (quotient !== 0) {
            right_answer = String(quotient) + "r" + String(remainder);
        } else {
            right_answer = "0r" + String(remainder);
        }
    } else {
        if (quotient !== 0) {
            right_answer = String(quotient);
        } else {
            right_answer = String(0);
        }
    }

    input_message = String(divident) + ":" + String(divisor) + " = ";
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.division_remainders = division_remainders;
})();
