// MATHS

function rand(a,b) {
    return Math.floor(Math.random()*(b-a+1))+a;
}

function gcd(a,b) {
    while(b)[a,b]=[b,a%b];
    return Math.abs(a);
}

function makeQuestion() {
    const exerciseFunction = window.TrainingExercises && window.TrainingExercises[exerciseId];
    if (!exerciseFunction) {
        throw new Error(`Exercise module not found: ${exerciseId}`);
    }
    const result = exerciseFunction(difficulty);
    return {
        answers: [].concat(result.right_answers).map(String),
        text: result.input_message
    };
}
