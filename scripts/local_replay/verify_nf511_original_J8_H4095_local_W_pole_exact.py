#!/usr/bin/env python3
"""NF511 genuine original NF494 H400/U400 source J8 local W/pole panel.

Exact Fraction interval calculation, matched original source artifacts:
mirrored original H4095 cell. The authentic J8 expression is
 W(B-d)=H(d)+U(B)*C8+U(B-d)/2*log(B/d)
with CONSTANT U(B), not U(B-d), in the seven-prime term.
No original 242D local e_H or NF404 patch decision is claimed.
"""
from __future__ import annotations
import argparse, hashlib, json, math, sys
from pathlib import Path
from fractions import Fraction as F
if hasattr(sys,'set_int_max_str_digits'):sys.set_int_max_str_digits(0)
SRC='0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce'
SEAM='c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675'
NATIVE='ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec'
NF494='39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181'
B=F(11,10);R=F(1,25);M=4096;J=4095
DLO=B-F(549,500);DMAX=DLO+F(549,500*M)
CENTER=(DLO+DMAX)/2
SCALE=10**100;ORDER=30;LOG_TERMS=135

def floor(x):return x.numerator//x.denominator
def ceil(x):return -floor(-x)
def dec_lo(x,n=65):return str(F(floor(x*10**n),10**n))
def dec_hi(x,n=65):return str(F(ceil(x*10**n),10**n))
def add(a,b):return a[0]+b[0],a[1]+b[1]
def as_fr(a):return F(a[0],SCALE),F(a[1],SCALE)

def posmul(a,xlo,xhi):
    lo,hi=a
    assert 0<=xlo<=xhi
    return (floor(lo*(xlo if lo>=0 else xhi)),
            ceil(hi*(xhi if hi>=0 else xlo)))

def signedmul(a,xlo,xhi):
    v=[q*x for q in a for x in (xlo,xhi)]
    return floor(min(v)),ceil(max(v))

def coeffs(receipt,key):
    out=[]
    for pair in receipt[key]:
        lo,hi=map(F,pair)
        assert lo<=hi
        out.append((floor(lo*SCALE),ceil(hi*SCALE)))
    assert len(out)==400
    return out

def shift_source_poly(c):
    # Horner automatic-differentiation Taylor shift around the actual
    # microcell center. This preserves high-cancellation source relations
    # that direct interval evaluation across a slab would otherwise lose.
    v=[(0,0) for _ in range(ORDER+1)]
    for a in reversed(c):
        vv=[(0,0) for _ in v]
        vv[0]=add(posmul(v[0],CENTER,CENTER),a)
        for k in range(1,ORDER+1):
            vv[k]=add(posmul(v[k],CENTER,CENTER),v[k-1])
        v=vv
    tmax=(DMAX-DLO)/2
    tail=tmax**(ORDER+1)*sum(
        (F(max(abs(z[0]),abs(z[1])),SCALE)*math.comb(n,ORDER+1)
        *DMAX**(n-ORDER-1) for n,z in enumerate(c) if n>ORDER),F(0))
    assert tail<F(1,10**45)
    return v,tail

def value_shifted(v,d1,d2):
    t1,t2=d1-CENTER,d2-CENTER
    r=(0,0)
    for coeff in reversed(v):r=add(signedmul(r,t1,t2),coeff)
    return as_fr(r)

def log_positive(z):
    assert z>0
    y=z;k=0
    while y>=2:y/=2;k+=1
    while y<1:y*=2;k-=1
    t=(y-1)/(y+1)
    assert 0<=t<=F(1,3)
    def positive_atanh(s):
        low=2*sum((s**(2*j+1)/F(2*j+1)
                  for j in range(LOG_TERMS)),F(0))
        high=low+2*s**(2*LOG_TERMS+1)/((2*LOG_TERMS+1)*(1-s*s))
        return low,high
    l,h=positive_atanh(t)
    a,b=positive_atanh(F(1,3))
    return (l+k*a,h+k*b) if k>=0 else (l+k*b,h+k*a)

def sqrt_bounds(n):
    k=math.isqrt(n*10**200)
    return F(k,10**100),F(k+1,10**100)

def sinh_bounds(x,terms=30):
    assert 0<=x<=B
    low=sum((x**(2*k+1)/math.factorial(2*k+1)
             for k in range(terms)),F(0))
    first=x**(2*terms+1)/math.factorial(2*terms+1)
    ratio=x*x/F((2*terms+2)*(2*terms+3))
    assert ratio<F(1,10)
    return low,low+first/(1-ratio)

