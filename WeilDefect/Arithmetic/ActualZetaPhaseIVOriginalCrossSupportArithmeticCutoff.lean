import WeilDefect.Arithmetic.ActualZetaPhaseIVOriginalCrossSupportExtension
import WeilDefect.Arithmetic.ActualZetaOriginalCollarPrimeBound
import Mathlib.Tactic

namespace WeilDefect
noncomputable section

open MeasureTheory
open scoped SchwartzMap ComplexConjugate BigOperators

/-!
IV011: authentic ORIGINAL mixed cross-support arithmetic reduction.

For an old Schwartz test s supported inside [-a,a] and a newly
admitted Schwartz test t supported inside [-b,b], a≤b, the original
two-input correlation C_b(s,t) is supported in [-a-b,a+b], a strictly
sharper statement than the generic doubled-window [-2b,2b] bound.

Consequently the EXACT von-Mangoldt mixed prime side of the literal
zeta EF is a FINITE sum, truncated past exp(a+b). Pole and gamma
contributions remain unchanged, so this is NOT a sign argument.

The second component gives the explicit original-source negative
Schur witness when the genuine mixed Weil determinant bound fails
and the new diagonal is strictly positive. Together with IV010,
this characterizes the exact missing one-new-support condition
without silently declaring that zeta satisfies it.
-/

/-- The actual original two-argument physical correlation agrees
pointwise with the unwindowed Schwartz translated product integral.
The equality is proved using the authentic L² representative a.e.
dictionary, preserving the direction of the two complex inputs. -/
theorem neutralIV011MixedCorrelation_eq_schwartzIntegral
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (τ : ℝ) :
    neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) τ =
      ∫ x : ℝ, t x * conj (s (x - τ)) := by
  have hswide : ∀ x : ℝ, x ∉ Set.Icc (-b) b → s x = 0 :=
    neutralIV006Schwartz_support_expand a b hab s hs
  have hsae := neutralIV006Schwartz_window_ae b s hswide
  have htae := neutralIV006Schwartz_window_ae b t ht
  have hshift :=
    (measurePreserving_sub_right volume τ).quasiMeasurePreserving.ae_eq_comp hsae
  unfold neutralWindowCorrelation
  apply integral_congr_ae
  filter_upwards [htae, hshift] with x htx hsx
  change neutralWindowRepresentative b (s.toLp 2 volume) (x - τ) =
    s (x - τ) at hsx
  rw [htx, hsx]

/-- SOURCE-SHARP mixed support radius a+b (not 2b). This holds for
arbitrary complex physical Schwartz inputs on distinct nested
supports and derives from the real translated overlap geometry. -/
theorem neutralIV011MixedCorrelation_vanish_far
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (τ : ℝ) (hfar : a + b < |τ|) :
    neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume) τ = 0 := by
  rw [neutralIV011MixedCorrelation_eq_schwartzIntegral a b hab s t hs ht τ]
  apply integral_eq_zero_of_ae
  filter_upwards [] with x
  by_cases htx : x ∈ Set.Icc (-b) b
  · have hsnot : x - τ ∉ Set.Icc (-a) a := by
      intro hsx
      have hbound : |τ| ≤ a + b := by
        apply abs_le.mpr
        constructor <;> linarith [htx.1, htx.2, hsx.1, hsx.2]
      exact (not_lt_of_ge hbound) hfar
    simp [hs (x - τ) hsnot]
  · simp [ht x htx]

/-- At any integer log frequency beyond the genuine sum of source
support radii, both ORIGINAL mixed prime samples vanish exactly. -/
theorem neutralIV011MixedPrime_logFar_vanish
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (n : ℕ) (hn : a + b < Real.log n) :
    neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (Real.log n) = 0 ∧
      neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
        (-Real.log n) = 0 := by
  have hp : a + b < |Real.log n| :=
    lt_of_lt_of_le hn (le_abs_self _)
  constructor
  · exact neutralIV011MixedCorrelation_vanish_far a b hab s t hs ht _ hp
  · exact neutralIV011MixedCorrelation_vanish_far a b hab s t hs ht _
      (by simpa only [abs_neg] using hp)

