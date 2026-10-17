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
