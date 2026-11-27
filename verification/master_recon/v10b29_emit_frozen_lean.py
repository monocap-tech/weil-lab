"""Emit the concrete V10B29Frozen Lean source from authenticated V10B19 data.
Usage: python v10b29_emit_frozen_lean.py INPUT OUTPUT
This is an uncompiled candidate; the file must be audited with V10B29c.
"""
import hashlib,json,sys
from pathlib import Path
p=Path(sys.argv[1]);d=json.loads(p.read_text())
assert hashlib.sha256(p.read_bytes()).hexdigest()=='bccbd53fd2e02cb887868f588ef7f8765e780086f7fabe748518d5685d7c7616'
rows=d['trial']
assert d['denominator']==2**48 and len(rows)==16 and all(len(row)==160 for row in rows)
source='''import WeilDefect.MasterRecon.V10B29c

/-! Frozen V10B19 integer trials. This generated module is a source candidate,
not a compiled certificate. Parent SHA256 bccbd53fd2e02cb887868f588ef7f8765e780086f7fabe748518d5685d7c7616. -/
namespace WeilDefect.MasterRecon.V10B29Frozen

open MeasureTheory
open scoped BigOperators

def trialNumerators : List (List ℤ) := [
'''
source+=',\n'.join('  ['+', '.join(map(str,row))+']' for row in rows)+']\n'
source+='''
def coeffNumerator (i : Fin 16) (k : ℕ) : ℤ :=
  (2:ℤ)^k * ∑ j ∈ Finset.range 160,
    if k ≤ j then ((trialNumerators.getD i.val []).getD j 0) *
      (-1:ℤ)^(j-k) * (j.choose k:ℤ) * ((j+k).choose k:ℤ)
    else 0

noncomputable def coeff (i : Fin 16) (k : ℕ) : ℂ :=
  (coeffNumerator i k:ℂ)/281474976710656

noncomputable def physicalPolynomial (i : Fin 16) : ℝ → ℂ :=
  V10B29b.poly 160 (coeff i)

theorem frozen_trial_exists (i : Fin 16)
    (hS : V10B23b.SeriesSupply) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) :
    ∃ g : V08I.logCarrier (1/4),
      (V08I.physicalInclusion (1/4) g : ℝ → ℂ) =ᵐ[volume]
        V10B28c.trial (1/4) (physicalPolynomial i) :=
  V10B29b.poly_carrier_exists 160 (coeff i) hS C hC

end WeilDefect.MasterRecon.V10B29Frozen

#print axioms WeilDefect.MasterRecon.V10B29Frozen.frozen_trial_exists
'''
out=Path(sys.argv[2]);out.write_text(source)
assert hashlib.sha256(out.read_bytes()).hexdigest()=='14e606eff7374111f83f7eaaaf3e7a06b41c250f0b3b63cfb8df3358106b163f'
print('Frozen Lean source hash matches; native compilation outstanding.')
