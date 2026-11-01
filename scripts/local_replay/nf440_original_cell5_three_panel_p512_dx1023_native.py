#!/usr/bin/env python3
"""NF440 original true physical CELL5 signed p and raw dx Chebyshev moments.

Exact actual NF406 seams J5=(log4-B, B-log2), original NF407 u4(B)
source interval and genuine original principal JUMP weights n2+n3+n4+n5 ONLY.
The original regular response z has FOUR minus shifts and no plus shifts;
the principal r has FOUR jumps throughout all three unchanged-source panels.
2048-bit native Arb enclosures of m_n=∫_J5 p(x)T_n and
J_k=∫_J5piece T_k for n<512 and k<1023; aggregate 3 p0 before NF410.
Analytic original log Cheb remainder charged; no x sampling/mesh.
No claim of original signed cell5 z integral until separate contraction.
"""
from __future__ import annotations
import argparse,hashlib,json,sys
from pathlib import Path
from fractions import Fraction as F
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10); PANELS=((F(565,1000),F(63,1000)),(F(677,1000),F(63,1000)),(F(789,1000),F(63,1000))); C,H=PANELS[0]
PRIMES=((2,2,1),(3,3,1),(4,2,1),(5,5,1))
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
def read(p):
 raw=Path(p).read_bytes()
 return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return arb(str(x))
def outward(x,digits=75):
 m,rad,e=x.mid_rad_10exp(digits);q=F(10)**int(e)
 return F(int(m)-int(rad))*q,F(int(m)+int(rad))*q
