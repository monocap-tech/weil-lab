#!/usr/bin/env python3
"""EF41: exact four ORIGINAL first-cluster SI10 even Fourier-jet rows.

Project the genuine EF39 finite signed source response H40=z+h40
against the native SI10 protected real-even jets
  cos(omega*x), x*sin(omega*x), x**2*cos(omega*x), x**3*sin(omega*x).
The first original frequency center is 37/64 and Taylor order 15;
all four directions lie inside its actual protected 469-source span.
All physical integrals use the original eight seven-prime cutoff cells,
true even pole, and all 40 signed half-integer arch cutoff modes.
Exact outward intervals at radix 10**340 cover 4x4 Gram and response.
The infinite m>=40 original arch tail is never dropped.
The four-row projected finite squared norm is <47/1000,
complete cofinite projected norm <1/3, original eta <25000/153.
No full 469D source projector or Weil positivity is claimed.
"""
import json
from fractions import Fraction as F
from math import factorial
from pathlib import Path

from validate_rpb108_ef24_original_even_edge_intervals import I,S,trig_pi
from validate_rpb108_ef29_original_even_mixed_vector import C0,OMEGA,exp_minus
from validate_rpb108_ef26_original_even_arch_laplace import epos
from validate_rpb108_ef28_pole_neutral_moment_kernel import original_source_and_geometry
from validate_rpb108_ef32_even_471_bell_negative_gate_stop import original_even_pole_diagonal
from validate_rpb108_ef37_original_even_correlated_prime_pole import full_original_prime_cells
from validate_rpb108_ef39_original_even_full_arch_cross_first_row import run_source,original_tail,N
from validate_rpb108_si06_negative_band import B

ROOT=Path(__file__).resolve().parents[1]
ORDER=4
MU=F(17,25000)
FOUR_SQUARE_CAP=F(47,1000)
FULL_NORM_CAP=F(1,3)
ENERGY_DUAL_CAP=F(25000,153)

def power(x,n):
    p=I(S)
    for _ in range(n):
        p=p*x
    return p

def cmul(z,w):
    return (z[0]*w[0]-z[1]*w[1],z[0]*w[1]+z[1]*w[0])

def cadd(z,w):
    return (z[0]+w[0],z[1]+w[1])

def endpoint(x):
    c,s=trig_pi(2*C0*x)
    c2,s2=trig_pi(4*C0*x)
    ep=epos(x/2)
    em=I(S)/ep
    return x,(c,s),(c2,s2),ep,em

def primitive(n,a,beta,point,expmag,phase):
    # Exact antiderivative for x^n exp[(a+i beta)x] with a
    # possibly negative. exmpag=e^(ax) (or scaled arch e^(-lam B+ax)).
    x=point[0]
    a=I.rational(a)
    beta=I.rational(beta) if isinstance(beta,F) else beta
    den=a*a+beta*beta
    assert den.lo>0
    inv=(a/den,-beta/den)
    term=inv
    p=(I(0),I(0))
    for j in range(n+1):
        coeff=F(((-1)**j)*factorial(n),factorial(n-j))
        p=cadd(p,(term[0]*coeff*power(x,n-j),
                  term[1]*coeff*power(x,n-j)))
        term=cmul(term,inv)
    return cmul((expmag*phase[0],expmag*phase[1]),p)

def mom(n,a,beta,left,right,mode):
    # Unscaled original physical moment with a=0 or +/-1/2;
    # mode 1=cos(omega*x), 2=cos(2omega*x), 0=trivial.
    if mode==0:
        assert beta==0 and a==0
        return (power(right[0],n+1)-power(left[0],n+1))/(n+1),I(0)
    def obj(p):
        magn=I(S) if a==0 else p[3] if a==F(1,2) else p[4]
        phase=p[1] if mode==1 else p[2]
        return primitive(n,a,beta,p,magn,phase)
    l,r=obj(left),obj(right)
    return (r[0]-l[0],r[1]-l[1])

def gram_four():
    aa=endpoint(I(0))
    bb=endpoint(I.rational(B))
    G=[[None]*ORDER for _ in range(ORDER)]
    for i in range(ORDER):
        for j in range(i,ORDER):
            n=i+j
            zero=(power(bb[0],n+1)-power(aa[0],n+1))/(n+1)
            twice=mom(n,0,2*OMEGA,aa,bb,2)
            if i%2==j%2:
                val=zero+(twice[0] if i%2==0 else -twice[0])
            else:
                val=twice[1]
            G[i][j]=G[j][i]=val
    return G

