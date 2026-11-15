#!/usr/bin/env python3
"""NF526 exact Fraction original endpoint prime-only support / conditional bounds.
No original NF494 source coefficients, zeta enumeration, or Lean build performed.
"""
import json,argparse,math
from fractions import Fraction as F
from pathlib import Path
B=F(11,10);D=F(1,500);LO=2*(B-D);HI=2*B
def log9_bounds(N):
    # log9 = 4*atanh(1/2); the rest is bounded by a geometric series.
    low=sum((F(4,2**(2*k+1)*(2*k+1)) for k in range(N)),F(0))
    tail=F(16,3*2**(2*N+1)*(2*N+1))
    return low,low+tail,tail
def main():
    p=argparse.ArgumentParser()
    p.add_argument('--output',default='/tmp/nf526-prime-support.json')
    a=p.parse_args()
    low,high,tail=log9_bounds(20)
    assert LO==F(549,250) and HI==F(11,5)
    assert LO<low<high<HI-D
    # log(1+x)>=x/(1+x) for x>0: bound log2,8,10 via log9.
    assert F(1,2)>D and high-F(1,9)<LO and low+F(1,10)>HI
    s_min=HI-high;s_max=HI-low
    assert F(4,3)*D<s_min<=s_max<2*D
    assert 3*B/D==1650
    # e^8 >= its first 9 positive Taylor terms > 1650; so log1650<8.
    assert sum((F(8)**k/F(math.factorial(k)) for k in range(9)),F(0))>1650
    # source-independent selection n=9; below conditional on pinned NF523 M0
    M0=F(2,10**7)
    assert high<F(12,5) # hence 2 log3/3 < 4/5
    prime_abs=F(4,5)*F(2,3)*D*(8*M0)**2
    z=(B+D)/2
    assert 0<z<1 and 1+z/(1-z/2)<2 # sinh((B-d)/2)<1
    pole_abs=2*(2*D*M0)**2
    out={
        'pass':'NF526-exact-original-endpoint-prime-support-9-only',
        'date':'2026-11-15 PT',
        'scope':'support/log9 rational geometry + original NF523-source-envelope conditional magnitude; NOT NF494 replay, Lean or Weil form acceptance',
        'B':str(B),'delta':str(D),
        'cross_positive':[str(LO),str(HI)],
        'log9_bounds':[str(low),str(high)],
        'log9_tail_upper':str(tail),
        's9_bounds':[str(s_min),str(s_max)],
        'only_prime_power':9,
        'original_NF523_envelope_premise':'|U(B-d)/2|<=2e-7 for 0<=d<=delta',
        'prime_absolute_bound':str(prime_abs),
        'pole_absolute_bound':str(pole_abs),
        'prime_sign':'UNDECIDED',
        'original_archimedean_signed_scalar':'OPEN',
        'original_400_source_replayed':False,
        'lean_compiled':False,
        'RH':'OPEN'
    }
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print(json.dumps(out,indent=2))
if __name__=='__main__':main()
