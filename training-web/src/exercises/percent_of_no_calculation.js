(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function percent_of_no_calculation(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    let n, percent;
    const switch_ = P.randint(1, 5);
    if (switch_ <= 4) {
        n = 10 * P.randint(20, 100);
        percent = P.randint(1, 20) * 5;
    } else if (switch_ === 5) {
        n = P.randint(1, 100);
        percent = P.randint(1, 60) * 10;
    } else if (switch_ === 6) {   // unreachable in the original too (switch is 1..5)
        n = P.randint(1, 600);
        percent = P.randint(0, 100);
    } else {                      // unreachable in the original too
        n = P.randint(1, 600);
        percent = P.randint(0, 600);
    }

    let coeff = percent / 100;
    if (coeff % 1 === 0) {
        coeff = P.int(coeff);
    }
    coeff = P.numStr(coeff);

    const right_answer = String(n) + "*" + coeff;
    right_answers = [right_answer];
    input_message = String(percent) + "% of " + String(n) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.percent_of_no_calculation = percent_of_no_calculation;
})();
