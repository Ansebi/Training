(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function complete_square_a5(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const the_multiplier = P.randint(2, 5);

    const n2 = P.randint(1, 13);

    const the_noise_v1 = P.randint(-20, 20);
    const the_noise_v2 = 10 * P.randint(-5, 5);
    const the_noise = P.choice([the_noise_v1, the_noise_v2]);
    let the_noise_string;
    if (the_noise > 0) {
        the_noise_string = '+' + String(the_noise);
    } else if (the_noise === 0) {
        the_noise_string = '';
    } else {
        the_noise_string = String(the_noise);
    }

    const the_sign = P.choice(['+', '-']);

    const right_answer = String(the_multiplier) + '(x' + the_sign + String(n2) + ')2' + the_noise_string;

    input_message = (String(the_multiplier) + 'x2' +
                     the_sign +
                     String(the_multiplier * 2 * n2) + 'x' +
                     '+' + String((n2 ** 2) * the_multiplier + the_noise) + ' = ');

    right_answers = [right_answer];

    prompt = 'represent as: a(x+b)2+c';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.complete_square_a5 = complete_square_a5;
})();
