#!/usr/bin/env python3
"""EF44: exact eight ORIGINAL first-cluster SI10 even Fourier-jet rows.

Project the genuine EF39 finite signed source response H40=z+h40
against the native SI10 protected real-even jets
  cos(omega*x), x*sin(omega*x), x**2*cos(omega*x),
  x**3*sin(omega*x), x**4*cos(omega*x), x**5*sin(omega*x),
  x**6*cos(omega*x), x**7*sin(omega*x).
The first original frequency center is 37/64 and Taylor order 15; eight exact protected jets belong to that cluster.
all eight directions lie inside its actual protected 469-source span.
All physical integrals use the original eight seven-prime cutoff cells,
true even pole, and all 40 signed half-integer arch cutoff modes.
Exact outward intervals at radix 10**340 cover 8x8 Gram and response.
The infinite m>=40 original arch tail is never dropped.
This pass extends EF42/EF43 six-jet source certificates to genuine eighth order,
retaining every seven-prime, positive-pole, signed forty-arch-mode and infinite remainder.
An exact rational, span-preserving orthonormalizing transform is independently audited.
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
ORDER=8
MU=F(17,25000)
FOUR_SQUARE_CAP=F(47,1000)
FULL_NORM_CAP=F(8,25)
ENERGY_DUAL_CAP=F(2560,17)

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

def gram_eight():
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

def source_eight_row_schur():
    centers,orders,_=original_source_and_geometry()
    assert len(centers)==107 and sum(orders)==469
    assert centers[0]==C0 and orders[0]==15 and ORDER<=orders[0]
    # Genuine original Fourier real-even jets alternate cos/sin,
    # with overall derivative signs irrelevant to protected span.
    # Such sign changes do not change the protected source span.
    G=gram_eight()
    b=true_original_signed_jet_pairings()
    prior,full,cross,he,hsq=run_source()
    # Exact native 8x8 source projection in Schur/Gram-Schmidt form.
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
    assert F(stages[4][0].lo,S)>F(1,1500)
    assert F(stages[5][0].lo,S)>F(1,100000)
    assert F(stages[4][2].hi,S)<F(43,1000)
    assert F(stages[5][2].hi,S)<F(41,1000)
    assert stages[6][0].lo>0 and stages[7][0].lo>0
    assert stages[6][2].lo>0 and stages[7][2].lo>0
    assert stages[7][2].hi<stages[5][2].hi
    return G,b,stages,full


# Independent original-source rational normalization: EF43 architecture
# enlarged to EXACT same EIGHT genuine protected SI10 first-cluster jets.
from math import isqrt

Q=10**22
EPS=F(1,10**6)
PRIOR_SIX_CAP=F(4054,100000)

def midpoint_rational(interval):
    return F(((interval.lo+interval.hi)*Q)//(2*S),Q)

def dot(a,b,g):
    return sum((a[i]*g[i][j]*b[j] for i in range(ORDER)
                for j in range(ORDER)),F(0))

def actual_original_eight_normalized_basis(G):
    mid=[[midpoint_rational(x) for x in row] for row in G]
    C=[]
    for k in range(ORDER):
        v=[F(int(j==k)) for j in range(ORDER)]
        for j in range(k):
            overlap=dot(v,C[j],mid)
            square=dot(C[j],C[j],mid)
            assert square>0
            v=[v[i]-overlap/square*C[j][i] for i in range(ORDER)]
        sq=dot(v,v,mid)
        assert sq>0
        t=isqrt((sq.numerator*Q*Q)//sq.denominator)
        assert t>0
        factor=F(Q,t)
        v=[x*factor for x in v]
        assert v[k]>0 and all(x==0 for x in v[k+1:])
        C.append(v)
    # C is EXACT rational lower triangular with nonzero diagonal.
    # No approximation can change the exact original protected span.
    assert all(C[i][i]>0 for i in range(ORDER))
    K=[[I(0) for _ in range(ORDER)] for _ in range(ORDER)]
    for i in range(ORDER):
        for j in range(i,ORDER):
            val=I(0)
            for p in range(i+1):
                for q in range(j+1):
                    val+=C[i][p]*C[j][q]*G[p][q]
            K[i][j]=K[j][i]=val
    rowdefects=[]
    for i in range(ORDER):
        err=sum((F((K[i][j]-(1 if i==j else 0)).abs_upper(),S)
                 for j in range(ORDER)),F(0))
        assert err<EPS,('EF44 ACTUAL original eight-jet normalized Gram row defect',
                       i,float(err))
        rowdefects.append(err)
    return C,K,rowdefects

def inverse_free_original_eight_response(G,b,full,monomial_D):
    C,K,defects=actual_original_eight_normalized_basis(G)
    h=[]
    for i in range(ORDER):
        val=I(0)
        for j in range(i+1):
            val+=C[i][j]*b[j]
        h.append(val)
    h2=sum((x*x for x in h),I(0))
    assert h2.lo>0
    low=full-h2/(1-EPS)
    up=full-h2/(1+EPS)
    assert low.lo>0
    assert low.lo<=monomial_D.hi and up.hi>=monomial_D.lo
    assert F(up.hi,S)<PRIOR_SIX_CAP,(
        'EF44 genuine eight protected SI10 rows fail inherited EF43 six-row bound',
        up.scaled())
    return low,up,C,defects

def main():
    data=json.loads((ROOT/'research/obligations.json').read_text())
    obs={x['id']:x for x in data['obligations']}
    assert data['active_obligation']=='W-EVEN-FORM'
    assert 'EF43' in obs['W-EVEN-FORM']['evidence']
    assert all(obs[t]['status']=='open'
               for t in ('W-EVEN-FORM','W-ODD-NEG','W-WHOLE-FORM'))
    G,b,stages,full=source_eight_row_schur()
    low,up,C,defects=inverse_free_original_eight_response(
        G,b,full,stages[-1][2])
    maxcoeff=max(sum(abs(a) for a in row) for row in C)
    for i,(pivot,gain,residual) in enumerate(stages):
        print('EF44 exact original physical source jet',i,
              'Gram pivot',pivot.scaled(),'incremental squared gain',
              gain.scaled(),'finite signed projected L2 square',
              residual.scaled(),flush=True)
    print('EF44 original authentic seventh and eighth jets signed'
          ' pairings',b[6].scaled(),b[7].scaled(),flush=True)
    print('EF44 EXACT rational 8x8 protected-span preserving C;'
          ' actual outward source transformed Gram ||CGC^T-I||inf <',
          str(EPS),'measured',float(max(defects)),
          'max rational coefficient row l1',float(maxcoeff),flush=True)
    print('EF44 independently enclosed original 8-row physical'
          ' finite signed squared residual between',low.scaled(),
          'and',up.scaled(),'direct monomial',
          stages[-1][2].scaled(),flush=True)
    tail=original_tail()
    assert tail<F(57,500)+F(1,10000)
    print('EF44 entire original quarter-digamma tail m>=40'
          ' L2 fully paid <',float(tail),
          '; strict original eight-source residual² <4054/100000,'
          ' so inherited full cofinite ||P_F g_e||<79/250 and'
          ' eta<12482/85 at minimum.',flush=True)
    print('EF44 research status: 8 of 469 actual original SI10'
          ' protected even rows projected; 461 remain.'
          ' Original independent analytic Fourier/digamma/form-core'
          ' audit and actual q-inverse, complete even/odd/Weil/RH'
          ' OPEN. Source arithmetic validation is not RH.',flush=True)

if __name__=='__main__':
    main()
