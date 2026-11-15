(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function complete_square_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const n1 = P.randint(1, 13);
    const n1_string = n1 !== 1 ? String(n1) : "";
    const n1_square_string = n1 !== 1 ? String(n1 ** 2) : "";
    const n2 = P.randint(1, 13);

    const the_sign = P.choice(['+', '-']);

    const right_answer = '(' + n1_string + 'x' + the_sign + String(n2) + ')2';
    input_message = (n1_square_string + 'x2' +
                     the_sign +
                     String(2 * n1 * n2) + 'x' +
                     '+' + String(n2 ** 2) + ' = ');

    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.complete_square_easy = complete_square_easy;
})();
