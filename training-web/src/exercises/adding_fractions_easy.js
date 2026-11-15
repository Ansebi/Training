(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function adding_fractions_easy(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const threshold = (difficulty + 1) * 10;
    let okay = false;
    const mode = P.choice(['+', '+', '*', ':']);
    let n11, n12, n21, n22, numerator, denominator, top, bottom, right_answer;
    if (mode === '+') {
        while (!okay) {
            n11 = P.randint(1, 13);
            n12 = P.randint(1, 13);
            n21 = P.randint(1, 13);
            n22 = P.randint(1, 13);

            numerator = n11 * n22 + n21 * n12;
            denominator = n12 * n22;
            [top, bottom] = S.crossout(S.factorize(numerator), S.factorize(denominator));
            if (top + bottom < threshold) {
                okay = true;
                right_answer = S.fraction_simplifier(numerator, denominator);
            }
        }
        input_message = `${n11}/${n12} + ${n21}/${n22} = `;
        right_answers = [right_answer];
    } else if (mode === '*') {
        while (!okay) {
            n11 = P.randint(1, 13);
            n12 = P.randint(1, 13);
            n21 = P.randint(1, 13);
            n22 = P.randint(1, 13);

            numerator = n11 * n21;
            denominator = n12 * n22;
            [top, bottom] = S.crossout(S.factorize(numerator), S.factorize(denominator));
            if (top + bottom < threshold) {
                okay = true;
                right_answer = S.fraction_simplifier(numerator, denominator);
            }
        }
        input_message = `${n11}/${n12} * ${n21}/${n22} = `;
        right_answers = [right_answer];
    } else if (mode === ':') {
        while (!okay) {
            n11 = P.randint(1, 13);
            n12 = P.randint(1, 13);
            n21 = P.randint(1, 13);
            n22 = P.randint(1, 13);

            numerator = n11 * n22;
            denominator = n12 * n21;
            [top, bottom] = S.crossout(S.factorize(numerator), S.factorize(denominator));
            if (top + bottom < threshold) {
                okay = true;
                right_answer = S.fraction_simplifier(numerator, denominator);
            }
        }
        input_message = `${n11}/${n12} : ${n21}/${n22} = `;
        right_answers = [right_answer];
    } else {
        // (the original has an unreachable subtraction branch after this raise)
        throw new Error('wrong mode');
    }

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.adding_fractions_easy = adding_fractions_easy;
})();
