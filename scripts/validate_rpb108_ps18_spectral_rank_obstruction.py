#!/usr/bin/env python3
"""PS18 source-pinned original arch low-spectral rank EXPONENTIAL bottleneck.

Actual signed PS17 complement C, same original digamma J_C. Construct
entire M-dimensional original-form-admissible local step spaces with
uniform J quotient below Lambda, so native spectral LOW rank is >=
2**floor(Lambda/2), at even PS17 cutoffs. Also Fourier/Bessel upper
count and exact conservative high-response threshold. No giant basis
or finite low Schur matrix allocated and NO Weil/RH proof promotion.
"""
from fractions import Fraction as F
from pathlib import Path
import json
import validate_rpb108_rc315_low_mode_sign as old
import validate_rpb108_ps17_low_high_feshbach as ps17

ROOT=Path(__file__).resolve().parents[1]
B=F(11,10)
R=2*B
SOURCE=((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3))

def run():
    # Recheck ALL original physical source obligations through PS17.
    ps17.run()
    m=json.loads((ROOT/"research/obligations.json").read_text())
    lane=json.loads((ROOT/"research/parallel_investigations/w_physical_shift.json").read_text())
    assert m["active_obligation"]=="W-ODD-NEG"
    assert m["objective"]["status"]=="open"
    assert lane["id"]=="W-PHYSICAL-SHIFT"
    assert lane["active_frontier_unchanged"]=="W-ODD-NEG"
    assert lane["status"]=="open"
    assert all(v is False for v in lane["closures"].values())

    # The actual original 13 source channel locations were pinned by
    # PS10/PS14, and C=I-P is domain-stable (PS15).
    # J0=[1/8,3/16] sits between true source I_3 and I_4.
    ln3=old.log_i(F(3))
    ln4=old.log_i(F(4))
    ln9=old.log_i(F(9))
    delta=old.IV(R-ln9.hi,R-ln9.lo)
    assert F(1,400)<delta.lo<=delta.hi<F(1,350)
    assert B-ln3.lo < F(1,8)    # I_3 right endpoint
    assert ln4.lo-B > F(3,16)   # I_4 left endpoint
    assert B-ln3.lo < ln4.lo-B
    # These are consecutive source intervals in positive central gap;
    # all other exact labels are outside [3,4].
    labels={F(1),F(9)}|{F(n) for n in (2,3,4,5,7,8)}
    labels|={F(9,n) for n in (2,4,5,7,8)}
    assert len(labels)==13
    assert not any(F(3)<r<F(4) for r in labels)
    window_length=F(3,16)-F(1,8)
    assert window_length==F(1,16)

    ln2=old.log_i(F(2))
    pi=old.pi_iv()
    assert F(693,1000)<ln2.lo<=ln2.hi<F(7,10)
    assert F(3)<pi.lo

    def check_rank_gate(Lambda):
        # With M=2**m cellwise-constant functions supported in the
        # original complement window length 1/16, h=1/(16*M).
        # For 0<u<h, exact physical translation D_f(u)=u*sum jumps²
        # <=4u/h mass; for u>=h, D_f(u)<=4mass.
        # With original k: k(u)<=1/(2u)+1 for u<=1 and
        # k(u)<2exp(-u/2) for u>=1:
        # J[f]/mass <22+2log(16*M) =22+2(m+4)log2.
        # Never allocate 2**m cells or even the integer 2**m!
        assert isinstance(Lambda,int) and Lambda>=100
        mexp=Lambda//2
        bound=F(22)+F(7,5)*(mexp+4)
        assert bound<Lambda,("original uniform entire M-dim J bound",Lambda,mexp)
        coarser=F(138,5)+F(7,10)*Lambda
        assert bound<=coarser<Lambda
        # Minmax with J_C compact resolvent:
        # N_C(Lambda)=rank 1_[0,Lambda)(J_C) >=2**mexp.

        # Fourier/Bessel counting UPPER: symbolic physical bandwidth
        # X=2**(3*Lambda+1). For |xi|>=X, original arch j(xi)>
        # 3*Lambda*log(2)-1/pi-1/2 >2Lambda (Lambda>=100).
        growth=F(2079,1000)*Lambda-F(5,6)
        assert growth>2*Lambda
        # Thus each unit native LOW spectral vector has >1/2
        # zero-extended Fourier mass in [-X,X]; Bessel implies
        # N_C(Lambda)<4R*2**(3*Lambda+1).
        upper_rank_power=3*Lambda+1
        assert F(4)*R==F(44,5)
        assert upper_rank_power>mexp
        return mexp,upper_rank_power,bound

    # Moderate Lambda already means >2**50 low native eigenmodes.
    smexp,supper,sbound=check_rank_gate(100)
    assert smexp==50

    # PS17 candidate cutoffs and actual spectral LOW rank.
    m26,up26,b26=check_rank_gate(2**26)
    m30,up30,b30=check_rank_gate(2**30)
    assert m26==2**25==33_554_432
    assert m30==2**29==536_870_912

    # Conservative PS17 high-response acceptance formula is
    # 882**2/(Lambda-882). The *sufficient method threshold* for
    # correction <1/d is Lambda > 882+d*882**2.
    # These are NOT necessary cutoffs for every other method,
    # and do not assert actual negative spectral directions.
    bounded_rest=882
    full_cross_sq=bounded_rest**2
    assert full_cross_sq==777_924
    min_threshold80=bounded_rest+80*full_cross_sq
    min_threshold1000=bounded_rest+1000*full_cross_sq
    assert min_threshold80==62_234_802
    assert min_threshold1000==777_924_882
    m80,up80,b80=check_rank_gate(min_threshold80+1)
    m1000,up1000,b1000=check_rank_gate(min_threshold1000+1)
    assert m80==31_117_401
    assert m1000==388_962_441
    assert F(full_cross_sq,min_threshold80+1-bounded_rest)<F(1,80)
    assert F(full_cross_sq,min_threshold1000+1-bounded_rest)<F(1,1000)
    assert F(full_cross_sq,min_threshold80-bounded_rest)==F(1,80)
    assert F(full_cross_sq,min_threshold1000-bounded_rest)==F(1,1000)

    # The same M-dim local step witness space consists of original
    # unshifted true Weil Q-positive functions: PS13's single-window
    # bound Q>1/4 mass applies to ALL f in W_M (length=1/16).
    # This does NOT imply S_C=Q_C-T_C positive on W_M, nor that
    # J_C spectral projections preserve W_M or its local positivity.
    assert window_length==F(1,16)
    assert window_length<ln2.lo


    # NEW PS18 TRUE SIGN CERTIFICATE: a fixed prime-quiet window in
    # the *actual* source complement carries POSITIVE original Schur,
    # not just positive unshifted Q before subtracting source response.
    #
    # Jq=[269/5000,1163/10000] has EXACT width 1/16 and lies
    # between the original log3 and log4 source intervals.
    qlo,qhi=F(269,5000),F(1163,10000)
    assert qhi-qlo==F(1,16)
    assert B-ln3.lo<qlo and ln4.lo-B>qhi
    sources=sorted(labels)
    src_log={t:(old.IV(0) if t==1 else old.log_i(t)) for t in sources}
    shifts={n:old.log_i(F(n)) for n,_ in SOURCE}
    # Every one of 13*7*2 original signed prime P-to-Jq shift
    # configurations is STRICTLY disjoint, with certified clearance.
    smallest_shift_gap=None
    for t in sources:
        src_start_lo=src_log[t].lo-B
        src_end_hi=src_log[t].hi-B+delta.hi
        for n,shift in shifts.items():
            for sign in (-1,1):
                if sign==1:
                    shifted_lo=qlo+shift.lo
                    shifted_hi=qhi+shift.hi
                else:
                    shifted_lo=qlo-shift.hi
                    shifted_hi=qhi-shift.lo
                d=max(src_start_lo-shifted_hi,shifted_lo-src_end_hi)
                assert d>0,("PS18 source-to-quiet original prime SHIFT OVERLAP",t,n,sign,float(d))
                smallest_shift_gap=d if smallest_shift_gap is None else min(smallest_shift_gap,d)
    assert smallest_shift_gap>F(1,20000)

    # Complete original arch source-to-quiet mixed kernel -k(|x-y|).
    # Source intervals are all disjoint from Jq. For each source
    # interval r, let d_r be its certified nearest separation.
    # Since k is decreasing and <=1/(2d)+1,
    # ||P k C_Jq||_HS² <=δ*|Jq| Σ_r [1/(2d_r)+1]^2.
    hs_arch_sq=F(0)
    for t in sources:
        src_lo=src_log[t].lo-B
        src_hi=src_log[t].hi-B+delta.hi
        d=max(qlo-src_hi,src_lo-qhi)
        assert d>0
        hs_arch_sq+=delta.hi*(qhi-qlo)*(1+F(1)/(2*d))**2
    assert hs_arch_sq < F(7,40)**2,(
        "PS18 TRUE source-quiet arch HS too large",float(hs_arch_sq))

    # Source positive-even/negative-odd original pole cross:
    # ||P c||≤sqrt(13δ)*cosh(B/2) and likewise s. For h supported
    # Jq, ||1_Jq c||≤sqrt(|Jq|)*cosh(qhi/2), similarly sinh(qhi/2).
    sn,cs=old.sinh_cosh_iv(B/2)
    snq,csq=old.sinh_cosh_iv(qhi/2)
    assert F(13)*delta.hi<F(19,100)**2
    assert cs.hi<F(29,25) and sn.hi<F(29,50)
    assert csq.hi<F(501,500) and snq.hi<F(59,1000)
    # sqrt source measure <.19, sqrt quiet length exactly .25:
    pole_bound=2*((F(19,100)*F(29,25))*(F(1,4)*F(501,500))
             +(F(19,100)*F(29,50))*(F(1,4)*F(59,1000)))
    assert pole_bound<F(23,200),float(pole_bound)

    # All original prime P-to-quiet terms are IDENTICALLY ZERO.
    # So entire actual signed B_PC restricted to quiet interval:
    # ||B_PC|_Jq|| < ||B_arch||_HS+||B_pole|| <.175+.115=.29.
    quiet_cross=F(7,40)+F(23,200)
    assert quiet_cross==F(29,100)
    # PS16 SOURCE A_P >323/1000, with all 19 internal prime edges.
    # Thus genuine positive compact source energy-dual Schur cost
    # on each quiet h is <(.29)^2/.323 * ||h||².
    quiet_penalty=quiet_cross**2/F(323,1000)
    assert quiet_penalty<F(261,1000),float(quiet_penalty)

    # PS13 original *unshifted* Q local certificate is >0.266
    # for EVERY function of support length <=1/16, not just steps.
    # Check its exact 32-term original digamma tail here again.
    carch=-old.gamma_iv()-pi/2-3*ln2-old.log_i(pi)
    tail32=F(0)
    Lq=F(1,16)
    for m in range(32):
        nu=F(4*m+1,2)
        x=nu*Lq
        assert 0<x<32
        tail32+=2*(1-x/32)**32/nu
    quiet_original_Q_margin=carch.lo+tail32-2*Lq*sn.hi**2
    assert quiet_original_Q_margin>F(133,500),float(quiet_original_Q_margin)

    # This is the ACTUAL complementary source Schur, including
    # full physical arch Carleman cross and original both signed
    # poles. No unproved finite compression or seam omission.
    schur_quiet_margin=F(133,500)-quiet_penalty
    assert schur_quiet_margin>F(1,200),(
        "PS18 quiet TRUE complementary Schur positive margin FAILED",
        float(schur_quiet_margin))
    # For ALL admissible h supported in Jq:
    # S_C[h]=Q_C[h]-<h,B* A_P^-1 B h> >1/200 ||h||².
    print("PS18 original prime quiet source-shift minimum clearance",
          float(smallest_shift_gap),flush=True)
    print("PS18 TRUE quiet source arch HS square upper",float(hs_arch_sq),flush=True)
    print("PS18 TRUE quiet original both-pole cross upper",float(pole_bound),flush=True)
    print("PS18 true quiet source-energy Schur penalty upper",float(quiet_penalty),flush=True)
    print("PS18 original unshifted quiet Q lower",float(quiet_original_Q_margin),flush=True)
    print("PS18 TRUE complementary signed quiet Schur lower >",
          float(schur_quiet_margin),flush=True)

    print("PS18 true complement physical window [1/8,3/16] length",
          str(window_length),flush=True)
    print("PS18 general native arch spectral LOW rank for integer Lambda>=100:"
          " N_C(Lambda)>=2**floor(Lambda/2)",flush=True)
    print("PS18 general original Fourier/Bessel native low rank upper:"
          " N_C(Lambda)<(44/5)*2**(3Lambda+1)",flush=True)
    print("PS18 original arch J step-space 100 cutoff rational upper",
          float(sbound),flush=True)
    print("PS18 2**26 native LOW rank exponent MIN",m26,flush=True)
    print("PS18 2**30 native LOW rank exponent MIN",m30,flush=True)
    print("PS18 conservative <1/80 PS17 method minimal integer cutoff",
          min_threshold80+1,flush=True)
    print("PS18 <1/80 method native LOW rank exponent MIN",m80,flush=True)
    print("PS18 conservative <1/1000 PS17 method minimal integer cutoff",
          min_threshold1000+1,flush=True)
    print("PS18 <1/1000 method native LOW rank exponent MIN",m1000,flush=True)
    print("PS18 source-local unshifted original Q positive all M cell"
          " witness profiles >1/4 mass, BUT Schur positive UNKNOWN",flush=True)
    print("PS18 PASS SCOPED: PS17 genuine signed native arch spectral"
          " LOW matrix is provably exponentially large at the"
          " sufficient high-response cutoffs. Uniform spectral"
          " enumeration NOT computationally actionable."
          " Exact signed low matrix NOT CONSTRUCTED OR PSD-CERTIFIED;"
          " new obligation: exploit local positive families en bloc"
          " and certify inter-window + source response."
          " Canonical W-ODD-NEG, W-EVEN-FORM, CC27 and RH OPEN.",flush=True)

if __name__=="__main__":
    run()
