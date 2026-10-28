#!/usr/bin/env python3
"""Weil-Lab NF359: independent exact-rational energy-dual retyping preflight.

Read only: validates pinned PR355 archive and its actual 4x4 interval matrices.
Proves only algebraic sufficient threshold and physical E*Y scale; DOES NOT
compute the unprobed energy-dual Schur correction or certify canonical domain.
"""
import sys, json, hashlib, zipfile
from fractions import Fraction as F
from decimal import Decimal, localcontext
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
sys.set_int_max_str_digits(100000)
ARCH = Path(str(CUSTODY_ROOT / 'pr355-exterior.zip'))
ARCH_HASH = 'f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
DIAG_HASH = 'd853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9'

def dy(x): return F(int(x[0]))*F(2)**int(x[1])
def ball(x):
    a,r=dy(x[0]),dy(x[1]); assert r>=0
    return a-r,a+r

def decimals(x):
    with localcontext() as c:
        c.prec=34
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
    assert hashlib.sha256(ARCH.read_bytes()).hexdigest()==ARCH_HASH
    with zipfile.ZipFile(ARCH) as z:
        raw=z.read('original_exterior_scalar_floor_stop.json')
        rank_raw=z.read('original_BS_pruned_rank_bound.json')
    assert hashlib.sha256(raw).hexdigest()==DIAG_HASH
    d=json.loads(raw)
    rank=json.loads(rank_raw)
    eps=F(rank['pruned_physical_complement_negative_upper'])
    assert 0<eps<F(17,10**6)
    assert d['selected_rank']==242 and d['source_direction_count']==4
    assert d['four_probe_upper_is_global_upper'] is False
    assert d['complete_strong_action_computed'] is False
    g=F(d['four_probe_Schur_energy_operator_upper'])
    assert 0<g<F(1,500)
    H_floor=F(99,100)
    E_dual_accept=H_floor*(1-g)
    assert E_dual_accept > F(988,1000)
    mu=F(499,50000)
    strong_accept=mu*E_dual_accept
    form_equivalence_factor=1+eps/mu
    astar_dual_sufficient=E_dual_accept/form_equivalence_factor
    assert form_equivalence_factor<F(1002,1000)
    assert astar_dual_sufficient>F(986,1000)
    assert strong_accept > F(986,100000)
    # Physical correction: E*E is the retained exact-physical quotient S,
    # Y is the exact dyadic four-probe coefficient matrix, not rounded.
    S=[[ball(e) for e in row] for row in d['physical_quotient_Gram_native']]
    Y=[[dy(e) for e in row] for row in d['exact_complement_variational_coefficients']]
    ys=[]
    for j in range(4):
        val=F(0); err=F(0)
        for i in range(4):
            for k in range(4):
                lo,hi=S[i][k];mid=(lo+hi)/2; rad=(hi-lo)/2
                prod=Y[i][j]*Y[k][j]
                val+=prod*mid; err+=abs(prod)*rad
        assert val-err>0
        assert val+err<F(1,5000)
        ys.append({'j':j,'EY_squared_norm_mid':decimals(val),
                   'EY_squared_norm_interval_uncertainty_upper':decimals(err),
                   'EY_squared_norm_upper_lt':'1/5000'})
    report={
      'status':'NF359_ENERGY_DUAL_RETYPING_ACCEPTANCE_THRESHOLD_ONLY',
      'source_pr':355,'archive_sha256':ARCH_HASH,'diagnostic_sha256':DIAG_HASH,
      'source_selected_space':'original 242', 'critical_source_dimension':4,
      'g_four_probe_schur_relative_upper_exact':str(g),
      'Hphi_min_lower':str(H_floor),
      'energy_dual_unprobed_schur_operator_norm_sufficient_lt_exact':str(E_dual_accept),
      'energy_dual_unprobed_schur_operator_norm_sufficient_lt_decimal':decimals(E_dual_accept),
      'old_strong_Frobenius_sq_sufficient_lt_exact':str(strong_accept),
      'pruned_negative_operator_upper_decimal':decimals(eps),
      'form_equivalence_Astar_le_factor_CQ_decimal':decimals(form_equivalence_factor),
      'Astar_energy_dual_relative_sufficient_lt_decimal':decimals(astar_dual_sufficient),
      'old_strong_Frobenius_sq_sufficient_lt_decimal':decimals(strong_accept),
      'energy_dual_gate_does_not_require_strong_operator_action':True,
      'form_space_correction_requires_closed_positive_complement_form':True,
      'finite_probe_form_projection_orthogonal_remainder_is_independent_of_Yc':True,
      'EYc_physical_sq_norms':ys,
      'energy_dual_unprobed_operator_norm_computed':False,
      'original_canonical_domain_identification_open':True,
      'complete_242_schur_closed':False,
      'W_ODD_NEG':'OPEN'
    }
    dst=Path(str(CUSTODY_ROOT / 'nf359_energy_dual_entry.json'))
    dst.write_text(json.dumps(report,indent=2)+'\n')
    print(json.dumps({k:v for k,v in report.items() if k!='EYc_physical_sq_norms' and not k.endswith('_exact')},indent=2))
    for x in ys: print('EY squared',x)

if __name__=='__main__': main()
