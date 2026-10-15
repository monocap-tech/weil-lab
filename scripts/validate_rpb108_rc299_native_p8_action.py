"""RC299: extend the generic native signed Weil original action to even P8.

Build a fifth independently evaluated even input column, retaining all
regular, pole, prime and endpoint pieces and the original omitted-output
energy. This is a low-output (n<=64) construction only, NOT a complete
2048-mode action, arbitrary input evaluator, or RC292 inverse proof.
"""
import argparse
import base64
import hashlib
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

import validate_rpb108_rc240_three_trial_signed_response as legacy

ROOT=Path(__file__).resolve().parents[1]
B=F(11, 10)
o=legacy.orig
up=legacy.up
down=legacy.down
root=legacy.root

PINS={
 "certificates/rpb108_rc43_native_prime_head.json":
  "b4893953109e6fdc55d52b505c2bcfbf0d38281e",
 "certificates/rpb108_rc46_native_archimedean_head.json":
  "be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
 "certificates/rpb108_rc129_four_vector_joint_moment.json":
  "33e681e688450c987993603354544fe3919b435f",
 "certificates/rpb108_rc240_three_trial_signed_response.json":
  "6c41b7f196052fea179b956099fb69cc5d07813c",
 "certificates/rpb108_rc296_native_p6_action.json":
  "ff03088daa67d681e0371e92c40576d8c3219b4b",
 "certificates/rpb108_rc298_four_column_dual_obstruction.json":
  "609eb6c0a411f0f171b4704d952309b5d906f85d",
 "scripts/validate_rpb108_rc237_two_trial_signed_response.py":
  "d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
 "scripts/validate_rpb108_rc240_three_trial_signed_response.py":
  "9e1f46907a3c96d2f916d709163d0dea0db5190a",
 "scripts/validate_rpb108_rc296_native_p6_action.py":
  "e0707fde1acc8cb12af9e54cf4aad6f15ed154df",
}

