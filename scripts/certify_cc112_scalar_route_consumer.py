#!/usr/bin/env python3
"""Authenticate DNE45 and freshly pay its packet thresholds and ceiling trials."""
from pathlib import Path
from fractions import Fraction as F
import json,argparse,hashlib
import validate_cc105_selected_response as data
import certify_cc81_boundary_response_consumer as c
import certify_cc88_correlated_seventh_response as r
import certify_cc101_next_source_packet as proof
BASE=Path(__file__).resolve().parents[1];ROOT='notes/cc112-source/'
def run():
 checks=0;rows=[]
 def check(v):
  nonlocal checks
  assert v;checks+=1
 for x in json.loads((BASE/ROOT/'input_custody.json').read_text())['files']:check(hashlib.sha256((BASE/ROOT/x['path']).read_bytes()).hexdigest()==x['stored_sha256'])
 cert,ch,_=data.read(ROOT+'notes/data/RPB108_DNE45_SCALAR_ROUTE_LIMIT_20261010.json.gz.b64');audit,ah,_=data.read(ROOT+'notes/data/RPB108_DNE45_SCALAR_ROUTE_VALIDATION_20261010.json');check(audit['status']=='PASS' and audit['certificate_sha256']==ch)
 for p,h in zip(cert['input_paths'],cert['input_sha256']):check(data.read(('notes/cc109-source/' if 'DNE43' in p else 'notes/cc110-source/')+p)[1]==h)
 num=c.iv(cert['prime_Rayleigh_numerator']);den=c.iv(cert['prime_Rayleigh_denominator']);ray=F(cert['prime_Rayleigh_lower']);prime=F(cert['prime_norm_lower']);alpha=F(cert['fixed_arch_input']);ceiling=F(cert['scalar_route_ceiling']);check(num[0]>0 and den[0]>0 and ray==num[0]/den[1] and 0<prime<ray);check(alpha==F(2772351243732,10**12) and ceiling==alpha-prime)
 for row in cert['rows']:
  s,ss,_=data.read('notes/cc110-source/'+row['source_path']);prior,ps,_=data.read('notes/cc110-source/'+row['prior_certificate_path']);check(ss==row['source_sha256'] and ps==row['prior_certificate_sha256'])
  Q=c.matrix(s['native_block']);G=c.matrix(s['original_projected_source_Gram']);v=list(map(F,row['exact_trial']));q=c.quad(Q,v);g=c.quad(G,v);check(q[0]>0 and g[0]>0)
  sq=c.iv(row['trial_native_energy']);sg=c.iv(row['trial_source_energy']);check(sq[0]<=q[0]<=q[1]<=sq[1] and sg[0]<=g[0]<=g[1]<=sg[1])
  low=g[0]/q[1];upper=F(row['critical_uniform_floor_upper']);check(sg[0]/sq[1]==F(row['critical_uniform_floor_lower'])<=low and ceiling<low<upper)
  d,pc=proof.proof(r.sub(r.scale(Q,upper),G),row['full_packet_target_certificate']['exact_congruence_U']);check(d>0)
  budget=c.sub(c.mul(c.iv(ceiling),q),g);check(budget[1]<0)
  rows.append(dict(parity=row['parity'],critical_uniform_floor_lower=str(low),critical_uniform_floor_upper=str(upper),fresh_target_positive_proof=pc,fresh_ceiling_trial_budget=c.pair(budget),fixed_arch_input_improvement_necessary_lower=str(low-ceiling)))
 return dict(milestone='CC112',status='PASS',exact_consumer_checks=checks,DNE45_certificate_sha256=ch,DNE45_validation_sha256=ah,prime_norm_lower=str(prime),fixed_arch_input=str(alpha),fixed_input_scalar_route_ceiling=str(ceiling),Rayleigh_integral_band_validation_inherited=True,band_integrals_recomputed=False,parity_checks=rows,fixed_input_global_prime_norm_route_cannot_close_either_full_packet=True,actual_high_floor_upper_bound_claimed=False,original_high_floor='603/1000',integrated_retained_rank=85,uncovered_retained_dimension=27,whole_aperture_positive=False,RH=False,F4=False,Lean=False)
if __name__=='__main__':
 p=argparse.ArgumentParser();p.add_argument('--output',required=True);a=p.parse_args();Path(a.output).write_text(json.dumps(run(),indent=2)+'\n')
