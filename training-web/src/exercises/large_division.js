(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function large_division(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // c = a * b
    let ok = false;
    let a, b;
    while (!ok) {
        const d = P.randint(1, difficulty + 1);
        const a1 = P.choice([1, 1, 1, 5, 10, 100, 101, 1001]);
        const a2 = P.randint(1, 101);
        const a3 = P.randint(1, 10);
        a = a1 * a2 * a3 * d;
        const b1 = P.randint(1, 100);
        const b2 = P.choice([1, 1, 1, 5, 10, 100, 101]);
        b = b1 * b2;
        if (500 < a && a < 10000) {
            if (90 < b && b < 1000) {
                ok = true;
            }
        }
    }
    const c = a * b;
    prompt = 'Divide the following, the answer is a whole number:';
    input_message = `${c} / ${b} = ... \n`;
    right_answers = [a];   // a number, as in the Python original

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.large_division = large_division;
})();
