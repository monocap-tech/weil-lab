import hashlib,json,zipfile,sys,subprocess,shutil
from pathlib import Path
H=lambda b:hashlib.sha256(b).hexdigest()
base=Path('historical/custody/run_46076027949-attempt_1')
r=next(x for x in json.loads((base/'recovery.json').read_text())['records'] if x['artifact_id']==14558233793)
with open('payload.zip','wb') as out:
    for c in r['chunks']:
        b=(base/c['file']).read_bytes()
        assert H(b)==c['sha256'] and len(b)==c['bytes']
        out.write(b)
assert H(Path('payload.zip').read_bytes())=='2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70'
phase=Path('direct/archives/14580099864/part0000.bin')
assert H(phase.read_bytes())=='fba35eada4a0614260109add6e3762b90447bf047541817c7529348121f33ab3'
p=Path('producer/custody/run_46105392388-attempt_1/evidence.zip')
md=json.loads(p.with_name('metadata.json').read_bytes())
assert md['workflow_run']['id']==46105392388 and md['workflow_run']['head_sha']=='e5a3d704a1fadd23c76164f259d1e323b045224c' and md['name']=='nf618-w02-batch27'
assert md['digest']=='PRODUCER_EVIDENCE_DIGEST_PENDING'
assert H(p.read_bytes())==md['digest'].removeprefix('sha256:') and p.stat().st_size==md['size_in_bytes']
with zipfile.ZipFile(p) as z:
    assert z.testzip() is None
    for n in ('generate.py','emit_pi.py','GuardParams.lean','GuardPiBase.lean','NF618W02Seeds.lean','RootAttachmentCandidate.lean','audit.py','release.json','parent-admission.json','Batch27Plan.json','FrequencyDecomposition.json'):
        assert z.read(n)==(Path('candidate')/n).read_bytes(),n
    d=Path('regen').resolve();d.mkdir()
    research=Path('research').resolve()
    subprocess.run([sys.executable,str(Path('candidate/emit_pi.py').resolve()),'--output',str(d/'guard-pi'),'--full'],check=True)
    subprocess.run([sys.executable,str(Path('candidate/generate.py').resolve()),str(phase.resolve()),str(Path('payload.zip').resolve()),str(d)],cwd=research,check=True)
    m=json.loads(z.read('manifest.json'))
    assert (d/'manifest.json').read_bytes()==z.read('manifest.json')
    assert (d/'targets.txt').read_bytes()==z.read('targets.txt')
    for n,h in m['files'].items():
        assert H((d/n).read_bytes())==h and (d/n).read_bytes()==z.read(n),n
    pi=list((d/'guard-pi').iterdir())
    assert len(pi)==128
    for f in pi:assert f.read_bytes()==z.read('guard-pi/'+f.name),f.name
    result={'source_regeneration':'PASS','generated_modules':len(m['files']),'guard_pi_files':len(pi),'manifest_sha256':H(z.read('manifest.json')),'scope':'deterministic source replay from original frozen inputs; not a fresh native build','new_admissions':0}
    Path('evidence/regeneration.json').write_text(json.dumps(result,indent=2)+'\n')
    print(json.dumps(result))
