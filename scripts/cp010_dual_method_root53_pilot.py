#!/usr/bin/env python3
"""CP010 true first-RS-zero cross-method candidate precision/accounting gate.

Two numerical-only candidate brackets for global positive zero index 53:
RS local index 1, and independently Euler-Maclaurin source-tested index 1.
Exact Fraction computes a one-exception full-roster operator error budget;
optional original SHA-verified RS source imposes genuine source nesting.
Optional mpmath screening is NOT proof of Hardy-Z signs or zero enclosure.
Direct real Zeta Lean v4.35 build is a completely separate mandatory gate.
"""
import argparse
import hashlib
import json
from fractions import Fraction as F
from pathlib import Path

from cp005_formal_zero_roster_adapter import E_tail, E_QUAD_ALLOWANCE, EPS_MAX, RADII
from cp008_real_first52_refinement_preflight import parse_candidate
from cp009_riemann_siegel_precision_policy import (
    N_RS, HALFWIDTH_BASE, row_weight, original_first52_error
)
from cp007_original_first52_precision_obstruction import parse_original52

ROOT=Path(__file__).resolve().parents[1]
DIR=ROOT/"cp010_zeta_v435"
EULER=DIR/"python/out/euler_maclaurin/zeros/zeros_00001.txt"
RS=DIR/"python/out/riemann_siegel/zeros/zeros_00001.txt"
E_MANIFEST=EULER.parent/"manifest.json"
R_MANIFEST=RS.parent/"manifest.json"
LEAN=DIR/"CP010DualMethods.lean"
SOURCE_RS_SHA="1029bed8a315d1b39d7c45e55a6476acbbf8baf1"
SOURCE_TAG="c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
COARSE=(F(15000,100),F(15010,100))
NARROW=(F(15005352,100000),F(15005353,100000))
SOURCE_COUNT=1748002

def gitblob(path):
    data=path.read_bytes()
    return hashlib.sha1(b"blob "+str(len(data)).encode()+b"\0"+data).hexdigest()

def strict_candidates():
    src=parse_original52()
    assert len(src)==52 and src[-1][1]==F(299,2)
    raw=EULER.read_text("utf-8").strip().split(",")
    original=ROOT/"data/cp007_original_euler_maclaurin_first52.txt"
    orig_last=[x.strip() for x in original.read_text("utf-8").strip().splitlines()[-1].split(",")]
    assert len(raw)==7 and raw[0].strip()=="1"
    assert [x.strip() for x in raw[3:]] == orig_last[3:] == ["92","93","20","20"]
    vals=(F(raw[1]),F(raw[2]))
    assert vals==NARROW
    rs=[x.strip() for x in RS.read_text("utf-8").strip().split(",")]
    assert len(rs)==3 and rs[0]=="1"
    assert (F(rs[1]),F(rs[2]))==COARSE
    assert COARSE[0]<NARROW[0]<NARROW[1]<COARSE[1]
    assert NARROW[1]-NARROW[0]==F(1,100000)
    assert COARSE[1]-COARSE[0]==F(1,10)
    for store,manifest,cols,last in [
        (EULER,E_MANIFEST,
         ["idx","left","right","left_cutoff","right_cutoff","left_bernoulli","right_bernoulli"],
         "150.05353"),
        (RS,R_MANIFEST,["idx","left","right"],"150.10")
    ]:
        meta=json.loads(manifest.read_text("utf-8"))
        assert meta["rows"]==1 and meta["cols"]==cols and meta["files"]==[
            {"file":"zeros_00001.txt","rows":1,"height":last}]
    lean=LEAN.read_text("utf-8")
    assert "build_batch 0 1" in lean and "build_batch_rs 0 1" in lean
    assert "BatchSpec 1 15005352 100000 15005353 100000" in lean
    assert "BatchSpec 1 15000 100 15010 100" in lean
    assert SOURCE_COUNT==N_RS+52
    return True

def analytic_rs_bound():
    """Published NamedRS remainder E(t)=25/(4t^1.25)+1/(32t^3.75)."""
    lower=F(25,4)/(F(150)*4) # 150^(1/4)<4, so E_RS(150)>1/96.
    upper=F(25,4)/(F(150)*3)+F(1,32)/(F(150)**3*27)
    assert lower==F(1,96) and lower<upper
    # 150^(1/4)>3 from 150>81. This is a rigorous rational
    # UPPER bound for the published analytic remainder at t>=150.
    return lower,upper

