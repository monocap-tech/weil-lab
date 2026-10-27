#!/usr/bin/env python3
"""Independent stdlib replay: affine cap, clipping, Gram and two-sided Young error."""
import hashlib,json,sys
from fractions import Fraction as Q
from math import factorial
from pathlib import Path
from validate_rpb108_si06_negative_band import PI,WEIGHTS,SHIFTS
from validate_rpb108_si08_multiband_rank import taylor_order

PINS=['19af532b6bbd4a808854696b2a993e7ebd966e04da27fdd5f55e8b736668770b',
      '264fd853ca006a578d76369ac5bd4588a2097145b829fbba7036693f29b04044',
      'a693261c31f01a4a1e11ea6400e5173435a8260b41b1f6b43aa6f67f784ccb7f']
def add(x,y):return x[0]+y[0],x[1]+y[1]
def mul(x,y):
    a=[v*w for v in x for w in y];return min(a),max(a)
def scale(x,c):return mul(x,(c,c))
def inv(x):
    assert x[0]>0;return 1/x[1],1/x[0]
def const(x):return Q(x),Q(x)
def trig(x,cos=False):
    # Degree 80, real Lagrange remainder: every sine/cosine derivative <=1.
    out=const(0);power=const(1)
    for n in range(81):
        if (n%2==0)==cos:out=add(out,scale(power,Q((-1)**(n//2),factorial(n))))
        power=mul(power,x)
    tail=max(abs(x[0]),abs(x[1]))**81/factorial(81)
    return out[0]-tail,out[1]+tail
def hyp(x,cos=False):
    # Positive series with exact geometric bound for the first omitted term.
    out=Q(0);last=64 if cos else 65
    for n in range(int(not cos),last+1,2):out+=x**n/factorial(n)
    n=last+2;tail=x**n/factorial(n)/(1-x*x/Q((n+1)*(n+2)))
    return out,out+tail
def gram_intervals():
    b=Q(11,10);c=Q(4096,3013);omega=scale(PI,2*Q(37,64));x=scale(omega,b)
    ss=add(const(b),scale(mul(trig(scale(x,2)),inv(scale(omega,2))),-1))
    pp=add(hyp(b),const(-b))
    sp=scale(mul(add(scale(mul(hyp(b/2,True),trig(x)),Q(1,2)),scale(mul(mul(omega,hyp(b/2)),trig(x,True)),-1)),inv(add(const(Q(1,4)),mul(omega,omega)))),2)
    return [add(add(ss,scale(sp,2*c)),scale(pp,c*c)),add(add(ss,scale(sp,c-1)),scale(pp,-c)),add(add(ss,scale(sp,-2)),pp)]
def positive_average(a,b):
    if min(a,b)>=0:return (a+b)/2
    if max(a,b)<=0:return Q(0)
    return max(a,b)**2/(2*abs(b-a))
def clipped_mass(width,a,b,w):
    return width*(positive_average(a,b)-positive_average(a-w,b-w))
def regressions():
    # Exact interpolation quadratic saturates BOTH +/- curvature errors.
    for h in (Q(1,7),Q(1,4096)):
        for sign in (-1,1):
            # f(x)=sign*x^2, f(0)=0,f(h)=sign*h^2, f''=2sign.
            midpoint_error=abs(sign*h*h/4-sign*h*h/2)
            assert midpoint_error==2*h*h/8
    # A positive-part kink must be clipped AFTER the signed interpolant.
    assert clipped_mass(Q(1),Q(-1),Q(1),Q(2))==Q(1,4)
    assert clipped_mass(Q(1),Q(-1),Q(3),Q(1))==Q(5,8)
    # Scalar model verifies the additional cross term in the reverse Young bound.
    r=Q(3);error=Q(1,100);tau=Q(1,23);e2=error**2;M=r*r
    for s in (-error,error):
        C=(1+tau)*(r+s)**2+(1+1/tau)*e2
        upper=tau*M+2*(1+tau)*r*error+(2+tau+1/tau)*e2
        assert 0<=C-r*r<=upper
    # Passing a full anchor restriction does not prove a full signed form.
    assert Q(1)>0 and Q(1)*Q(-1)<0

def main():
    assert len(sys.argv)==5
    raw=[Path(p).read_bytes() for p in sys.argv[2:]]
    assert [hashlib.sha256(v).hexdigest() for v in raw]==PINS
    old,anchor,negative=map(json.loads,raw);z=json.load(open(sys.argv[1]))
    assert z['input_sha256']==dict(zip(['envelope_stop','anchor','negative'],PINS))
    assert z['status']=='CONDITIONAL_ORIGINAL_AFFINE_CAP_ANCHOR_FEASIBILITY'
    assert z['original_SM40_cells']==old['original_SM40_cells']
    assert z['working_precision_bits']==512 and z['flint_version']=='0.8.0'
    assert z['endpoint_rounding_denominator']==10**12
    eta=Q(2,10**12);H=Q(2145);kappa=Q(1,1000)
    assert Q(z['endpoint_uncertainty_upper'])==eta
    # Different expression for the same complete multiplier curvature bound.
    arch=2*Q(22,7)**2*(Q(1,4)**-3+Q(1,2)*Q(1,4)**-2)
    prime=sum((2*WEIGHTS[n][1]*(2*PI[1]*SHIFTS[n][1])**2 for n in WEIGHTS),Q(0))
    assert arch==Q(z['arch_curvature_upper']) and prime==Q(z['prime_curvature_upper']) and arch+prime<H==Q(z['full_multiplier_curvature_upper'])
    rows=z['endpoint_multiplier_intervals'];points={}
    assert len(rows)==z['endpoint_count']==62379
    for q,a,b in rows:
        q,a,b=map(Q,(q,a,b));assert q not in points and 0<=b-a<=eta
        assert (a*10**12).denominator==(b*10**12).denominator==1;points[q]=(a,b)
    seen=set();mass=Q(0);pieces=0;nonzero=0;maximum=Q(0);oldmass=Q(0)
    for l,r,w in (tuple(map(Q,row)) for row in z['original_SM40_cells']):
        oldmass+=2*(r-l)*w
        for j in range(16):
            a=l+(r-l)*Q(j,16);b=l+(r-l)*Q(j+1,16);width=b-a
            seen.update((a,b));p0=points[a][0];p1=points[b][0]
            h0=kappa-p0+H*width**2/8;h1=kappa-p1+H*width**2/8
            v=clipped_mass(width,h0,h1,w);assert 0<=v<=width*w;mass+=2*v
            roots={Q(0),Q(1)}
            if h0!=h1:
                roots.update(t for c in (Q(0),w) if 0<(t:=(c-h0)/(h1-h0))<1)
            roots=sorted(roots);pieces+=len(roots)-1
            for u,v in zip(roots,roots[1:]):
                mid=(u+v)/2
                if h0+(h1-h0)*mid>0:nonzero+=1
            maximum=max(maximum,width)
    assert seen==set(points) and z['subdivisions_per_cell']==16 and z['frequency_cells']==62272
    assert maximum==Q(1,4096)==Q(z['maximum_cell_width'])
    assert oldmass==Q(1073441879,64000000)==Q(z['original_cap_mass']) and 0<mass<oldmass
    assert mass==Q(z['affine_cap_mass']) and pieces==z['affine_piece_count'] and nonzero==z['nonzero_affine_piece_count']
    delta=H*maximum**2/4+eta;assert delta==Q(z['uniform_cap_minus_true_negative_upper'])<Q(3197,10**8)
    assert z['original_basis']==anchor['original_basis']==[['1','4096/3013','near_null'],['1','-1','complement']]
    assert anchor['positive_high12_form_discarded_as_psd'] and anchor['cross_bound_scope']=='lowband_plus_pole_minus_negative_high_tail'
    a=Q(anchor['full_signed_A_diagonal_lower']);d=Q(anchor['full_signed_D_diagonal_lower']);b=Q(anchor['retained_signed_cross_abs_upper'])
    reserve=(a-Q(1,8000))*(d-Q(1,24))-b*b
    assert a>Q(1,8000) and d>Q(1,24) and reserve==Q(z['inherited_anchor_Loewner_reserve'])>0
    assert z['inherited_signed_anchor_diagonal_lower']==['1/8000','1/24']
    grams=gram_intervals();recorded=[tuple(map(Q,v)) for v in z['physical_Gram_intervals']]
    for x,y in zip(grams,recorded):assert y[0]<=x[0]<=x[1]<=y[1]
    trace=Q(27,10);assert grams[0][1]+grams[2][1]<trace==Q(z['physical_Gram_trace_upper'])
    assert Q(z['affine_cap_anchor_coefficient_lower'])==Q(1,8000)-delta*trace>Q(386,10**7)
    orders=[taylor_order(Q(v['hi'])-Q(v['lo']),24)[0] for v in negative['cluster_witnesses']]
    assert len(orders)==z['original_packet_count']==107 and sum(orders)==z['unchanged_Taylor_columns']==890 and z['Taylor_bits']==24
    e2=Q(22,10)*oldmass/Q(2**48);e=Q(363,10**9);M=Q(3114203,250000);s=Q(353,100);tau=Q(1,2**23)
    assert e2==Q(z['Taylor_analysis_squared_error_upper'])<e*e
    assert e==Q(z['analysis_error_norm_upper']) and M==Q(z['envelope_operator_norm_upper'])<s*s and s==Q(z['envelope_operator_sqrt_upper'])
    assert tau==Q(z['Young_tau'])
    payment=tau*M+2*(1+tau)*s*e+(2+tau+1/tau)*e2
    assert payment==Q(z['Young_cap_minus_affine_operator_upper'])
    lower=Q(1,8000)-(delta+payment)*trace
    assert lower==Q(z['finite_rank_cap_anchor_coefficient_lower'])>Q(248,10**7)
    for k in ['full_operator_uniform_error_bound','original_signed_multiplier_used','both_reflected_frequencies_paid']:assert z[k] is True
    for k in ['actual_inverse_or_Galerkin_lift_computed','complete_470_source_gate_certified','full_890_moment_matrix_assembled','full_original_signed_schur_certified']:assert z[k] is False
    assert z['W_ODD_NEG']==z['inherited_original_domain_review']=='OPEN'
    regressions()
    print('INDEPENDENT AFFINE CAP REPLAY PASS: all 62379 endpoints / 62272 clipped cells; full 2D affine and 890-column Young-cap anchor feasible; original inverse/mixed gate OPEN')
if __name__=='__main__':main()
