(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function round_whole_numbers(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const n = P.randint(1, 1000000);
    const n_sign = P.randint(0, 1) === 1 ? -1 : 1;

    const m = 10 ** P.randint(1, 5);
    let right_answer = n_sign * Math.trunc(P.round(n / m, 0) * m);
    right_answer = String(right_answer);
    right_answers = [right_answer];
    input_message = String(n * n_sign) + " rounded by " + String(m) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.round_whole_numbers = round_whole_numbers;
})();
