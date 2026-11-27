import hashlib,json,re,sys,zipfile
from pathlib import Path
from fractions import Fraction
root=Path(sys.argv[1]); archive=Path(sys.argv[2]); evidence=Path(sys.argv[3])
H=lambda b:hashlib.sha256(b).hexdigest()
assert H(archive.read_bytes())=='2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70'
mp=root/'notes/provisional/NF618W02RootAttachment/FrequencyDecomposition.json'
rows=json.loads(mp.read_text())['rows']
assert len(rows)==7835
# Select by admitted cohort only; no held rows evaluated.
admitted=[x for x in rows if x[7] is not None and (x[1] or x[2])]
assert len([x for x in rows if x[7] is not None])==6097
chosen=[sorted((x for x in admitted if x[1]==h),key=lambda x:(-x[3],-abs(x[6]),x[0]))[0] for h in (-1,0,1)]
chosen.append(min((x for x in admitted if x[1]==0),key=lambda x:abs(x[2])))
assert [x[0] for x in chosen]==[1,180,7736,99]
held=[x for x in rows if x[7] is None]
assert len(held)==1738 and sum(x[3]+1 for x in held)==8658
plans=[{'batch':b,'slots':[x[0] for x in held if x[8]==b],'rows':sum(x[3]+1 for x in held if x[8]==b)} for b in range(25,40)]
assert sum(len(p['slots']) for p in plans)==1738
(evidence/'held-demand-preflight.json').write_text(json.dumps({'scope':'inventory only; no native dispatch','plans':plans},indent=2)+'\n')
def rat(x):return f'({x}:ℚ)'
names=[]; records=[]
with zipfile.ZipFile(archive) as z:
    assert z.testzip() is None and len(z.namelist())==len(set(z.namelist()))
    mb=z.read('manifest.json')
    assert H(mb)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7'
    m=json.loads(mb); slots={x['index']:x for x in m['slots']}; files={x['file']:x['sha256'] for x in m['files']}
    assert len(slots)==7835
    for i,h2,F,d,t,q,r,g,b in chosen:
        s=slots[i]; h=Fraction(h2,2); f=Fraction(F,1408)
        assert list(map(Fraction,s['key']))==[h,f] and s['rows']==d+1
        assert F==1280*t+320*q+r and 0<=q<=3 and abs(r)<=160
        name=s['chunk']+'.lean'; raw=z.read(name);assert H(raw)==files[name]
        block=re.findall(r'#\[\n    (.*?)\n  \]',raw.decode(),re.S)[s['offset']]
        n=f'nf618W02Pilot{i:05d}'; positive=str(r>=0).lower()
        # Literal array copied byte-for-byte from the authenticated chunk.
        src=f'''import WeilDefect.Arithmetic.NF618W02Seeds
namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

def {n}Table : NF624KeyTable := ⟨⟨{rat(h)}, {rat(f)}⟩, #[
    {block}
  ]⟩
def {n}Cache : NF617MomentCache := nf618HybridCache nf618W02Pi {rat(h)} {rat(f)} neutralNF616Q
  (nf618W02Real {rat(h)}) (nf618W02Real {rat(-h)})
  (nf618W02PhaseRect nf618W02Seed nf618W02Quarter neutralNF616Q {q} {abs(r)} {positive}) true
theorem {n}RowsCheck : (List.range {n}Table.rows.size).all (neutralNF617MomentRowCheck {n}Cache {n}Table.key.lower neutralNF616Q {n}Table.rows)=true := by
  decide +kernel
theorem {n}Sound : neutralNF690TableSound {n}Table := by
  apply nf618W02RootTable_sound nf618W02Pi nf618W02Pi_sound {n}Table neutralNF616Q neutralNF616Q_pos
    (nf618W02Real {rat(h)}) (nf618W02Real {rat(-h)}) nf618W02Seed nf618W02Quarter
  · exact nf618W02Real_sound {rat(h)} (by norm_num)
  · exact nf618W02Real_sound {rat(-h)} (by norm_num)
  · exact nf618W02Seed_sound
  · exact nf618W02Quarter_sound
  · exact {t if t>=0 else '('+str(t)+')'}
  · exact {q}
  · exact {abs(r)}
  · exact {positive}
  · norm_num [{n}Table]
  · decide +kernel
  · intro j hj
    exact List.all_eq_true.mp {n}RowsCheck j (List.mem_range.mpr hj)
#print axioms {n}RowsCheck
#print axioms {n}Sound
end WeilDefect
'''
        # supply all explicit witness arguments before subgoals (Lean apply otherwise creates metavariable-dependent goals).
        src=src.replace('nf618W02Seed nf618W02Quarter\n  · exact',f'nf618W02Seed nf618W02Quarter\n    (nf618W02Real_sound {rat(h)} (by norm_num)) (nf618W02Real_sound {rat(-h)} (by norm_num))\n    nf618W02Seed_sound nf618W02Quarter_sound ({t}) {q} {abs(r)} {positive}\n  · exact',1)
        start=src.index('  · exact nf618W02Real_sound'); end=src.index('  · norm_num',start)
        src=src[:start]+src[end:]
        dest=root/'WeilDefect/Arithmetic'/f'NF618W02Pilot{i:05d}.lean'
        dest.write_text(src); (evidence/dest.name).write_text(src)
        records.append({'slot':i,'key':s['key'],'rows':s['rows'],'group':g,'chunk':name,'chunk_sha256':H(raw),'literal_rows_sha256':H(block.encode()),'source_sha256':H(src.encode())})
        names.extend([n+'RowsCheck',n+'Sound'])
(evidence/'pilot-manifest.json').write_text(json.dumps({'scope':'already admitted sample, no new slot admissions; literal local table only, no bank-read equality claimed','tables':records,'theorems':names},indent=2)+'\n')
print('Selected admitted pilot', [r['slot'] for r in records],sum(r['rows'] for r in records))
