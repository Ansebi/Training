(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function multiplication_table(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    // n*m
    const n = P.randint(1, 11);
    const m = P.randint(1, 11);
    const right_answer = n * m;
    right_answers = [String(right_answer)];
    input_message = String(n) + " * " + String(m) + " = ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.multiplication_table = multiplication_table;
})();
