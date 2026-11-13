#!/usr/bin/env python3
"""NF504 authentic J8 two-collar SUPPORT-SATURATED complete exterior Schur.

Original unchanged physical source NF407/NF406, genuine 242 selected J,
source-matched archived 400 complete H/U Taylor jets from NF494, true
NF495 whole terminal positive square, original entire NF401 selected
moment column, true NF479/NF478/NF495 complete centered response energy.

This computes one *actual* exterior J242 Gram on |x|<=549/500, all
original 242 physical collar mixed moments of the COMPLETE response W,
and the full physical support-saturated optimum from NF503.

Original source errors are paid AFTER correlation-preserving old D
frame transformation; NEVER independently overcharge raw source moments
then multiply the near-orthogonal giant-coefficient original D frame.

Scope is entire physical L2 support S, not a Weil image/domain theorem,
and the result requires independent exact/interval validation.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys,time
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
from flint import arb, arb_mat, ctx
import flint
import verify_rpb108_si29_full_J_L2_normalization as phys
from verify_rpb108_original_signed_frame_transport import candidate
from verify_nf374_original_matched_curvature import load,RANK_SHA,PR355_SHA
from verify_nf380_original_archived_signed_dual import interval,FRAME_SHA
sys.path.insert(0,str(Path(__file__).parent/"local_replay"))
import nf500_original_J242_full_smooth_log_mixed_source_native as native

SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
NF401="644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515"
NF494_H="39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181"
NF495="ebd45c76e3bfca33572fac77cfaeb7134e21150443d84cbd206711f26a2f9460"
NF500="7e261d540c8b658bced4b44d1bf998c23ef7f975fc07daa0f30ae6438dcffb05"
NF501="7726a8a9af5faa7a22fd7581c38548c26c5a48a52cb92dc75f815c57f6e3ad7a"
B=F(11,10);DELTA=F(1,500);B_OUT=B-DELTA
TD=400

def read(p):
    x=Path(p).read_bytes()
    return json.loads(x),hashlib.sha256(x).hexdigest()
def ball(p):
    a,b=map(F,p)
    assert a<=b
    return arb(native.A((a+b)/2),native.A((b-a)/2))
def col(xs):return arb_mat([[x] for x in xs])
def cmpoverlap(x,p):
    a,b=map(F,p)
    return x.lower()<=native.A(b) and x.upper()>=native.A(a)
def absmax(x):return max(abs(x.lower()),abs(x.upper()))
def finite_moment_weights(A,C,h,M=TD+14):
    qA=[];qL=[]
    two_delta=native.A(2*DELTA)
    for j in range(M):
        a=arb(0);ell=arb(0)
        for i in range(len(A)):
            den=native.A(F(1,j+i+1))
            a+=A[i]*den
        for i in range(len(C)):
            den=native.A(F(1,j+i+1))
            ell+=C[i]*(h*den+den*den)
        qA.append(two_delta*a)
        qL.append(two_delta*ell)
    return qA,qL
def source_norm_check(H,D):
    N=D.transpose()*H*D
    err=max(sum((abs(N[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    assert err<arb("0.01"),"METHOD STOP historical original physical selected frame"
    digest=hashlib.sha256()
    for i in range(242):
        for j in range(242):
            digest.update((json.dumps(phys.dyadic(D[i,j]),separators=(",",":"))+"\n").encode())
    assert digest.hexdigest()==FRAME_SHA
    return N,err
def main(o):
    t=time.monotonic()
    assert flint.__version__=="0.8.0" and o.bits==4096
    ctx.prec=o.bits
    native.D=TD
    source,srcsha=read("notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json")
    seams,ss=read("notes/data/provisional/NF406_original_prime_support_partition_exact.json")
    assert srcsha==SRC and ss==SEAM
    rank=load(o.rank,RANK_SHA)
    _=load(o.source,PR355_SHA)
    old,osha=read("notes/data/provisional/NF401_original_242D_selected_column_source_native.json")
    receipt,_=read("notes/data/provisional/NF401_original_242D_execution_receipt.json")
    nf404,s404=read("notes/data/provisional/NF404_original_selected_pole_shear_exact.json")
    nf478,s478=read("notes/data/provisional/NF478_original_complete_J7_signed_seven_panel_custody.json")
    nf479,s479=read("notes/data/provisional/NF479_original_full_J8_forced_positive_NF404_transfer_custody.json")
    nf411,s411=read("notes/data/provisional/NF411_original_source_boundary_jet.json")
    Hjet,hsha=read(o.nf494_native)
    last,lsha=read(o.nf495)
    nf500,msha=read(o.nf500)
    nf501,nsha=read(o.nf501)
    assert osha==NF401==receipt["original_native_json_sha256"]
    assert hsha==NF494_H==last["original_nf494_native_source_json_sha256"]
    assert lsha==NF495
    assert msha==NF500 and nsha==NF501
    assert Hjet["pass"]=="NF494-native" and last["pass"]=="NF494"
    assert nf500["pass"]=="NF500-native" and nf501["pass"]=="NF501-native"
    for obj,k,k2 in [
        (Hjet,"original_nf407_source_sha256","original_nf406_seams_sha256"),
        (last,"original_nf407_source_sha256","original_nf406_seams_sha256"),
        (nf500,"original_nf407_source_sha256","original_nf406_seams_sha256"),
        (nf501,"original_nf407_source_SHA256","original_nf406_seams_SHA256")]:
        assert obj[k]==SRC and obj[k2]==SEAM
    assert nf501["original_physical_frame_SHA256"]==FRAME_SHA
    assert old["original_frame_sha256"]==FRAME_SHA
    assert Hjet["original_true_terminal_delta"]=="1/500"
    assert Hjet["original_source_400_jet_order"]==400
    assert last["true_original_J8_terminal_delta"]=="1/500"
    assert last["original_full_source_400_H_and_400_U_native_exact_interval_coefficients"] is True
    assert last["original_true_same_source_joint_normalized_coeff_retained_count"]==102
    assert nf404["original_selected_pole_index"]==241 and nf404["original_dimension"]==242
    assert nf404["fixed_dyadic_pole_coefficient"]=="6677356497477490213/4611686018427387904"
    assert nf478["pass"]=="NF478" and nf479["pass"]=="NF479"
    assert nf478["source_original_nf407_sha256"]==SRC
    assert nf479["original_nf407_source_sha256"]==SRC
    assert nf411["nf407_source_sha256"]==SRC
    nodes=[]
    for (freq,maxk),count in zip(rank["original_nodes"],rank["selected_multiplicities"]):
        assert 0<=count<=maxk
        for k in range(count):nodes.append((F(freq),k))
    assert len(nodes)==241 and rank["retained_original_pole"]
    nodes.append((None,None))
    basis=[["pole",None] if f is None else [str(f),k] for f,k in nodes]
    assert basis==nf500["original_selected_basis_242_raw_index_order"]
    assert len(Hjet["original_H_400_native_outward"])==len(Hjet["original_U_400_native_outward"])==400
    print("NF504 source SHA native original complete H400/U400; old frame/242 selected order accepted",flush=True)

    J=[phys.pole_terms() if f is None else phys.source_terms(f,k) for f,k in nodes]
    kern=phys.Integrals()
    H=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            H[i,j]=H[j,i]=phys.gram(J[i],J[j],kern)
    D=candidate(H)
    N,frame_err=source_norm_check(H,D)
    print("NF504 original full J242 Gram and historical D frame SHA independently reproduced",flush=True)
    kern_out=phys.Integrals()
    kern_out.b=native.A(B_OUT)
    Hout=arb_mat(242,242)
    for i in range(242):
        for j in range(i+1):
            Hout[i,j]=Hout[j,i]=phys.gram(J[i],J[j],kern_out)
        if (i+1)%60==0:
            print("NF504 actual SOURCE-original central exterior physical Gram rows",i+1,"/242",flush=True)
    Nout=D.transpose()*Hout*D
    Nout=(Nout+Nout.transpose())/2
    Ns=N-Nout
    # Raw source original polar continuum, no unproved endpoint spectral
    # conditioning: record it, solve true interval exterior Gram.
    out_deviation=max(sum((abs(Nout[i,j]-int(i==j)) for j in range(242)),arb(0)) for i in range(242))
    print("NF504 original actual exterior D-frame maximal row deviation:",out_deviation.str(16),flush=True)

    # NF505 ORIGINAL SOURCE-CORRELATED PRIME CONSTANT REPAIR:
    # c_n = Lambda(n)/sqrt(n), where all seven n are EXACT original
    # prime powers. The old NF411 custody enclosures are safe but some
    # are only ~40 decimal digits. Multiplying their independently
    # overpaid widths through the historic D frame with source
    # coefficient l1 ~2.765e149 creates completely vacuous original
    # 242D moment balls (up to 1e101), even though the true physical
    # source is small. These are KNOWN arithmetic constants: evaluate
    # each original prime-power Lambda(n) from the exact prime base at
    # the SAME 4096-bit Arb precision as the ORIGINAL H400/U400 source;
    # independently assert genuine NF411 original custody overlap.
    # No prime list/source/carrier is changed or refitted.
    prime_base={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    c8=arb(0);seen=[]
    for row in nf411["all_seven_original_prime_seam_derivative_identities"]:
        n=row["prime_power"]
        assert n in prime_base and n not in seen
        cn=native.A(prime_base[n]).log()/native.A(n).sqrt()
        assert cn.lower()>0
        assert cmpoverlap(cn,row["c_n_positive_outward"]), (
            "METHOD STOP original NF411 arithmetic prime weight custody does not overlap exact source-native 4096bit Lambda(n)/sqrt(n)",n)
        c8+=cn
        seen.append(n)
    assert seen==[2,3,4,5,7,8,9]
    print("NF505 original exact seven Lambda(n)/sqrt(n) source arithmetic restored at full 4096bit; original NF411 custody overlaps all seven",flush=True)
    H400=[ball(r) for r in Hjet["original_H_400_native_outward"]]
    U400=[ball(r) for r in Hjet["original_U_400_native_outward"]]
    assert U400[0].upper()<0 and H400[0].upper()<0
    K_nf495=last["original_true_same_source_joint_normalized_coeff_retained_count"]
    assert K_nf495==102
    # NF505 independent source-consistency repair: the original D frame
    # has raw selected coefficient l1 as large as 2.77e149. A
    # source-native 102-term H polynomial has a physically small
    # global tail (2.24e-71), but raw high-condition moment transport
    # can exhibit enormous cancellation artifacts. Retain ALL 400
    # authentic source-matched analytic H coefficients and ALL 400
    # U-log coefficients BEFORE applying the fixed historical D frame.
    # Pay only the genuine analytic 400-jet source remainder AFTER
    # this correlation-preserving projection. NF495's independently
    # accepted original square still retains its own 102-term policy.
    K=TD
    assert K==400
    A=[];C=[]
    scale=F(1)
    for i in range(K):
        a=H400[i]+(U400[0]*c8 if i==0 else arb(0))
        A.append(a*native.A(scale))
        C.append(U400[i]*native.A(scale)/2)
        scale*=DELTA
    tailA=F(last["original_full_H400_remaining_source_normalized_l1"])
    tailC=F(last["original_full_U400_remaining_source_normalized_l1"])
    EH=F(Hjet["original_original_H400_analytic_tail"])
    EU=F(Hjet["original_original_U400_analytic_tail"])
    assert 0<tailA<F(1,10**69) and 0<tailC<F(1,10**69)
    # Source-real true H400 residual bound is the ORIGINAL accepted
    # analytic Cauchy remainder, not the old H102 omitted polynomial.
    erra=EH
    errc=EU/2
    assert erra+9*errc<F(1,10**99)
    print("NF505 source-normalized full original H400/U400 selected-frame contraction, original NF495 102 only for prior positive square; remaining L2 correlated analytic fee",(erra+9*errc)/7,flush=True)
    hlo,hhi=map(F,nf500["original_exact_log550_rational_positive_atanh_410term_interval"])
    assert F(6)<hlo<=hhi<F(7) and hhi-hlo<F(1,10**375)
    h=ball([hlo,hhi])
    aweights,lweights=finite_moment_weights(A,C,h)
    oldlog=nf500["original_selected_242_odd_source_full_two_collar_basis_moments_outward"]
    rawW=[];rawLog=[]
    for idx,(f,k) in enumerate(nodes):
        coeff=(native.hyperpole_coeffs(DELTA) if f is None else native.selected_ordinary_coeffs(f,k))
        assert len(coeff)>=TD
        analytic=arb(0);log=arb(0)
        for j,tj in enumerate(coeff):
            analytic+=tj*aweights[j]
            log+=tj*lweights[j]
        assert cmpoverlap(log,oldlog[idx]["original_true_raw_log_source_moment_outward"]),(
            "METHOD STOP original H/U log part inconsistent with old actual independently source-certified NF500",idx)
        rawLog.append(log)
        rawW.append(analytic+log)
        if (idx+1)%40==0:
            print("NF504 genuine original complete W H+Ulog two-collar mixed moments",idx+1,"/242",flush=True)
    rawcol=col(rawW)
    dSnom=D.transpose()*rawcol
    # Charge H400/U400 full original source tails only AFTER correct D
    # correlation-preserving contraction: ||D_j||_L2(I)<2 from N_jj.
    # ∫S|(Aerr+Cerr L)|² <=2δ(erra+9errc)² and
    # sqrt(2δ)<1/15; hence source fee <(erra+9errc)/7.
    # Basis 400 Taylor remainder is genuinely generator-dependent and
    # scales with ∑|D_ij|. Use original 12^400/400! and
    # total true complete ||W||_L1(S)<110 (NF492 envelope).
    basis_tail=F(200*10**6*12**TD,math.factorial(TD))
    assert basis_tail<F(1,10**425)
    dS=[]
    maxfee=arb(0);maxampl=arb(0)
    for j in range(242):
        amp=sum((abs(D[i,j]) for i in range(242)),arb(0))
        fee=native.A((erra+9*errc)/7)+native.A(110*basis_tail)*amp
        maxfee=max(maxfee,fee)
        maxampl=max(maxampl,amp)
        dS.append(dSnom[j,0]+arb(0,fee.upper()))
    dS=col(dS)
    assert maxfee.upper()<arb("1e-45"), "METHOD STOP source H/U original new correlated D-frame error"
    print("NF504 original direct D-frame true W mixed 242 moments max fee",maxfee.str(16),flush=True)
    # Hard Cauchy necessary source-consistency gate for the genuine
    # physical normalized selected-frame source vectors. The true
    # original positive two-collar square is already independently
    # source-certified; Njj<=1.01 from the original full selected
    # frame. Therefore |<D_j,W_S>|<1e-9 for all 242. A purported
    # narrow source interval centered at 1e82 can NEVER represent
    # the original physical scalar, even if a later interval LU
    # quotient returns an interval containing all real numbers.
    Es_source=2*ball(last["original_complete_J8_true_improper_whole_terminal_positive_square_EwT_outward"])
    assert Es_source.upper()<arb("1e-20")
    cauchy_guard=arb("1e-9")
    bad=[i for i in range(242) if dS[i,0].lower()>cauchy_guard or dS[i,0].upper() < -cauchy_guard]
    if bad:
        print("NF505 METHOD STOP: original selected-frame S physical Cauchy mismatch, violating actual ||W_S|| and Njj. Indices:",bad[:20],"count",len(bad),flush=True)
        print("NF505 first actual impossible source interval:",interval(dS[bad[0],0]),flush=True)
        raise AssertionError("METHOD STOP: original D-frame source contraction does not enclose physical mixed moments; source-verified Cauchy inconsistency")

    dOld=col([ball(x) for x in old["original_selected_D_frame_moment_column_outward"]])
    es=col([int(j==241) for j in range(242)])
    aPole=native.A(F(nf404["fixed_dyadic_pole_coefficient"]))
    dW=dOld-aPole*D.transpose()*H*es
    RW=(dW.transpose()*N.solve(dW,algorithm="lu"))[0,0]
    RAlo=F(nf404["original_selected_after_pole_shear_power_lower_exact"])
    RAhi=F(nf404["original_selected_after_pole_shear_power_upper_exact"])
    assert cmpoverlap(RW,[RAlo,RAhi])
    dO=dW-dS
    E_S=2*ball(last["original_complete_J8_true_improper_whole_terminal_positive_square_EwT_outward"])
    Klo,Khi=map(F,nf479["original_exact_K_outward_approx"])
    D7lo,D7hi=map(F,nf478["original_seven_panel_J7_signed_D_outward"])
    D8lo,D8hi=map(F,last["original_true_full_J8_signed_D8_outward"])
    Efull=ball([Klo+D7lo+D8lo,Khi+D7hi+D8hi])
    Eout=Efull-E_S
    assert Eout.lower()>0
    original_q2=ball(nf501["true_original_Q_Jw_squared_from_K_D7_D8_R_outward"])
    assert cmpoverlap(Efull-RW,interval(original_q2))
    print("NF504 original whole original centered E and true exterior E physical source verified",flush=True)
    x=Nout.solve(dO,algorithm="lu")
    projection=(dO.transpose()*x)[0,0]
    qsat=Eout-projection
    # Independent near-equal original source equation:
    # qS²=||W_S||²-2< P W, W_S >+||P W||_S².
    # source exterior annihilator: R=||q||²-||q_S||²
    #   - <J_S,q_S>^T G_O^-1 <J_S,q_S>.
    z=N.solve(dW,algorithm="lu")
    qS2=E_S-2*(z.transpose()*dS)[0,0]+(z.transpose()*Ns*z)[0,0]
    qSmixed=dS-Ns*z
    q2=Efull-RW
    residual2=q2-qS2-(qSmixed.transpose()*Nout.solve(qSmixed,algorithm="lu"))[0,0]
    assert cmpoverlap(residual2,interval(qsat)), "METHOD STOP full exterior physical Schur vs independent primal original energy decomposition"
    gamma2=native.A(F(nf404["exact_source_original_full_complement_power_budget"]))
    assert gamma2.lower()>0
    decision=("CERTIFIED_PHYSICAL_SUPPORT_NO_GO" if qsat.lower()>gamma2.upper()
              else "PHYSICAL_SUPPORT_SUFFICIENT_POSSIBLE" if qsat.upper()<gamma2.lower()
              else "SOURCE_INTERVAL_INDETERMINATE")
    print("NF504 actual ORIGINAL J8 saturated residual =",qsat.str(30),flush=True)
    print("NF504 actual ORIGINAL J8 saturated vs unchanged gamma² =",decision,flush=True)
    result={
        "pass":"NF504-native",
        "standing":"4096bit ORIGINAL source 242D genuine complete two-collar physical support saturated Hilbert residual, NOT an admissible original Weil multiplier/range or RH proof; independent acceptance pending",
        "source_original_NF407_sha256":SRC,
        "source_original_NF406_sha256":SEAM,
        "original_NF401_native_sha256":osha,
        "original_NF494_native_400_HU_sha256":hsha,
        "original_NF495_independent_true_square_sha256":lsha,
        "original_NF500_log_column_sha256":msha,
        "original_NF501_complete_QJ_native_sha256":nsha,
        "original_nf404_sha256":s404,
        "original_nf411_sha256":s411,
        "original_nf478_sha256":s478,
        "original_nf479_sha256":s479,
        "original_selected_J_dimension":242,
        "original_source_basis_nodes":basis,
        "original_original_D_frame_SHA256":FRAME_SHA,
        "original_actual_full_D_normalization_max_row_deviation":interval(frame_err),
        "original_exterior_center_radius":"549/500",
        "original_terminal_two_collar_delta":"1/500",
        "original_actual_exterior_D_Gram_max_row_deviation":interval(out_deviation),
        "original_actual_exterior_D_Gram_inverse_executed":True,
        "original_source_all_242_true_complete_W_H_and_Ulog_moments_source_cross_NF500":True,
        "original_H_U_normalized_retained_terms":K,
        "original_U_full_log_source_normalized_terms":len(C),
        "original_original_basis_Taylor_order":TD,
        "original_source_global_correlated_W_analytic_fee":str((erra+9*errc)/7),
        "original_generator_Taylor_source_remainder":str(basis_tail),
        "original_D_frame_abs_raw_amplification_max":interval(maxampl),
        "original_actual_D_frame_W_S_moment_max_absolute_fee":interval(maxfee),
        "original_actual_complete_W_D_frame_selected_moments_S_outward":[interval(dS[i,0]) for i in range(242)],
        "original_actual_exterior_J242_D_Gram_rows_outward":[[phys.ball(Nout[i,j]) for j in range(242)] for i in range(242)],
        "original_actual_exterior_W_moments_D_outward":[interval(dO[i,0]) for i in range(242)],
        "original_original_W_whole_energy_outward":interval(Efull),
        "original_original_W_two_collar_energy_outward":interval(E_S),
        "original_original_W_exterior_energy_outward":interval(Eout),
        "original_original_W_exterior_selected_projection_power_outward":interval(projection),
        "original_original_entire_Q_JW_squared_outward":interval(q2),
        "original_original_Q_JW_squared_S_outward":interval(qS2),
        "original_original_saturated_exterior_residual_outward":interval(qsat),
        "original_original_primal_independent_Schur_residual_outward":interval(residual2),
        "original_original_gamma_squared":str(F(nf404["exact_source_original_full_complement_power_budget"])),
        "original_support_saturated_physical_Hilbert_gate":decision,
        "source_native_4096bit_complete_two_collar_S_saturation_result":True,
        "independent_242D_exterior_source_Gram_replay":"OPEN",
        "original_weil_multiplier_source_image_domain":"OPEN",
        "W_ODD_NEG":"OPEN",
        "full_even_odd_Weil_operator_and_RH":"OPEN",
        "elapsed_seconds":round(time.monotonic()-t,3)
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+"\n")
    print("NF504 original source-native outward result written",o.output,flush=True)
if __name__=="__main__":
    ap=argparse.ArgumentParser()
    ap.add_argument("--nf494-native",required=True)
    ap.add_argument("--nf495",required=True)
    ap.add_argument("--nf500",required=True)
    ap.add_argument("--nf501",required=True)
    ap.add_argument("--rank",default="notes/data/provisional/parents/pr350_original_BS_pruned_rank_bound.json")
    ap.add_argument("--source",default="notes/data/provisional/nf372_pr355_fields.json")
    ap.add_argument("--bits",type=int,default=4096)
    ap.add_argument("--output",required=True)
    main(ap.parse_args())
