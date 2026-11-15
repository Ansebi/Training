(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function factorizing_square_of_sum(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const alphabet_small = ['a', 'b', 'c', 'd', 'e', 'f', 'g',
                            'h', 'i', 'j', 'k', 'l', 'm', 'n',
                            'o', 'q', 'r', 's', 't', 'u', 'v',
                            'w', 'x', 'y', 'z'];
    let switch_ = 'NOT OKAY';

    const n1 = P.randint(1, 13);
    const n1_string = n1 !== 1 ? String(n1) : "";
    const n1_square_string = n1 !== 1 ? String(n1 ** 2) : "";
    const n2 = P.randint(1, 13);
    const n2_string = n2 !== 1 ? String(n2) : "";
    const n2_square_string = n2 !== 1 ? String(n2 ** 2) : "";

    const the_sign = P.choice(['+', '-']);

    // list.pop(index)
    const pop = (arr, idx) => arr.splice(idx, 1)[0];

    let letter1, letter1_power, letter2, letter2_power;
    while (switch_ === 'NOT OKAY') {
        letter1 = P.choice([pop(alphabet_small, P.randint(0, alphabet_small.length - 1)), ""]);
        letter1_power = letter1 !== "" ? '2' : "";
        letter2 = P.choice([pop(alphabet_small, P.randint(0, alphabet_small.length - 1)), ""]);
        letter2_power = letter2 !== "" ? '2' : "";
        switch_ = (letter1 !== letter2 && letter1 !== n1_string && letter2 !== n2_string) ? 'OKAY, GO' : 'NOT OKAY';
    }

    const right_answer = '(' + n1_string + letter1 + the_sign + n2_string + letter2 + ')2';
    input_message = (n1_square_string + letter1 + letter1_power +
                     the_sign +
                     String(2 * n1 * n2) + letter1 + letter2 +
                     '+' + n2_square_string + letter2 + letter2_power + ' = ');

    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.factorizing_square_of_sum = factorizing_square_of_sum;
})();
