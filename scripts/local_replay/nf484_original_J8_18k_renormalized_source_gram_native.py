#!/usr/bin/env python3
"""NF484 source-native authentic 18k leading-cancelled image PURE quadratic Gram.

Input: nine independent 4096-bit all-273-mode original-source NF484
c_m=T_m, d_m=T_m-U(B)/(m+1/4) outward source balls, m=0...17999.
Reconstruct d_m as exact signed fixed-point integer coefficients (all
original source signs/correlations retained); two full convolution and
one cross correlation via python-flint exact fmpz_poly, and integrate the
resulting finite physical image square on terminal J8 [B-1/500,B] using
4096-bit rigorously enclosed Arb analytic exponential moment kernels.

The small reflected image is truncated only in its coefficient *tail*
m>=360 with a paid original-source exact geometric bound <1e-230.
Source input + rounding are conservatively paid at <1e-230 uniform
finite-image amplitude, hence <1e-40 *squared-energy* error even for original\nlow-m image source amplitudes as large as 10^180 (source correlations\nmust still be preserved to obtain the complete small physical signed scalar). This
remains ONLY the renormalized finite-image-square component, not the
mixed original complete J8 signed energy, original 19 Phi moments or
NF404. Never substitute a scalar Gram for the complete physical response.
"""
from __future__ import annotations
import argparse,json,sys,hashlib
from pathlib import Path
from fractions import Fraction as F
from flint import arb, fmpz_poly, ctx
from nf415_original_cell6_I1_validated_acb import A
from nf454_original_n9_contact_native_moment import enclosure
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10);DELTA=F(1,500)
M=18000;R=360;S=10**240;BITS=4096
SRC="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def iv(v):
    a,b=map(F,v);assert a<=b
    return a,b
def load(p):
    content=Path(p).read_bytes()
    return json.loads(content),hashlib.sha256(content).hexdigest()
def integer_coarsen(lo,hi):
    assert lo<=hi
    middle=(lo+hi)/2*S
    # exact fixedpoint floor, outward 1 unit charged separately
    return middle.numerator//middle.denominator
def integral_kernel(lam):
    # On terminal d>=0: exact Arb of ∫_0^(1/500) exp(-lam*d)dd.
    # λ rational half-integer or integer; λ=0 removable value.
    if lam==0:return A(DELTA)
    x=A(lam)*A(DELTA)
    return (1-(-x).exp())/A(lam)
def dec(x):
    from decimal import Decimal,localcontext
    with localcontext() as c:
        c.prec=48
        return str(Decimal(x.numerator)/Decimal(x.denominator))
