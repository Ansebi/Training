(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function percent_of(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    let n, percent, right_answer;
    const switch_ = P.randint(1, 7);
    if (switch_ <= 4) {
        n = 10 * P.randint(20, 100);
        percent = P.randint(1, 20) * 5;
        right_answer = n * percent / 100;
    } else if (switch_ === 5) {
        n = P.randint(1, 100);
        percent = P.randint(1, 60) * 10;
        right_answer = n * percent / 100;
    } else if (switch_ === 6) {
        right_answer = 0.1;
        while (right_answer % 1 !== 0) {
            n = P.randint(1, 600);
            percent = P.randint(0, 100);
            right_answer = n * percent / 100;
        }
    } else {
        right_answer = 0.1;
        percent = 100;
        while (right_answer % 1 !== 0 || percent === 100) {
            n = P.randint(1, 600);
            percent = P.randint(0, 600);
            right_answer = n * percent / 100;
        }
    }

    input_message = String(percent) + "% of " + String(n) + " = ";
    if (right_answer % 1 === 0) {
        right_answer = P.int(right_answer);
    }
    right_answer = P.numStr(right_answer);
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.percent_of = percent_of;
})();
