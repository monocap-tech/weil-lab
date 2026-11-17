#!/usr/bin/env python3
"""Verify the exact compressed Lean ceiling table against a fresh direct
NF587 full primitive coefficient-box interval receipt. No floating point.
The archived NF494 receipt produced the same 400 integer ceilings.
This audits finite data, not a Lean embedding of Arb's interval proofs.
"""
import hashlib
import json
import re
import sys
import zipfile
from pathlib import Path
from fractions import Fraction as F

if hasattr(sys,"set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)
ROOT = Path(__file__).resolve().parents[2]
TABLE = ROOT/"WeilDefect/Arithmetic/ActualZetaOriginalU400NormalizedBudget.lean"
p=Path(sys.argv[1])
raw=(zipfile.ZipFile(p).read("nf587-full-box-U400.json")
     if zipfile.is_zipfile(p) else p.read_bytes())
j=json.loads(raw)
assert j["pass"]=="NF587-full-box-normalized-400-jet"
assert j["original_nf407_source_sha256"]=="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
assert j["direct_source_box"] and j["actual_sinh_pole"]
assert j["selected"]==242 and j["critical"]==4 and j["grouped_modes"]==273
assert j["N"]==400 and j["precision_bits"]==4096
assert F(j["B"])==F(11,10) and F(j["delta"])==F(1,500)
assert F(j["cauchy_R"])==F(1,25) and F(j["cauchy_M"])==10**400
text=TABLE.read_text()
block=text.split("def neutralNF588U400CeilPrefix",1)[1].split(":=",1)[1].split("]",1)[0]
prefix=list(map(int,re.findall(r"\d+",block)))
assert len(prefix)==67
b=prefix+[1]*(400-len(prefix))
Q=10**40
iv=[(F(lo),F(hi)) for lo,hi in j["normalized_intervals"]]
assert len(iv)==400 and all(lo<=hi for lo,hi in iv)
actual=[]
for lo,hi in iv:
    r=Q*max(abs(lo),abs(hi))
    actual.append(-(-r.numerator//r.denominator))
assert b==actual
S0=sum(b); S1=sum(n*v for n,v in enumerate(b))
assert S0==1965965555768486224139685001519513
assert S1==13914197645839925749935241233441099
q=F(1,20);M=F(10)**400
T0=M*q**400/(1-q)
T1=500*M*q**400*(400/(1-q)+q/(1-q)**2)
assert T0==F(j["tail0"]) and T1==F(j["tail1"])
assert F(S0,Q)+T0 < F(2,10**7)
assert F(500*S1,Q)+T1 < F(7,10**4)
assert iv[0][1]<-F(1,10**11)
print("NF588 normalized exact ceiling audit PASS (all 400)",hashlib.sha256(raw).hexdigest())
print("integer sums",S0,S1)
