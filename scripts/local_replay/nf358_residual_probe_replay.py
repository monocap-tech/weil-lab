#!/usr/bin/env python3
"""Exact-rational, read-only replay of the four-probe slice of NF357 strong residual.

Does NOT calculate the whole strong residual. Uses full original PR355
native 4x4 interval data as enclosures; does not use point midpoints as proofs.
"""
import hashlib, json, zipfile, sys
from pathlib import Path
import os
CUSTODY_ROOT = Path(os.environ.get("WEIL_CUSTODY_DATA_DIR", "/mnt/data"))
from fractions import Fraction as F
from decimal import Decimal, localcontext
sys.set_int_max_str_digits(100000)
ARCHIVE=Path(str(CUSTODY_ROOT / 'pr355-exterior.zip'))
PIN_ARCHIVE='f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0'
PIN_DIAG='d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9'

def dy(v): return F(int(v[0]))*F(2)**int(v[1])
def ball(b):
    a,r=dy(b[0]),dy(b[1]);assert r>=0
    return a-r,a+r

def neg(a): return (-a[1],-a[0])
def add(a,b): return (a[0]+b[0],a[1]+b[1])
def scale(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def absup(a):return max(abs(a[0]),abs(a[1]))
def dec(x):
    with localcontext() as c:
        c.prec=35
        return str(Decimal(x.numerator)/Decimal(x.denominator))

def main():
    assert hashlib.sha256(ARCHIVE.read_bytes()).hexdigest()==PIN_ARCHIVE
    with zipfile.ZipFile(ARCHIVE) as z:
        raw=z.read('original_exterior_scalar_floor_stop.json')
    assert hashlib.sha256(raw).hexdigest()==PIN_DIAG
    d=json.loads(raw)
    CE=[[ball(v) for v in row] for row in d['actual_exterior_signed_Gram_native']]
    Z=[[ball(v) for v in row] for row in d['actual_exterior_weak_coupling_native']]
    Y=[[dy(v) for v in row] for row in d['exact_complement_variational_coefficients']]
    assert all(len(row)==4 for row in (CE+Z+Y))
    D=[[add(Z[i][j],neg(sum_interval([scale(CE[i][k],Y[k][j]) for k in range(4)]))) for j in range(4)] for i in range(4)]
    dsq=sum((absup(e)**2 for row in D for e in row),F(0))
    inherited=F(d['four_probe_inverse_action_residual_Frobenius_squared_upper'])
    sfloor=F(d['physical_quotient_coefficient_floor'])
    proj=dsq/sfloor
    parent_proj=inherited/sfloor
    target=F(24651099,2500000000)
    mu=F(499,50000);gamma=F(99,100)
    g=F(d['four_probe_Schur_energy_operator_upper'])
    refined_target=mu*gamma*(1-g)
    assert dsq<inherited, 'direct interval enclosure exceeds accepted independent parent RC bound'
    assert proj<target/F(10)**300
    assert refined_target>target
    out={
      'status':'EXACT_LOCAL_RATIONAL_FOUR_PROBE_RESIDUAL_PROJECTION_ONLY',
      'archive_sha256':PIN_ARCHIVE,'diagnostic_sha256':PIN_DIAG,
      'parent_original_four_probe_residual_Frobenius_sq_upper':dec(inherited),
      'direct_independent_interval_four_probe_residual_Frobenius_sq_upper':dec(dsq),
      'physical_probe_Gram_coefficient_floor':dec(sfloor),
      'direct_projected_strong_residual_Frobenius_sq_upper':dec(proj),
      'parent_projected_strong_residual_Frobenius_sq_upper':dec(parent_proj),
      'complete_strong_residual_Frobenius_sq_required_below':dec(target),
      'retained_four_probe_energy_operator_upper':dec(g),
      'slightly_refined_complete_residual_Frobenius_sq_sufficient_threshold':dec(refined_target),
      'what_is_measured':'||P_E R||_F^2 <= ||Z-C_E Y_C||_F^2 / lambda_min(E*E), for exact physical E',
      'what_is_NOT_measured':'||(I-P_E)R||_F^2, or complete ||R||_F^2',
      'whole_R_bounded':False,'W_ODD_NEG':'OPEN'
    }
    p=Path(str(CUSTODY_ROOT / 'nf358_residual_probe_projection.json'))
    p.write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))

def sum_interval(v):
    s=(F(0),F(0))
    for x in v:s=add(s,x)
    return s

if __name__=='__main__':main()
