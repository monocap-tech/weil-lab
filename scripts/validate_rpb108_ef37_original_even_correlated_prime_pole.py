#!/usr/bin/env python3
"""EF37: certified original 7-prime / positive even pole correlations and full arch bound.

Unchanged first SI10 source e=1_[-B,B]cos(omega x), B=11/10,
omega=2*pi*37/64. Original full row-reduced gradient:
 h=g_e-a_arch(c0)*e =
   -SUM_{n=2,3,4,5,7,8,9} w_n P_I[e(x+ln n)+e(x-ln n)]
   + 2u cosh(x/2) + h_cut(x),
where w_n=ln(prime(n))/sqrt(n) and u=<cosh(x/2),e>.

The prime+pole combination is a genuine correlated signed source:
on each of 8 positive-half physical cutoff cells it has
 P cos(omega x)+Q sin(omega x)+2u cosh(x/2).
We integrate its squared norm EXACTLY by primitive identities with
native 10^340 integer outward interval. No free or omitted prime channel.
The full untruncated original arch cut h_cut receives a sharper
whole-L2 norm via 80 directed outward half-integer mode norms and
a rigorously summed infinite lambda^-3/2 plus exponential tail.

No inverse Schur projection is computed. The resulting global
L2 norm, though dramatically tighter than EF36, is still only an
upper on ||P_F g_e||, not an actual distance to original V469.
The original physical EF26/29 arch identity and Fourier/domain
attachment remain separate independent analytic audit obligations.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json
from validate_rpb108_si06_negative_band import B,ACTIVE,ln_bounds
from validate_rpb108_ef24_original_even_edge_intervals import (
    I,S,PI,trig_pi,source_sqrt
)
from validate_rpb108_ef29_original_even_mixed_vector import (
    C0,OMEGA,exp_minus,source_weights_and_phases
)
from validate_rpb108_ef26_original_even_arch_laplace import epos,eneg
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import (
    original_even_pole_diagonal
)
from validate_rpb108_ef28_pole_neutral_moment_kernel import (
    original_source_and_geometry
)

ROOT=Path(__file__).resolve().parents[1]
NS=(2,3,4,5,7,8,9)
MU=F(17,25000)
ARCH_TERM_COUNT=80
BASE_SQ_CAP=F(7,10)
BASE_NORM_CAP=F(17,20)
ARCH_NORM_CAP=F(3,5)
COMBINED_CAP=F(29,20)
DUAL_CAP=COMBINED_CAP**2/MU

def full_original_prime_cells():
    logs={n:ln_bounds(n,terms=450) for n in NS}
    weights,phases=source_weights_and_phases(logs)
    # All genuine even source shifts 0<ln n<2B and no ln n=B.
    cuts=[]
    for n in NS:
        lo,hi=logs[n]
        assert 0<lo<hi<2*B
        assert (hi<B or lo>B)
        a,b=(B-hi,B-lo) if hi<B else (lo-B,hi-B)
        assert 0<a<=b<B
        cuts.append((a,b,n))
    cuts.sort(key=lambda x:(x[0]+x[1])/2)
    assert [n for _,_,n in cuts]==[3,4,2,5,7,8,9]
    endpoints=[I.rational(0)]+[I.rational_bounds(a,b) for a,b,_ in cuts]+[I.rational(B)]
    assert all(endpoints[k].hi<endpoints[k+1].lo for k in range(8))
    cells=[]
    for ix in range(8):
        left,right=endpoints[ix],endpoints[ix+1]
        probe=F(left.hi+right.lo,2*S)
        p=I(0);q=I(0);flags={}
        for n in NS:
            lo,hi=logs[n]
            plus=probe < B-hi
            plus_off=probe > B-lo
            assert plus or plus_off
            minus=probe > hi-B
            minus_off=probe < lo-B
            assert minus or minus_off
            flags[n]=(int(plus),int(minus))
            cn,sn=phases[n]
            w=weights[n]
            p=p-w*cn*(int(plus)+int(minus))
            q=q+w*sn*(int(plus)-int(minus))
        cells.append((left,right,p,q,flags))
    return cells,cuts

def endpoint_data(x):
    c,s=trig_pi(2*C0*x)
    c2,s2=trig_pi(4*C0*x)
    ep=epos(x/2)
    em=I(S)/ep
    ch=(ep+em)/2
    sh=(ep-em)/2
    den=OMEGA*OMEGA+F(1,4)
    fc=(sh*c/2+OMEGA*ch*s)/den
    fs=(sh*s/2-OMEGA*ch*c)/den
    return c2,s2,fc,fs

def original_prime_plus_pole_signed_norm_sq():
    centers,orders,xs=original_source_and_geometry()
    assert len(centers)==107 and sum(orders)==469
    cells,cuts=full_original_prime_cells()
    pole,u=original_even_pole_diagonal()
    assert u.hi<0 and pole.hi<S//2
    k=2*u
    integral=I(0)
    records=[]
    for a,b,p,q,flags in cells:
        ca,sa,fca,fsa=endpoint_data(a)
        cb,sb,fcb,fsb=endpoint_data(b)
        L=b-a
        cos2=L/2+(sb-sa)/(4*OMEGA)
        sin2=L/2-(sb-sa)/(4*OMEGA)
        cos_sin=(ca-cb)/(4*OMEGA)
        p2=p*p*cos2+q*q*sin2+2*p*q*cos_sin
        cross=p*(fcb-fca)+q*(fsb-fsa)
        integral=integral+2*p2+4*k*cross
        records.append((flags,L))
    # Full original true positive even pole term k²*(B+sinh B).
    expB=epos(I.rational(B))
    sinhB=(expB-I(S)/expB)/2
    full=integral+k*k*(B+sinhB)
    assert full.lo>0, "true original prime+pole square has positive lower"
    assert F(full.hi,S)<BASE_SQ_CAP,("original signed base too large",full.scaled())
    assert BASE_SQ_CAP<BASE_NORM_CAP**2
    return full,cells

def arch_cut_complete_l2():
    phase_c,phase_s=trig_pi(2*B*C0)
    n=ARCH_TERM_COUNT
    total=F(0)
    for m in range(n):
        lam=F(2*m)+F(1,2)
        lam_i=I.rational(lam)
        # actual EF29 signed coefficient without |...| until final norm
        real=(lam_i*phase_c-OMEGA*phase_s)/(lam_i*lam_i+OMEGA*OMEGA)
        E=exp_minus(lam_i*B)
        # original full physical integral, preserving exponential decay:
        # ||e^(-lambda B)cosh(lambda x)||²
        # =B e^(-2lambda B)+(1-e^(-4lambda B))/(4lambda)
        # <=B e^(-2lambda B)+1/(4lambda).
        norm2=I.rational(B)*E*E+I.rational(F(1)/(4*lam))
        assert norm2.lo>=0
        upper_sqrt=F(isqrt(norm2.hi*S)+1,S)
        upper_amp=F(2*real.abs_upper(),S)
        total+=upper_amp*upper_sqrt
    # Remainder sum_{m>=n} lambda^-3/2
    # <=integral_(n-1)^inf (2t+1/2)^-3/2 dt
    # =1/sqrt(2n-3/2) < 8/100 for n=80.
    assert n==80
    assert F(1,2*n-F(3,2))<F(8,100)**2
    # complete higher-mode exp contribution:
    # 2sqrt B*sum e^-lambda B/lambda
    # <=(11/5) exp(-lambda_n B)/lambda_n * (16/11).
    # Original directed native exp bound <10^-20, thus <10^-4.
    lam_n=F(2*n)+F(1,2)
    e_n=exp_minus(I.rational(lam_n*B))
    assert e_n.hi<S//10**20
    exp_tail=F(11,5)*F(1,10**20)*F(1,lam_n)*F(16,11)
    assert exp_tail<F(1,10000)
    assert total<F(513,1000),("80 original arch absolute modes exceed cap",float(total))
    full_upper=total+F(8,100)+exp_tail
    assert full_upper<ARCH_NORM_CAP,("full infinite arch cutoff tail",float(full_upper))
    return total,exp_tail,full_upper

def main():
    manifest=json.loads((ROOT/'research/obligations.json').read_text())
    ob={x['id']:x for x in manifest['obligations']}
    assert manifest['active_obligation']=='W-EVEN-FORM'
    assert all(ob[k]['status']=='open' for k in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    full,cells=original_prime_plus_pole_signed_norm_sq()
    first,tail,arch=arch_cut_complete_l2()
    assert BASE_NORM_CAP+ARCH_NORM_CAP==COMBINED_CAP
    assert DUAL_CAP<F(17955125,136)
    assert DUAL_CAP>F(1,500)*10**6
    print('EF37 original SI10 107/469 signed even first source,'
          ' genuine 7 prime shifts + true positive pole on 8'
          ' exact physical cutoff cells; exact source positive half'
          ' partition includes n3,n4,n2,n5,n7,n8,n9.',flush=True)
    print('EF37 CERTIFIED original whole signed prime+pole'
          ' correlated physical L2 norm squared:',full.scaled(),
          'strictly <7/10; original signed base L2 <17/20',flush=True)
    print('EF37 original complete quarter-digamma cutoff L2'
          ' absolute 80 exact native outward modes',float(first),
          '+ entire higher lambda tail <',float(F(8,100)+tail),
          'total <3/5',flush=True)
    print('EF37 original full source-row reduced physical gradient'
          ' L2 <29/20=1.45; original full even cofinite projected'
          ' gradient L2 <=same without inverting 469 sources.',flush=True)
    print('EF37 genuine original residual eta energy-dual squared'
          ' <',str(DUAL_CAP),' (approximately',float(DUAL_CAP),')',
          ' after EF36 <17955125/136.',flush=True)
    print('EF37 SCOPE: signed prime+pole correlation is certified;'
          ' arch cutoff is bounded with an infinite full source'
          ' tail but cross with prime+pole remains budgeted by'
          ' triangle. NO actual original V469 L2 projection'
          ' coefficient solve, delta, eta sign comparison or'
          ' full 469-source Schur. W-EVEN-FORM, odd, whole Weil'
          ' and RH remain OPEN.',flush=True)

if __name__=='__main__':
    main()