/-- Every pair of finite physical support radii has a NATURAL
prime cutoff. No prime-distribution hypothesis or RH is used. -/
theorem neutralIV011ExistsPrimeCutoff (a b : ℝ) :
    ∃ N : ℕ, ∀ n : ℕ, N ≤ n → a + b < Real.log n := by
  obtain ⟨N, hN⟩ := exists_nat_gt (Real.exp (a + b))
  refine ⟨N, ?_⟩
  intro n hn
  have hcast : (N : ℝ) ≤ (n : ℝ) := by exact_mod_cast hn
  have hgt : Real.exp (a + b) < (n : ℝ) := lt_of_lt_of_le hN hcast
  calc
    a + b = Real.log (Real.exp (a + b)) := (Real.log_exp _).symm
    _ < Real.log (n : ℝ) := Real.log_lt_log (Real.exp_pos _) hgt

/-- Exact ORIGINAL prime component of the literal mixed
Zeta23.EF.literatureRHS. The full actual von-Mangoldt
coefficient and both sign frequencies are preserved. -/
def neutralIV011OriginalMixedPrime (b : ℝ)
    (s t : 𝓢(ℝ, ℂ)) : ℂ :=
  ∑' n : ℕ,
    ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
      (neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
          (Real.log n) +
        neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
          (-Real.log n))

/-- Exact finite arithmetic prime formula for mixed supports:
all original prime-power terms at n≥N vanish, when
log(N)>a+b. This is a source-specific finite TRUNCATION,
not an approximation or a numerical error estimate. -/
theorem neutralIV011OriginalMixedPrime_eq_finite
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ)
    (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n) :
    neutralIV011OriginalMixedPrime b s t =
      ∑ n ∈ Finset.range N,
        ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
          (neutralWindowCorrelation b
            (s.toLp 2 volume) (t.toLp 2 volume) (Real.log n) +
          neutralWindowCorrelation b
            (s.toLp 2 volume) (t.toLp 2 volume) (-Real.log n)) := by
  unfold neutralIV011OriginalMixedPrime
  apply tsum_eq_sum
  intro n hn
  have hnN : N ≤ n := Nat.le_of_not_gt (by
    intro hlt
    exact hn (Finset.mem_range.mpr hlt))
  obtain ⟨hpos, hneg⟩ :=
    neutralIV011MixedPrime_logFar_vanish a b hab s t hs ht n (hN n hnN)
  simp [hpos, hneg]

