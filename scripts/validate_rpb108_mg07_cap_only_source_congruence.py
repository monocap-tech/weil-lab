#!/usr/bin/env python3
"""W-ODD-NEG cap-only preflight simplification for V=range(J).

On the *original* SM35 470D source span, let H=J*J>0,
A_J=J*Astar J>0 and C_J=J*Kcap J>=0. The Astar-Galerkin response
Z=J A_J^{-1} H obeys Z*(J-Astar Z)=0. With theta=51/56,

theta*(Z*Astar Z) - Z*Kcap Z
= (A_J^{-1}H)^* (theta*A_J-C_J)(A_J^{-1}H).

Moreover E=(I-J H^{-1}J*)Astar J satisfies J*E=0 and\nR=-E(A_J^{-1}H). The FULL MG07 inequality is congruent to\n(1+t)C_J+(1+1/t)(Hminus/kstar)E*B14^{-1}E <= theta*A_J.\nThe strong-action residual covariance is exactly\nE*E=(Astar J)*(Astar J)-A_J H^{-1} A_J.\nTherefore cap-only feasibility on this precise trial space is equivalent
to theta*A_J-C_J>0; a certified nonpositive rational source ray rules
out this fixed cap and Galerkin trial, NOT the true signed Weil operator.
The original full 470D physical stiffness, strong-action moment, and cap are NOT evaluated.
"""
import json
from fractions import Fraction as F
from pathlib import Path
from validate_rpb108_sm35_full_original_resolvent_galerkin_enclosure import (
 ROOT,mat,transpose,mm,scale,add,sub,inv,eye,quad,
 actual_original_basis_and_cap_geometry)
from validate_rpb108_sm34_positive_energy_dual_schur import CLEAN_THRESHOLD

def strict_spd(X):
    """Exact rational strictly-positive LDL diagonal pivots."""
    n=len(X)
    assert n>0 and all(len(row)==n for row in X)
    assert all(X[i][j]==X[j][i] for i in range(n) for j in range(n))
    S=[row[:] for row in X]
    for i in range(n):
        pivot=S[i][i]
        if pivot<=0:return False
        for j in range(i+1,n):
            for k in range(j,n):
                S[k][j]-=S[i][k]*S[i][j]/pivot
        for j in range(i+1,n):
            for k in range(j+1,n):
                S[j][k]=S[k][j]
    return True

def exact_toy():
    # These are rational hypothetical 3D SOURCE GRAMS, not original data.
    H=mat([[2,F(1,3),0],[F(1,3),2,F(1,4)],[0,F(1,4),1]])
    A=mat([[3,F(1,2),0],[F(1,2),4,F(1,4)],[0,F(1,4),5]])
    C=mat([[F(1,4),F(1,12),0],
           [F(1,12),F(1,2),F(1,15)],
           [0,F(1,15),F(1,5)]])
    theta=CLEAN_THRESHOLD
    assert theta==F(51,56)
    assert all(strict_spd(X) for X in (H,A,C))
    assert mm(A,C)!=mm(C,A) # no invented simultaneous diagonalization
    Q=mm(inv(A),H)  # Z=JQ on the exact parent physical trial space
    G0=mm(mm(transpose(Q),A),Q)
    N0=mm(mm(transpose(Q),C),Q)
    T=sub(scale(theta,A),C)
    Delta=sub(scale(theta,G0),N0)
    assert Delta==mm(mm(transpose(Q),T),Q)
    assert strict_spd(T) and strict_spd(Delta)
    # For common coefficient-space slack delta, the congruence
    # preserves the relative Loewner inequality exactly.
    delta=F(1,4)
    assert strict_spd(sub(T,scale(delta,A)))
    assert strict_spd(sub(Delta,scale(delta,G0)))
    # One bad rational source-space ray rejects the *entire*
    # fixed same-space 3D Galerkin cap-only matrix regardless of
    # any later nonnegative residual charge.
    Cbad=add(C,mat([[4,0,0],[0,0,0],[0,0,0]]))
    assert strict_spd(Cbad)
    Tbad=sub(scale(theta,A),Cbad)
    v=[F(1),F(0),F(0)]
    assert quad(Tbad,v)==F(-85,56)<0
    assert not strict_spd(Tbad)
    Dbad=mm(mm(transpose(Q),Tbad),Q)
    source=mm(inv(Q),[[a] for a in v])
    y=[row[0] for row in source]
    assert quad(Dbad,y)==quad(Tbad,v)
    assert not strict_spd(Dbad)
    return {
      "matched_noncommuting_spd_case":True,
      "galerkin_congruence_exact":True,
      "normalized_slack_congruence_exact":True,
      "adverse_rational_source_ray":[str(x) for x in v],
      "adverse_cap_only_quadratic":str(quad(Tbad,v)),
      "negative_direction_not_actual_original_operator":True
    }

