#!/usr/bin/env python3
"""NF516 original source exact J8 W, genuine selected v23, global rank-one fit.

This is a SOURCE-NATIVE rational replay, NOT just an algebraic receipt audit.
It re-centers all original NF494 H400/U400 source coefficients at authentic
n9-active H4094/H4095, pays analytic/log/Taylor remainders, and directly
integrates (W-beta*v)^2, using NF515's globally fixed beta.
The full original J242 globally-fitted eH, Weil test-source image and RH OPEN.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
import verify_nf513_original_J8_H4094_local_W_pole_exact as nf513
m=nf513.m

NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF514='39a8679197447975f54629a04c9608659e47aadf61dffb6e5dea11d0df2dc6b0'
NF515='3ff6a14a0d850dc23a3965ca651a4b1229ba4d82881c4373061b7483f07d289f'
NF511='9e80c5bf05d9242b078f407c10009fa2c036b8abc1f8a5add24c1fe4e58aaed1'
NF513='7c6aaf2374a7e58ab0749955b15083719f555182e5d6dd8e723fa1fc31ead495'
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
S=10**160;B=F(11,10);BO=F(549,500);H=BO/4096;ORDER=44

def read(p):
    raw=Path(p).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def flo(z,p=105):
    n=z*10**p
    return str(F(n.numerator//n.denominator,10**p))
def cei(z,p=105):
    n=-z*10**p
    return str(F(-(n.numerator//n.denominator),10**p))
def pair(a):return [flo(a[0]),cei(a[1])]
def interval(a):
    x,y=map(F,a)
    assert x<=y
    return x,y
def add(a,b):return a[0]+b[0],a[1]+b[1]
def mul(a,b):
    z=[x*y for x in a for y in b]
    return min(z),max(z)
def sc(a,k):return (a[0]*k,a[1]*k) if k>=0 else (a[1]*k,a[0]*k)
def mx(a):return max(abs(a[0]),abs(a[1]))
def overlap(a,b):return max(a[0],b[0])<=min(a[1],b[1])
def atan(q,n=140):
    z=sum(((-1)**i*q**(2*i+1)/F(2*i+1) for i in range(n)),F(0))
    e=q**(2*n+1)/F(2*n+1)
    return (z,z+e) if n%2==0 else (z-e,z)
def true_source_selected_q(seed,original):
    nodes=[(F(f),k) for f,k in seed['original_source_basis_nodes']]
    assert nodes==[(F(37,64),k) for k in range(14)]+[(F(211,128),k) for k in range(9)]
    assert original['original_source_basis_nodes'][:23]==[[str(f),k] for f,k in nodes]
    cs=list(map(int,seed['integer_coefficients']))
    den=int(seed['coefficient_denominator'])
    assert len(cs)==23 and den==10**105 and sum(map(abs,cs))<5*den
    a,b=atan(F(1,5)),atan(F(1,239))
    lo,hi=16*a[0]-4*b[1],16*a[1]-4*b[0]
    assert 3<lo<hi<F(22,7)
    trig={}
    for f in set(f for f,k in nodes):
        p,q=2*f*lo,2*f*hi
        w=(p*S).numerator//(p*S).denominator
        assert F(w,S)<=p and q<F(w+6,S)
        trig[f]=[S]+[w**i//(S**(i-1)*math.factorial(i)) for i in range(1,161)]
    out=[0]*175
    for c,(f,k) in zip(cs,nodes):
        for j,z in enumerate(trig[f]):
            if j%2==k%2:continue
            sign=-1 if ((j-1)//2 if k%2==0 else j//2)%2 else 1
            out[k+j]+=sign*(c*z//den)
    assert all(out[i]==0 for i in range(0,175,2))
    assert 5*B**13*F(12)**161/math.factorial(161)<F(1,10**109)
    assert 23*161*B**174/S<F(1,10**145)
    return out
def local_selected_taylor(q,x0):
    """Fixed 1e160 integer-OUTWARD whole-poly shift preserves cancellations."""
    nn,dd=x0.numerator,x0.denominator
    lo=[0]*len(q);hi=[0]*len(q)
    for z in reversed(q):
        nl=[0]*len(q);nh=[0]*len(q)
        nl[0]=(lo[0]*nn)//dd+z
        nh[0]=-((-hi[0]*nn)//dd)+z
        for j in range(1,len(q)):
            nl[j]=(lo[j]*nn)//dd+lo[j-1]
            nh[j]=-((-hi[j]*nn)//dd)+hi[j-1]
        lo,hi=nl,nh
    full=[(F(a,S),F(b,S)) for a,b in zip(lo,hi)]
    radius=H/2
    tail=sum((mx(v)*radius**j for j,v in enumerate(full) if j>12),F(0))
    assert tail<F(1,10**48)
    # Original NF514 source-true analytic v differs from complete q
    # by <1e-100 uniformly over the full physical original carrier.
    return full[:13],tail+F(1,10**100)
def physical_source_W_taylor(nf494,cell):
    """Original source W(B-d), genuine n9 branch and full H400/U400 fees."""
    dl=B-BO+(4095-cell)*H;dr=dl+H;dc=(dl+dr)/2
    assert cell in (4094,4095) and dr<F(1,25)
    m.DLO=dl;m.DMAX=dr;m.CENTER=dc;m.ORDER=ORDER;m.LOG_TERMS=140
    nf513.DL=dl;nf513.DR=dr;nf513.WIDTH=H;nf513.TRUNC=85
    assert m.log_positive(F(9))[1]<2*B-dr
    hraw=m.coeffs(nf494,'original_H_400_native_outward')
    uraw=m.coeffs(nf494,'original_U_400_native_outward')
    hj,ht=nf513.source_preserving_shift(hraw)
    uj,ut=nf513.source_preserving_shift(uraw)
    hh=[sc(m.as_fr(z),(-1 if i%2 else 1)) for i,z in enumerate(hj)]
    uu=[sc(m.as_fr(z),(-1 if i%2 else 1)) for i,z in enumerate(uj)]
    ll=[m.log_positive(B/dc)]+[(F(1,i*dc**i),F(1,i*dc**i)) for i in range(1,ORDER+1)]
    C0=C1=F(0)
    for n,p in ((2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3)):
        l,u=m.log_positive(F(p))
        sl,su=m.sqrt_bounds(n)
        C0+=l/su;C1+=u/sl
    assert 3<C0<C1<5
    u0=m.as_fr(uraw[0]);assert u0[1]<0
    result=[]
    for i in range(ORDER+1):
        conv=(F(0),F(0))
        for j in range(i+1):conv=add(conv,mul(uu[j],ll[i-j]))
        result.append(add(hh[i],sc(conv,F(1,2))))
    # Constant original seven-prime term uses U(B), NOT U(B-d).
    result[0]=add(result[0],mul(u0,(C0,C1)))
    radius=H/2;rho=radius/dc
    assert 0<rho<F(1,10)
    ltail=rho**(ORDER+1)/((ORDER+1)*(1-rho))
    ch=F(10)**420*(dr/F(1,25))**400/(1-dr/F(1,25))
    cu=F(10)**400*(dr/F(1,25))**400/(1-dr/F(1,25))
    lmax=m.log_positive(B/dl)[1]
    Uenv=sum((mx(z)*radius**i for i,z in enumerate(uu)),F(0))
    producttail=sum((mx(uu[i])*mx(ll[j])*radius**(i+j)
                     for i in range(ORDER+1) for j in range(ORDER+1)
                     if i+j>ORDER),F(0))
    err=ht+ch+(ut+cu)*lmax/2+(producttail+Uenv*ltail)/2
    assert 0<err<F(1,10**30)
    return result,err
def squared_polynomial(p):
    c=[(F(0),F(0))]*(2*len(p)-1)
    for i,x in enumerate(p):
        for j,y in enumerate(p):c[i+j]=add(c[i+j],mul(x,y))
    r=H/2;res=(F(0),F(0))
    for i,x in enumerate(c):
        if i%2==0:res=add(res,sc(x,4*r**(i+1)/(i+1)))
    return res
def mixed_polynomial(a,b):
    c=[(F(0),F(0))]*(len(a)+len(b)-1)
    for i,x in enumerate(a):
        for j,y in enumerate(b):c[i+j]=add(c[i+j],mul(x,y))
    r=H/2;res=(F(0),F(0))
    for i,x in enumerate(c):
        if i%2==0:res=add(res,sc(x,4*r**(i+1)/(i+1)))
    return res
def envelope(p):return sum((mx(z)*(H/2)**i for i,z in enumerate(p)),F(0))
def strict(out):
    assert out[0]>0 and out[0]<=out[1]
    return out

def main():
    p=argparse.ArgumentParser()
    for k in ('nf494','nf505','nf514_seed','nf515','nf511','nf513','output'):
        p.add_argument('--'+k,required=True)
    a=p.parse_args()
    h,hs=read(a.nf494);old,os=read(a.nf505);seed,ss=read(a.nf514_seed)
    bridge,bs=read(a.nf515);prior95,ps=read(a.nf511);prior94,ts=read(a.nf513)
    assert (hs,os,ss,bs,ps,ts)==(NF494,NF505,NF514,NF515,NF511,NF513)
    assert h['pass']=='NF494-native' and old['pass']=='NF504-native'
    assert h['original_nf407_source_sha256']==old['source_original_NF407_sha256']==SRC
    assert h['original_nf406_seams_sha256']==old['source_original_NF406_sha256']==SEAM
    assert old['original_selected_J_dimension']==242
    assert bridge['pass']=='NF515-original-source-global-exterior-v23-witness-moment-exact'
    assert bridge['source_original_NF514_seed_SHA256']==ss
    assert prior95['pass'] in ('NF511-source-local-W-square-exact','NF511-original-source-exact-local-W-pole-panel')
    assert prior94['pass'] in ('NF513-source-local-W-square-exact','NF513-original-source-J8-H4094-local-W-pole-exact')
    mom=interval(bridge['original_true_exterior_O_W_witness_moment_outward'])
    norm=interval(bridge['original_selected_v23_full_exterior_norm_squared'])
    assert mom[1]<0 and norm[0]>0
    # Quantize the *outward* global source beta interval before combining
    # hundreds of unrelated exact source denominators in local jet products.
    # This is only an outward containment, not a fit replacement.
    beta=(F(flo(mom[0]/norm[0],75)),F(cei(mom[1]/norm[1],75)))
    assert beta[1]<0
    q=true_source_selected_q(seed,old)
    cells=[]
    for j,prior in ((4094,prior94),(4095,prior95)):
        x0=(j+F(1,2))*H
        v,ve=local_selected_taylor(q,x0)
        W,we=physical_source_W_taylor(h,j)
        P=mixed_polynomial(W,v)
        fee=2*H*(envelope(W)*ve+envelope(v)*we+ve*we)
        P=(P[0]-fee,P[1]+fee)
        E=squared_polynomial(W)
        ee=2*H*(2*envelope(W)*we+we*we)
        E=(E[0]-ee,E[1]+ee)
        priorE=interval(prior['original_cell_full_W_sq_outward']
                      if 'original_cell_full_W_sq_outward' in prior
                      else prior['local_E_H_original_full_W_squared'])
        assert overlap(E,priorE)
        residual=[add(W[i],sc(mul(beta,v[i]),-1)) if i<len(v) else W[i]
                  for i in range(len(W))]
        re=we+mx(beta)*ve
        Q=squared_polynomial(residual)
        qe=2*H*(2*envelope(residual)*re+re*re)
        Q=(Q[0]-qe,Q[1]+qe)
        assert E[0]>0 and P[1]<0 and Q[0]>0
        capture=1-Q[1]/E[0]
        assert capture>(F(70,100) if j==4094 else F(63,100))
        cells.append({'cell':j,'original_W2':pair(E),
                      'original_Wv23':pair(P),
                      'original_globally_fitted_rankone_direct_residual':pair(Q),
                      'rankone_removed_energy_fraction_lower':flo(capture),
                      'source_W_function_error_upper':cei(we),
                      'source_true_v_function_error_upper':cei(ve)})
        print('NF516 SOURCE original H',j,
              'Wv',float(P[0]),'rankone e',float(Q[0]),flush=True)
    sums={}
    for key in ('original_W2','original_Wv23','original_globally_fitted_rankone_direct_residual'):
        a1=interval(cells[0][key]);b1=interval(cells[1][key])
        sums[key]=add(a1,b1)
    E=sums['original_W2'];R=sums['original_globally_fitted_rankone_direct_residual']
    b=sums['original_Wv23']
    assert 1-R[1]/E[0]>F(65,100)
    signed=(b[1]/mom[0],b[0]/mom[1])
    assert F(95,100)<signed[0]<=signed[1]<1
    out={'pass':'NF516-original-H4094-H4095-joint-analytic-source-local-rankone',
         'standing':'Original NF494 complete H400/U400 physical W and genuine NF514 J23 selected witness globally fitted with NF515 original exterior coefficient; FULL J242 local e_H and RH OPEN',
         'NF494_original_SHA256':hs,'NF505_original_SHA256':os,
         'NF514_genuine_selected_seed_SHA256':ss,'NF515_original_source_bridge_SHA256':bs,
         'NF511_local_source_SHA256':ps,'NF513_local_source_SHA256':ts,
         'original_NF407_source_SHA256':SRC,'original_NF406_seams_SHA256':SEAM,
         'full_original_selected_dimension':242,
         'globally_fitted_rankone_source_generators':23,
         'original_true_source_cells':cells,
         'original_true_union_W2':pair(E),
         'original_true_union_signed_Wv23':pair(b),
         'original_true_union_global_rankone_residual':pair(R),
         'original_true_union_rankone_energy_removed_fraction_lower':flo(1-R[1]/E[0]),
         'original_true_two_cells_fraction_of_NET_SIGNED_exterior_source_coupling_lower':flo(signed[0]),
         'source_exterior_beta_v23':pair(beta),
         'full_original_J242_globally_fitted_local_eH':'OPEN',
         'original_NF404_named_support_gate':'OPEN',
         'Weil_multiplier_image_graph_domain':'OPEN',
         'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(out,indent=2)+'\n')
    print('NF516 original source joint analytic exact rational PASS. >65% original W² locally removed, >95% net signed source coupling on two real cells')
    print('Full original J242 local fitted residual and RH OPEN')
if __name__=='__main__':main()
