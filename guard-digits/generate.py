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
d=root/'WeilDefect/Generated/NF618W02Segmented';d.mkdir(parents=True,exist_ok=True);mod='WeilDefect.Generated.NF618W02Segmented'
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
def nf618SegArg : NF591Rect := {rect(arg)}
def nf618SegState0000 : NF633ExpState := {state(*states[0])}
theorem nf618SegPrefix0000 : neutralNF633State nf618SegArg nf618GuardQ 0=nf618SegState0000 := by
  apply neutralNF633StateEq_sound
  decide +kernel
'''+end)
prior='Seed';prev=0;ks=list(states)[1:]
for k in range(0,len(ks),6):
    file=f'Part{k//6:02d}';src=f'import {mod}.{prior}\n'+head
    for j in ks[k:k+6]:
        src+=f'''
def nf618SegState{j:04d} : NF633ExpState := {state(*states[j])}
theorem nf618SegGate{j:04d} : neutralNF633StateEq (neutralNF633Segment nf618SegArg nf618GuardQ {prev} nf618SegState{prev:04d} {j-prev}) nf618SegState{j:04d}=true := by
  decide +kernel
theorem nf618SegPrefix{j:04d} : neutralNF633State nf618SegArg nf618GuardQ {j}=nf618SegState{j:04d} :=
  neutralNF633Prefix_extend nf618SegArg nf618GuardQ {prev} {j-prev} nf618SegState{prev:04d} nf618SegState{j:04d} nf618SegPrefix{prev:04d} nf618SegGate{j:04d}
'''
        prev=j
    emit(file,src+end);prior=file
emit('Root',f'''import {mod}.{prior}
{head}
def nf618SegSmall : NF591Rect := {rect(small)}
def nf618SegPower01 : NF591Rect := {rect(val)}
theorem nf618SegArgCheck : neutralNF633RectEq (neutralNF592PhaseArg nf618GuardPiPi (1/1408) nf618GuardQ) nf618SegArg=true := by
  decide +kernel
theorem nf618SegSmallCheck : neutralNF633RectEq (nf618SegState1200.sumState.expand (1/(nf618GuardQ:ℚ))) nf618SegSmall=true := by
  decide +kernel
theorem nf618SegRootCheck : neutralNF633RectEq ((nf618SegSmall.mulQ nf618SegSmall nf618GuardQ).mulQ (nf618SegSmall.mulQ nf618SegSmall nf618GuardQ) nf618GuardQ) nf618SegPower01=true := by
  decide +kernel
theorem nf618SegRootEq : neutralNF593Phase nf618GuardPiPi (1/1408) nf618GuardQ nf618GuardExpN=nf618SegPower01 := by
  apply neutralNF633Phase_of_small nf618GuardPiPi (1/1408) nf618GuardQ nf618GuardExpN nf618SegSmall nf618SegPower01
  · rw [neutralNF633RectEq_sound _ _ nf618SegArgCheck]
    exact neutralNF633SmallExp_of_state nf618SegArg nf618GuardQ nf618GuardExpN nf618SegState1200 nf618SegSmall nf618SegPrefix1200 nf618SegSmallCheck
  · exact nf618SegRootCheck
theorem nf618SegPower01_sound : nf618SegPower01.Contains (nf618HybridPhase (1/1408)^1) := by
  rw [pow_one, ← nf618SegRootEq, neutralNF593Phase_eq]
  exact neutralNF592PhaseBall_sound nf618GuardPiPi nf618GuardPiPiSound (1/1408) nf618GuardQ nf618GuardExpN nf618GuardQ_pos (by decide +kernel) nf618GuardExpFee
#print axioms nf618SegRootEq
#print axioms nf618SegPower01_sound
'''+end)
names.extend(['nf618SegRootEq','nf618SegPower01_sound'])
src=f'import {mod}.Root\n'+head;a=val
for j in range(2,15):
    a=zmul(a,val)
    src+=f'''
def nf618SegPower{j:02d} : NF591Rect := {rect(a)}
theorem nf618SegPower{j:02d}_eq : (nf618SegPower{j-1:02d}.mulQ nf618SegPower01 nf618GuardQ)=nf618SegPower{j:02d} := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618SegPower{j:02d}_sound : nf618SegPower{j:02d}.Contains (nf618HybridPhase (1/1408)^{j}) := by
  rw [← nf618SegPower{j:02d}_eq]
  exact NF591Rect.contains_mulQ nf618SegPower{j-1:02d}_sound (by simpa only [pow_one] using nf618SegPower01_sound) nf618GuardQ nf618GuardQ_pos
