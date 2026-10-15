"""RC285: degree-localize reduced-reference P0/P1 original-source inverse correction.

RC274 actual original source output intervals and infinite tail are reused
without new original Weil actions. Exact rational cuts implement RC278's
rescaled trial under RC283's rank-301/317/334 positive references.
"""
import argparse, hashlib, json
from fractions import Fraction as F
from pathlib import Path

ROOT=Path(__file__).resolve().parents[1]
PINS={
 "certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc274_mixed_diagonal_inverse.json":"2059b48ee4e0b22a0dfb8a9a803644cf0c5fb5f8",
 "certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
 "certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
 "certificates/rpb108_rc284_reduced_source_transfer.json":"bc80e1fb9168f5aaf0b69e57a47b95f02c8739a6"
}
B=F(11,10)
SCALE=10**20
YOUNG=F(1,100)
def down(v):return F(v.numerator*SCALE//v.denominator,SCALE)
def up(v):return -down(-v)
def energy_normalized(n,bound,dl):
    return up(F(2)*B*bound*bound/(2*n+1)/dl)

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==sha,("pin",path)
        data[path]=json.loads(raw)
    def get(k):return data["certificates/rpb108_rc"+k+".json"]
    metric=get("129_four_vector_joint_moment")
    old274=get("274_mixed_diagonal_inverse")
    old278=get("278_smaller_positive_reference")
    red=get("283_reduced_reference")
    coarse=get("284_reduced_source_transfer")
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    assert 0<sl<=sh
    H=[F(0)]
    for n in range(1,2053):H.append(H[-1]+F(1,n))
    dlo=[down(h+sl) for h in H]
    dhi=[up(h+sh) for h in H]
    records=[]
    for base in range(2):
        r274=old274["projection_mixed_inverse_response_certificates"][base]
        r278=old278["smaller_reference_certificates"][base]
        r283=red["reduced_reference_options"][base]
        r284=coarse["certified_source_response_transfer"][base]
        parity=("even","odd")[base]
        assert r274["parity"]==r278["parity"]==r283["parity"]==r284["parity"]==parity
        lam=F(r278["augmentation_coefficient"])
        t=F(r278["exact_trial_scale"])
        centers=r278["retained_low_residual_certificate"]
        assert len(centers)==65
        assert len(r274["residual_physical_numerator_intervals_65_through_2048"])>900
        assert lam==F(r278["physical_negative_allowance_C"])
        lo_terms=[]
        for c in centers:
            n=c["degree"];value=F(c["residual_center"])
            lo_terms.append(up(F(2)*B*dhi[n]*value*value/(2*n+1)))
        numerator={}
        for v in r274["residual_physical_numerator_intervals_65_through_2048"]:
            n=v["degree"]
            assert 65<=n<=2048 and n%2==base and n not in numerator
            numerator[n]=max(abs(F(v["lower"])),abs(F(v["upper"])))
        expected=list(range(66 if base==0 else 65,2049,2))
        assert sorted(numerator)==expected
        tail=F(r274["complete_full_trial_model_tail_D_energy_upper"])
        firsttail=2050 if base==0 else 2049
        mu_old=F(r278["full_D_reference_floor_lower"])
        # Reverse check: old model budget is a validated upper envelope of
        # its exact coefficients, parity tail and same rational scaling.
        old_first=r278["first_omitted_degree"]
        old_terms=list(lo_terms)
        for n in expected:
            w=F(1) if n<old_first else down(1-lam/dlo[n])
            assert w>=mu_old
            old_terms.append(up(t*t*energy_normalized(n,numerator[n],dlo[n])/w))
        old_tailweight=down(1-lam/dlo[firsttail])
        old_model=up(sum(old_terms,F(0))+up(t*t*tail/old_tailweight))
        assert old_model<=F(r278["complete_model_weighted_inverse_energy_upper"]),("old model mismatch",base)
        source_mass=F(r278["native_auxiliary_source_mass"])
        centerhi=F(r278["variational_inverse_center_upper"])
        radius=F(r278["weighted_source_and_center_rounding_energy_upper"])
        faultnorm=F(r278["remaining_global_D_fault_norm_upper"])
        models=[]
        for o,coarse_row in zip(r283["reduced_reference_options"],r284["new_reference_response_enclosures"]):
            first=o["first_discarded_matching_degree"]
            mu=F(o["certified_D_reference_floor_lower"])
            assert first>65 and coarse_row["new_reference_rank"]==o["new_low_reference_rank"]
            assert mu<=down(1-lam/dlo[first]) and mu>0
            segments=[sum(lo_terms,F(0)),F(0),F(0)]
            for n in (reversed(expected) if reverse else expected):
                w=F(1) if n<first else down(1-lam/dlo[n])
                assert w>=mu
                e=up(t*t*energy_normalized(n,numerator[n],dlo[n])/w)
                if n<first:segments[1]+=e
                else:segments[2]+=e
            tail_w=down(1-lam/dlo[firsttail])
            assert tail_w>=mu
            tail_new=up(t*t*tail/tail_w)
            model=up(sum(segments,F(0))+tail_new)
            fault=up(faultnorm*faultnorm/mu)
            correction=up((1+YOUNG)*model+2*(1+1/YOUNG)*(radius+fault))
            responsehi=up(centerhi+correction)
            gate=down(source_mass-lam*responsehi)
            assert model<=F(coarse_row["new_complete_model_inverse_correction_upper"]),("no localization improvement",base,first)
            assert gate>=F(coarse_row["actual_native_source_gate_lower"]),("new gate worsened",base,first)
            models.append(dict(
                rank=o["new_low_reference_rank"],
                first_omitted_degree=first,
                low_0_64_model_energy_upper=str(up(segments[0])),
                retained_65_to_cutoff_model_energy_upper=str(up(segments[1])),
                omitted_cutoff_to_2048_model_energy_upper=str(up(segments[2])),
                infinite_tail_model_energy_upper=str(tail_new),
                complete_model_inverse_energy_upper=str(model),
                complete_global_fault_payment_upper=str(fault),
                complete_original_inverse_residual_correction_upper=str(correction),
                original_source_inverse_response_upper=str(responsehi),
                native_gate_lower=str(gate),
                positive_native_pivot_certified=gate>0,
                model_improves_RC284=True,
                all_degree_residual_intervals_paid=True,
                infinite_original_tail_paid=True))
        records.append(dict(parity=parity,source="P"+str(base),
            rescaled_original_trial_factor=str(t),
            original_degree_intervals_count=len(expected),
            old_reference_model_reconstruction_upper=str(old_model),
            source_rounding_energy_upper=str(radius),
            global_D_fault_norm_upper=str(faultnorm),
            parity_certificates=models))
    outcome=dict(
        milestone="RC285",
        parent="17c5900dec38469eb18d4a54e564c7668ab371a2",
        input_git_blob_pins=PINS,
        degree_localized_original_source_certificates=records,
        cross_reference_old_pivots_not_assumed=True,
        full_rank317_gate_certified=False,
        new_original_Weil_actions_performed=False,
        all_RC274_actual_original_outputs_and_infinite_tails_paid=True,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC286: extend localized source gates to same-parity mixed P0,P2,P4 and P1,P3,P5 trials in rank-317 new reference, then certify full correlations."
    )
    return outcome

if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--replay",action="store_true")
    args=ap.parse_args()
    result=run(args.replay)
    # CANDIDATE is printed on purpose while constructing the initial
    # certificate; remove print before the production checkpoint merge.
    print("RC285_CANDIDATE_JSON="+json.dumps(result,sort_keys=True),flush=True)
    if args.replay:
        assert result==json.loads(args.output.read_text(encoding="utf-8"))
    else:
        args.output.write_text(json.dumps(result,sort_keys=True,indent=2)+"\n",encoding="utf-8")
    print("RC285 VALIDATED: degree-localized source transfer; Stage I OPEN",flush=True)
