(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function add_decimals_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    let n, m;
    if (P.randint(1, 5) > 2) {
        n = P.randint(0, 10);
    } else {
        n = P.randint(10, 100) / 10;
    }
    const n_sign = P.randint(1, 10) > 4 ? -1 : 1;

    if (P.randint(1, 3) === 1 && n % 1 !== 0) {
        m = P.randint(0, 10);
    } else {
        m = P.randint(10, 100) / 10;
    }
    const m_sign = P.randint(1, 10) > 3 ? -1 : 1;

    n = n * n_sign;
    m = m * m_sign;

    let right_answer = P.round(n + m, 2);

    if (n % 1 === 0) {
        n = P.int(n);
    }
    if (m % 1 === 0) {
        m = P.int(m);
    }

    let m_string;
    if (m >= 0) {
        m_string = "+" + P.numStr(m);
    } else {
        m_string = P.numStr(m);
    }

    input_message = P.numStr(n) + m_string + " = ";

    if (right_answer % 1 === 0) {
        right_answer = P.int(right_answer);
    }
    right_answer = P.numStr(right_answer);
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.add_decimals_easy = add_decimals_easy;
})();
