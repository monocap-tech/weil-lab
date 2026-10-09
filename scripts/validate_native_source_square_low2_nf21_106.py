#!/usr/bin/env python3
"""NF21 exact rational source-square sector independent consumer.

Recomputes complete prime-plus-signed-pole physical low2 source squares
using the separately committed producer, compares original pole native
moments to the immutable E112 source, and rounds all eight entries
outward to 1e-12. Does not compute the archimedean source, full Gram D,
or P2.
"""
from fractions import Fraction as F
from pathlib import Path
import argparse,gzip,hashlib,json
from certify_native_source_square_prime_pole_nf21_106 import certificate
OLD_SHA='f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81'
PARTS=(
 'prime_only_source_square_gram_00','prime_only_source_square_gram_11',
 'pole_only_source_square_gram_00','pole_only_source_square_gram_11',
 'prime_pole_source_cross_00','prime_pole_source_cross_11',
 'prime_plus_pole_source_square_gram_00','prime_plus_pole_source_square_gram_11')
def run(e112_path):
    with gzip.open(e112_path,'rb') as f: raw=f.read()
    assert hashlib.sha256(raw).hexdigest()==OLD_SHA
    Q=json.loads(raw)['complete_form'];D=certificate();count=0
    for idx,key in [('0,0','native_pole_form_00'),('1,1','native_pole_form_11')]:
        lo,hi=map(F,D[key]);l,h=map(F,Q[idx]['poles'])
        assert max(lo,l)<=min(hi,h)
        count+=1
    rounded={}
    for key in PARTS:
        lo,hi=map(F,D[key]);g=10**12
        l=F((lo*g).__floor__(),g);h=F((hi*g).__ceil__(),g)
        assert l<=lo<=hi<=h and h-l<=F(1,g)
        rounded[key]=[str(l),str(h)];count+=1
    assert D['prime_only_source_square_gram_01']==['0','0'];count+=1
    assert D['complete_prime_plus_pole_source_gram_01']==['0','0'];count+=1
    assert D['overlapping_ordered_source_shift_pairs']==82;count+=1
    for p in ('00','11'):
        prime=list(map(F,D[f'prime_only_source_square_gram_{p}']))
        pole=list(map(F,D[f'pole_only_source_square_gram_{p}']))
        cross=list(map(F,D[f'prime_pole_source_cross_{p}']))
        combo=list(map(F,D[f'prime_plus_pole_source_square_gram_{p}']))
        assert combo[0]<=prime[1]+pole[1]+cross[1]
        assert combo[1]>=prime[0]+pole[0]+cross[0]
        assert cross[1]<0 and combo[0]>0
        count+=2
    assert all(F(x)>0 for x in rounded['prime_only_source_square_gram_00']);count+=1
    assert count==18
    return dict(status='PASS',exact_rational_checks=count,
      original_E112_sha256=OLD_SHA,
      complete_prime_pole_rounded_outward_1e12=rounded,
      archimedean_source_included=False,full_P2_built=False,
      whole_aperture_positive=False)
if __name__=='__main__':
    p=argparse.ArgumentParser()
    p.add_argument('original_E112_archive')
    p.add_argument('--output')
    a=p.parse_args()
    r=json.dumps(run(a.original_E112_archive),indent=2)+'\n'
    if a.output:Path(a.output).write_text(r)
    print(r)
