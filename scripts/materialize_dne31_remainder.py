#!/usr/bin/env python3
"""Expand the exact frozen optimized remainder into source-engine columns."""
from pathlib import Path
from fractions import Fraction as F
import argparse,base64,gzip,hashlib,json
def read(p):
    b=Path(p).read_bytes()
    if p.endswith('.gz.b64'):b=gzip.decompress(base64.b64decode(b))
    return json.loads(b),hashlib.sha256(b).hexdigest()
def run(frame_path,native_path,selected_path,out):
    frame,fh=read(frame_path);native,nh=read(native_path);selected,sh=read(selected_path)
    assert frame['parity']==native['parity']==selected['parity'] and nh==frame['input_sha256'][0] and sh==frame['input_sha256'][3]
    ids=native['retained_indices'];T=[{ids[0]:F(1)}]+[dict(zip(v['indices'],map(F,v['coefficients']))) for v in selected['columns']]
    K=[list(map(F,row)) for row in frame['frozen_original_projection_K']];columns=[]
    for j,(row,record) in enumerate(zip(native['exact_W_columns'],frame['exact_frozen_remainder_column_records'])):
        v=dict(zip(ids,map(F,row)))
        for i,t in enumerate(T):
            for n,x in t.items():v[n]=v.get(n,F(0))-x*K[i][j]
        indices=sorted(v);coeff=[v[n] for n in indices]
        assert indices==record['indices'] and sum(x*x for x in coeff)==F(record['exact_mass_squared'])
        columns.append(dict(record,coefficients=list(map(str,coeff))))
    Path(out).write_text(json.dumps(dict(stage='DNE31',parity=frame['parity'],input_sha256=[fh,nh,sh],columns=columns,complete_remaining_source_Gram_certified=False),indent=2)+'\n')
    print(frame['parity'],'52 exact remainder polynomials materialized')
if __name__=='__main__':
    p=argparse.ArgumentParser()
    for key in ['frame','native','selected','output']:p.add_argument(key)
    a=p.parse_args();run(a.frame,a.native,a.selected,a.output)
