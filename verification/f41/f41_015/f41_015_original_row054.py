#!/usr/bin/env python3
"""F41-015: genuine original NF674 physical row54 against the full NF702 payment.

Emitter is a PROPOSAL, never a certificate. Only later Lean compilation, strict
axiom audit and independent archived source reconciliation can promote row54.
"""
import argparse
import gzip
import hashlib
import json
import sys
import zipfile
from fractions import Fraction as F
from pathlib import Path

sys.set_int_max_str_digits(0)
ROW = 54
N = 242
SOURCE_SHA = 'a431f903254000bb5ad8edbc276ccc8599da98f5'
H_ARCHIVE = 'e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9'
H_INNER = '9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6'
INPUT_ARCHIVE = '258637da71e96468ed7c6ac5b0a4480ce06cdee9989aef8e71a4cd09059789e0'
PAY_INNER = 'e6eac42fde8404c5198c78eebe56fdd3fb543549079695a641c9cc60acca9b03'
ALLOWED = {'propext', 'Classical.choice', 'Quot.sound'}
SUFFIXES = ('HRowGate','HColGate','VGate','EH','EV','ActualPayment')

def sha(data):
    return hashlib.sha256(data).hexdigest()

def hashfile(p):
    return sha(Path(p).read_bytes())

def row_values(records, i=ROW):
    assert len(records) == N and [r['row'] for r in records] == list(range(N))
    for j, r in enumerate(records):
        assert len(r['H_lower']) == j+1 and len(r['V']) == 4
        assert all(len(v)==2 and int(v[1]) >= 0 for v in r['H_lower']+r['V'])
    return ([int(records[max(i,j)]['H_lower'][min(i,j)][0]) for j in range(N)],
            [int(v[0]) for v in records[i]['V']])

def selftest():
    rec=[{'row':i,'H_lower':[[i*1000+j,0] for j in range(i+1)],
          'V':[[i*10+j,0] for j in range(4)]} for i in range(N)]
    h,v=row_values(rec)
    assert len(h)==N and len(v)==4 and h[0]==54000 and h[54]==54054
    assert h[241]==241054 and v==[540,541,542,543]
    rec[54]['H_lower'][0][1]=-1
    try: row_values(rec)
    except AssertionError: pass
    else: raise AssertionError('negative-radius mutation unexpectedly accepted')
    rec[54]['H_lower'][0][1]=0
    rec[54]['row']=55
    try: row_values(rec)
    except AssertionError: pass
    else: raise AssertionError('wrong-index mutation unexpectedly accepted')
    assert len(SUFFIXES)==6 and ROW not in range(54)
    print('F41-015 strict row projection selftest PASS (2/2 mutations rejected); NO numerical certificate')

