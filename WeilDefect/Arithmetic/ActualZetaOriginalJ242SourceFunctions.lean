import WeilDefect.Arithmetic.ActualZetaOriginalJ242ExponentialSignature
import Mathlib.Analysis.SpecialFunctions.Trigonometric.DerivHyp

namespace WeilDefect
noncomputable section

/-!
NF545 original selected FUNCTIONS, not only an anonymous 242-element
Hilbert basis. They use the EXACT NF407 frequency/order signature
and the fixed genuine sinh-pole row 241.

Source fidelity is independently checked by the SHA-pinned NF545
Python auditor against the original NF407 JSON; Lean itself checks
the rational signature but not the source JSON file's SHA256.
-/

/-- Expand each of the 67 ACTUAL original oscillator frequencies into
its historical contiguous source monomial rows k=0,...,m_f-1. -/
def nf545OriginalSelectedOscillatorNodes : List (ℚ × ℕ) :=
  nf545OriginalSelectedFrequencyGroups.flatMap fun group =>
    (List.range group.2).map fun k => (group.1, k)

/-- The actual source oscillator-node expansion has exactly 241 rows.
The 242nd original selected generator is the separate sinh pole. -/
theorem nf545OriginalSelectedOscillatorNodes_length :
    nf545OriginalSelectedOscillatorNodes.length = 241 := by
  decide

/-- The source-exact rational frequency and monomial order for an
original non-pole selected mode. The fixed index is preserved. -/
def nf545OriginalOscillatorNodeAt (i : Fin 241) : ℚ × ℕ :=
  nf545OriginalSelectedOscillatorNodes[i.val]'(by
    rw [nf545OriginalSelectedOscillatorNodes_length]
    exact i.isLt)

/-- The actual original odd real source generator in each of the
242 selected rows. Even monomial orders carry sine, odd orders carry
cosine, and the true last mode is sinh(x/2). These are the original
physical J242 functions, not numerical samples or a polynomial proxy. -/
def nf545OriginalSelectedRealGenerator (i : Fin 242) (x : ℝ) : ℝ :=
  if hi : i.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨i.val, hi⟩
    x ^ node.2 *
      (if Even node.2 then
        Real.sin (2 * Real.pi * (node.1 : ℝ) * x)
      else
        Real.cos (2 * Real.pi * (node.1 : ℝ) * x))
  else
    Real.sinh (x / 2)

/-- The last entry is exactly the genuine original sinh pole. -/
theorem nf545OriginalSelectedPole_is_sinh (x : ℝ) :
    nf545OriginalSelectedRealGenerator ⟨241, by omega⟩ x =
      Real.sinh (x / 2) := by
  simp [nf545OriginalSelectedRealGenerator]

end
end WeilDefect
