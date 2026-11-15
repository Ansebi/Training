(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function complex_roots(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const primes_list = [2, 3, 5, 7, 11, 13, 17, 19, 23];
    let proper_condition = false;
    let prime, to_be_squarred, squarred, msg;
    while (proper_condition === false) {
        const prime_option_1 = P.choice(primes_list.slice(0, 3));
        const prime_option_2 = P.choice(primes_list);
        prime = P.choice([prime_option_1, prime_option_2]);
        to_be_squarred = P.randint(2, 12);
        squarred = to_be_squarred ** 2;
        msg = squarred * prime;
        if (prime === prime_option_1) {
            proper_condition = true;
        }
        if (msg < 200) {
            proper_condition = true;
        }
        if (msg > 360) {
            proper_condition = false;
        }
    }

    input_message = 'r2(' + String(msg) + ') = ';
    let right_answer = String(to_be_squarred);
    right_answer += 'r2(' + String(prime) + ')';
    right_answers = [right_answer];

    // prompt='type r2(x) of square root of x'

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.complex_roots = complex_roots;
})();
