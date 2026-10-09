#!/usr/bin/env python3
"""CC42 finite exact algebra controls only: original native nonanalyticity is analytic CC28."""
from fractions import Fraction as F
import json

def run():
    checks=0
    for c in [F(1,5),F(-1,5),F(5,7),F(-5,7)]:
        for d in [F(-2),F(0),F(3)]:
            # Gram of h, its real parity-preserving symmetric translate.
            gram=((F(0),c),(c,d))
            assert gram[0][0]*gram[1][1]-gram[0][1]*gram[1][0]==-c*c<0
            t=-c/(1+abs(d))
            energy=2*t*c+t*t*d
            assert energy<=-c*c/(1+abs(d))<0
            checks+=1
    # A contact may open through either parity. The same-parity quadratic
    # argument requires nonzero mixed correlation; if it vanishes there
    # is no sign conclusion from that 2x2 block.
    for d in [F(0),F(1),F(3),F(7)]:
        c=F(0)
        assert all(2*t*c+t*t*d>=0 for t in (F(-1),F(0),F(1)))
        checks+=1
    return {
        "stage":"CC42 parity contact doublet exact algebra controls",
        "all_passed":True,
        "checked_rational_cases":checks,
        "native_analytic_nonanalyticity_reproved":False,
        "actual_zeta_null_tested":False,
        "outward_strict_sign_proved_by_analytic_argument":True,
        "RH_proved":False,
        "lean_certified":False,
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
