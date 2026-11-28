#!/usr/bin/env python3
"""Segment the exact reference root evaluation and check one already-admitted table."""
import hashlib,json,re,sys,zipfile
from fractions import Fraction as F
from pathlib import Path
sys.set_int_max_str_digits(0)
root=Path.cwd(); e=Path(sys.argv[3]).resolve()
sys.path.insert(0,str(root/'scripts'))
import verify_nf620_physical_key_tables as v
from verify_nf620_physical_key_tables import Q,N,M,ZERO,exact,mul,add,div,real,pi,zmul,zadd,neg
H=lambda b:hashlib.sha256(b).hexdigest()
def need(x,msg):
    if not x:raise ValueError(msg)
def archive(p,d):
    p=Path(p);need(H(p.read_bytes())==d,'archive identity')
    z=zipfile.ZipFile(p);need(z.testzip() is None,'ZIP CRC');return z
with archive(sys.argv[1],'fba35eada4a0614260109add6e3762b90447bf047541817c7529348121f33ab3') as z:
    raw=z.read('NF632/manifest.json');need(H(raw)=='b4d290d158af245635d17b58f1c8e9f8bfa5076f773c1a35aa7e789bf850b086','pi manifest')
    out=root/'WeilDefect/Generated/NF632';out.mkdir(parents=True,exist_ok=True)
    for f in json.loads(raw)['files']:
        b=z.read('NF632/'+f['file']);need(H(b)==f['sha256'],'pi source');(out/f['file']).write_bytes(b)
    (out/'manifest.json').write_bytes(raw)
