(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function linear_equation_lvl_2(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // ax/d + b=c
    let a, b, c, d;
    let right_answer = 0.1;
    while (right_answer % 1 !== 0) {
        a = P.randint(1, 10) * P.choice([-1, 1]);
        b = P.int(P.round(P.triangular(-50, 50, 0), 0));
        c = b + P.randint(-13, 13);
        d = P.randint(1, 13) * P.choice([-1, 1]);
        right_answer = d * (c - b) / a;
    }
    right_answer = String(P.int(right_answer));

    let a_input_message, b_input_message;
    if (a === 1) {
        a_input_message = "";
    } else if (a === -1) {
        a_input_message = "-";
    } else {
        a_input_message = String(a);
    }

    if (b !== 0) {
        b_input_message = b > 0 ? "+" + String(b) : String(b);
    } else {
        b_input_message = "";
    }

    input_message = a_input_message + "x/" + String(d) + " " + b_input_message + "=" + String(c) + "\nx = ";
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.linear_equation_lvl_2 = linear_equation_lvl_2;
})();
