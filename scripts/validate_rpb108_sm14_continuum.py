#!/usr/bin/env python3
"""SM14 exact original positive continuum on a true physical witness."""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_si18_odd_rank_two_woodbury import gram
from validate_rpb108_si21_odd_jensen_four import KAPPA
from validate_rpb108_sm11_rank17_c16_nogo import certify_all_negative_windows,RADIUS as RN
from validate_rpb108_sm12_positive_reference_33 import OLD_POSITIVE,CENTERS as NEW33,RADIUS as R33
from validate_rpb108_sm13_c33_physical_negative_rayleigh import physical_single_rayleigh,positive_data
C=F(721,50)
R=F(3,200)
S=((703,4),(705,4),(707,4),(709,3),(711,2),(713,1),
   (728,1),(730,2),(732,3),(734,3),(736,3),(738,3),(740,2))
def err(rad):return (2*PI[1]*rad*B)**2/6
def run():
    assert certify_all_negative_windows()<-F(2,5)
    old=[(c-r,c+r) for c,r,d,k in OLD_POSITIVE]
    new=[(c-R33,c+R33) for c in NEW33]
    reserved=old+new+[(C-RN,C+RN)]
    lower=[]
    minima=[]
    for i,(numer,delta) in enumerate(S):
        d=F(numer,50)
        left,right=d-R,d+R
        if i: assert left>S[i-1][0]/50+R
        assert all(not(left<b and a<right) for a,b in reserved)
        smallest=None
        for j in range(8):
            l=left+(right-left)*j/8
            r=left+(right-left)*(j+1)/8
            mlo=arch_lower(l)+prime_interval((l+r)/2)[0]-F(69,2)*(r-l)
            assert mlo>KAPPA+delta,('SM14 interval failed',str(d),j,float(mlo))
            smallest=mlo if smallest is None else min(smallest,mlo)
        minima.append(smallest)
        z=gram(C,d)
        abslo=z[0] if z[0]>0 else -z[1] if z[1]<0 else F(0)
        cross=max(F(0),abslo-2*B*(err(R)+err(RN)))
        val=4*R*delta*cross**2
        lower.append((d,val))
    mass=sum((v for d,v in lower),F(0))
    assert mass>F(1,2),('positive mass target not met',float(mass))
    nlo=(1-err(RN))**2*gram(C,C)[0]
    prev=physical_single_rayleigh(C,positive_data())
    assert prev['margin']>F(15,1000)
    print('SM14 original signed positive windows',len(S),flush=True)
    print('SM14 smallest full-window original m lower',float(min(minima)),flush=True)
    print('SM14 additional A_o physical quadratic lower',float(mass),flush=True)
    print('SM14 A_o quadratic lower with scalar baseline',float(mass+KAPPA*nlo),flush=True)
    print('SM14 old C33 quadratic upper',float(prev['positive_upper']),flush=True)
    for d,v in lower: print('SM14 original window',float(d),'lower',float(v),flush=True)
    print('SM14 PASS SCOPED: missing original positive continuum >0.5 on witness; full odd Schur remains open',flush=True)
if __name__=='__main__':run()