/-- The unmodified two polar residues of the genuine zeta EF
on the same original mixed correlation. -/
def neutralIV011OriginalMixedPole (b : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℂ :=
  let k := neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
  Zeta23.paperFT k (Complex.I / 2) + Zeta23.paperFT k (-Complex.I / 2)

/-- The unmodified archimedean digamma/Gamma bracket contribution
of the original Zeta23.EF.literatureRHS. -/
def neutralIV011OriginalMixedArch (b : ℝ) (s t : 𝓢(ℝ, ℂ)) : ℂ :=
  let k := neutralWindowCorrelation b (s.toLp 2 volume) (t.toLp 2 volume)
  (1 / (2 * Real.pi) : ℂ) *
    ∫ r : ℝ, Zeta23.paperFT k r * (Zeta23.EF.gammaBracket r : ℂ)

/-- Exact original arithmetic CROSS-SUPPORT decomposition into
pole minus prime plus arch, with every sign and 2π retained. -/
theorem neutralIV011OriginalMixed_arithmeticSplit
    (b : ℝ) (s t : 𝓢(ℝ, ℂ)) :
    neutralIV010Mixed b s t =
      neutralIV011OriginalMixedPole b s t -
      neutralIV011OriginalMixedPrime b s t +
      neutralIV011OriginalMixedArch b s t := by
  rfl

/-- Exact finite-prime representation of the genuine original
mixed Weil entry under one NEW larger support. The difficult
cross-support estimate is now isolated in a FINITE arithmetic
prime sum plus the unchanged pole and arch terms. -/
theorem neutralIV011OriginalMixed_finitePrimeArithmetic
    (a b : ℝ) (hab : a ≤ b)
    (s t : 𝓢(ℝ, ℂ))
    (hs : ∀ x : ℝ, x ∉ Set.Icc (-a) a → s x = 0)
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (N : ℕ)
    (hN : ∀ n : ℕ, N ≤ n → a + b < Real.log n) :
    neutralIV010Mixed b s t =
      neutralIV011OriginalMixedPole b s t -
      (∑ n ∈ Finset.range N,
        ((ArithmeticFunction.vonMangoldt n / Real.sqrt n : ℝ) : ℂ) *
          (neutralWindowCorrelation b
            (s.toLp 2 volume) (t.toLp 2 volume) (Real.log n) +
          neutralWindowCorrelation b
            (s.toLp 2 volume) (t.toLp 2 volume) (-Real.log n))) +
      neutralIV011OriginalMixedArch b s t := by
  rw [neutralIV011OriginalMixed_arithmeticSplit,
    neutralIV011OriginalMixedPrime_eq_finite a b hab s t hs ht N hN]

/-- The explicit coefficient that minimizes the genuine
Hermitian 2×2 real block when the new diagonal D≠0.
The sign is -conj(B)/D because the cross term is 2Re(B*v). -/
def neutralIV011SchurMinimizer (B : ℂ) (D : ℝ) : ℂ :=
  ⟨-B.re / D, B.im / D⟩

/-- An exact rational algebra identity. It makes violation of the
mixed determinant test a concrete NEGATIVE quadratic witness,
rather than merely a nonconstructive abstract failure. -/
theorem neutralIV011SchurMinimizer_value
    (A D : ℝ) (B : ℂ) (hD : D ≠ 0) :
    A + 2 * (B * neutralIV011SchurMinimizer B D).re +
        D * ((neutralIV011SchurMinimizer B D).re ^ 2 +
          (neutralIV011SchurMinimizer B D).im ^ 2) =
      (A * D - (B.re^2 + B.im^2)) / D := by
  dsimp [neutralIV011SchurMinimizer, Complex.mul_re]
  field_simp [hD]
  ring

/-- Sharp strict negative witness when D>0 but
|B|²>AD. No assumption that genuine zeta satisfies such a
violation is made: it is the TEST OF FAILURE. -/
theorem neutralIV011SchurFailure_negative
    (A D : ℝ) (B : ℂ)
    (hD : 0 < D)
    (hfail : A * D < B.re^2 + B.im^2) :
    A + 2 * (B * neutralIV011SchurMinimizer B D).re +
        D * ((neutralIV011SchurMinimizer B D).re ^ 2 +
          (neutralIV011SchurMinimizer B D).im ^ 2) < 0 := by
  rw [neutralIV011SchurMinimizer_value A D B (ne_of_gt hD)]
  exact div_neg_of_neg_of_pos (sub_neg.mpr hfail) hD

/-- Authentic original arithmetic Weil negative test if the NEW
cross-support zeta mixed determinant fails with strictly positive
new diagonal. The old source and new physical Schwartz test are
unchanged; the witness coefficient is completely explicit. -/
theorem neutralIV011OriginalCrossFailure_negativeWitness
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hD : 0 < (neutralIV010Diagonal b t).re)
    (hfail :
      (neutralIV007OriginalMixedEnergy a s u).re *
        (neutralIV010Diagonal b t).re <
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2) :
    (neutralIV010Diagonal b
      (neutralIV009PhysicalSchwartzSum s u +
        (neutralIV011SchurMinimizer
          (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t)
          (neutralIV010Diagonal b t).re) • t)).re < 0 := by
  rw [neutralIV010OldPlusNew_realBlock a b hab s u hs t ht]
  exact neutralIV011SchurFailure_negative
    (neutralIV007OriginalMixedEnergy a s u).re
    (neutralIV010Diagonal b t).re
    (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t)
    hD hfail

