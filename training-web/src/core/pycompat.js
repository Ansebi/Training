(() => {
"use strict";

// Python-compatible helpers so converted exercises keep Python's exact behaviour.
// Exercises must call these lazily (inside the exercise function), via window.TrainingPy.

// random.randint(a, b): inclusive on both ends
function randint(a, b) {
    if (a > b) throw new Error("empty range for randint(" + a + ", " + b + ")");   // Python raises ValueError
    return Math.floor(Math.random() * (b - a + 1)) + a;
}

// random.choice(list)
function choice(arr) {
    return arr[Math.floor(Math.random() * arr.length)];
}

// random.shuffle(list): in place, same algorithm as CPython
function shuffle(arr) {
    for (let i = arr.length - 1; i > 0; i--) {
        const j = Math.floor(Math.random() * (i + 1));
        const tmp = arr[i]; arr[i] = arr[j]; arr[j] = tmp;
    }
}

// np.random.randint(low, high): high is EXCLUSIVE; raises if low >= high (like numpy)
function npRandint(low, high) {
    if (low >= high) throw new Error("low >= high");
    return randint(low, high - 1);
}

// random.triangular(low, high, mode): same formula as CPython
function triangular(low, high, mode) {
    let u = Math.random();
    if (high === low) return low;                    // CPython: ZeroDivisionError -> return low
    let c = (mode - low) / (high - low);
    if (u > c) {
        u = 1.0 - u;
        c = 1.0 - c;
        const t = low; low = high; high = t;
    }
    return low + (high - low) * Math.sqrt(u * c);
}

// int(x): truncation toward zero; never returns -0 (Python ints have no negative zero)
function int(x) {
    return Math.trunc(x) + 0;
}

// str(x) where Python holds an int when x is integer-valued and a float otherwise
function numStr(x) {
    return Number.isInteger(x) ? String(x) : floatStr(x);
}

// "{:.{nd}f}".format(x) for nd >= 0: exact-value rounding, ties to even
function fixed(x, nd) {
    if (!Number.isFinite(x) || Math.abs(x) >= 1e21 || nd > 99) return x.toFixed(Math.min(nd, 100));
    if (Number.isInteger(x * Math.pow(2, nd + 1))) {
        // x is exactly representable with nd+1 decimals, so toFixed(nd+1) is exact
        const s = x.toFixed(nd + 1);
        if (s.endsWith("5")) {                       // exact tie -> round half to even
            const neg = s[0] === "-";
            const digits = s.replace("-", "").replace(".", "").slice(0, -1);
            let q = BigInt(digits);
            if (q % 2n === 1n) q += 1n;
            const t = q.toString().padStart(nd + 1, "0");
            const res = nd > 0 ? t.slice(0, -nd) + "." + t.slice(-nd) : t;
            return (neg ? "-" : "") + res;
        }
    }
    return x.toFixed(nd);                            // non-tie: correctly rounded
}

// round(x, ndigits) for float x (ndigits may be negative): exact-value rounding, ties to even
// (Math.round rounds ties up and works on x * 10^n, so it differs from Python)
function round(x, nd = 0) {
    if (!Number.isFinite(x) || x === 0) return x;    // keeps -0
    if (nd >= 0) {
        if (nd > 99 || Math.abs(x) >= 1e21) return x;
        return Number(fixed(x, nd));
    }
    // negative ndigits: round to a multiple of 10^-nd
    const neg = x < 0, ax = Math.abs(x);
    const whole = BigInt(Math.floor(ax)), frac = ax - Math.floor(ax);
    const p = 10n ** BigInt(-nd);
    let q = whole / p;
    const twice = 2n * (whole % p);
    if (twice > p || (twice === p && (frac > 0 || q % 2n === 1n))) q += 1n;
    return (neg ? -1 : 1) * Number(q * p);
}

// str(x) for a Python float (repr): "3.0", "-0.0", "1e-05", ...
function floatStr(x) {
    if (Number.isNaN(x)) return "nan";
    if (!Number.isFinite(x)) return x > 0 ? "inf" : "-inf";
    if (Object.is(x, -0)) return "-0.0";
    if (x === 0) return "0.0";
    const [mant, expStr] = x.toExponential().split("e");
    const e = parseInt(expStr, 10);
    if (e < -4 || e >= 16) {
        return mant + "e" + (e < 0 ? "-" : "+") + String(Math.abs(e)).padStart(2, "0");
    }
    const s = String(x);
    return s.includes(".") ? s : s + ".0";
}

window.TrainingPy = { randint, choice, shuffle, npRandint, triangular, int, numStr, fixed, round, floatStr };
})();
