(() => {
"use strict";

window.TrainingExercises = window.TrainingExercises || {};

function convert_units(difficulty) {
    const P = window.TrainingPy;
    let right_answers, input_message, prompt;

    const S = window.TrainingSupport;
    const DELTA_RANGE = 10;  // a power of 10 the range between the units to convert
    let MAX_ZEROS = 7;
    const MAX_ZEROS_EASY = 5;
    const MAX_SIGNIFICANT_FIGURES = 100;

    // Python mixes ints and floats in these lists; the type decides how str(n * k) prints
    const I = v => ({ v, is_int: true });
    const F = v => ({ v, is_int: false });
    let magnitudes = [F(0.000001), F(0.000005),
                      F(0.00001), F(0.00005),
                      F(0.0005), F(0.005), F(0.01), F(0.5),
                      F(0.0001), F(0.001), F(0.01), F(0.1),
                      I(1), I(5), I(10), I(50), I(100), I(500),
                      I(1000), I(5000), I(10000), I(50000)];
    const magnitudes_EASY = [F(0.005), F(0.01), F(0.5),
                             F(0.001), F(0.01), F(0.1),
                             I(1), I(5), I(10), I(50), I(100), I(500),
                             I(1000), I(5000)];

    let prefixes_dict = { 'p': -12, 'n': -9, 'mc': -6, 'm': -3,
                          'c': -2, 'd': -1, 'u': 0,
                          'k': 3, 'M': 6, 'G': 9, 'T': 12 };
    const prefixes_dict_RUS = { 'м': -3, 'c': -2, 'д': -1, 'u': 0, 'к': 3 };

    let units = ['g', 'm', 's', 'N', 'J', 'W', 'A', 'Hz'];
    const units_RUS = ['м'];

    if (!difficulty) {
        units = units_RUS;
        prefixes_dict = prefixes_dict_RUS;
        magnitudes = magnitudes_EASY;
        MAX_ZEROS = MAX_ZEROS_EASY;
    }

    const prefixes = Object.keys(prefixes_dict);
    prefixes.splice(prefixes.indexOf('u'), 1);

    const unit = P.choice(units);

    const n = P.randint(1, MAX_SIGNIFICANT_FIGURES);
    const k = P.choice(magnitudes);

    let value = k.is_int ? String(n * k.v) : P.floatStr(n * k.v);   // str(n * k)
    const e_remover = S.e_remover;
    value = e_remover(value);

    const fixer = S.re_based_decimal_fixer_zero;
    const auto_round = S.auto_round;
    value = e_remover(auto_round(fixer(value)));

    let okay = false;
    let prefix_1, prefix_2, right_answer;
    while (!okay) {
        prefix_1 = P.choice(prefixes);
        prefix_2 = P.choice(prefixes);
        if (prefix_2 !== prefix_1) {
            const delta = prefixes_dict[prefix_1] - prefixes_dict[prefix_2];
            if (Math.abs(delta) < DELTA_RANGE) {
                // 10 ** delta: int for delta >= 0, float for delta < 0
                const power_of_ten = delta >= 0 ? 10 ** delta : Number("1e" + delta);
                right_answer = Number(value) * power_of_ten;   // a float
                if (!e_remover(right_answer).includes('0'.repeat(MAX_ZEROS))) {
                    okay = true;
                }
            }
        }
    }

    right_answer =
        e_remover(
            fixer(
                e_remover(
                    auto_round(
                        e_remover(
                            right_answer
                        )))));

    right_answers = [right_answer];
    if (prefix_1 === 'u') {
        prefix_1 = '';
    }
    if (prefix_2 === 'u') {
        prefix_2 = '';
    }

    prompt = 'Convert the following values to the new units:';
    input_message = String(value) + ' ' + prefix_1 + unit + ' = ... ' + prefix_2 + unit + '\n';

    return { right_answers, input_message, prompt };
}

window.TrainingExercises.convert_units = convert_units;
})();
