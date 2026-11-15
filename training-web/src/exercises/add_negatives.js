(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function add_negatives(difficulty) {
    let right_answers, input_message, prompt;

    const n = Math.floor(Math.random() * (100 - 10 + 1)) + 10;
    const n_sign = Math.floor(Math.random() * 2) === 1 ? -1 : 1;

    const m = Math.floor(Math.random() * (100 - 10 + 1)) + 10;
    const m_sign = Math.floor(Math.random() * 2) === 1 ? -1 : 1;

    let right_answer = n * n_sign + m * m_sign;
    right_answer = String(right_answer);
    right_answers = [right_answer];
    input_message = String(n * n_sign) + (m_sign === 1 ? "+" : "") +
        String(m * m_sign) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.add_negatives = add_negatives;
})();
