(() => {
"use strict";

// Python-compatible helpers so converted exercises keep Python's exact behaviour.
// Exercises must call these lazily (inside the exercise function), via window.TrainingPy.

// random.randint(a, b): inclusive on both ends
function randint(a, b) {
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

// round(x, ndigits) for ndigits >= 0 and float x: exact-value rounding, ties to even
// (Math.round rounds ties up and works on x * 10^n, so it differs from Python)
function round(x, nd = 0) {
    if (!Number.isFinite(x) || x === 0 || Math.abs(x) >= 1e21) return x; // keeps -0
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
            return Number((neg ? "-" : "") + res);
        }
    }
    return Number(x.toFixed(nd));                    // non-tie: correctly rounded
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

window.TrainingPy = { randint, choice, shuffle, round, floatStr };
})();
