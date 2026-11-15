(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function division_mixed_fractions(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;

    // composing appropriate numbers
    const divident = P.choice(
        [P.randint(80, 160),
         P.randint(80, 480),
         P.randint(80, 800)]
    );
    const divisor = Math.floor(divident / P.randint(1, 10));

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

window.TrainingExercises.division_mixed_fractions = division_mixed_fractions;
})();
