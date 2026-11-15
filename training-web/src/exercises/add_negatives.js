(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function add_negatives(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const n = P.randint(10, 100);
    const n_sign = P.randint(0, 1) === 1 ? -1 : 1;

    const m = P.randint(10, 100);
    const m_sign = P.randint(0, 1) === 1 ? -1 : 1;

    let right_answer = n * n_sign + m * m_sign;
    right_answer = String(right_answer);
    right_answers = [right_answer];
    input_message = m_sign === 1
        ? String(n * n_sign) + "+" + String(m * m_sign) + " = "
        : String(n * n_sign) + String(m * m_sign) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.add_negatives = add_negatives;
})();
