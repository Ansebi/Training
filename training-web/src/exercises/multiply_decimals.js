(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function multiply_decimals(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const n_sign = P.randint(0, 1) === 1 ? -1 : 1;

    // np.random.randint(0, 9, size) -> digits 0..8; int("".join(...))
    // size < 0 or size == 0 raises in Python (numpy ValueError / int("") ValueError)
    function random_digits_to_int(size) {
        if (size < 0) throw new Error("negative dimensions are not allowed");
        let s = "";
        for (let i = 0; i < size; i++) s += String(P.randint(0, 8));
        if (s === "") throw new Error("invalid literal for int() with base 10: \x27\x27");
        return parseInt(s, 10);
    }
    // 10 ** randint(-3, -1) in Python is a float
    const POW10_NEG = { "-3": 0.001, "-2": 0.01, "-1": 0.1 };

    const whole_part_n = random_digits_to_int(difficulty + P.choice([0, -1]));
    const whole_part_m = random_digits_to_int(difficulty + P.choice([0, -1]));

    const n = P.round(whole_part_n * POW10_NEG[String(P.randint(-3, -1))], 4);
    const m = P.round(whole_part_m * POW10_NEG[String(P.randint(-3, -1))], 4);

    let right_answer = P.round(n_sign * n * m, 4);
    let is_int = false;
    if (!(right_answer % 1)) {
        right_answer = Math.trunc(right_answer);
        is_int = true;
    }
    if (!right_answer && n_sign < 0) {
        right_answer = 0;
        is_int = true;
    }
    right_answers = [is_int ? String(right_answer) : P.floatStr(right_answer)];
    input_message = P.floatStr(n * n_sign) + " * " + P.floatStr(m) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.multiply_decimals = multiply_decimals;
})();
