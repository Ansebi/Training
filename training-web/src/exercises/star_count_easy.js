(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function star_count_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const max_n = 9;
    const max_len = 20;
    let n1, n2, product;
    input_message = ' '.repeat(max_len + 1);
    while (input_message.length > max_len) {
        n1 = P.randint(1, max_n);
        if (n1 > 2) {
            n2 = P.randint(2, (max_n - n1 + 3));
        } else {
            n2 = P.randint(4, 9);
        }
        n2 = n2 === 0 ? 1 : n2;
        product = n1 * n2;
        if (product < 4) {
            n1 = P.randint(5, 7);
            n2 = P.randint(3, 5);
            product = n1 * n2;
        }
        input_message = ('*'.repeat(n1) + '\n').repeat(n2) + ' = ';
    }
    const right_answer = String(product);
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.star_count_easy = star_count_easy;
})();
