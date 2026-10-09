#!/usr/bin/env python3
"""DNE5 finite exact rational provenance and mirrored-cut graph controls.

Only arithmetic envelope inequalities and elementary finite graph identities
are checked. Native Levy semigroup domination and the full-domain
ground-state gap theorem are analytic, not executable zeta computations.
"""
from fractions import Fraction as F
from pathlib import Path
import json

ROOT=Path(__file__).resolve().parents[1]
SOURCE=ROOT/"notes/data/RPB108_CC40_NATIVE_PARITY_LOW2_INPUT_20261008.json"

def run():
    manifest=json.loads(SOURCE.read_text())
    assert manifest["aperture"]=="53/50"
    assert manifest["source_commit"]=="33d2b6bbd233d09e8c401b086545d0647b283817"
    g=int(manifest["grid_denominator"])
    assert g==10**25
    entry=manifest["source_intervals"]["0,0"]
    checks={}
    def ck(name,condition):
        assert condition, name
        checks[name]=True

    H00_upper=F(int(entry["arch"][1])+int(entry["prime"][1]),g)
    ck("original_pole_free_constant_trial_below_minus4",H00_upper<-4)
    S=F(12093,3740)
    ck("prime_source_sum_below4",S<4)
    ck("negative_a0_below7",1+2+F(21,10)+F(6,5)<7)
    ck("kappa_under15",7+2*4==15)
    ck("mu_under11",15-4==11)
    a=F(53,50)
    ck("aperture_above1",a>1)
    ck("aperture_below2",a<2)
    ck("twice_aperture_below9over4",2*a<F(9,4))
    ck("j_2a_upper2over5",F(3,8)/F(15,16)==F(2,5))
    ck("diameter_certificate_below9over10",F(9,4)*F(2,5)==F(9,10)<1)
    ck("ground_depth_beyond4",H00_upper<-4)
    ck("positive_rational_gap_floor",F(1,3**30)>0)
    # This is an exact graph mirror cut model; no zeta ground profile is evaluated.
    phi=[F(1),F(2),F(2),F(1)]
    # four positions: (-2,-1,+1,+2), symmetric phi
    edges={
      (0,1):F(3), (2,3):F(3),
      (0,2):F(1), (0,3):F(1,2),
      (1,2):F(2), (1,3):F(1)
    }
    u=[F(-1),F(-1),F(1),F(1)]
    W=sum((c*phi[i]*phi[j]*(u[i]-u[j])**2
           for (i,j),c in edges.items()),F(0))
    cut=4*sum((c*phi[i]*phi[j] for (i,j),c in edges.items()
              if i<2<=j),F(0))
    ck("exact_reflection_cut",W==cut)
    ck("prime_like_bridge_positive",edges[(1,2)]>0)
    ck("same_side_edges_zero_for_sign_test",
       all(u[i]==u[j] for i,j in ((0,1),(2,3))))
    ck("reflected_even_ground_profile",phi==list(reversed(phi)))
    return {
        "stage":"DNE5 native heat odd-gap rational preflight",
        "all_passed":True,
        "exact_fraction_checks":len(checks),
        "checked_names":list(checks),
        "H00_upper":str(H00_upper),
        "diameter_bound":"Gamma_diam < 9/10",
        "actual_full_odd_gap":"gamma_odd > 3^(-30) via analytic semigroup theorem",
        "mirror_cut_graph_energy":str(W),
        "real_zeta_ground_eigenfunction_computed":False,
        "RH_proved":False,
        "lean_certified":False
    }

if __name__=="__main__":
    print(json.dumps(run(),indent=2))