def main():
    ap=argparse.ArgumentParser()
    ap.add_argument("--input-dir",required=True)
    ap.add_argument("--output",required=True)
    args=ap.parse_args()
    ctx.prec=BITS
    data=Path(args.input_dir)
    cballs=[];dballs=[];shas=[]
    vg=None
    for start in range(0,M,2000):
        p=data/f"nf484-source-renormalized-{start}-{start+2000}.json"
        q,sha=load(p);shas.append({"start":start,"sha256":sha})
        assert q["pass"]=="NF484-source-native"
        assert q["original_nf407_source_sha256"]==SRC
        assert q["original_nf406_seams_sha256"]==SEAM
        assert q["native_precision_bits"]==BITS
        assert q["original_246_generators"] and q["original_273_grouped_modes"] and q["original_sinh_m0_removable_pole"]
        assert q["all_finite_original_image_coefficients_m_from"]==start
        assert q["all_finite_original_image_coefficients_m_stop"]==start+2000
        assert q["original_source_input_radii_sum_lt"]=="1e-700"
        rows=q["original_source_Tm_and_same_source_dm_outward"]
        assert len(rows)==2000
        v=iv(q["original_source_v_at_B_outward"])
        assert v[1]<0
        if vg is None:vg=v
        else:assert v[0]<=vg[1] and vg[0]<=v[1]
        for j,row in enumerate(rows):
            assert len(row)==4
            c=iv(row[:2]);d=iv(row[2:])
            assert c[1]-c[0]<F(1,10**240)
            assert d[1]-d[0]<F(1,10**240)
            aa=F(4*(start+j)+1,4)
            # Shared source identity T_m - d_m = v/a_m, exact raw
            assert c[0]-d[1]<=v[1]/aa and v[0]/aa<=c[1]-d[0]
            cballs.append(c);dballs.append(d)
    assert len(cballs)==len(dballs)==M and len(shas)==9
    maxd=max(max(abs(a),abs(b)) for a,b in dballs)
    assert maxd<F(10)**180,("source residual amplitude > 1e180, revise global norm",dec(maxd))
    D=[]
    for lo,hi in dballs:
        q=integer_coarsen(lo,hi)
        # Native midpoint rounding plus unchanged source dyadic input
        # epsilon 10^-50 for each coefficient is heavily overcharged.
        assert lo-F(1,10**230) <= F(q,S) <= hi+F(1,10**230)
        D.append(q)
    assert len(D)==M
    E=[]
    for m in range(R):
        a=A(F(D[m],S))
        exp=(-A(B)*(4*m+1)).exp()
        val=a*exp
        lo,hi=enclosure(val,420)
        assert hi-lo<F(1,10**240)
        q=integer_coarsen(lo,hi)
        assert lo-F(1,10**240)<=F(q,S)<=hi+F(1,10**240)
        E.append(q)
    # Remainder of negative endpoint family m>=R over *entire* true
    # physical terminal δ: exp(-2a_m(2B-d)) =
    # exp(-(4m+1)(B-d/2)) <=(3/8)^(4m+1)
    # since B-d/2>=B-δ/2 =1.099>log(8/3).
    # Crucial: old 1/100 assumption is NOT valid for the actual low-m
    # source before central/regular cancellation; use ACTUAL maxd.
    neglected_right=maxd*F(3,8)**(4*R+1)/(1-F(3,8)**4)
    assert neglected_right<F(1,10**230)
    # Original source input S0<1e-700; k<=13, a_m>=1/4,
    # each source original input error is amplified by at most
    # 4*(B+26)^13<1e20, and |δv|/a<=4*10*S0,
    # hence each original dm input error <1e-679. Charge 1e-230.
    assert 4*(B+26)**13<F(10)**20
    each_round_source=F(2,10**230)
    epsilonI=F(1,10**224)
    # Left: 18k original source coefficient midpoint+input deltas,
    # right: R=360 coefficients and at most exp(δ(4R-1)/2)<5;
    # tiny remaining actual source right family. The 1/2 in I_m
    # is retained, no false all-J8 endpoint source tail.
    bound_deltaI=(F(M,2)+F(5*R,2))*each_round_source+neglected_right/2
    assert bound_deltaI<epsilonI
    # True full original finite renormalized image bound on
    # this original terminal uses ACTUAL full original source maxd,
    # not a false uniform 1/100 low-image coefficient assumption.
    amplitude_sup=(M+R)*maxd
    energy_fee=DELTA*(2*amplitude_sup*epsilonI+epsilonI**2)
    assert energy_fee<F(1,10**40)
    # All products of *signed original source data*, never absolute
    # squares of independent source contributions.
    print("NF484 exact source integer polynomial convolutions begin",flush=True)
    # Fixedpoint b_m eventually rounds to EXACT ZERO: at 100 decimal
    # places the original right reflected modes near m=120 are already
    # far smaller than 10^-100. A sparse trailing zero is NOT lost
    # source evidence: the <=2e-50 per right-coefficient overcharge
    # already includes EVERY m<120 exact true source value.
    # python-flint fmpz_poly canonically trims trailing zeros. Use the
    # actual NONZERO original right coefficient length for the
    # convolution exponent shift, not the nominal R=120 cutoff.
    Ractive=1
    for j,value in enumerate(E):
        if value:Ractive=j+1
    assert 1<=Ractive<=R
    right_finite=E[:Ractive]
    left=fmpz_poly(D)
    right=fmpz_poly(right_finite)
    LL=left*left
    RR=right*right
    LR=left*fmpz_poly(right_finite[::-1])
    assert len(LL)==2*M-1 and len(RR)==2*Ractive-1 and len(LR)==M+Ractive-1
    den=A(F(S*S))
    Il=arb(0);Ir=arb(0);Ic=arb(0)
    for s in range(len(LL)):
        v=int(LL[s])
        if v:Il+=A(F(v))*integral_kernel(2*s+1)
        if (s+1)%5000==0:print("NF484 left signed original image Gram moments",s+1,"/",len(LL),flush=True)
    for s in range(len(RR)):
        v=int(RR[s])
        if v:Ir+=A(F(v))*integral_kernel(-(2*s+1))
    for j in range(len(LR)):
        v=int(LR[j])
        if v:Ic+=A(F(v))*integral_kernel(2*(j-(Ractive-1)))
        if (j+1)%5000==0:print("NF484 signed original image cross-correlation moments",j+1,"/",len(LR),flush=True)
    Egram=(Il+Ir-2*Ic)/(4*den)
    Elo,Ehi=enclosure(Egram,105)
    assert Elo>=0,("ACTUAL original square enclosure unexpectedly negative",str(Elo))
    outward_lo=max(F(0),Elo-energy_fee)
    outward_hi=Ehi+energy_fee
    assert F(0)<=outward_lo<outward_hi<F(1,100)
    # The linear mean of the same original renormalized finite source:
    # I_m=1/2[sum_m D_m e^{-(2m+1/2)d}
    # -sum_m E_m e^{+(2m+1/2)d}].
    mu=arb(0)
    for m,q in enumerate(D):
        if q:mu+=A(F(q))*integral_kernel(F(4*m+1,2))
    for m,q in enumerate(right_finite):
        if q:mu-=A(F(q))*integral_kernel(-F(4*m+1,2))
    mu/=(2*A(F(S)))
    mlo,mhi=enclosure(mu,105)
    mean_lo=mlo-DELTA*epsilonI
    mean_hi=mhi+DELTA*epsilonI
    assert mean_lo<=mean_hi
    out={
      "pass":"NF484",
      "standing":"original source 246/273 exact coefficient-contracted genuine 18k same-source mu0-leading-cancelled matched-image finite GRAM and finite mean, first actual terminal scalar-component numerical interval; remaining central+seven-prime+19 endpoint Phi mixed physical D upper OPEN",
      "source_original_nf407_sha256":SRC,"original_nf406_seams_sha256":SEAM,
      "actual_original_m0_sinh_pole_included":True,
      "native_original_full_4096bit_source_generator_blocks":9,
      "original_full_M_image_coefficients":M,
      "original_right_image_tail_kept_m_lt":R,
      "original_right_image_fixedpoint_effective_length":Ractive,
      "original_right_image_fixedpoint_trailing_zeros_pay_rounding":True,
      "original_full_source_mode_groups":273,
      "original_original_source_input_radius_total_lt":"1e-700",
      "source_original_same_v_U_B_leading_cancellation":"d_m=T_m-v/(m+1/4), v EXACT same NF407 original physical source",
      "source_original_v_outward":[str(vg[0]),str(vg[1])],
      "original_maximum_renormalized_dm_abs_upper":str(maxd),
      "native_original_18k_source_fragments_sha256":shas,
      "finite_renormalized_source_Gram_fmpz_convolution_lengths":[len(LL),len(RR),len(LR)],
      "genuine_original_J8_terminal_interval":["549/500","B"],
      "physical_terminal_delta":"1/500",
      "original_source_fixedpoint_precision_digits":240,\n      "original_original_source_large_low_m_modes_supported":True,\n      "original_true_finite_image_uniform_sup_original_source_bound":str(amplitude_sup),
      "original_true_right_image_m_ge_120_geometric_discarded_upper":str(neglected_right),
      "original_true_right_image_geometric_discarded_upper_decimal":dec(neglected_right),
      "original_finite_image_uniform_input_native_rounding_error_upper":str(epsilonI),
      "original_finite_image_square_integral_error_charge":str(energy_fee),
      "original_finite_image_square_integral_error_charge_decimal":dec(energy_fee),
      "source_original_only_finite_image_renormalized_squared_Gram_interval":[str(outward_lo),str(outward_hi)],
      "source_original_only_finite_image_renormalized_squared_Gram_interval_decimal":[dec(outward_lo),dec(outward_hi)],
      "source_original_finite_image_renormalized_linear_terminal_integral_interval":[str(mean_lo),str(mean_hi)],
      "source_original_finite_image_renormalized_linear_terminal_integral_decimal":[dec(mean_lo),dec(mean_hi)],
      "squared_component_type":"∫_549/500^B (1/2 sum_m<18000 (T_m-v/a_m) [e^-2a_m(B-x)-e^-2a_m(B+x)])² dx",
      "linear_component_type":"∫_549/500^B (1/2 sum_m<18000 (T_m-v/a_m) F_m(x)) dx",
      "original_actual_terminal_mixed_pz_complete_integrated":False,
      "original_actual_terminal_full_z2_complete_integrated":False,
      "original_full_19_Phi_moments_mixed_integrated":False,
      "original_actual_terminal_signed_D8_upper":"OPEN",
      "NF404":"OPEN","W_ODD_NEG":"OPEN","RH":"OPEN",
      "next_bold":"NF485 preserve all computed original image Gram and mean; add complete central + n2,3,4,5,7,8,9 source regular, exact H-principal cancellation and 19 Phi-mixed original signed J8 terminal moments to compare NF404"
    }
    path=Path(args.output);path.parent.mkdir(parents=True,exist_ok=True)
    path.write_text(json.dumps(out,indent=2)+"\n")
    print("NF484 original true renormalized 18k finite matched-image quadratic Gram",dec(outward_lo),dec(outward_hi),flush=True)
    print("NF484 original true renormalized 18k finite matched-image linear integral",dec(mean_lo),dec(mean_hi),flush=True)
    print("NF484 full original terminal mixed signed D8 UPPER, NF404, W_ODD_NEG, RH remain OPEN",flush=True)
if __name__=="__main__":main()
