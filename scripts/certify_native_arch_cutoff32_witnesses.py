"""Exact rational outward certificates of two negative ORIGINAL-arithmetic cutoffs.

The original untruncated form is not declared negative. No floating arithmetic
is used by this certificate; discovery of the saved vectors was numerical.
"""
from fractions import Fraction as F
from math import isqrt
from pathlib import Path
import json

GRID=10**40


def outward(lo,hi):
    return (F((lo*GRID).__floor__(),GRID),F((hi*GRID).__ceil__(),GRID))


def point(v):
    return (F(v),F(v))


def add(a,b):
    return outward(a[0]+b[0],a[1]+b[1])


def neg(a):
    return (-a[1],-a[0])


def sub(a,b):
    return add(a,neg(b))


def mul(a,b):
    vals=[x*y for x in a for y in b]
    return outward(min(vals),max(vals))


def inv(a):
    assert a[0]>0
    return outward(1/a[1],1/a[0])


def scale(a,v):
    return mul(a,point(v))


def logarithm(v,terms=200):
    assert v>=1
    z=point((v-1)/(v+1));z2=mul(z,z);power=z;total=point(0)
    for j in range(terms):
        total=add(total,scale(power,F(2,2*j+1)))
        power=mul(power,z2)
    tail=2*power[1]/F(2*terms+1)/(1-z2[1])
    return outward(total[0],total[1]+tail)


def atan(v,terms):
    total=sum(((-1)**j*v**(2*j+1)/F(2*j+1) for j in range(terms)),F(0))
    next_term=(-1)**terms*v**(2*terms+1)/F(2*terms+1)
    return outward(min(total,total+next_term),max(total,total+next_term))


def exp_point(v):
    if v<0:
        return inv(exp_point(-v))
    assert v<=2
    term=point(1);total=point(1)
    for j in range(1,65):
        term=scale(term,v/F(j));total=add(total,term)
    next_hi=term[1]*v/F(65)
    tail=next_hi/(1-v/F(66))
    return outward(total[0],total[1]+tail)


def constants():
    logs={n:logarithm(F(n)) for n in [2,3,4,5,7,8]}
    pi=scale(sub(scale(atan(F(1,5),32),4),atan(F(1,239),12)),4)
    logpi=(logarithm(pi[0])[0],logarithm(pi[1])[1])
    harmonic=point(0)
    for j in range(1,4097):
        harmonic=add(harmonic,point(F(1,j)))
    harmonic_minus_log=sub(harmonic,scale(logs[2],12))
    gamma=(harmonic_minus_log[0]-F(1,4096),harmonic_minus_log[1])
    m00=neg(add(add(gamma,scale(pi,F(1,2))),add(scale(logs[2],3),logpi)))
    return logs,m00


def sqrt_interval(v):
    n=isqrt(v*GRID*GRID)
    return F(n,GRID),F(n+1,GRID)


def certify(row,logs,m00):
    a=F(row['a']);n=row['cells'];N=row['N'];d=2*a/n
    assert a in (F(1),F(21,20)) and n==128 and N==32
    w=[F(v,row['value_denominator']) for v in row['cell_value_numerators']]
    parity=row['parity'];assert all(w[n-1-i]==(-w[i] if parity=='odd' else w[i]) for i in range(n))
    corr=[sum((w[i]*w[i+k] for i in range(n-k)),F(0)) for k in range(n)]
    mass=d*corr[0];assert mass>0
    L=add(m00,point(sum((F(4,4*j+1) for j in range(N)),F(0))))
    krow=[point(0) for _ in range(n)]
    for j in range(N):
        alpha=F(4*j+1,2)
        t=exp_point(-alpha*d);u=sub(point(1),t)
        diag=sub(point(2/alpha),scale(u,2/(alpha*alpha*d)))
        krow[0]=add(krow[0],diag)
        off=scale(mul(u,u),1/(alpha*alpha*d))
        power=point(1)
        for k in range(1,n):
            krow[k]=add(krow[k],mul(off,power));power=mul(power,t)
    K=scale(krow[0],d*corr[0])
    for k in range(1,n):
        K=add(K,scale(krow[k],2*d*corr[k]))
    arch=sub(scale(L,mass),K)
    prime=point(0)
    dictionary=[(2,2),(3,3),(4,2),(5,5),(7,7)]+([(8,2)] if a>1 else [])
    for z,p in dictionary:
        shift=scale(logs[z],1/d)
        cell=int(shift[0]);assert cell==int(shift[1]) and cell+1<n
        frac=sub(shift,point(cell))
        C=scale(add(scale(sub(point(1),frac),corr[cell]),
                    scale(frac,corr[cell+1])),d)
        amplitude=mul(logs[p],inv(sqrt_interval(z)))
        prime=add(prime,scale(mul(amplitude,C),2))
    plus=point(0);minus=point(0)
    for i in range(n):
        left=-a+i*d;right=left+d
        plus=add(plus,scale(sub(exp_point(right/2),exp_point(left/2)),2*w[i]))
        minus=add(minus,scale(sub(exp_point(-left/2),exp_point(-right/2)),2*w[i]))
    pole=scale(mul(plus,minus),2)
    form=add(sub(arch,prime),pole)
    target=F(49,1000) if a==1 else F(59,1000)
    assert form[1]<-target*mass
    result={'a':str(a),'N':N,'cells':n,'parity':parity,'physical_mass':str(mass),
            'Q_N_interval':[str(x) for x in form],
            'strict_rayleigh_upper':str(-target),
            'original_form_declared_negative':False,
            'original_control':'certified positive aperture-one anchor applies' if a==1 else 'original sign not certified here',
            'complete_active_prime_powers':[z for z,p in dictionary]}
    B=F(77937,40000) if a==1 else F(1063939,500000)
    assert L[0]-B>F(157,1000)
    assert L[1]<F(5,2) and B<F(11,5)
    sinh=scale(sub(exp_point(a),exp_point(-a)),F(1,2))
    assert sinh[1]<F(13,10)
    # ||F_N|| <= L_N+B+2(a+sinh(a)) < 10.
    assert L[1]+B+2*(a+sinh[1])<10
    result['cutoff_compact_gain_strict_lower']=str(1+target/10)
    return result


def run():
    source=Path(__file__).resolve().parents[1]/'notes/data/RPB108_ARCH_CUTOFF32_WITNESSES_20261008.json'
    rows=json.loads(source.read_text())['witnesses']
    logs,m00=constants()
    # Structural controls distinguish the cutoff from the original.
    assert m00[0]>-F(27,5)
    assert logs[8][0]>2 and logs[8][1]<F(21,10)
    assert 2*logs[3][0]>F(21,10)
    results=[certify(row,logs,m00) for row in rows]
    return {'passed':True,'scope':'exact rational physical-vector cutoff sign certificates',
            'certified_negative_cutoff_vectors':len(results),'results':results,
            'whole_original_positivity_extended':False,'lean_certified':False}


if __name__=='__main__':
    print(json.dumps(run(),indent=2))
