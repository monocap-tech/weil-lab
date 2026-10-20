#!/usr/bin/env python3
"""MG17A: exact original non-flat positive-multiplier pilot-site scout.

MG16 established that all 24 previous original physical source panels
had TRUE a_o(xi)=kappa, so multiplier-weighted J0,J1,J2 cannot differ
from MG15 there. This script searches a reproducible rational grid of
NEW frequency locations and certifies, without sampled trigonometry,
the opposite regime: a_o(xi)>kappa throughout every selected panel,
and strictly nonconstant true a_o on the panel, witnessed by
DISJOINT original signed endpoint intervals.

Crucial: this is only panel discovery and a method viability gate.
No original source moment, complete low band, Galerkin residual,
470D inverse, even, Weil or RH result follows from scouting.
"""
import argparse,json
from fractions import Fraction as F
from validate_rpb108_mg16_weighted_affine_source_moments import (
    ROOT,original_source_centered_windows,affine_cell_error,
    moments_reference,positive_cell_weight_interval,
    arch_lower_at,arch_upper_at,prime_interval,KAPPA
)

def candidates():
    bases=(F(2),F(3),F(4),F(6),F(8),F(12),
           F(16),F(24),F(32),F(48),F(64),F(96),F(128))
    offsets=(F(0),F(1,8),F(1,4),F(3,8),
             F(1,2),F(5,8),F(3,4),F(7,8))
    for base in bases:
        for off in offsets:
            a=base+off;b=a+F(1,64)
            yield a,b

def scout():
    centers,sources,_=original_source_centered_windows()
    assert len(sources)==25
    selected=[];examined=0
    counts={"endpoint_disjoint":0,"entire_cell_above_kappa":0,
            "affine_reference_chosen":0,
            "nonzero_weight_first_moment":0}
    for a,b in candidates():
        examined+=1
        al=arch_lower_at(a)+prime_interval(a)[0]
        au=arch_upper_at(a)+prime_interval(a)[1]
        bl=arch_lower_at(b)+prime_interval(b)[0]
        bu=arch_upper_at(b)+prime_interval(b)[1]
        assert al<=au and bl<=bu
        separate=(au<bl or bu<al)
        counts["endpoint_disjoint"]+=int(separate)
        if not separate:continue
        low,high,info=positive_cell_weight_interval(a,b)
        above=low>KAPPA
        counts["entire_cell_above_kappa"]+=int(above)
        if not above:continue
        eps,meta=affine_cell_error(a,b,centers,sources)
        affine=meta["reference_choice"]=="signed_positive_part_affine"
        counts["affine_reference_chosen"]+=int(affine)
        if not affine:continue
        moments,_=moments_reference(a,b,centers,sources)
        j1=moments[1][0][1]
        nonzero=j1!=0
        counts["nonzero_weight_first_moment"]+=int(nonzero)
        if not nonzero:continue
        selected.append({
            "left":str(a),"right":str(b),
            "endpoint_original_signed_intervals":[[str(al),str(au)],[str(bl),str(bu)]],
            "certified_multiplier_lower":str(low),
            "certified_multiplier_upper":str(high),
            "original_true_above_kappa_entire_panel":True,
            "true_multiplier_nonconstant_endpoint_witness":True,
            "reference_affine_selected":True,
            "reference_J1_nonzero":True,
            "reference_weight_J1":str(j1),
            "signed_multiplier_reference_error":str(meta["exact_curvature_error"])
        })
        if len(selected)>=24:break
    return {"status":"ORIGINAL_NONFLAT_MULTIPLIER_PANEL_SCOUT",
            "canonical_W_ODD_NEG":"OPEN",
            "actual_original_25_source_catalog_replayed":True,
            "candidate_panels_examined":examined,
            "certification_stage_counts":counts,
            "selected_nonflat_original_cells":selected,
            "selected_cell_count":len(selected),
            "every_selected_cell_proves_original_true_nonconstancy":True,
            "every_selected_cell_true_positive_multiplier_strictly_above_floor":True,
            "selected_cells_disjoint":all(
                F(selected[i]["right"])<F(selected[i+1]["left"])
                for i in range(len(selected)-1)),
            "complete_original_low_band_certified":False,
            "original_Astar_squared_and_Galerkin_residual_certified":False,
            "full_original_470_odd_inverse":"OPEN",
            "even_Weil_CC27_RH":"OPEN",
            "independent_Fourier_and_domain_audit":"OPEN"}
def main():
    p=argparse.ArgumentParser()
    p.add_argument("--output",default="artifacts/mg17_original_nonflat_multiplier_scout.json")
    opts=p.parse_args()
    d=scout()
    out=ROOT/opts.output
    out.parent.mkdir(parents=True,exist_ok=True)
    out.write_text(json.dumps(d,indent=2)+"\n")
    print("MG17 original nonflat multiplier scout:",json.dumps({
        "examined":d["candidate_panels_examined"],
        "selected":d["selected_cell_count"],
        "stages":d["certification_stage_counts"],
        "selected_short":[(x["left"],x["right"]) for x in d["selected_nonflat_original_cells"][:8]],
        "complete_odd_even_Weil_RH":"OPEN"
    }),flush=True)
    assert len(d["selected_nonflat_original_cells"])>=8,(
        "MG17 SCOUT METHOD GATE: fewer than eight rigorously verified "
        "nonconstant original multiplier panels; redesign search")
if __name__=="__main__":
    main()
