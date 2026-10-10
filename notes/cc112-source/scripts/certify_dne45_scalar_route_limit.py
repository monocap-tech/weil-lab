#!/usr/bin/env python3
"""Rational certificates for the fixed-input global-norm route obstruction."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,json
import numpy as np
from certify_dne39_signed_comparison import read,matrix,quadratic,positive
from certify_dne32_native_remainder import I
from validate_dne43_high_floor import position,add,mul,exact
PARENT='bb7220c07aa66c2fea00bbc36452a59130ee3fb1'
def save(out,path):
 b=(json.dumps(out,indent=2)+'\n').encode()
 Path(path).write_bytes(base64.b64encode(gzip.compress(b,mtime=0))+b'\n' if path.endswith('.gz.b64') else b)
def run(output):
 paths=['notes/data/RPB108_DNE43_PRIME_SCHUR_REPLAY_20261010.json.gz.b64','notes/data/RPB108_DNE43_HIGH_FLOOR_VALIDATION_20261010.json','notes/data/RPB108_DNE44_POSITIVE_SUBSPACE_VALIDATION_20261010.json']
 inp=[read(p) for p in paths];p,h,a=[x for x,_ in inp]
 assert h['status']==a['status']=='PASS'
 assert next(r for r in h['rows'] if r['path']==paths[0])['sha256']==inp[0][1]
 num=exact(0);den=exact(0)
 for row in p['rows']:
  left=position((row['left'][0],F(row['left'][1])));right=position((row['right'][0],F(row['right'][1])))
  length=(right[0]-left[1],right[1]-left[0]);assert length[0]>0
  w=tuple(map(F,row['weight']));pw=tuple(map(F,row['prime_weight']));assert w[0]>0 and pw[0]>0
  num=add(num,mul(length,mul(w,pw)));den=add(den,mul(length,mul(w,w)))
 ray=num[0]/den[1];assert ray>0
 # Round down to a convenient, strictly weaker rational for the stated ceiling.
 r=F((ray*10**8).__floor__(),10**8);assert 0<r<ray
 alpha=F(p['inherited_arch_minus_pole_strict_lower']);assert alpha==F(2772351243732,10**12)
 ceiling=alpha-r;rows=[]
 print('prime lower',float(r),'route ceiling',float(ceiling),flush=True)
 for parity in ('even','odd'):
  sp=f'notes/data/RPB108_DNE44_{parity.upper()}_JOINT_SOURCE_REPLAY_20261010.json.gz.b64'
  cp=f'notes/data/RPB108_DNE44_{parity.upper()}_POSITIVE_SUBSPACE_20261010.json.gz.b64'
  s,sh=read(sp);c,ch=read(cp);ar=next(x for x in a['rows'] if x['parity']==parity)
  assert ar['certificate_sha256']==ch and ar['input_sha256'][0]==sh
  N=matrix(s['native_block']);G=matrix(s['original_projected_source_Gram'])
  nm=np.array([[float((x.l+x.h)/2) for x in row] for row in N]);gm=np.array([[float((x.l+x.h)/2) for x in row] for row in G]);li=np.linalg.inv(np.linalg.cholesky(nm));rr=li@gm@li.T;_,vv=np.linalg.eigh((rr+rr.T)/2)
  v=[F(round(float(x)*10**20),10**20) for x in li.T@vv[:,-1]]
  q=quadratic(N,v);g=quadratic(G,v);assert q.l>0 and g.l>0
  lo=g.l/q.h;hi=F((lo*10**8).__ceil__(),10**8)
  for tick in range(3):
   cert=positive([[I(hi)*x-y for x,y in zip(nr,gr)] for nr,gr in zip(N,G)])
   if cert is not None:break
   hi+=F(1,10**8)
  assert cert is not None and 0<hi-lo<=F(3,10**8) and lo>ceiling
  budget=I(ceiling)*q-g;assert budget.h<0
  rows.append(dict(parity=parity,source_path=sp,source_sha256=sh,prior_certificate_path=cp,prior_certificate_sha256=ch,packet_dimension=44,exact_trial=list(map(str,v)),trial_native_energy=q.box(),trial_source_energy=g.box(),critical_uniform_floor_lower=str(lo),critical_uniform_floor_upper=str(hi),target_bracket_width=str(hi-lo),full_packet_target_certificate=cert,ceiling_trial_budget=budget.box(),fixed_arch_input_improvement_necessary_lower=str(lo+r-alpha)))
  print(parity,'threshold',float(lo),float(hi),'route obstruction',float(lo-ceiling),flush=True)
 out=dict(stage='DNE45',parent=PARENT,input_paths=paths,input_sha256=[x[1] for x in inp],weight='P^17 1',band_count=len(p['rows']),prime_Rayleigh_numerator=list(map(str,num)),prime_Rayleigh_denominator=list(map(str,den)),prime_Rayleigh_lower=str(ray),prime_norm_lower=str(r),fixed_arch_input=str(alpha),scalar_route_ceiling=str(ceiling),rows=rows,fixed_input_global_norm_route_cannot_close_full_packet=True,current_original_high_floor='603/1000',actual_certified_retained_dimension=85,uncovered_retained_dimension=27,source_integrals_recomputed=False,target_high_floor_established=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 save(out,output)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);run(ap.parse_args().output)
