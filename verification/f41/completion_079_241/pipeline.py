"""F41 completion scheduling and independent metadata custody (no Lean claims)."""
import hashlib,json,os,re,subprocess,sys,urllib.request
from pathlib import Path
ROOT=Path(__file__).resolve().parents[3]
PLAN=Path(__file__).with_name('plan.json')
PRODUCER='F41 completion producer rows079-241'
WORKFLOW='.github/workflows/f41-completion-producer-079-241.yml'
REPO='monocap-tech/weil-lab'
def digest_blob(path):
    data=path.read_bytes()
    return hashlib.sha1(b'blob '+str(len(data)).encode()+b'\0'+data).hexdigest()
def load_plan():
    p=json.loads(PLAN.read_text())
    assert p['schema']=='F41-completion-plan-v1'
    assert (p['first_row'],p['last_row'],p['batch_width'])==(79,241,8)
    rows=p['rows']
    assert [x['row'] for x in rows]==list(range(79,242))
    for x in rows:
        i=x['row']; rr=f'{i:03d}'; k=f'{2*i-93:03d}'; v=f'{2*i-92:03d}'
        assert (x['active'],x['rr'],x['k'],x['v'])==(True,rr,k,v)
        assert x['generator']==f'verification/f41/f41_{k}/f41_{k}_original_row{rr}.py'
        assert x['auditor']==f'verification/f41/f41_{v}/f41_{v}_row{rr}_archive_audit.py'
        assert x['artifact']==f'f41-{k}-original-full-payment-row{rr}-kernel-evidence'
        assert x['receipt']==f'f41-{v}-original-physical-row{rr}-independent-audit'
        for key in ('generator','auditor'):
            assert digest_blob(ROOT/x[key])==x[key+'_blob'], x[key]
    return rows
def batches(rows):
    out=[]
    for i in range(0,len(rows),8):
        block=rows[i:i+8]
        out.append({'batch':f'{block[0]["rr"]}-{block[-1]["rr"]}',
                    'rows':block+[{'active':False,'row':-1,'rr':'','k':'','v':'','artifact':'','receipt':''}]*(8-len(block))})
    assert len(out)==21
    return {'include':out}
def output_matrix(rows):
    with open(os.environ['GITHUB_OUTPUT'],'a') as f:
        f.write('matrix='+json.dumps(batches(rows),separators=(',',':'))+'\n')
def api(path):
    root=os.environ['GITHUB_API_URL']+'/repos/'+REPO
    req=urllib.request.Request(root+path,headers={'Authorization':'Bearer '+os.environ['GH_TOKEN'],'Accept':'application/vnd.github+json'})
    with urllib.request.urlopen(req,timeout=45) as r:return json.load(r)
def validate_run(run,run_id,head):
    assert run['id']==run_id and run['status']=='completed' and run['conclusion']=='success'
    assert run['name']==PRODUCER and run['path'].split('@')[0]==WORKFLOW
    assert run['head_sha']==head and run['head_branch']=='main' and run['event'] in ('workflow_dispatch','push')
    assert run['head_repository']['full_name']==REPO
def pin_rows(rows,artifacts,run_id,head):
    assert len(artifacts)==len(rows), 'unexpected artifact count'
    byname={a['name']:a for a in artifacts}
    assert len(byname)==len(rows) and set(byname)=={x['artifact'] for x in rows}
    assert len({a['id'] for a in artifacts})==len(rows)
    pinned=[]
    for x in rows:
        a=byname[x['artifact']]
        assert isinstance(a['id'],int) and a['id']>0
        assert a['workflow_run']['id']==run_id and a['workflow_run']['head_sha']==head
        assert not a['expired'] and a['size_in_bytes']>0
        assert re.fullmatch(r'sha256:[0-9a-f]{64}',a['digest'])
        pinned.append(dict(x,artifact_id=a['id'],zip_sha256=a['digest'][7:],run_id=run_id,head=head))
    return pinned
