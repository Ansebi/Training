(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function linear_equation(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // ax+b=c
    let a = P.randint(1, 9);
    const a_sign = P.randint(0, 1) > 0 ? 1 : -1;
    a = a * a_sign;

    let right_answer = P.randint(0, 11);
    const right_answer_sign = P.randint(0, 1) > 0 ? 1 : -1;
    right_answer = P.int(right_answer * right_answer_sign);

    const b = P.int(P.round(P.triangular(-50, 50, 0), 0));

    const c = a * right_answer + b;

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

    input_message = a_input_message + "x" + b_input_message + "=" + String(c) + "\nx = ";
    right_answers = [right_answer];   // a number, as in the Python original

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.linear_equation = linear_equation;
})();
