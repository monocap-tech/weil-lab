#!/usr/bin/env python3
"""NF368 exact rational four-mode margin; inherited PR348/PR355 evidence only."""
import argparse, hashlib, zipfile, io, json
from fractions import Fraction as F
ZIP_SHA="f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0"
FOUR_SHA="a84b19c1fefc4e680c5c19ea643bbe5badce639374cb0a424211ee980020f922"
EXT_SHA="d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9"
def dyad(p):
    n,e=map(int,p)
    return F(n<<e) if e>=0 else F(n,1<<(-e))
def positive_ldlt(A):
    L=[[F(i==j) for j in range(4)] for i in range(4)];d=[]
    for k in range(4):
        p=A[k][k]-sum((L[k][j]**2*d[j] for j in range(k)),F(0))
        assert p>0,("nonpositive pivot",k)
        d.append(p)
        for i in range(k+1,4):
            L[i][k]=(A[i][k]-sum((L[i][j]*L[k][j]*d[j] for j in range(k)),F(0)))/p
    return d
def main():
    parser=argparse.ArgumentParser();parser.add_argument("--offline",required=True);args=parser.parse_args()
    raw=open(args.offline,"rb").read()
    assert hashlib.sha256(raw).hexdigest()==ZIP_SHA
    with zipfile.ZipFile(io.BytesIO(raw)) as z:
        a=z.read("original_four_mode_critical_block.json")
        b=z.read("original_exterior_scalar_floor_stop.json")
        c=z.read("original_BS_pruned_rank_bound.json")
    assert hashlib.sha256(a).hexdigest()==FOUR_SHA
    assert hashlib.sha256(b).hexdigest()==EXT_SHA
    four=json.loads(a);ext=json.loads(b);rank=json.loads(c)
    assert four["near_critical_dimension_lower"]==4
    assert ext["selected_rank"]==242 and ext["existing_critical_witness_count"]==4
    source=four["complete_signed_Gram_intervals"]
    m=[[(F(lo)+F(hi))/2 for lo,hi in row] for row in source]
    rad=[[(F(hi)-F(lo))/2 for lo,hi in row] for row in source]
    for i in range(4):
        for j in range(4):
            assert m[i][j]==m[j][i] and rad[i][j]==rad[j][i] and rad[i][j]>=0
    err=max((sum(row,F(0)) for row in rad))
    assert err<F(1,10**35)
    target=F(5,10**23)
    shifted=[[m[i][j]-(target+err)*F(i==j) for j in range(4)] for i in range(4)]
    piv=positive_ldlt(shifted)
    S=sum((dyad(ext["physical_quotient_Gram_native"][i][i][0])+dyad(ext["physical_quotient_Gram_native"][i][i][1]) for i in range(4)),F(0))
    C=sum((dyad(ext["actual_exterior_signed_Gram_native"][i][i][0])+dyad(ext["actual_exterior_signed_Gram_native"][i][i][1]) for i in range(4)),F(0))
    assert S<F(1,2**604) and C>0
    delta=F(9,2**290)+C
    assert delta<F(1,2**286)
    floor=F(49,10**24)
    assert target-delta>floor
    eps=F(rank["pruned_physical_complement_negative_upper"])
    mu=F(1,1000)-eps
    assert mu>F(98,10**5)
    print("PASS NF368 complete original coupled four-mode w(Fz)>5e-23||z||^2")
    print("PASS NF368 actual physically projected four-plane w(PFz)>4.9e-23||z||^2")
    print("4x4 exact LDL pivots",*[f"{float(v):.8g}" for v in piv])
    print("max interval row error",float(err),"signed quotient transfer",float(delta))
    print("old certified exterior floor",float(mu))
    print("sufficient strong forcing norm ceiling",float(mu*floor)**.5)
    print("NOT full 242D or infinite signed Schur positivity; original realization review OPEN")
if __name__=="__main__":main()
