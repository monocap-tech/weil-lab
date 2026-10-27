"""Complete original scalar physical form via grouped exponential correlation.

Same analytic construction as accepted #347; no numerical quadrature input.
Native enclosure and independent domain-review standing remain separate.
"""
from fractions import Fraction as F
from flint import arb,acb,ctx
B=F(11,10)
def dy(x):
    n,e=x.man_exp();return [str(n),int(e)]
def rat(v):return F(int(v[0]))*F(2)**int(v[1])
def ball(v):return [dy(v.mid()),dy(v.rad())]
def bounds(v,D):
    l=rat(dy(v.lower()))*D;h=rat(dy(v.upper()))*D
    return F(l.numerator//l.denominator,D),F(-(-h.numerator//h.denominator),D)
def physical_form(a,b):
    ctx.prec=512
    pi=arb.pi();bb=arb(str(B));L=2*bb;I=acb(0,1)
    rates=[];co=[]
    for n,c in enumerate(a,1):
        nu=2*pi*arb(str(F(5*n,11)));rates.extend([acb(0,nu),acb(0,-nu)]);co.extend([acb(0,-arb(str(c))/2),acb(0,arb(str(c))/2)])
    rates.extend([acb('1/2'),acb('-1/2')]);co.extend([acb(arb(str(b))/2),acb(-arb(str(b))/2)])
    size=len(rates);d=[acb(0) for _ in rates];t=[acb(0) for _ in rates]
    # Group the exact translated correlation into O(size) exponentials.
    for j in range(size):
        for k in range(size):
            c=co[j]*co[k]
            if k==(j^1):d[k]+=L*c;t[k]-=c
            else:
                rho=rates[j]+rates[k]
                d[j^1]+=c*(rho*bb).exp()/rho;d[k]-=c*(-rho*bb).exp()/rho
    norm=sum(d,acb(0))
    def overlap(s):return sum(((d[j]+t[j]*s)*(rates[j]*s).exp() for j in range(size)),acb(0))
    def exprel(z):return (z/2).exp()*(I*z/2).sinc()
    def D(s):return -sum((d[j]*rates[j]*exprel(rates[j]*s)+t[j]*(rates[j]*s).exp() for j in range(size)),acb(0))
    endpoint=sum((co[j]*(rates[j]*bb).exp() for j in range(size)),acb(0))
    assert (D(acb(0))-endpoint*endpoint).contains(0)
    # Independent norm/pole formulas use sine orthogonality and explicit overlaps.
    pp=bb.sinh()-bb;sp=[]
    for n in range(1,33):
        nu=2*pi*arb(str(F(5*n,11)))
        sp.append(-2*nu*(bb/2).sinh()*((-1)**n)/(arb('1/4')+nu**2))
    pole=sum((arb(str(c))*s for c,s in zip(a,sp)),arb(0))+arb(str(b))*pp
    norm2=bb*sum((arb(str(c))**2 for c in a),arb(0))+2*arb(str(b))*sum((arb(str(c))*s for c,s in zip(a,sp)),arb(0))+arb(str(b))**2*pp
    assert (norm.real-norm2).contains(0) and norm.imag.contains(0)
    def direct_overlap(s):
        out=acb(0)
        for j in range(size):
            for k in range(size):
                c=co[j]*co[k];rho=rates[j]+rates[k]
                out+=c*((L-s)*(rates[k]*s).exp() if k==(j^1) else ((rho*bb-rates[j]*s).exp()-(-rho*bb+rates[k]*s).exp())/rho)
        return out
    for s in [acb(0),acb('1/7'),acb(L)]:
        assert (overlap(s)-direct_overlap(s)).contains(0)
        if s!=0:assert (D(s)-(norm-overlap(s))/s).contains(0)
    integ=acb.integral(lambda s,_:(s/2).exp()/(I*s).sinc()*D(s),0,L,rel_tol=arb(2)**-160,abs_tol=arb(2)**-160,eval_limit=100000,depth_limit=24)
    assert integ.is_finite() and integ.imag.contains(0)
    tail=arb(0)
    for n in range(64):
        lam=arb(2*n)+arb('1/2');tail+=2*(-lam*L).exp()/lam
    rem=2*(-arb('257/2')*L).exp()/(arb('257/2')*(1-(-2*L).exp()));tail+=arb(0,rem.upper())
    c0=-arb.const_euler()-pi/2-3*arb(2).log()-pi.log();assert (c0-(acb('1/4').digamma().real-pi.log())).contains(0)
    prime=acb(0)
    for n,pn in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]:
        s=arb(n).log();v=overlap(acb(s));assert (v-direct_overlap(acb(s))).contains(0)
        prime-=2*arb(pn).log()/arb(n).sqrt()*v
    Q=(c0+tail)*norm+integ+prime-2*pole*pole
    assert Q.is_finite() and Q.imag.contains(0)
    qlo,qhi=bounds(Q.real,10**40);nlo,nhi=bounds(norm.real,10**40)
    return dict(native_balls={k:ball(v.real if isinstance(v,acb) else v) for k,v in dict(norm=norm,arch_constant=c0,arch_integral=integ,arch_tail=tail,prime=prime,pole=pole,signed=Q).items()},physical_norm_interval=list(map(str,[nlo,nhi])),signed_energy_interval=list(map(str,[qlo,qhi])))
