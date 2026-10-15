"""RC291 — soft even signed-projection identifiability audit.

For the new rank-317 positive reference, prove that RC288's total
inverse-residual energy *upper envelope* cannot determine the signed
120-mode projection of the soft trial response P4-t P0. In particular,
both the canceling and the reversed-center hypothetical projected
residual are admissible to the PRESENT UPPER-BOUND INFORMATION.

This is a rigorously checked limitation of inherited estimates, NOT
an assertion that any hypothetical vector solves the original-source
residual equation, nor a negative original Weil direction.
"""
from pathlib import Path
from fractions import Fraction as F
import argparse
import hashlib
import json

ROOT = Path(__file__).resolve().parents[1]
B = F(11,10)
SCALE=10**20
PINS = {
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
 "certificates/rpb108_rc280_combined_jump_tail.json":"bb0dd3f6174761037ed0f20f17177ddad5749227",
 "certificates/rpb108_rc288_new_six_mode_covariance.json":"8876f15e8647072daa3bbd9919c4c3cd3354d1b6",
 "certificates/rpb108_rc289_joint_cross_bottleneck.json":"22f1551e676d23427f7891e652be9450f638ff82",
 "certificates/rpb108_rc290_soft_source_decomposition.json":"c0d90be6ea686141f088f70eb4cf3821354671be"
}

def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def gitsha(raw):return hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
def controls():
    # Given only ||x||_G^2 <= q and G<=nu D, energy constraint admits
    # signed center cancellation provided nu||z||_D^2<=q. Choosing
    # x=-2z even reverses its sign if 4nu||z||_D^2<q.
    z=F(1,10);weight=F(2);nu=F(3);q=F(1)
    assert 4*nu*weight*z*z<q
    assert z+(-z)==0 and z+(-2*z)==-z and z+(2*z)==3*z
    assert 4*nu*weight*z*z<q
    return True