def true_original_signed_jet_pairings():
    cells,_=full_original_prime_cells()
    points=[endpoint(cells[0][0])]+[endpoint(c[1]) for c in cells]
    assert len(points)==9 and points[0][0].lo==0 and points[-1][0].lo==B*S
    _,u=original_even_pole_diagonal()
    pole=2*u
    b=[]
    pc,ps=trig_pi(2*B*C0)
    for n in range(ORDER):
        trig_cos=(n%2==0)
        primepole=I(0)
        for i,(_,__,P,Q,flags) in enumerate(cells):
            left,right=points[i],points[i+1]
            int0=(power(right[0],n+1)-power(left[0],n+1))/(n+1)
            cos2,sin2=mom(n,0,2*OMEGA,left,right,2)
            if trig_cos:
                part=P*(int0+cos2)/2+Q*sin2/2
            else:
                part=P*sin2/2+Q*(int0-cos2)/2
            # Original even pole cosh(x/2) is half sum of +/- exponentials.
            plus=mom(n,F(1,2),OMEGA,left,right,1)
            minus=mom(n,F(-1,2),OMEGA,left,right,1)
            s=0 if trig_cos else 1
            part+=pole*(plus[s]+minus[s])/2
            primepole+=2*part
        arch=I(0)
        for m in range(N):
            lam=F(2*m)+F(1,2)
            li=I.rational(lam)
            coeff=2*(li*pc-OMEGA*ps)/(li*li+OMEGA*OMEGA)
            # Physical arch endpoints: exp[-lambda(B +/-x)] no overflow.
            def one(point,sgn):
                x,phase,twice,ep,em=point
                mag=exp_minus(li*(I.rational(B)-x if sgn>0 else I.rational(B)+x))
                return primitive(n,sgn*lam,OMEGA,point,mag,phase)
            lo=one(points[0],1); hi=one(points[-1],1)
            lo2=one(points[0],-1); hi2=one(points[-1],-1)
            ind=0 if trig_cos else 1
            arch+=coeff*((hi[ind]-lo[ind])+(hi2[ind]-lo2[ind]))
        b.append(primepole+arch)
    return b

def source_four_row_schur():
    centers,orders,_=original_source_and_geometry()
    assert len(centers)==107 and sum(orders)==469
    assert centers[0]==C0 and orders[0]==15
    # Original Fourier even real jet signs:
    # x^0 cos, -x sin, -x^2 cos, +x^3 sin.
    # Such sign changes do not change the protected source span.
    G=gram_four()
    b=true_original_signed_jet_pairings()
    prior,full,cross,he,hsq=run_source()
    # Exact native 4x4 source projection in Schur/Gram-Schmidt form.
    A=[[G[i][j] for j in range(ORDER)] for i in range(ORDER)]
    r=[x for x in b]
    D=full
    stages=[]
    for k in range(ORDER):
        pivot=A[k][k]
        assert pivot.lo>0,('true protected Gram pivot',k,pivot.scaled())
        gain=r[k]*r[k]/pivot
        D=D-gain
        assert D.lo>0,('source projected squared negative',k,D.scaled())
        stages.append((pivot,gain,D))
        for i in range(k+1,ORDER):
            for j in range(i,ORDER):
                A[i][j]=A[i][j]-A[i][k]*A[j][k]/pivot
                A[j][i]=A[i][j]
            r[i]=r[i]-A[i][k]*r[k]/pivot
    assert F(stages[0][2].hi,S)<F(63,1000)
    assert F(stages[1][2].hi,S)<F(29,500)
    assert F(stages[2][0].lo,S)>F(1,7)
    assert F(stages[3][0].lo,S)>F(1,40)
    assert F(stages[2][2].hi,S)<F(56,1000)
    assert F(stages[3][2].hi,S)<FOUR_SQUARE_CAP
    assert FOUR_SQUARE_CAP<F(217,1000)**2
    return G,b,stages,full

def main():
    data=json.loads((ROOT/'research/obligations.json').read_text())
    obs={x['id']:x for x in data['obligations']}
    assert data['active_obligation']=='W-EVEN-FORM'
    assert 'EF40' in obs['W-EVEN-FORM']['evidence']
    assert all(obs[x]['status']=='open' for x in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    G,b,stages,full=source_four_row_schur()
    for i,x in enumerate(b):
        print('EF41 real original first-cluster Taylor jet',i,
              'exact full signed physical <H40,v_i>:',x.scaled(),flush=True)
    for i,(pivot,gain,residual) in enumerate(stages):
        print('EF41 genuine original source 4x4 Schur step',i,
              'pivot',pivot.scaled(),'gain',gain.scaled(),
              'finite signed projected norm²',residual.scaled(),flush=True)
    tail=original_tail()
    assert tail < F(57,500)+F(1,10000)
    assert F(217,1000)+F(57,500)+F(1,10000)<FULL_NORM_CAP
    assert FULL_NORM_CAP**2/MU==ENERGY_DUAL_CAP
    assert ENERGY_DUAL_CAP<F(3240,17)
    print('EF41 certified ORIGINAL finite 4-row signed physical'
          ' projected squared L2 residual <47/1000;'
          ' complete native 40+ infinite arch tail norm <',
          float(tail),'so the complete 469D cofinite first-source'
          ' projected norm <1/3 and unseen energy dual eta'
          ' <25000/153 =',float(ENERGY_DUAL_CAP),flush=True)
    print('EF41 status: original 4 of 469 SI10 even source rows only;'
          ' true physical full signed form Schur and RH OPEN.'
          ' Independent Fourier/digamma/form-domain audit OPEN.',flush=True)

if __name__=='__main__':
    main()
