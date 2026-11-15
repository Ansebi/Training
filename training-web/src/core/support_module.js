(() => {
"use strict";

// Port of support_module.py (all but flatten, which no converted exercise uses).
// Helpers from window.TrainingPy are used lazily, inside the functions.

// generate proper multiples to form a number for further factorization
// Literal port: like the Python, it never returns for n == 0 (infinite loop).
function factorize(n) {
    const results = [];
    let divisor = 2;
    while (Math.abs(n) > 1) {
        if (n % divisor === 0) {
            results.push(divisor);
            n = n / divisor;
            divisor = 2;
        } else {
            divisor += 1;
        }
    }
    return results;
}

function lists_equal(a, b) {
    return a.length === b.length && a.every((x, i) => x === b[i]);
}

// NOTE: like the Python, this mutates the lists it is given
function crossout(a, b) {
    if (lists_equal(a, b)) {
        a = [1]; b = [1];
    } else {
        let a_count = 0;
        while (a_count >= 0 && a_count < a.length) {
            let switch_ = 0;
            let b_count = 0;
            while (b_count >= 0 && b_count < b.length) {
                if (b[b_count] === a[a_count]) {
                    b.splice(b_count, 1);
                    b_count = b.length + 1;
                    a.splice(a_count, 1);
                    switch_ = 1;
                } else {
                    b_count += 1;
                }
            }
            if (switch_ === 0) {
                a_count += 1;
            }
            if (!a.length) {
                a = [1];
            }
            if (!b.length) {
                b = [1];
            }
        }
    }
    let c = 1;
    for (const i of a) c = c * i;
    a = c;
    c = 1;
    for (const i of b) c = c * i;
    b = c;
    return [a, b];
}

function fraction_simplifier(numerator, denominator) {
    const [top, bottom] = crossout(factorize(numerator), factorize(denominator));
    if (bottom === 1) {
        return String(top);
    } else {
        return `${top}/${bottom}`;
    }
}

// 5 in the middle of the line turns into '+ 5'; -1.0 turns into '-1'
function num_to_str(n, in_middle = true, remove_one = false) {
    const P = window.TrainingPy;
    if (!(n % 1)) {
        n = P.int(n);
    }
    const s = P.numStr(n);
    let n_str;
    if (n < 0) {
        n_str = s;
    } else {
        n_str = in_middle ? `+ ${s}` : s;
    }
    if (remove_one) {
        if (Math.abs(n) === 1) {
            n_str = n_str.split("1").join("");
        }
    }
    return n_str;
}


// all (a, b, c, x1, x2) with integer roots, a in [-10, 9], b in [-13, 12], c in [-100, 99]
// Literal port, including a quirk: for a == 0 the Python division raises ZeroDivisionError,
// is swallowed by try/except, and x1 / x2 keep their values from an earlier iteration.
function quadratics_composer() {
    const P = window.TrainingPy;
    const total_set = [];
    let counter = 0;
    let x1, x2;
    for (let a = -10; a < 10; a++) {
        for (let b = -13; b < 13; b++) {
            for (let c = -100; c < 100; c++) {
                const D = b ** 2 - 4 * a * c;
                if (D >= 0) {
                    const r2D = Math.sqrt(D);
                    if (2 * a !== 0) x1 = (-b + r2D) / (2 * a);       // try / except: pass
                    if (x1 % 1 === 0) {
                        if (2 * a !== 0) x2 = (-b - r2D) / (2 * a);   // try / except: pass
                        if (x2 % 1 === 0) {
                            counter += 1;
                            total_set.push([a, b, c, P.int(x1), P.int(x2)]);
                        }
                    }
                }
            }
        }
    }
    return total_set;
}

// Converts fractions like 6.25000007 (4 zeros or above) to the normal form like 6.25. Takes and returns a string.
function re_based_decimal_fixer_zero(input_number_string) {
    const P = window.TrainingPy;
    let result = false;
    const z0 = /[1-9]+\.(000)+0*[1-9]*/.test(input_number_string);
    if (z0) {
        result = String(P.int(P.round(Number(input_number_string), 0)));   // str(round(float(s)))
    }

    if (!result) {
        for (let i = 1; i < input_number_string.length + 1; i++) {
            const str_i = input_number_string.slice(0, i);
            if (/\.[1-9]+(000)/.test(str_i)) {
                result = str_i.slice(0, -3);
                break;
            }
        }
    }

    if (!result) {
        for (let i = 1; i < input_number_string.length + 1; i++) {
            const str_i = input_number_string.slice(0, i);
            if (/\.[1-9]*0+[1-9]+0+/.test(str_i)) {
                result = str_i.slice(0, -1);
                break;
            }
        }
    }

    if (!result) {
        result = input_number_string;
    }

    return result;
}

// value: a string, or a JS number standing for a Python float.
// Returns a string (string_output = true). With string_output = false the raw value is returned
// (a number there means a Python int when it came out of the int() step).
function e_remover(value, string_output = true) {
    const P = window.TrainingPy;
    let kind = typeof value === "string" ? "str" : "float";
    if ((kind === "str" ? value : P.floatStr(value)).includes("e")) {
        value = P.fixed(Number(value), 16);
        kind = "str";
        let fixed = false;
        while (!fixed) {
            if (value[value.length - 1] === "0") {
                value = value.slice(0, -1);
            } else {
                fixed = true;
            }
        }
    }
    if (!(Number(value) % 1)) {
        value = P.int(Number(value));
        kind = "int";
    }
    if (string_output) {
        value = kind === "str" ? value : kind === "int" ? String(value) : P.floatStr(value);
    }
    return value;
}

// accepts strings like 0.369999999997654, returns adequate versions
function auto_round(number, ignore_zeros = true, string_output = true, restrict = false) {
    const P = window.TrainingPy;
    const MAX_REPS = 4;

    if (restrict) {
        const v = Number(number);
        if (!(1e-14 < v && v < 1e14)) {
            throw new Error("the value has to be between 10**-14 and 10**14");
        }
    }

    const number_string = typeof number === "string" ? number : P.floatStr(number);

    let prev_digit = "";
    let counter = 1;
    let round_pos = number_string.length;
    let round_pos_change = false;
    let hit_a_cluster = false;
    let point_pos = number_string.length;
    let round_pos_i;

    const zero_condition = ignore_zeros ? (x => x !== "0") : (x => true);

    for (let i = 0; i < number_string.length; i++) {
        const digit = number_string[i];
        if (digit === ".") {
            point_pos = i;
        }
        if (digit === prev_digit && zero_condition(digit)) {
            if (!hit_a_cluster) {
                hit_a_cluster = true;
                round_pos_i = i - 1;
            }
            counter += 1;
        } else {
            if (digit !== ".") {
                counter = 1;
                hit_a_cluster = false;
                prev_digit = digit;
            }
        }
        if (counter >= MAX_REPS) {
            round_pos = round_pos_i;
            round_pos_change = true;
        }
    }
    let result, result_is_float;
    if (round_pos_change) {
        result = P.round(Number(number), round_pos - point_pos);
        result_is_float = true;
    } else {
        result = number;
        result_is_float = typeof number !== "string";
    }

    if (P.round(Number(result), 0) === Number(result)) {
        result = P.round(Number(number), round_pos - point_pos);
        result_is_float = true;
    }

    if (string_output) {
        result = result_is_float ? P.floatStr(result) : String(result);
    }

    return result;
}

// ' .,-0123456789' are the numeric characters; everything from the first other char on is the variable part
function get_var_chars(nx) {
    const num_chars = " .,-0123456789";
    let var_region = false;
    let var_part = "";
    for (const ch of nx) {
        if (!num_chars.includes(ch)) {
            var_region = true;
        }
        if (var_region) {
            var_part += ch;
        }
    }
    return var_part;
}

// ['8', '-5x', 2] returns '8 -5x + 2'
function list_to_str(raw_list) {
    const processed_list = [];
    raw_list.forEach((i, n) => {
        const var_char = get_var_chars(String(i));
        const contains_variable = var_char ? true : false;
        if (contains_variable) {
            i = i.split(var_char).join("");
        }
        const text = String(i).trim();
        if (!/^[+-]?(\d+\.?\d*|\.\d+)([eE][+-]?\d+)?$/.test(text)) {      // float(i) would raise
            let warning = `Wrong data type of the element: ${i}.\n`;
            warning += "Must be a float or an integer, a numeric string at least.\n";
            warning += "Or something like '5x' or '-4a'. These are supported and are a reason to make this function.";
            console.log(warning);
            throw new TypeError("unsupported operand for %: 'str' and 'int'");   // what Python does next
        }
        i = Number(text);
        const in_middle = n ? true : false;
        i = num_to_str(i, in_middle, contains_variable) + var_char;
        processed_list.push(i);
    });
    return processed_list.join(" ");
}

// given the target 5 and n=2 it would propose e.g. [2, 3] which add up to 5
// spread controls the deviation of the generated addends
function generate_target_sum(target, n, spread) {
    const P = window.TrainingPy;
    if (n <= 0) {
        throw new Error("n must be a positive integer, or a zero to return an empty list");
    }
    // (np.random.randint(1, max(1, spread+1), n) * np.random.choice([1, -1], n) + target / n).astype(int)
    const magnitudes = Array.from({ length: n }, () => P.npRandint(1, Math.max(1, spread + 1)));
    const signs = Array.from({ length: n }, () => P.choice([1, -1]));
    const addends = magnitudes.map((m, k) => P.int(m * signs[k] + target / n));
    const delta = target - addends.reduce((x, y) => x + y, 0);
    for (let i = 0; i < Math.abs(delta); i++) {
        addends[i % n] += Math.floor(delta / Math.abs(delta));
    }
    return addends;
}

window.TrainingSupport = Object.assign(window.TrainingSupport || {},
    { factorize, crossout, fraction_simplifier, num_to_str, quadratics_composer,
      re_based_decimal_fixer_zero, e_remover, auto_round, get_var_chars, list_to_str, generate_target_sum });
})();
