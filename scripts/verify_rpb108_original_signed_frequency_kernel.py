"""Native analytic COMPLETE original sine kernel and local frequency jets.

No arch quadrature or global monomial expansion. Complex-bilinear analytic
continuation is used internally; real physical combinations give the form.
"""
from math import factorial
from fractions import Fraction as F
from flint import arb,acb,acb_series,ctx

class Kernel:
    def __init__(self):
        ctx.prec=512;self.pi=arb.pi();self.I=acb(0,1);self.B=acb('11/10');self.L=2*self.B
        self.pole=acb(0,'1/2');self.pp=arb('11/10').sinh()-arb('11/10')
        # Cauchy radius 1/4, imaginary-frequency strip <=3/4.
        tail=(2*(-arb('511/4')*arb('11/5')).exp()/(arb('511/4')*(1-(-arb('22/5')).exp()))).upper()
        self.tail=arb(2)**-406
        assert tail<self.tail  # clean rational majorant, independently replayed
        self.exps=[(-acb(str(2*j+F(1,2)))*self.L).exp() for j in range(1,64)]
        self.primes=[(arb(p).log()/arb(n).sqrt(),arb(n).log()) for n,p in [(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]]
    def sin(self,z):return ((self.I*z).exp()-(-self.I*z).exp())/(2*self.I)
    def cos(self,z):return ((self.I*z).exp()+(-self.I*z).exp())/2
    def exprel(self,z):
        if z[0]==0:
            out=acb_series([1]);power=acb_series([1])
            for j in range(1,ctx.cap):power*=z;out+=power/factorial(j+1)
            return out
        return (z.exp()-1)/z
    def functions(self,v0,n):
        ctx.cap=n;v=acb_series([v0,1]);I=self.I;L=self.L
        zp=acb('5/4')+I*v0/2;zm=acb('5/4')-I*v0/2
        sp=acb_series([zp.digamma()]+[zp.polygamma(k)*(I/2)**k/factorial(k) for k in range(1,n)])
        sm=acb_series([zm.digamma()]+[zm.polygamma(k)*(-I/2)**k/factorial(k) for k in range(1,n)])
        ep=self.exprel((-acb('1/2')+I*v)*L);em=self.exprel((-acb('1/2')-I*v)*L)
        e0=(-self.B).exp()
        Jhead=2*L*((e0-1)/(-self.B)-(ep+em)/2)
        Is=L/I*(ep-em)+(sp-sm)/(2*I)
        As=(sp+sm)/2-self.pi.log()-4+4*e0+Jhead
        cv,sv=self.cos(v*L),self.sin(v*L)
        for j,ex in enumerate(self.exps,1):
            alpha=acb(str(2*j+F(1,2)));den=alpha*alpha+v*v
            As+=2*ex*(alpha*cv-v*sv)/den
            Is-=2*ex*(alpha*sv+v*cv)/den
        # Every omitted tail coefficient is bounded by M/(1/4)^k.
        for k in range(n):
            err=arb(0,self.tail*4**k);ball=acb(err,err)
            As[k]=As[k]+ball;Is[k]=Is[k]+ball
        return v,As,Is
    def point(self,v0):
        v,A,I=self.functions(v0,1);return A[0],I[0]
    def gram(self,v,mu):
        return self.sin((v-mu)*self.B)/(v-mu)-self.sin((v+mu)*self.B)/(v+mu)
    def pole_overlap(self,v,pole=False):
        if pole:return self.I*self.pp
        return 2*(acb('1/2')*(self.B/2).cosh()*self.sin(v*self.B)-v*(self.B/2).sinh()*self.cos(v*self.B))/(acb('1/4')+v*v)
    def correlation(self,v,mu,s):
        length=self.L-s
        return self.sin((v-mu)*length/2)/(v-mu)*self.cos((v+mu)*s/2)-self.sin((v+mu)*length/2)/(v+mu)*self.cos((v-mu)*s/2)
    def mixed(self,v,Av,Iv,mu,Am,Im,source_pole=False):
        ctx.cap=v.prec
        G=self.gram(v,mu)
        arch=G*(Av+Am)/2-(self.cos((v-mu)*self.B)*(Im-Iv)/(v-mu)+self.cos((v+mu)*self.B)*(Iv+Im)/(v+mu))/2
        prime=acb_series([0])
        for weight,s in self.primes:prime-=2*weight*self.correlation(v,mu,s)
        pole=-2*self.pole_overlap(v,source_pole)*self.pole_overlap(mu,mu==self.pole)
        return arch,prime,pole
    def diagonal(self,v0):
        v,A,I=self.functions(v0,2);ctx.cap=1
        G=self.B-self.sin(2*v0*self.B)/(2*v0)
        arch=G*A[0]+I[1]/2-self.cos(2*v0*self.B)*I[0]/(2*v0)
        prime=acb(0)
        for weight,s in self.primes:
            C=(self.B-s/2)*self.cos(v0*s)-self.sin(2*v0*self.B-v0*s)/(2*v0)
            prime-=2*weight*C
        pole=-2*self.pole_overlap(v0,v0==self.pole)**2
        return arch,prime,pole
