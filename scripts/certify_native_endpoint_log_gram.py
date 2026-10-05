"""Rational interval endpoint-log residual Gram, physical degrees 0..7."""
import json
from math import comb
from certify_native_legendre_small_window import F,I,legendre,mul,atan,sqrt_rational


def shifted_legendre(degree):
    out=[]
    for p in legendre(degree):
        row=[F(0)]*len(p)
        for n,c in enumerate(p):
            for k in range(n+1):
                row[k]+=c*comb(n,k)*2**k*(-1)**(n-k)
        out.append(row)
    return out


def exact_log_data(source_degree=7,projection_dimension=64):
    if (source_degree,projection_dimension) not in ((35,36),(47,48),(51,52)) and (source_degree not in (7,19) or projection_dimension not in (20,64)):
        raise ValueError('Unsupported finite source/projection dimensions')
    p=shifted_legendre(max(projection_dimension-1,source_degree))
    maximum_degree=max(projection_dimension-1+source_degree,2*source_degree)
    harmonic=[F(0)]
    harmonic2=[F(0)]
    for n in range(1,maximum_degree+2):
        harmonic.append(harmonic[-1]+F(1,n))
        harmonic2.append(harmonic2[-1]+F(1,n*n))
    moments=[(F(1,(k+1)**2)+harmonic[k+1]/(k+1))/2 for k in range(maximum_degree+1)]
    projections=[]
    for n in range(projection_dimension):
        row=[]
        for i in range(source_degree+1):
            product=mul(p[n],p[i])
            row.append(sum((c*moments[k] for k,c in enumerate(product)),F(0)))
        projections.append(row)
    pi=16*atan(F(1,5))-4*atan(F(1,239))
    zeta2=pi*pi/I(6)
    gram=[[I(0) for _ in range(source_degree+1)] for _ in range(source_degree+1)]
    for i in range(source_degree+1):
        for j in range(i,source_degree+1):
            if (i+j)%2:
                continue
            product=mul(p[i],p[j])
            rational, zeta_coefficient=F(0),F(0)
            for k,c in enumerate(product):
                n=k+1
                moment=(F(2,n**3)+(harmonic[n]**2+harmonic2[n])/n
                        +2*harmonic[n]/n**2+2*harmonic2[n]/n)/4
                rational+=c*moment
                zeta_coefficient-=c/F(2*n)
            full=I(rational)+zeta_coefficient*zeta2
            projected=sum(((2*n+1)*projections[n][i]*projections[n][j]
                           for n in range(projection_dimension)),F(0))
            normalized=(full-projected)*sqrt_rational(F((2*i+1)*(2*j+1)))
            gram[i][j]=gram[j][i]=normalized
    assert max(x.hi-x.lo for row in gram for x in row)<F(1,10**35)
    assert gram[0][0].lo>0
    return p,projections,gram


def certificate():
    _,_,gram=exact_log_data()
    return dict(status='certified endpoint-log part only',
                source_degrees=[0,7],projected_away_degrees=[0,63],
                physical_basis='sqrt(2n+1) P_n(2x)',
                endpoint_log='-0.5 log((x+0.5)(0.5-x))',
                residual_gram_intervals=[[[str(x.lo),str(x.hi)] for x in row] for row in gram],
                largest_entry_width_bound='1/10^35',
                full_source_gram_certified=False,schur_sign_certified=False)


if __name__=='__main__':
    print(json.dumps(certificate(),indent=2))

