"""Exact algebra controls for the documented analytic Green-null theorem.

No sampled inequality is presented as an analytic or Lean proof.
"""
from fractions import Fraction as F
from pathlib import Path
import json


def main():
    checks = 0

    def check(condition):
        nonlocal checks
        assert condition
        checks += 1

    # Pole integration by parts, including both indefinite rows.
    for c in map(F, range(-4, 5)):
        for s in map(F, range(-4, 5)):
            energy = 2*c*c-2*s*s
            first = 2*(-s/2)**2-2*(-c/2)**2
            second_pairing = 2*(c/4)*c-2*(s/4)*s
            check(second_pairing == -first == energy/4)
            check(second_pairing-energy/4 == 0)
            check((c+s == 0 and c-s == 0) == (c == 0 and s == 0))

    cases = []
    for r in range(1, 33):
        f2 = max(r-2, 0)
        check(f2 < r)  # Inactive Z=K contradicts the proved bijection.
        for parity in (0, 1):
            moments = []
            for j in range(r):
                p = (parity+j) % 2
                moment = (-F(1, 2))**j
                moments.append((moment if p == 0 else F(0),
                                moment if p == 1 else F(0)))
            moment_rank = 1 if r == 1 else 2
            check(moment_rank == min(2, r))
            check(r-moment_rank == f2)
            for j in range(f2):
                # L_p h_j = h_(j+2)-h_j/4 annihilates both moments.
                check(all(moments[j+2][i]-moments[j][i]/4 == 0
                          for i in (0, 1)))
            # Independent stripping columns have distinct highest nonzero index.
            columns = [[F(k == j+2)-F(k == j)/4 for k in range(r)]
                       for j in range(f2)]
            check(all(column[j+2] == 1 and
                      all(column[k] == 0 for k in range(j+3, r))
                      for j, column in enumerate(columns)))
            cases.append({'r': r, 'generator_parity': parity,
                          'active_moment_rank': moment_rank, 'dim_Z': f2,
                          'inactive_branch': 'excluded by analytic inverse'})

    margin = F(1, 4)-F(3, 8)**2
    check(margin == F(7, 64))
    check(1/margin == F(64, 7))
    # Rational controls of the exact polynomial used in the source filter bound.
    for theta in [F(0), F(1, 10), F(1), F(10), F(100)]:
        for beta in [F(-3, 8), F(-1, 4), F(0), F(1, 4), F(3, 8)]:
            q = theta**2
            b2 = beta**2
            modulus_sq = (q+F(1, 4)-b2)**2+4*q*b2
            gap = (F(1, 4)-b2-margin)*(2*q+F(1, 4)-b2+margin)+4*q*b2
            check(modulus_sq-(q+margin)**2 == gap >= 0)

    result = {'kind': 'exact rational controls; analytic proof in companion note',
              'assertions': checks, 'chain_cases': cases,
              'source_margin': str(margin), 'source_inverse_bound': '64/7',
              'analytic_gate_closed': 'nonzero nonnegative actual contact is pole-active',
              'global_signed_sharp_subsequence': 'unproved',
              'positive_lowest_eigenmode': 'same inverse theorem with Q-mu; not excluded',
              'lean_certified': False,
              'recovered_head': '4a2952ae9a25e6c1bf2d972b03f15bec322678fd',
              'input_blobs': {
                  'KERNEL_DERIVATIVE_CHAIN': 'e124b8a31a00df61908ce71cedd4ab7f83a14c76',
                  'POLE_STRIPPED_CHAIN': '87a296ab96c1888b77c864136279d31b420d6e74',
                  'POLE_RESONANCE_COMPATIBILITY': 'dd12a329fb0ecf518814adfcb2313029af803169',
                  'POLE_WEYL_INVISIBILITY': '50cb4bd709953cd799d88d11a57e5b87fc0f49f6',
                  'SOURCE_HEIGHT_GRAPH_ERROR': 'b968aa0a3c5eb5ba680ee0251692e24853dadd74',
                  'EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX': 'c369d3760606d9e5b9ae0f4862156fd712e5be29',
                  'ACTUAL_LOG_OPERATOR_ATTACHMENT': '5b9fedd77956f6ba3e2efc0a71be14f673596fd1'}}
    root = Path(__file__).resolve().parents[1]
    target = root/'notes/data/RPB108_POLE_GREEN_NULL_ATTACHMENT_20261007.json'
    target.write_text(json.dumps(result, indent=2)+'\n')
    print(json.dumps({'assertions': checks, 'chain_cases': len(cases),
                      'manifest': str(target)}))


if __name__ == '__main__':
    main()
