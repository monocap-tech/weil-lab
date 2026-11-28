#!/usr/bin/env python3
"""Qualification of exactly frozen Batch26, external integer replay, not native admission."""
import hashlib, json, re, sys, zipfile, io
from pathlib import Path
from fractions import Fraction as F
sys.set_int_max_str_digits(0)
sys.path.insert(0,str(Path('research/scripts').resolve()))
import verify_nf620_physical_key_tables as v
H=lambda b:hashlib.sha256(b).hexdigest()
def require(x,msg):
    if not x: raise ValueError(msg)
def archive(base,rec,digest):
    require(rec['status']=='BYTE_PASS' and rec['sha256']==digest,'archive receipt')
    parts=[]
    for c in rec['chunks']:
        b=(base/c['file']).read_bytes()
        require(H(b)==c['sha256'] and len(b)==c['bytes'],'chunk')
        parts.append(b)
    b=b''.join(parts); require(H(b)==digest and len(b)==rec['bytes'],'archive digest')
    z=zipfile.ZipFile(io.BytesIO(b)); require(z.testzip() is None,'CRC');return z
base=Path('historical/custody/run_46076027949-attempt_1')
rec=next(x for x in json.loads((base/'recovery.json').read_text())['records'] if x['artifact_id']==14558233793)
plan=json.loads(Path('research/notes/provisional/NF618Batch26Plan.json').read_text())
demand=json.loads(Path('research/notes/provisional/NF618W02RootAttachment/FrequencyDecomposition.json').read_text())['rows']
hold=json.loads(Path('release/notes/provisional/NF618CustodyHold.json').read_text())
require(hold['allow_native_batches_25_39'] and not hold['allow_dependent_universal_dispatch'],'scope')
ids=[i for g in plan['groups'] for i,sign in g['slots']]
parent=Path('release/notes/provisional/NF618CertifiedSlotLedgerBatch25.json').read_bytes()
require(H(parent)=='65d3a7ca4aff2ad04ffab9f5a08d6f85160e4f7c34a5320ff5a1c20c2e7441ff','parent ledger')
ledger=json.loads(parent)
require(sorted(ids)==[s['index'] for s in ledger['slots'] if s['scheduled_batch']==26 and s['certified_group'] is None],'parent residual partition')
require(plan['batch']==26 and len(ids)==len(set(ids))==120,'plan identity')
require(set(ids)=={r[0] for r in demand if r[8]==26 and r[7] is None},'demand partition')
data=[]
with archive(base,rec,'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70') as z:
    raw=z.read('manifest.json')
    require(H(raw)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7','manifest')
    m=json.loads(raw);files={r['file']:r['sha256'] for r in m['files']};chunks={}
    for i in sorted(ids):
        s=m['slots'][i]; d=demand[i]; h,f=map(F,s['key'])
        require(s['index']==d[0]==i and h==0 and 2*h==d[1] and 1408*f==d[2] and s['rows']==d[3]+1,'slot identity')
        require(d[2]==1280*d[4]+320*d[5]+d[6] and 0<=d[5]<4 and abs(d[6])<=160,'phase decomposition')
        name=s['chunk']+'.lean'
        if name not in chunks:
            b=z.read(name);require(H(b)==files[name],'chunk literal')
            chunks[name]=re.findall(r'#\[\n    (.*?)\n  \]',b.decode(),re.S)
        literal=chunks[name][s['offset']]
        nums=list(map(int,re.findall(r'\((-?\d+):ℚ\)/\(neutralNF616Q:ℚ\)',literal)))
        require(len(nums)==3*s['rows'],'row grammar')
        rows=[tuple(nums[k:k+3]) for k in range(0,len(nums),3)]
        require(literal==',\n    '.join('⟨'+','.join(f'({x}:ℚ)/(neutralNF616Q:ℚ)' for x in row)+'⟩' for row in rows),'full literal roundtrip')
        data.append((i,f,d[5],d[6],rows,H(literal.encode()),files[name]))
require(sum(len(x[4]) for x in data)==plan['rows']==537,'row count')
Q=v.Q
def reset(q):
    v.Q=q;v.ONE=(q,0);v.pi.cache_clear();v.phase_reduced.cache_clear();v.real_exp.cache_clear()
def conj(a):return a[0],v.neg(a[1])
def power(a,n,mode):
    if mode=='linear':
        r=a
        for _ in range(1,n):r=v.zmul(r,a)
        return r
    if n==1:return a
    b=power(a,n//2,mode);b=v.zmul(b,b)
    return v.zmul(b,a) if n%2 else b
def project(a,factor):
    return tuple((m//factor,v.ceildiv(r,factor)+1) for m,r in a)
def measure(z,pos,neg,rows,delta):
    require(v.Q==Q,'checker scale')
    out=[]
    for n,(x,y,R) in enumerate(rows):
        boundary=v.zadd(v.zmul(v.real(F(11,10)**n),pos),v.zneg(v.zmul(v.real(F(-11,10)**n),neg)))
        if n:
            a,b,r=rows[n-1]
            boundary=v.zadd(boundary,v.zneg(v.zmul(v.real(n),((a,0),(b,0)))))
        else:r=0
        residual=v.zadd(boundary,v.zneg(v.zmul(z,((x,0),(y,0)))))
        upper=v.upper(residual);budget=delta*R-n*r
        require(budget>0,'positive budget')
        out.append({'n':n,'upper_scaled':str(upper),'budget_scaled':str(budget),'slack_scaled':str(budget-upper),'ratio':float(F(upper)/budget),'pass':upper<=budget})
    return out
def phases(extra):
    factor=10**extra;reset(Q*factor)
    seed=v.phase(F(1,1408));quarter=(v.ZERO,v.ONE)
    powers=[v.real(1),seed]
    for k in range(2,161):powers.append(v.zmul(powers[-1],seed))
    qp=[v.real(1),quarter]
    for k in range(2,4):qp.append(v.zmul(qp[-1],quarter))
    # This matches the rounded generic phase decomposition, not an
    # unproved exact coordinate rotation. Project only once afterward.
    result={}
    for _,_,q,r,*_ in data:
        if (q,r) not in result:
            a=powers[abs(r)]
            if r<0:a=conj(a)
            result[q,r]=project(v.zmul(qp[q],a),factor) if extra else v.zmul(qp[q],a)
    reset(Q);return result
def run(label,p=None):
    results=[]
    for i,f,q,r,rows,lh,ch in data:
        z=(v.ZERO,v.mul(v.pi(),v.exact(2*f)))
        if p is None:
            pos=v.endpoint(0,f);neg=v.endpoint(0,-f)
        else:
            a=p[q,r];pos=v.zmul(v.real(1),a);neg=v.zmul(v.real(1),conj(a))
        rs=measure(z,pos,neg,rows,6*abs(f))
        results.append({'slot':i,'f':str(f),'q':q,'r':r,'literal_sha256':lh,'chunk_sha256':ch,'rows':rs})
    flat=[r for s in results for r in s['rows']]
    summary={'label':label,'table_pass':sum(all(r['pass'] for r in s['rows']) for s in results),'row_pass':sum(r['pass'] for r in flat),'max_ratio':max(r['ratio'] for r in flat),'failed_slots':[s['slot'] for s in results if not all(r['pass'] for r in s['rows'])]}
    print(json.dumps(summary),flush=True);return {'summary':summary,'slots':results}
reset(Q)
runs=[run('historical direct control')]
require(runs[0]['summary']['row_pass']==537,'original control')
for extra in (4,6,8):
    runs.append(run('shared root +'+str(extra)+' digits',phases(extra)))
    if runs[-1]['summary']['row_pass']==537:break
out=Path('evidence');out.mkdir(exist_ok=True)
(out/'qualification.json').write_text(json.dumps({'scope':'exact external Batch26 qualification only; native certification and admission not performed','plan_git_blob':'26aef7a4b21aa2985fbbd72675f16be131202a99','tables':120,'rows':537,'phase_pairs':len({(x[2],x[3]) for x in data}),'historical_head':'Batch25','runs':runs},indent=2)+'\n')
(out/'summary.json').write_text(json.dumps([r['summary'] for r in runs],indent=2)+'\n')
