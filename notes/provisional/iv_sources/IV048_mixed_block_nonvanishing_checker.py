#!/usr/bin/env python3
"""Weil-Lab IV048: exact arithmetic for original-W low/high mixed-block obstruction.

ANALYTIC-ONLY / NONKERNEL. Continuum Gamma kernel, interval-Dirichlet,
reflection, and form-domain assertions are proved in the companion report,
not machine-proved by this arithmetic checker. No repository actions.
"""
from fractions import Fraction as F
from hashlib import sha256
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parent
OUT=ROOT/'IV048_mixed_block_nonvanishing_receipt.json'

predecessors={
    'IV047_infinite_dim_high_mode_checker.py': 'd64d8b08529e529a1be86923d25d2a76ce81aa42889eab97257c5f6aa0e083a5',
    'IV046_fixed_window_multicell_variational_checker.py': 'd2ae448c0c28981fed1ebc8d271a1370070a24cf88649f50acf7af18759e59ac',
    'IV044_pole_parity_schur_checker.py': 'b2142d08a295819bd27e554e23c91e7ba774e5fcfa29920c23f1c990ec5a5b1f',
}
for name, digest in predecessors.items():
    got=sha256((ROOT/name).read_bytes()).hexdigest()
    assert got==digest, (name,got,digest)

# Actual source kernel: K(u)=exp(-u/2)/(1-exp(-2u)),
# H(s)=int_s^infinity K(u) du=atanh(exp(-s/2))+atan(exp(-s/2)).
# On 0<s<=1/10, 0<=K(s)-1/(2s)<=1.
# The *non-rational* analytic inequality is proved in companion report.
# For e=1_J/sqrt(w), q=(2*1_middle - 1_J)/sqrt(w),
# Gamma(e,q) = -(1/2)log(27/16)+epsilon, |epsilon|<=2w.
# log(27/16) = 2 atanh(11/43) >22/43, exact rational atanh series.
assert (F(27,16)-1)/(F(27,16)+1)==F(11,43)
LOG_LO=F(22,43)
GAMMA_MIX_MAG_LO=LOG_LO/2
assert GAMMA_MIX_MAG_LO==F(11,43)
assert GAMMA_MIX_MAG_LO-F(1,4)==F(1,172)

# Two-term L2 density q lies in the cell-mean-zero complement.
# For any interval width L, D[1_interval]=sum_n (1-e^(-2 a_n L))/(2 a_n^2)
# <= L*(sum_{n<2^17}1/a_n)+ 1/(2*(2^17-1)).
# Harmonic dyadic groups give sum_{n<2^17}1/(n+1/4) <=4+17=21.
N=1<<17
HARMONIC_COARSE_UP=F(21)
TAIL_UP=F(1,2*(N-1))
assert N==131072 and HARMONIC_COARSE_UP==F(21)

