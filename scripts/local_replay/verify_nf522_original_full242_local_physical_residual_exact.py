#!/usr/bin/env python3
"""NF522 actual original J242 globally fitted local W-p squared, exact source.

Inputs are immutable original NF494 H400/U400 and NF505 full source plus
NF522 verified historical-frame physical beta. All 242 original selected
physical generators, original sinh pole and complete original W are retained.

A complete, correlated 160-jet of the globally fitted physical response
is assembled BEFORE squaring, and all source, Taylor, residual and frame
uncertainty is paid. No finite-select result proves admissible Weil
multiplier image/domain, W_ODD_NEG or RH.
"""
from __future__ import annotations
import argparse,hashlib,json,math,sys
from fractions import Fraction as F
from pathlib import Path
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
import nf521_original_historical_prefix_700digit_gram as gram
gram.configure()
m=gram.m
import verify_nf516_original_edge_rankone_joint_source_exact as source
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
NF505='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
S=m.S;B=F(11,10);BO=F(549,500);H=BO/4096;R=H/2
K=160;W_K=44

def read(path):
    raw=Path(path).read_bytes()
    return json.loads(raw),hashlib.sha256(raw).hexdigest()
def ab(z):return max(abs(z[0]),abs(z[1]))
def env(pol):
    return sum((ab(z)*R**i for i,z in enumerate(pol)),F(0))/S
def iv(z):
    a,b=map(F,z);assert a<=b
    return a,b