def sinh_minus_x(x,terms=30):
    assert 0<=x<=B
    low=sum((x**(2*k+1)/math.factorial(2*k+1)
             for k in range(1,terms+1)),F(0))
    first=x**(2*terms+3)/math.factorial(2*terms+3)
    ratio=x*x/F((2*terms+4)*(2*terms+5))
    assert ratio<F(1,10)
    return low,low+first/(1-ratio)

def Wcell(H,U,U0,c8,d1,d2,errH,errU):
    hlo,hhi=value_shifted(H,d1,d2)
    ulo,uhi=value_shifted(U,d1,d2)
    hlo-=errH;hhi+=errH
    ulo-=errU;uhi+=errU
    u0lo,u0hi=U0
    clo,chi=c8
    assert u0hi<0 and ulo>0 and clo>0
    ll=log_positive(B/d2)[0]
    lh=log_positive(B/d1)[1]
    # Original complete response, including authentic original odd pole
    # in H/U. Prime C8 multiplies v=U(B) only.
    wl=hlo+u0lo*chi+ulo*ll/2
    wh=hhi+u0hi*clo+uhi*lh/2
    assert wl<wh<0, 'METHOD STOP: cannot certify original W sign'
    return wl,wh

def panel(H,U,U0,c8,errH,errU,slabs):
    width=(DMAX-DLO)/slabs
    El=Eh=bl=bh=F(0)
    minW=maxW=None
    for k in range(slabs):
        d1=DLO+k*width;d2=d1+width
        wl,wh=Wcell(H,U,U0,c8,d1,d2,errH,errU)
        El+=2*width*wh*wh
        Eh+=2*width*wl*wl
        sl=sinh_bounds((B-d2)/2)[0]
        sh=sinh_bounds((B-d1)/2)[1]
        assert sl>0
        bl+=2*width*wl*sh
        bh+=2*width*wh*sl
        if minW is None or wl<minW:minW=wl
        if maxW is None or wh>maxW:maxW=wh
    return El,Eh,bl,bh,minW,maxW

