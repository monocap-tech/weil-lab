import hashlib,json,re,statistics,zipfile
from pathlib import Path
root=Path('/mnt/data'); p=root/'iv230-sector-seven-receipts.zip'
sha=lambda b:hashlib.sha256(b).hexdigest()
assert sha(p.read_bytes())=='492d48a8aad4e9b386d1d2041a4fd7cff67c44770c0dbc52ac1ba84960c97ebe'
with zipfile.ZipFile(p) as z:
 assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
 m=json.loads(z.read('sector7/manifest.json')); records=m['records']; plan=m['plan']; assert plan['block_interval']==[896,1024] and plan['row_interval']==[7168,8192]
 mods={r['module'] for r in records}; assert len(mods)==len(records)==81 and mods==set(plan['modules'])
 names=[]; leaves=[]; hashes=edges=0; ts=[]; rss=[]; obytes=0
 for r in records:
  stem=r['module']; prefix='sector7/'; source=z.read(prefix+stem+'.lean'); log=z.read(prefix+stem+'.log'); s=source.decode(); l=log.decode()
  assert r['pass'] and sha(source)==r['source_sha256'] and sha(log)==r['log_sha256']; hashes+=2
  assert not re.search(r'\b(?:sorry|admit|sorryAx|native_decide|axiom)\b',s)
  assert not re.search(r'(?m)^.*error(?:\(lean[^)]*\))?:',l) and 'Build completed successfully' in l and 'Exit status: 0' in l
  for name,h in r['objects'].items():
   b=z.read(prefix+name); assert sha(b)==h; hashes+=1
   if name.endswith('.olean'): obytes+=len(b)
  assert stem+'.olean' in r['objects']
  internal=re.findall(r'^import WeilDefect\.Arithmetic\.IV160Bank\.(\w+)$',s,re.M); assert set(internal)<=mods; edges+=len(internal)
  assert re.findall(r'^theorem (\w+)',s,re.M)==r['names']
  leaf=bool(re.fullmatch(r'Row\d{4}',stem))
  for n in r['names']:
   pat=rf"'WeilDefect\.{re.escape(n)}'"; empty=len(re.findall(pat+r' does not depend on any axioms',l)); dep=re.findall(pat+r' depends on axioms: \[([^\]]*)\]',l)
   assert empty+len(dep)==1 and (not dep or set(dep[0].replace(' ','').split(','))<={'propext','Classical.choice','Quot.sound'})
   if leaf:
    assert empty==1; leaves.append(int(n.rsplit('_',1)[1]))
   names.append(n)
  if leaf:
   ts.append(r['seconds']); rss.append(int(re.search(r'Maximum resident set size \(kbytes\): (\d+)',l)[1])/1024**2)
 assert sorted(leaves)==list(range(896,1024)); assert len(names)==len(set(names))==145 and edges==80 and hashes==324
 exact=z.read('exact-audit.json'); prior=[]
 for q in sorted(root.glob('*receipts.zip')):
  if q==p:continue
  with zipfile.ZipFile(q) as other:
   if 'exact-audit.json' in other.namelist() and q.name!='iv159-am-receipts.zip':
    assert other.read('exact-audit.json')==exact,q.name; prior.append(q.name)
 result=dict(artifact_id=15168028090,run_id=45928491091,archive_bytes=p.stat().st_size,sha256=sha(p.read_bytes()),zip_entries=len(z.namelist()),modules=len(mods),hashes_verified=hashes,named_receipts=len(names),axiom_free_leaf_receipts=len(leaves),internal_import_edges=edges,block_interval=plan['block_interval'],row_interval=plan['row_interval'],total_seconds=sum(r['seconds'] for r in records),median_leaf_seconds=statistics.median(ts),median_leaf_rss_gib=statistics.median(rss),max_leaf_rss_gib=max(rss),olean_bytes=obytes,sector_object_sha256=sha(z.read('sector7/RowSector07.olean')),exact_audit_sha256=sha(exact),exact_audit_byte_identical_to=prior,scope='ZIP CRC, SHA256, manifest hashes, source coverage, import edges and recorded axiom outputs; no fresh Lean kernel replay')
(root/'iv235_am_sector_seven_audit.json').write_text(json.dumps(result,indent=2)+'\n');print(json.dumps(result,indent=2))