def emit(archive:Path, input_root:Path, output:Path):
    # Import the exact historical generator functions; no modified arithmetic.
    from emit_nf675_original_literal_first_row import get_631, rat, vec, N as original_N, Q
    from emit_nf627_original_moment_bank import filetext
    assert original_N==N and hashfile(archive)==H_ARCHIVE
    _,_,eh,ev,head,summary=get_631(archive)
    assert summary['widened_entry_sha256']==H_INNER
    with zipfile.ZipFile(archive) as z:
        names=[name for name in z.namelist() if Path(name).name=='nf631-widened-entries.jsonl.gz']
        assert len(names)==1
        contents=z.read(names[0])
        assert sha(contents)==H_INNER
    lines=gzip.decompress(contents).splitlines()
    assert len(lines)==N+1
    assert json.loads(lines[0])['scale']=='10^2600'
    records=[json.loads(x) for x in lines[1:]]
    h,v=row_values(records)
    ims=[p for p in input_root.rglob('manifest.json') if p.parent.name=='NF702Inputs']
    audits=list(input_root.rglob('nf702-input-complete-audit.json'))
    assert len(ims)==len(audits)==1
    inp=ims[0].parent
    m=json.loads(ims[0].read_bytes())
    a=json.loads(audits[0].read_bytes())
    assert m['schema']==a['schema']=='NF702-original-global-input-projection-v1'
    assert a['manifest_sha256']==hashfile(ims[0])
    assert m['entries_sha256']==H_INNER and m['payment_sha256']==PAY_INNER
    assert m['rows']==N and [r['row'] for r in m['projection_rows']]==list(range(8))
    assert set(a['axioms'])=={'nf702InputH_symm','nf702OriginalW'} | {s for r in m['projection_rows'] for s in r['theorems']}
    assert len(a['axioms'])==50 and all(set(v)<=ALLOWED for v in a['axioms'].values())
    for item in m['files']:
        assert hashfile(inp/item['file'])==item['sha256'],item['file']
    output.mkdir(parents=True,exist_ok=True)
    stem='f41015Row054'
    body='set_option maxRecDepth 100000\nset_option maxHeartbeats 0\n\n'
    body+=vec(stem+'H',h)+vec(stem+'V',v)
    body+=f'''def {stem}Payment : NF625PaymentData :=
  ⟨fun _ _ => 0,
   fun a b => if a.val = {ROW} then {stem}H[b.val]!
              else if b.val = {ROW} then {stem}H[a.val]!
              else 0,
   fun a b => if a.val = {ROW} then {stem}V[b.val]! else 0,
   fun _ => 0, {rat(F(eh,Q))}, {rat(F(ev,Q))}, 0⟩

theorem {stem}Fast : neutralNF674OriginalRowCheck
    nf691OriginalLookup {stem}Payment ({ROW}:Fin 242) = true := by
  decide +kernel

theorem {stem}ActualBank : neutralNF674OriginalRowCheck
    (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
    {stem}Payment ({ROW}:Fin 242) = true := by
  rw [nf691OriginalLookup_eq]
  exact {stem}Fast

theorem {stem}PaymentTransport (p : NF625PaymentData)
    (hrow : ∀ j : Fin 242, {stem}Payment.H0 ({ROW}:Fin 242) j = p.H0 ({ROW}:Fin 242) j)
    (hcol : ∀ j : Fin 242, {stem}Payment.H0 j ({ROW}:Fin 242) = p.H0 j ({ROW}:Fin 242))
    (hV : ∀ j : Fin 4, {stem}Payment.V0 ({ROW}:Fin 242) j = p.V0 ({ROW}:Fin 242) j)
    (heH : {stem}Payment.eH = p.eH) (heV : {stem}Payment.eV = p.eV) :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      p ({ROW}:Fin 242) = true :=
  neutralNF675OriginalRow_true_of_projection _ _ _ _ hrow hcol hV heH heV
    {stem}ActualBank

#print axioms {stem}Fast
#print axioms {stem}ActualBank
#print axioms {stem}PaymentTransport
'''
    rowpath=output/'Row054.lean'
    rowpath.write_text(filetext(['WeilDefect.Generated.NF691.OriginalLookup',
       'WeilDefect.Arithmetic.ActualZetaOriginalPhysicalLiteralRowProjection'],body))
    attach='f41015Attach054'
    full=f'''set_option maxRecDepth 100000
set_option maxHeartbeats 0

theorem {attach}HRowGate :
    (List.finRange 242).all (fun j =>
      decide ({stem}Payment.H0 ({ROW}:Fin 242) j =
        nf702OriginalInputs.payment.H0 ({ROW}:Fin 242) j)) = true := by
  decide +kernel

theorem {attach}HColGate :
    (List.finRange 242).all (fun j =>
      decide ({stem}Payment.H0 j ({ROW}:Fin 242) =
        nf702OriginalInputs.payment.H0 j ({ROW}:Fin 242))) = true := by
  decide +kernel

theorem {attach}VGate :
    (List.finRange 4).all (fun j =>
      decide ({stem}Payment.V0 ({ROW}:Fin 242) j =
        nf702OriginalInputs.payment.V0 ({ROW}:Fin 242) j)) = true := by
  decide +kernel

theorem {attach}EH : {stem}Payment.eH = nf702OriginalInputs.payment.eH := by
  decide +kernel

theorem {attach}EV : {stem}Payment.eV = nf702OriginalInputs.payment.eV := by
  decide +kernel

theorem {attach}ActualPayment :
    neutralNF674OriginalRowCheck
      (neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank))
      nf702OriginalInputs.payment ({ROW}:Fin 242) = true := by
  apply {stem}PaymentTransport
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {attach}HRowGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {attach}HColGate) j (by simp))
  · intro j
    exact of_decide_eq_true ((List.all_eq_true.mp {attach}VGate) j (by simp))
  · exact {attach}EH
  · exact {attach}EV

'''
    full+='\n'.join('#print axioms '+attach+x for x in SUFFIXES)+'\n'
    attachpath=output/'Attach054.lean'
    attachpath.write_text(filetext(['WeilDefect.Generated.NF702Inputs.Data',
                                    'WeilDefect.Generated.F41015.Row054'],full))
    names=[stem+x for x in ('Fast','ActualBank','PaymentTransport')]+[attach+x for x in SUFFIXES]
    manifest={'schema':'F41-015-original-physical-row054-proposal-v1',
      'source_original_commit':SOURCE_SHA,'research_replay_commit':'3d3fa66956bef3a63f90ed9b5325141afaf43cb5',
      'original_nf631_entries_archive_sha256':H_ARCHIVE,'original_nf631_entries_gzip_sha256':H_INNER,
      'nf702_original_input_archive_sha256':INPUT_ARCHIVE,
      'nf702_input_manifest_sha256':hashfile(ims[0]),
      'nf702_original_payment_payload_sha256':PAY_INNER,
      'original_bank':'neutralNF624Lookup nf690OriginalBank (neutralNF624Index nf690OriginalBank)',
      'original_payment':'nf702OriginalInputs.payment',
      'row':ROW,'H_lower_comparisons':ROW+1,'V_mixed_comparisons':4,
      'center_symmetry_comparisons':N,
      'radius_H':str(F(eh,Q)),'radius_V':str(F(ev,Q)),
      'generated_files':{p.name:hashfile(p) for p in (rowpath,attachpath)},
      'axiom_names':names,
      'actual_payment_Lean_passed':False,'full_F41_matrix_certified':False,'F42_positive':False,'RH_proved':False}
    (output/'manifest.json').write_text(json.dumps(manifest,indent=2,sort_keys=True)+'\n')
    print('F41-015 original row54 Lean PROPOSAL, 55 H lower + 4 V + 242 centers; no acceptance')