with archive(sys.argv[2],'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70') as z:
    raw=z.read('manifest.json');need(H(raw)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7','bank manifest')
    m=json.loads(raw);s=m['slots'][99]
    need(s['index']==99 and list(map(F,s['key']))==[F(0),F(7,704)] and s['rows']==4,'pilot key')
    files={x['file']:x['sha256'] for x in m['files']};name=s['chunk']+'.lean';b=z.read(name);need(H(b)==files[name],'literal chunk')
    rows=re.findall(r'#\[\n    (.*?)\n  \]',b.decode(),re.S)[s['offset']]
decomp=json.loads((root/'notes/provisional/NF618W02RootAttachment/FrequencyDecomposition.json').read_text())['rows']
need(decomp[99]==[99,0,14,3,0,0,14,'combined',None],'admitted slot')
d=root/'WeilDefect/Generated/NF618W02Batch27';d.mkdir(parents=True,exist_ok=True);mod='WeilDefect.Generated.NF618W02Batch27'
head='namespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n';end='\nend WeilDefect\n'
names=[];modules=[]
def emit(file,src):
    (d/(file+'.lean')).write_text(src);(e/(file+'.lean')).write_text(src);modules.append(file)
def ball(b):return '⟨'+','.join(f'({v}:ℚ)/nf618GuardQ' for v in b)+'⟩'
def rect(a):return '⟨'+','.join(map(ball,a))+'⟩'
def state(t,s):return '⟨'+rect(t)+','+rect(s)+'⟩'
v.Q=10**2604;v.ONE=(v.Q,0);v.pi.cache_clear();v.phase_reduced.cache_clear();v.real_exp.cache_clear()
arg=(ZERO,mul(pi(),exact(F(1,2560))));t=real(1);s=(ZERO,ZERO);states={0:(t,s)}
for j in range(N):
    s=zadd(s,t);t=tuple(div(a,j+1) for a in zmul(t,arg))
    if (j+1)%32==0 or j+1==N:states[j+1]=(t,s)
small=tuple((x,r+1) for x,r in s);b=zmul(small,small);val=zmul(b,b)
emit('Seed',f'''import WeilDefect.Arithmetic.NF618W02RootAttachmentCandidate
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedExp
import WeilDefect.Generated.NF618GuardPi.Pi
{head}
def nf618B27SegArg : NF591Rect := {rect(arg)}
def nf618B27SegState0000 : NF633ExpState := {state(*states[0])}
theorem nf618B27SegPrefix0000 : neutralNF633State nf618B27SegArg nf618GuardQ 0=nf618B27SegState0000 := by
  apply neutralNF633StateEq_sound
  decide +kernel
'''+end)
prior='Seed';prev=0;ks=list(states)[1:]
for k in range(0,len(ks),6):
    file=f'Part{k//6:02d}';src=f'import {mod}.{prior}\n'+head
    for j in ks[k:k+6]:
        src+=f'''
def nf618B27SegState{j:04d} : NF633ExpState := {state(*states[j])}
theorem nf618B27SegGate{j:04d} : neutralNF633StateEq (neutralNF633Segment nf618B27SegArg nf618GuardQ {prev} nf618B27SegState{prev:04d} {j-prev}) nf618B27SegState{j:04d}=true := by
  decide +kernel
theorem nf618B27SegPrefix{j:04d} : neutralNF633State nf618B27SegArg nf618GuardQ {j}=nf618B27SegState{j:04d} :=
  neutralNF633Prefix_extend nf618B27SegArg nf618GuardQ {prev} {j-prev} nf618B27SegState{prev:04d} nf618B27SegState{j:04d} nf618B27SegPrefix{prev:04d} nf618B27SegGate{j:04d}
'''
        prev=j
    emit(file,src+end);prior=file
emit('Root',f'''import {mod}.{prior}
{head}
def nf618B27SegSmall : NF591Rect := {rect(small)}
def nf618B27SegPower01 : NF591Rect := {rect(val)}
theorem nf618B27SegArgCheck : neutralNF633RectEq (neutralNF592PhaseArg nf618GuardPiPi (1/1408) nf618GuardQ) nf618B27SegArg=true := by
  decide +kernel
theorem nf618B27SegSmallCheck : neutralNF633RectEq (nf618B27SegState1200.sumState.expand (1/(nf618GuardQ:ℚ))) nf618B27SegSmall=true := by
  decide +kernel
theorem nf618B27SegRootCheck : neutralNF633RectEq ((nf618B27SegSmall.mulQ nf618B27SegSmall nf618GuardQ).mulQ (nf618B27SegSmall.mulQ nf618B27SegSmall nf618GuardQ) nf618GuardQ) nf618B27SegPower01=true := by
  decide +kernel
theorem nf618B27SegRootEq : neutralNF593Phase nf618GuardPiPi (1/1408) nf618GuardQ nf618GuardExpN=nf618B27SegPower01 := by
  apply neutralNF633Phase_of_small nf618GuardPiPi (1/1408) nf618GuardQ nf618GuardExpN nf618B27SegSmall nf618B27SegPower01
  · rw [neutralNF633RectEq_sound _ _ nf618B27SegArgCheck]
    exact neutralNF633SmallExp_of_state nf618B27SegArg nf618GuardQ nf618GuardExpN nf618B27SegState1200 nf618B27SegSmall nf618B27SegPrefix1200 nf618B27SegSmallCheck
  · exact nf618B27SegRootCheck
theorem nf618B27SegPower01_sound : nf618B27SegPower01.Contains (nf618HybridPhase (1/1408)^1) := by
  rw [pow_one, ← nf618B27SegRootEq, neutralNF593Phase_eq]
  exact neutralNF592PhaseBall_sound nf618GuardPiPi nf618GuardPiPiSound (1/1408) nf618GuardQ nf618GuardExpN nf618GuardQ_pos (by decide +kernel) nf618GuardExpFee
#print axioms nf618B27SegRootEq
#print axioms nf618B27SegPower01_sound
'''+end)
names.extend(['nf618B27SegRootEq','nf618B27SegPower01_sound'])

# Build a shared materialized high precision prefix, in bounded source modules.
plan=json.loads((root/'notes/provisional/NF618Batch27Plan.json').read_text())
ids=sorted(i for g in plan['groups'] for i,_ in g['slots'])
need(len(ids)==len(set(ids))==114 and plan['rows']==594,'frozen plan')
need(set(ids)=={r[0] for r in decomp if r[8]==27 and r[7] is None},'demand partition')
pairs=sorted({(decomp[i][5],decomp[i][6]) for i in ids})
need(len(pairs)==26,'signed phases')
powers={0:real(1),1:val};a=val;prev='Root'
for start in range(2,max(abs(r) for _,r in pairs)+1,12):
    file=f'PowerBlock{start:03d}';src=f'import {mod}.{prev}\n'+head
    for j in range(start,min(start+12,max(abs(r) for _,r in pairs)+1)):
        a=zmul(a,val);powers[j]=a
        src+=f'''
def nf618B27SegPower{j:02d} : NF591Rect := {rect(a)}
theorem nf618B27SegPower{j:02d}_eq : (nf618B27SegPower{j-1:02d}.mulQ nf618B27SegPower01 nf618GuardQ)=nf618B27SegPower{j:02d} := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618B27SegPower{j:02d}_sound : nf618B27SegPower{j:02d}.Contains (nf618HybridPhase (1/1408)^{j}) := by
  rw [← nf618B27SegPower{j:02d}_eq]
  exact NF591Rect.contains_mulQ nf618B27SegPower{j-1:02d}_sound (by simpa only [pow_one] using nf618B27SegPower01_sound) nf618GuardQ nf618GuardQ_pos
'''
    emit(file,src+end);prev=file
def rat(f):
    f=F(f);return f'({f.numerator}/{f.denominator}:ℚ)'
def tag(q,r):return f'Q{q}'+('P' if r>=0 else 'N')+f'{abs(r):03d}'
def conj(a):return a[0],neg(a[1])
quarter=(v.ZERO,v.ONE);qp=[real(1),quarter]
for j in range(2,4):qp.append(zmul(qp[-1],quarter))
phasevals={}
for q,r in pairs:
    n='nf618B27'+tag(q,r);file='Phase'+tag(q,r);rep=F(320*q+r,1408)
    a=powers[abs(r)];a=a if r>=0 else conj(a)
    high=zmul(qp[q],a)
    lo=tuple((m//10**4,v.ceildiv(rad,10**4)+1) for m,rad in high)
    phasevals[q,r]=lo
    pn=f'nf618B27SegPower{abs(r):02d}'
    need(r!=0,'nonzero retained power')
    powerexpr=pn if r>=0 else f'(nf618HybridConj {pn})'
    proof=f'{pn}_sound' if r>=0 else f'(nf618HybridConj_sound _ _ {pn}_sound)'
    boolstr=str(r>=0).lower()
    # Specialize the actual Bool coercion proposition, not True/False.
    branchproof='if_pos (rfl : (true : Bool) = true)' if r>=0 else 'if_neg (by decide : (false : Bool) ≠ true)'
    src=f'''import {mod}.{prev}
import WeilDefect.Arithmetic.NF618W02Seeds
import WeilDefect.Generated.NF632.Pi
{head}
def {n}High : NF591Rect := {rect(high)}
theorem {n}HighEq :
    (nf618W02RectPow nf618W02Quarter nf618GuardQ {q}).mulQ {powerexpr} nf618GuardQ = {n}High := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem {n}HighSound : {n}High.Contains (nf618HybridPhase {rat(rep)}) := by
  rw [← {n}HighEq, nf618W02Phase_decompose {rat(rep)} 0 {q} {abs(r)} {boolstr} (by norm_num)]
  rw [{branchproof}]
  exact NF591Rect.contains_mulQ
    (nf618W02RectPow_sound nf618W02Quarter _ nf618GuardQ nf618GuardQ_pos nf618W02Quarter_sound {q})
    {proof} nf618GuardQ nf618GuardQ_pos
'''
    # Original-scale outward rounding only after complete signed phase.
    lo_literal='⟨'+','.join('⟨'+','.join(f'({x}:ℚ)/neutralNF616Q' for x in c)+'⟩' for c in lo)+'⟩'
    src+=f'''
def {n}Phase : NF591Rect := {lo_literal}
theorem {n}ProjectionEq :
    (⟨{n}High.re.round neutralNF616Q,{n}High.im.round neutralNF616Q⟩ : NF591Rect) = {n}Phase := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem {n}PhaseSound : {n}Phase.Contains (nf618HybridPhase {rat(rep)}) := by
  rw [← {n}ProjectionEq]
  exact ⟨NF591Ball.contains_round {n}HighSound.1 neutralNF616Q neutralNF616Q_pos,
    NF591Ball.contains_round {n}HighSound.2 neutralNF616Q neutralNF616Q_pos⟩
'''
    emit(file,src+end);names.extend([n+'HighEq',n+'HighSound',n+'ProjectionEq',n+'PhaseSound'])
v.Q=Q;v.ONE=(Q,0);v.pi.cache_clear();v.phase_reduced.cache_clear();v.real_exp.cache_clear()
def ball(b):return '⟨'+','.join(f'({x}:ℚ)/neutralNF616Q' for x in b)+'⟩'
emit('Unit',f'''import {mod}.Root
{head}
theorem nf618B27Unit : NF591Rect.one.Contains (Complex.exp ((0:ℂ)*(11/10))) := by
  norm_num [NF591Rect.one,NF591Rect.Contains,NF591Ball.Contains]
'''+end)
records=[];slotmodules=[]
with archive(sys.argv[2],'2327fbf952d4894c9f28f81cad9e94d226c93131d9ef2fafa14c35f482211b70') as zz:
    files={x['file']:x['sha256'] for x in m['files']}
    for i in ids:
        s=m['slots'][i];dr=decomp[i];h,f=map(F,s['key']);turn,q,r=dr[4:7];rep=F(320*q+r,1408)
        need(i==s['index']==dr[0] and h==0 and 1408*f==dr[2] and s['rows']==dr[3]+1,'slot identity')
        need(f==F(10*turn,11)+rep,'decomposition')
        ch=s['chunk'];b=zz.read(ch+'.lean');need(H(b)==files[ch+'.lean'],'chunk identity')
        literal=re.findall(r'#\[\n    (.*?)\n  \]',b.decode(),re.S)[s['offset']]
        nums=list(map(int,re.findall(r'\((-?\d+):ℚ\)/\(neutralNF616Q:ℚ\)',literal)))
        count=s['rows'];need(len(nums)==3*count,'row grammar')
        rows=[tuple(nums[k:k+3]) for k in range(0,len(nums),3)]
        need(literal==',\n    '.join('⟨'+','.join(f'({x}:ℚ)/(neutralNF616Q:ℚ)' for x in row)+'⟩' for row in rows),'literal roundtrip')
        a=phasevals[q,r];pos=zmul(real(1),a);negend=zmul(real(1),conj(a));z=(ZERO,mul(pi(),exact(2*f)))
        n=f'nf618B27Slot{i:05d}';pn='nf618B27'+tag(q,r);file=f'Slot{i:05d}';delta=6*abs(f)
        src=f'''import {mod}.Phase{tag(q,r)}
import {mod}.Unit
import WeilDefect.Generated.NF690.Bank
{head}
def {n}Table : NF624KeyTable := ⟨⟨0,{rat(f)}⟩, (nf690{ch}[{s['offset']}]?).getD #[]⟩
def {n}LiteralZ : NF591Rect := {rect(z)}
def {n}LiteralPos : NF591Rect := {rect(pos)}
def {n}LiteralNeg : NF591Rect := {rect(negend)}
def {n}Cache : NF617MomentCache := ⟨{n}LiteralZ,{n}LiteralPos,{n}LiteralNeg⟩
theorem {n}PhaseIdentity : nf618HybridPhase {rat(f)} = nf618HybridPhase {rat(rep)} := by
  unfold nf618HybridPhase
  rw [neutralNF592Phase_identity,neutralNF592Phase_identity]
  rw [show neutralNF592Reduced {rat(f)}=neutralNF592Reduced {rat(rep)} from by decide +kernel]
theorem {n}ZEq : neutralNF615LambdaRect nf632Pi 0 {rat(f)} neutralNF616Q = {n}LiteralZ := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem {n}PosEq : NF591Rect.one.mulQ {pn}Phase neutralNF616Q = {n}LiteralPos := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem {n}NegEq : NF591Rect.one.mulQ (nf618HybridConj {pn}Phase) neutralNF616Q = {n}LiteralNeg := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem {n}CacheEq : nf618HybridCache nf632Pi 0 {rat(f)} neutralNF616Q NF591Rect.one NF591Rect.one {pn}Phase true = {n}Cache := by
  change NF617MomentCache.mk (neutralNF615LambdaRect nf632Pi 0 {rat(f)} neutralNF616Q)
    (NF591Rect.one.mulQ {pn}Phase neutralNF616Q)
    (NF591Rect.one.mulQ (nf618HybridConj {pn}Phase) neutralNF616Q) = _
  rw [{n}ZEq,{n}PosEq,{n}NegEq]
  rfl
theorem {n}CacheSound : {n}Cache.SemanticSound {n}Table.key := by
  rw [← {n}CacheEq]
  exact nf618HybridCache_sound nf632Pi nf632PiSound 0 {rat(f)} neutralNF616Q neutralNF616Q_pos
    NF591Rect.one NF591Rect.one {pn}Phase
    (by simpa only [Rat.cast_zero] using nf618B27Unit)
    (by simpa only [neg_zero,Rat.cast_zero] using nf618B27Unit) true
    (by
      change {pn}Phase.Contains (nf618HybridPhase {rat(f)})
      rw [{n}PhaseIdentity]
      exact {pn}PhaseSound)
theorem {n}Size : {n}Table.rows.size = {count} := by rfl
theorem {n}Lower : {n}Table.key.lower = {rat(delta)} := by decide +kernel
'''
        targets=[n+'CacheEq',n+'CacheSound']
        for j in range(count):
            src+=f'''theorem {n}Row{j} : neutralNF617MomentRowCheck {n}Cache {rat(delta)} neutralNF616Q {n}Table.rows {j}=true := by
  decide +kernel
'''
            targets.append(n+f'Row{j}')
        src+=f'''theorem {n}RowsCheck : (List.range {n}Table.rows.size).all (neutralNF617MomentRowCheck {n}Cache {n}Table.key.lower neutralNF616Q {n}Table.rows)=true := by
  rw [{n}Size,{n}Lower]
  apply List.all_eq_true.mpr
  intro j hj
  have hj' := List.mem_range.mp hj
'''
        if count==1:
            src+=f'  have h : j=0 := by omega\n  subst j\n  exact {n}Row0\n'
        else:
            src+='  have h : '+' ∨ '.join(f'j={j}' for j in range(count))+' := by omega\n'
            src+='  rcases h with '+' | '.join(['rfl']*count)+'\n'
            src+=''.join(f'  · exact {n}Row{j}\n' for j in range(count))
        src+=f'''theorem {n}Sound : neutralNF690TableSound {n}Table := by
  apply neutralNF690TableSound_of_semantic_cache {n}Cache {n}Table {n}CacheSound (by rw [{n}Lower]; norm_num) neutralNF616Q neutralNF616Q_pos
  intro j hj
  exact List.all_eq_true.mp {n}RowsCheck j (List.mem_range.mpr hj)
theorem {n}Concrete : neutralNF690TableSound (neutralNF624BankRead nf690OriginalBank {i}) := by
  rw [show nf690OriginalBank = neutralNF690Bank nf687Read nf687Size nf690Payload from rfl]
  rw [neutralNF690Bank_read nf687Read nf687Size nf690Payload {i} (by decide +kernel)]
  rw [neutralNF690Table_eq nf687Read nf690Payload {i} {n}Table (by decide +kernel) (by rfl) (by decide +kernel)]
  exact {n}Sound
'''
        targets.extend([n+'RowsCheck',n+'Sound',n+'Concrete']);names.extend(targets)
        emit(file,src+end);slotmodules.append(file)
        records.append({'slot':i,'key':s['key'],'rows':count,'chunk':ch,'offset':s['offset'],'source_row_sha256':H(literal.encode()),'chunk_sha256':files[ch+'.lean'],'module':file+'.lean','concrete':n+'Concrete','targets':targets})
need(sum(x['rows'] for x in records)==594,'row total')
audit=''.join(f'import {mod}.{x}\n' for x in slotmodules)+head+''.join(f'#print axioms {n}\n' for n in names)+end
emit('AuditBatch27',audit)
need(len(names)==len(set(names)),'audit uniqueness')
(e/'targets.txt').write_text('\n'.join(names)+'\n')
(e/'manifest.json').write_text(json.dumps({'scope':'Batch27 candidate; no admission','plan_blob':'ed7119ed73f589cd3ac6f4ca289415c427f5a57a','tables':records,'theorems':names,'files':{f+'.lean':H((d/(f+'.lean')).read_bytes()) for f in modules},'source_fingerprint':H('\n'.join(f'{f}.lean:{H((d/(f+".lean")).read_bytes())}' for f in sorted(modules)).encode())},indent=2)+'\n')
print('Generated Batch27',len(records),sum(x['rows'] for x in records),len(names),len(modules),flush=True)
