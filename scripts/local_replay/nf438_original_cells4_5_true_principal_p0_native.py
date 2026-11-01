#!/usr/bin/env python3
"""NF438 native original principal p zeroth-moment controls cells 4 and 5.

Source exactly NF407 q+r with r jump thresholds (not u4 translate
multiplicities). Native 2048-bit Arb analytic primitive for original
logarithmic q term at genuine NF406 irrational endpoints. Cross-check
with independent accepted original NF410 cell-4/5 m0 source moments.
"""
import argparse,hashlib,json,sys
from fractions import Fraction as F
from pathlib import Path
from flint import arb,ctx
if hasattr(sys,"set_int_max_str_digits"):sys.set_int_max_str_digits(0)
B=F(11,10)
SOURCE_SHA="0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce"
SEAM_SHA="c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675"
CONFIG={
 4:{"L":lambda A:A(B)-A(2).log(),"R":lambda A:A(5).log()-A(B),"jump":[2,3,4],"left":"B-log(2)","right":"-B+log(5)"},
 5:{"L":lambda A:A(5).log()-A(B),"R":lambda A:A(7).log()-A(B),"jump":[2,3,4,5],"left":"-B+log(5)","right":"-B+log(7)"}}
BASE={2:2,3:3,4:2,5:5}
def read(path):
 raw=Path(path).read_bytes();return json.loads(raw),hashlib.sha256(raw).hexdigest()
def A(x):return arb(str(x))
def encl(z,digits=75):
 m,r,e=z.mid_rad_10exp(digits);f=F(10)**int(e)
 return F(int(m)-int(r))*f,F(int(m)+int(r))*f
def overlap(x,y):return x[0]<=y[1] and y[0]<=x[1]
def primitive(x):
 # Integral of log(B/(B-x)) dx = x+(B-x)*log((B-x)/B).
 d=A(B)-x;assert d>0
 return x+d*(d/A(B)).log()
def main():
 ap=argparse.ArgumentParser()
 ap.add_argument('--source',default='notes/data/provisional/NF407_original_fourth_physical_coefficients_native.json')
 ap.add_argument('--seams',default='notes/data/provisional/NF406_original_prime_support_partition_exact.json')
 ap.add_argument('--principal',default='notes/data/provisional/NF407_original_prime_jump_log_power_exact.json')
 ap.add_argument('--nf410',default='notes/data/provisional/NF410_original_signed_taylor_moments.json')
 ap.add_argument('--precision',type=int,default=2048)
 ap.add_argument('--output',required=True)
 a=ap.parse_args();assert a.precision>=1024;ctx.prec=a.precision
 s,sha=read(a.source);seams,ksha=read(a.seams)
 principal,psha=read(a.principal);old,oldsha=read(a.nf410)
 assert sha==SOURCE_SHA and ksha==SEAM_SHA
 assert s['original_dimension']==242 and len(s['original_exact_native_original_four_critical_coefficients_mid_radius'])==4
 assert principal['original_nf406_seams_sha256']==ksha
 assert old['original_nf406_source_sha256']==ksha and old['original_nf407_source_sha256']==psha
 assert all(x['W_ODD_NEG']==x['RH']=='OPEN' for x in (s,seams,principal,old))
 vpair=tuple(map(F,principal['original_source_u4_endpoint_interval']))
 assert vpair[0]<vpair[1]<0
 vmid=sum(vpair)/2;vrad=(vpair[1]-vpair[0])/2
 knots=seams['certified_ordered_knots'];cells=old['original_positive_original_physical_cells']
 out={"pass":"NF438","standing":"ORIGINAL PRINCIPAL p0 MOMENTS TRUE PHYSICAL CELLS4/5 SOURCE-NATIVE AND INDEPENDENT NF410 OVERLAP; COMPLETE SIGNED z OPEN",
  "source_sha256":sha,"seams_sha256":ksha,
  "principal_sha256":psha,"original_NF410_parent_sha256":oldsha,
  "original_principal_endpoint_v_interval":list(map(str,vpair)),
  "original_native_precision_bits":a.precision,"cells":{},"W_ODD_NEG":"OPEN","RH":"OPEN"}
 for n,g in CONFIG.items():
  oldcell=cells[n-1]
  assert oldcell['cell']==n and (oldcell['left_label'],oldcell['right_label'])==(g['left'],g['right'])
  assert knots[n+7]['label']==g['left'] and knots[n+8]['label']==g['right']
  L,R=g['L'](A),g['R'](A)
  assert 0<L<R<A(B)
  W=sum((A(BASE[j]).log()/A(j).sqrt() for j in g['jump']),arb(0))
  assert 0<W<A(4)
  l=R-L
  native=A(vmid)*(W*l+(primitive(R)-primitive(L))/2)
  x,y=encl(native)
  # On x∈[0,B) log(B/(B-x))<3 for cells4/5, W<4,
  # length<1/2; hence v midpoint error <(4+1.5)*.5*vrad<3vrad.
  assert l<A(F(1,2))
  fee=3*vrad
  x-=fee;y+=fee
  prior=tuple(map(F,oldcell['signed_original_p_moments_by_degree_0_to_3'][0]))
  assert overlap((x,y),prior),('original NF410 m0 mismatch',n,float(x),float(prior[0]))
  assert y<0 and y-x<F(1,10**30)
  out['cells'][str(n)]={
    "true_left_label":g['left'],"true_right_label":g['right'],
    "original_active_principal_jump_prime_powers":g['jump'],
    "original_inactive_principal_jump_prime_powers":[j for j in (2,3,4,5,7,8,9) if j not in g['jump']],
    "independent_original_NF410_p0_interval":[str(z) for z in prior],
    "original_true_principal_p0_interval":[str(x),str(y)],
    "original_signed_principal_p0_negative":True,
    "original_NF410_independent_original_p0_overlap":True,
    "original_true_cell_signed_pz_z2_integrated":False}
  print('NF438 original cell',n,'principal p0',float(x),float(y),'overlap NF410 PASS',flush=True)
 dest=Path(a.output);dest.parent.mkdir(parents=True,exist_ok=True)
 dest.write_text(json.dumps(out,indent=2)+'\\n'.replace('\\n','\n'))
 print('NF438 original p0 both cells source-native PASS; whole cells signed integrals OPEN')
if __name__=='__main__':main()