def budgets():
    assert strict_candidates()
    result={}
    for radius in RADII:
        L0=row_weight(radius,0)
        L7=row_weight(radius,7)
        base=E_tail(radius)+E_QUAD_ALLOWANCE + original_first52_error(radius) + N_RS*HALFWIDTH_BASE*L0
        assert base<EPS_MAX
        methods={}
        for name,interval in [("coarse_Riemann_Siegel",COARSE),("narrow_Euler_Maclaurin",NARROW)]:
            half=(interval[1]-interval[0])/2
            adjusted=base+(half-HALFWIDTH_BASE)*L7
            methods[name]={"halfwidth":str(half),"first_rs_localization":str(half*L7),
                            "conditional_total_upper":str(adjusted),
                            "within_target":adjusted<EPS_MAX}
        assert methods["narrow_Euler_Maclaurin"]["within_target"]
        assert not methods["coarse_Riemann_Siegel"]["within_target"]
        max_halfwidth=HALFWIDTH_BASE+(EPS_MAX-base)/L7
        assert F(1,200000)<max_halfwidth<F(1,20)
        result[str(radius)]={
            "conditional_uniform_base":str(base),
            "rs_root53_L7":str(L7),
            "max_one_exception_halfwidth_if_all_other_rs_at_2e-9":str(max_halfwidth),
            "two_methods":methods,
        }
        print(f"radius={radius}: one narrow Euler bracket full-roster conditional "
              f"{float(F(methods['narrow_Euler_Maclaurin']['conditional_total_upper'])):.12f} < 0.002")
        print(f"radius={radius}: one coarse RS bracket full-roster conditional "
              f"{float(F(methods['coarse_Riemann_Siegel']['conditional_total_upper'])):.12f} > 0.002")
        print(f"radius={radius}: first RS one-exception half-width ceiling "
              f"{float(max_halfwidth):.12f}")
    return result

def source_first_rs(original_full_shard):
    if gitblob(original_full_shard)!=SOURCE_RS_SHA:
        raise ValueError("Original external source RS shard full Git blob mismatch")
    with original_full_shard.open("r",encoding="ascii") as inp:
        fields=[x.strip() for x in inp.readline().strip().split(",")]
    if len(fields)!=3 or fields[0]!="1":
        raise ValueError("First original RS row is not local root index 1")
    orig=(F(fields[1]),F(fields[2]))
    if not (orig[0]<=COARSE[0]<NARROW[0]<NARROW[1]<COARSE[1]<=orig[1]):
        raise ValueError(f"Two proposed brackets do not both fit original first RS source interval {orig}")
    print(f"CP010 FIRST RS ORIGINAL SOURCE BLOBS MATCH; first RS true original row is [{orig[0]}, {orig[1]}]")
    print("Source inclusion does NOT assert a zero in the proposed candidate subintervals.")

def numeric_screen():
    import mpmath as mp
    mp.mp.dps=75
    g=mp.im(mp.zetazero(53))
    for name,(a,b) in [("coarse_RS",COARSE),("narrow_Euler",NARROW)]:
        l=mp.mpf(a.numerator)/a.denominator
        u=mp.mpf(b.numerator)/b.denominator
        za,zb=mp.siegelz(l),mp.siegelz(u)
        assert l<g<u and za*zb<0, f"Numerical-only Hardy Z pilot FAILED for {name}"
        print(f"{name}: HIGH-PRECISION NUMERICAL ONLY signs Z(a)={mp.nstr(za,18)}; "
              f"Z(b)={mp.nstr(zb,18)}; center numerical zero={mp.nstr(g,25)}")
    for a in [F(15000,100),F(15010,100),F(15005352,100000),F(15005353,100000)]:
        t=mp.mpf(a.numerator)/a.denominator
        z=abs(mp.siegelz(t))
        e=mp.mpf(25)/(4*t**mp.mpf("1.25"))+1/(32*t**mp.mpf("3.75"))
        print(f"t={a}: NUMERIC |Hardy Z|/analytic RS remainder "
              f"={mp.nstr(z/e,17)} (not a Lean error certificate)")
    print("NUMERICAL SCREEN NOT A ZERO CERTIFICATE, RIGOROUS INTERVAL, OR KERNEL PASS")

def main():
    p=argparse.ArgumentParser()
    p.add_argument("--self-test",action="store_true")
    p.add_argument("--numeric-screen",action="store_true")
    p.add_argument("--original-rs-shard",type=Path)
    p.add_argument("--out",type=Path)
    a=p.parse_args()
    if a.self_test:
        lo,hi=analytic_rs_bound()
        assert lo==F(1,96) and hi<F(1,70)
        print(f"ORIGINAL RS analytic remainder at t=150: {lo}<E_RS(150)<{hi} (valid rational inequalities)")
        results=budgets()
        print("CP010 REAL 53RD ZERO TWO-METHOD EXACT RATIONAL BUDGET PASS; NO LEAN KERNEL ACCEPTANCE")
        if a.out:
            a.out.write_text(json.dumps({"status":"CONDITIONAL_SOURCE_BUDGET_ONLY",
                                         "source_commit":SOURCE_TAG,"results":results},indent=2)+"\n")
    if a.numeric_screen:
        assert strict_candidates()
        numeric_screen()
    if a.original_rs_shard:
        assert strict_candidates()
        source_first_rs(a.original_rs_shard)
    if not (a.self_test or a.numeric_screen or a.original_rs_shard):
        p.print_help()

if __name__=="__main__":
    main()
