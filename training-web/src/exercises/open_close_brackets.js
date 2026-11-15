(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function open_close_brackets(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    /*
    forward: n(ax + by) = nax + nby
    backward: nax + nby = n(ax + by)
    */
    const S = window.TrainingSupport;
    const alphabet = 'abcdefghijkmnpqrstuvwxyz';
    const d = Math.abs(difficulty);
    const mode = P.choice(['forward', 'backward']);
    // np.random.choice(list, k, replace=False): k distinct items, in random order
    const choice_without_replacement = (arr, k) => {
        const rest = arr.slice();
        const picked = [];
        for (let j = 0; j < k; j++) picked.push(rest.splice(P.randint(0, rest.length - 1), 1)[0]);
        return picked;
    };
    const [x, y] = choice_without_replacement(Array.from(alphabet), 2);
    let a, b, n;
    if (mode === 'forward') {
        let okay = false;
        while (!okay) {
            // np.random.randint(1, 6 + d, 3) * np.random.choice([-1, 1], 3)
            const mags = Array.from({ length: 3 }, () => P.npRandint(1, 6 + d));
            const signs = Array.from({ length: 3 }, () => P.choice([-1, 1]));
            [a, b, n] = mags.map((v, k) => v * signs[k]);
            const conditions = [Math.abs(a) !== Math.abs(b), Math.abs(n) !== 1];
            okay = conditions.every(Boolean) ? true : false;
        }
    } else {
        const primes = [1, 2, 3, 5, 7, 11, 13, 17, 19, 23, 29, 31, 37];
        const picked = choice_without_replacement(primes.slice(0, Math.max(d, 6)), 2);
        const signs = Array.from({ length: 2 }, () => P.choice([-1, 1]));
        [a, b] = picked.map((v, k) => v * signs[k]);
        n = P.randint(2, 12) * P.choice([-1, 1]);
    }
    const na = S.num_to_str(n * a, false, true);
    const nb = S.num_to_str(n * b, true, true);
    a = S.num_to_str(a, false, true);
    b = S.num_to_str(b, true, true);
    const n_str = S.num_to_str(n, false, true);
    let state0 = `${n_str}(${a}${x} ${b}${y})`;
    let state1 = `${na}${x} ${nb}${y}`;
    prompt = 'Open the brackets. Example: 5(x + 2y) = 5x + 10y';
    if (mode === 'backward') {
        [state0, state1] = [state1, state0];
        const factor_sign = n < 0 ? 'NEGATIVE (-)' : 'POSITIVE (+)';
        prompt = 'Factorize the following. Example: 5x + 10y = 5(x + 2y)';
        prompt += `\nThe factor is ${factor_sign}`;
    }
    input_message = `${state0} = `;
    right_answers = [state1];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.open_close_brackets = open_close_brackets;
})();
