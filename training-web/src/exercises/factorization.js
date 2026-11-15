(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function factorization(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const factorize = window.TrainingSupport.factorize;   // provisional, see core/support_module.js

    const prime_numbers_up_to_100 = [
        2, 3, 5, 7, 11, 13, 17, 19, 23,
        29, 31, 37, 41, 43, 47, 53, 59,
        61, 67, 71, 73, 79, 83, 89, 97
    ];

    const n_1 = P.choice(prime_numbers_up_to_100.slice(0, 3));
    let n_2, n_3, n_4, n_5, n_6;
    if (P.randint(0, 1)) {
        n_2 = P.choice(prime_numbers_up_to_100.slice(0, 3));
    } else {
        n_2 = 1;
    }
    if (P.randint(0, 1)) {
        n_3 = P.choice(prime_numbers_up_to_100.slice(0, 3));
    } else {
        n_3 = 1;
    }
    if (P.randint(0, 1)) {
        n_4 = P.choice(prime_numbers_up_to_100.slice(0, 3));
    } else {
        n_4 = 1;
    }
    if (P.randint(0, 1)) {
        n_5 = P.choice(prime_numbers_up_to_100.slice(0, 4));
    } else {
        n_5 = 1;
    }
    if (P.randint(0, 1)) {
        n_6 = P.choice(prime_numbers_up_to_100.slice(0, 6));
    } else {
        n_6 = 1;
    }

    const n = n_1 * n_2 * n_3 * n_4 * n_5 * n_6;

    const prime_multiples_list = factorize(n);
    const right_answer = prime_multiples_list.map(i => String(i)).join("*");
    right_answers = [right_answer];
    input_message = `${n} = `;
    prompt = "Factorize a number (reveal ascending prime multiples).";
    prompt += "\n";
    prompt += "Example: 60 = 2*2*3*5";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.factorization = factorization;
})();