results={}
for M in (100000,132000):
    a=F(11,10)
    width=2*a/M
    assert 0<width<=F(1,10)
    # Pick an ACTUAL cell containing 1/4, and reflect it.
    j=int((F(1,4)+a)//width)
    left=-a+j*width
    right=left+width
    mirror_index=M-1-j
    assert left<=F(1,4)<right and j!=mirror_index
    assert left>0 and F(49,100)<2*left<=2*right<F(51,100)
    # log2>2/3 by atanh(1/3) and full reflected-pair diameter<51/100.
    assert F(51,100)<F(2,3)
    # Exact geometry ensures no active prime n>=2 couples same-cell or reflected pair.
    # Both original crossed poles satisfy |Pole(f,g)|<=8||f||_1||g||_1.
    # Local same-cell: Gamma(e,q) <=-11/43+2w; pole <=8w.
    local_abs_lower=GAMMA_MIX_MAG_LO-10*width
    assert local_abs_lower>F(1,4)
    # Reflected cell separation >49/100; K(delta)<=1+1/(2delta)<=99/49.
    cross_gamma_ub=F(99,49)
    cross_signed_ub=cross_gamma_ub+8
    assert cross_signed_ub<F(11)
    # Parity-symmetric/antisymmetric normalized e_±,q_±.
    parity_abs_lower=GAMMA_MIX_MAG_LO-21*width
    assert parity_abs_lower>F(1,4)
    # Coarse exact Gamma form-energy bound for q on one cell:
    # D[J]/w<22, D[C]/w<11, q=(2*1_C-1_J)/sqrt(w),
    # D[q]<=8 D[C]/w+2 D[J]/w<132.
    assert TAIL_UP/width<F(1,2), (M,TAIL_UP/width)
    DJ_over_w_up=HARMONIC_COARSE_UP+TAIL_UP/width
    DC_over_w_up=HARMONIC_COARSE_UP/2+TAIL_UP/width
    assert DJ_over_w_up<22 and DC_over_w_up<11
    DQ_UP=8*F(11)+2*F(22)
    assert DQ_UP==132
    # q has prime-free support in its cell and gamma(0)<0.
    WQ_UP=F(133)
    assert DQ_UP+8*width<WQ_UP
    # For the reflected +/- combination, D[q±] <=2D[q]<264,
    # prime remains zero, |Pole|<=16w, gamma(0)<0.
    WQ_PARITY_UP=F(265)
    assert 2*DQ_UP+16*width<WQ_PARITY_UP
    # IV047 proves the high compression positive: c>1/100 here.
    # Exact variational Schur loss >= |W(e,q)|²/W(q,q), with W(q,q)>0.
    loss_single_lower=F(1,16)/WQ_UP
    loss_parity_lower=F(1,16)/WQ_PARITY_UP
    assert loss_single_lower==F(1,2128)
    assert loss_parity_lower==F(1,4240)
    # Check the naive norm-only cross upper correction cannot be called small
    # using only IV047's c=1/100 and |B|>1/4:
    naive_norm_upper_budget_min=(F(1,4)**2)/F(1,100)
    assert naive_norm_upper_budget_min==F(25,4)
    results[str(M)]={
        'cell_width':str(width), 'chosen_cell_index_zero_based':j,
        'chosen_physical_cell':[str(left),str(right)],
        'reflected_index':mirror_index,
        'cross_reflection_sep_lower':str(2*left),
        'union_diameter_upper':str(2*right),
        'cross_kernel_upper':str(cross_gamma_ub),
        'original_W_local_mixed_magnitude_strict_lower':str(local_abs_lower),
        'original_W_both_parity_mixed_magnitude_strict_lower':str(parity_abs_lower),
        'original_single_high_test_energy_strict_upper':str(WQ_UP),
        'original_parity_high_test_energy_strict_upper':str(WQ_PARITY_UP),
        'source_Schur_loss_single_strict_lower':str(loss_single_lower),
        'source_Schur_loss_each_parity_strict_lower':str(loss_parity_lower),
        'naive_cross_norm_budget_value_at_known_lower':str(naive_norm_upper_budget_min),
    }

# The gain identity in IV047 does not control the cross terms of the
# cell indicator projection; true source mixed K and pole are necessary.
report={
 'stage':'IV048',
 'status':'exact Fraction geometry and Schur inequalities PASS; classical continuum proofs, NOT Lean',
 'source':'original signed Zeta23 W=Gamma - prime + both crossed poles on I=(-11/10,11/10)',
 'K_antiderivative':'H(s)=atanh(exp(-s/2))+atan(exp(-s/2)); H_prime=-K',
 'original_source_gamma_mixed_limit':'-(1/2)*log(27/16) for normalized cell e and mean-zero central-edge q',
 'log_lower':'log(27/16)>22/43',
 'valid_small_kernel_delta':'0<=K(s)-1/(2s)<=1 for 0<s<=1/10 (calculus proof in report)',
 'finite_energy_upper':'D(q)<132 from dyadic harmonic envelope N=2^17, q=2 middle minus whole',
 'original_actual_prime_mixed':'exactly zero within chosen cell and its reflected pair; log(2)>2/3',
 'original_two_poles':'|Pole(e,q)|<=8w; reflected cross <=8w; full source signs retained',
 'mesh_certificates':results,
 'proof_scope':'mixing nonvanishing and strict nonzero Schur correction on two IV047 physical partitions; NOT whole W positivity or RH',
 'mathematical_not_machine_proved':['exact original Gamma physical kernel source attachment','classical Fourier atom/limit','K antiderivative derivative and inequalities','closed Gamma form domain and smoothing','IV047 high-mode positive form','source operator Schur completion'],
 'predecessor_SHA256':predecessors,
 'no_new_CI':True,
}
report['checker_SHA256']=sha256(Path(__file__).read_bytes()).hexdigest()
OUT.write_text(json.dumps(report,sort_keys=True,indent=2)+'\n')
print('IV048 original signed mixed-block / finite Schur loss exact arithmetic PASS — NONKERNEL')
for n,d in results.items():
 print('cells',n,'width',d['cell_width'],'indices',d['chosen_cell_index_zero_based'],d['reflected_index'])
 print(' |W(e,q)|>',d['original_W_local_mixed_magnitude_strict_lower'],
       '; parity |W(e±,q±)|>',d['original_W_both_parity_mixed_magnitude_strict_lower'])
 print(' exact variational Schur loss >',d['source_Schur_loss_single_strict_lower'],
       'and on each parity >',d['source_Schur_loss_each_parity_strict_lower'])
print('IV047 coarse high-block c=1/100 alone yields a norm-only Schur correction budget at least 25/4; not a positivity proof')
print('script sha256',report['checker_SHA256'])
print('receipt',OUT)
