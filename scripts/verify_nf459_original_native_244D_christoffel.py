#!/usr/bin/env python3
"""NF459: real 244D original Gram/Schur Christoffel endpoint and collar."""
import sys,json,hashlib,time,argparse,traceback
from pathlib import Path
from fractions import Fraction as F
import flint
from flint import arb,arb_mat,ctx
HERE=Path(__file__).resolve().parent
sys.path.insert(0,str(HERE))
import verify_rpb108_si29_full_J_L2_normalization as p
from verify_rpb108_original_signed_frame_transport import candidate
RANK="9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2"
B=F(11,10);DELTA=F(1,10**15)
def load(s,sha=None):
    raw=(HERE.parent/"notes/data/provisional"/s).read_bytes()
    h=hashlib.sha256(raw).hexdigest()
    if sha is not None: assert h==sha,(s,h)
    return json.loads(raw),h
def rat(x):
    m,e=x.man_exp()
    return F(int(m))*F(2)**int(e)
def iv(x): return [str(rat(x.lower())),str(rat(x.upper()))]
def evaluate(raw, x):
    if raw is None:return (x/2).sinh()
    c,k=raw; angle=2*arb.pi()*p.a(c)*x
    return x**k*(angle.sin() if k%2==0 else angle.cos())
def evaluate_basis(rows,x):
    return arb_mat([[evaluate(z,x)] for z in rows])
