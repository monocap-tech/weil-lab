"""RC289: exact full-range cross bound for the newly positive 3-mode rank-317 block.

Preserves RC288's joint even P0/P4 and odd P1 new-reference pivots.
Reports both an exact rational certified mass majorant and a quantitative
obstruction to making that majorant subunit using only the full residual
energy trace. This is NOT a remaining-principal-form positivity claim.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
B = F(11, 10)
SCALE = 10**20
PINS = {
    "certificates/rpb108_rc129_four_vector_joint_moment.json":
        "33e681e688450c987993603354544fe3919b435f",
    "certificates/rpb108_rc280_combined_jump_tail.json":
        "bb0dd3f6174761037ed0f20f17177ddad5749227",
    "certificates/rpb108_rc283_reduced_reference.json":
        "1dc4bba375af6bfd7a274fccc07638e0eead56e6",
    "certificates/rpb108_rc288_new_six_mode_covariance.json":
        "8876f15e8647072daa3bbd9919c4c3cd3354d1b6",
    "certificates/rpb108_rc286_full_cross_payment.json":
        "bbcbe94608550c4fcb9df21dae8b2cf0d81a76c1",
}

def down(x):
    return F(x.numerator*SCALE//x.denominator,SCALE)

def up(x):
    return -down(-x)

def mass(n):
    return 2*B/F(2*n+1)

def inverse(A):
    assert A and all(len(row)==len(A) for row in A)
    if len(A)==1:
        assert A[0][0]>0
        return [[1/A[0][0]]]
    assert len(A)==2
    (a,b),(c,d)=A
    det=a*d-b*c
    assert b==c and a>0 and det>0
    return [[d/det,-b/det],[-c/det,a/det]]

def traceprod(A,B):
    assert len(A)==len(B)
    return sum((A[i][j]*B[j][i]
                for i in range(len(A)) for j in range(len(A))),F(0))

def exact_controls():
    # A positive pivot and a full-range cross upper bound do not certify
    # the remaining principal Schur form.
    gamma=F(1,2);c=F(1,3);f=F(0)
    assert c*c/gamma>0 and f-c*c/gamma<0
    # Upper envelope E(theta) = (1+theta)A+(1+1/theta)B
    # is always > B; thus lambda^2 B>1 blocks a subunit proof
    # by this *specific* positive-energy matrix Young majorant.
    a,b,lam=F(1,10),F(3,100),F(10)
    for theta in (F(1,5),F(1),F(5)):
        cost=lam*lam*((1+theta)*a+(1+1/theta)*b)
        assert cost>lam*lam*b>1
    return True

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        git=hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
        assert git==sha,("immutable dependency changed",path)
        data[path]=json.loads(raw)
    def get(k):return data["certificates/rpb108_rc"+k+".json"]
    metric=get("129_four_vector_joint_moment")
    oldtrials=get("280_combined_jump_tail")
    refs=get("283_reduced_reference")
    newgate=get("288_new_six_mode_covariance")
    oldcross=get("286_full_cross_payment")
    assert refs["proposed_buffered_reference_rank"]==317
    assert newgate["full_new_rank317_three_by_three_covariance_both_parities_computed"]
    assert oldcross["new_rank317_remaining_coupled_Schur_dimension"]==315
    assert not oldcross["Stage_I_closed"] and not newgate["Stage_I_closed"]
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<sl<=sh
    H=[F(0)]
    for k in range(1,66):H.append(H[-1]+F(1,k))
    assert exact_controls()
    result=[]
    for base in range(2):
        even=base==0
        parity=("even","odd")[base]
        picked=[0,2] if even else [0]
        pivotdegrees=[0,4] if even else [1]
        firstremaining=2 if even else 3
        row=newgate["parity_certificates"][base]
        old=oldtrials["combined_jump_tail_gate_certificates"][base]
        choice=refs["reduced_reference_options"][base]["reduced_reference_options"][1]
        prior=oldcross["full_cross_column_Schur_payment_certificates"][base]
        assert row["parity"]==old["parity"]==parity
        assert row["certified_new_positive_subset"]==pivotdegrees
        assert row["reference_rank"]==choice["new_low_reference_rank"]
        assert row["first_omitted_degree"]==choice["first_discarded_matching_degree"]
        reference_degrees=list(range(base,choice["first_discarded_matching_degree"],2))
        assert len(reference_degrees)==row["reference_rank"]
        rest=[n for n in reference_degrees if n not in pivotdegrees]
        assert len(rest)==choice["new_low_reference_rank"]-len(picked)
        assert rest[0]==firstremaining
        Gamma=[[F(row["complete_native_six_mode_gate_lower"][i][j])
                for j in picked] for i in picked]
        GI=inverse(Gamma)
        residual=[[F(row["complete_new_inverse_residual_covariance_Loewner_upper"][i][j])
                   for j in picked] for i in picked]
        inverse(residual)
        Z=[[F(x) for x in old["combined_trial_tail_certificates"][i]["exact_trial_Legendre_coefficients"]]
           for i in picked]
        assert all(len(z)==65 for z in Z)
        assert all(all(x==0 or j%2==base for j,x in enumerate(z)) for z in Z)
        center=[[sum((mass(n)*u[n]*v[n] for n in rest if n<65),F(0))
                 for v in Z] for u in Z]
        A=traceprod(GI,center)
        dmin=H[firstremaining]+sl
        Q=traceprod(GI,residual)/dmin
        assert A>0 and Q>0
        theta=F(7) if even else F(2)
        lam=F(prior["augmentation_coefficient"])
        assert lam>0
        bound=up(lam**2*((1+theta)*A+(1+1/theta)*Q))
        goal=F(159) if even else F(3)
        assert bound<goal
        floor=down(lam**2*Q)
        lower_target=F(120) if even else F(1)
        assert floor>lower_target
        result.append(dict(
            parity=parity,
            pivot_degrees=pivotdegrees,
            remaining_reference_coordinates=len(rest),
            first_remaining_degree=firstremaining,
            rank317_reference_parity_rank=choice["new_low_reference_rank"],
            positive_pivot_native_lower_matrix=[[str(x) for x in r] for r in Gamma],
            correlated_residual_inverse_Gram_selected=[[str(x) for x in r] for r in residual],
            trial_center_projection_Gram=[[str(x) for x in r] for r in center],
            rigorous_remaining_D_weight_floor=str(down(dmin)),
            Young_parameter=str(theta),
            pretrace_center_contribution=str(up(A)),
            pretrace_residual_contribution_over_D=str(up(Q)),
            collective_Schur_cross_native_mass_upper=str(bound),
            exact_strict_mass_majorant_target=str(goal),
            strict_majorant_pass=True,
            method_minimum_bound_exceeds=str(lower_target),
            variance_only_method_cost_strict_lower=str(floor),
            variance_only_cost_precludes_subunit_majorant=True,
            complete_cross_columns_covered=True,
            full_remaining_principal_gate_certified_positive=False,
        ))
    assert sum(x["remaining_reference_coordinates"] for x in result)==314
    return dict(
        milestone="RC289",
        parent="b96d942b60a725646fe71e53c2fa7980ac33b3d2",
        input_git_blob_pins=PINS,
        reference_rank=317,
        positive_native_pivot_dimension=3,
        remaining_new_rank317_Schur_dimension=314,
        selected_joint_even_positive_block=[0,4],
        selected_odd_positive_block=[1],
        cross_mass_certificates=result,
        previous_RC286_independent_single_pivot_subunit_cross_bounds_preserved=True,
        even_pivot_enlargement_does_not_inherit_RC286_cross_bound=True,
        universal_variance_only_method_cannot_prove_subunit_cross_payment=True,
        remaining_principal_block_positive=False,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC290: replace global residual-energy projection with degree-localized, source-correlated cross-Gram of inverse responses for the soft even P0/P4 direction; retain the RC286 tighter separate P0/P1 cross certificates.",
    )

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    value=run(args.replay)
    if args.replay:
        assert value==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(value,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC289 VALIDATED: 314 full cross columns bounded; "
          "variance-only method insufficient for subunit bound. Stage I OPEN.",flush=True)
