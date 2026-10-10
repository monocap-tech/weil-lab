#!/usr/bin/env python3
"""Certify a route ceiling and exact high trial geometry; no inverse evaluated."""
from pathlib import Path
from fractions import Fraction as F
import argparse,json
from certify_dne39_signed_comparison import read,positive,matrix
from validate_dne43_high_floor import logarithm
from materialize_dne44_joint_sources import run as materialize
from certify_dne44_joint_source_Gram import root
PARENT='61b896309a4c426a9259290b92dbd039a26f96ef'
def run(output):
 paths=['notes/data/RPB108_DNE45_SCALAR_ROUTE_LIMIT_20261010.json.gz.b64','notes/data/RPB108_DNE45_SCALAR_ROUTE_VALIDATION_20261010.json','notes/data/RPB108_DNE46_POSITIVE_SUBSPACE_VALIDATION_20261010.json','notes/data/RPB108_DNE44_EVEN_JOINT_SOURCE_REPLAY_20261010.json.gz.b64'];inp=[read(p) for p in paths];c,a,current,s=[x for x,_ in inp];assert a['status']==current['status']=='PASS' and a['certificate_sha256']==inp[0][1];assert next(r for r in current['rows'] if r['parity']=='even')['input_sha256'][0]==inp[3][1]
 A=F(53,50);pi_lo=F(314159,100000);top=F(169,10);assert (2*A*pi_lo*top)**2>112*113
 lg=logarithm(top);r=F(c['prime_norm_lower']);ceiling=lg[1]-r;target=F(next(x for x in c['rows'] if x['parity']=='even')['critical_uniform_floor_lower']);assert ceiling<target
 pp=output+'.packet';materialize(s['certificate_path'],pp);packet,ph=read(pp);Path(pp).unlink();assert ph==s['normalized_packet_sha256'];cols=[]
 for i in range(1,4):
  p=packet['columns'][i];pairs=[(n,F(v)) for n,v in zip(p['indices'],p['coefficients']) if n>=112 and F(v)];mass=sum(v*v for _,v in pairs);assert mass>0;scale=root(mass);values=[v/scale for _,v in pairs];m=sum(v*v for v in values);assert 0<m<1
  cols.append(dict(parent_packet_column=i,indices=[n for n,_ in pairs],coefficients=list(map(str,values)),original_high_mass_squared=str(mass),rational_normalization=str(scale),exact_mass_squared=str(m)))
 raw=[dict(zip(c['indices'],map(F,c['coefficients']))) for c in cols];Gram=[[sum(row.get(n,F(0))*other.get(n,F(0)) for n in set(row)|set(other)) for other in raw] for row in raw];pc=positive(matrix([[[str(x),str(x)] for x in row] for row in Gram]));assert pc
 out=dict(stage='DNE47',parent=PARENT,parity='even',input_paths=paths,input_sha256=[h for _,h in inp],aperture=str(A),retained_cutoff=112,pi_lower=str(pi_lo),universal_positive_region_top_upper=str(top),top_log_interval=list(map(str,lg)),prime_norm_lower=str(r),positive_region_shell_route_ceiling_upper=str(ceiling),full_even_packet_threshold_lower=str(target),remaining_even_packet_cannot_close_by_positive_region_shell_route=True,normalized_packet_sha256=ph,physical_high_trial_columns=cols,physical_trial_Gram=[[list(map(str,(x,x))) for x in row] for row in Gram],physical_trial_positive_certificate=pc,physical_high_trial_dimension=3,current_original_high_floor='647/1000',actual_certified_retained_dimension=87,uncovered_retained_dimension=25,required_new_projected_source_correlations=138,trial_native_energy_certified=False,trial_source_Gram_certified=False,response_upper_established=False,source_integrals_recomputed=False,true_high_inverse_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 Path(output).write_text(json.dumps(out,indent=2)+'\n');print('route ceiling',float(ceiling),'even threshold',float(target),'high trial dimension',3,flush=True)
if __name__=='__main__':
 ap=argparse.ArgumentParser();ap.add_argument('--output',required=True);run(ap.parse_args().output)
