#!/usr/bin/env python3
"""NF507 exact-original source-custody symmetric-hole existence gate.

Input: NF505 4096-bit outward 242D saturated Schur JSON and NF506 local
independent posterior receipt. Output is a mathematical EXISTENCE bound
for unrestricted physical L2 corrections on almost the entire carrier,
NOT a located cell, localized repair, admissible Weil source, or RH proof.
"""
import argparse,hashlib,json
from pathlib import Path
from fractions import Fraction as F

SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NATIVE="ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec"
B=F(549,500)

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()

def toy_controls():
    # Exact finite-space projection checks for the explicit physical
    # candidate phi_j=1_(I\H_j)(W-Ja). These cannot prove original source
    # eligibility or evaluate the genuine interior cell energies.
    xs=list(map(F,(-7,-5,-3,-1,1,3,5,7)))
    cells=((0,7),(1,6),(2,5),(3,4))
    dot=lambda x,y:sum((a*b for a,b in zip(x,y)),F(0))
    n=0
    for c0,c1 in ((F(0),F(0)),(F(2),F(-7)),(F(10**12),F(-99,17))):
        W=[t*t+F(5,13)*t*t*t+c0+c1*t for t in xs]
        project=lambda w:(sum(w,F(0))/len(w),dot(xs,w)/dot(xs,xs))
        a,b=project(W)
        residual=[w-a-b*t for t,w in zip(xs,W)]
        R=dot(residual,residual)
        energies=[]
        for cell in cells:
            cap=sum((residual[k]**2 for k in cell),F(0))
            energies.append(cap)
            phi=[F(0) if k in cell else residual[k] for k in range(len(xs))]
            Wminus=[w-p for w,p in zip(W,phi)]
            av,bv=project(Wminus)
            Q=[v-av-bv*t for t,v in zip(xs,Wminus)]
            assert dot(Q,Q)<=cap
            n+=1
        assert sum(energies,F(0))==R
        assert min(energies)*len(energies)<=R
    return n

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--native",required=True)
    p.add_argument("--nf506",required=True)
    p.add_argument("--output",required=True)
    o=p.parse_args()
    n,sha=read(o.native)
    v,vsha=read(o.nf506)
    assert sha==NATIVE==v["original_native_json_sha256"]
    assert n["pass"]=="NF504-native" and v["pass"]=="NF506-local-a-posteriori"
    assert n["source_original_NF407_sha256"]==SRC
    assert n["source_original_NF406_sha256"]==SEAM
    assert n["original_selected_J_dimension"]==242
    assert n["original_exterior_center_radius"]==str(B)
    assert n["original_terminal_two_collar_delta"]=="1/500"
    assert n["original_support_saturated_physical_Hilbert_gate"]=="CERTIFIED_PHYSICAL_SUPPORT_NO_GO"
    assert v["verdict"]=="INDEPENDENT_242D_SCHUR_CONTRACTION_CERTIFIED_PHYSICAL_SUPPORT_NO_GO"
    assert v["integer_verified_inverse_Neumann_epsilon_lt_one"]
    lo,hi=map(F,n["original_original_saturated_exterior_residual_outward"])
    gamma=F(n["original_original_gamma_squared"])
    assert gamma==F(v["original_NF404_gamma_squared"]) and 0<gamma<lo<hi
    # ALL admissible physical repairs of the original O quotient must
    # eliminate strictly more than 1-gamma/R of its old squared residual.
    fraction_needed=1-gamma/lo
    assert fraction_needed>F(999,1000)
    # Mirrored partition H_j of O into m symmetric cells. Let a be the
    # exact original 242D least-squares coefficients on O, r=W-Ja.
    # sum_j ||1_Hj r||² = R(O) <= hi. Thus some H_j has at most hi/m.
    # The EXPLICIT physical correction phi_j=1_(I\Hj)r gives
    # Q_J(W-phi_j)=Q_J(1_Hj r), so its squared norm <= hi/m.
    # This requires no unknown inversion or source for the new support.
    min_m=hi//gamma+1
    assert min_m==3131
    m=4096
    h=B/m
    cap=hi/m
    assert m>=min_m and cap<gamma
    assert toy_controls()==12
    data={
       "pass":"NF507-exact-source-custody",
       "scope":"EXISTENTIAL LARGE-SUPPORT PHYSICAL L2 SUFFICIENT FEASIBILITY ONLY; hole index unknown, source eligibility OPEN",
       "original_nf505_native_sha256":sha,"original_nf506_receipt_sha256":vsha,
       "original_nf407_sha256":SRC,"original_nf406_sha256":SEAM,
       "original_source_saturated_residual_outward":[str(lo),str(hi)],
       "original_fixed_nf404_gamma_squared":str(gamma),
       "must_eliminate_residual_fraction_greater_than":str(fraction_needed),
       "must_eliminate_residual_fraction_lower_float":float(fraction_needed),
       "minimum_symmetric_partition_count_for_guaranteed_feasible_hole":int(min_m),
       "demonstration_partition_count":m,
       "symmetric_hole_one_side_width":str(h),
       "symmetric_hole_total_length":str(2*h),
       "guaranteed_some_cell_projected_residual_upper":str(cap),
       "guaranteed_some_cell_upper_over_original_gamma":str(cap/gamma),
       "guaranteed_some_cell_upper_over_gamma_float":float(cap/gamma),
       "constructive_candidate":"phi_j=1_(I minus H_j)*(W-J*a_O), a_O=G_O^(-1)*b_O",
       "which_symmetric_cell_index":"NOT_LOCATED",
       "new_reintegrated_original_physical_cell_integrals":False,
       "Weil_multiplier_image_and_graph_domain":"OPEN",
       "small_support_repair":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
       "exact_prototype_controls":12
    }
    Path(o.output).write_text(json.dumps(data,indent=2)+"\n")
    print("NF507 exact original-custody physical support-pigeonhole gate PASS")
    print("Need remove >",float(fraction_needed),"of saturated residual power (not support measure).")
    print("Mirrored cell count >=",min_m,"; demonstration m",m)
    print("Some unlocated physical hole total length",float(2*h),
          "gives squared residual <= gamma² ×",float(cap/gamma))
    print("No source-range/domain eligibility, located correction, Weil sign, or RH claim.")

if __name__=="__main__":
    main()
