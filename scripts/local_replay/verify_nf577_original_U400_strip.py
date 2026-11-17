#!/usr/bin/env python3
"""NF577 exact arithmetic replay of the frozen NF494 U400 and strip constants.

Usage: python scripts/local_replay/verify_nf577_original_U400_strip.py NF494-native.zip
The archive can also be supplied as the raw JSON. Analytic source identity,
holomorphic majorant, Fourier integration by parts, and graph limits are not
proved by this script; see the accompanying NF577 note.
"""
import hashlib
import json
import sys
import zipfile
from pathlib import Path
from fractions import Fraction as F

if hasattr(sys, "set_int_max_str_digits"):
    sys.set_int_max_str_digits(0)

p = Path(sys.argv[1])
if zipfile.is_zipfile(p):
    with zipfile.ZipFile(p) as z:
        b = z.read("nf494-original-J8-source-H400-joint-compact-native.json")
else:
    b = p.read_bytes()
sha = hashlib.sha256(b).hexdigest()
assert sha == "39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181"
j = json.loads(b)
assert j["pass"] == "NF494-native"
assert j["original_nf407_source_sha256"] == "0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
assert j["original_nf406_seams_sha256"] == "c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
assert j["original_source_original_246_generators_273_modes"]
assert j["original_source_true_sinh_zero_rate_pole"]
B, d, R, N = F(11,10), F(1,500), F(1,25), 400
assert F(j["original_B"]) == B and F(j["original_true_terminal_delta"]) == d
assert F(j["original_source_analytic_Cauchy_radius"]) == R
assert j["original_source_400_jet_order"] == N
u = [(F(lo),F(hi)) for lo,hi in j["original_U_400_native_outward"]]
assert len(u) == N and all(lo <= hi for lo,hi in u)
a = [max(abs(lo),abs(hi)) for lo,hi in u]
q, CM = d/R, F(10)**400
t0 = CM*q**N/(1-q)
t1 = CM/R*q**(N-1)*(N/(1-q)+q/(1-q)**2)
assert t0 == F(j["original_original_U400_analytic_tail"])
M0 = sum(v*d**k for k,v in enumerate(a))+t0
M1 = sum(k*v*d**(k-1) for k,v in enumerate(a) if k)+t1
m0,m1 = F(1,5000000), F(7,10000)
assert M0 < m0 and M1 < m1 and u[0][1] < -F(1,10**11)
# log(2)>2/3 via atanh; e>27/10 via finite exponential sum.
assert B/2 < F(2,3)
assert sum(F(1,k) for k in (1,1,2,6,24,120)) > F(27,10)
assert F(27,10)**7 > B/d
c0,c1 = m0,m1+m0/2
C_half = F(1,40000)
# log(BT)<=1+log(2+T), log(B/d)<7; high T>=1/d.
assert (3*c0+4*c0+8*d*c1)*(1+d) < C_half
# Low T<=1/d, direct L1 estimate.
assert 8*d*c0*(1+1/d) < C_half
# The combined affine phase and mollifier factor is less than 2:
# s>=1/2, epsilon=(1-s)*d/4, c=B-d/2.
c=B-d/2
assert (c+d/4)/4 < F(2,3)
C_target=2*C_half
C_seed=4*C_half
assert C_seed == F(1,10000)
print("NF577 exact rational arithmetic PASS; SHA256",sha)
print("M0",float(M0),"M1",float(M1),"U(B) upper",float(u[0][1]))
print("tail0",float(t0),"tail1",float(t1))
print("half/target/common envelope constants",C_half,C_target,C_seed)
print("Cauchy/source identity and analytic/Lean graph obligations are separate.")
