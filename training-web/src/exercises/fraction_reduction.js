(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function fraction_reduction(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const common_factor = P.randint(1, 11);
    const n_1 = P.randint(1, 13);
    const n_2 = P.randint(1, 13);
    let right_answer;
    if (!(n_1 % n_2)) {
        right_answer = P.int(n_1 / n_2);   // a number here, a string in the else branch (as in the Python)
    } else {
        const numerator = n_1 * common_factor;
        const denominator = n_2 * common_factor;
        right_answer = S.fraction_simplifier(numerator, denominator);
    }
    input_message = String(n_1 * common_factor) + "/" + String(n_2 * common_factor) + "= ";
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.fraction_reduction = fraction_reduction;
})();