def true_physical_source_polynomial(beta,nodes,center):
    """Full true original 242D projection, one correlated 160-jet."""
    p=[(0,0)]*(K+1);largest=F(0);maxfreq=F(0)
    for (f,k),c in zip(nodes,beta):
        b=m.const(c)
        if f=='pole':
            ep=m.expint(center/2);em=m.expint(-center/2)
            sh=m.half(m.sub(ep,em));ch=m.half(m.add(ep,em))
            t=(S,S)
            for n in range(K+1):
                if n:t=m.divint(t,2*n)
                p[n]=m.add(p[n],m.mul(b,m.mul(sh if n%2==0 else ch,t)))
            largest+=abs(c)
            continue
        f=F(f);k=int(k);maxfreq=max(maxfreq,f)
        sn,cs=m.sincos(2*f*center)
        omega=m.mulint(m.mul(m.const(f),m.PI),2)
        assert omega[0]>0
        t=(S,S);trig=[]
        for n in range(K+1):
            if n:t=m.divint(m.mul(t,omega),n)
            v=m.mul(sn if (k%2==0 and n%2==0) else
                    cs if (k%2==0 and n%2) else
                    cs if n%2==0 else sn,t)
            sign=(-1)**((n//2) if n%2==0 else ((n-1)//2))
            if k%2 and n%2:sign=-sign
            trig.append(m.mulint(v,sign))
        powers=[m.const(center**j) for j in range(k+1)]
        for n in range(K+1):
            x=(0,0)
            for l in range(min(k,n)+1):
                x=m.add(x,m.mulint(m.mul(powers[k-l],trig[n-l]),
                                    math.comb(k,l)))
            p[n]=m.add(p[n],m.mul(b,x))
        largest+=abs(c)*BO**k
    assert maxfreq==F(113013,128)
    assert 2*F(22,7)*maxfreq*R<F(4,5)
    tail=3*F(4,5)**(K-13+1)/math.factorial(K-13+1)*largest
    assert 0<tail<F(1,10**100)
    return p,tail

def local_source_energy(cell,original_HU,nodes,beta,epsilon):
    """Original mirrored source H4094/H4095, full globally fitted J242."""
    center=(F(cell)+F(1,2))*H
    assert cell in (4094,4095)
    w,wt=source.physical_source_W_taylor(original_HU,cell)
    assert len(w)==W_K+1 and 0<wt<F(1,10**29)
    q,tail=true_physical_source_polynomial(beta,nodes,center)
    high=sum((ab(z)*R**i for i,z in enumerate(q) if i>W_K),0)/S
    assert high<F(1,10**14),('original source selected correlation METHOD STOP',cell)
    ww=[(m.const(a)[0],m.const(b)[1]) for a,b in w]
    r=[m.sub(ww[i],q[i]) for i in range(W_K+1)]
    bound=env(r)
    assert 0<bound<F(1,10**6)
    err=wt+tail+high
    local_fee=2*H*(2*bound*err+err**2)
    assert local_fee<F(1,10**35)
    sq=[(0,0)]*(2*len(r)-1)
    for i,a in enumerate(r):
        for j,b in enumerate(r):
            sq[i+j]=m.add(sq[i+j],m.mul(a,b))
    lo=hi=F(0)
    for k,v in enumerate(sq):
        if k%2==0:
            qmom=4*R**(k+1)/F(k+1)
            lo+=F(v[0],S)*qmom
            hi+=F(v[1],S)*qmom
    # NF518 certified fit L2(O) <5e-83; NF522 source original
    # weighted raw beta bound epsilon yields L2(O) <=1.5 epsilon.
    fitdist=F(5,10**83)+F(3,2)*epsilon
    fitfee=2*F(13,10**12)*fitdist+fitdist**2
    assert fitfee<F(2,10**93)
    lo-=local_fee+fitfee;hi+=local_fee+fitfee
    assert 0<lo<=hi<F(1,10**27)
    return {'cell':cell,
      'original_full242D_source_r2_outward':[str(lo),str(hi)],
      'original_full242D_source_r2_display':[float(lo),float(hi)],
      'physical_W_uniform_analytic_tail':str(wt),
      'physical_p160_analytic_tail':str(tail),
      'source_correlated_p_over44_tail':str(high),
      'source_total_local_function_error':str(err),
      'source_local_r_polynomial_abssum':str(bound),
      'source_local_polynomial_sq_error_fee':str(local_fee),
      'source_global_fit_and_frame_error_fee':str(fitfee)}

def main():
    p=argparse.ArgumentParser()
    for name in ('nf494','nf505','beta','output'):
        p.add_argument('--'+name,required=True)
    a=p.parse_args()
    H494,hs=read(a.nf494);old,ns=read(a.nf505);b,bs=read(a.beta)
    assert hs==NF494 and ns==NF505
    assert H494['pass']=='NF494-native' and old['pass']=='NF504-native'
    assert old['original_selected_J_dimension']==242
    assert b['pass']=='NF522-original-242D-raw-physical-beta-source-exact'
    assert b['original_nf505_sha256']==ns
    assert b['original_original_basis_nodes']==old['original_source_basis_nodes']
    assert b['original_full_selected_rank']==242
    epsilon=F(b['source_original_weighted_beta_error_upper'])
    assert epsilon<F(1,10**19)
    den=int(b['original_raw_physical_beta_denominator'])
    beta=[F(int(v),den) for v in b['original_raw_physical_beta_numerators']]
    assert len(beta)==242
    cells=[local_source_energy(j,H494,old['original_source_basis_nodes'],
                               beta,epsilon) for j in (4094,4095)]
    lo=sum((F(v['original_full242D_source_r2_outward'][0]) for v in cells),F(0))
    hi=sum((F(v['original_full242D_source_r2_outward'][1]) for v in cells),F(0))
    assert 0<lo<=hi<F(3,10**27)
    result={
      'pass':'NF522-original-source-certified-full242D-named-local-residual-energy',
      'source_original_nf494_SHA256':hs,
      'source_original_nf505_SHA256':ns,
      'source_original_full242D_physical_beta_SHA256':bs,
      'original_selected_dimension':242,
      'true_original_two_cells':cells,
      'original_two_cell_union_eD_outward':[str(lo),str(hi)],
      'original_two_cell_union_eD_display':[float(lo),float(hi)],
      'source_original_NF517_full_energy_upper_targets':['1e-27','1e-27','3e-27'],
      'all_three_original_full242D_local_energy_gates_PASSED':True,
      'original_full242D_true_Fredholm_gaps_NF520_source_certified':True,
      'original_admissible_Weil_multiplier_image_graph_domain':'OPEN',
      'W_ODD_NEG':'OPEN','RH':'OPEN'}
    Path(a.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF522 SOURCE-EXACT original FULL J242 local eH on H4094/H4095 and union PASS')
    print('All three finite-selected original NF517 physical energy obligations PASS')
    print('Weil source image/domain, signed form and RH remain OPEN')
if __name__=='__main__':main()
