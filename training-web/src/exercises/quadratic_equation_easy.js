(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function quadratic_equation_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const quadratics_composer = S.quadratics_composer;
    const total_set = quadratics_composer();
    const the_particular_set = P.choice(total_set);

    let a = the_particular_set[0];
    let b = the_particular_set[1];
    let c = the_particular_set[2];
    const x1 = the_particular_set[3];
    const x2 = the_particular_set[4];

    const right_answer1 = String(x1) + ',' + String(x2);
    const right_answer2 = String(x2) + ',' + String(x1);
    right_answers = [right_answer1, right_answer2];
    if (x1 === x2) {
        right_answers = [right_answer1, String(x1)];
    }

    a = String(a);
    if (a === '1') {
        a = '';
    }
    if (a === '-1') {
        a = '-';
    }
    const ax2 = a + 'x2';

    let b_sign;
    if (b > 0) {
        b_sign = '+';
    } else {
        b_sign = '';
    }
    b = String(b);
    let bx = b + 'x';
    if (b === '0') {
        bx = '';
    }
    if (b === '1') {
        bx = 'x';
    }
    if (b === '-1') {
        bx = '-x';
    }
    bx = b_sign + bx;

    let c_sign;
    if (c > 0) {
        c_sign = '+';
    } else {
        c_sign = '';
    }
    c = String(c);
    if (c === '0') {
        c = '';
    }
    c = c_sign + c;

    input_message = ax2 + bx + c + '=0\n';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.quadratic_equation_easy = quadratic_equation_easy;
})();
