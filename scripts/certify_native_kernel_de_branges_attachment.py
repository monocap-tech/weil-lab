"""Exact Gaussian-rational controls, not proofs of the analytic attachment."""
from fractions import Fraction as F
from itertools import product
from pathlib import Path
import json


def g(a=0, b=0):
    return (F(a), F(b))


def add(x, y):
    return (x[0]+y[0], x[1]+y[1])


def neg(x):
    return (-x[0], -x[1])


def sub(x, y):
    return add(x, neg(y))


def mul(x, y):
    return (x[0]*y[0]-x[1]*y[1], x[0]*y[1]+x[1]*y[0])


def conj(x):
    return (x[0], -x[1])


def scale(x, t):
    return (x[0]*t, x[1]*t)


def abs2(x):
    return x[0]**2+x[1]**2


def pole(c, s, v, t):
    return scale(sub(mul(c, conj(v)), mul(s, conj(t))), F(2))


def linear_product(q, w):
    """(z-w)q(z), in ascending coefficient order."""
    result = [g() for _ in range(len(q)+1)]
    for j, value in enumerate(q):
        result[j] = sub(result[j], mul(w, value))
        result[j+1] = add(result[j+1], value)
    return result


def evaluate(p, z):
    result = g()
    for value in reversed(p):
        result = add(mul(result, z), value)
    return result


def main():
    count = 0

    def check(x):
        nonlocal count
        assert x
        count += 1

    choices = [g(), g(1), g(0, 1), g(F(1, 2), F(-1, 3))]
    for c, s, v, t in product(choices, repeat=4):
        first = pole(scale(s, -F(1, 2)), scale(c, -F(1, 2)), v, t)
        second = pole(c, s, scale(t, -F(1, 2)), scale(v, -F(1, 2)))
        check(add(first, second) == g())

    # Expanding the two energies with a skew derivative pairing q=i b.
    parameters = [g(1), g(-1), g(F(1, 4), F(1, 3)),
                  g(F(-1, 4), F(2, 5))]
    for lam, ed, eu, b in product(parameters, [F(0), F(1), F(9)],
                                  [F(0), F(1), F(4)], [F(-2), F(0), F(3)]):
        q = g(0, b)
        base = g(ed+abs2(lam)*eu)
        old = sub(sub(base, mul(conj(lam), q)), mul(lam, conj(q)))
        flipped = add(add(base, mul(lam, q)), mul(conj(lam), conj(q)))
        check(old == flipped)
        mixed = sub(q, scale(lam, eu))
        check(mixed[0] == -lam[0]*eu)
        check((mixed[0] == 0) == (eu == 0))  # Re lambda is nonzero.

    ws = [g(0, F(1, 4)), g(F(2), F(-1, 3)), g(F(-1), F(3, 8))]
    etas = list(map(F, [-3, -1, 0, 1, 4]))
    divisions = 0
    for r in range(2, 18):
        for w in ws:
            q = [g(F(j+1, j+2), F((-1)**j, j+3)) for j in range(r-1)]
            original = linear_product(q, w)
            flipped = linear_product(q, conj(w))
            check(evaluate(original, w) == g())
            check(evaluate(flipped, conj(w)) == g())
            check(len(q) == r-1 and len(flipped) == r)
            lam = mul(g(0, -1), w)
            check(lam[0] == w[1] != 0)
            for eta in etas:
                check(abs2(evaluate(original, g(eta))) ==
                      abs2(evaluate(flipped, g(eta))))
                check(abs2(sub(g(eta), w)) == abs2(sub(g(eta), conj(w))))
            divisions += 1

    # Genuine finite de Branges polynomial control with norm |a|2+|b|2/64.
    for w, b in product(ws, choices[1:]):
        a = neg(mul(b, w))
        reflected_a = neg(mul(b, conj(w)))
        check(abs2(a)+abs2(b)/64 == abs2(reflected_a)+abs2(b)/64)

    z = g(0, F(1, 4))
    onb = [[g(1)], [g(), g(8)]]
    diagonal = sum(abs2(evaluate(p, z)) for p in onb)
    reflected = g()
    signed_pairs = F(0)
    for p in onb:
        f = evaluate(p, z)
        fbar = evaluate(p, conj(z))
        reflected = add(reflected, mul(f, conj(fbar)))
        positive = scale(add(f, fbar), F(1, 2))
        negative = scale(sub(fbar, f), F(1, 2))
        signed_pairs += abs2(positive)-abs2(negative)
    check(abs(z[1]) <= F(3, 8))
    check(diagonal == 5)
    check(reflected == g(-3))
    check(signed_pairs == reflected[0] == -3)
    check(sum(abs2(evaluate(p, g())) for p in onb) == 1)

    result = {
        'kind': 'exact Gaussian-rational controls; analytic proof in companion note',
        'assertions': count, 'polynomial_division_cases': divisions,
        'reflected_kernel_control': {'beta': '1/4', 'diagonal': '5', 'reflected': '-3'},
        'actual_attachment': 'physical L2 finite kernel satisfies all three de Branges axioms',
        'native_energy_evaluation_at_nonzero_contact': 'does not descend to quotient',
        'positive_eigenmode': 'same attachment with Q-mu; spectral shift retained',
        'global_signed_sharp_subsequence': 'unproved', 'lean_certified': False,
        'recovered_head': '81dca4d9765fbcbfe9d0718f3d116ce6f22b44ac',
        'input_blobs': {
            'POLE_GREEN_NULL_ATTACHMENT': 'bc08f1d10446088871c490815d3e833b46b0c293',
            'KERNEL_DERIVATIVE_CHAIN': 'e124b8a31a00df61908ce71cedd4ab7f83a14c76',
            'SHARP_ARITHMETIC_FRAMEWORK_AUDIT': 'a2607dee10e2aa834456ea363ea56ec4e9b5d76f',
            'ACTUAL_SHARP_LOG_LIMIT': '310fbfd874f2fb6a0cda70f38d50fb656c26029e',
            'CRITICAL_EIGENMODE_TARGET': '3354b89638b643d5b21c4c428f069f738ccf59f5'},
        'primary_framework': {
            'author': 'Yurii Belov', 'title': 'Complementability of exponential systems',
            'doi': '10.1016/j.crma.2014.12.004', 'section': '3.1, page 217',
            'url': 'https://comptes-rendus.academie-sciences.fr/mathematique/item/10.1016/j.crma.2014.12.004.pdf',
            'used': 'three-axiom definition only; actual hypotheses proved in companion note',
            'not_imported': 'complementability, later no-common-real-zero hypothesis, RH claim'}}
    target = Path(__file__).resolve().parents[1]/'notes/data/RPB108_KERNEL_DE_BRANGES_ATTACHMENT_20261007.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'assertions': count, 'division_cases': divisions, 'manifest': str(target)}))


if __name__ == '__main__':
    main()
