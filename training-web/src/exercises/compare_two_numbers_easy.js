(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function compare_two_numbers_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const POW10_NEG = { "-4": 0.0001, "-3": 0.001, "-2": 0.01, "-1": 0.1 };

    function make_option(rand_low, rand_high, exp_low, exp_high) {
        const r = P.randint(rand_low, rand_high);
        const e = P.randint(exp_low, exp_high);
        if (e >= 0) {
            return { value: P.round(r * 10 ** e, 6), is_float: false };
        }
        return { value: P.round(r * POW10_NEG[String(e)], 6), is_float: true };
    }

    const to_str = o => o.is_float ? P.floatStr(o.value) : String(o.value);

    let option1 = make_option(-1000, 1000, -4, 4);
    let option2 = make_option(-100, 100, -4, 3);
    const n1 = P.choice([option1, option2]);

    option1 = make_option(-1000, 1000, -4, 4);
    option2 = make_option(-100, 100, -4, 3);
    const n2 = P.choice([option1, option2]);

    let right_answer;
    if (n1.value < n2.value) {
        right_answer = "<";
    } else if (n1.value > n2.value) {
        right_answer = ">";
    } else {
        right_answer = "=";
    }

    prompt = to_str(n1) + " ... " + to_str(n2);
    input_message = to_str(n1) + " ";
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.compare_two_numbers_easy = compare_two_numbers_easy;
})();