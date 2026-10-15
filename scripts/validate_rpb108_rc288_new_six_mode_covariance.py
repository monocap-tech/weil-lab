"""RC288: new rank-317 3x3 correlated inverse-residual covariance."""
import argparse,hashlib,json,math
from fractions import Fraction as F
from pathlib import Path
ROOT=Path(__file__).resolve().parents[1]
B=F(11,10);S=10**20
PINS={
"certificates/rpb108_rc129_four_vector_joint_moment.json":"33e681e688450c987993603354544fe3919b435f",
"certificates/rpb108_rc274_mixed_diagonal_inverse.json":"2059b48ee4e0b22a0dfb8a9a803644cf0c5fb5f8",
"certificates/rpb108_rc278_smaller_positive_reference.json":"edc59d6cec516d597c2c7816bec2a38a2677e18d",
"certificates/rpb108_rc279_six_mode_gate.json":"bd729c0f5a41debac61a0f3c37276bb94e7834e5",
"certificates/rpb108_rc280_combined_jump_tail.json":"bb0dd3f6174761037ed0f20f17177ddad5749227",
"certificates/rpb108_rc283_reduced_reference.json":"1dc4bba375af6bfd7a274fccc07638e0eead56e6",
"certificates/rpb108_rc287_six_source_covariance_transfer.json":"3eb4968176cdb746c578b41f2176d80f33fe521c"}
def down(x):return F(x.numerator*S//x.denominator,S)
def up(x):return -down(-x)
def rt(x):return F(math.isqrt(x.numerator*S*S//x.denominator)+1,S) if x else F(0)
def mass(n):return 2*B/(2*n+1)
def ser(A):return [[str(v) for v in row] for row in A]
def roundmat(A,kind):
    # Gershgorin: each downward-rounded matrix entry errs by <1/S.
    # Three extra diagonal units ensure a global Loewner envelope.
    n=len(A)
    assert n==3 and all(len(row)==n for row in A)
    R=[[down(v) for v in row] for row in A]
    assert all(R[i][j]==R[j][i] for i in range(n) for j in range(n))
    for i in range(n):R[i][i]+=(F(3,S) if kind=="up" else -F(3,S))
    return R
def subspd(A,I):
    G=[[A[i][j] for j in I] for i in I];n=len(G)
    for k in range(n):
        d=G[k][k]
        if d<=0:return False
        for i in range(k+1,n):
            for j in range(k+1,n):G[i][j]-=G[i][k]*G[k][j]/d
    return True
def run(reverse=False):
    data={}
    for path,pin in sorted(PINS.items(),reverse=reverse):
        raw=(ROOT/path).read_bytes()
        assert hashlib.sha1(b"blob "+str(len(raw)).encode()+bytes([0])+raw).hexdigest()==pin,path
        data[path]=json.loads(raw)
    def get(s):return data["certificates/rpb108_rc"+s+".json"]
    metric=get("129_four_vector_joint_moment")
    oldhigh=get("274_mixed_diagonal_inverse")["projection_mixed_inverse_response_certificates"]
    oldref=get("278_smaller_positive_reference")["smaller_reference_certificates"]
    old279=get("279_six_mode_gate")["coupled_six_mode_gate_certificates"]
    old280=get("280_combined_jump_tail")["combined_jump_tail_gate_certificates"]
    reduced=get("283_reduced_reference")["reduced_reference_options"]
    assert get("287_six_source_covariance_transfer")["full_new_317_source_covariance_reconstructed"] is False
    sl=F(metric["actual_D_Gram_entry_lower"][0][0])/(2*B)
    sh=F(metric["actual_D_Gram_entry_upper"][0][0])/(2*B)
    sm=(sl+sh)/2
    H=[F(0)]
    for n in range(1,2051):H.append(H[-1]+F(1,n))
    output=[]
    for base in range(2):
        ref=oldref[base];src=old279[base];old=old280[base]
        parity=("even","odd")[base];assert ref["parity"]==src["parity"]==old["parity"]==parity
        choice=reduced[base]["reduced_reference_options"][1]
        first=choice["first_discarded_matching_degree"]
        rank=choice["new_low_reference_rank"]
        mu=F(choice["certified_D_reference_floor_lower"])
        lam=F(ref["augmentation_coefficient"])
        assert (rank,first)==((122,244) if base==0 else (195,391)) and mu>F(1,200)
        weights=[F(1) if n<first else down(1-lam/down(H[n]+sl)) for n in range(2050)]
        for n in range(base,2050,2):assert weights[n]>=mu
        tailfirst=2050 if base==0 else 2049
        tw=down(1-lam/down(H[tailfirst]+sl));assert tw>=mu
        Z0=[F(v) for v in ref["exact_trial_Legendre_coefficients"]]
        Y=[[F(v) for v in row["exact_basis_coefficients"]] for row in src["response_trials"]]
        assert len(Y)==3 and all(len(y)==4 for y in Y)
        for j,(a,b,c,d) in enumerate(Y):
            expected=[a*Z0[n]+b*F(n==base)+c*F(n==base+2)+d*F(n==base+4) for n in range(65)]
            assert expected==list(map(F,old["combined_trial_tail_certificates"][j]["exact_trial_Legendre_coefficients"]))
        e0=[F(0)]*2049;er=[F(0)]*2049
        for v in ref["retained_low_residual_certificate"]:
            n=v["degree"];e0[n]=F(v["residual_center"]);er[n]=F(v["source_and_center_rounding_radius"])
        scale=F(ref["exact_trial_scale"])
        for v in oldhigh[base]["residual_physical_numerator_intervals_65_through_2048"]:
            n=v["degree"];vl=[scale*F(v[k])/(H[n]+s) for k in ("lower","upper") for s in (sl,sh)]
            lo,hi=min(vl),max(vl)
            e0[n]=down((lo+hi)/2);er[n]=up(max(e0[n]-lo,hi-e0[n]))
        acts=src["actual_polynomial_action_certificates"]
        O=[[F(v["coefficient"]) for v in a["finite_original_D_action"]] for a in acts]
        assert all(len(a)==2049 for a in O)
        rounding0=up(sum((up(mass(n)*(H[n]+sh)*er[n]**2/weights[n])
                            for n in range(base,2049,2)),F(0)))
        eps=[up(rt(up(scale**2*F(oldhigh[base]["complete_full_trial_model_tail_D_energy_upper"])/tw))
                +rt(up(F(ref["remaining_global_D_fault_norm_upper"])**2/mu))
                +rt(rounding0))]
        for a in acts:
            eps.append(up(rt(up(F(a["model_D_energy_beyond_2048_upper"])/tw))
                          +rt(up(F(a["global_D_fault_norm_upper"])**2/mu))))
        rows=[[],[],[]];rad=[]
        for j,(a,b,c,d) in enumerate(Y):
            rr=[]
            for n in range(base,2049,2):
                num=F(n==base+2*j)-a*F(n==base)-lam*(b*F(n==base)+c*F(n==base+2)+d*F(n==base+4))
                rows[j].append(a*e0[n]+num/(H[n]+sm)-b*O[0][n]-c*O[1][n]-d*O[2][n])
                radn=max(abs(num/(H[n]+sl)-num/(H[n]+sm)),
                         abs(num/(H[n]+sh)-num/(H[n]+sm)))
                rr.append(up(mass(n)*(H[n]+sh)*radn**2/weights[n]))
            rad.append(up(sum(reversed(rr) if reverse else rr,F(0))))
        degrees=list(range(base,2049,2))
        intervals=[]
        for i in range(3):
            line=[]
            for j in range(3):
                vals=[mass(n)*(H[n]+sh)*rows[i][k]*rows[j][k]/weights[n]
                      for k,n in enumerate(degrees)]
                if reverse:vals.reverse()
                line.append((sum(map(down,vals),F(0)),sum(map(up,vals),F(0))))
            intervals.append(line)
        radius=up(max(sum(((u-l)/2 for l,u in line),F(0)) for line in intervals))
        Gram=[[(l+u)/2+(radius if i==j else 0) for j,(l,u) in enumerate(line)]
              for i,line in enumerate(intervals)]
        noise=[[5*sum((eps[k]**2*Y[i][k]*Y[j][k] for k in range(4)),F(0))
               +(15*rad[i] if i==j else 0) for j in range(3)] for i in range(3)]
        Gram=roundmat(Gram,"up");noise=roundmat(noise,"up")
        CI=[[(F(l),F(u)) for l,u in line] for line in src["variational_response_center_intervals"]]
        center=[[(l+u)/2 for l,u in line] for line in CI]
        centerRadius=up(F(src["center_interval_Loewner_radius"]))
        check=[]
        for th in [F(1,100),F(1,10),F(1,3),F(1),F(3),F(10),F(100)]:
            covariance=roundmat([[(1+th)*Gram[i][j]+(1+1/th)*noise[i][j] for j in range(3)] for i in range(3)],"up")
            gate=roundmat([[(mass(base+2*i) if i==j else 0)
                   -lam*(center[i][j]+covariance[i][j]+(centerRadius if i==j else 0))
                   for j in range(3)] for i in range(3)],"down")
            candidates=[I for I in ([0],[0,1],[0,2],[0,1,2]) if subspd(gate,I)]
            subset=max(candidates,key=len,default=[])
            gersh=down(min(gate[i][i]-sum(abs(gate[i][j]) for j in range(3) if j!=i) for i in range(3)))
            check.append((len(subset),gersh,th,covariance,gate,subset))
        count,gfloor,theta,Snew,gate,subset=max(check,key=lambda a:(a[0],a[1],-a[2]))
        # Proved in the *new* rank-317 inverse metric, not inherited from RC280.
        assert subset==([0,4] if base==0 else [1]),(parity,subset)
        assert subspd(gate,([0,2] if base==0 else [0]))
        output.append(dict(parity=parity,reference_rank=rank,first_omitted_degree=first,
            reference_D_floor_lower=str(mu),source_degrees=[base,base+2,base+4],
            original_source_amplitude_error_upper=list(map(str,eps)),
            finite_original_center_Gram_Loewner_upper=ser(Gram),
            correlated_fault_Gram_Loewner_upper=ser(noise),
            selected_Young_parameter=str(theta),
            complete_new_inverse_residual_covariance_Loewner_upper=ser(Snew),
            unchanged_variational_center_radius=str(centerRadius),
            complete_native_six_mode_gate_lower=ser(gate),
            certified_new_positive_subset=[base+2*i for i in subset],
            positive_subset_dimension=count,full_three_source_positive_certified=count==3,
            full_gate_Gershgorin_lower=str(gfloor),
            all_original_output_modes_through_2048_paid=True,complete_infinite_tails_paid=True))
    return dict(milestone="RC288",starting_commit="7bad1336df47036872705b5f1db65a388f8f1fbd",
        input_git_blob_pins=PINS,full_new_rank317_three_by_three_covariance_both_parities_computed=True,
        new_original_Weil_actions_performed=False,old_rank371_pivots_not_transferred=True,
        parity_certificates=output,Stage_I_closed=False,RH=False,F4=False,Lean=False,
        next_cursor="RC289: improve new-reference covariance with RC280 combined jump/continuous tail and source-trial optimization; remaining principal Schur remains open.")
if __name__=="__main__":
    a=argparse.ArgumentParser()
    a.add_argument("--output",type=Path,required=True)
    a.add_argument("--replay",action="store_true")
    x=a.parse_args()
    o=run(x.replay)
    if x.replay:assert o==json.loads(x.output.read_text())
    else:x.output.write_text(json.dumps(o,sort_keys=True,indent=2)+"\n")