'''
# Numeral exponents are definitionally equal to predecessor + 1.
emit('Powers',src+end)
# Round the high-precision root power outward once onto the original checker scale.
factor=10**4
a=tuple((m//factor,v.ceildiv(r,factor)+1) for m,r in a)
v.Q=Q;v.ONE=(Q,0);v.pi.cache_clear();v.phase_reduced.cache_clear();v.real_exp.cache_clear()
def ball(b):return '⟨'+','.join(f'({v}:ℚ)/neutralNF616Q' for v in b)+'⟩'
emit('Projection',f'''import {mod}.Powers
import WeilDefect.Generated.NF632.Pi
{head}
def nf618SegProjected14 : NF591Rect := {rect(a)}
theorem nf618SegProjectionEq :
    (⟨nf618SegPower14.re.round neutralNF616Q,nf618SegPower14.im.round neutralNF616Q⟩ : NF591Rect) =
      nf618SegProjected14 := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618SegProjectionSound :
    nf618SegProjected14.Contains (nf618HybridPhase (1/1408)^14) := by
  rw [← nf618SegProjectionEq]
  exact ⟨NF591Ball.contains_round nf618SegPower14_sound.1 neutralNF616Q neutralNF616Q_pos,
    NF591Ball.contains_round nf618SegPower14_sound.2 neutralNF616Q neutralNF616Q_pos⟩
#print axioms nf618SegProjectionEq
#print axioms nf618SegProjectionSound
'''+end)
names.extend(['nf618SegProjectionEq','nf618SegProjectionSound'])
# Materialize the three executable cache rectangles separately. Bind each
# to the actual hybrid-cache computation by a checked equality.
z=(exact(0),mul(pi(),exact(F(7,352))))
pos=zmul(real(1),a)
negend=zmul(real(1),(a[0],neg(a[1])))
emit('Cache',f'''import {mod}.Projection
{head}
def nf618SegPilotTable : NF624KeyTable := ⟨⟨0,7/704⟩, #[
    {rows}
  ]⟩
theorem nf618SegPilotPhase : nf618SegProjected14.Contains (nf618HybridPhase (7/704)) := by
  rw [show (7/704:ℚ)=(14:ℕ)*(1/1408:ℚ) by norm_num, nf618W02Phase_nat]
  exact nf618SegProjectionSound
theorem nf618SegUnit : NF591Rect.one.Contains (Complex.exp ((0:ℂ)*(11/10))) := by
  norm_num [NF591Rect.one,NF591Rect.Contains,NF591Ball.Contains]
def nf618SegLiteralZ : NF591Rect := {rect(z)}
def nf618SegLiteralPos : NF591Rect := {rect(pos)}
def nf618SegLiteralNeg : NF591Rect := {rect(negend)}
def nf618SegPilotCache : NF617MomentCache := ⟨nf618SegLiteralZ,nf618SegLiteralPos,nf618SegLiteralNeg⟩
theorem nf618SegZEq : neutralNF615LambdaRect nf632Pi 0 (7/704) neutralNF616Q=nf618SegLiteralZ := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618SegPosEq : NF591Rect.one.mulQ nf618SegProjected14 neutralNF616Q=nf618SegLiteralPos := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618SegNegEq : NF591Rect.one.mulQ (nf618HybridConj nf618SegProjected14) neutralNF616Q=nf618SegLiteralNeg := by
  apply neutralNF633RectEq_sound
  decide +kernel
theorem nf618SegCacheEq : nf618HybridCache nf632Pi 0 (7/704) neutralNF616Q NF591Rect.one NF591Rect.one nf618SegProjected14 true = nf618SegPilotCache := by
  change NF617MomentCache.mk (neutralNF615LambdaRect nf632Pi 0 (7/704) neutralNF616Q)
    (NF591Rect.one.mulQ nf618SegProjected14 neutralNF616Q)
    (NF591Rect.one.mulQ (nf618HybridConj nf618SegProjected14) neutralNF616Q) = _
  rw [nf618SegZEq,nf618SegPosEq,nf618SegNegEq]
  rfl
theorem nf618SegCacheSound : nf618SegPilotCache.SemanticSound nf618SegPilotTable.key := by
  rw [← nf618SegCacheEq]
  apply nf618HybridCache_sound nf632Pi nf632PiSound 0 (7/704) neutralNF616Q neutralNF616Q_pos NF591Rect.one NF591Rect.one nf618SegProjected14
  · exact nf618SegUnit
  · convert nf618SegUnit using 1 <;> norm_num
  · change nf618SegProjected14.Contains (nf618HybridPhase (7/704))
    exact nf618SegPilotPhase
