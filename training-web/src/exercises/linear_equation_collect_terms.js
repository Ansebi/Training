(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function linear_equation_collect_terms(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const d = difficulty;
    /*
    nax + nbx + ncx + nd + ne + nf = ngx + nhx + njx + nk + nm + np

    solved as
    n(a+b+c-g-h-j)x = n(k+m+p-d-e-f)
    (a+b+c-g-h-j)x = k+m+p-d-e-f
    or
    effective_coef * x = effective_const

    x = effective_const/effective_coef

    x is a pre-defined integer
    */
    const sum = arr => arr.reduce((p, q) => p + q, 0);
    // list(np.random.randint(1, 6 + d, n) * np.random.choice([-1, 1], n))
    const random_coefs = n => {
        const mags = Array.from({ length: n }, () => P.npRandint(1, 6 + d));
        const signs = Array.from({ length: n }, () => P.choice([-1, 1]));
        return mags.map((v, k) => v * signs[k]);
    };

    const n_coefs = P.randint(1, 3 + d);
    const n_coefs_left = P.randint(0, n_coefs);
    const n_coefs_right = n_coefs - n_coefs_left;

    let okay = false;
    let left_coefs, right_coefs;
    while (!okay) {
        left_coefs = random_coefs(n_coefs_left);
        right_coefs = random_coefs(n_coefs_right);
        if (sum(left_coefs) !== sum(right_coefs)) {
            okay = true;
        }
    }
    const x = P.randint(-(7 + d), 7 + d);
    const effective_coef = sum(left_coefs) - sum(right_coefs);
    const effective_const = x * effective_coef;
    let [sum_left_cts, sum_right_cts] = S.generate_target_sum(effective_const, 2, 6 + d ** 2);
    sum_left_cts = P.int(sum_left_cts * -1);
    const left_cts = S.generate_target_sum(sum_left_cts, P.randint(1, 2 + d), 5 + d ** 2);
    const right_cts = S.generate_target_sum(sum_right_cts, P.randint(1, 2 + d), 5 + d ** 2);
    const left_xs = left_coefs.map(i => `${i}x`);
    const right_xs = right_coefs.map(i => `${i}x`);
    let left = [...left_xs, ...left_cts].filter(i => i);
    let right = [...right_xs, ...right_cts].filter(i => i);
    P.shuffle(left);
    P.shuffle(right);
    if (!left.length) {
        left = [0];
    }
    if (!right.length) {
        right = [0];
    }
    left = S.list_to_str(left);
    right = S.list_to_str(right);
    input_message = `${left} = ${right}\nx = `;
    right_answers = [x];   // a number, as in the Python original
    prompt = 'Collect the terms and find x.';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.linear_equation_collect_terms = linear_equation_collect_terms;
})();
