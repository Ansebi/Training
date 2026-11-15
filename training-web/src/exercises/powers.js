(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function powers(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // constants:
    const low = 0, high = 15, mode = 2, how_narrow_is_option_2 = 3, option_2_probability = 70;

    const option_1 = Math.trunc(P.round(P.triangular(low, high, mode), 0));

    const option_2 = Math.trunc(P.round(
        P.triangular(
            mode - (mode - low) / how_narrow_is_option_2,
            mode + (high - mode) / how_narrow_is_option_2,
            mode),
        0));

    let n, m;
    if (P.randint(1, 100) > option_2_probability) {
        n = option_1;
    } else {
        n = option_2;
    }
    // adjusting the power according to the base, excluding 0**0
    if (n !== 0) {
        m = n < 8 ? P.randint(0, 9 - n) : P.randint(0, 2);
    } else {
        m = n < 8 ? P.randint(1, 9 - n) : P.randint(1, 2);
    }
    // adjusting the power according to the base, excluding 0**0 end
    const right_answer = String(n ** m);
    right_answers = [right_answer];
    input_message = String(String(n) + " to the power of " + String(m) + " = ");

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.powers = powers;
})();
