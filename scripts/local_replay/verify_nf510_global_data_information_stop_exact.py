#!/usr/bin/env python3
"""NF510: exact source-ledger gate and odd localized-data nonidentifiability.

Certifies a *method* information stop: complete NF505 global physical
Gram, mixed moments, and W energy do not determine any individual residual
cell energy, even when the selected functions and responses are odd.

Not a claim that the ORIGINAL NF407 source is indeterminate: the original
source fixes W, and must be evaluated again to certify local E_H and b_H.
"""
from __future__ import annotations
import argparse
import hashlib
import json
from fractions import Fraction as Q
from pathlib import Path

SOURCE = '0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAMS = 'c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NATIVE_SHA = 'ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
AUDIT_SHA = '0fd77189a8b49106ca634bda33173e8adae91126144e33ba740e437f831b9a28'


def read(path):
    b = Path(path).read_bytes()
    return json.loads(b), hashlib.sha256(b).hexdigest()


def dot(x, y):
    return sum((a*b for a, b in zip(x, y)), Q(0))


def solve(a, b):
    n = len(b)
    t = [list(a[i])+[b[i]] for i in range(n)]
    for c in range(n):
        k = next((r for r in range(c, n) if t[r][c]), None)
        assert k is not None, 'Singular source-control Gram'
        t[k], t[c] = t[c], t[k]
        pivot = t[c][c]
        t[c] = [v/pivot for v in t[c]]
        for r in range(n):
            if r != c:
                z = t[r][c]
                t[r] = [u-z*v for u, v in zip(t[r], t[c])]
    return [r[-1] for r in t]


def mat_gram(rows, indices):
    m = len(rows[0])
    return [[sum((rows[k][i]*rows[k][j] for k in indices), Q(0))
             for j in range(m)] for i in range(m)]


def moments(rows, w, indices):
    m = len(rows[0])
    return [sum((rows[k][i]*w[k] for k in indices), Q(0)) for i in range(m)]


def quadratic(a, v):
    return dot(v, [dot(row, v) for row in a])


def localized_odd_control(seed):
    # Two mirrored 6-point microcells H_A and H_B, with odd analytic
    # selected functions x and x^3. A local 3-vector of residual values
    # is chosen orthogonal to both columns on its mirrored cell.
    # Disjoint positive nodes ensure different physical localization.
    pos_a = [Q(j+1, 10) for j in range(3)]
    pos_b = [Q(j+6, 10) for j in range(3)]
    x = pos_a + pos_b + [-v for v in pos_a+pos_b]
    J = [[v, v**3] for v in x]
    H_a = (0,1,2,6,7,8)
    H_b = (3,4,5,9,10,11)
    O = tuple(range(len(x)))
    G = mat_gram(J, O)
    a = [Q(3, 7), Q(-8, 11)]
    projection = [dot(row, a) for row in J]

    def local_r(vals, cell):
        # Cross product of (x_i) and (x_i^3) on three positive nodes.
        v0, v1, v2 = vals
        y = [v1*v2**3-v2*v1**3,
             v2*v0**3-v0*v2**3,
             v0*v1**3-v1*v0**3]
        assert dot(vals, y) == dot([v**3 for v in vals], y) == 0
        r = [Q(0) for _ in O]
        for i, k in enumerate(cell[:3]):
            r[k] = y[i]
        for i, k in enumerate(cell[3:]):
            r[k] = -y[i]
        assert all(dot(col, r) == 0 for col in zip(*J))
        return r

    r_a = local_r(pos_a, H_a)
    r_b = local_r(pos_b, H_b)
    qa = dot(r_a, r_a)
    qb = dot(r_b, r_b)
    assert qa > 0 and qb > 0

    # Set r_A' = sqrt(qb/qa)*r_A and r_B'=r_B.
    # Both have squared norm qb, so W_A and W_B have exactly identical
    # FULL Gram G, mixed moments b=Ga, and full energy a^TGa+qb.
    # The square root need not be rational; all identities are exact.
    b = [dot(row, a) for row in G]
    total_energy = quadratic(G, a)+qb
    assert solve(G, b) == a
    local_energy_vectors = ([qb, Q(0)], [Q(0), qb])

    # For each target cell, source-local E_H, b_H and C_H are needed.
    # Validate exact refit identity using unscaled example residuals;
    # scaling to matched qb does not change its logical content.
    for r in (r_a, r_b):
        w = [projection[k]+r[k] for k in O]
        gg = mat_gram(J, O)
        bb = moments(J, w, O)
        aa = solve(gg, bb)
        RR = dot(w,w)-dot(bb,aa)
        assert RR == dot(r,r)
        for H in (H_a, H_b):
            out = tuple(i for i in O if i not in H)
            C = mat_gram(J, H)
            bH = moments(J, w, H)
            EH = sum((w[i]**2 for i in H), Q(0))
            eH = EH-2*dot(aa,bH)+quadratic(C, aa)
            assert eH == sum((r[i]**2 for i in H), Q(0))
            kH = [bH[i]-dot(C[i],aa) for i in range(2)]
            gain = eH+dot(kH, solve(mat_gram(J,out), kH))
            new = sum((w[i]**2 for i in out), Q(0))
            bout=moments(J,w,out)
            new -= dot(bout,solve(mat_gram(J,out),bout))
            assert RR-new==gain
            if not any(r[i] for i in H):
                assert gain == 0 and new == RR
            else:
                assert new == 0 and gain == RR
    return {'odd_selected_functions': ['x','x^3'],
            'mirrored_disjoint_microcells': 2,
            'selected_gram_example': [[str(v) for v in row] for row in G],
            'common_mixed_moments': [str(v) for v in b],
            'common_full_energy': str(total_energy),
            'common_perpendicular_energy': str(qb),
            'local_perpendicular_energy_pattern_A': [str(v) for v in local_energy_vectors[0]],
            'local_perpendicular_energy_pattern_B': [str(v) for v in local_energy_vectors[1]],
            'exact_refit_identities_checked': 4}