def audit(output:Path, log:Path):
    m=json.loads((output/'manifest.json').read_text())
    assert m['schema']=='F41-015-original-physical-row054-proposal-v1' and m['row']==ROW
    for filename,dig in m['generated_files'].items():
        assert hashfile(output/filename)==dig
    import re
    names=set(m['axiom_names'])
    assert len(names)==9
    found={}
    for line in log.read_text().splitlines():
        mm=re.fullmatch(r"'WeilDefect\.([^']+)' depends on axioms: \[([^\]]*)\]",line)
        if mm and mm[1] in names:
            assert mm[1] not in found
            found[mm[1]]={x.strip() for x in mm[2].split(',') if x.strip()}
        mm=re.fullmatch(r"'WeilDefect\.([^']+)' does not depend on any axioms",line)
        if mm and mm[1] in names:
            assert mm[1] not in found
            found[mm[1]]=set()
    assert set(found)==names,(len(found),names-set(found))
    assert all(x<=ALLOWED for x in found.values()),found
    m['axiom_report']={name:sorted(found[name]) for name in sorted(found)}
    m['source_sha256_links_reverified']=True
    m['actual_payment_Lean_passed']=True
    # This is only a local conditional Lean receipt; never promote F41 itself.
    (output/'f41-015-kernel-audit.json').write_text(json.dumps(m,indent=2,sort_keys=True)+'\n')
    print('F41-015 row54 exact full-payment Lean audit locally PASS; independent ZIP audit still due')

def main():
    p=argparse.ArgumentParser()
    sub=p.add_subparsers(dest='cmd',required=True)
    sub.add_parser('selftest')
    e=sub.add_parser('emit');e.add_argument('--archive',type=Path,required=True)
    e.add_argument('--input-dir',type=Path,required=True);e.add_argument('--output',type=Path,required=True)
    a=sub.add_parser('audit');a.add_argument('--output',type=Path,required=True)
    a.add_argument('--axioms-log',type=Path,required=True)
    z=p.parse_args()
    if z.cmd=='selftest': selftest()
    elif z.cmd=='emit':emit(z.archive,z.input_dir,z.output)
    else: audit(z.output,z.axioms_log)
if __name__=='__main__': main()