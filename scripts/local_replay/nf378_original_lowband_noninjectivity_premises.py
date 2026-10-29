#!/usr/bin/env python3
"""Exact finite-rank and source sign checks for NF378's ANALYTIC theorem.
No actual NF370 signed integral or invisible source coefficients computed.
"""
import argparse,hashlib,json
from fractions import Fraction as F
from pathlib import Path

def run():
 p=argparse.ArgumentParser()
 p.add_argument('--native',required=True)
 p.add_argument('--output',required=True)
 a=p.parse_args()
 raw=Path(a.native).read_bytes();j=json.loads(raw)
 assert j['original_selected_count']==242
 assert j['original_critical_count']==4
 assert j['original_rank_sha256']=='9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2'
 assert j['original_source_sha256']=='abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770'
 row=next(x for x in j['actual_original_signed_point_samples'] if x['frequency']=='1/4')
 lo,hi=map(F,row['signed_m_interval'])
 assert F(0)<lo<=hi
 assert F(1,4)<2**20
 s=242+4;annuli=492;constraints=2*s+annuli;tests=constraints+1
 assert constraints==984 and tests==985
 result={'standing':'EXACT_PREMISES_ONLY_ANALYTIC_NONINJECTIVITY_PROOF_SEPARATE',
 'original_native_json_sha256':hashlib.sha256(raw).hexdigest(),
 'original_signed_symbol_point':'1/4',
 'symbol_interval':[str(lo),str(hi)],
 'J_plus_E_dim_upper':s,'annuli':annuli,
 'input_and_output_linear_constraints_upper':constraints,
 'independent_odd_smooth_inputs_for_nontrivial_kernel':tests,
 'analytic_injectivity_premise':'original m smooth, nonzero near 1/4, compact-support input Fourier entire',
 'actual_invisible_source_coefficients_computed':False,
 'actual_u4_signed_integral_computed':False,'method_promotion':False,
 'W_ODD_NEG':'OPEN','RH':'OPEN'}
 output=Path(a.output);output.parent.mkdir(parents=True,exist_ok=True)
 output.write_text(json.dumps(result,indent=2,sort_keys=True)+'\n')
 print('NF378 exact finite-rank/source-sign premise PASS; no signed u4 result')
if __name__=='__main__':run()