/-- A mathematically PRECISE necessary condition for positivity
of the actual new-support one-site extension when D>0. Combined
with IV010 it yields sharp support-extension equivalence (given
old-block nonnegativity), but supplies NO new arithmetic estimate. -/
theorem neutralIV011OriginalCrossBound_necessary
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hD : 0 < (neutralIV010Diagonal b t).re)
    (hpos : ∀ v : ℂ, 0 ≤
      (neutralIV010Diagonal b
        (neutralIV009PhysicalSchwartzSum s u + v • t)).re) :
    (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re := by
  by_contra hn
  have hfail :
      (neutralIV007OriginalMixedEnergy a s u).re *
        (neutralIV010Diagonal b t).re <
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 :=
    lt_of_not_ge hn
  have hneg :=
    neutralIV011OriginalCrossFailure_negativeWitness
      a b hab s u hs t ht hD hfail
  exact (not_lt_of_ge (hpos _)) hneg

/-- Source-identical SHARP one-new-support equivalence, when the
old original family has nonnegative mixed energy and the newly
admitted diagonal is strictly positive. The RHS is the exact
required ORIGINAL arithmetic cross estimate, not a proved fact. -/
theorem neutralIV011OriginalOneNew_nonnegative_iff_crossBound
    {n : ℕ} (a b : ℝ) (hab : a ≤ b)
    (s : Fin n → 𝓢(ℝ, ℂ)) (u : Fin n → ℂ)
    (hs : ∀ i : Fin n, ∀ x : ℝ,
      x ∉ Set.Icc (-a) a → s i x = 0)
    (t : 𝓢(ℝ, ℂ))
    (ht : ∀ x : ℝ, x ∉ Set.Icc (-b) b → t x = 0)
    (hOld : 0 ≤ (neutralIV007OriginalMixedEnergy a s u).re)
    (hD : 0 < (neutralIV010Diagonal b t).re) :
    (∀ v : ℂ, 0 ≤ (neutralIV010Diagonal b
        (neutralIV009PhysicalSchwartzSum s u + v • t)).re) ↔
      (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).re^2 +
        (neutralIV010Mixed b (neutralIV009PhysicalSchwartzSum s u) t).im^2 ≤
        (neutralIV007OriginalMixedEnergy a s u).re *
          (neutralIV010Diagonal b t).re := by
  constructor
  · intro hpos
    exact neutralIV011OriginalCrossBound_necessary
      a b hab s u hs t ht hD hpos
  · intro hCross v
    exact neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
      a b hab s u hs t ht hOld (le_of_lt hD) hCross v

#print axioms neutralIV006Schwartz_window_ae
#print axioms neutralIV010OldPlusNew_realBlock
#print axioms neutralIV010OriginalOneNewSource_nonnegative_of_crossBound
#print axioms neutralNF600Correlation_eq
#print axioms neutralIV011MixedCorrelation_eq_schwartzIntegral
#print axioms neutralIV011MixedCorrelation_vanish_far
#print axioms neutralIV011MixedPrime_logFar_vanish
#print axioms neutralIV011ExistsPrimeCutoff
#print axioms neutralIV011OriginalMixedPrime_eq_finite
#print axioms neutralIV011OriginalMixed_arithmeticSplit
#print axioms neutralIV011OriginalMixed_finitePrimeArithmetic
#print axioms neutralIV011SchurMinimizer_value
#print axioms neutralIV011SchurFailure_negative
#print axioms neutralIV011OriginalCrossFailure_negativeWitness
#print axioms neutralIV011OriginalCrossBound_necessary
#print axioms neutralIV011OriginalOneNew_nonnegative_iff_crossBound

end
end WeilDefect
