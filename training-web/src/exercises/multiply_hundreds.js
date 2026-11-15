(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function multiply_hundreds(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // 26.05.2018 edition
    let m = 1, n = 1;
    if (P.choice([0, 0, 1, 1, 1]) === 0) {
        n = P.randint(0, 13) * 10 ** P.randint(0, 4);
        m = P.randint(1, 13) * 10 ** P.randint(0, 4);
    } else {
        while (m * n % 10 !== 0) {
            n = P.choice([P.randint(2, 9), P.randint(11, 13)]);
            m = P.choice([P.randint(2, 9), P.randint(11, 13)]);
        }
    }
    n = n * 10 ** P.randint(0, 4);
    m = m * 10 ** P.randint(0, 4);
    const n_sign = P.choice([-1, 1]);
    const m_sign = P.choice([-1, 1]);

    const right_answer = n_sign * n * m_sign * m;
    right_answers = [String(right_answer)];
    input_message = m_sign === 1
        ? String(n * n_sign) + " * " + String(m) + " = "
        : String(n * n_sign) + " * (" + String(m * m_sign) + ") = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.multiply_hundreds = multiply_hundreds;
})();