def complete_gate_exact_toy():
    # Exact nontrivial SI29-style feature + true in-source pole model.
    # A positive ORIGINAL-STYLE Hilbert operator, source map 4x3.
    J=mat([[1,0,0],[F(1,3),1,0],[0,F(1,4),1],[0,0,0]])
    Aop=mat([[4,F(1,3),0,F(1,5)],
             [F(1,3),3,F(1,4),F(1,7)],
             [0,F(1,4),5,F(1,11)],
             [F(1,5),F(1,7),F(1,11),2]])
    g=mat([[F(1,2)],[0],[F(1,2)],[F(1,2)]])
    pole=mat([[0],[0],[F(1,4)],[0]])  # is 1/4 of J's third column
    assert pole==scale(F(1,4),[[row[2]] for row in J])
    gamma=F(1,2);kappa=F(1)
    Cref=add(eye(4),scale(gamma,mm(g,transpose(g))))
    Bref=sub(Cref,scale(2,mm(pole,transpose(pole))))
    assert strict_spd(Bref) and strict_spd(sub(Aop,Bref))
    w=mat([[1],[2],[0],[1]])
    Kcap=add(scale(F(1,8),eye(4)),
             scale(F(1,100),mm(w,transpose(w))))
    theta=CLEAN_THRESHOLD
    assert strict_spd(Kcap)
    H=mm(transpose(J),J)
    AJ=mm(mm(transpose(J),Aop),J)
    CJ=mm(mm(transpose(J),Kcap),J)
    SJ=mm(mm(transpose(J),mm(Aop,Aop)),J)
    assert strict_spd(H) and strict_spd(AJ)
    Q=mm(inv(AJ),H)
    Z=mm(J,Q)
    R=sub(J,mm(Aop,Z))
    # E=(I-P_J) Astar J is the full source-orthogonal strong action.
    E=sub(mm(Aop,J),mm(J,mm(inv(H),AJ)))
    zero=mat([[0,0,0],[0,0,0],[0,0,0]])
    assert mm(transpose(J),E)==zero
    assert mm(transpose(E),pole)==mat([[0],[0],[0]])
    assert R==scale(-1,mm(E,Q))
    variance=sub(SJ,mm(mm(AJ,inv(H)),AJ))
    assert variance==mm(transpose(E),E)
    # Correct-sign SI29 Woodbury reference: positive-source feature
    # inverse correction NEGATIVE, conditioned pole correction POSITIVE.
    M=add([[1/gamma]],mm(transpose(g),g))
    Mi=inv(M)
    Ci=sub(eye(4),mm(mm(g,Mi),transpose(g)))
    alpha=F(1)-2*mm(mm(transpose(pole),Ci),pole)[0][0]
    assert alpha==F(39,44)>0
    Fr=mm(transpose(g),E)
    q=mm(transpose(g),pole)
    z=scale(-1,mm(mm(transpose(Fr),Mi),q))
    assert any(row[0]!=0 for row in z)
    EBE=add(sub(variance,mm(mm(transpose(Fr),Mi),Fr)),
            scale(2/alpha,mm(z,transpose(z))))
    assert EBE==mm(mm(transpose(E),inv(Bref)),E)
    DB=mm(mm(transpose(R),inv(Bref)),R)
    assert DB==mm(mm(transpose(Q),EBE),Q)
    # Full MG07 reference-weighted gate, no fictitious cancellation
    # of SI29's pole correction even though E*pole=0.
    Hneg=F(1,2);kstar=F(1);t=F(1)
    source_gate=sub(scale(theta,AJ),
        add(scale(1+t,CJ),scale((1+1/t)*Hneg/kstar,EBE)))
    trial_gate=sub(scale(theta,mm(mm(transpose(Z),Aop),Z)),
        add(scale(1+t,mm(mm(transpose(Z),Kcap),Z)),
            scale((1+1/t)*Hneg/kstar,DB)))
    assert trial_gate==mm(mm(transpose(Q),source_gate),Q)
    assert strict_spd(source_gate) and strict_spd(trial_gate)
    return {
      "complete_raw_source_gate_congruence":True,
      "strong_residual_orthogonal_to_all_sources_and_pole":True,
      "strong_action_schur_variance_exact":True,
      "strict_full_toy_source_gate":True,
      "SI29_style_Woodbury_feature_pole_response_exact":True,
      "nonzero_pole_inverse_correction_despite_orthogonal_pole":True,
      "reference_B_below_A_for_this_toy":True,
      "full_original_470_operator_data_measured":False
    }

def run():
    g=actual_original_basis_and_cap_geometry()
    assert g["source_dim"]==470 and g["cap_columns"]==890
    m=json.loads((ROOT/"research/obligations.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    odd=next(x for x in m["obligations"] if x["id"]=="W-ODD-NEG")
    assert odd["status"]=="open" and m["objective"]["status"]=="open"
    record={
      "scope":"SM35 ORIGINAL 470D J-RITZ CAP-ONLY ANALYTIC REDUCTION",
      "original_source_dimension":g["source_dim"],
      "negative_cap_columns":g["cap_columns"],
      "theta":str(CLEAN_THRESHOLD),
      "raw_original_acceptance":"theta*(J*Astar*J)-(J*Kcap*J) > 0",
      "physical_original_470_stiffness_computed":False,
      "physical_original_470_cap_gram_computed":False,
      "true_original_ray_witness_computed":False,
      "general_enlarged_trial_method_nogo":False,
      "odd_even_CC27_Weil_RH":"OPEN",
      "exact_rational_algebra_toy":exact_toy(),
      "complete_source_orthogonal_residual_toy":complete_gate_exact_toy()
    }
    print(json.dumps(record,indent=2))
    print("PASS scoped congruence: no original 470D cap-only result claimed.")

if __name__=="__main__":
    run()
