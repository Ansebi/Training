(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function round_decimals(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // random.uniform(a, b) == a + (b - a) * random()
    const n = P.round(-1000 + (1000 - -1000) * Math.random(), P.randint(5, 7));
    const dp = P.randint(0, 4);
    let right_answer = P.round(n, dp);
    if (!dp) {
        right_answer = String(Math.trunc(right_answer));   // int(...)
    } else {
        right_answer = P.floatStr(right_answer);
    }
    right_answers = [right_answer];
    // Python: 10 ** (-dp) is int 1 for dp == 0, float otherwise
    const step = dp === 0 ? "1" : P.floatStr(Math.pow(10, -dp));
    input_message = P.floatStr(n) + " rounded by " + step + "(" + String(dp) + " d.p.) = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.round_decimals = round_decimals;
})();
