(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function fractions_to_decimals(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // generating numerator
    let numerator, denominator;
    const switch_ = P.randint(0, 2);
    if (switch_ === 0) {
        numerator = P.randint(1, 9);
    } else if (switch_ === 1) {
        numerator = P.randint(1, 1000);
    } else {
        numerator = P.randint(1, 100);
    }
    // end generating numerator

    // generating denominator
    if (P.randint(0, 2) === 0) {
        denominator = 10 ** P.int(P.round(P.triangular(1, 6, 2), 0));
    } else {
        denominator = 100;
    }
    // end generating denominator

    const right_answer = numerator / denominator;
    right_answers = [right_answer];   // a number, as in the Python original
    input_message = "convert to decimals:" + String(numerator) + "/" + String(denominator) + "= ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.fractions_to_decimals = fractions_to_decimals;
})();