def original_source_gate(n, audit):
    assert n['pass'] == 'NF504-native' and audit['pass'] == 'NF505'
    assert n['source_original_NF407_sha256'] == audit['original_nf407_source_sha256'] == SOURCE
    assert n['source_original_NF406_sha256'] == audit['original_nf406_seams_sha256'] == SEAMS
    assert n['original_selected_J_dimension'] == audit['original_selected_true_J_dimension'] == 242
    assert n['original_source_basis_nodes'][241] == ['pole', None]
    assert n['original_exterior_center_radius'] == '549/500'
    assert n['original_support_saturated_physical_Hilbert_gate'] == 'CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert audit['original_original_S_support_saturated_physical_Hilbert_verdict'] == 'CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert n['original_weil_multiplier_source_image_domain'] == 'OPEN'
    lo,hi = map(Q, n['original_original_saturated_exterior_residual_outward'])
    gamma = Q(n['original_original_gamma_squared'])
    assert gamma == Q(audit['original_original_gamma_squared']) and 0 < gamma < lo <= hi
    E = tuple(map(Q, n['original_original_W_exterior_energy_outward']))
    assert 0 < E[0] <= E[1]
    return lo,hi,gamma,E


def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--native', required=True)
    ap.add_argument('--audit', required=True)
    ap.add_argument('--output', required=True)
    o=ap.parse_args()
    n,nsha=read(o.native)
    audit,asha=read(o.audit)
    assert nsha==NATIVE_SHA and asha==AUDIT_SHA
    assert audit['original_nf504_original_entire_242_exterior_4096bit_native_json_sha256']==nsha
    lo,hi,gamma,E=original_source_gate(n,audit)
    tests=[localized_odd_control(j) for j in range(5)]
    assert all(x==tests[0] for x in tests)
    result={
        'pass':'NF510-source-aggregate-information-limit-exact',
        'standing':'ANALYTIC COUNTERMODELS + EXACT SOURCE GLOBAL DATA; NO ORIGINAL LOCAL W CELL INTEGRATIONS',
        'original_nf505_native_sha256':nsha,
        'original_nf505_independent_audit_sha256':asha,
        'original_source_nf407_sha256':SOURCE,
        'original_source_nf406_sha256':SEAMS,
        'original_selected_dimension':242,
        'original_exterior_full_schur_interval':[str(lo),str(hi)],
        'original_nf404_gamma_squared':str(gamma),
        'old_exterior_energy_interval':[str(v) for v in E],
        'global_Gram_moments_and_energy_do_not_determine_per_cell_residual_energy':True,
        'odd_mirrored_two_selected_generator_exact_countermodel':tests[0],
        'functional_analytic_argument':'Each positive-measure open mirrored H supports odd C_c^infty functions in the orthogonal complement of the 242 restricted analytic generators: take 243 disjoint odd bump pairs, solve 242 homogeneous moment equations, normalize. Two different H can carry equal-energy residuals with identical global Gram, mixed moments, and total energy after adding fixed projection.',
        'original_nf407_full_source_still_determines_W':True,
        'sufficient_per_cell_source_inputs':['E_H=integral_H W^2','b_H=integral_H J W','C_H=integral_H J J^T'],
        'exact_local_energy_formula':'e_H=E_H-2*a^T*b_H+a^T*C_H*a; a=G_O^-1 b_O',
        'exact_local_refit_gain':'R(O)-R(O\\H)=e_H+k_H^T*(G_O-C_H)^-1*k_H; k_H=b_H-C_H*a',
        'original_individual_microcell_residual_energy_ej_computed':False,
        'NF509_full_selected_leverage_original_native_accepted':False,
        'named_original_local_support_decision':'OPEN',
        'Weil_multiplier_image_graph_domain':'OPEN',
        'W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF510 SHA-pinned original source aggregate ledger + odd two-cell information countermodel PASS')
    print('NF505 R(O) lower/gamma²>',float(lo/gamma),'but named local energy is NOT determined')
    print('Next required source data: actual full physical E_H,b_H,C_H from ORIGINAL W, not global-ledger inversion')
    print('W-ODD-NEG / source eligibility / RH OPEN')

if __name__=='__main__':main()
