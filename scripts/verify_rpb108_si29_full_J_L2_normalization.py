#!/usr/bin/env python3
"""Certified physical full-J470 projection and L2 normalization of actual SI29.

Closed-form trigonometric/Laurent integrals, evaluated in Arb balls. No
Astar matrix entries or inverse-response values are computed here.
"""
import argparse, hashlib, json, time, traceback
from fractions import Fraction as F
from functools import lru_cache
from math import factorial
from pathlib import Path

import flint
from flint import arb, acb, arb_mat, ctx
from validate_rpb108_si10_complement_positivity import protected_inner_cover
from validate_rpb108_si08_multiband_rank import taylor_order
from validate_rpb108_si29_pole_threshold_three_bands import FEATURES
from validate_rpb108_sm17_compact_spectral_gate import KAPPA_STAR
from verify_rpb108_si29_normalized_residual_coordinates import band_moments

B=F(11,10)
def a(x): return arb(str(x))
def ac(x): return acb(a(x))
def addfreq(x,y): return (x[0]+y[0],x[1]+y[1])
def subfreq(x,y): return (x[0]-y[0],x[1]-y[1])
def canonical(freq,kind):
    if freq[0]<0 or (freq[0]==0 and freq[1]<0):
        return (-freq[0],-freq[1]), (-1 if kind=='s' else 1)
    return freq,1

class Integrals:
    def __init__(self):
        self.pi=arb.pi(); self.b=a(B); self.tables={}; self.neg={}
    def w(self,f): return acb(2*self.pi*a(f[0]),a(f[1]))
    def get(self,p,kind,f):
        f,sign=canonical(f,kind)
        return sign*self._get(p,kind,f)
    def _get(self,p,kind,f):
        assert (p%2==0 and kind=='c') or (p%2!=0 and kind=='s')
        if f==(0,0):
            return acb(self.b**(p+1)/(p+1)) if p>=0 and kind=='c' else acb(0)
        w=self.w(f); b=self.b
        if f not in self.tables:
            sn,co=(w*b).sin_cos()
            self.tables[f]=(w,sn,co,[(sn/w,(1-co)/w)])
        w,sn,co,tab=self.tables[f]
        if p>=0:
            while len(tab)<=p:
                n=len(tab); cp,sp=tab[-1]
                tab.append((b**n*sn/w-n*sp/w,-b**n*co/w+n*cp/w))
            return tab[p][0 if kind=='c' else 1]
        if f not in self.neg:
            si=(w*b).si()
            c2=(1-co)/b-w*si
            s3=(w*b-sn)/(2*b*b)+w*c2/2
            c4=(1-co-w*w*b*b/2)/(3*b**3)-w*s3/3
            self.neg[f]={-1:si,-2:c2,-3:s3,-4:c4}
        assert -4<=p<=-1
        return self.neg[f][p]

def source_terms(c,k):
    return [(k,'s' if k%2==0 else 'c',(c,F(0)),ac(1))]
def pole_terms():
    # sinh(x/2) = -i sin(i*x/2).
    return [(0,'s',(F(0),F(1,2)),acb(0,-1))]
def feature_terms(feature):
    c,r,d=feature; R=2*arb.pi()*a(r)
    plus=(c+r,F(0)); minus=(c-r,F(0))
    if d==0:
        return [(-1,'c',minus,acb(1/(2*R))),(-1,'c',plus,acb(-1/(2*R)))]
    assert d==1
    return [(-2,'s',plus,acb(3/(2*R*R))),(-2,'s',minus,acb(-3/(2*R*R))),
            (-1,'c',plus,acb(-3/(2*R))),(-1,'c',minus,acb(-3/(2*R)))]

def gram(x,y,kernel):
    value=acb(0)
    for p,kind,f,c in x:
        for q,other,g,d in y:
            power=p+q; plus=addfreq(f,g); minus=subfreq(f,g)
            if kind==other=='s':
                z=kernel.get(power,'c',minus)-kernel.get(power,'c',plus)
            elif kind==other=='c':
                z=kernel.get(power,'c',minus)+kernel.get(power,'c',plus)
            elif kind=='s':
                z=kernel.get(power,'s',plus)+kernel.get(power,'s',minus)
            else:
                z=kernel.get(power,'s',plus)-kernel.get(power,'s',minus)
            value+=c*d*z  # product-to-sum /2 cancels reflected physical interval factor 2
    assert value.imag.contains(0)
    return value.real

