#!/usr/bin/env python3
"""EF38: first ACTUAL original SI10 protected-source L2 projection.

The original first source e=1_[-11/10,11/10]cos(2*pi*(37/64)x)
belongs to the actual original 469D even SI10 exceptional space V.
EF37 gave the whole genuine correlated signed physical base
 z=P_I[-sum_{n=2,3,4,5,7,8,9} w_n(e(x+ln n)+e(x-ln n))]
    +2<u,e>u, with u=cosh(x/2),
and an exact interval certificate for ||z||²<7/10.

Instead of bounding z BEFORE source projection, compute
  <z,e>=2 sum over the genuine eight positive-half source
  cutoff cells of P_j int cos² + Q_j int sin cos
                        + 2<u,e> int cosh cos.
All integrals use ORIGINAL EF37 340-digit outward intervals,
all seven physical cutoff flags, exact pole interval, actual
SI10 first frequency and physical support. The true
one-row orthogonal projection is
  ||z-P_span{e} z||²=||z||²-|<z,e>|²/||e||²<4/25.
As e belongs to V469, P_F e=0, so
  ||P_F g_e|| <= ||z-P_e z|| + ||h_arch,cut||
               <2/5+3/5=1.
The h_arch cutoff is the ENTIRE original EF37 infinite
quarter-digamma physical response (including its rigorous tail).
Thus the true original even cofinite first-source energy dual
and EF34 unseen eta<1/(17/25000)=25000/17.

This is a true source projection, but ONLY on the single exact
SI10 protected row e of 469. The remaining 468 rows, projection
conditioning, complete signed arch/base CROSS, actual eta, and
full first-source Schur sign remain OPEN. Analytic physical
attachment and core/digamma normalization audit separately open.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_ef24_original_even_edge_intervals import I,S,trig_pi
from validate_rpb108_ef29_original_even_mixed_vector import C0,OMEGA
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import (
    original_even_pole_diagonal
)
from validate_rpb108_ef37_original_even_correlated_prime_pole import (
    full_original_prime_cells,endpoint_data,
    original_prime_plus_pole_signed_norm_sq,arch_cut_complete_l2
)
from validate_rpb108_si06_negative_band import B

ROOT=Path(__file__).resolve().parents[1]
MU=F(17,25000)
BASE_PERP_SQ_UPPER=F(4,25)
ORIGINAL_ARCH_NORM_UPPER=F(3,5)
PROJECTION_NORM_UPPER=F(1)
ORIGINAL_ETA_UPPER=F(25000,17)

def original_source_project_one_exact_row():
    full,cells=original_prime_plus_pole_signed_norm_sq()
    _,u=original_even_pole_diagonal()
    k=2*u
    assert k.hi<0
    _,sin4B=trig_pi(4*C0*B)
    s0=I.rational(B)+sin4B/(2*OMEGA)
    assert F(6,5)<F(s0.lo,S)<F(s0.hi,S)<F(13,10)
    pairing=I(0)
    provenance=[]
    for a,b,p,q,flags in cells:
        ca,sa,fca,fsa=endpoint_data(a)
        cb,sb,fcb,fsb=endpoint_data(b)
        cell_width=b-a
        cos2=cell_width/2+(sb-sa)/(4*OMEGA)
        cos_sin=(ca-cb)/(4*OMEGA)
        # Exact native original signed P,Q prime cutoffs and
        # TRUE original 2u cosh pole/e mixed term on each cell.
        pairing+=2*(p*cos2+q*cos_sin+k*(fcb-fca))
        provenance.append((float(F(cell_width.lo,S)),
                           tuple((n,flags[n]) for n in (2,3,4,5,7,8,9))))
    assert F(79,100)<F(pairing.lo,S)<F(pairing.hi,S)<F(81,100)
    coefficient=pairing/s0
    assert F(3,5)<F(coefficient.lo,S)<F(coefficient.hi,S)<F(7,10)
    reduced_square=full-pairing*pairing/s0
    assert reduced_square.lo>0
    assert F(reduced_square.hi,S)<BASE_PERP_SQ_UPPER, (
        'Original genuine one-row projected prime-pole norm fails',
        reduced_square.scaled())
    return full,s0,pairing,coefficient,reduced_square,provenance

def original_complete_source_response_bound():
    full,s0,pairing,coeff,reduced,cells=original_source_project_one_exact_row()
    # The untruncated original quarter-digamma cutoff bound is
    # revalidated using EF37's full 100 original half-integer
    # coefficients and its explicit infinite remainder.
    partial,tail,whole=arch_cut_complete_l2()
    assert whole<ORIGINAL_ARCH_NORM_UPPER
    assert BASE_PERP_SQ_UPPER==F(2,5)**2
    assert F(2,5)+ORIGINAL_ARCH_NORM_UPPER==PROJECTION_NORM_UPPER
    assert ORIGINAL_ETA_UPPER==PROJECTION_NORM_UPPER**2/MU
    assert ORIGINAL_ETA_UPPER<F(105125,34)
    # Single-row projector P_e is physical orthogonal projection
    # onto exact original SI10 row. Genuine cofinite F subset e^perp.
    # The actual signed arch row a_arch(c0)e is also protected,
    # so P_F g_e=P_F[z+h_arch], with the complete original pole.
    # Contractivity+cofinite positivity yields eta<25000/17;
    # no claim it is actual eta or full 469D projection.
    return full,s0,pairing,coeff,reduced,whole,cells

def main():
    m=json.loads((ROOT/'research/obligations.json').read_text())
    assert m['active_obligation']=='W-EVEN-FORM'
    obs={x['id']:x for x in m['obligations']}
    assert all(obs[k]['status']=='open' for k in (
        'W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    assert 'EF37' in obs['W-EVEN-FORM']['evidence']
    z2,s0,p,coeff,resid,arch,cells=original_complete_source_response_bound()
    print('EF38 genuine original SI10 first source e norm²:',
          s0.scaled(),'true signed original 7-prime+pole z norm²:',
          z2.scaled(),flush=True)
    print('EF38 all ORIGINAL 8 physical cutoff cells and full 7-prime'
          ' plus true cosh pole CORRELATED signed <z,e>:',
          p.scaled(), 'actual optimal first protected-row'
          ' coefficient <z,e>/||e||²:',coeff.scaled(),flush=True)
    print('EF38 ORIGINAL first actual protected SI10 source row'
          ' one-dimensional L2 projection residual norm²:',
          resid.scaled(),'<4/25 (not full 469D projector)',flush=True)
    print('EF38 COMPLETE original quarter-digamma entire cutoff'
          ' remains L2 <3/5, original full physical signed'
          ' projected response ||P_F g_e||<1,'
          ' inherited original even cofinite eta<25000/17',
          float(ORIGINAL_ETA_UPPER),flush=True)
    print('EF38 METHOD SCOPE: genuine original 1 of 469 protected'
          ' source rows projected. Full original 469D projected'
          ' response, true q-energy inverse, eta vs EF33 S2'
          ' >1/500, and complete even PSD still OPEN.'
          ' Independent analytic Fourier/source-core audit'
          ' and paused odd/whole Weil/RH OPEN.',flush=True)

if __name__=='__main__':
    main()