def run_original(d,reg,prime,eps,sl,sh,reverse=False):
    """Degree-parameterized RC296 original action, with finite cutoff 64."""
    assert d in (4,6,8)
    assert 65>3*d+1 and sl>0 and sl<=sh
    regpoly=legacy.trial.regular_poly(d,reg)
    rc=[o.project(regpoly,n) for n in range(len(regpoly))]
    pc,pt,pfault,segs=legacy.trial.prime_poly(d,prime,reverse)
    assert len(pc)==65 and len(segs)==15
    rtail=up(sum((o.mass(n)*v*v for n,v in enumerate(rc) if n>64),F(0)))
    phi=[F(11,20)**k/factorial(k) if k%2==d%2 else F(0)
         for k in range(41)]
    moment=B*o.integral(o.product(o.legendre(d),phi))
    pole=[2*(-1)**d*moment*v for v in phi]
    oc=[o.project(pole,n) for n in range(65)]
    tau=2*F(11,20)**41/factorial(41)
    polefault=up(16*B*tau*root(o.mass(d)))
    ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1)
              for k in range(100)),F(0))
    lh=ll+2*F(1,3)**201/(201*(1-F(1,9)))
    out=[]
    rnd=F(0)
    for n in range(65):
        if n%2!=d%2:
            out.append(dict(degree=n,coefficient="0",radius="0"))
            continue
        h=(2*o.H(2*n)-2*o.H(n)+F(1,2*n+1)) if n==d else F(
            2*n+1,abs(n-d)*(n+d+1))
        lo=h-(lh if n==d else 0)-rc[n]+pc[n]+oc[n]-(
            F(789,125) if n==d else 0)
        hi=h-(ll if n==d else 0)-rc[n]+pc[n]+oc[n]-(
            F(789,125) if n==d else 0)
        vals=[q/(o.H(n)+s)+F(n==d)
              for q in (lo,hi) for s in (sl,sh)]
        c=down((min(vals)+max(vals))/2)
        radius=max(c-min(vals),max(vals)-c)
        rnd+=o.mass(n)*(o.H(n)+sh)*radius*radius
        out.append(dict(degree=n,coefficient=str(c),radius=str(up(radius))))
    first=66
    comp=dict(
      finite_rounding=up(rnd),
      endpoint_omitted_output=up(3*B/((o.H(first)+sl)*(64-d)**2)),
      regular_omitted_output=up(rtail/(o.H(first)+sl)),
      prime_omitted_output=up(pt/(o.H(first)+sl)),
      regular_kernel=up((2*B*eps)**2*o.mass(d)/sl),
      prime_arithmetic=up(pfault**2/sl),
      pole_Taylor=up(polefault**2/sl))
    total=up(sum((root(v) for v in comp.values()),F(0))**2)
    assert total>0 and all(x>=0 for x in comp.values())
    assert all(v["coefficient"]=="0" and v["radius"]=="0"
               for v in out if v["degree"]%2)
    return dict(input="P"+str(d),input_degree=d,parity="even",
       finite_original_D_action=out,
       D_energy_component_squared_errors={k:str(v) for k,v in comp.items()},
       complete_original_action_D_error_squared_upper=str(total),
       original_output_cutoff=64,
       first_omitted_even_degree=first,
       complete_active_prime_pairs=7,
       all_omitted_outputs_paid=True)

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        digest=hashlib.sha1(b"blob "+str(len(raw)).encode()+b"\0"+raw).hexdigest()
        assert digest==sha,(path,"imported input pin changed")
        if path.endswith(".json"):data[path]=json.loads(raw)
    def get(x):return data["certificates/rpb108_rc"+x+".json"]
    prior=get("298_four_column_dual_obstruction")
    assert prior["four_column_universal_RC292_acceptance_exclusion_for_both"]
    moment=get("129_four_vector_joint_moment")
    sl=F(moment["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(moment["actual_D_Gram_entry_upper"][0][0])/(2*B)
    arch=get("46_native_archimedean_head")
    reg=list(map(F,arch["regular_kernel_coefficients"]))
    eps=F(arch["regular_kernel_uniform_error_upper"])
    prime=get("43_native_prime_head")
    assert len(prime["active_prime_powers"])==7
    old4=get("240_three_trial_signed_response")[
        "parity_three_trial_signed_response_certificates"][0][
        "new_complete_original_action"]
    old6=get("296_native_p6_action")["new_native_P6_original_action"]
    # Regression through independent generic evaluator: all 65 values
    # and every error component must agree identically for P4 and P6.
    same=("finite_original_D_action",
          "D_energy_component_squared_errors",
          "complete_original_action_D_error_squared_upper")
    for degree,previous in ((4,old4),(6,old6)):
        candidate=run_original(degree,reg,prime,eps,sl,sh,reverse)
        assert all(candidate[k]==previous[k] for k in same), (
            degree,"native formula regression")
        print("RC299: P"+str(degree)+" exact full low-output regression passed",
              flush=True)
    new=run_original(8,reg,prime,eps,sl,sh,reverse)
    assert len(new["finite_original_D_action"])==65
    assert new["finite_original_D_action"][8]["coefficient"]!="0"
    assert F(new["complete_original_action_D_error_squared_upper"])>0
    print("RC299: computed independent P8 original input action to degree 64",
          flush=True)
    return dict(
       milestone="RC299",
       starting_commit="acb7ce39ff7f354fcc4e155870eb0a4bc5ddaa94",
       input_git_blob_pins=PINS,
       P4_full_low_original_action_regression_exact=True,
       P6_full_low_original_action_regression_exact=True,
       new_native_P8_original_action=new,
       new_original_Weil_input_degree=8,
       original_P8_active_prime_pairs_all_paid=True,
       original_P8_complete_degree_64_output_and_omitted_tail_paid=True,
       original_input_action_degrees_now_available_low_cutoff=[0,2,4,6,8],
       P8_output_degrees_65_through_2048_available=False,
       rank317_augmented_P8_action_available=False,
       five_column_RC292_inverse_seed_certified=False,
       full_operator_arbitrary_input_action_available=False,
       stage_I_status="OPEN",Stage_I_closed=False,RH=False,F4=False,Lean=False,
       next_cursor=(
         "RC300: project P8 original prime and analytic endpoint output "
         "through degree 2048, preserve the infinite tail, attach the "
         "rank317 augmentation at output n=8, and test the five-column "
         "input family with paid dual obstructions.")
    )

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("--output",type=Path,required=True)
    p.add_argument("--replay",action="store_true")
    args=p.parse_args()
    result=run(args.replay)
    payload=json.dumps(result,sort_keys=True,indent=2)+"\n"
    if args.replay:
        if payload!=args.output.read_text(encoding="utf-8"):
            # Bootstrap aid: expose computed candidate only on a failed
            # replay, never silently accept a missing/changed certificate.
            print("RC299_PROPOSED_CERT_BASE64="+base64.b64encode(
                payload.encode()).decode(),flush=True)
            raise AssertionError("RC299 stored certificate does not equal evaluated action")
    else:
        args.output.write_text(payload,encoding="utf-8")
    print("RC299 VALIDATED: fifth native P8 low-output action; Stage I OPEN",
          flush=True)
