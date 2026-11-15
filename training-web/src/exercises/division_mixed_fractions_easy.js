(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function division_mixed_fractions_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;

    // composing apropriate numbers
    const n1 = P.choice([1, P.choice([2, 3, 5])]);
    let n2 = P.choice([1, 10, P.choice([2, 3, 5])]);
    let n3 = P.choice([1, 1, 1, P.choice([2, 3, 5, 7, 11])]);
    let n4 = P.choice([2, 3, 5, 7, 11, 13]);
    const divident = n1 * n2 * n3 * n4;

    n2 = P.choice([1, P.choice([2, 3, 5])]);
    n3 = P.choice([1, 1, P.choice([2, 3, 5, 7, 11])]);
    n4 = P.choice([2, 3, 5, 7, 11, 13]);
    const divisor = n2 * n3 * n4;

    const [top, bottom] = S.crossout(S.factorize(divident), S.factorize(divisor));
    const fraction_reduced = S.fraction_simplifier(top, bottom);

    // converting fraction to a mixed number
    let right_answer;
    if (top < bottom || bottom === 1) {
        right_answer = fraction_reduced;
    } else {
        const whole = Math.floor(top / bottom);
        const fraction_top = top % bottom;
        right_answer = `${whole} ${fraction_top}/${bottom}`;
    }
    // end converting fraction to a mixed number
    input_message = `${divident}/${divisor} = `;
    right_answers = [right_answer];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.division_mixed_fractions_easy = division_mixed_fractions_easy;
})();
