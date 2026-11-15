(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function simultaneous_equations_3(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    /*
    ax + by = n1
    cy + dz = n2
    ez + fx = n3
    */
    const S = window.TrainingSupport;

    // np.random.randint(1, 11, 9) * np.random.choice([-1, 1], 9)
    const magnitudes = Array.from({ length: 9 }, () => P.npRandint(1, 11));
    const signs = Array.from({ length: 9 }, () => P.choice([-1, 1]));
    const [a, b, c, d, e, f, x, y, z] = magnitudes.map((v, k) => v * signs[k]);

    const n1 = a * x + b * y;
    const n2 = c * y + d * z;
    const n3 = e * z + f * x;

    const line1 = `${S.num_to_str(a, false, true)}x ${S.num_to_str(b, true, true)}y = ${n1}`;
    const line2 = `${S.num_to_str(c, false, true)}y ${S.num_to_str(d, true, true)}z = ${n2}`;
    const line3 = `${S.num_to_str(e, false, true)}z ${S.num_to_str(f, true, true)}x = ${n3}`;

    input_message = [line1, line2, line3].join("\n") + "\n";
    prompt = "Find x y z. Response Example: 5 -5 10";
    right_answers = [`${x} ${y} ${z}`, `${x}, ${y}, ${z}`, ` ${x} ${y} ${z}`, ` ${x} ${y} ${z} `];

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.simultaneous_equations_3 = simultaneous_equations_3;
})();
