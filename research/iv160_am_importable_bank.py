#!/usr/bin/env python3
"""Deterministic importable proof source generator, not a verifier.
No evidence manifest is accepted as a proof. The generated modules
must be kernel checked and their terminal declaration axiom-audited."""
from pathlib import Path
import argparse

p=argparse.ArgumentParser()
p.add_argument('--root',type=Path,default=Path('WeilDefect/Arithmetic/IV160Bank'))
p.add_argument('--kind',choices=['sym','row','both'],default='both')
p.add_argument('--start',type=int,default=0)
p.add_argument('--stop',type=int)
p.add_argument('--assemble',action='store_true')
a=p.parse_args()
root=a.root
root.mkdir(parents=True,exist_ok=True)
module='WeilDefect.Arithmetic.IV160Bank'
for kind,N,pred,dep in [
    ('Sym',128,'neutralIV157SymBlock','ActualZetaIV157AMSymmetryPilot'),
    ('Row',1024,'neutralIV159RowBlock','ActualZetaIV159AMRowReceiver')]:
    if a.kind not in ('both',kind.lower()): continue
    stop=N if a.stop is None else a.stop
    assert 0<=a.start<stop<=N and a.start%2==0 and stop%2==0
    for b in range(a.start,stop,2):
        stem=f'{kind}{b:04}'
        s=f'import WeilDefect.Arithmetic.{dep}\nnamespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
        for j in (b,b+1):
            n=f'neutralIV159{kind}_{j:04}'
            s+=f'theorem {n} : {pred} {j} = true := by decide\n#print axioms {n}\n'
        (root/(stem+'.lean')).write_text(s+'end WeilDefect\n')
    if a.assemble:
        assert stop%8==0
        missing=[b for b in range(0,stop,2) if not (root/f'{kind}{b:04}.lean').is_file()]
        assert not missing,missing
        # Use an eight-block local dispatch (four imported proof modules)
        # and a small top-level dispatch tree, not a single 1024-way fin_cases.
        for b in range(0,stop,8):
            s=''.join(f'import {module}.{kind}{j:04}\n' for j in range(b,b+8,2))
            s+='namespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
            s+=f'theorem neutralIV160{kind}Group_{b:04} (i : ℕ) (hl : {b} ≤ i) (hu : i < {b+8}) : {pred} i = true := by\n'
            s+='  interval_cases i\n'
            s+=''.join(f'  · exact neutralIV159{kind}_{j:04}\n' for j in range(b,b+8))
            s+=f'#print axioms neutralIV160{kind}Group_{b:04}\n'
            (root/f'{kind}Group{b:04}.lean').write_text(s+'end WeilDefect\n')
        s=''.join(f'import {module}.{kind}Group{b:04}\n' for b in range(0,stop,8))
        s+='namespace WeilDefect\nset_option maxRecDepth 100000\nset_option maxHeartbeats 0\n'
        bank=f'{kind}Bank' if stop==N else f'{kind}Prefix{stop:04}'
        s+=f'theorem neutralIV160{bank} (i : ℕ) (hi : i < {stop}) : {pred} i = true := by\n'
        s+=f'  have hb : i/8 < {stop//8} := by omega\n  generalize hq : i/8 = q at hb\n  interval_cases q\n'
        # interval_cases on an expression with named equation may require
        # elaboration repair; no claim of compilation.
        s+=''.join(f'  · exact neutralIV160{kind}Group_{b:04} i (by omega) (by omega)\n' for b in range(0,stop,8))
        s+=f'#print axioms neutralIV160{bank}\nend WeilDefect\n'
        (root/f'{bank}.lean').write_text(s)
if a.assemble and a.kind=='both' and a.stop is None:
    (root/'Terminal.lean').write_text(f'''import {module}.SymBank
import {module}.RowBank
import WeilDefect.Arithmetic.ActualZetaIV160AMTerminalReceiver

namespace WeilDefect
noncomputable section
open MeasureTheory
open scoped SchwartzMap BigOperators

theorem neutralIV160Terminal (f : 𝓢(ℝ,ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-2:ℝ) 2 → f x = 0) :
    ‖∑' n : ℕ, neutralIV085PrimeSummand (neutralIV103Correlation 2 f f) n‖ ≤
      (7979648/1000000:ℝ)*∫ x : ℝ, ‖f x‖^2 :=
  neutralIV160Original_bound neutralIV160SymBank neutralIV160RowBank f hs

#print axioms neutralIV160Terminal
end
end WeilDefect
''')
