(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function find_sum(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    input_message = "";
    let right_answer = 0;

    const n = [], n_quantity = [], input_message_raw = [];
    for (let i = 0; i < 3; i++) {
        n.push(P.randint(-50, 50));
        n_quantity.push(P.randint(0, 6));
        right_answer += n[i] * n_quantity[i];
        for (let counter = 0; counter < n_quantity[i]; counter++) {
            input_message_raw.push(n[i]);
        }
        P.shuffle(input_message_raw);
    }
    for (let counter = 0; counter < input_message_raw.length; counter++) {
        input_message += " " + String(input_message_raw[counter]) + " ";
    }
    input_message = "sum(" + input_message + ")= ";
    right_answers = [String(right_answer)];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.find_sum = find_sum;
})();
