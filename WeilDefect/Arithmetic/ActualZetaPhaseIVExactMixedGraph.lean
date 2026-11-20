import WeilDefect.Arithmetic.ActualZetaOriginalCollarCoercivity
import WeilDefect.Arithmetic.ActualZetaOriginalSignedGraphForm
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open InnerProductSpace MeasureTheory
open scoped SchwartzMap ComplexConjugate

/-!
IV003: exact *source-specific* signed mixed form on the already-constructed
actual full-divisor graph. This line is independent of the Phase III
matrix/product runners and uses no NF702/NF703 numerical source objects.

Mathlib's complex inner product is linear in its SECOND slot. We reverse
the arguments below to make the mixed Weil form linear in its FIRST
argument (the convention of the centered test-function Weil pairing).

No assertion of global positivity is made: the difference of P/N Hilbert
inner products can be indefinite. Graph-norm continuity is not the same
as physical L²-continuity. A graph lift of every arbitrary compact smooth
test and an unwindowed EF identification remain additional obligations.
-/

/-- Full-divisor, multiplicity-preserving signed Hermitian mixed form.
Its diagonal is the existing NF598 signed graph Weil energy. -/
def neutralIV003GraphMixed (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a) : ℂ :=
  (inner ℂ (neutralActualZetaPositiveAnalysis a v)
      (neutralActualZetaPositiveAnalysis a u) -
   inner ℂ (neutralActualZetaNegativeAnalysis a v)
      (neutralActualZetaNegativeAnalysis a u)) / 2

theorem neutralIV003GraphMixed_linear_first_add (a : ℝ)
    (u v w : NeutralActualZetaSourceDomain a) :
    neutralIV003GraphMixed a (u + v) w =
      neutralIV003GraphMixed a u w + neutralIV003GraphMixed a v w := by
  simp only [neutralIV003GraphMixed, map_add, inner_add_right]
  ring

theorem neutralIV003GraphMixed_linear_first_smul (a : ℝ)
    (z : ℂ) (u v : NeutralActualZetaSourceDomain a) :
    neutralIV003GraphMixed a (z • u) v =
      z * neutralIV003GraphMixed a u v := by
  simp only [neutralIV003GraphMixed, map_smul, inner_smul_right, smul_eq_mul]
  ring

/-- The diagonal is REAL, with precisely the existing NF598 factor 1/2. -/
theorem neutralIV003GraphMixed_self (a : ℝ)
    (u : NeutralActualZetaSourceDomain a) :
    neutralIV003GraphMixed a u u =
      (neutralNF598GraphWeil a u : ℂ) := by
  unfold neutralIV003GraphMixed neutralNF598GraphWeil
  rw [inner_self_eq_norm_sq_to_K, inner_self_eq_norm_sq_to_K]
  push_cast
  ring

theorem neutralIV003GraphMixed_self_re (a : ℝ)
    (u : NeutralActualZetaSourceDomain a) :
    (neutralIV003GraphMixed a u u).re = neutralNF598GraphWeil a u := by
  rw [neutralIV003GraphMixed_self]
  rfl

theorem neutralIV003GraphMixed_continuous (a : ℝ) :
    Continuous (fun p : NeutralActualZetaSourceDomain a ×
        NeutralActualZetaSourceDomain a =>
        neutralIV003GraphMixed a p.1 p.2) := by
  let P := neutralActualZetaPositiveAnalysis a
  let N := neutralActualZetaNegativeAnalysis a
  have hpu : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => P p.1) :=
    P.continuous.comp continuous_fst
  have hpv : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => P p.2) :=
    P.continuous.comp continuous_snd
  have hnu : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => N p.1) :=
    N.continuous.comp continuous_fst
  have hnv : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => N p.2) :=
    N.continuous.comp continuous_snd
  have hP : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => inner ℂ (P p.2) (P p.1)) :=
    hpv.inner (𝕜 := ℂ) hpu
  have hN : Continuous (fun p : NeutralActualZetaSourceDomain a ×
      NeutralActualZetaSourceDomain a => inner ℂ (N p.2) (N p.1)) :=
    hnv.inner (𝕜 := ℂ) hnu
  exact (hP.sub hN).div_const 2

/-- The EXISTING genuine full-divisor source algebra already knows the
*off-diagonal* P/N difference at each actual zero and multiplicity copy.
This is an exact mixed zero-side dictionary, not a positivity bound,
and it does not yet sum to an unrestricted external EF mixed formula. -/
theorem neutralIV003GraphMixed_coordinate (a : ℝ)
    (u v : NeutralActualZetaSourceDomain a)
    (q : NeutralActualZetaDivisorCoordinate) :
    conj (neutralActualZetaPositiveAnalysis a u q) *
        neutralActualZetaPositiveAnalysis a v q -
      conj (neutralActualZetaNegativeAnalysis a u q) *
        neutralActualZetaNegativeAnalysis a v q =
      conj (neutralWindowEvaluation a
        (conj (neutralActualZetaDivisorOrdinate q))
        (neutralNF598GraphPhysical a u)) *
        neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
          (neutralNF598GraphPhysical a v) +
      conj (neutralWindowEvaluation a (neutralActualZetaDivisorOrdinate q)
        (neutralNF598GraphPhysical a u)) *
        neutralWindowEvaluation a
          (conj (neutralActualZetaDivisorOrdinate q))
          (neutralNF598GraphPhysical a v) := by
  have hu := neutralActualZetaSourceAnalysis_sampling a u q
  have hv := neutralActualZetaSourceAnalysis_sampling a v q
  rw [hu.1, hu.2, hv.1, hv.2]
  exact neutralLogPairSource_mixed_difference a
    (neutralActualZetaDivisorOrdinate q)
    (neutralActualZetaSourcePhysical a u)
    (neutralActualZetaSourcePhysical a v)

/-- The local EF support bound also controls the exact signed full
source-graph mixed diagonal, provided the lift represents that
supported test. It supplies NO mixed estimate for separated supports. -/
theorem neutralIV003LocalGraphDiagonal_coercive
    (u : NeutralActualZetaSourceDomain (11/10:ℝ))
    (s : 𝓢(ℝ,ℂ))
    (hs : ∀ x, x ∉ neutralNF543OriginalCollars → s x = 0)
    (hp : neutralNF598GraphPhysical (11/10) u = s.toLp 2 volume) :
    (2/5:ℝ) * ‖s.toLp 2 volume‖^2 ≤
      (neutralIV003GraphMixed (11/10) u u).re := by
  rw [neutralIV003GraphMixed_self_re]
  have h := neutralNF600SmoothCollarLower s hs
  rw [neutralNF598GraphWeil_eq_smooth u s hs hp]
  exact h

#print axioms neutralIV003GraphMixed_linear_first_add
#print axioms neutralIV003GraphMixed_linear_first_smul
#print axioms neutralIV003GraphMixed_self
#print axioms neutralIV003GraphMixed_self_re
#print axioms neutralIV003GraphMixed_continuous
#print axioms neutralIV003GraphMixed_coordinate
#print axioms neutralIV003LocalGraphDiagonal_coercive

end WeilDefect
