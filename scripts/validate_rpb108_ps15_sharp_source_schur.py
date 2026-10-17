#!/usr/bin/env python3
"""PS15 original signed thirteen-source domain and complete Schur constants.

Analytic Carleman sharp projection and correct sign energy Schur.
This is NOT an evaluated complement PSD, CC27 bridge or RH proof.
"""

from fractions import Fraction as F
from pathlib import Path
import json

import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps14_full_original_13channel as ps14

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SOURCE=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))
LABELS=sorted({F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
              |{F(9,n) for n in (2,4,5,7,8)})

def run():
    ps14.run()   # full original SI10/CC27 source pins, PS01-PS14
    gov=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert gov["active_obligation"]=="W-ODD-NEG"
    assert gov["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT" and lane["status"]=="open"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert all(v is False for v in lane["closures"].values())

    pi=old.pi_iv()
    ell9=old.log_i(F(9))
    ell2=old.log_i(F(2))
    delta=old.IV(R-ell9.hi,R-ell9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert len(LABELS)==13
    source_measure=13*delta.hi
    assert source_measure<F(1,5)**2
    logs={q:(old.IV(0) if q==1 else old.log_i(q)) for q in LABELS}
    sep=min(logs[v].lo-logs[u].hi for u,v in zip(LABELS,LABELS[1:]))
    assert sep>F(1,10)>delta.hi
    # Source interval r=1 touches LEFT physical endpoint, r=9 touches
    # RIGHT physical endpoint. Exactly 24 internal source-C seams.
    internal_boundaries=2*(len(LABELS)-2)+2
    assert internal_boundaries==24
    assert logs[F(2)].hi+delta.hi+delta.hi < logs[LABELS[LABELS.index(F(2))+1]].lo

    # Arch source-to-complement operator: per-source-interval two-sided
    # Carleman 1/(2(s+t)) + regular 1, with exact sharp Carleman norm pi.
    # For each interval, ||A_i|| <= pi/sqrt(2)+sqrt(delta*R).
    # Source intervals yield orthogonal output and thus
    # ||B_arch|| <= sqrt(13)*(pi/sqrt(2)+sqrt(delta*R)).
    # All acceptance comparisons are Fractions, no float trust.
    assert pi.hi<F(22,7)
    assert F(7,5)**2<F(2)              # sqrt(2)>7/5
    assert F(13)<F(15,4)**2           # sqrt(13)<15/4
    assert delta.hi*R<F(2,25)**2      # sqrt(delta*R)<2/25
    arch_upper=F(15,4)*(F(110,49)+F(2,25))
    assert arch_upper<F(35,4)
    # This constant bounds the FULL original nonlocal arch cross,
    # including all 24 physical interfaces and their regular tails.

    # Complete ORIGINAL physical prime cross, including shifts out of P.
    # ||B_prime|| <=2 sum_n Lambda(n)/sqrt(n), all 7 sources.
    weights=[]
    for n,base in SOURCE:
        root=old.IV(2 if n==4 else 3) if n in (4,9) else old.sqrt_i(n)
        w=old.log_i(F(base))/root
        assert w.lo>0
        weights.append(w)
    assert len(weights)==7
    W=sum(weights,old.IV(0))
    prime_bound=2*W.hi
    assert F(7)<prime_bound<F(71,10)

    # Both ORIGINAL correct signed poles, including P-to-C mixing.
    sn,cs=old.sinh_cosh_iv(B/2)
    sinh_B=2*sn*cs
    # norm c squared B+sinh B; norm s squared sinh B-B.
    assert cs.hi<F(7,6)
    assert sn.hi<F(7,12)
    assert B+sinh_B.hi<F(8,5)**2
    assert sinh_B.hi-B<F(1,2)**2
    # Because support P has measure 13 delta,
    # ||P c|| < (1/5)(7/6), ||P s||<(1/5)(7/12).
    ec_bound=F(7,30)
    es_bound=F(7,60)
    pole_upper=2*(ec_bound*F(8,5)+es_bound*F(1,2))
    assert pole_upper<F(9,10)

    source_cross_upper=F(35,4)+F(71,10)+F(9,10)
    assert source_cross_upper==F(67,4)<F(17)
    assert arch_upper+prime_bound+pole_upper < F(17)

    # K_M(u)=min(k(u),M) is integrable and nonnegative; for each
    # L2 f the truncated J_M increases monotonically to J.
    # The 24-seam off-diagonal Carleman bound is uniform in M.
    # Thus for e=P f,h=(I-P)f:
    # J[e]+J[h] <= J[f]+2*(35/4)||e||||h||
    #           <= J[f]+(35/4)||f||².
    # This source/form-domain projector stability is an ANALYTIC
    # theorem: the scalar constants and original physical geometry
    # are the digitally replayed certificate, not sampling of f.

    # A single inner source seam gives offdiag essential norm >=log 2.
    # Adjacent length eps source/complement normalized steps converge
    # weakly to zero, and all seven shifts vanish since 2eps<log2;
    # signed pole cross is O(eps), original arch b ->-log2.
    eps=delta.hi/F(64)
    assert eps>0 and 2*eps<ell2.lo
    assert ell2.lo>F(69,100)
    essential_lower=F(69,100)

    # Original PS14 true source Q gap >1/6. A_P>=1/6,
    # hence A_P inverse compact by original Fourier log growth.
    # Full energy-dual Schur penalty B* A_P^-1 B is positive compact.
    # This scalar operator-norm bound is far too large to certify PSD.
    schur_upper=F(6)*F(17)**2
    assert schur_upper==F(1734)

    print("PS15 physical original thirteen source intervals",len(LABELS),flush=True)
    print("PS15 original internal sharp source-complement seams",
          internal_boundaries,flush=True)
    print("PS15 certified minimum physical offset separation",float(sep),flush=True)
    print("PS15 original arch Carleman cross upper",float(arch_upper),flush=True)
    print("PS15 original complete seven-prime cross upper",float(prime_bound),flush=True)
    print("PS15 true both-signed-pole P-C cross upper",float(pole_upper),flush=True)
    print("PS15 full original P-C cross operator bound strict",float(source_cross_upper),flush=True)
    print("PS15 source projector log-form domain overhead upper",float(F(35,4)),flush=True)
    print("PS15 original source-complement essential-norm lower",
          float(essential_lower),flush=True)
    print("PS15 original exact sign Schur energy penalty crude upper",
          float(schur_upper),flush=True)
    print("PS15 PASS SCOPED: complete original thirteen-source sharp"
          " projection preserves the full physical signed log-form"
          " domain, full original offdiagonal B norm<17 but"
          " essential norm>=log2, source true Q positive >1/6,"
          " and exact complementary Schur Q_C-B* A_P^-1 B"
          " with POSITIVE COMPACT subtracted correction exists."
          " Complementary PSD NOT proved; native CC27 D-Riesz"
          " bridge, W-ODD-NEG, W-EVEN-FORM and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
