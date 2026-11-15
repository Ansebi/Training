(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function roots(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // constants:
    const low = 0, high = 17, mode = 2, how_narrow_is_option_2 = 3, option_2_probability = 40;

    const option_1 = P.int(P.round(P.triangular(low, high, mode), 0));

    const option_2 = P.int(P.round(
        P.triangular(5, 20, 11), 0));

    let right_answer, power;
    if (P.randint(1, 100) > option_2_probability) {
        right_answer = option_1;
    } else {
        right_answer = option_2;
    }

    // proper powers
    if (right_answer === 2) {
        power = P.randint(2, 14);
    } else if (right_answer < 6) {
        power = P.randint(2, 9 - right_answer);
    } else if (right_answer < 9) {
        power = P.randint(2, 3);
    } else {
        power = 2;
    }
    // end(proper powers)

    const n = right_answer ** power;

    let degree_of_the_root;
    if (power === 2) {
        degree_of_the_root = "square";
    } else if (power === 3) {
        degree_of_the_root = "cubic";
    } else {
        degree_of_the_root = String(power) + "th";
    }

    input_message = String(degree_of_the_root + " root of " + String(n) + " = ");
    right_answers = [right_answer];   // a number, as in the Python original

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.roots = roots;
})();
