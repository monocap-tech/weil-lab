"""Fail closed on a deployment plan before fetching dependencies or installing Lean."""
import hashlib,json,re,sys
from pathlib import Path
from fractions import Fraction as F

def check(index, plan):
    x=json.loads(index.read_bytes())
    assert x['schema']=='NF618-deployment-index-v1'
    assert x['columns']==['batch','git_blob','tables','rows','modules','audit_targets','repair_count','reflexivity_count','audit_module']
    rows=x['batches'];assert [r[0] for r in rows]==list(range(40))
    assert [sum(r[i] for r in rows) for i in range(2,8)]==[4443,22879,8541,23508,1998,27]
    raw=plan.read_bytes();p=json.loads(raw);i=p['batch'];assert isinstance(i,int) and 0<=i<40
    r=rows[i];h=hashlib.sha1(b'blob '+str(len(raw)).encode()+b'\0'+raw).hexdigest()
    assert h==r[1],('Git blob mismatch',i,h,r[1])
    groups=p['groups'];slots=[];tags=[];phases=[]
    for g in groups:
        f=F(g['family']);assert 0<f<F(1,2)
        ps={F(q[0]) for q in g['phases']};assert len(ps)==len(g['phases']) and ps<={f,-f}
        for v,tag,digest in g['phases']:
            assert re.fullmatch(r'Phase\d{4}',tag) and re.fullmatch(r'[0-9a-f]{64}',digest)
            phases.append(F(v));tags.append(tag)
        for slot,sign in g['slots']:
            assert type(slot)==int and 0<=slot<7835 and sign in (-1,0,1)
            assert ({f,-f}<=ps if sign==0 else sign*f in ps)
            slots.append(slot)
    assert len(slots)==len(set(slots))==r[2]
    assert len(tags)==len(set(tags))==len(set(phases))
    assert [p[k] for k in ('rows','modules','audit_targets','repair_count','reflexivity_count','audit_module')]==r[3:]
    assert all(re.fullmatch(r'[0-9a-f]{64}',p[k]) for k in ('row_fingerprint','source_fingerprint','normalized_fingerprint','reflexive_fingerprint'))
    assert p['modules']==len(slots)+7*len(tags)+2
    assert p['audit_targets']==5*len(slots)+2*len(tags)+3+sum(s==0 for g in groups for _,s in g['slots'])
    return {'batch':i,'git_blob':h,'tables':len(slots),'phases':len(tags),'modules':p['modules'],'audit_targets':p['audit_targets']}
if __name__=='__main__':
    assert len(sys.argv)==3
    print('NF618 early deployment preflight PASS',json.dumps(check(Path(sys.argv[1]),Path(sys.argv[2])),sort_keys=True))