def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert gitsha(raw)==pin,("input blob custody",path)
        data[path]=json.loads(raw)
    def c(s):return data["certificates/rpb108_rc"+s+".json"]
    moment=c("129_four_vector_joint_moment")
    rc278=c("278_smaller_positive_reference")
    rc280=c("280_combined_jump_tail")
    rc288=c("288_new_six_mode_covariance")
    rc289=c("289_joint_cross_bottleneck")
    rc290=c("290_soft_source_decomposition")
    assert controls()
    assert rc290["reference_rank"]==rc289["reference_rank"]==317
    assert rc289["remaining_new_rank317_Schur_dimension"]==314
    assert rc288["parity_certificates"][0]["certified_new_positive_subset"]==[0,4]
    assert rc290["original_positive_pivot_degrees"]==[0,4]
    assert not any(z["Stage_I_closed"] for z in (rc288,rc289,rc290))
    t=F(rc290["exact_soft_mixing_parameter"])
    assert F(82,100)<t<F(83,100)
    even=rc280["combined_jump_tail_gate_certificates"][0]
    trial0=[F(z) for z in even["combined_trial_tail_certificates"][0]["exact_trial_Legendre_coefficients"]]
    trial4=[F(z) for z in even["combined_trial_tail_certificates"][2]["exact_trial_Legendre_coefficients"]]
    assert len(trial0)==len(trial4)==65
    assert all(x==0 for i,x in enumerate(trial0) if i%2)
    assert all(x==0 for i,x in enumerate(trial4) if i%2)
    zsoft=[trial4[n]-t*trial0[n] for n in range(65)]
    span=list(range(0,244,2))
    rest=[n for n in span if n not in (0,4)]
    assert len(span)==122 and len(rest)==120
    assert all(n>=2 and n!=4 for n in rest)
    low_s=F(moment["actual_D_Gram_entry_lower"][0][0])/(2*B)
    high_s=F(moment["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<low_s<=high_s
    nu=F(rc278["smaller_reference_certificates"][0]["full_D_reference_upper"])
    assert nu>1
    H=[F(0)]
    for n in range(1,65):H.append(H[-1]+F(1,n))
    terms=[2*B/F(2*n+1)*(H[n]+high_s)*zsoft[n]**2 for n in rest if n<65]
    signed=[(n,zsoft[n]) for n in rest if n<65 and zsoft[n]!=0]
    if reverse:terms.reverse()
    Dcenter=up(sum((up(term) for term in terms),F(0)))
    physical=up(sum((up(2*B/F(2*n+1)*v*v) for n,v in signed),F(0)))
    assert physical>0 and Dcenter>0
    # Cross-check against RC290's *exact* projected center Gram.
    center_exact=F(rc290["orthogonalized_center_projection_Gram"][1][1])
    assert physical>=center_exact
    assert physical-center_exact<F(100,S)
    assert Dcenter>=sum(terms,F(0))
    # S_soft was not recalculated: exact congruence of the old
    # certified NEW-rank-317 2x2 full inverse-residual covariance.
    S2=[[F(v) for v in row] for row in rc289["cross_mass_certificates"][0]["correlated_residual_inverse_Gram_selected"]]
    assert len(S2)==2 and all(len(x)==2 for x in S2)
    q=up(S2[1][1]-2*t*S2[0][1]+t*t*S2[0][0])
    assert q>=F(rc290["orthogonalized_correlated_residual_Gram"][1][1])
    assert q>0
    worst_energy=up(4*nu*Dcenter)
    assert 0<worst_energy<q
    ratio=down(q/worst_energy)
    assert ratio>F(2),("sign-reversal witness not admitted by bound",ratio)
    delta=F(rc290["exact_soft_schur_pivot_native_floor"])
    lam=F(rc278["smaller_reference_certificates"][0]["augmentation_coefficient"])
    assert delta>0 and lam>0
    # The center-only cost of THIS Cauchy majorant is intrinsically
    # superunit; it does not lower bound actual cross-coupling.
    center_cost=down(lam*lam*center_exact/delta)
    assert center_cost>2
    # This numerical test is about the admissible ENERGY BALL, not
    # the exact residual equation: X=-Z or X=±2Z on the 120-mode
    # projection obey the RC288 q upper without determining X.
    return dict(
      milestone="RC291",
      parent="a967d9095e353a49bf9b998e7fa62f7578c84d51",
      input_git_blob_pins=PINS,
      reference_rank=317,
      soft_original_source="P4-t*P0",
      soft_mixing_rational=str(t),
      even_retained_rank=122,
      positive_even_pivot_degrees=[0,4],
      remaining_even_projection_rank=120,
      soft_trial_support_degree_upper=64,
      signed_nonzero_center_projection_count=len(signed),
      exact_soft_projected_physical_mass_squared=str(center_exact),
      finite_center_physical_mass_upper=str(physical),
      finite_center_D_energy_upper=str(Dcenter),
      full_reference_D_form_upper=str(nu),
      source_soft_correlated_inverse_residual_D_energy_upper=str(q),
      worst_energy_required_for_projected_signed_reversal_bound=str(worst_energy),
      residual_allowance_to_reversal_energy_ratio_lower=str(ratio),
      present_energy_bound_allows_exact_center_cancellation=True,
      present_energy_bound_allows_both_signed_reversals=True,
      hypothetical_projection_residual_coefficients={
        "canceling":"X_R=-Z_soft,R; resulting R-projected response=0",
        "reversing":"X_R=-2Z_soft,R; resulting R-projected response=-Z_soft,R",
        "amplifying":"X_R=+2Z_soft,R; resulting R-projected response=3Z_soft,R",
      },
      hypothetical_residuals_are_not_solutions_of_native_equation=True,
      no_signed_actual_inverse_response_certified=True,
      center_only_existing_Cauchy_cross_mass_lower=str(center_cost),
      existing_positive_three_pivot_block_preserved=True,
      remaining_rank317_Schur_principal_positive=False,
      Stage_I_closed=False,RH=False,F4=False,Lean=False,
      next_cursor="RC292: execute or certify original-reference operator applications to the soft residual (or a dual resolvent trial) and enclose signed projected P4-tP0 response on 120 retained even degrees. Upper energy Gram alone cannot select a sign; maintain all tail/fault covariance payments."
    )
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    out=run(args.replay)
    print("RC291_CANDIDATE="+json.dumps(out,sort_keys=True),flush=True)
    if args.replay:
        assert out==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(out,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC291 VALIDATED: signed projection unidentifiable from covariance energy alone; Stage I OPEN",flush=True)