def main():
    ap=argparse.ArgumentParser()
    ap.add_argument('--nf494',required=True)
    ap.add_argument('--nf505',required=True)
    ap.add_argument('--output',required=True)
    ap.add_argument('--slabs',type=int,default=128)
    o=ap.parse_args()
    assert 16<=o.slabs<=1024 and o.slabs&(o.slabs-1)==0
    raw494=Path(o.nf494).read_bytes()
    raw505=Path(o.nf505).read_bytes()
    h=json.loads(raw494);old=json.loads(raw505)
    assert hashlib.sha256(raw494).hexdigest()==NF494
    assert hashlib.sha256(raw505).hexdigest()==NATIVE
    assert h['pass']=='NF494-native' and old['pass']=='NF504-native'
    assert h['original_nf407_source_sha256']==old['source_original_NF407_sha256']==SRC
    assert h['original_nf406_seams_sha256']==old['source_original_NF406_sha256']==SEAM
    assert old['original_selected_J_dimension']==242
    assert old['original_source_basis_nodes'][241]==['pole',None]
    assert old['original_exterior_center_radius']=='549/500'
    assert h['original_source_analytic_Cauchy_radius']=='1/25'
    assert h['original_B']=='11/10' and h['original_true_terminal_delta']=='1/500'
    assert h['original_source_400_jet_order']==400
    assert old['original_support_saturated_physical_Hilbert_gate']=='CERTIFIED_PHYSICAL_SUPPORT_NO_GO'
    assert DLO<DMAX<R
    # Stay on the same true original n=9-active J8 physical source cell.
    assert log_positive(F(9))[1]<2*B-DMAX

    weights={2:2,3:3,4:2,5:5,7:7,8:2,9:3}
    clo=chi=F(0)
    for n,p in weights.items():
        lp,up=log_positive(F(p))
        sqlo,sqhi=sqrt_bounds(n)
        clo+=lp/sqhi
        chi+=up/sqlo
    assert 3<clo<=chi<5
    rawH=coeffs(h,'original_H_400_native_outward')
    rawU=coeffs(h,'original_U_400_native_outward')
    U0=as_fr(rawU[0]);assert U0[1]<0
    H,feeH=shift_source_poly(rawH)
    U,feeU=shift_source_poly(rawU)
    ratio=DMAX/R
    cauchyH=F(10)**420*ratio**400/(1-ratio)
    cauchyU=F(10)**400*ratio**400/(1-ratio)
    assert cauchyH<F(1,10**77) and cauchyU<F(1,10**97)
    broad=panel(H,U,U0,(clo,chi),feeH+cauchyH,feeU+cauchyU,16)
    fine=panel(H,U,U0,(clo,chi),feeH+cauchyH,feeU+cauchyU,o.slabs)
    assert broad[0]<=fine[0]<=fine[1]<=broad[1]
    assert broad[2]<=fine[2]<=fine[3]<=broad[3]
    assert fine[1]/fine[0]<F(110,100)

    s0l,s0h=sinh_minus_x(B-DLO)
    s1l,s1h=sinh_minus_x(B-DMAX)
    cp_lo,cp_hi=s0l-s1h,s0h-s1l
    assert 0<cp_lo<cp_hi
    assert fine[2]<fine[3]<0
    pole_power_lower=fine[3]*fine[3]/cp_hi
    rem_upper=fine[1]-pole_power_lower
    capture_floor=pole_power_lower/fine[1]
    assert 0<rem_upper<fine[1]
    assert capture_floor>F(96,100)
    # Recompute conservative scalar implications from separately printed
    # outward *decimal* input intervals, so independent Fraction replay
    # does not rely on unprinted extra precision.
    Ehi_receipt=F(dec_hi(fine[1]))
    bhi_receipt=F(dec_hi(fine[3]))
    Chi_receipt=F(dec_hi(cp_hi))
    capture_power_receipt=F(dec_lo(bhi_receipt**2/Chi_receipt))
    unexplained_receipt=F(dec_hi(Ehi_receipt-capture_power_receipt))
    fraction_receipt=F(dec_lo(capture_power_receipt/Ehi_receipt))
    assert fraction_receipt>F(96,100)
    result={
      'pass':'NF511-original-source-exact-local-W-pole-panel',
      'standing':'LOCAL SOURCE-EXACT original full W² and sinh-pole W moment/Gram on named J8 H4095; full 242D residual e_H and named NF404 patch verdict OPEN',
      'original_nf494_raw_SHA256':NF494,'original_nf505_raw_SHA256':NATIVE,
      'original_nf407_source_SHA256':SRC,'original_nf406_seams_SHA256':SEAM,
      'original_selected_dimension':242,'original_sinh_pole_index':241,
      'mirrored_cell_index':J,'mirrored_cell_count':M,
      'x_positive_cell':[str(B-DMAX),str(B-DLO)],
      'd_positive_cell':[str(DLO),str(DMAX)],
      'analytic_radius':str(R),'recentered_taylor_order':ORDER,
      'cauchy_H400_tail_upper':dec_hi(cauchyH,90),
      'cauchy_U400_tail_upper':dec_hi(cauchyU,110),
      'source_C8_interval':[dec_lo(clo),dec_hi(chi)],
      'local_E_H_original_full_W_squared':[dec_lo(fine[0]),dec_hi(fine[1])],
      'local_b_H_original_sinh_pole_cross':[dec_lo(fine[2]),dec_hi(fine[3])],
      'local_C_H_original_sinh_pole_Gram':[dec_lo(cp_lo),dec_hi(cp_hi)],
      'local_best_scalar_pole_capture_power_lower':str(capture_power_receipt),
      'local_best_scalar_pole_unexplained_upper':str(unexplained_receipt),
      'local_best_scalar_pole_alignment_fraction_lower':str(fraction_receipt),
      'coarse_16_slab_W2':[dec_lo(broad[0]),dec_hi(broad[1])],
      'coarse_16_slab_Ws':[dec_lo(broad[2]),dec_hi(broad[3])],
      'slabs':o.slabs,'original_named_W_local_EH':True,
      'original_named_full_242D_bH':False,'original_named_full_242D_CH':False,
      'original_named_residual_eH':'OPEN','NF404_named_patch_verdict':'OPEN',
      'Weil_multiplier_image_graph_domain':'OPEN','W_ODD_NEG':'OPEN','RH':'OPEN'
    }
    Path(o.output).write_text(json.dumps(result,indent=2)+'\n')
    print('NF511 authentic original H4095 W^2',float(fine[0]),float(fine[1]))
    print('NF511 original W*sinh pole',float(fine[2]),float(fine[3]))
    print('NF511 local best-pole capture >=',float(capture_floor))
    print('No full original residual e_H / Weil image or RH promotion.')
if __name__=='__main__':main()
