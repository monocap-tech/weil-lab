#!/usr/bin/env python3
"""Complete original prime-translation J470-to-normalized-SI29 mixed block.

Only the seven-prime component is computed. No archimedean mixed block,
complete Astar forcing, energy projection, or signed positivity is asserted.
"""
import argparse,gc,hashlib,json,time
from fractions import Fraction as F
from math import comb,factorial
from pathlib import Path
from flint import arb,acb,arb_mat,ctx
import verify_rpb108_si29_full_J_L2_normalization as m
from validate_rpb108_si06_negative_band import ACTIVE

SHA='c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60'
def dy(x):return arb((int(x[0]),int(x[1])))
def ball(x):return arb(dy(x[0]),dy(x[1]))
def rat(x):
    n,e=int(x[0]),int(x[1]);return F(n*2**max(e,0),2**max(-e,0))

class Clipped:
    def __init__(self,shift):
        self.pi=arb.pi();self.b=m.a(m.B);self.shift=shift
        self.right=self.b-shift;assert self.right> -self.b and not self.right.contains(0)
        self.tables={};self.negative={}
    def w(self,f):return acb(2*self.pi*m.a(f[0]),m.a(f[1]))
    def primitives(self,p,kind,f,x,which):
        if f==(0,0):
            return acb(x**(p+1)/(p+1)) if p>=0 and kind=='c' else acb(0)
        key=(f,which);w=self.w(f)
        if key not in self.tables:
            sn,co=(w*x).sin_cos()
            self.tables[key]=(sn,co,[(sn/w,(1-co)/w)])
        sn,co,tab=self.tables[key]
        if p>=0:
            while len(tab)<=p:
                n=len(tab);cp,sp=tab[-1]
                tab.append((x**n*sn/w-n*sp/w,-x**n*co/w+n*cp/w))
            return tab[p][0 if kind=='c' else 1]
        assert p in (-1,-2)
        if key not in self.negative:
            # H(t)=Ci(t)-log(t)-EulerGamma is ENTIRE and EVEN. Choose
            # x>=0 to avoid a negative-real branch cut in individual terms.
            t=w*abs(x);H=t.ci()-t.log()-arb.const_euler()
            si=(w*x).si()
            self.negative[key]={(-1,'s'):si,(-1,'c'):H,
              (-2,'c'):(1-co)/x-w*si,
              (-2,'s'):(w*x-sn)/x+w*H}
        return self.negative[key][p,kind]
    def get(self,p,kind,f):
        f,sign=m.canonical(f,kind)
        # Primitive parity: cos moment p+1, sin moment p.
        parity=(-1)**(p+1 if kind=='c' else p)
        return sign*(self.primitives(p,kind,f,self.right,'right')-
                     parity*self.primitives(p,kind,f,self.b,'B'))

def shifted(terms,kernel):
    out=[]
    for p,t,f,c in terms:
        assert p>=0
        sn,co=(kernel.w(f)*kernel.shift).sin_cos()
        for q in range(p+1):
            v=c*comb(p,q)*kernel.shift**(p-q)
            out.append((q,t,f,v*co))
            out.append((q,'c' if t=='s' else 's',f,v*sn*(1 if t=='s' else -1)))
    return out

def clipped_gram(x,y,kernel):
    v=acb(0)
    for p,t,f,c in x:
        for q,s,g,d in y:
            plus=m.addfreq(f,g);minus=m.subfreq(f,g);power=p+q
            if t==s=='s':z=kernel.get(power,'c',minus)-kernel.get(power,'c',plus)
            elif t==s=='c':z=kernel.get(power,'c',minus)+kernel.get(power,'c',plus)
            elif t=='s':z=kernel.get(power,'s',plus)+kernel.get(power,'s',minus)
            else:z=kernel.get(power,'s',plus)-kernel.get(power,'s',minus)
            v+=c*d*z/2
    assert v.imag.contains(0)
    return v.real

