"""One actual degree-112 complement trial, not a full Schur certificate.

Uses exact rational polynomial integration and outward endpoint-log moments.
Reconstructs only the even part of the saved witness and one rational trial.
Odd witness coordinates remain included in the saved baseline lower bound.
"""
import json, hashlib, sys, gzip
from pathlib import Path
from math import factorial, lcm
from functools import lru_cache
from certify_native_legendre_small_window import F,I,add,bernoulli,atan
from certify_native_endpoint_log_gram import shifted_legendre
from certify_native_prime8_translation_panels_105 import translation_panels
from certify_native_prime8_source112_engine_105 import compose,exact_reflect,regular_difference_factor,sqrt_rational

ROOT=Path(__file__).resolve().parents[1]
D=F(21,10)
I.grid=10**800

@lru_cache(None)
def log(x):
    # Fixed-grid interval summation avoids powers of huge endpoint denominators.
    assert x>0
    exponent=0
    while x>=2:x/=2;exponent+=1
    while x<1:x*=2;exponent-=1
    def unit(y):
        z=I((y-1)/(y+1));z2=z*z;power=z;value=I(0)
        for k in range(1000):
            value+=2*power/(2*k+1);power*=z2
        # |z| <= 1/3 after range reduction. The nonnegative tail is
        # <= 2*(1/3)^2001 / (2001*(1-1/9)); interval arithmetic rounds out.
        tail=F(9,4*2001*3**2001)
        return value+I(0,tail)
    return unit(x)+exponent*unit(F(2))

def mul(p,q):
    dp=lcm(*(x.denominator for x in p));dq=lcm(*(x.denominator for x in q))
    pp=[int(x*dp) for x in p];qq=[int(x*dq) for x in q]
    out=[0]*(len(p)+len(q)-1)
    for i,x in enumerate(pp):
        if x:
            for j,y in enumerate(qq):
                if y:out[i+j]+=x*y
    return [F(x,dp*dq) for x in out]

def dot(p,m):
    den=lcm(*(c.denominator for c in p))
    lo=hi=0
    for c,x in zip(p,m):
        c=int(c*den);a=int(x.lo*I.grid);b=int(x.hi*I.grid)
        lo+=c*(a if c>=0 else b);hi+=c*(b if c>=0 else a)
    return I(F(lo,den*I.grid),F(hi,den*I.grid))

def source(p,M0,M1):
    """Actual q_p = endpoint-log*p + piecewise regular polynomial + error.

    All inputs here are even under t -> 1-t. M1 bounds |d_t p|.
    The kernel remainder follows the original uniform-source constructor.
    The enlarged factor 100 on the pole remainder is conservative.
    """
    assert exact_reflect(p)==p
    N,K=140,180
    B=bernoulli(2*K+2)
    bp=[F(0)]*(2*K+1);bp[0],bp[1]=F(1),D
    for k in range(1,K+1):bp[2*k]=B[2*k]*(2*D)**(2*k)/factorial(2*k)
    A=[c/2 for c in mul(bp,[(-D/2)**k/factorial(k) for k in range(N+1)])]
    ce=F(23,10)*(D/2)**(N+1)/factorial(N+1)
    cb=4*(D/3)**(2*K+2)/(1-(D/3)**2)
    he=ce/(N+1)+cb/(2*K+2);ae=ce/(N+2)+cb/(2*K+3)
    H=[F(0)]+[-A[k]/k for k in range(1,len(A))]
    smooth=mul(p,add(H,exact_reflect(H)))
    left=[F(0)]*(len(p)+len(A)-1)
    for j,c in enumerate(p):
        for k,a in enumerate(A):left[j+k]+=c*a*regular_difference_factor(j,k)
    smooth=add(smooth,[-c for c in add(left,exact_reflect(left))])
    pi=16*atan(F(1,5),500)-4*atan(F(1,239),500)
    gamma=I(sum((F(1,k) for k in range(1,101)),F(0))-F(1,200))-log(F(100))
    gamma+=sum((B[2*k]/F(2*k*100**(2*k)) for k in range(1,57)),F(0))
    ge=abs(B[114])/F(114*100**114);gamma+=I(-ge,ge)
    constant=-gamma-log(F(2))-I(log(pi.lo).lo,log(pi.hi).hi)-log(D)
    ep=compose([(D/2)**k/factorial(k) for k in range(N+1)],F(-1,2))
    em=exact_reflect(ep)
    mp=D*sum((c/F(k+1) for k,c in enumerate(mul(p,ep))),F(0))
    core=[I(c)+constant*(p[k] if k<len(p) else 0) for k,c in enumerate(smooth)]
    core=add(core,[mp*(ep[k]+em[k]) for k in range(N+1)])
    ns=[2,3,4,5,7,8]
    amplitudes=[log(F(2))/sqrt_rational(F(2)),log(F(3))/sqrt_rational(F(3)),
                log(F(2))/2,log(F(5))/sqrt_rational(F(5)),
                log(F(7))/sqrt_rational(F(7)),log(F(2))/sqrt_rational(F(8))]
    geom=translation_panels(F(21,20),logarithm=log)
    shifts={(i,s):[-amplitudes[i]*c for c in compose(p,s*log(F(n))/D)] for i,n in enumerate(ns) for s in (1,-1)}
    panels=[];radius=F(0);grid=10**250
    for active in geom['active']:
        row=core[:]
        for i,s in active:row=add(row,shifts[i,s])
        mids=[];err=F(0)
        for x in row:
            x=x if isinstance(x,I) else I(x)
            mid=F((((x.lo+x.hi)/2)*grid).__floor__(),grid)
            mids.append(mid);err+=max(abs(x.lo-mid),abs(x.hi-mid))
        panels.append(mids);radius=max(radius,err)
    exp_error=2*(D/4)**(N+1)/factorial(N+1)
    uniform=2*M0*he+2*M1*ae+100*D*M0*exp_error+radius
    return panels,sqrt_rational(D).hi*uniform,pi,geom

