#!/usr/bin/env python3
"""GERM-99: close delta13<v<=omega11 by direct thirteenth cones."""
from fractions import Fraction as F
from pathlib import Path
import hashlib,json
assert __debug__
ROOT=Path(__file__).resolve().parents[1]
PIN='tools/sz_post_u_c11_eleventh_last_visit_audit.py'
PIN_SHA='9cf48a34efe672d09edd083d32c3d8e17e45d8dbd0a7d37c0e029412d8ab15c7'
assert hashlib.sha256((ROOT/PIN).read_bytes()).hexdigest()==PIN_SHA
import sz_post_u_c11_eleventh_last_visit_audit as p
g97=p.parent; old=p.old; product,det=p.product,p.det
TW={'D10':['A']*9+['D'],'E10':['A']*9+['E'],'D11':['A']*10+['D'],'E11':['A']*10+['E']}
TH={'A0':['D11','D10'],'A1':['D11','E10'],'A2':['E11','E10'],
    'B0':['D11','D10','E10'],'B1':['D11','E10','E10'],'B2':['E11','E10','E10']}
SG={'A0':1,'A1':-1,'A2':1,'B0':1,'B1':-1,'B2':1}; CH=p.CHART; FACTOR=F(10**6)
af,add,sub,vertices=p.af,p.add,p.sub,p.vertices; scale,audit=p.scale,p.audit
seed=p.seed; ell,w,r12,o12=p.ell,p.w,p.r12,p.om12; c,u,v=p.c,p.u,p.v
d13,cut=p.delta13,p.cut13; x=sub(v,d13); zero=af(); RANGE=p.RANGE
GLOBAL=RANGE+(u,sub(c,u),v,sub(w,v),d13,r12,o12,cut)

def build():
    l10,l11,_,pv=p.build_matrices(); l12={k:product(q,l11) for k,q in TW.items()}; return l10,l12,pv

def tw_req(k,y):
    n=10 if k.endswith('10') else 11; q=sub(add(y,scale(n,w)),ell)
    m=[('y>0',y),('y<w',sub(w,y)),('q>0',q),('q<w',sub(w,q)),
       ('lower_global_scope',sub(v,d13)),('upper_global_scope',sub(w,v)),
       ('cut',sub(y,r12) if n==10 else sub(r12,y))]
    if k=='D10':m+=[('bit',sub(y,add(r12,v)))]
    if k=='E10':m+=[('bit',sub(add(r12,v),y))]
    s=add(y,o12)
    if k=='D11':m+=[('bit',sub(s,v))]
    if k=='E11':m+=[('bit',sub(v,s))]
    return q,m

def tw_lift(k,y):
    q,m=tw_req(k,y); word=TW[k]; n=len(word); pp=[add(y,scale(j,w)) for j in range(n)]+[q]
    for j,a in enumerate(word):
        z,lo=p.level11_lift(a,pp[j]); assert z==pp[j+1]
        m += [(f'{j}:{n}',r) for n,r in lo]
        m += [(f'early{j}',sub(z,w) if j<n-1 else sub(w,z))]
    return q,m

def th_req(k,y):
    sh=k[0]=='A'; q=add(y,d13) if sh else sub(y,cut)
    return q,[('y>0',y),('y<r12',sub(r12,y)),('q>0',q),('q<r12',sub(r12,q)),
      ('lower_global_scope',sub(v,d13)),('upper_global_scope',sub(w,v)),
      ('cut',sub(cut,y) if sh else sub(y,cut))]

def th_lift(k,y):
    q,m=th_req(k,y); word=TH[k]
    pp=[y,add(y,o12),add(y,d13)] if k[0]=='A' else [y,add(y,o12),add(y,d13),sub(y,cut)]
    for j,a in enumerate(word):
        z,lo=tw_lift(a,pp[j]); assert z==pp[j+1]
        m += [(f'{j}:{n}',r) for n,r in lo]
        m += [(f'early{j}',sub(z,r12) if j<len(word)-1 else sub(r12,z))]
    return q,m

def extra(k,y):
    dI=sub(add(y,o12),v); iI=sub(v,add(y,o12)); dL=sub(y,x); iL=sub(x,y)
    return (dI,dL) if k in ('A0','B0') else ((dI,iL) if k in ('A1','B1') else (iI,))

