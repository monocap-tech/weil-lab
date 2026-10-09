#!/usr/bin/env python3
"""NF16 complete signed E96 finite positivity from exact rational E80+new rows.
Validates 2352 source entries, 9408 arch/prime/pole/full enclosures,
48 even and 48 odd exact shifted pivots. NO whole a=53/50 sign.
"""
import argparse,gzip,json,hashlib
from fractions import Fraction as F
from pathlib import Path
ORIGINAL_80_SHA='9188d9b48525c1e1af41292e3bfe8d3004470e03b00520428d9d5b0cc76a8513'
NEW_96_SHA='aff17c786d41287f077680f412e4b2c14d59fdebacbaf11272d23033aee6e3ac'
def read(path):
 with gzip.open(path,"rb") if str(path).endswith('.gz') else open(path,"rb") as f: raw=f.read()
 return raw,json.loads(raw)
def verify(new96,old80):
 raw,d=read(new96);prior,old=read(old80)
 assert hashlib.sha256(raw).hexdigest()==NEW_96_SHA
 assert hashlib.sha256(prior).hexdigest()==ORIGINAL_80_SHA
 assert d['aperture']=='53/50' and d['dim']==96 and d['N']==600 and d['K']==520
 assert len(d['complete_form'])==2352 and len(old['complete_form'])==1640
 entries=d['complete_form']
 assert all(entries[k]==v for k,v in old['complete_form'].items())
 assert len(entries)-len(old['complete_form'])==712
 n=96;g=10**43;matrix=[[F(0)]*n for _ in range(n)]
 eps=F(0);width=F(0);count=0
 for key,parts in entries.items():
  i,j=map(int,key.split(','));assert i<=j and (i+j)%2==0
  assert set(parts)=={'arch','prime','poles','full'}
  for kind in ('arch','prime','poles','full'):
   lo,hi=map(F,parts[kind]);assert lo<=hi;count+=1
  lo,hi=map(F,parts['full'])
  assert lo<=sum(F(parts[c][1]) for c in ('arch','prime','poles'))
  assert hi>=sum(F(parts[c][0]) for c in ('arch','prime','poles'))
  center=F((((lo+hi)/2)*g).__floor__(),g)
  eps=max(eps,abs(center-lo),abs(center-hi))
  width=max(width,hi-lo)
  matrix[i][j]=matrix[j][i]=center
 assert count==9408
 assert all(matrix[i][j]==matrix[j][i] for i in range(n) for j in range(n))
 assert all(matrix[i][j]==0 for i in range(n) for j in range(n) if (i+j)%2)
 eta=n*eps;shift=F(1,10**35)
 assert eta<F(1,10**39)
 pivots={}
 for parity in (0,1):
  ids=list(range(parity,n,2));B=[
   [matrix[i][j]-(shift if i==j else 0) for j in ids] for i in ids]
  for k in range(len(ids)):
   p=B[k][k];assert p>0,(parity,k,'INCONCLUSIVE')
   for i in range(k+1,len(ids)):
    for j in range(i,len(ids)):
     B[i][j]=B[j][i]=B[i][j]-B[i][k]*B[k][j]/p
  pivots['even' if parity==0 else 'odd']=48
 assert shift-eta>F(9,10**36)
 return dict(status='PASS',aperture='53/50',
  E96_original_source_sha256=NEW_96_SHA,
  E80_original_source_sha256=ORIGINAL_80_SHA,
  native_entries=len(entries),new_native_entries=712,
  signed_component_interval_checks=count,
  max_entry_width=str(width),whole_symmetric_error_upper=str(eta),
  exact_positive_shifted_parity_pivots=pivots,
  strict_original_native_E96_physical_lower='9/10^36',
  full_E112_native_matrix=False,full_corrected_Schur=False,
  whole_original_aperture_positive=False,Lean_certified=False)
if __name__=='__main__':
 p=argparse.ArgumentParser()
 p.add_argument('new96_json_gz')
 p.add_argument('old80_json_gz')
 a=p.parse_args()
 print(json.dumps(verify(a.new96_json_gz,a.old80_json_gz),indent=2))
