#!/usr/bin/env python3
"""Authenticate and combine the completed even/odd independent source audits."""
from pathlib import Path
import json
from certify_dne39_signed_comparison import read

def run():
 rows=[]
 for par,count,old in [('even',59,47),('odd',56,44)]:
  v,_=read(f'notes/data/RPB108_DNE50_{par.upper()}_SOURCE_VALIDATION_20261010.json');assert v['status']=='PASS' and v['parity']==par and v['stage']=='DNE50';assert v['source_dimension']==count and v['reused_source_dimension']==old and v['new_native_dimension']==12
  for key in ('primary','replay'):
   s,h=read(v[key+'_path']);assert h==v[key+'_sha256'] and s['parity']==par and s['normalized_packet_sha256']==v['packet_sha256'] and s['complete_remaining_source_Gram_certified']
  assert v['new_upper_triangle_correlations']==count*(count+1)//2-old*(old+1)//2;rows.append(v)
 out=dict(stage='DNE50',status='PASS',exact_rational_checks=sum(v['exact_rational_checks'] for v in rows),rows=rows,new_upper_triangle_correlations=sum(v['new_upper_triangle_correlations'] for v in rows),complete_remaining_source_Grams_certified=True,actual_certified_all_high_retained_dimension=88,uncovered_retained_dimension=24,full_response_budget_evaluated=False,whole_aperture_positive=False,RH=False,Lean=False)
 assert out['new_upper_triangle_correlations']==1248
 Path('notes/data/RPB108_DNE50_COMPLETE_SOURCE_VALIDATION_20261010.json').write_text(json.dumps(out,indent=2)+'\n');print('PASS complete source validation combined',out['exact_rational_checks'],flush=True)
if __name__=='__main__':run()