def geometry():
    assert add(d13,cut)==r12 and add(d13,r12)==o12 and add(o12,r12)==w
    C={}
    for k in TH:
        _,r=th_req(k,seed);_,m=th_lift(k,seed); C[k]=audit(m,vertices(GLOBAL+tuple(z for _,z in r)+extra(k,seed)))
    for k in ('A0','B0'):
        _,r=th_req(k,seed);_,m=th_lift(k,seed); C[k]['entry']=audit(m,vertices(GLOBAL+tuple(z for _,z in r)+extra(k,seed)+(sub(v,d13),sub(d13,v))))
    for k in ('A2','B2'):
        _,r=th_req(k,seed);_,m=th_lift(k,seed); C[k]['endpoint']=audit(m,vertices(GLOBAL+tuple(z for _,z in r)+extra(k,seed)+(sub(v,w),sub(w,v))))
    J={}
    for nm,face,ks in [('rho12',r12,('A1','B0')),('omega12',o12,('A1','B1')),('omega11-delta13',sub(w,d13),('A2','B1'))]:
        J[nm]={}
        for k in ks:
            _,r=th_req(k,seed);_,m=th_lift(k,seed); J[nm][k]=audit(m,vertices(GLOBAL+tuple(z for _,z in r)+extra(k,seed)+(sub(v,face),sub(face,v))))
    return {'cells':C,'junctions':J,'entry':['A0','B0'],'endpoint':['A2','B2'],
      'regimes':['A0,A1,B0','A1,B0,B1','A1,A2,B1','A2,B1,B2'],'sampled_topology':False}

def arithmetic():
    a,s,m=old.add,old.sub,old.mul; h,k=(-4,4,-1),(4,-1,-1)
    kap=s(k,m(5,h));tau=s(h,m(5,kap));th=s(kap,m(8,tau));al=s(tau,m(3,th));be=s(th,al);ga=s(al,be)
    xi=s(m(5,ga),be);om=s(ga,m(19,xi));eta=s(xi,om);chi=s(m(2,om),xi);psi=s(eta,chi);sig=s(m(3,psi),chi)
    rho=s(psi,m(3,sig));cc=s(sig,rho);o10=s(sig,m(10,cc));ll=s(cc,o10);ww=s(cc,m(4,ll));rr=s(ll,m(10,ww));oo=s(ww,rr);dd=s(oo,rr)
    L98=(29136426436,-25609175812,4932606194); inc=s(ww,dd); L99=a(L98,inc); top=a((4,-1,0),m(3,h))
    assert inc==m(2,rr) and L99==(1020029612,-896545004,172684332)
    logs=[old.log_box(n) for n in (2,3,5)]; enc=lambda z:sum((q*t for q,t in zip(z,logs)),old.box(0))
    return {'endpoint':L99,'endpoint_decimal':p.g77.show_box(enc(L99),45),'increment':inc,'increment_decimal':p.g77.show_box(enc(inc),45),
      'remaining_tenth':p.g77.show_box(enc(s(cc,a(ll,ww))),45),'remaining_sixth_seventh':p.g77.show_box(enc(s(eta,a(ll,ww))),45),
      'remaining_three_layer':p.g77.show_box(enc(s(top,L99)),45)}

def matrices():
    l10,l12,pv=build(); C={}
    for k,q in TH.items():
        B=product(q,l12); disc=(B[0][0]+B[1][1])**2-4*det(B); assert disc.lo>0
        C[k]=p.g77.cone_test(B,CH,SG[k],FACTOR)
    N=product(['A1','B0','B0','B1'],l10); tr=N[0][0]+N[1][1]; dd=det(N); disc=tr*tr-4*dd
    assert dd.lo<=1<=dd.hi and disc.hi<0
    fk=min(C,key=lambda z:F(C[z]['forward_lower'])); bk=min(C,key=lambda z:F(C[z]['backward_lower']))
    return {'chart':[[str(z) for z in r] for r in CH],'factor':'1000000','certificates':C,
      'minimum_forward_lower':C[fk]['forward_lower'],'minimum_backward_lower':C[bk]['backward_lower'],
      'next_word':['A1','B0','B0','B1'],'next_trace':old.display_matrix([[tr]]),'next_discriminant':old.display_matrix([[disc]])}

def main():
    print(json.dumps({'pass':'SZ-KERNEL-EDGE-GERM-99','standing':'UNRATIFIED','entry_commit':'4b9f4e294939410bd542ef1e427faf3e0c61e2ea',
      'dependency_sha256':{PIN:PIN_SHA},'scope':'delta13<v<=omega11; x=v-delta13=e-e98','arithmetic':arithmetic(),'matrix_audit':matrices(),
      'geometry':geometry(),'fourteenth_or_deeper_induction_used':False,'new_retained_coordinates':0,
      'canonical_cursor':'SZ-CROSS-COLLAR-3','canonical_effect':'NONE'},indent=2))
if __name__=='__main__':main()