def primitive_series_check(kernel):
    # Independent entire-power integration, including BOTH formerly
    # parity-forbidden Ci primitives and all asymmetric endpoint signs.
    K=255;f=(F(1,4),F(1,2));w=kernel.w(f);b=kernel.b;r=kernel.right
    t=F(11,10)*(F(11,7)+F(1,2))
    for p in (-2,-1,0,1,5,15):
        for kind in ('s','c'):
            s=acb(0)
            for k in range(1 if kind=='s' else 0,K+1,2):
                if p+k<0:continue
                s+=(-1)**(k//2)*w**k/factorial(k)*(r**(p+k+1)-(-b)**(p+k+1))/(p+k+1)
            fee=m.a(2*m.B**(p+1)*t**(K+1)/factorial(K+1)/(1-t/F(K+2)))
            assert abs(kernel.get(p,kind,f)-s)<fee,('primitive series',p,kind)
    return True

def evaluate(terms,x,kernel):
    v=acb(0)
    for p,t,f,c in terms:
        w=kernel.w(f)*x
        v+=c*x**p*(w.sin() if t=='s' else w.cos())
    return v

def translation_checks(terms,kernel):
    x=-kernel.shift/2
    for i in (0,14,468,469):
        v=evaluate(shifted(terms[i],kernel),x,kernel)
        exact=evaluate(terms[i],x+kernel.shift,kernel)
        assert abs(v-exact)<arb('1e-1000'),('translation identity',i)
    # Reflection of the clipped interval proves symmetry for odd functions.
    # Independently check Laurent features against all first-node generators.
    for i in (0,14,469):
        for j in (0,14,469):
            a=clipped_gram(terms[i],shifted(terms[j],kernel),kernel)
            b=clipped_gram(terms[j],shifted(terms[i],kernel),kernel)
            assert abs(a-b)<arb('1e-1000'),('clipped odd symmetry',i,j)
    return True

def feature_series_check(features,terms,kernel):
    # Independent entire Taylor integrals of ALL actual features against
    # translated original sine and pole on the WHOLE clipped interval.
    K=255;odds=list(range(1,K+1,2));U=arb_mat(128,14);errors=[]
    for j,f in enumerate(features):
        c,r,d=f;mu=m.band_moments(f,K)
        for i,n in enumerate(odds):U[i,j]=(-1)**((n-1)//2)*m.a(mu[n])*(2*kernel.pi*kernel.b)**n/factorial(n)
        t=F(44,7)*m.B*(c+r)
        errors.append(m.a((F(3,2) if d else 1)*t**(K+1)/factorial(K+1)))
    V=arb_mat(K+1,2);source_errors=[]
    for j,index in enumerate((0,469)):
        power,kind,f,c=terms[index][0];assert power==0 and kind=='s'
        w=kernel.w(f);sn,co=(w*kernel.shift).sin_cos()
        for n in range(K+1):
            value=c*(sn if n%2==0 else co)*(-1)**(n//2)*(w*kernel.b)**n/factorial(n)
            assert value.imag.contains(0);V[n,j]=value.real
        t=F(44,7)*m.B*f[0] if index==0 else m.B/2
        source_errors.append(m.a((1 if index==0 else 6)*t**(K+1)/factorial(K+1)))
    assert ((kernel.shift+kernel.b)/2).exp()<6
    ratio=kernel.right/kernel.b;powers=[arb(1)]
    for n in range(2*K+1):powers.append(powers[-1]*ratio)
    moments=arb_mat([[kernel.b*(powers[n+k+1]-(-1)**(n+k+1))/(n+k+1) for k in range(K+1)] for n in odds])
    poly=U.transpose()*moments*V
    width=2*kernel.b-kernel.shift
    for i,f in enumerate(features):
        amp=m.a(F(3,2) if f[2] else F(1))
        for j,index in enumerate((0,469)):
            fee=width*(errors[i]+amp*source_errors[j]+errors[i]*source_errors[j])
            exact=clipped_gram(terms[470+i],shifted(terms[index],kernel),kernel)
            assert abs(exact-poly[i,j])<fee,('continuous feature clipped Taylor',i,index)
    return True

def main():
    p=argparse.ArgumentParser();p.add_argument('--certificate',required=True)
    p.add_argument('--output',default='artifacts/si29_original_prime_mixed.json')
    p.add_argument('--self-test',action='store_true');p.add_argument('--prime-limit',type=int,default=7)
    args=p.parse_args();raw=Path(args.certificate).read_bytes();assert hashlib.sha256(raw).hexdigest()==SHA
    z=json.loads(raw);ctx.prec=z['working_precision_bits'];assert ctx.prec==4096 and m.flint.__version__=='0.8.0'
    nodes=[(F(c),p) for c,p in z['original_source_nodes']];features=[(F(c),F(r),d) for c,r,d in z['feature_definitions']]
    assert sum(p for c,p in nodes)==469 and len(features)==14
    terms=[m.source_terms(c,k) for c,p in nodes for k in range(p)]+[m.pole_terms()]+[m.feature_terms(f) for f in features]
    X=arb_mat([[ball(v) for v in row] for row in z['full_physical_projection_coefficient_balls']])
    C=arb_mat([[dy(v) for v in row] for row in z['exact_dyadic_feature_transform']])
    Q=arb_mat([[-X[i,j] for j in range(14)] for i in range(470)]+[[arb(int(i==j)) for j in range(14)] for i in range(14)])*C
    primes=list(ACTIVE.items());assert primes==[(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)]
    total=arb_mat(470,14);witnesses=[];start=time.monotonic()
    for n,prime in primes[:args.prime_limit]:
        shift=arb(n).log();kernel=Clipped(shift)
        assert shift>0 and shift<2*kernel.b
        primitive_series_check(kernel);translation_checks(terms,kernel)
        feature_series_check(features,terms,kernel)
        print('Clipped primitive/translation checks',n,'PASS',flush=True)
        if args.self_test:continue
        translated=[shifted(t,kernel) for t in terms[:470]]
        A=arb_mat(470,484)
        for i in range(470):
            for j in range(i,470):
                # Exact odd reflection makes the original J/J block symmetric.
                A[i,j]=A[j,i]=clipped_gram(terms[j],translated[i],kernel)
            for j in range(470,484):A[i,j]=clipped_gram(terms[j],translated[i],kernel)
            if i%100==0:print('Prime',n,'mixed raw row',i,'seconds',round(time.monotonic()-start,1),flush=True)
        weight=arb(prime).log()/arb(n).sqrt()
        mixed=(-2*weight)*(A*Q);total+=mixed
        maxrad=max((abs(mixed[i,j].rad()) for i in range(470) for j in range(14)),default=arb(0))
        assert maxrad<arb('1e-100'),('unresolved mixed enclosure',n,maxrad.str(10))
        witnesses.append(dict(n=n,prime_base=prime,shift_ball=m.ball(shift),coefficient_ball=m.ball(weight),maximum_entry_radius=m.ball(maxrad)))
        print('Complete original prime mixed block',n,'PASS; radius',maxrad.str(5),'seconds',round(time.monotonic()-start,1),flush=True)
        del A,kernel,translated,mixed;gc.collect()
    if args.self_test:
        print('ALL ORIGINAL CLIPPED-TRANSLATION SELF CHECKS PASS');return
    complete=args.prime_limit==7
    radius2=sum((rat(m.dyadic(total[i,j].rad()))**2 for i in range(470) for j in range(14)),F(0))
    assert 0<radius2<F(1,10**180)
    epsilon=F(1)
    while epsilon**2/4>=radius2:epsilon/=2
    assert radius2<=epsilon**2 and epsilon<F(1,10**90)
    result=dict(status='COMPLETE_ORIGINAL_SEVEN_PRIME_J470_W14_MIXED_BLOCK' if complete else 'DIAGNOSTIC_PARTIAL_PRIME_BLOCK',
      native_input_sha256=SHA,working_precision_bits=4096,original_J_count=470,actual_feature_count=14,
      physical_trial='W=(I-P_J470)FC, unaligned, same accepted exact C',
      prime_multiplier='-2 sum_(n,p) log(p)/sqrt(n) cos(2*pi*xi*log(n))',
      physical_identity='Jstar Pprime W = -2 sum log(p)/sqrt(n) integral_(-B)^(B-log(n)) W(x) J(x+log(n)) dx',
      prime_count=len(witnesses),prime_witnesses=witnesses,mixed_block_balls=m.balls(total),
      independent_entire_primitive_series_degree=255,translation_and_odd_reflection_checks=True,
      independent_all_continuous_feature_clipped_Taylor_degree=255,
      exact_Frobenius_entry_radius_squared=str(radius2),coupled_mixed_midpoint_operator_error_upper=str(epsilon),
      archimedean_mixed_computed=False,negative_multiplier_mixed_computed=False,
      complete_Astar_mixed_computed=False,energy_projection_computed=False,matched_forcing_computed=False,
      inverse_response_value_certified=False,W_ODD_NEG='OPEN',inherited_original_domain_review='OPEN',elapsed_seconds=time.monotonic()-start)
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True);out.write_text(json.dumps(result,indent=2)+'\n')
    print('ORIGINAL PRIME MIXED BLOCK',len(witnesses),'of 7; full Astar mixed OPEN',flush=True)
if __name__=='__main__':main()