def ov(a,b):return a[0]<=b[1] and b[0]<=a[1]
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 ap.add_argument('--panel',type=int,required=True,choices=(1,2,3))
 ap.add_argument('--degree',type=int,default=511)
 ap.add_argument('--log-modes',type=int,default=110)
 ap.add_argument('--precision',type=int,default=2048)
 ap.add_argument('--output',required=True)
 args=ap.parse_args()
 assert args.degree==511 and args.log_modes>=110 and args.precision>=2048
 ctx.prec=args.precision
 global C,H
 C,H=PANELS[args.panel-1]
 s,sha=read(args.source);knots,ksha=read(args.seams)
 principal,psha=read(args.principal);old,oldsha=read(args.nf410)
 assert sha==SOURCE_SHA and ksha==SEAM_SHA
 assert principal['original_nf406_seams_sha256']==ksha
 assert old['original_nf406_source_sha256']==ksha
 assert old['original_nf407_source_sha256']==psha
 assert s['original_dimension']==242
 assert len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert len(s['original_source_critical_sine_frequencies'])==32
 assert all(v['W_ODD_NEG']==v['RH']=='OPEN' for v in (s,knots,principal,old))
 assert len(old['original_positive_original_physical_cells'])==8
 cell=old['original_positive_original_physical_cells'][4]
 assert cell['cell']==5 and cell['left_label']=='-B+log(5)' and cell['right_label']=='-B+log(7)'
 ordered=knots['certified_ordered_knots']
 assert ordered[12]['label']=='-B+log(5)' and ordered[13]['label']=='-B+log(7)'
 cuts=(A(F(31,50)),A(F(73,100)))
 left=A(5).log()-A(B) if args.panel==1 else cuts[args.panel-2]
 right=A(7).log()-A(B) if args.panel==3 else cuts[args.panel-1]
 assert A(F(1,2))<left<right<A(F(852,1000))
 assert A(C-H)<left<right<A(C+H)
 tl=(left-A(C))/A(H);tr=(right-A(C))/A(H)
 assert -1<tl<tr<1
 length=right-left
 assert length<A(F(1,8))
 thetaL=tl.acos();thetaR=tr.acos()
 # Original independent NF407 source endpoint source interval v<0.
 vpair=tuple(map(F,principal['original_source_u4_endpoint_interval']))
 assert vpair[0]<vpair[1]<0 and vpair[1]-vpair[0]<F(1,10**40)
 v_mid=(vpair[0]+vpair[1])/2
 v_rad=(vpair[1]-vpair[0])/2
 v=A(v_mid)
 weights=[]
 for n,base,mult in PRIMES:
  entry=next(z for z in principal['source_true_original_prime_jump_terms'] if z['n']==n)
  w=A(base).log()/A(n).sqrt()
  a,b=outward(w)
  z=list(map(F,entry['signed_mangoldt_weight_positive_interval']))
  assert ov((a,b),z),('actual original Mangoldt source mismatch',n)
  weights.append((n,mult,w))
 assert [(n,m) for n,m,w in weights]==[(2,1),(3,1),(4,1),(5,1)]
 W=sum((w*m for n,m,w in weights),arb(0))
 assert A(0)<W<A(3)
 # Chebyshev theta primitive. Evaluate at actual irrational NF406
 # endpoints, not rational surrogate knot midpoints or Gauss samples.
 nmax=max(2*args.degree, args.degree+args.log_modes)+1
 diff=[(arb(n)*thetaR).cos()-(arb(n)*thetaL).cos() for n in range(nmax+2)]
 J=[A(H)*(tr-tl),A(H)*(tr*tr-tl*tl)/2]
 for n in range(2,nmax+1):
  J.append(A(H)*(diff[n+1]/(2*(n+1))-diff[n-1]/(2*(n-1))))
 assert len(J)==nmax+1
 raw=[outward(J[n]) for n in range(2*args.degree+1)]
 assert len(raw)==1023
 raw_len=outward(length)
 assert ov(raw[0],raw_len)
 for n,(a,b) in enumerate(raw):
  assert a<=b and b-a<F(1,10**35),(n,'original dx-moment not resolved')
  assert -raw_len[1]-F(1,10**35)<a<=b<raw_len[1]+F(1,10**35),(n,'|T_n|≤1 missing')
 # Original J5 p(x)=v*(log(B/(B-x))/2+w2+w3+w4+w5).
 # NF407 r(x)=v*sgn(x)*sum w_n 1_(|x| > |B-log n|).
 # On all three J5 pieces n2,n3,n4,n5 principal jumps are ON;
 # all four original regular minus shifts active, no plus.
 # D=B-C, original endpoint log Cheb exact analytic coefficients.
 D=A(B-C)
 disc=(D*D-A(H)**2).sqrt()
 Q=(D+disc)/2
 q=A(H)/(D+disc)
 assert A(0)<q<A(F(1,5))
 K=args.log_modes
 ell=[(A(B)/Q).log()]+[2*q**k/k for k in range(1,K+1)]
 # Exact conservative Chebyshev log tail from q<1/5.
 log_tail=F(2)*F(1,5)**(K+1)/(F(K+1)*(1-F(1,5)))
 assert log_tail<F(1,10**70)
 log_moment_tail=log_tail*F(1,8)
 # On all J5 pieces, W<3 and log(B/(B-x))/2<1.
 # Every |T_n|≤1, each length<1/8 and W+log/2<4 gives <v_rad/2
 # overcharge by v_rad/2. Also source log tail and v uncertainty.
 source_charge=v_rad/2
 assert source_charge<F(1,10**40)
 signed=[]
 for n in range(args.degree+1):
  logmom=ell[0]*J[n]
  for k in range(1,K+1):
   logmom+=ell[k]*(J[n+k]+J[abs(n-k)])/2
  pvalue=v*(W*J[n]+logmom/2)
  lo,hi=outward(pvalue)
  fee=source_charge + abs(vpair[0])*log_moment_tail/2
  lo-=fee;hi+=fee
  assert lo<=hi and hi-lo<F(1,10**25),(n,'original signed p moments unresolved')
  # Per-panel p0 is not an independent full-cell NF410 moment:
  # retain each actual interval, sum all three before NF410 comparison.
  signed.append([str(lo),str(hi)])
  if (n+1)%128==0:print('NF440 original true signed J5 p moments',n+1,'/512',flush=True)
 assert F(signed[0][1])<0
 result={
  'pass':'NF440',
  'standing':'ORIGINAL TRUE CELL5 SIGNED p CHEB MOMENTS m0..m511 AND RAW dx MOMENTS J0..J1022 SOURCE-NATIVE CERTIFIED; NO z SIGNED INTEGRAL YET',
  'original_nf407_source_sha256':sha,'original_nf406_seams_sha256':ksha,
  'original_nf407_principal_source_sha256':psha,'original_nf410_signed_taylor_parent_sha256':oldsha,
  'original_true_cell5':'(log(5)-11/10,log(7)-11/10)',
  'original_true_irrational_left_label':'-B+log(5)',
  'original_true_irrational_right_label':'-B+log(7)',
  'source_selected_plus_critical':246,'original_NF404_dyadic_center':'6677356497477490213/4611686018427387904',
  'original_active_minus_prime_powers':[2,3,4,5],'original_active_plus_prime_powers':[],
  'original_inactive_prime_powers':[7,8,9],
  'original_principal_jump_weights_active':[2,3,4,5],
  'original_principal_jump_weights_inactive':[7,8,9],
  'original_principal_jump_weight_multiplicities':{'2':1,'3':1,'4':1,'5':1},
  'original_regular_z_four_minus_and_principal_four_jump_terms_on_all_panels':True,
  'original_native_precision_bits':args.precision,
  'original_endpoint_v_source_interval':list(map(str,vpair)),
  'original_endpoint_v_uncertainty_charge_per_signed_moment':str(source_charge),
  'original_endpoint_log_Cheb_truncation_modes':K,
  'original_panel_number':args.panel,
  'original_panel_center':str(C),
  'original_panel_halfwidth':str(H),
  'original_internal_rational_cuts_not_original_seams':['31/50','73/100'],
  'original_endpoint_log_uniform_tail_exact':str(log_tail),
  'original_endpoint_log_moment_tail_exact':str(log_moment_tail),
  'original_nf410_full_true_cell5_p0_overlap_requires_all_three_panels':True,
  'original_source_signed_p_cheb_moments_n0_to_n511':signed,
  'original_cell5_raw_dx_cheb_moments_n0_to_n1022':[[str(a),str(b)] for a,b in raw],
  'original_cell5_signed_p0_negative':True,
  'number_original_signed_p_moments':len(signed),
  'number_original_raw_dx_moments':len(raw),
  'original_true_cell5_signed_pz_z2_integrated':False,
  'original_nf410_nf404_global_signed_scalar_decided':False,
  'W_ODD_NEG':'OPEN','RH':'OPEN'}
 dest=Path(args.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(result,indent=2)+'\n')
 print('NF440 source-original true cell5 signed p512 and dx1023 moments PASS, NF410 aggregate n0 control pending all panels')
 print('original signed p0',float(F(signed[0][0])),float(F(signed[0][1])),'length',float(raw_len[0]))
 print('original physical true cell5 signed z integral NOT YET evaluated')
if __name__=='__main__': main()
