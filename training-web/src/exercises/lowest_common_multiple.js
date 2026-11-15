(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function lowest_common_multiple(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const primes = [2, 3, 5, 7, 11, 13];
    let okay = false;
    let hcf, sum_powers;
    while (!okay) {
        hcf = 1;
        sum_powers = 0;
        for (const i of primes) {
            let power = P.choice([0, 1]);
            if (power) {
                const from_ = 0;
                let to_;
                if (i === 2) {
                    to_ = 4 + difficulty;
                } else if (i === 3) {
                    to_ = 5;
                } else {
                    to_ = 1;
                }
                power = P.randint(from_, to_);
            }
            if (sum_powers >= 4 + difficulty) {
                break;
            }
            hcf *= i ** power;
            sum_powers += power;
        }
        if (2 + difficulty <= sum_powers && sum_powers <= 4 + difficulty) {
            okay = true;
        }
    }

    okay = false;

    function generate_ab_parts() {
        const small_primes = primes.slice(0, -2);
        const random_bools = () => Array.from({ length: 4 }, () => P.randint(0, 1) === 1);
        let a_scheme = random_bools();
        a_scheme[0] = true;
        P.shuffle(a_scheme);
        let b_scheme = a_scheme.map(x => !x);
        let mask = random_bools();
        a_scheme = a_scheme.map((x, k) => x && mask[k]);
        mask = random_bools();
        b_scheme = b_scheme.map((x, k) => x && mask[k]);
        // primes[:-2] ** np.random.randint(1, 2 + difficulty, 4), then *= scheme, zeros -> 1
        const a_difference = small_primes.map((p, k) => a_scheme[k] ? p ** P.npRandint(1, 2 + difficulty) : 1);
        const b_difference = small_primes.map((p, k) => b_scheme[k] ? p ** P.npRandint(1, 2 + difficulty) : 1);
        const a = a_difference.reduce((x, y) => x * y, 1);
        const b = b_difference.reduce((x, y) => x * y, 1);
        return [a, b];
    }

    function generate_ab_differences(difficulty) {
        return generate_ab_parts();
    }
    let [a, b] = generate_ab_differences(difficulty);
    let conditions = [
        a === b,
        !(a % b),
        !(b % a)
    ];
    if (conditions.some(Boolean)) {
        [a, b] = generate_ab_differences(difficulty);
    }
    /* do twice: */
    conditions = [
        a === b,
        !(a % b),
        !(b % a)
    ];
    if (conditions.some(Boolean)) {
        [a, b] = generate_ab_differences(difficulty);
    }
    const lcm = hcf * a * b;
    right_answers = [lcm];   // NOTE: a number, not a string (as in the Python original)
    input_message = `Find LCM for ${a * hcf} and ${b * hcf}:\n`;

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.lowest_common_multiple = lowest_common_multiple;
})();
