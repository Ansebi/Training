(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function estimate(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const total_n = P.randint(3, 8);
    const max_species = 4;
    const bottom = 100;
    const ceiling = 800;
    const min_repeat = 1;
    const max_repeat = 5;

    const g = { items_remaining: total_n, question: '', estimate: 0 };   // "it's a global costyl"

    function item_n(bottom, ceiling, max_repeat, i) {
        const item_i = P.randint(bottom, ceiling);
        let n_item_i;
        if (g.items_remaining > 0) {
            n_item_i = P.randint(min_repeat, g.items_remaining);
            g.items_remaining -= n_item_i;
        } else {
            n_item_i = 0;
        }

        g.question += (String(item_i) + '   ').repeat(n_item_i);
        const the_order = 10 ** (String(item_i).length - 1);
        const item_i_estimate = P.int(P.round(item_i / the_order, 0)) * the_order;
        g.estimate += item_i_estimate * n_item_i;
    }

    for (let i = 1; i < max_species + 1; i++) {
        item_n(bottom, ceiling, max_repeat, i);
    }

    input_message = g.question + '\n'.repeat(2);
    const right_answer = String(g.estimate);
    right_answers = [right_answer];
    prompt = 'Estimate the sum, 1 s.f. each:';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.estimate = estimate;
})();