theorem nf618SegPilotSize : nf618SegPilotTable.rows.size = 4 := by rfl
theorem nf618SegPilotLower : nf618SegPilotTable.key.lower = (21/352:ℚ) := by
  decide +kernel
#print axioms nf618SegCacheEq
#print axioms nf618SegCacheSound
'''+end)
# The bool is an explicit argument AFTER the two amplitude premises. Supply it
# in the theorem application directly rather than asking apply to infer it.
cache=(d/'Cache.lean').read_text()
old='''  apply nf618HybridCache_sound nf632Pi nf632PiSound 0 (7/704) neutralNF616Q neutralNF616Q_pos NF591Rect.one NF591Rect.one nf618SegProjected14
  · exact nf618SegUnit
  · convert nf618SegUnit using 1 <;> norm_num
  · change nf618SegProjected14.Contains (nf618HybridPhase (7/704))
    exact nf618SegPilotPhase'''
new='''  exact nf618HybridCache_sound nf632Pi nf632PiSound 0 (7/704) neutralNF616Q neutralNF616Q_pos
    NF591Rect.one NF591Rect.one nf618SegProjected14
    (by simpa only [Rat.cast_zero] using nf618SegUnit)
    (by simpa only [neg_zero, Rat.cast_zero] using nf618SegUnit) true nf618SegPilotPhase'''
need(old in cache,'cache proof repair anchor')
cache=cache.replace(old,new)
(d/'Cache.lean').write_text(cache);(e/'Cache.lean').write_text(cache)
emit('Diagnostic',f'''import {mod}.Cache
{head}
#eval (List.range 4).map (neutralNF617MomentRowCheck nf618SegPilotCache (21/352) neutralNF616Q nf618SegPilotTable.rows)
'''+end)
src=f'import {mod}.Cache\n'+head
for j in range(4):
    src+=f'''
theorem nf618SegPilotRow{j} : neutralNF617MomentRowCheck nf618SegPilotCache (21/352) neutralNF616Q nf618SegPilotTable.rows {j}=true := by
  decide +kernel
'''
src+='''
theorem nf618SegPilotRowsCheck : (List.range nf618SegPilotTable.rows.size).all (neutralNF617MomentRowCheck nf618SegPilotCache nf618SegPilotTable.key.lower neutralNF616Q nf618SegPilotTable.rows)=true := by
  rw [nf618SegPilotSize,nf618SegPilotLower]
  apply List.all_eq_true.mpr
  intro j hj
  have hj' := List.mem_range.mp hj
  have h : j=0 ∨ j=1 ∨ j=2 ∨ j=3 := by omega
  rcases h with rfl | rfl | rfl | rfl
  · exact nf618SegPilotRow0
  · exact nf618SegPilotRow1
  · exact nf618SegPilotRow2
  · exact nf618SegPilotRow3
theorem nf618SegPilotSound : neutralNF690TableSound nf618SegPilotTable := by
  apply neutralNF690TableSound_of_semantic_cache nf618SegPilotCache nf618SegPilotTable nf618SegCacheSound
  · rw [nf618SegPilotLower]
    norm_num
  · exact neutralNF616Q_pos
  · intro n hn
    exact List.all_eq_true.mp nf618SegPilotRowsCheck n (List.mem_range.mpr hn)
#print axioms nf618SegPilotRow0
#print axioms nf618SegPilotRow1
#print axioms nf618SegPilotRow2
#print axioms nf618SegPilotRow3
#print axioms nf618SegPilotRowsCheck
#print axioms nf618SegPilotSound
'''
emit('Pilot',src+end)
names.extend(['nf618SegCacheEq','nf618SegCacheSound','nf618SegPilotRow0','nf618SegPilotRow1','nf618SegPilotRow2','nf618SegPilotRow3','nf618SegPilotRowsCheck','nf618SegPilotSound'])
(e/'targets.txt').write_text('\n'.join(names)+'\n')
(e/'manifest.json').write_text(json.dumps({'slot':99,'rows':4,'literal_rows_sha256':H(rows.encode()),'chunk_sha256':files[name],'modules':{f:H((d/(f+'.lean')).read_bytes()) for f in modules},'scope':'one admitted literal table; no new admission or bank equality'},indent=2)+'\n')
print('Segmented source emitted',len(modules),'modules for slot 99')
