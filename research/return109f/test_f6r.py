import contextlib, io, json, os, pathlib, subprocess, sys, tempfile
from unittest.mock import patch
from types import SimpleNamespace
import prepare_f_assembly as P
import audit_f_stage as A

E = b'fixture receiving attachment\n'
EB = P.digest(E)

def generator(fault):
    with tempfile.TemporaryDirectory() as tmp:
        root=pathlib.Path(tmp); base=root/'base.py'; out=root/'out.py'
        added={f'supplier{i}':{'blob':f'blob{i}'} for i in range(31)}
        entries={k:{'blob':v['blob'],'required_by':['IV']} for k,v in added.items()}
        if fault=='delta': entries['extra']={'blob':'extra','required_by':['IV']}
        if fault=='lineage': entries['supplier0']['required_by']=['RECON']
        if fault=='supplier': entries['supplier0']['blob']='bad'
        base.write_text('import pathlib,json,hashlib\n'+
            'def digest(b): return hashlib.sha1(b"blob "+str(len(b)).encode()+b"\\0"+b).hexdigest()\n'+
            f'manifest={dict.fromkeys(range(283),{})!r}\nentries={entries!r}\n'+
            'def visit(p,side): manifest.update(entries)\n'+
            '# No source files are written until the entire selected closure passes.\n'+
            'pathlib.Path("WeilDefect/MasterReturn").mkdir(parents=True)\n'+
            f'# {EB}\n'+
            f'pathlib.Path("WeilDefect/MasterReturn/LogCarrierBoundedAnalysis.lean").write_bytes({(b"wrong" if fault=="E" else E)!r})\n'+
            ('pathlib.Path("WeilDefect/MasterReturn/M0.lean").touch()\n' if fault=='collision' else ''))
        files={}; mods=[]
        for i in range(16):
            p=f'research/master-return-109f/M{i}.lean'; names=[f'M{i}.t{j}' for j in range(7 if i<15 else 6)]
            b=('import Mathlib\n'+'\n'.join('#print axioms '+n for n in names)+'\n').encode(); files[p]=b
            mods.append(dict(path=p,blob=P.digest(b),names=names,imports=['Mathlib']))
        if fault=='source': mods[0]['blob']='bad'
        if fault=='names': mods[0]['names'][0]='bad'
        if fault=='imports': mods[0]['imports']=['Wrong']
        roots=dict(roots=[dict(path=f'supplier{i}',blob=f'blob{i}',inE2=False) for i in range(4)],base_manifest_count=283,IV='i',RECON='r')
        disc=dict(pending=[],added=added,base_count=283,IV='i',RECON='r')
        for n,obj in [('F_NAMED_AUDIT_MANIFEST',dict(modules=mods,total=111,unique=111)),('F_SUPPLIER_ROOTS',roots),('F_CLOSURE_DISCOVERY',disc)]: files[str(P.DIR/(n+'.json'))]=json.dumps(obj).encode()
        pins=dict(BASE_BLOB=P.digest(base.read_bytes()) if fault!='base' else 'wrong',E_BLOB=EB)
        for key,n in [('MANIFEST_BLOB','F_NAMED_AUDIT_MANIFEST'),('ROOTS_BLOB','F_SUPPLIER_ROOTS'),('DISCOVERY_BLOB','F_CLOSURE_DISCOVERY')]: pins[key]=P.digest(files[str(P.DIR/(n+'.json'))])
        with patch.multiple(P,**pins),patch.object(P.subprocess,'check_output',side_effect=lambda a:files[a[-1].split(':',1)[1]]),patch.object(sys,'argv',['gen',str(base),str(root),str(out)]),contextlib.redirect_stdout(io.StringIO()):
            try: P.main()
            except AssertionError:
                assert fault in ['base','source','names','imports']; assert not out.exists(); return
        p=subprocess.run([sys.executable]+(['-O'] if fault=='optimized' else [])+[str(out)],cwd=root,capture_output=True)
        receipt=root/'return109f-closure.json'
        if fault: assert p.returncode and not receipt.exists(),(fault,p.stdout,p.stderr)
        else:
            assert p.returncode==0,p.stderr; r=json.loads(receipt.read_text()); assert r['supplier_count']==314 and r['admitted_E_blob']==EB and len(r['staged'])==16 and r['named_targets']==111

def audit(fault):
    with tempfile.TemporaryDirectory() as tmp:
        old=os.getcwd(); os.chdir(tmp)
        try:
            p=pathlib.Path('WeilDefect/MasterReturn/M.lean'); p.parent.mkdir(parents=True); p.write_text('#print axioms M.good\n#print axioms M.other\n')
            e=p.parent/'LogCarrierBoundedAnalysis.lean'; e.write_bytes(b'wrong' if fault=='E' else E)
            blob=A.digest(p.read_bytes()); plan=dict(allowed_axioms=['propext','Classical.choice','Quot.sound'],stages=[dict(stage='test',count=2,modules=[dict(module='WeilDefect.MasterReturn.M',blob=blob,targets=['M.good','M.other'])])]); pathlib.Path('plan.json').write_text(json.dumps(plan))
            closure=dict(named_targets=111,admitted_E_blob='bad' if fault=='E_receipt' else EB,base_assembler_blob='bad' if fault=='base' else A.BASE_BLOB,supplier_count=313 if fault=='count' else 314,staged={str(p):dict(blob='bad' if fault=='closure' else blob)})
            pathlib.Path('return109f-closure.json').write_text(json.dumps(closure))
            if fault=='source': p.write_text('wrong')
            def run(cmd,stdout,stderr):
                if cmd[1]=='build': return SimpleNamespace(returncode=int(fault=='build'))
                log="'M.good' depends on axioms: [propext,\n Classical.choice, Quot.sound]\n'M.other' does not depend on any axioms\n"
                if fault=='forbidden': log=log.replace('Quot.sound','sorryAx')
                if fault=='missing': log=log.split("'M.other'")[0]
                if fault=='duplicate': log+="'M.other' does not depend on any axioms\n"
                stdout.write(log.encode()); return SimpleNamespace(returncode=int(fault=='audit'))
            with patch.multiple(A,PLAN_BLOB='bad' if fault=='plan' else A.digest(pathlib.Path('plan.json').read_bytes()),E_BLOB=EB),patch.object(A.subprocess,'run',side_effect=run),patch.object(sys,'argv',['audit','plan.json','test','evidence']),contextlib.redirect_stdout(io.StringIO()):
                try: A.main()
                except AssertionError: assert fault
                else: assert not fault
            r=pathlib.Path('evidence/receipt.json')
            if fault=='plan': assert not r.exists()
            else: assert json.loads(r.read_text())['complete']==(fault is None)
        finally: os.chdir(old)

if __name__=='__main__':
    total=0
    for fun,faults in [(generator,[None,'base','source','names','imports','delta','supplier','lineage','collision','E','optimized']),(audit,[None,'plan','source','closure','build','audit','forbidden','missing','duplicate','E','E_receipt','base','count'])]:
        for fault in faults: fun(fault); print('PASS',fun.__name__,fault); total+=1
    for file in ['prepare_f_assembly.py','audit_f_stage.py']:
        p=subprocess.run([sys.executable,'-O',str(pathlib.Path(__file__).parent/file)],capture_output=True); assert p.returncode and b'verification requires assertions enabled' in p.stderr; print('PASS optimized',file); total+=1
    print(f'{total}/{total} PASS')
