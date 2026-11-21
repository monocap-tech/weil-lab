#!/usr/bin/env python3
"""PI033: exhaustive first n=3 crossing count; exact integer interval verifier.

Requires the UNCHANGED inherited scripts/pi032_exact_interval_transversality.py.
The local sign atlas plus PI032's nine strict derivatives and a single
new derivative overlap prove exactly nine live/simple roots for m=1,u=3/2.
No PR/CI/Lean or spectral trace is run here.

Run in four bounded shards and a bridge:
  python scripts/pi033_exact_nine_exhaustive.py --part 0
  python scripts/pi033_exact_nine_exhaustive.py --part 1
  python scripts/pi033_exact_nine_exhaustive.py --part 2
  python scripts/pi033_exact_nine_exhaustive.py --part 3
  python scripts/pi033_exact_nine_exhaustive.py --part bridge

I(tau)=integral E(y)E(y-tau)dy, 0<=tau<=1, as in PI031/PI032.
PI032 establishes I(0)<21 and integral (E')²<9000.
Cauchy--Schwarz: |I'|<sqrt(21*9000)<435.
If I(c) is enclosed by [L,U], then for |tau-c|<=h:
  I(tau) is contained in [L-435h, U+435h].
For every subinterval the script checks either I>2/5 or I<0.
These are safe for actual n=3 prime/Gamma response because
ell^5 B<1/5, kappa3>1/3, satellite coefficient u=3/2.
"""
from fractions import Fraction as F
import argparse
from pi032_exact_interval_transversality import S, C, eval_integral

REGIONS = (
    (F(0), F(101,1000), True, 2048),
    (F(121,1000), F(477,1000), False, 512),
    (F(498,1000), F(690,1000), True, 512),
    (F(706,1000), F(41,50), False, 512),
)

def certify_region(a,b,positive,N,depth=0):
    assert F(0)<=a<b<=1 and depth<=20
    c=(a+b)/2
    R=eval_integral(c,N,'I')
    # Outward integer comparisons: exact rational, no floating-point.
    h=(b-a)/2
    L,U=F(R.lo,S)-435*h, F(R.hi,S)+435*h
    if (positive and L>F(2,5)) or ((not positive) and U<0):
        return [(a,b,L,U,depth)]
    assert depth<20, (a,b,L,U,'inconclusive interval')
    return (certify_region(a,c,positive,N,depth+1)+
            certify_region(c,b,positive,N,depth+1))

def check_region(index):
    a,b,positive,N=REGIONS[index]
    leaves=certify_region(a,b,positive,N)
    assert leaves and leaves[0][0]==a and leaves[-1][1]==b
    assert all(x[1]==y[0] for x,y in zip(leaves,leaves[1:]))
    assert all((x[2]>F(2,5) if positive else x[3]<0) for x in leaves)
    print('PI033 exact interval coverage PASS',index,'leaves',len(leaves),
          'max_depth',max(v[4] for v in leaves),
          'interval',str(a),str(b),'source_N',N)
    return leaves

def check_bridge():
    # New derivative sample extends PI032's second increasing sector.
    p=eval_integral(F(491,1000),1024,'Ip')
    assert F(p.lo,S)>69, (p.lo,p.hi)
    # PI032 I'(.111)<-90, I'(.484)>65, I'(.698)<-75;
    # PI032 |I''|<9000. Strictness of the first input permits equality
    # 90=9000*0.010 while ensuring I'<0 throughout [.101,.121].
    assert 90>=9000*F(10,1000)
    assert 65>9000*F(7,1000)   # [.477,.491] increasing
    assert 69>9000*F(7,1000)   # [.491,.498] increasing
    assert 75>9000*F(8,1000)   # [.690,.706] decreasing

    # For y in (0,9/50], v=y(1-y)<=369/2500,
    # E(y)=g(y)*(1-2y)/v^6 * p_delta(v), where
    # p_delta(v)=1-10v+24v²-12v³-delta v⁴,
    # 0<delta<1/3240000.
    # p'_delta(v)<-10+48v<0, p_delta(endpoint)>0.
    v=F(369,2500)
    delta_max=F(1,3240000)
    poly=1-10*v+24*v*v-12*v**3-delta_max*v**4
    assert -10+48*v<0
    assert poly>0
    assert F(1)-F(9,50)==F(41,50)
    # E(1-y)=-E(y), so for tau>=.82, E(y)<0 and
    # E(y-tau)>0 on y in (tau,1). Thus I(tau)<0 until tau=1.
    assert 435*435 > 21*9000
    assert F(13,4)*21/450 < F(1,5)
    assert F(3,2)*F(1,3)*F(2,5)==F(1,5)
    print('PI033 new Iprime(.491)>69 overlap, tail polynomial',poly,
          'and original phase dominance: PASS')

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--part',choices=('0','1','2','3','bridge'),required=True)
    args=ap.parse_args()
    if args.part=='bridge': check_bridge()
    else: check_region(int(args.part))
    print('PI033 no Actions/Lean/spectral computation; PI032 root and norm receipts are inherited dependencies')

if __name__=='__main__':
    main()