def primitives(t,degree):
    powers=[I(1)]
    for _ in range(degree+1):powers.append(powers[-1]*t)
    lt=None if t.hi==0 else I(log(t.lo).lo,log(t.hi).hi)
    rev=I(1)-t
    lr=None if rev.hi==0 else I(log(rev.lo).lo,log(rev.hi).hi)
    h=I(0);lm=[]
    for k in range(degree+1):
        n=k+1;h+=powers[n]/n
        first=I(0) if lt is None else powers[n]*(lt/n-F(1,n*n))
        second=-h/n if lr is None else ((powers[n]-1)*lr-h)/n
        lm.append(-(first+second)/2)
    return powers,lm

def bracket(x):return [str(x.lo),str(x.hi)]
def display(x):return [float(x.lo),float(x.hi)]

def compute():
    witness_path=ROOT/'notes/data/RPB108_PRIME8_SCHUR112_105_CERTIFICATE_20261008.json'
    saved=json.loads(witness_path.read_bytes())
    native_path=ROOT/'notes/data/RPB108_PRIME8_MATRIX112_105_COMPACT80_20261008.json.gz'
    native_raw=gzip.decompress(native_path.read_bytes())
    assert hashlib.sha256(native_raw).hexdigest()==saved['input_sha256']['native']
    native=json.loads(native_raw)
    nativeQ=[[None]*112 for _ in range(112)];index=0
    for i in range(112):
        for j in range(i+1):
            lo,hi=native['lower_triangle_row_major'][index];index+=1
            nativeQ[i][j]=nativeQ[j][i]=I(F(int(lo),10**80),F(int(hi),10**80))
    v=list(map(F,saved['rational_coefficient_witness']))
    assert len(v)==112 and saved['physical_complement_lower']=='699/1000'
    P=shifted_legendre(112)
    norms=[sqrt_rational(F(2*j+1)/D) for j in range(113)]
    weights=[v[j]*(norms[j].lo+norms[j].hi)/2 if j%2==0 else F(0) for j in range(112)]
    ph=[sum((weights[j]*(P[j][k] if k<=j else 0) for j in range(112)),F(0)) for k in range(111)]
    # z is DEFINED with a rational scale: exact complement membership.
    nz=(norms[112].lo+norms[112].hi)/2;pz=[nz*c for c in P[112]]
    M0h=sum(map(abs,weights),F(0));M1h=sum((abs(weights[j])*j*(j+1) for j in range(112)),F(0))
    M0z=abs(nz);M1z=M0z*112*113
    print('source witness',file=sys.stderr,flush=True)
    rh,eh,pi,geom=source(ph,M0h,M1h)
    print('source trial',file=sys.stderr,flush=True)
    rz,ez,_,_=source(pz,M0z,M1z)
    # Normalization substitution error. Each physical basis source has norm
    # < 10^6 by the endpoint log, kernel-difference, prime and pole bounds;
    # hence the 112-source operator norm is < 2*10^7. See CC3 note.
    norm_error=2*F(10**7)*sum((abs(v[j])*sqrt_rational(D/F(2*j+1)).hi/(2*I.grid) for j in range(0,112,2)),F(0))
    eh+=norm_error
    assert eh<F(1,10**45) and ez<F(1,10**45)
    degree=max(max(len(r) for r in rh),max(len(r) for r in rz))*2-2
    prim=[primitives(t,degree) for t in geom['cuts']]
    hn=[I(0) for _ in range(113)];zn=[I(0) for _ in range(113)]
    hz=I(0);zz=I(0)
    h1=[];h2=[];harm=F(0);harm2=F(0)
    for k in range(225):
        n=k+1;harm+=F(1,n);harm2+=F(1,n*n)
        h1.append(I((F(1,n*n)+harm/n)/2))
        h2.append(I((F(2,n**3)+(harm*harm+harm2)/n+2*harm/n**2+2*harm2/n)/4)-pi*pi/(12*n))
    hz+=dot(mul(ph,pz),h2);zz+=dot(mul(pz,pz),h2)
    for panel,(a,b) in enumerate(zip(prim,prim[1:])):
        print('integrate panel',panel,file=sys.stderr,flush=True)
        m=[(b[0][k+1]-a[0][k+1])/(k+1) for k in range(degree+1)]
        lm=[b[1][k]-a[1][k] for k in range(degree+1)]
        m=[I(max(0,x.lo),x.hi) for x in m];lm=[I(max(0,x.lo),x.hi) for x in lm]
        for k in range(113):hn[k]+=dot(rh[panel],m[k:]);zn[k]+=dot(rz[panel],m[k:])
        hz+=dot(mul(rh[panel],rz[panel]),m)+dot(add(mul(ph,rz[panel]),mul(pz,rh[panel])),lm)
        zz+=dot(mul(rz[panel],rz[panel]),m)+2*dot(mul(pz,rz[panel]),lm)
    for k in range(113):hn[k]+=dot(ph,h1[k:]);zn[k]+=dot(pz,h1[k:])
    # Coarse actual source norm bounds, used only in tiny approximation budgets.
    Mh=F(10**8)*(1+M0h);Mz=F(10**8)*(1+M0z)
    hz=D*hz+I(-(eh*Mz+ez*Mh+eh*ez),eh*Mz+ez*Mh+eh*ez)
    zz=D*zz+I(-(2*ez*Mz+ez*ez),2*ez*Mz+ez*ez)
    b=D*nz*dot(P[112],hn);q=D*nz*dot(P[112],zn)
    zmass=D*nz*nz/225
    b+=I(-eh*sqrt_rational(zmass).hi,eh*sqrt_rational(zmass).hi)
    q+=I(-ez*sqrt_rational(zmass).hi,ez*sqrt_rational(zmass).hi)
    projections=[]
    for j in range(0,112,2):
        x=D*norms[j]*dot(P[j],hn)+I(-eh,eh)
        y=D*norms[j]*dot(P[j],zn)+I(-ez,ez)
        audit=sum((v[i]*nativeQ[j][i] for i in range(0,112,2)),I(0))
        assert max(x.lo,audit.lo)<=min(x.hi,audit.hi), ('native witness audit',j)
        hz-=x*y;zz-=y*y;projections.append(dict(degree=j,witness=bracket(x),trial=bracket(y)))
    symmetric_b=D*dot(ph,zn)
    symmetric_b+=I(-ez*sqrt_rational(F(saved['witness_mass_squared'])).hi,ez*sqrt_rational(F(saved['witness_mass_squared'])).hi)
    assert max(b.lo,symmetric_b.lo)<=min(b.hi,symmetric_b.hi)
    c=F(699,1000)
    linear=2*hz/c-2*b;quadratic=zz/c-q
    assert quadratic.lo>0
    tmid=(linear.lo+linear.hi)/(2*(quadratic.lo+quadratic.hi))
    scale=10**100;t=F((tmid*scale).__floor__(),scale)
    improvement=t*linear-t*t*quadratic
    baseline=I(*saved['corrected_witness_interval'])
    trial_lower=baseline+improvement
    result=dict(stage='CC3 one actual complement trial',aperture='21/20',trial_degree=112,
        trial_rational_normalization=str(nz),trial_mass_squared=str(zmass),coefficient=str(t),
        complement_lower=str(c),witness_source_error=str(eh),trial_source_error=str(ez),
        native_cross_pairing=bracket(b),trial_native_pairing=bracket(q),
        residual_source_cross=bracket(hz),trial_complement_source_norm_squared=bracket(zz),
        linear_improvement=bracket(linear),quadratic_cost=bracket(quadratic),
        improvement=bracket(improvement),baseline=bracket(baseline),trial_lower=bracket(trial_lower),
        displays={k:display(x) for k,x in [('b',b),('q',q),('v',hz),('w',zz),('linear',linear),('quadratic',quadratic),('improvement',improvement),('trial_lower',trial_lower)]},
        improvement_certified=improvement.lo>0,witness_direction_positive=trial_lower.lo>0,
        full_target_schur_certified=False,whole_domain_positivity=False,checkpoint_A=False,
        lean_formalized=False,odd_witness_handling='exact orthogonality to even trial; retained in baseline',
        integration_degree=degree,grid_digits=800,coefficient_grid_digits=250,log_terms=1000,
        exponential_order=140,bernoulli_pairs=180,gamma_order=56,
        projection_degrees=list(range(112)),even_projection_pairings=projections,
        witness_sha256=hashlib.sha256(witness_path.read_bytes()).hexdigest(),
        native_sha256=hashlib.sha256(native_raw).hexdigest(),native_witness_pairing_audits=56,
        symmetry_cross_pairing_audited=True,
        constructor_sha256=hashlib.sha256(Path(__file__).read_bytes()).hexdigest())
    return result

if __name__=='__main__':
    result=compute()
    destination=ROOT/'notes/data/RPB108_COUPLED_TRIAL_CC3_CERTIFICATE_20261008.json'
    destination.write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result['displays'],indent=2))
