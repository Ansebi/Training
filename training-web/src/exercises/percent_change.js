(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function percent_change(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    let n, percent, percent_delta;
    const switch_ = P.randint(1, 7);
    if (switch_ <= 4) {
        n = P.randint(1, 100) * 10 ** P.randint(0, 2);
        percent = P.randint(1, 20) * 5;
        percent_delta = n * percent / 100;
    } else if (switch_ === 5) {
        percent_delta = 0.1;
        while (percent_delta % 1 !== 0) {
            n = P.randint(1, 600);
            percent = P.randint(0, 100);
            percent_delta = n * percent / 100;
        }
    // the following two are up to 600%
    } else if (switch_ === 6) {
        n = P.randint(1, 100);
        percent = P.randint(1, 60) * 10;
        percent_delta = n * percent / 100;
    } else {
        percent_delta = 0.1;
        percent = 100;
        while (percent_delta % 1 !== 0 || percent === 100) {
            n = P.randint(1, 600);
            percent = P.randint(0, 600);
            percent_delta = n * percent / 100;
        }
    }
    // end(the following two are up to 600%)

    let percent_delta_sign, crease;
    if (P.randint(0, 4) <= 3 && switch_ <= 5) {
        percent_delta_sign = -1;
        crease = "Decrease ";
    } else {
        percent_delta_sign = 1;
        crease = "Increase ";
    }

    let right_answer = n + percent_delta * percent_delta_sign;
    if (!(right_answer % 1)) {
        right_answer = P.int(right_answer);
    }
    right_answers = [right_answer];   // a number, as in the Python original
    input_message = "It was " + String(n) + "." + crease + String(percent) + "%. Now it equals ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.percent_change = percent_change;
})();
