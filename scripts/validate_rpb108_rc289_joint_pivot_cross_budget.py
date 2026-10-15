"""RC289: paid whole-range Schur coupling for the NEW rank-317 3-pivot block.

Provides a correct but potentially very coarse mass-Loewner upper estimate
of the even P0,P4 + odd P1 Schur cross payment. Uses the full selected 2x2
correlated covariance and exact source trial coefficients from RC288/RC280.
Does NOT establish positivity of the remaining 314x314 principal Schur.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
SCALE=10**20
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc280_combined_jump_tail.json":"bb0dd3f6174761037ed0f20f17177ddad5749227",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc286_full_cross_payment.json":"bbcbe94608550c4fcb9df21dae8b2cf0d81a76c1",
 "certificates/rpb108_rc288_new_six_mode_covariance.json":"8876f15e8647072daa3bbd9919c4c3cd3354d1b6"
}
def down(x):return F(x.numerator*SCALE//x.denominator,SCALE)
def up(x):return -down(-x)
def trans(A):return [list(row) for row in zip(*A)]
def inverse(A):
    n=len(A)
    assert 1<=n<=2 and all(len(row)==n for row in A)
    assert A==trans(A)
    work=[list(row)+[F(i==j) for j in range(n)] for i,row in enumerate(A)]
    for k in range(n):
        p=work[k][k]
        assert p>0,("nonpositive inherited Schur pivot",k)
        work[k]=[v/p for v in work[k]]
        for j in range(n):
            if j!=k:
                c=work[j][k]
                work[j]=[a-c*b for a,b in zip(work[j],work[k])]
    R=[row[n:] for row in work]
    assert all(sum((A[i][k]*R[k][j] for k in range(n)),F(0))==F(i==j)
               for i in range(n) for j in range(n))
    return R
def trace(A,B):
    n=len(A)
    assert len(B)==n
    return sum((A[i][j]*B[j][i] for i in range(n) for j in range(n)),F(0))
def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        got=hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()
        assert got==pin,("immutable predecessor changed",path)
        data[path]=json.loads(raw)
    get=lambda n:data["certificates/rpb108_rc"+n+".json"]
    moment=get("129_four_vector_joint_moment")
    old=get("280_combined_jump_tail")
    reduced=get("283_reduced_reference")
    prior286=get("286_full_cross_payment")
    new=get("288_new_six_mode_covariance")
    assert new["full_new_rank317_three_by_three_covariance_both_parities_computed"]
    assert not new["Stage_I_closed"] and not prior286["Stage_I_closed"]
    slo=F(moment["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sup=F(moment["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<slo<=sup
    H=[F(0)]
    for n in range(1,66):H.append(H[-1]+F(1,n))
    sectors=[]
    for base in (0,1):
        parity=("even","odd")[base]
        current=new["parity_certificates"][base]
        oldrow=old["combined_jump_tail_gate_certificates"][base]
        ref=reduced["reduced_reference_options"][base]
        oldcross=prior286["full_cross_column_Schur_payment_certificates"][base]
        option=ref["reduced_reference_options"][1]
        assert current["parity"]==oldrow["parity"]==ref["parity"]==oldcross["parity"]==parity
        pivots=[0,4] if base==0 else [1]
        assert current["certified_new_positive_subset"]==pivots
        rank=option["new_low_reference_rank"]
        assert rank==current["reference_rank"]==(122 if base==0 else 195)
        degree_indices=[(d-base)//2 for d in pivots]
        assert current["source_degrees"]==[base,base+2,base+4]
        gam3=[[F(v) for v in row] for row in current["complete_native_six_mode_gate_lower"]]
        S3=[[F(v) for v in row] for row in current["complete_new_inverse_residual_covariance_Loewner_upper"]]
        assert len(gam3)==len(S3)==3 and all(len(row)==3 for row in gam3+S3)
        assert gam3==trans(gam3) and S3==trans(S3)
        Gamma=[[gam3[i][j] for j in degree_indices] for i in degree_indices]
        Cov=[[S3[i][j] for j in degree_indices] for i in degree_indices]
        Gi=inverse(Gamma)
        inverse(Cov) # This selected certified full covariance upper is SPD.
        lam=F(ref["parameter_lambda"])
        degrees=[base+2*k for k in range(rank)]
        remain=[n for n in degrees if n not in pivots]
        assert len(remain)==rank-len(pivots) and remain[0]==base+2
        dmin=H[base+2]+slo
        assert dmin>0
        trial=[]
        for deg in pivots:
            row=oldrow["combined_trial_tail_certificates"][(deg-base)//2]
            assert row["source"]=="P"+str(deg)
            z=[F(v) for v in row["exact_trial_Legendre_coefficients"]]
            assert len(z)==65 and all(v==0 or n%2==base for n,v in enumerate(z))
            trial.append(z)
        Gram=[[sum((2*B/F(2*n+1)*a[n]*b[n] for n in remain if n<65),F(0))
               for b in trial] for a in trial]
        assert Gram==trans(Gram)
        center=trace(Gi,Gram)
        residual=trace(Gi,Cov)/dmin
        assert center>0 and residual>0
        theta=F(7) if base==0 else F(9,4)
        charge=lam**2*((1+theta)*center+(1+1/theta)*residual)
        assert 0<charge<(F(160) if base==0 else F(3))
        centeronly=lam**2*center
        # This lower threshold is for THIS upper-bound technique's
        # unavoidable nonnegative center term, NOT the actual cross form.
        if base==0:
            assert centeronly>2
            target=None
        else:
            assert centeronly<1
            # With Young theta=1, a sufficient mass-subunit condition
            # for this method would be residual < 1/(2 lambda^2)-center.
            target=F(1)/(2*lam**2)-center
            assert 0<target<residual
            assert residual/target>5
        earlier=F(oldcross["source_response_certificates"][1]["entire_cross_Schur_payment_native_mass_strict_upper"])
        assert 0<earlier<(F(4,5) if base==0 else F(3,4))
        sectors.append(dict(
            parity=parity,positive_pivot_degrees=pivots,remaining_coordinates=len(remain),
            source_native_gate_Loewner_lower=[[str(v) for v in row] for row in Gamma],
            selected_correlated_inverse_residual_Loewner_upper=[[str(v) for v in row] for row in Cov],
            inverse_positive_native_gate_lower=[[str(v) for v in row] for row in Gi],
            reference_D_remaining_lower=str(dmin),
            physical_trial_center_mass_Gram=[[str(v) for v in row] for row in Gram],
            correlated_trial_center_trace_upper=str(up(center)),
            correlated_inverse_residual_trace_over_D_upper=str(up(residual)),
            exact_Young_parameter=str(theta),
            whole_remaining_Schur_cross_Mass_upper=str(up(charge)),
            cross_payment_below=(str(F(160)) if base==0 else str(F(3))),
            strict_upper_pass=True,
            bound_method_center_only_Mass_lower=str(down(centeronly)),
            bound_method_center_already_above_one=bool(centeronly>1),
            theta_one_subunit_required_residual_trace_upper=(str(down(target)) if target else None),
            theta_one_existing_residual_payment_insufficient=(bool(residual>target) if target else None),
            already_certified_single_P0_or_P1_cross_Mass_upper=str(earlier),
            weaker_new_joint_cross_bound_does_not_invalidate_old_single_pivot_bound=True))
    assert sum(x["remaining_coordinates"] for x in sectors)==314
    assert [F(x["whole_remaining_Schur_cross_Mass_upper"])<b for x,b in zip(sectors,[F(160),F(3)])]==[True,True]
    assert F(sectors[0]["bound_method_center_only_Mass_lower"])>2
    return dict(milestone="RC289",starting_commit="b96d942b60a725646fe71e53c2fa7980ac33b3d2",
        input_git_blob_pins=PINS,new_joint_positive_pivot_dimension=3,
        native_reduced_reference_rank=317,remaining_new_Schur_dimension=314,
        complete_three_pivot_cross_Mass_payment_certificates=sectors,
        complete_three_pivot_cross_payment_certified=True,
        remaining_314_principal_Schur_positivity_certified=False,
        subunit_new_joint_cross_payment_certified=False,
        existing_P0_and_P1_single_source_cross_bounds_preserved=True,
        new_original_Weil_actions_performed=False,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC290: target even P0/P4 trial-center geometry and near-singular 2x2 native pivot; optimize correlated source responses, not merely residual precision. Odd P1 may benefit from a ~6-fold projected covariance tightening at theta=1.")
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",required=True,type=Path)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    result=run(args.replay)
    if args.replay:assert result==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n")
    print("RC289 VALIDATED: complete new 3-pivot cross payment; Schur positivity OPEN",flush=True)
