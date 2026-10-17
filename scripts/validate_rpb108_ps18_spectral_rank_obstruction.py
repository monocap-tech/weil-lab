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
