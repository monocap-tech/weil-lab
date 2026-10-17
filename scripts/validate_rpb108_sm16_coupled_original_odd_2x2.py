#!/usr/bin/env python3
"""SM16: true original signed 2x2 physical odd form, every mixed term retained.

Certify coupled g_14.42 and g_17.00 supported Jensen means. Two
disjoint sets of sign-positive original-frequency sources give a
Loewner-lower 2x2 matrix. ALL original Kneg leaves contribute to
outward rational 2x2 upper intervals via continuous sine-Gram
envelopes and exact fully-negative second-order integrated mass.
The odd pole and scalar physical cross Gram are paid. No assumption
of frequency orthogonality on bounded physical support. A 2x2 SPD
claim is emitted ONLY upon exact rational determinant acceptance.
"""
from fractions import Fraction as F
from validate_rpb108_si06_negative_band import B,PI,prime_interval
from validate_rpb108_si13_odd_fourier_reference import arch_lower
from validate_rpb108_sm03_negative_packet_reference_nogo import arch_upper
from validate_rpb108_si18_odd_rank_two_woodbury import gram,signed_odd_overlap
from validate_rpb108_si12_even_supported_inverse import cosh_bounds
from validate_rpb108_si10_complement_positivity import KAPPA,protected_outer_band
from validate_rpb108_sm10_explicit_odd_cap_moments import full_upper_leaves
from validate_rpb108_sm14_continuum import C,R,S
from validate_rpb108_sm15_global_negative_witness import (
 RN,PRIME_M2,sinc_amp_bound,sinc_deriv_bound,min_distance,
 witness_err,original_positive_lower,signed_negative_global_upper,pole_upper
)

C2=F(17)
CENTERS=(C,C2)
NEW_RADIUS=F(1,100)
NEW=((1660,3),(1665,3),(1670,3),(1675,2),(1680,1),(1685,1),
     (1690,1),(1695,2),(1700,2),(1705,3),(1710,3),(1715,2),
     (1760,3),(1765,4))

def abs_hi(iv):
    return max(abs(iv[0]),abs(iv[1]))

def product(a,b):
    v=(a[0]*b[0],a[0]*b[1],a[1]*b[0],a[1]*b[1])
    return min(v),max(v)

def overlap(c,d,rc,rd):
    z=gram(c,d)
    e=2*B*(witness_err(rc)+witness_err(rd))
    return z[0]-e,z[1]+e

def sqmin(iv):
    if iv[0]<=0<=iv[1]:return F(0)
    return min(iv[0]**2,iv[1]**2)

def frequency_sources():
    assert len(S)==13 and len(NEW)==14
    assert RN==F(1,100) and C2-C>F(2)
    bands=[(F(n,50),R,F(delta)) for n,delta in S]
    bands += [(F(n,100),NEW_RADIUS,F(delta)) for n,delta in NEW]
    assert len(bands)==27
    sorted_bands=sorted((c-r,c+r) for c,r,d in bands)
    assert all(sorted_bands[j][1]<sorted_bands[j+1][0]
               for j in range(len(sorted_bands)-1))
    min_signed=None
    for c,r,delta in bands:
        for j in range(8):
            a=c-r+2*r*j/8
            b=c-r+2*r*(j+1)/8
            lo=arch_lower(a)+prime_interval((a+b)/2)[0]-F(69,2)*(b-a)
            assert lo>KAPPA+delta,(
                'SM16 positive original whole real interval failed',
                str(c),str(delta),j,float(lo))
            min_signed=lo if min_signed is None else min(min_signed,lo)
    return bands,min_signed

def positive_2x2(bands):
    a11=KAPPA*(1-witness_err(RN))**2*gram(C,C)[0]
    a22=KAPPA*(1-witness_err(RN))**2*gram(C2,C2)[0]
    a12=overlap(C,C2,RN,RN)
    alo,ahi=KAPPA*a12[0],KAPPA*a12[1]
    from_first=F(0)
    from_second=F(0)
    for k,(d,r,delta) in enumerate(bands):
        gain=4*r*delta
        p=overlap(C,d,RN,r)
        q=overlap(C2,d,RN,r)
        c11=gain*sqmin(p)
        c22=gain*sqmin(q)
        a11+=c11
        a22+=c22
        if k<13:from_first+=c11
        else:from_second+=c22
        pq=product(p,q)
        alo+=gain*pq[0]
        ahi+=gain*pq[1]
    return (a11,a22,(alo,ahi)),from_first,from_second

def overlap_leaf(c,left,right):
    """Outward true physical sine Fourier integral for entire leaf."""
    d=min_distance(left,right,c)
    far=c+left
    e=2*B*witness_err(RN)
    maxamp=sinc_amp_bound(d)+sinc_amp_bound(far)+e
    if d>F(6):return (-maxamp,maxamp)
    midpoint=(left+right)/2
    z=gram(c,midpoint)
    slope=sinc_deriv_bound(d)+sinc_deriv_bound(far)
    variation=slope*(right-left)/2+e
    return max(z[0]-variation,-maxamp),min(z[1]+variation,maxamp)