def pin():
    rows=load_plan(); run_id=int(os.environ['PRODUCER_RUN']);head=os.environ['PRODUCER_HEAD']
    validate_run(api(f'/actions/runs/{run_id}'),run_id,head)
    artifacts=[]
    for page in range(1,5):
        chunk=api(f'/actions/runs/{run_id}/artifacts?per_page=100&page={page}')['artifacts']
        artifacts.extend(chunk)
        if len(chunk)<100:break
    pinned=pin_rows(rows,artifacts,run_id,head)
    Path('f41-completion-pins.json').write_text(json.dumps({'producer_run':run_id,'producer_head':head,'rows':pinned},indent=2)+'\n')
    output_matrix(pinned)
def audit_one():
    x=json.loads(os.environ['ROW_PIN'])
    row=next(z for z in load_plan() if z['row']==x['row'])
    assert all(x[k]==v for k,v in row.items())
    run_id=x['run_id'];head=x['head'];id=x['artifact_id'];digest=x['zip_sha256']
    validate_run(api(f'/actions/runs/{run_id}'),run_id,head)
    a=api(f'/actions/artifacts/{id}')
    assert a['id']==id and a['name']==row['artifact'] and a['workflow_run']['id']==run_id
    assert a['workflow_run']['head_sha']==head and not a['expired'] and a['size_in_bytes']>0
    assert a['digest']=='sha256:'+digest and re.fullmatch(r'[0-9a-f]{64}',digest)
    out=Path('custody')/row['rr'];out.mkdir(parents=True,exist_ok=True)
    archive=out/'producer.zip'
    url=os.environ['GITHUB_API_URL']+f'/repos/{REPO}/actions/artifacts/{id}/zip'
    subprocess.run(['curl','-fsSL','--retry','3','-H','Authorization: Bearer '+os.environ['GH_TOKEN'],url,'-o',str(archive)],check=True)
    assert hashlib.sha256(archive.read_bytes()).hexdigest()==digest
    subprocess.run([sys.executable,row['auditor'],'selftest'],check=True)
    subprocess.run([sys.executable,row['auditor'],'audit','--zip',str(archive),'--expected-zip-sha256',digest,
        '--run-url',f'https://github.com/{REPO}/actions/runs/{run_id}','--run-status','success','--output',str(out/'independent-custody.json')],check=True)
    (out/'validated-producer.json').write_text(json.dumps(x,indent=2)+'\n')
    archive.unlink()
def preflight():
    rows=load_plan(); m=batches(rows)
    assert [z['row'] for b in m['include'] for z in b['rows'] if z['active']]==list(range(79,242))
    for x in rows:
        for key in ('generator','auditor'):
            path=ROOT/x[key]
            compile(path.read_bytes(),str(path),'exec')
            subprocess.run([sys.executable,str(path),'selftest'],cwd=ROOT,check=True)
    head='a'*40;rid=123
    a=[{'id':i+1,'name':x['artifact'],'workflow_run':{'id':rid,'head_sha':head},'expired':False,'size_in_bytes':1,'digest':'sha256:'+'b'*64} for i,x in enumerate(rows)]
    assert len(pin_rows(rows,a,rid,head))==163
    for bad in (a[:-1],a+[a[0]], [dict(a[0],digest='bad')]+a[1:], [dict(a[0],expired=True)]+a[1:], [dict(a[0],workflow_run={'id':999,'head_sha':head})]+a[1:]):
        try:pin_rows(rows,bad,rid,head)
        except AssertionError:pass
        else:raise AssertionError('metadata negative control accepted')
    print('163 generators and 163 auditors passed source selftests; 21 batches; five metadata mutations rejected. No Lean.')
if __name__=='__main__':
    mode=sys.argv[1]
    if mode=='preflight':preflight()
    elif mode=='matrix':output_matrix(load_plan())
    elif mode=='pin':pin()
    elif mode=='audit-one':audit_one()
    else:raise SystemExit('unknown mode')
