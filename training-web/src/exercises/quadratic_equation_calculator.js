(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function quadratic_equation_calculator(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const a1 = P.randint(-10, -1);
    const a2 = P.randint(1, 10);
    let a = P.choice([a1, a2]);
    const b1 = P.randint(-10, -1);
    const b2 = P.randint(1, 10);
    let b = P.choice([b1, b2]);
    const c1 = P.randint(-10, -1);
    const c2 = P.randint(1, 10);
    let c = P.choice([c1, c2]);
    const D = b ** 2 - 4 * a * c;
    if (D < 0) {
        right_answers = [''];
    } else if (D === 0) {
        let x = -b / (2 * a);
        x = P.round(x, 1);
        if (x % 1 === 0) {
            x = P.int(x);
        }
        right_answers = [P.numStr(x)];
    } else {
        let x1 = (-b + Math.sqrt(D)) / (2 * a);
        x1 = P.round(x1, 1);
        if (x1 % 1 === 0) {
            x1 = P.int(x1);
        }
        let x2 = (-b - Math.sqrt(D)) / (2 * a);
        x2 = P.round(x2, 1);
        if (x2 % 1 === 0) {
            x2 = P.int(x2);
        }
        const right_answer1 = P.numStr(x1) + ',' + P.numStr(x2);
        const right_answer2 = P.numStr(x2) + ',' + P.numStr(x1);
        right_answers = [right_answer1, right_answer2];
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

    prompt = 'give your answers rounded to 1d.p.';

    // input_message=prompt
    // input_message+='\n'
    input_message = ax2 + bx + c + '=0\n';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.quadratic_equation_calculator = quadratic_equation_calculator;
})();
