import json,re,hashlib
from pathlib import Path
from fractions import Fraction as F
from verify_nf620_physical_key_tables import Q,ZERO,exact,mul,add,zmul,real,pi
sha=lambda b:hashlib.sha256(b).hexdigest()
root='WeilDefect.Generated.NF618HybridPilot';out=Path(root.replace('.','/'));out.mkdir(parents=True,exist_ok=True)
assert not any(out.iterdir())
head='namespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n';end='\nend WeilDefect\n'
def write(file,s): (out/(file+'.lean')).write_text(s)
def rect(a):return '⟨'+','.join('⟨'+','.join(f'({v}:ℚ)/neutralNF616Q' for v in b)+'⟩' for b in a)+'⟩'
def state(t,s):return f'⟨{rect(t)},{rect(s)}⟩'
def rat(x):return f'({x}:ℚ)'
names=[];records=[];phases=[]
for sign,tag,digest in [(1,'Phase0726','c358b3752a5f7610073cd9a018856a834426ea98df0d6283fcc72f161a040095'),(-1,'Phase0727','e73bfe89429e15f337e8e2e09c032bd6350df47824c004dcd8a6ccf4ebd187c5')]:
 v=sign*F(13,40);f=10*v/11;n='nf618Pilot'+tag
 arg=(ZERO,mul(pi(),exact(v/2)));t=real(1);s=(ZERO,ZERO);states={0:(t,s)}
 for j in range(1200):
  s=tuple(add(x,y) for x,y in zip(s,t));t=tuple((x//(j+1),-(-r//(j+1))+1) for x,r in zmul(t,arg))
  if (j+1)%32==0 or j==1199:states[j+1]=(t,s)
 small=tuple((x,r+1) for x,r in s);b=zmul(small,small);val=zmul(b,b);assert sha(rect(val).encode())==digest
 seed=f'import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalHybridEndpoint\nimport WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalLocalMoment\nimport WeilDefect.Generated.NF632.Pi\n\n{head}\ndef {n}Arg : NF591Rect := {rect(arg)}\ndef {n}State0000 : NF633ExpState := {state(*states[0])}\ntheorem {n}Prefix0000 : neutralNF633State {n}Arg neutralNF616Q 0={n}State0000 := by\n  apply neutralNF633StateEq_sound\n  decide +kernel\n'
 write(tag+'Seed',seed+end);prior=tag+'Seed';ks=list(states)[1:];prev=0
 for k in range(0,len(ks),8):
  file=tag+f'Part{k//8:02d}';src=f'import {root}.{prior}\n\n'+head
  for j in ks[k:k+8]:
   src+=f'\ndef {n}State{j:04d} : NF633ExpState := {state(*states[j])}\ntheorem {n}Gate{j:04d} : neutralNF633StateEq (neutralNF633Segment {n}Arg neutralNF616Q {prev} {n}State{prev:04d} {j-prev}) {n}State{j:04d}=true := by\n  decide +kernel\ntheorem {n}Prefix{j:04d} : neutralNF633State {n}Arg neutralNF616Q {j}={n}State{j:04d} :=\n  neutralNF633Prefix_extend {n}Arg neutralNF616Q {prev} {j-prev} {n}State{prev:04d} {n}State{j:04d} {n}Prefix{prev:04d} {n}Gate{j:04d}\n';prev=j
  write(file,src+end);prior=file
 src=f'''import {root}.{prior}
{head}
def {n}Small : NF591Rect := {rect(small)}
def {n}Value : NF591Rect := {rect(val)}
theorem {n}ArgCheck : neutralNF633RectEq (neutralNF592PhaseArg nf632Pi {rat(f)} neutralNF616Q) {n}Arg=true := by
  decide +kernel
theorem {n}SmallCheck : neutralNF633RectEq ({n}State1200.sumState.expand (1/(neutralNF616Q:ℚ))) {n}Small=true := by
  decide +kernel
theorem {n}ValueCheck : neutralNF633RectEq (({n}Small.mulQ {n}Small neutralNF616Q).mulQ ({n}Small.mulQ {n}Small neutralNF616Q) neutralNF616Q) {n}Value=true := by
  decide +kernel
theorem {n}OriginalEq : neutralNF593Phase nf632Pi {rat(f)} neutralNF616Q neutralNF616ExpN={n}Value := by
  apply neutralNF633Phase_of_small nf632Pi {rat(f)} neutralNF616Q neutralNF616ExpN {n}Small {n}Value
  · rw [neutralNF633RectEq_sound _ _ {n}ArgCheck]
    exact neutralNF633SmallExp_of_state {n}Arg neutralNF616Q neutralNF616ExpN {n}State1200 {n}Small {n}Prefix1200 {n}SmallCheck
  · exact {n}ValueCheck
theorem {n}Sound : {n}Value.Contains (nf618HybridPhase {rat(f)}) := by
  rw [← {n}OriginalEq, neutralNF593Phase_eq]
  exact neutralNF592PhaseBall_sound nf632Pi nf632PiSound {rat(f)} neutralNF616Q neutralNF616ExpN (by decide +kernel) (by decide +kernel) neutralNF616ExpFee
'''
 write(tag,src+end);names.extend([n+'OriginalEq',n+'Sound']);phases.append({'phase':str(v),'module':tag})
broot=Path('WeilDefect/Generated/NF690');mb=(broot/'manifest.json').read_bytes()
assert sha(mb)=='8d064584205c62907a397ebc854630a5481a675923648dcdcb7c4051af218bf7'
slots={r['index']:r for r in json.loads(mb)['slots']}
ids=[86,3313,5833,5842,5847,5849,5859,5862,5867,5874,5881,5888,5895,5900,5909,5919,5924,5933,5940,5948,5955,5963,5969,5976,5982,5993,6002,6009,6020,6029,6041,6052,6060,6074,6087,6812,7821]
for i in ids:
 t=slots[i];ch=t['chunk'];off=t['offset'];h,f=map(F,t['key']);sign=-1 if i==86 else 1;positive=i not in (86,6812)
 raw=re.findall(r'#\[\n    (.*?)\n  \]',(broot/(ch+'.lean')).read_text(),re.S)[off]
 signedf=f if positive else -f;rep=sign*F(13,44);u=signedf*F(11,10)
 assert u-(u+F(1,2))//1==sign*F(13,40)
 tag='Phase0726' if sign==1 else 'Phase0727';pn='nf618Pilot'+tag;n=f'nf618PilotSlot{i:05d}';file=f'Slot{i:05d}'
 if h==0:rp=rn='NF591Rect.one';sp=sn='nf618PilotUnitSound'
 elif abs(h)==F(1,2):
  rp,rn,sp,sn=('nf703Real0001Value','nf703Real0003Value','nf618PilotRealNeg','nf618PilotRealPos') if h<0 else ('nf703Real0003Value','nf703Real0001Value','nf618PilotRealPos','nf618PilotRealNeg')
 else:raise ValueError(h)
 src=f'''import {root}.{tag}
import {root}.Amplitude
import WeilDefect.Generated.NF690.Bank
{head}
def {n}Table : NF624KeyTable := ⟨⟨{rat(h)}, {rat(f)}⟩, (nf690{ch}[{off}]?).getD #[]⟩
def {n}Cache : NF617MomentCache := nf618HybridCache nf632Pi {rat(h)} {rat(f)} neutralNF616Q {rp} {rn} {pn}Value {str(positive).lower()}
theorem {n}PhaseIdentity : nf618HybridPhase {rat(signedf)} = nf618HybridPhase {rat(rep)} := by
  unfold nf618HybridPhase
  rw [neutralNF592Phase_identity, neutralNF592Phase_identity]
  rw [show neutralNF592Reduced {rat(signedf)}=neutralNF592Reduced {rat(rep)} from by decide +kernel]
theorem {n}CacheSound : {n}Cache.SemanticSound {n}Table.key := by
  apply nf618HybridCache_sound nf632Pi nf632PiSound {rat(h)} {rat(f)} neutralNF616Q {'' if False else '(by decide +kernel)'} {rp} {rn}
  · convert {sp} using 1 <;> norm_num
  · convert {sn} using 1 <;> norm_num
  · change {pn}Value.Contains (nf618HybridPhase {rat(signedf)})
    rw [{n}PhaseIdentity]
    exact {pn}Sound
theorem {n}RowsCheck : (List.range {n}Table.rows.size).all (neutralNF617MomentRowCheck {n}Cache {n}Table.key.lower neutralNF616Q {n}Table.rows)=true := by
  decide +kernel
theorem {n}Sound : neutralNF690TableSound {n}Table := by
  apply neutralNF690TableSound_of_semantic_cache {n}Cache {n}Table {n}CacheSound (by decide +kernel) neutralNF616Q (by decide +kernel)
  intro n hn
  exact List.all_eq_true.mp {n}RowsCheck n (List.mem_range.mpr hn)
theorem {n}Concrete : neutralNF690TableSound (neutralNF624BankRead nf690OriginalBank {i}) := by
  rw [show nf690OriginalBank = neutralNF690Bank nf687Read nf687Size nf690Payload from rfl]
  rw [neutralNF690Bank_read nf687Read nf687Size nf690Payload {i} (by decide +kernel)]
  rw [neutralNF690Table_eq nf687Read nf690Payload {i} {n}Table (by decide +kernel) (by rfl) (by decide +kernel)]
  exact {n}Sound
'''
 write(file,src+end);names.extend(n+x for x in ('PhaseIdentity','CacheSound','RowsCheck','Sound','Concrete'));records.append({'slot':i,'key':t['key'],'rows':t['rows'],'sign':sign,'source_row_sha256':sha(raw.encode()),'module':file})
amp='''import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalHybridEndpoint
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable
import WeilDefect.Generated.NF703.Real0001
import WeilDefect.Generated.NF703.Real0003
namespace WeilDefect
set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem nf618PilotUnitSound : NF591Rect.one.Contains (Complex.exp ((0:ℂ)*(11/10))) := by
  norm_num [NF591Rect.one,NF591Rect.Contains,NF591Ball.Contains]
theorem nf618PilotRealNeg : nf703Real0001Value.Contains (Complex.exp ((-1/2:ℚ)*(11/10:ℂ))) := by
  rw [← nf703Real0001OriginalEq, neutralNF621RealEndpoint_eq]
  exact neutralNF615RealEndpoint_sound (-1/2) (by norm_num) neutralNF616Q neutralNF616ExpN (by decide +kernel) (by decide +kernel) neutralNF616ExpFee
theorem nf618PilotRealPos : nf703Real0003Value.Contains (Complex.exp ((1/2:ℚ)*(11/10:ℂ))) := by
  rw [← nf703Real0003OriginalEq, neutralNF621RealEndpoint_eq]
  exact neutralNF615RealEndpoint_sound (1/2) (by norm_num) neutralNF616Q neutralNF616ExpN (by decide +kernel) (by decide +kernel) neutralNF616ExpFee
end WeilDefect
'''
write('Amplitude',amp);names.extend(['nf618PilotUnitSound','nf618PilotRealNeg','nf618PilotRealPos'])
write('Audit0726',''.join(f'import {root}.{r["module"]}\n' for r in records)+''.join(f'#print axioms WeilDefect.{n}\n' for n in names))
files={f.name:sha(f.read_bytes()) for f in out.glob('*.lean')}
assert len(files)==53 and len(names)==192 and sum(r['rows'] for r in records)==87
assert sha('\n'.join(f"{r['slot']}:{r['source_row_sha256']}" for r in records).encode())=='7f49dc338c94ea053afec7c4ff43521c7d0c7dafe82163d6eef718bec21e5835'
fingerprint=sha('\n'.join(f'{n}:{h}' for n,h in sorted(files.items())).encode())
assert fingerprint=='9fdc64081e2d5732781d86ba9a01443ab5ced0cfcc28c4287362486211a65eb3',fingerprint
(out/'manifest.json').write_text(json.dumps({'phases':phases,'tables':records,'theorems':names,'files':files,'source_fingerprint':fingerprint},indent=2)+'\n')
print('NF618 pilot source PASS',len(files),len(records),len(names),fingerprint)
