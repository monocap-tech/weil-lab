"""RC30 directed Decimal enclosure of the actual eight-mode trial metric."""
from decimal import Decimal as D, Context, ROUND_FLOOR, ROUND_CEILING, ROUND_HALF_EVEN
from fractions import Fraction as F
import json
from validate_rpb108_rc29_atom_reduction import overlap, legendre, B, R

P=220
loctx=Context(prec=P,rounding=ROUND_FLOOR)
hictx=Context(prec=P,rounding=ROUND_CEILING)
near=Context(prec=P,rounding=ROUND_HALF_EVEN)

class I:
    def __init__(self,l,h=None):
        if isinstance(l,F):
            self.l=loctx.divide(D(l.numerator),D(l.denominator))
            self.h=hictx.divide(D(l.numerator),D(l.denominator))
        else: self.l,self.h=D(l),D(l if h is None else h)
    def __add__(a,b):
        b=iv(b); return I(loctx.add(a.l,b.l),hictx.add(a.h,b.h))
    __radd__=__add__
    def __neg__(a): return I(a.h.copy_negate(),a.l.copy_negate())
    def __sub__(a,b): return a+-iv(b)
    def __rsub__(a,b): return iv(b)+-a
    def __mul__(a,b):
        b=iv(b)
        return I(min(loctx.multiply(x,y) for x in (a.l,a.h) for y in (b.l,b.h)),
                 max(hictx.multiply(x,y) for x in (a.l,a.h) for y in (b.l,b.h)))
    __rmul__=__mul__
    def __truediv__(a,b):
        b=iv(b); assert not b.l<=0<=b.h
        return a*I(loctx.divide(D(1),b.h),hictx.divide(D(1),b.l))
    def __rtruediv__(a,b): return iv(b)/a
    def exp(a):
        return I(near.next_minus(near.exp(a.l)),near.next_plus(near.exp(a.h)))
    def log(a):
        assert a.l>0
        return I(near.next_minus(near.ln(a.l)),near.next_plus(near.ln(a.h)))
    def sqrt(a):
        assert a.l>=0
        return I(near.next_minus(near.sqrt(a.l)),near.next_plus(near.sqrt(a.h)))
    def pair(a): return [str(a.l),str(a.h)]

def iv(x): return x if isinstance(x,I) else I(x)
def atan_small(x):
    assert 0<=x.l<=x.h<D('0.21')
    z=x*x; term=x; total=I(0)
    for j in range(180):
        total=total+((-1)**j)*term/(2*j+1)
        term=term*z
    rem=(term/361).h
    return total+I(rem.copy_negate(),rem)

PI=16*atan_small(I(F(1,5)))-4*atan_small(I(F(1,239)))
def atan(x):
    if x.l>1: return PI/2-atan(1/x)
    # For a small interval straddling 1 the same half-angle formula is valid.
    y=x
    for _ in range(3): y=y/(1+(1+y*y).sqrt())
    return 8*atan_small(y)

def product(a,b):
    out=[F(0)]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b): out[i+j]+=x*y
    return out
def endpoint(i,j):
    p=product(legendre(i),legendre(j))
    return 2*B*sum((a*sum((F(1,2*q+1) for q in range(k//2+1)),F(0))/F(k+1)
                    for k,a in enumerate(p) if k%2==0),F(0))

def run():
    # Independently enclose known transcendental controls.
    assert PI.l>D('3.14159265358979323846264338327950288419716939937510')
    assert PI.h<D('3.14159265358979323846264338327950288419716939937511')
    e=I(1).exp(); c=2*PI
    h=I(10)*I(10).log()/1000
    start=-5*I(10).log()
    rows={(i,j):overlap(i,j) for i in range(8) for j in range(i,8) if (i+j)%2==0}
    Q={key:I(0) for key in rows}
    for j in range(1000):
        t=(start+(I(j)+I(F(1,2)))*h).exp()
        tt=t*t; cc=c*c
        moments=[atan(c*I(R)/t)/(c*t), (1+(c*I(R)/t)*(c*I(R)/t)).log()/(2*cc)]
        for p in range(2,16):
            moments.append(I(R**(p-1))/(cc*(p-1))-(tt/cc)*moments[p-2])
        weight=h*t*(1-(-e*t).exp())
        for key,poly in rows.items():
            atom=2*sum((I(a)*moments[p] for p,a in enumerate(poly)),I(0))
            Q[key]=Q[key]+weight*atom
    maxwidth=max(hictx.subtract(q.h,q.l) for q in Q.values())
    assert maxwidth<D('1e-30'), maxwidth
    # Rational outward entry endpoints retain 20 decimal places.
    den=D(10)**20
    Qhat=[[F(0) for _ in range(8)] for _ in range(8)]
    entry=[]
    for (i,j),q in Q.items():
        l=int(loctx.multiply(q.l,den).to_integral_value(rounding=ROUND_FLOOR))
        u=int(hictx.multiply(q.h,den).to_integral_value(rounding=ROUND_CEILING))
        Qhat[i][j]=Qhat[j][i]=F(l+u,2*10**20)
        entry.append(dict(i=i,j=j,lower=str(F(l,10**20)),upper=str(F(u,10**20))))
    # A row sum normalized by sqrt(D_i D_j), bounded using minimum mass.
    entry_error=max(F(x['upper'])-F(x['lower']) for x in entry)/2
    eta=8*entry_error/F(11,75)
    assert eta<F(1,10**15)
    scalar=F(-3203794213-3203306050,2*10**9)
    scalar_error=F(488163,2*10**9)
    G=[]
    mass=[2*B/F(2*i+1) for i in range(8)]
    for i in range(8):
        row=[]
        for j in range(8):
            v=endpoint(i,j)+Qhat[i][j]
            if i==j: v+=(sum((F(1,k) for k in range(1,i+1)),F(0))+scalar)*mass[i]
            row.append(v)
        G.append(row)
    total=F(109,500000)+eta+scalar_error
    # G_true>=D is inherited from its actual Fourier weight; this does not
    # imply original Weil Q positivity.
    assert total<F(1,2000)
    return dict(milestone='RC30',status='PASS',precision=P,atoms=1000,
                evaluated_upper_triangle_nonzero_parity_entries=len(entry),
                mixture_entry_intervals=entry,
                metric_center=[[str(x) for x in row] for row in G],
                physical_mass=[str(x) for x in mass],
                mass_metric_error_upper=str(total),entry_error_transport=str(eta),
                metric_diagonal_centers=[float(G[i][i]) for i in range(8)],
                complete_physical_trial_metric_enclosed=True,
                Riesz_solve=False,whole_weak_residuals=False,
                native_head_certified=False,aperture_extended=False)

if __name__=='__main__': print(json.dumps(run(),indent=2))
