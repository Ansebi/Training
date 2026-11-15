(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function complete_square_a3(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const the_multiplier = P.randint(2, 5);

    const n2 = P.randint(1, 13);

    const the_sign = P.choice(['+', '-']);

    const right_answer = String(the_multiplier) + '(x' + the_sign + String(n2) + ')2';

    input_message = (String(the_multiplier) + 'x2' +
                     the_sign +
                     String(the_multiplier * 2 * n2) + 'x' +
                     '+' + String((n2 ** 2) * the_multiplier) + ' = ');

    right_answers = [right_answer];
    prompt = 'represent as: a(x+b)2';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.complete_square_a3 = complete_square_a3;
})();
