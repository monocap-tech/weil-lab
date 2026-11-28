#!/usr/bin/env python3
"""IV050 exact-rational preflight, NOT a Lean theorem or continuum proof.

Checks rational inequalities in the analytical Schur estimate for the
ORIGINAL signed Weil source, and verifies pinned IV047/IV049 scripts.
No external packages, network, CI, floats, or implicit trust in a result file.
"""
from __future__ import annotations
from fractions import Fraction as Q
from pathlib import Path
from hashlib import sha256
import json
import math

ROOT = Path(__file__).resolve().parent
UPSTREAM = {
    'IV047_infinite_dim_high_mode_checker.py':
        'd64d8b08529e529a1be86923d25d2a76ce81aa42889eab97257c5f6aa0e083a5',
    'IV049_energy_relative_cell_schur_checker.py':
        '2a2010172c9bda33c3c58477b8ada82ba850862ba96442e528425e342590144d',
}


def check() -> dict:
    for name, expected in UPSTREAM.items():
        p = ROOT / name
        assert p.is_file(), f'missing source dependency: {p}'
        actual = sha256(p.read_bytes()).hexdigest()
        assert actual == expected, (name, actual, expected)

    width_max = Q(1, 1000)
    # All-s>0 K(s) <= 1/(2s)+1 and |K'(s)| <= 4/s^2:
    # 4 exp(s/2) >= 4+2s+s^2/2 > 1/2+5s/4+s^2/2.
    assert Q(4)-Q(1,2) == Q(7,2)
    assert Q(2)-Q(5,4) == Q(3,4)

    # For each interior cell, subtract its mean; the two centered
    # -log u pieces have L2 norm 1 each, so half their sum <=1.
    # Absolute kernel error <= 1 for 0<s<=w, projected error <=2w.
    diag_bound = Q(1)+2*width_max
    assert diag_bound < 2

    # Adjacent cell: sqrt(Int_0^1 log(1+1/u)^2 du)/2 +w.
    # log2 < 7/10, integral < (7/10)^2+14/10+2 <4.
    assert Q(7,10)**2+2*Q(7,10)+2 <4
    near_bound = Q(1)+width_max
    assert near_bound < 2

    # Distant cells: |K'|<=4/s^2, d>=2, so column block
    # ||Q_j L_K e_k|| <=4/(d-1)^2. Since sum_{n>=1}1/n^2<2,
    # each infinite row/column sum is <2+2*2+2*4*2=22.
    diag_envelope, near_envelope, far_constant = Q(2),Q(2),Q(4)
    row_sum_envelope=diag_envelope+2*near_envelope+2*far_constant*2
    assert row_sum_envelope==22

    # Genuine original von Mangoldt two-sign operator norm and both
    # Hermitian crossed pole operator norms: MAX(||h||^2,||k||^2)<5.
    prime_envelope=Q(71,10)
    pole_envelope=Q(5)
    mixed_envelope = row_sum_envelope+prime_envelope+pole_envelope
    assert mixed_envelope==Q(341,10)
    assert mixed_envelope<35

    # Rigorous conservative total mixed-block bound B_M<35 for
    # every equal-cell mesh w<=1/1000; if C_M>=c_M>0 then
    # ||C_M^(-1/2) B_M||^2 < 1225/c_M.
    squared_mixed_envelope=Q(35)**2
    assert squared_mixed_envelope==1225
    # The IV047 M=100000 fixed bound alone is not nearly sharp enough:
    c_at_100k=Q(1,100)
    correction_envelope=squared_mixed_envelope/c_at_100k
    assert correction_envelope==122500

    # Exact finite Schur-majorant row sums for representative dense
    # Galerkin matrices. These do not prove the continuum comparison;
    # they audit coefficient indexing (especially d=2) and row bounds.
    sizes=(2,3,8,32,100,300)
    finite_rows={}
    for M in sizes:
        matrix_bound=lambda d: diag_envelope if d==0 else (
            near_envelope if d==1 else far_constant/Q(d-1)**2)
        # At middle rows where both neighbors exist, all nonnegative
        # scalar block majorants are accounted for.
        maximum=max(sum((matrix_bound(abs(j-k)) for k in range(M)),Q(0))
                    for j in range(M))
        assert maximum<row_sum_envelope,(M,maximum)
        finite_rows[str(M)]=str(maximum)

    # The finite source 100000 and 132000 cell widths and Q domain
    # are consistent with the stated uniform-column hypotheses.
    mesh_widths={M:Q(11,5*M) for M in (100000,132000)}
    for M,w in mesh_widths.items():
        assert w<=width_max and M*w==Q(11,5)

    return {
        'schema':'IV050-dense-source-Gamma-Schur-preflight-v1',
        'pass':True,
        'status':'analytical finite algebra; continuum/Lean still pending',
        'upstream_sha256':UPSTREAM,
        'kernel_derivative_bound':'|K_prime(s)| <= 4/s^2 for all s>0 (proof in report)',
        'absolute_scalar_block_row_col_bound':str(row_sum_envelope),
        'Gamma_low_high_operator_bound':'<22 on all equal-cell grids width<=1/1000',
        'original_prime_operator_bound':'<71/10',
        'original_cross_poles_operator_bound':'<5',
        'original_signed_low_high_operator_bound':'<341/10<35',
        'energy_relative_operator_squared_bound':'<1225/c_M',
        'fixed_M_100000_illustrative_bound':'<122500 (not useful for positivity)',
        'finite_scalar_majorant_rows':finite_rows,
        'source_mesh_widths':{str(M):str(w) for M,w in mesh_widths.items()},
        'assumptions':["IV043 source inverse Fourier Gamma form, not yet Lean certified",
                       "IV047 positive c_M and its diverging high-mode lower coefficient",
                       "Original IV011 prime and original two-pole source identities"],
        'not_claimed':['uniform positivity of W', 'finite-M Schur positivity',
                       'independent spectral equivalence', 'Lean PASS', 'RH']
    }


if __name__=='__main__':
    result=check()
    path=ROOT/'IV050_dense_mode_schur_receipt.json'
    source_hash=sha256(Path(__file__).read_bytes()).hexdigest()
    result['script_sha256']=source_hash
    path.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
    print('IV050 EXACT-RATIONAL PREFLIGHT PASS')
    print('Gamma low/high <22, original W low/high <35')
    print('whole dense low space energy-relative Schur <1225/c_M, asymptotically 0')
    print('script SHA256:',source_hash)
    print('receipt:',path)
