"""RC26 certified scalar in the RC25 physical metric decomposition.

All bounds use Fraction arithmetic. Partial trial matrices are physical
polynomial metrics, not canonical Riesz-head Gram matrices.
"""
from fractions import Fraction as F
import json
from validate_rpb108_rc25_legendre_metric_split import exact_components, harmonic
from validate_rpb108_rc23_canonical_matrix_gate import psd

def atan_bounds(x, n=32):
    assert 0 < x < 1 and n > 0
    s=sum(((-1)**j*x**(2*j+1)/F(2*j+1) for j in range(n)), F(0))
    next_term=(-1)**n*x**(2*n+1)/F(2*n+1)
    return min(s,s+next_term),max(s,s+next_term)

def log_bounds(x, n=128):
    assert x >= 1 and n > 0
    t=(x-1)/(x+1)
    s=2*sum((t**(2*j+1)/F(2*j+1) for j in range(n)),F(0))
    tail=2*t**(2*n+1)/(F(2*n+1)*(1-t*t))
    return s,s+tail

def scalar_bounds(R=F(11,5), N=2048):
    a,b=atan_bounds(F(1,5)); c,d=atan_bounds(F(1,239))
    pi_lo,pi_hi=16*a-4*d,16*b-4*c
    # N=2**11; log(N+1)=11 log(2)+log(1+1/N).
    assert N==2048
    l2,u2=log_bounds(F(2),32)
    lr,ur=log_bounds(1+F(1,N),16)
    hn=harmonic(N)
    gamma_lo=hn-11*u2-ur
    gamma_hi=hn-11*l2
    lx,_=log_bounds(2*R*pi_lo)
    _,ux=log_bounds(2*R*pi_hi)
    return -gamma_hi-ux,-gamma_lo-lx

def outward(lo,hi,denominator=10**9):
    l=(lo*denominator).__floor__()
    u=(hi*denominator).__ceil__()
    return F(l,denominator),F(u,denominator)

def partial_matrix_bounds(count=8):
    lo,hi=outward(*scalar_bounds())
    pieces=exact_components(count)
    D,S,W=(pieces[k] for k in ('physical_mass','singular_metric','endpoint_metric'))
    lower=[[S[i][j]+W[i][j]+lo*D[i][j] for j in range(count)] for i in range(count)]
    upper=[[S[i][j]+W[i][j]+hi*D[i][j] for j in range(count)] for i in range(count)]
    return lo,hi,D,lower,upper

def controls():
    checks=0
    def check(v):
        nonlocal checks
        assert v,checks+1
        checks+=1
    a,b=atan_bounds(F(1,5))
    check(0<a<b<F(1,5))
    c,d=atan_bounds(F(1,239))
    pi_lo,pi_hi=16*a-4*d,16*b-4*c
    check(F(314159,100000)<pi_lo<pi_hi<F(314160,100000))
    # Machin angle: tan(4 atan(1/5))=120/119 and subtraction gives 1.
    tangent4=F(120,119)
    check((tangent4-F(1,239))/(1+tangent4/F(239))==1)
    check(0<4*b-c<1)  # angle in (0,pi/2), since pi>2
    l,u=log_bounds(F(2),32)
    check(F(693147,1000000)<l<u<F(693148,1000000))
    check(u-l<F(1,10**30))
    check(log_bounds(F(1))==(0,0))
    hn=harmonic(2048)
    lr,ur=log_bounds(1+F(1,2048),16)
    gl,gu=hn-11*u-ur,hn-11*l
    check(F(576,1000)<gl<gu<F(578,1000))
    check(gu-gl<F(1,2000))
    lo,hi,D,L,U=partial_matrix_bounds()
    check(-F(321,100)<lo<hi<-F(32,10))
    check(hi-lo<F(1,2000))
    check(psd([[U[i][j]-L[i][j] for j in range(8)] for i in range(8)]))
    check(all(U[i][j]-L[i][j]==(hi-lo)*D[i][j] for i in range(8) for j in range(8)))
    check(all(L[i][j]==L[j][i] for i in range(8) for j in range(8)))
    check(all(L[i][j]==0 for i in range(8) for j in range(8) if (i+j)%2))
    check(L[0][0]==F(11,5)*(1+lo))
    check(L[0][2]==F(11,30))
    # Increasing the cutoff lowers the scalar by log(2), within enclosures.
    lo2,hi2=scalar_bounds(F(22,5))
    check(lo2<=hi-l and hi2>=lo-u and hi2<lo)
    return {'milestone':'RC26','status':'PASS','exact_rational_checks':checks,
            'scalar_formula':'c_R = -gamma - log(2*pi*R)',
            'R':'11/5','scalar_lower':str(lo),'scalar_upper':str(hi),
            'scalar_interval_width':str(hi-lo),'partial_trial_dimension':8,
            'remaining_trial_metric_component':'compact kernel K_B',
            'complete_metric_matrix_evaluated':False,
            'actual_Riesz_head_matrix_evaluated':False,
            'actual_head_certified':False,'whole_centered_aperture_extended':False,
            'RH':False,'F4':False,'Lean':False}

if __name__=='__main__': print(json.dumps(controls(),indent=2))
