#!/usr/bin/env python3
"""NF20: exact original native two-mode source Gram obstruction.

Certified inputs: NF17 complete original signed E112, NF18 first exterior
and NF19 second exterior; NF19's independently exact 58x58 Bareiss strict
R2 lower bounds are used as declared dependencies, NOT recomputed here.

For the finite polynomial E112 source, the physical L2 representative
s_x exists: Fourier decay O(1/|xi|) dominates logarithmic-symbol growth.
Its norm satisfies ||s_x||² >= ||(Q(x,e_first),Q(x,e_second))||².
The standard bound
G(x) <= ||s_x||²/kappa therefore cannot prove A-G>0 on every x;
the first two measured columns ALREADY make its upper estimate >4 A
in one even direction and >19/5 A in one odd direction.
This says nothing about the *actual* inverse or RH sign.
"""
import argparse,gzip,json,hashlib
from fractions import Fraction as F

SHA={
"E112":"f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81",
"first":"da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee",
"second":"0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad",
}
KAPPA=F(207,1000)
R2_LOWER={"even":F(302,1000),"odd":F(275,1000)}

def read(path,expected):
    with gzip.open(path,'rb') as f: raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==expected
    return json.loads(raw)

def certify(e112,first,second):
    a=read(e112,SHA["E112"]);b=read(first,SHA["first"]);c=read(second,SHA["second"])
    assert a["aperture"]==b["aperture"]==c["aperture"]=="53/50"
    assert a["dim"]==112 and b["new_columns"]==[112,113] and c["new_columns"]==[114,115]
    assert b["parent_sha256"]==SHA["E112"]
    assert c["parent_E112_SHA256"]==SHA["E112"]
    assert c["parent_first_boundary_SHA256"]==SHA["first"]
    src={**a["complete_form"],**b["original_full_source"],**c["original_full_source"]}
    assert len(src)==3422
    def ends(key):return tuple(map(F,src[key]["full"]))
    def gt(key,value):
        lo,hi=ends(key);assert lo>F(value),(key,str(lo))
    def abs_lt(key,value):
        lo,hi=ends(key);assert max(abs(lo),abs(hi))<F(value),(key,str(lo),str(hi))
    gt("112,112",F(69,20));gt("114,114",F(7,2))
    abs_lt("112,114",F(13,20))
    gt("113,113",F(339,100));gt("115,115",F(351,100))
    abs_lt("113,115",F(1,2))
    # 2-by-2 Gershgorin lower eigenvalue, obtained from native intervals.
    high_floor={"even":F(14,5),"odd":F(289,100)}
    ratio={k:high_floor[k]*R2_LOWER[k]/KAPPA for k in ("even","odd")}
    assert ratio["even"]>4 and ratio["odd"]>F(19,5)
    return dict(status="PASS",aperture="53/50",source_sha256=SHA,
       original_high_physical_complement_lower=str(KAPPA),
       first_two_high_Gram_strict_eigenvalue_floors={k:str(v) for k,v in high_floor.items()},
       certified_NF19_two_mode_reaction_strict_lower={k:str(v) for k,v in R2_LOWER.items()},
       strict_lower_on_physical_source_Gram_over_kappa_relative_to_A={k:str(v) for k,v in ratio.items()},
       even_crude_relative_source_upper_bound_exceeds_retained_energy_by_more_than_factor=4,
       odd_crude_relative_source_upper_bound_exceeds_retained_energy_by_more_than_factor="19/5",
       physical_source_representation_for_finite_E112_proved_by_BV_log_multiplier=True,
       valid_unconditionally_as_two_column_native_bilinear_test=True,
       actual_infinite_inverse_sign_evaluated=False,whole_aperture_positive=False,
       arithmetic_nonimplication_from_full_Weil_identities_proved=False)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("e112");p.add_argument("first_boundary");p.add_argument("second_boundary")
    a=p.parse_args()
    print(json.dumps(certify(a.e112,a.first_boundary,a.second_boundary),indent=2))