def main(dest):
    st=time.monotonic()
    assert flint.__version__=="0.8.0"
    ctx.prec=4096
    rank,hr=load("parents/pr350_original_BS_pruned_rank_bound.json",RANK)
    nf404,_=load("NF404_original_selected_pole_shear_exact.json")
    nf403,_=load("NF403_original_joint_complement_power_exact.json")
    q512,_=load("NF380_original_archived_unfitted_signed_dual_native.json")
    q513,_=load("NF389_original_n513_signed_native.json")
    assert nf404["original_rank_sha256"]==hr
    rows=[(F(z[0]),k) for z,m in zip(rank["original_nodes"],rank["selected_multiplicities"]) for k in range(m)]
    assert len(rows)==241 and max(k for c,k in rows)==13
    rows.append(None)
    terms=[p.pole_terms() if z is None else p.source_terms(*z) for z in rows]
    raw=[(F(5*n,11),0) for n in (512,513)]
    probes=[p.source_terms(*t) for t in raw]
    ker=p.Integrals()
    print("NF459 original 242 physical Gram begin",flush=True)
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=p.gram(terms[i],terms[j],ker)
        if i%80==0:print("Gram row",i,flush=True)
    D=candidate(H);N=D.transpose()*H*D
    err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert err<arb("0.01")
    C=arb_mat([[p.gram(t,v,ker) for v in probes] for t in terms])
    P=arb_mat([[p.gram(t,v,ker) for v in probes] for t in probes])
    V=D.transpose()*C
    Y=N.solve(V,algorithm="lu")
    S=P-V.transpose()*Y
    S2=P-V.transpose()*Y-Y.transpose()*V+Y.transpose()*N*Y
    for i in range(2):
        for j in range(2):assert (S[i,j]-S2[i,j]).contains(0)
    assert S[0,0].lower()>0
    assert (S[1,1]-S[0,1]*S[1,0]/S[0,0]).lower()>0
    for i,q in enumerate((q512,q513)):
        lo,hi=map(F,q["physical_q_norm2_interval"])
        assert lo<=rat(S[i,i].upper()) and rat(S[i,i].lower())<=hi
    print("NF459 original physical Schur SPD; seconds",round(time.monotonic()-st,1),flush=True)
    def K_at(x,exact_B=False):
        ej=evaluate_basis(rows,x)
        e=D.transpose()*ej
        z=N.solve(e,algorithm="lu")
        u=arb_mat([[arb(0) if exact_B else evaluate(t,x)] for t in raw])
        g=u-V.transpose()*z
        return (e.transpose()*z)[0,0]+(g.transpose()*S.solve(g,algorithm="lu"))[0,0]
    mid=p.a(B-DELTA/2)
    interval=arb(mid,p.a(DELTA/2))
    assert rat(interval.lower())<=B-DELTA and rat(interval.upper())>=B
    k_B=K_at(p.a(B),True)
    print("NF459 K(B)",str(k_B),flush=True)
    k_left=K_at(p.a(B-DELTA))
    print("NF459 K(B-delta)",str(k_left),flush=True)
    k_all=K_at(interval)
    print("NF459 original complete collar enclosure",str(k_all),flush=True)
    assert k_B.lower()>0 and k_left.lower()>0
    gate=p.a(F(4500,17)**2)
    from nf459_original_correlated_endpoint_taylor import certify
    k_taylor,tail_error,taylor_terms=certify(rows,D,N,V,S,B,DELTA,p)
    print("NF459 original 72-term correlated full-collar K",str(k_taylor),flush=True)
    passed=bool(k_taylor.upper()<gate)
    # Accepted original selected source + two exterior power (NF403/NF404).
    Rhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    dUP=F(nf403["source_strict_joint_dual_power_upper"])
    assert Rhi+dUP<F(34,10**12)**2
    if passed:
        assert k_taylor.upper()<p.a(114**2)
        # NF457 original source-valid terminal regular part <5.5e-10;
        # source-verified |v|/2<117/(2*10^13), L=log(B/delta)<36.
        nf457,_=load("NF457_original_log_peel_info_ceiling_custody.json")
        assert nf457["original_regular_plus_actual_prime_term_strict_uniform_bound"]=="5.5e-10"
        projected_sup=F(114)*F(34,10**12)
        regular=projected_sup+F(55,10**11)
        collar_power=4*F(117,2*10**13)**2*DELTA*(36**2+2*36+2)+4*regular**2*DELTA
        assert projected_sup<F(4,10**9)
        assert collar_power<F(8,10**32)
    # NF461: source-native enlargement into the authentic *bulk* of J8.
    outer=F(1,10**13)
    k_outer,tail_outer,_=certify(rows,D,N,V,S,B,outer,p)
    print("NF461 entire extended J8 inner slice K",str(k_outer),flush=True)
    nf461_certified=bool(passed and k_outer.upper()<p.a(114**2))
    if nf461_certified:
        nf451,_=load("NF451_original_J8_terminal_collar_custody_index.json")
        nf450,_=load("NF450_original_B_complete_Laplace_native_sign_custody_index.json")
        nf411,_=load("NF411_original_source_boundary_jet.json")
        nf407,_=load("NF407_original_prime_jump_log_power_exact.json")
        sourceSHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
        assert nf451["original_source_sha256"]==nf411["nf407_source_sha256"]==sourceSHA
        assert nf450["source_SHA256"]==sourceSHA
        assert nf451["analytic_modulus"]=="|z(B-d)-z(B)|<14000*d+600*d*log(2B/d)"
        assert nf451["original_J8_seam_n9_strictly_before_collar"] is True
        assert nf407["source_all_original_prime_jumps_cancelled_from_z"] is True
        assert F(8,3)**32 > 2*B/outer
        assert 2*B/outer>F(8,3)
        v=tuple(map(F,nf407["original_source_u4_endpoint_interval"]))
        assert -F(117,10**13)<v[0]<=v[1]<0
        c8=sum(F(z["c_n_positive_outward"][1]) for z in
               nf411["all_seven_original_prime_seam_derivative_identities"])
        assert c8<F(18,5)
        zl,zu=map(F,nf450["complete_z_B_outward_24_decimal"])
        assert -F(44,10**11)<zl<=zu<0
        source_mod=outer*(F(14000)+F(600)*32)
        assert source_mod==F(33200,10**13)
        projector=F(114)*F(34,10**12)
        regular_outer=F(117,10**13)*c8+F(44,10**11)+source_mod+projector
        assert regular_outer<F(8,10**9)
        # Exact global two-sided log-square primitive on [B-outer,B].
        original_two_sided=4*outer*(F(117,2*10**13)**2*(32*32+64+2)+F(8,10**9)**2)
        assert original_two_sided<F(26,10**30)
        # Original NF459 [B-1e-15,B] is included, so the new *bulk slice*
        # [B-1e-13,B-1e-15] has a separately valid upper by monotonicity.
        assert DELTA<outer
        assert nf403["source_sufficient_Jperp_full_action_power_budget"]
    out={
     "pass":"NF459","standing":"REAL SOURCE-NATIVE 244D PHYSICAL GRAM/COLLAR K UPPER" if passed else "REAL SOURCE-NATIVE K ENDPOINT; TERMINAL UNIFORM GATE OPEN/METHOD STOP",
     "source_rank_sha256":hr,"working_precision_bits":4096,
     "physical_frame_row_sum_less_than":"1/100",
     "original_rank":242,"raw_exterior_n":[512,513],
     "exterior_quotient_strict_SPD":True,
     "K_B_outward":iv(k_B),"K_left_outward":iv(k_left),
     "K_naive_raw_one_box_diagnostic":str(k_all),
     "K_whole_terminal_collar_outward":iv(k_taylor),
     "K_correlated_taylor_terms":taylor_terms,
     "source_Cauchy_transformed_tail_upper":str(tail_error),
     "original_collar_christoffel_sufficient_gate":"(4500/17)^2",
     "original_terminal_K_gate_certified":passed,
     "NF457_two_sided_T_collar_upper_certified":passed,
     "NF457_two_sided_T_collar_upper_if_pass":"4.01e-31",
     "original_terminal_K_lt_12996":bool(passed),
     "NF461_outer_delta":"1e-13",
     "NF461_whole_outer_K_Arb":str(k_outer),
     "NF461_whole_outer_K_lt_12996":nf461_certified,
     "NF461_original_J8_two_sided_bulk_slice_upper_if_certified":"2.6e-29",
     "NF461_original_extended_collar_and_bulk_slice_upper_if_certified":"2.6e-29",
     "original_projector_collar_abs_lt_if_pass":"3.876e-9",
     "NF459_stronger_two_sided_T_collar_upper_if_pass":"8e-32",
     "full_T_upper":"OPEN","NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
     "elapsed_seconds":round(time.monotonic()-st,2)}
    dest.parent.mkdir(parents=True,exist_ok=True)
    dest.write_text(json.dumps(out,indent=2)+"\n")
    print("NF459 RESULT K gate",passed,"elapsed",round(time.monotonic()-st,1),flush=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser();ap.add_argument("--output",required=True)
    args=ap.parse_args();path=Path(args.output)
    try:main(path)
    except Exception:
        path.parent.mkdir(parents=True,exist_ok=True)
        path.write_text(json.dumps({"pass":"NF459","standing":"FAILED_CLOSED","traceback":traceback.format_exc(),"K_gate_certified":False,"NF404":"OPEN"},indent=2)+"\n")
        traceback.print_exc();raise
