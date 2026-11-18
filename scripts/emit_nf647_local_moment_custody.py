#!/usr/bin/env python3
"""Use three retained integer table proposals and exact indexed endpoint values.
Check their original cache identity independently with only four local lookups.
Emit a conditional moment-soundness theorem per key; the endpoint leaves and
pi equality must be supplied by their own certificates.
"""
import argparse,gzip,hashlib,json,re
from pathlib import Path
from fractions import Fraction as F
from emit_nf627_original_moment_bank import filetext
from verify_nf620_physical_key_tables import exact,mul,zmul,reduced
BASE='WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLocalMomentCustody'
BANK='WeilDefect.Generated.NF635.Banks'
OPT='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
def sha(p): return hashlib.sha256(p.read_bytes()).hexdigest()
def main():
    ap=argparse.ArgumentParser()
    for k in ('tables','bank','output'): ap.add_argument('--'+k,type=Path,required=True)
    a=ap.parse_args(); a.output.mkdir(parents=True,exist_ok=True)
    tm=json.loads((a.tables/'manifest.json').read_text())
    bm=json.loads((a.bank/'manifest.json').read_text())
    assert tm['schema']=='NF638-integer-table-pilots-v1'
    assert bm['full_values'] and (bm['real_count'],bm['phase_count'])==(5,1276)
    for d,m in [(a.tables,tm),(a.bank,bm)]:
        for x in m['files']: assert sha(d/x['file'])==x['sha256']
    assert sha(a.tables/'Join.lean')==tm['join_sha256']
    assert tm['input_sha256']==bm['input_sha256']
    with gzip.open(a.bank/'endpoints.json.gz','rt') as f: b=json.load(f)
    assert b['schema']=='NF635-original-shared-endpoints-v1' and b['scale']=='10^2600'
    p=tuple(map(int,b['pi']))
    def inventory(label):
        return {F(k):(i,tuple(tuple(map(int,x)) for x in v))
                for i,(k,v) in enumerate(b[label])}
    R,P=inventory('real'),inventory('phase')
    out=[]; routes=[]
    for rec in tm['files']:
        label=rec['file'].removesuffix('.lean'); v='nf638'+label
        h,f=map(F,rec['key'])
        r0,R0=R[h]; r1,R1=R[-h]
        u0,u1=reduced(f),reduced(-f)
        p0,P0=P[u0]; p1,P1=P[u1]
        cache=( (exact(h),mul(p,exact(2*f))), zmul(R0,P0), zmul(R1,P1) )
        line=next(x for x in (a.tables/rec['file']).read_text().splitlines() if x.startswith('def '+v+' : NF638Table :='))
        # First two integer coordinates are denominator numerator/denominator only
        # if explicitly annotated; the cache is the twelve explicitly typed integers.
        coords=list(map(int,re.findall(r'\((-?\d+):ℤ\)',line)))
        assert coords==[x for c in cache for z in c for x in z], (label,'cache mismatch')
        routes.append({'label':label,'key':rec['key'],'real':[r0,r1],'phase':[p0,p1],
                       'rows':rec['rows']})
        name='nf647'+label
        body=f'''theorem {name}CacheCheck : neutralNF647CacheCheck {v}.cache nf635Pi
    nf635RealBank nf635PhaseBank {v}.key=true := by
  decide +kernel

theorem {name}Moment
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=nf635Pi)
    (hr : nf635RealBank.lookup {v}.key.h=neutralNF635RealRef {v}.key.h)
    (hrn : nf635RealBank.lookup (-{v}.key.h)=neutralNF635RealRef (-{v}.key.h))
    (hp : nf635PhaseBank.lookup (neutralNF592Reduced {v}.key.f)=
      neutralNF635PhaseRef nf635Pi (neutralNF592Reduced {v}.key.f))
    (hpn : nf635PhaseBank.lookup (neutralNF592Reduced (-{v}.key.f))=
      neutralNF635PhaseRef nf635Pi (neutralNF592Reduced (-{v}.key.f)))
    (n : ℕ) (hn : n < ({v}.keyTable neutralNF616Q).rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) {v}.key.value n-
      (neutralNF617MomentRead ({v}.keyTable neutralNF616Q).rows n).value‖ ≤
      (neutralNF617MomentRead ({v}.keyTable neutralNF616Q).rows n).rad :=
  neutralNF647Moment_of_local {v} nf635Pi nf635RealBank nf635PhaseBank
    hpi {name}CacheCheck hr hrn hp hpn {v}Check n hn

#print axioms {name}CacheCheck
#print axioms {name}Moment
'''
        path=a.output/(label+'.lean')
        path.write_text(filetext([BASE,BANK,'WeilDefect.Generated.NF638.'+label],OPT+body))
        out.append({'file':path.name,'sha256':sha(path)})
    assert sum(x['rows'] for x in routes)==42 and len(routes)==3
    (a.output/'manifest.json').write_text(json.dumps({'schema':'NF647-local-cache-proposals-v1',
       'table_manifest_sha256':sha(a.tables/'manifest.json'),'bank_manifest_sha256':sha(a.bank/'manifest.json'),
       'routes':routes,'files':out,'scope':'exact retained local cache comparison proposals; local endpoint and pi identities remain premises'},indent=2)+'\n')
    print('NF647 three retained cache matches, 42 original rows; local soundness proposals emitted')
if __name__=='__main__': main()