def dyadic(x):
    m,e=x.man_exp();return [str(m),int(e)]
def ball(x): return [dyadic(x.mid()),dyadic(x.rad())]
def balls(m): return [[ball(m[i,j]) for j in range(m.ncols())] for i in range(m.nrows())]

def independent_series_check(nodes,features,kernel):
    # Entire Taylor polynomials at x=B*t; integrate their exact moment
    # matrix on [-1,1]. This is independent of the Laurent/Si formulas.
    K=255; powers=list(range(1,K+1,2)); n=len(powers)
    c,p=nodes[0]
    descriptions=[('j',(c,k)) for k in range(p)]+[('pole',None)]+[('f',f) for f in features]
    terms=[source_terms(*arg) if kind=='j' else pole_terms() if kind=='pole'
           else feature_terms(arg) for kind,arg in descriptions]
    V=arb_mat(n,len(terms)); amps=[]; errors=[]
    pi=arb.pi(); bb=a(B)
    for j,(kind,arg) in enumerate(descriptions):
        if kind=='f':
            c,r,d=arg; mu=band_moments(arg,K)
            for i,k in enumerate(powers):
                V[i,j]=((-1)**((k-1)//2))*a(mu[k])*(2*pi*bb)**k/factorial(k)
            t=F(44,7)*B*(c+r)
            errors.append(a((F(3,2) if d else 1)*t**(K+1)/factorial(K+1)))
            amps.append(a(F(3,2) if d else 1))
        elif kind=='pole':
            for i,k in enumerate(powers):V[i,j]=(bb/2)**k/factorial(k)
            t=B/2
            errors.append(a(t**(K+1)/factorial(K+1)/(1-t/F(K+2))))
            amps.append(arb(1))
        else:
            c,k=arg
            for i,total in enumerate(powers):
                degree=total-k
                if degree>=0:
                    assert degree%2==1-k%2
                    sign=(-1)**((degree-(1-k%2))//2)
                    V[i,j]=sign*(2*pi*a(c))**degree*bb**total/factorial(degree)
            t=F(44,7)*B*c; degree=K-k
            errors.append(a(B**k*t**(degree+1)/factorial(degree+1)))
            amps.append(a(B**k))
    H=arb_mat([[2*bb/(i+j+1) for j in powers] for i in powers])
    poly=V.transpose()*H*V
    for i in range(len(terms)):
        for j in range(i+1):
            exact=gram(terms[i],terms[j],kernel)
            payment=2*bb*(errors[i]*amps[j]+errors[j]*amps[i]+errors[i]*errors[j])
            assert abs(exact-poly[i,j])<payment, ('independent series',i,j)
    pole=gram(pole_terms(),pole_terms(),kernel)
    assert (pole-(bb.sinh()-bb)).contains(0)
    return dict(entire_Taylor_degree=K,original_J_generators_checked=p,
                original_pole_checked=True,all_actual_SI29_features_checked=14,
                independent_full_comparison_dimension=len(terms),
                rigorous_Taylor_product_tail_payments_verified=True)

def normalize(S):
    # Construct a candidate from the midpoint only. Factoring and then
    # inverting interval Cholesky factors loses correlations severely.
    # The certificate is the final check against the ORIGINAL ball S.
    S0=S.mid()
    n=S.nrows(); L=arb_mat(n,n)
    for i in range(n):
        for j in range(i+1):
            x=S0[i,j]-sum((L[i,k]*L[j,k] for k in range(j)),arb(0))
            if i==j:
                assert x>0, ('unresolved midpoint candidate pivot',i,x.str(15))
                L[i,j]=x.sqrt()
            else:L[i,j]=x/L[j,j]
    I=arb_mat([[int(i==j) for j in range(n)] for i in range(n)])
    R=L.transpose().solve(I,algorithm='lu')
    # A fixed exact dyadic transformation, not an uncertain interval basis.
    C=arb_mat([[R[i,j].mid() for j in range(n)] for i in range(n)])
    N=C.transpose()*S*C
    rows=[]
    for i in range(n):
        err=sum((abs(N[i,j]-int(i==j)).abs_upper() for j in range(n)),arb(0))
        assert err<arb('1/100'), ('normalization row',i,err.str(15))
        rows.append(ball(err))
    return C,N,rows

def run(args):
    ctx.prec=args.bits
    start=time.monotonic(); progress={'phase':'original_geometry','bits':args.bits}
    out=Path(args.output);out.parent.mkdir(parents=True,exist_ok=True)
    def record(phase):
        progress['phase']=phase;progress['elapsed_seconds']=time.monotonic()-start
        out.with_suffix('.progress.json').write_text(json.dumps(progress,indent=2)+'\n')
        print(phase,round(progress['elapsed_seconds'],2),flush=True)
    try:
        clusters,_,_,leaves,_=protected_inner_cover()
        nodes=[((l+r)/2,taylor_order(r-l,9)[0]) for l,r,_ in clusters]
        features=tuple((c,r,d) for c,r,delta,d in FEATURES)
        assert len(nodes)==107 and leaves==973 and sum(p for c,p in nodes)==469
        assert len(features)==14 and KAPPA_STAR==F(33621,10**9)
        J=[source_terms(c,k) for c,p in nodes for k in range(p)]+[pole_terms()]
        Fs=[feature_terms(f) for f in features]
        assert len(J)==470
        kernel=Integrals();record('independent_entire_series_check')
        checks=independent_series_check(nodes,features,kernel)
        record('full_original_J470_physical_Gram')
        H=arb_mat(470,470)
        for i in range(470):
            for j in range(i+1):H[i,j]=H[j,i]=gram(J[i],J[j],kernel)
            if i%100==0:print('Gram row',i,flush=True)
        record('all_actual_JstarF_and_FstarF_entries')
        Bm=arb_mat([[gram(j,f,kernel) for f in Fs] for j in J])
        Fm=arb_mat([[gram(f,g,kernel) for g in Fs] for f in Fs])
        record('verified_full_470_source_physical_projection')
        X=H.solve(Bm,algorithm='precond')
        # Exact full-J physical Schur. No Astar projection is substituted.
        S=Fm-Bm.transpose()*X;S=(S+S.transpose())/2
        progress['S']=balls(S);record('actual_14D_physical_residual_normalization')
        C,N,rows=normalize(S)
        result=dict(status='CERTIFIED_FULL_ORIGINAL_J470_SI29_L2_QUOTIENT_NORMALIZATION',
            working_precision_bits=args.bits,python_flint_version=flint.__version__,
            original_source_nodes=[[str(c),p] for c,p in nodes],
            feature_definitions=[[str(c),str(r),d] for c,r,d in features],
            full_original_source_count=470,actual_feature_count=14,
            independent_entire_series_validation=checks,
            exact_integral_representation='finite trigonometric Laurent sums, regularized primitives through power -4, complex Si for the pole',
            physical_projection='X=(Jstar J)^-1 Jstar F using all original 470 sources',
            physical_Schur='S=Fstar F-Fstar J X',
            physical_Schur_balls=balls(S),
            full_physical_projection_coefficient_balls=balls(X),
            exact_dyadic_feature_transform=[[dyadic(C[i,j]) for j in range(14)] for i in range(14)],
            normalized_physical_Schur_balls=balls(N),normalized_row_error_upper_balls=rows,
            normalized_physical_Schur_lower='99/100',normalized_physical_Schur_upper='101/100',
            normalized_Astar_energy_Schur_lower=str(F(99,100)*KAPPA_STAR),
            physical_full_J_projection_computed=True,
            physical_L2_quotient_condition_number_upper='101/99',
            full_J_Astar_energy_projection_computed=False,
            Astar_energy_condition_number_certified=False,
            normalized_forcing_entries_computed=False,inverse_response_value_certified=False,
            inherited_original_analytic_domain_review='OPEN',W_ODD_NEG='OPEN',even_CC27_Weil_RH='OPEN',
            elapsed_seconds=time.monotonic()-start)
        out.write_text(json.dumps(result,indent=2)+'\n');record('PASS')
        print('ACTUAL FULL-J SI29 L2 NORMALIZATION PASS; original energy lower',result['normalized_Astar_energy_Schur_lower'],flush=True)
        return result
    except Exception:
        progress['exception']=traceback.format_exc();record('FAILED_'+progress['phase'])
        raise

if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('--bits',type=int,default=4096)
    p.add_argument('--output',default='artifacts/si29_full_J_L2_normalization.json')
    run(p.parse_args())
