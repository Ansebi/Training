(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function value_function_quadratic(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const x_v1 = P.randint(-9, 9);
    const x_v2 = P.randint(-2, 0);
    const x_v3 = P.randint(-5, -1);
    const x_v4 = P.randint(-3, -1);
    const x = P.choice([x_v1, x_v2, x_v3, x_v4]);
    const a1 = P.randint(-10, -1);
    const a2 = P.randint(1, 10);
    let a = P.choice([a1, a2]);
    const b1 = P.randint(-10, -1);
    const b2 = P.randint(1, 10);
    let b = P.choice([b1, b2]);
    const c1 = P.randint(-10, -1);
    const c2 = P.randint(1, 10);
    let c = P.choice([c1, c2]);
    const fx = a * (x ** 2) + b * x + c;
    right_answers = [String(fx)];

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

    prompt = 'find the value of the function:';

    // input_message=prompt
    // input_message+='\n'
    input_message = 'f(x)=' + ax2 + bx + c;
    input_message += '\n';
    input_message += 'f(' + String(x) + ')=';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.value_function_quadratic = value_function_quadratic;
})();