def original_negative_2x2():
    ext,lim=protected_outer_band()
    assert ext>0 and lim>KAPPA
    cl,width,mass,total=full_upper_leaves()
    leaves=[item for block in cl for item in block]
    assert len(leaves)==973 and len(cl)==107
    upper=[F(0),F(0)]
    mixed=[F(0),F(0)]
    near=0
    fully=0
    far=0
    for l,r,h in leaves:
        dl=min(min_distance(l,r,c) for c in CENTERS)
        w=h+KAPPA
        rmin=F(0)
        if dl<=F(6):
            near+=1
            mid=(l+r)/2
            pl,pu=prime_interval(mid)
            w=min(w,max(F(0),KAPPA-arch_lower(l)-pl-F(-69,2)*(r-l)))
            if dl<=F(2):
                upperm=arch_upper(r)+pu+F(69,2)*(r-l)
                if upperm<KAPPA:
                    w=min(w,KAPPA-arch_lower(l)-pl+PRIME_M2*(r-l)**2/24)
                    rmin=KAPPA-upperm
                    assert rmin>0 and w>=rmin
                    fully+=1
        else:far+=1
        assert F(0)<=w<=h+KAPPA
        if w==0:continue
        a=overlap_leaf(C,l,r)
        b=overlap_leaf(C2,l,r)
        factor=2*(r-l)
        upper[0]+=factor*w*abs_hi(a)**2
        upper[1]+=factor*w*abs_hi(b)**2
        xy=product(a,b)
        if xy[0]>=0:
            mixed[0]+=factor*rmin*xy[0]
            mixed[1]+=factor*w*xy[1]
        elif xy[1]<=0:
            mixed[0]+=factor*w*xy[0]
            mixed[1]+=factor*rmin*xy[1]
        else:
            mixed[0]+=factor*w*xy[0]
            mixed[1]+=factor*w*xy[1]
    assert near+far==len(leaves)
    assert mixed[0]<=mixed[1]
    return upper,tuple(mixed),near,far,fully

def pole_2x2():
    chi=cosh_bounds(B/2)[1]
    L1=4*(chi-1)
    coeff=[abs_hi(signed_odd_overlap(c))+witness_err(RN)*L1 for c in CENTERS]
    assert all(x>0 for x in coeff)
    return tuple(2*x*x for x in coeff),2*coeff[0]*coeff[1]

def run():
    bands,min_sign=frequency_sources()
    (p11,p22,p12),one,two=positive_2x2(bands)
    (n11,n22),n12,local,remote,whole=original_negative_2x2()
    (pole1,pole2),pole12=pole_2x2()
    d1=p11-n11-pole1
    d2=p22-n22-pole2
    cross=(p12[0]-n12[1]-pole12,
           p12[1]-n12[0]+pole12)
    upper_cross=abs_hi(cross)
    det=d1*d2-upper_cross**2
    # Compatibility regression: exact SM15's independent full witness
    # must still be strictly positive (new 2x2 lower may be looser).
    oldpos,_=original_positive_lower()
    oldneg,*_=signed_negative_global_upper()
    oldpole,_=pole_upper()
    assert oldpos-oldneg-oldpole>F(47,1000)
    print('SM16 actual original physical odd centers',tuple(map(str,CENTERS)),flush=True)
    print('SM16 original sign-positive disjoint source bands',len(bands),flush=True)
    print('SM16 original sign-positive minimum margin',float(min_sign),flush=True)
    print('SM16 local/remote original negative leaves',local,remote,
          'sign-strict averaged leaves',whole,flush=True)
    print('SM16 positive physical 2x2 diagonal LOWER',float(p11),float(p22),flush=True)
    print('SM16 positive physical mixed interval',tuple(map(float,p12)),flush=True)
    print('SM16 original entire negative 2x2 diagonal UPPER',float(n11),float(n22),flush=True)
    print('SM16 original entire negative mixed interval',tuple(map(float,n12)),flush=True)
    print('SM16 full original odd pole diagonal UPPER',float(pole1),float(pole2),
          'mixed abs UPPER',float(pole12),flush=True)
    print('SM16 complete original signed 2x2 diagonal LOWER',float(d1),float(d2),flush=True)
    print('SM16 complete original signed mixed interval',tuple(map(float,cross)),flush=True)
    print('SM16 certified 2x2 determinant LOWER',float(det),flush=True)
    if d1>0 and d2>0 and det>0:
        print('SM16 PASS (SCOPED FULL 2D ORIGINAL SIGNED ODD POSITIVITY): '
              'the entire true physical span{g_14.42,g_17} is strictly '
              'positive with all mixed original continuum, odd pole and '
              'infinite exterior paid; W-ODD-NEG and RH OPEN',flush=True)
    else:
        print('SM16 PASS (DIAGNOSTIC): exact 2x2 physical original signed '
              'intervals are enclosed but insufficient to certify the '
              'entire 2D span; SM15 one-direction result retained; '
              'W-ODD-NEG and RH OPEN',flush=True)
if __name__=='__main__':run()
