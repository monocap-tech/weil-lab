"""RC290: exact soft pivot source direction within RC288 rank-317 even gate.

Only algebra of certified rational native gate lower matrix and already
correlated source response Grams. The soft mixed source is P4-t*P0,
t=Gamma_lo[0,1]/Gamma_lo[0,0]. It is not an actual eigenvector claim.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
S=10**20
PINS={
 "certificates/rpb108_rc289_joint_cross_bottleneck.json":"22f1551e676d23427f7891e652be9450f638ff82",
 "certificates/rpb108_rc288_new_six_mode_covariance.json":"8876f15e8647072daa3bbd9919c4c3cd3354d1b6"
}
def down(x):return F(x.numerator*S//x.denominator,S)
def up(x):return -down(-x)
def tran(M):return [list(v) for v in zip(*M)]
def multiply(A,B):return [[sum((A[i][k]*B[k][j] for k in range(len(B))),F(0))
                         for j in range(len(B[0]))] for i in range(len(A))]
def rmat(rows):return [[F(v) for v in row] for row in rows]
def run(reverse=False):
    files={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        got=hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
        assert got==sha,("pin",path)
        files[path]=json.loads(raw)
    record=files["certificates/rpb108_rc289_joint_cross_bottleneck.json"]
    parent=files["certificates/rpb108_rc288_new_six_mode_covariance.json"]
    assert record["reference_rank"]==317 and record["remaining_new_rank317_Schur_dimension"]==314
    assert parent["full_new_rank317_three_by_three_covariance_both_parities_computed"]
    assert record["Stage_I_closed"] is False and parent["Stage_I_closed"] is False
    section=record["cross_mass_certificates"][0]
    assert section["parity"]=="even" and section["pivot_degrees"]==[0,4]
    assert section["remaining_reference_coordinates"]==120
    gam=rmat(section["positive_pivot_native_lower_matrix"])
    center=rmat(section["trial_center_projection_Gram"])
    residual=rmat(section["correlated_residual_inverse_Gram_selected"])
    assert all(len(v)==2 for v in gam+center+residual)
    assert all(M==tran(M) for M in (gam,center,residual))
    a,b=gam[0]
    assert gam[1][0]==b
    c=gam[1][1]
    assert a>0
    t=b/a
    delta=c-b*b/a
    assert F(82,100)<t<F(83,100)
    assert 0<delta<a/F(180)
    T=[[F(1),-t],[F(0),F(1)]]
    canonical=multiply(tran(T),multiply(gam,T))
    assert canonical==[[a,F(0)],[F(0),delta]]
    # The mixed direction is P4-tP0, where t is defined using a
    # *certified Loewner lower*, not necessarily actual orthogonality.
    def split(M):
        v00=M[0][0]
        soft=M[1][1]-2*t*M[0][1]+t*t*M[0][0]
        assert v00>0 and soft>0
        mt=multiply(tran(T),multiply(M,T))
        assert mt[1][1]==soft
        return v00,soft,mt
    A0,As,Anew=split(center)
    S0,Ss,Snew=split(residual)
    d=F(section["rigorous_remaining_D_weight_floor"])
    lam=F(files["certificates/rpb108_rc288_new_six_mode_covariance.json"]["parity_certificates"][0]["reference_D_floor_lower"])
    assert d>lam>0
    # Invariance of trace of Gamma^-1 times any covariance/Gram.
    C_h=A0/a
    C_soft=As/delta
    R_h=S0/(a*d)
    R_soft=Ss/(delta*d)
    total_C=C_h+C_soft
    total_R=R_h+R_soft
    Ginv=[[c/(a*delta),-b/(a*delta)],[-b/(a*delta),F(1)/delta]]
    direct_C=sum((Ginv[i][j]*center[j][i] for i in range(2) for j in range(2)),F(0))
    direct_R=sum((Ginv[i][j]*residual[j][i] for i in range(2) for j in range(2)),F(0))/d
    assert total_C==direct_C and total_R==direct_R
    assert 0<total_C<=F(section["pretrace_center_contribution"])
    assert 0<total_R<=F(section["pretrace_residual_contribution_over_D"])
    assert total_C-C_h==C_soft and total_R-R_h==R_soft
    center_share=C_soft/total_C
    residual_share=R_soft/total_R
    assert center_share>F(9,10)
    assert residual_share>F(99,100)
    amp=a/delta
    assert amp>180
    # This source-specific trial-center term ALONE already defeats a
    # mass-subunit estimate of the present variance-sum type. This is
    # not a lower bound on the actual cross Schur operator.
    # Recover source coefficient from the parent native response.
    lam_aug=F(section["variance_only_method_cost_strict_lower"])
    assert lam_aug>120
    return dict(
      milestone="RC290",
      parent="765e64555d2a1012f1eb1898c1af5269ce66a7d0",
      input_git_blob_pins=PINS,
      reference_rank=317,
      original_positive_pivot_degrees=[0,4],
      exactly_diagonalized_native_gate_Loewner_lower=[[str(v) for v in row] for row in canonical],
      mixed_source="P4-t*P0 (on original physical Legendre inputs)",
      exact_soft_mixing_parameter=str(t),
      exact_hard_pivot_native_floor=str(a),
      exact_soft_schur_pivot_native_floor=str(delta),
      hard_to_soft_pivot_floor_ratio_lower=str(down(amp)),
      orthogonalized_center_projection_Gram=[[str(v) for v in row] for row in Anew],
      orthogonalized_correlated_residual_Gram=[[str(v) for v in row] for row in Snew],
      decomposed_center_trace=dict(hard=str(up(C_h)),soft=str(up(C_soft)),
          total=str(up(total_C)),soft_share_lower=str(down(center_share))),
      decomposed_inverse_residual_trace_over_D=dict(hard=str(up(R_h)),soft=str(up(R_soft)),
          total=str(up(total_R)),soft_share_lower=str(down(residual_share))),
      strict_center_soft_share_above_nine_tenths=True,
      strict_residual_soft_share_above_ninety_nine_hundredths=True,
      original_six_source_trial_polynomials_unchanged=True,
      actual_Weil_action_newly_computed=False,
      residual_projected_soft_direction_computed=False,
      full_314_Schur_principal_positive=False,
      Stage_I_closed=False,RH=False,F4=False,Lean=False,
      next_cursor="RC291: calculate signed projected new-reference inverse response of P4-tP0 against all 120 retained rest modes. Current nonnegative center+variance bound cannot exploit cancellation; do not extrapolate old reference covariances."
    )
if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",required=True,type=Path)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text(encoding="utf-8"))
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("RC290 VALIDATED: exact soft-mode concentration; Stage I OPEN",flush=True)
