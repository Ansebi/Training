(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function factoring_quadratics(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const quadratics_composer = S.quadratics_composer;
    let x1 = 0;
    let x2 = 0;
    let a = 1, b, c;
    while (x1 === 0 || x2 === 0 || a === 1) {
        const total_set = quadratics_composer();
        const the_particular_set = P.choice(total_set);

        a = the_particular_set[0];
        b = the_particular_set[1];
        c = the_particular_set[2];
        x1 = the_particular_set[3];
        x2 = the_particular_set[4];
    }

    x1 = -x1;  // (x-x1) requires the opposite sign
    x2 = -x2;  // (x-x2) requires the opposite sign
    let str_x1, str_x2;
    if (x1 < 0) {
        str_x1 = String(x1);
    } else {
        str_x1 = '+' + String(x1);
    }
    if (x2 < 0) {
        str_x2 = String(x2);
    } else {
        str_x2 = '+' + String(x2);
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

    const right_answer1 = a + '(x' + str_x1 + ')(x' + str_x2 + ')';
    const right_answer2 = a + '(x' + str_x2 + ')(x' + str_x1 + ')';
    right_answers = [right_answer1, right_answer2];
    if (x1 === x2) {
        right_answers.push(a + '(x' + str_x1 + ')2');
    }

    input_message = ax2 + bx + c + '=';
    prompt = 'HINT: a(x-x1)(x-x2)';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.factoring_quadratics = factoring_quadratics;
})();
