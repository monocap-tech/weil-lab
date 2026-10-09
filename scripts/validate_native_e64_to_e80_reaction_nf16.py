#!/usr/bin/env python3
"""NF16: exact rational original native E64->E80 directional Schur loss.
Required input: complete E80 signed original interval JSON(.gz).
Verifies one explicitly specified rational critical even direction, NOT
the original infinite-complement reaction or the whole a=1.06 sign.
"""
import argparse,gzip,hashlib,json
from pathlib import Path
from fractions import Fraction as F

SOURCE_SHA="9188d9b48525c1e1af41292e3bfe8d3004470e03b00520428d9d5b0cc76a8513"
DEN=10**42
NUMS=(
"591198448621294696582858434281930593349775 -586443852151049383147960732842015573848281 "
"445236154853530441941022104804686641800575 -284199215087204914159143092726635549144824 "
"151074586531362649986998428045694841422969 -65213602611450861214340005724812226306699 "
"21584884658804840496791035275139809744719 -4580277584222598204832404018037420637958 "
"-21369689087921643591899536640954089224 520205876387070758548804145058359905967 "
"-258821175985880097025769561889286831799 77419870730642435477895372014565647200 "
"-16238846048807089383140665352366260820 3045678468968397910866485294547329005 "
"-1015904376686795326472299251394354264 523598175732164764226882850401582716 "
"-238176888405657940505372340559969954 90146899062729178672135853160117318 "
"-30576859433377991626594613323113869 9860257211680655508120236558273389 "
"-3029613568710113522412763777088970 843769766852803501879361622367657 "
"-192915778756163948637884105584846 26052540429588692613956587464355 "
"5199156772294879588610359021768 -6011721323101340098940827069439 "
"3094447502196551349740351438757 -1235627319512387243732728071186 "
"423173980196905983089362191558 -127971859719907486162432352471 "
"33875359611676537839407529379 -7039298767223827887007473906")
NUMS=[int(s) for s in NUMS.split()]
assert len(NUMS)==32

def verify(source):
    with gzip.open(source,"rb") if str(source).endswith(".gz") else open(source,"rb") as f:
        raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==SOURCE_SHA
    v=json.loads(raw)
    assert v["aperture"]=="53/50" and v["dim"]==80
    D=v["complete_form"]
    assert len(D)==1640
    x=[F(n,DEN) for n in NUMS]
    norm=sum(t*t for t in x)
    assert F(999,1000)<norm<F(1001,1000)
    A=[[F(0)]*40 for _ in range(40)]
    eps=F(0);rounding=10**55
    for i in range(40):
        for j in range(i,40):
            lo,hi=map(F,D[f"{2*i},{2*j}"]["full"])
            middle=(lo+hi)/2
            m=F((middle*rounding).__floor__(),rounding)
            A[i][j]=A[j][i]=m
            eps=max(eps,abs(m-lo),abs(m-hi))
    eta=80*eps
    assert eta<F(1,10**48)
    q=sum((x[i]*A[i][j]*x[j] for i in range(32) for j in range(32)),F(0))
    b=[sum((A[i+32][j]*x[j] for j in range(32)),F(0)) for i in range(8)]
    C=[[A[i+32][j+32] for j in range(8)] for i in range(8)]
    # Exact positive shell floor 9/5.
    Z=[[C[i][j]-(F(9,5) if i==j else 0) for j in range(8)] for i in range(8)]
    for k in range(8):
        p=Z[k][k];assert p>0
        for i in range(k+1,8):
            for j in range(i,8):
                Z[i][j]=Z[j][i]=Z[i][j]-Z[i][k]*Z[k][j]/p
    # Exact inverse along this particular source row, not C^-1 on F112.
    W=[C[i][:]+[b[i]] for i in range(8)]
    for k in range(8):
        p=W[k][k];assert p>0
        for i in range(k+1,8):
            factor=W[i][k]/p
            for j in range(k+1,9):W[i][j]-=factor*W[k][j]
            W[i][k]=0
    z=[F(0)]*8
    for i in range(7,-1,-1):
        z[i]=(W[i][8]-sum((W[i][j]*z[j] for j in range(i+1,8)))/W[i][i])
    reaction=sum(b[i]*z[i] for i in range(8))
    assert sum(t*t for t in b)<1
    # Whole source midpoint error<=eta; ||x||<2, ||b||<1,
    # Cmid >=9/5 and Ctrue >=1 imply:
    # |Qtrue(x)-q|<=4eta; |reaction_true-reaction|<=8eta.
    rlo,rhi=reaction-8*eta,reaction+8*eta
    qlo,qhi=q-4*eta,q+4*eta
    assert 0<rlo<rhi and 0<qlo<qhi
    assert F(2,3)<rlo/qhi and rhi/qlo<F(67,100)
    assert F(3,10**30)<qlo<F(4,10**30)
    return dict(status="PASS",aperture="53/50",
        original_E80_source_sha256=SOURCE_SHA,
        certified_strict_relative_E64_to_E80_even_reaction=["2/3","67/100"],
        strict_exact_old_Rayleigh_enclosure=[str(qlo/norm),str(qhi/norm)],
        strict_exact_incoming_reaction_enclosure=[str(rlo/norm),str(rhi/norm)],
        raw_old_Rayleigh_approx=float(q/norm),
        raw_incoming_reaction_approx=float(reaction/norm),
        raw_reaction_fraction_approx=float(reaction/q),
        positive_shell_C_physical_lower="9/5",
        full_NF10_infinite_complement_reaction_evaluated=False,
        full_112_retained_positive=False,whole_aperture_positive=False,
        Lean_certified=False)

if __name__=="__main__":
    p=argparse.ArgumentParser()
    p.add_argument("original_e80_json_gz")
    args=p.parse_args()
    print(json.dumps(verify(args.original_e80_json_gz),indent=2))
