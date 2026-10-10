"""Scoped precision upgrade for analytic source enclosures, not archive inputs.

Historical interval integers are promoted exactly before the shared arithmetic
grid changes. Canonical analytic sources and all inherited physical errors
remain unchanged. Finite series tails are explicit at each new precision.
"""
from fractions import Fraction as F
import certify_native_high_correction_nf26_106 as base
n=base.n

def promote(value,digits,old_digits=500):
    factor=10**(digits-old_digits)
    if isinstance(value,n.I):return n.I.raw(value.l*factor,value.h*factor)
    if isinstance(value,list):return [promote(z,digits,old_digits) for z in value]
    if isinstance(value,tuple):return tuple(promote(z,digits,old_digits) for z in value)
    return value

def configure(digits):
    assert digits in [800,900] and n.SCALE==10**500
    terms=1400 if digits==800 else 1600
    atan_terms=650 if digits==800 else 750
    em_terms=400 if digits==800 else 450
    harmonic_endpoint=800 if digits==800 else 900
    n.SCALE=10**digits;n.native.GRID=n.SCALE
    n.basis.cache_clear();n.log2i.cache_clear();n.native.log.cache_clear()
    def logunit(q):
        z=(q-1)/(q+1);assert z.absupper()<F(1,2)
        power=z;total=n.I(0)
        for k in range(terms):total+=2*power/F(2*k+1);power=power*z*z
        remainder=2*power.absupper()/F(2*terms+1)/(1-z.absupper()**2)
        return total+n.I(-remainder,remainder)
    n.log_unit=logunit
    def native_log(q,terms=None):
        # Reuse only the higher-precision outward atanh primitive. Its tail
        # is included above; native archives are never recomputed.
        z=n.logi(n.I(F(q)));return n.native.I(F(z.l,n.SCALE),F(z.h,n.SCALE))
    n.native.log=native_log
    def constants():
        pi=n.ni(16*n.native.atan(F(1,5),terms=atan_terms)-4*n.native.atan(F(1,239),terms=atan_terms))
        B=n.native.bern(2*em_terms+2);m=harmonic_endpoint
        gamma=n.I(sum((F(1,k) for k in range(1,m+1)),F(0))-F(1,2*m))-n.ni(n.native.log(m))
        for k in range(1,em_terms+1):gamma+=B[2*k]/F(2*k*m**(2*k))
        rem=abs(B[2*em_terms+2])/F((2*em_terms+2)*m**(2*em_terms+2));gamma+=n.I(-rem,rem)
        return -gamma-n.logi(2*pi),pi
    base.constants=constants
    return dict(interval_grid_digits=digits,atanh_terms=terms,pi_atan_terms=atan_terms,
                Euler_Maclaurin_terms=em_terms,Euler_Maclaurin_endpoint=harmonic_endpoint,
                finite_analytic_series_tails_paid=True,original_archives_regenerated=False)

def controls():
    for q in [F(1),F(2),F(3,2),F(8),F(1,8)]:
        value=n.logi(n.I(q));assert value.l<=value.h
    assert n.logi(n.I(1)).l<=0<=n.logi(n.I(1)).h
    a=n.logi(n.I(2));b=n.logi(n.I(8));assert max((3*a).l,b.l)<=min((3*a).h,b.h)
    saved=n.I.raw(-7,11);promoted=promote(saved,800)
    assert (promoted.l,promoted.h)==(-7*10**300,11*10**300)
    return dict(exact_signed_grid_promotion='PASS',higher_precision_log_identities='PASS')
