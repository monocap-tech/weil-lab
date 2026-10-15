"""RC296: extend exact RC240 original Legendre action to new P6 input."""
from fractions import Fraction as F
from pathlib import Path
from math import factorial
import argparse,hashlib,json
import validate_rpb108_rc240_three_trial_signed_response as legacy
ROOT=Path(__file__).resolve().parents[1];B=F(11,10);o=legacy.orig
up=legacy.up;down=legacy.down;root=legacy.root
PINS={
"certificates/rpb108_rc43_native_prime_head.json":"b4893953109e6fdc55d52b505c2bcfbf0d38281e",
"certificates/rpb108_rc46_native_archimedean_head.json":"be1a1a4ef8a6cfb41b96a8c29e72aa5f102298c9",
"certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
"certificates/rpb108_rc240_three_trial_signed_response.json":"6c41b7f196052fea179b956099fb69cc5d07813c",
"scripts/validate_rpb108_rc237_two_trial_signed_response.py":"d13e909c8aa8b91d5b55ec5e5e5179cdaf9325d2",
"scripts/validate_rpb108_rc240_three_trial_signed_response.py":"9e1f46907a3c96d2f916d709163d0dea0db5190a"}

def run_action(d,reg,prime,eps,sl,sh,reverse):
    assert d in (4,6) and 65>3*d+1 and sl>0
    regpoly=legacy.trial.regular_poly(d,reg)
    rc=[o.project(regpoly,n) for n in range(len(regpoly))]
    pc,pt,pfault,segs=legacy.trial.prime_poly(d,prime,reverse)
    assert len(pc)==65 and len(segs)==15
    rtail=up(sum((o.mass(n)*v*v for n,v in enumerate(rc) if n>64),F(0)))
    phi=[F(11,20)**k/factorial(k) if k%2==d%2 else F(0) for k in range(41)]
    moment=B*o.integral(o.product(o.legendre(d),phi))
    pole=[2*(-1)**d*moment*v for v in phi]
    oc=[o.project(pole,n) for n in range(65)]
    tau=2*F(11,20)**41/factorial(41)
    polefault=up(16*B*tau*root(o.mass(d)))
    ll=2*sum((F(1,3)**(2*k+1)/F(2*k+1) for k in range(100)),F(0))
    lh=ll+2*F(1,3)**201/(201*(1-F(1,9)))
    out=[];rnd=F(0)
    for n in range(65):
        if n%2!=d%2:
            out.append(dict(degree=n,coefficient="0",radius="0"));continue
        h=(2*o.H(2*n)-2*o.H(n)+F(1,2*n+1)) if n==d else F(2*n+1,abs(n-d)*(n+d+1))
        lo=h-(lh if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0)
        hi=h-(ll if n==d else 0)-rc[n]+pc[n]+oc[n]-(F(789,125) if n==d else 0)
        vals=[q/(o.H(n)+s)+F(n==d) for q in (lo,hi) for s in (sl,sh)]
        c=down((min(vals)+max(vals))/2)
        rad=up(max(c-min(vals),max(vals)-c))
        rnd+=o.mass(n)*(o.H(n)+sh)*rad*rad
        out.append(dict(degree=n,coefficient=str(c),radius=str(rad)))
    first=65 if d%2 else 66
    comp=dict(finite_rounding=up(rnd),
        endpoint_omitted_output=up(3*B/((o.H(first)+sl)*(64-d)**2)),
        regular_omitted_output=up(rtail/(o.H(first)+sl)),
        prime_omitted_output=up(pt/(o.H(first)+sl)),
        regular_kernel=up((2*B*eps)**2*o.mass(d)/sl),
        prime_arithmetic=up(pfault**2/sl),
        pole_Taylor=up(polefault**2/sl))
    total=up(sum((root(v) for v in comp.values()),F(0))**2)
    return dict(input="P"+str(d),input_degree=d,parity="even",
        finite_original_D_action=out,
        D_energy_component_squared_errors={k:str(v) for k,v in comp.items()},
        complete_original_action_D_error_squared_upper=str(total),
        original_output_cutoff=64,first_omitted_even_degree=first,
        complete_active_prime_pairs=7,all_omitted_outputs_paid=True)

def run(reverse=False):
    data={}
    for path,sha in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==sha,path
        if path.endswith(".json"):data[path]=json.loads(raw)
    metric=data["certificates/rpb108_rc129_four_vector_joint_moment.json"]
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/F(11,5)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/F(11,5)
    regcert=data["certificates/rpb108_rc46_native_archimedean_head.json"]
    reg=list(map(F,regcert["regular_kernel_coefficients"]))
    eps=F(regcert["regular_kernel_uniform_error_upper"])
    prime=data["certificates/rpb108_rc43_native_prime_head.json"]
    assert len(prime["active_prime_powers"])==7
    print("RC296: independently reproducing P4 full original action",flush=True)
    replay=run_action(4,reg,prime,eps,sl,sh,reverse)
    old=data["certificates/rpb108_rc240_three_trial_signed_response.json"]["parity_three_trial_signed_response_certificates"][0]["new_complete_original_action"]
    for key in ("finite_original_D_action","D_energy_component_squared_errors","complete_original_action_D_error_squared_upper"):
        assert replay[key]==old[key],("P4 formula regression",key)
    print("RC296: constructing new native original P6",flush=True)
    fresh=run_action(6,reg,prime,eps,sl,sh,reverse)
    assert all(v["coefficient"]=="0" and v["radius"]=="0" for v in fresh["finite_original_D_action"] if v["degree"]%2)
    return dict(milestone="RC296",starting_commit="4a7c3afd67f46c28efbbf94a83539ead4766a04a",
        input_git_blob_pins=PINS,regression_original_P4_action_reproduced=True,
        new_native_P6_original_action=fresh,
        certified_input_columns_before=[0,2,4],certified_input_columns_after=[0,2,4,6],
        new_original_Weil_action_performed=True,original_P6_input_D_error_paid=True,
        new_P6_high_output_65_to_2048_reconstructed=False,
        rank317_augmented_P6_action_certified=False,
        signed_inverse_response_certified=False,arbitrary_operator_action_certified=False,
        Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC297: extend certified P6 original outputs to degree 2048 with native prime/endpoint projection and apply rank-317 augmentation; test full 4-column inverse seeds.")
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--output",type=Path,required=True)
    ap.add_argument("--replay",action="store_true");args=ap.parse_args()
    r=run(args.replay)
    print("RC296_CANDIDATE="+json.dumps(r,sort_keys=True),flush=True)
    if args.replay:assert r==json.loads(args.output.read_text())
    else:args.output.write_text(json.dumps(r,sort_keys=True,indent=2)+"\n")
