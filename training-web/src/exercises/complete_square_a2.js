(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function complete_square_a2(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // (a+b)2=a2+2ab+b2

    const n1 = P.randint(1, 13);
    const n1_string = n1 !== 1 ? String(n1) : "";
    const n1_square_string = n1 !== 1 ? String(n1 ** 2) : "";
    const n2 = P.randint(1, 13);

    const the_noise_v1 = 10 * P.randint(-10, 10);
    const the_noise_v2 = P.randint(-20, 20);
    let the_noise = P.choice([the_noise_v1, the_noise_v2]);

    const the_sign = P.choice(['+', '-']);

    let b2 = n2 ** 2 + the_noise;
    if (b2 < 0) {
        b2 = String(b2);
    } else if (b2 === 0) {
        b2 = '';
    } else {
        b2 = '+' + String(b2);
    }

    if (the_noise < 0) {
        the_noise = String(the_noise);
    } else if (the_noise === 0) {
        the_noise = '';
    } else {
        the_noise = '+' + String(the_noise);
    }

    const right_answer = '(' + n1_string + 'x' + the_sign + String(n2) + ')2' + the_noise;
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     String(2 * n1 * n2) + 'x' + b2 + ' = ');
    prompt = 'HINT: answer in the form of (a+b)2+n';
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.complete_square_a2 = complete_square_a2;
})();
