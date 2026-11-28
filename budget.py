#!/usr/bin/env python3
"""External integer replay of original slot 99, not native proof."""
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
with archive(base,rec,'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70') as z:
    raw=z.read('manifest.json')
    require(H(raw)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7','manifest')
    m=json.loads(raw); s=m['slots'][99]
    require(s['index']==99 and list(map(F,s['key']))==[F(0),F(7,704)] and s['rows']==4,'key')
    name=s['chunk']+'.lean';b=z.read(name)
    require(H(b)==next(x['sha256'] for x in m['files'] if x['file']==name),'chunk literal')
    literal=re.findall(r'#\[\n    (.*?)\n  \]',b.decode(),re.S)[s['offset']]
    nums=list(map(int,re.findall(r'\((-?\d+):ℚ\)/\(neutralNF616Q:ℚ\)',literal)))
    require(len(nums)==12,'literal row grammar')
    rows=[tuple(nums[i:i+3]) for i in range(0,12,3)]
    require(literal==',\n    '.join('⟨'+','.join(f'({x}:ℚ)/(neutralNF616Q:ℚ)' for x in row)+'⟩' for row in rows),'full literal roundtrip')
Q=v.Q; f=F(7,704); delta=6*f
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
def measure(label,z,pos,neg):
    require(v.Q==Q,'checker scale')
    out=[]
    for n,(x,y,R) in enumerate(rows):
        boundary=v.zadd(v.zmul(v.real(F(11,10)**n),pos),v.zneg(v.zmul(v.real(F(-11,10)**n),neg)))
        if n:
            a,b,r=rows[n-1]
            boundary=v.zadd(boundary,v.zneg(v.zmul(v.real(n),((a,0),(b,0)))))
        else:r=0
        res=v.zadd(boundary,v.zneg(v.zmul(z,((x,0),(y,0)))))
        upper=v.upper(res)
        budget=delta*R-n*r
        out.append({'row':n,'upper_scaled':str(upper),'budget_scaled':str(budget),'slack_scaled':str(budget-upper),'upper_over_budget':float(F(upper)/budget) if budget>0 else None,'pass':upper<=budget,'residual':[[str(i) for i in c] for c in res]})
    print(label,[r['pass'] for r in out], 'ratios',[r['upper_over_budget'] for r in out],flush=True)
    return {'label':label,'rows':out,'endpoint_radius_scaled':[[str(c[1]) for c in e] for e in (pos,neg)]}
reset(Q)
z=(v.ZERO,v.mul(v.pi(),v.exact(2*f)))
direct=measure('historical direct endpoints',z,v.endpoint(0,f),v.endpoint(0,-f))
regen=v.table(F(0),f,3)
print('Frozen rows exactly reproduced by historical generator:',regen==rows,flush=True)
results=[direct]
for mode in ('linear','binary'):
    reset(Q)
    a=power(v.phase(F(1,1408)),14,mode)
    results.append(measure('shared root '+mode+' original scale',z,v.zmul(v.real(1),a),v.zmul(v.real(1),conj(a))))
    for extra in (2,4,8,16):
        factor=10**extra
        reset(Q*factor)
        a=power(v.phase(F(1,1408)),14,mode)
        a=project(a,factor)
        reset(Q)
        results.append(measure(f'shared root {mode} +{extra} decimal digits, projected',z,v.zmul(v.real(1),a),v.zmul(v.real(1),conj(a))))
require([x['pass'] for x in results[1]['rows']]==[False]*4,'does not reproduce native diagnostic; inspect inputs before use')
out=Path('evidence');out.mkdir(exist_ok=True)
(out/'budget.json').write_text(json.dumps({'scope':'external integer residual replay; no native theorem, no new admission','slot':99,'key':['0','7/704'],'literal_sha256':H(literal.encode()),'chunk_sha256':H(b) if isinstance(b,bytes) else next(x['sha256'] for x in m['files'] if x['file']==name),'original_rows':[[str(x) for x in r] for r in rows],'regenerated_rows_equal':regen==rows,'scale':'10^2600','delta':str(delta),'results':results},indent=2)+'\n')
