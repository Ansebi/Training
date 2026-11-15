(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function test(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const right_answer = "test";
    right_answers = [right_answer];
    input_message = "test: ";

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.test = test;
})();
