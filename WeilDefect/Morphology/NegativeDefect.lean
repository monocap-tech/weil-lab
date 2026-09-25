import WeilDefect.Filtration.FiniteNegativeSector
import WeilDefect.PairGeometry
import WeilDefect.RationalResponse
import WeilDefect.Arithmetic.Scalarization
import WeilDefect.Arithmetic.FarTail
import WeilDefect.Arithmetic.NextJet
import WeilDefect.Arithmetic.Coadaptation

namespace WeilDefect

open Filter
open scoped Topology BigOperators

/--
P3-N1: the convergent fixed-packet negative signature produces an actual
negative right-limit ray, outside a nonnegative endpoint space.
-/
theorem wd_t37_persistent_negative_endpoint_ray
    {Kpos M : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [FiniteDimensional ℂ M]
    (A : ℝ → ClosedSubmodule ℂ (WeilDefect.WDT16.CoeffSpace Kpos M))
    (c : ℝ) (t : ℕ → ℝ)
    (hA : Monotone A)
    (ht : Tendsto t atTop (𝓝 c))
    (a : ℕ → Kpos) (u : ℕ → M)
    (κ : ℝ) (hκ : 0 < κ)
    (hmem :
      ∀ n,
        WeilDefect.WDT16.coeff (a n) (u n) ∈ A (t n))
    (hnorm :
      ∀ n,
        ‖WeilDefect.WDT16.coeff (a n) (u n)‖ = 1)
    (hq :
      Tendsto
        (fun n => WeilDefect.WDT16.jValue (a n) (u n))
        atTop (𝓝 (-κ)))
    (hendpoint :
      ∀ y : WeilDefect.WDT16.CoeffSpace Kpos M,
        y ∈ A c →
        0 ≤ WeilDefect.WDT16.jValue y.fst y.snd) :
    ∃ y : WeilDefect.WDT16.CoeffSpace Kpos M,
      y ≠ 0
      ∧ y ∈ WeilDefect.WDT15.rightLimit A c
      ∧ y ∉ A c
      ∧ WeilDefect.WDT16.jValue y.fst y.snd ≤ -κ
      ∧ y.snd ≠ 0 := by
  have hqStar : -κ ≤ 0 := by linarith
  rcases
      WeilDefect.WDT16.wd_t16_nonpositive_limit_persists
        A c t hA ht a u (-κ) hqStar hmem hnorm hq with
    ⟨y, hy0, hyRight, hyNeg⟩
  have hyNot : y ∉ A c := by
    intro hy
    have hnonneg := hendpoint y hy
    linarith
  have hySnd : y.snd ≠ 0 := by
    intro hsnd
    have hjnonneg :
        0 ≤ WeilDefect.WDT16.jValue y.fst y.snd := by
      simp [WeilDefect.WDT16.jValue, hsnd]
    linarith
  exact ⟨y, hy0, hyRight, hyNot, hyNeg, hySnd⟩

/-- Direct normalized representatives used in P3-N2. -/
noncomputable def negativeNormalizedRepresentative
    {P : Type*}
    [NormedAddCommGroup P] [NormedSpace ℂ P]
    (g : ℕ → P) (ε : ℕ → ℝ) (n : ℕ) : P :=
  ((ε n : ℂ)⁻¹) • g n

/--
P3-N2 direct normalization: if the selected amplitude tends to zero through
positive values and the physical witnesses are unit vectors, the rescaled
representatives have reciprocal norm and diverge.
-/
theorem wd_t37_normalized_representative_blowup
    {P : Type*}
    [NormedAddCommGroup P] [NormedSpace ℂ P]
    (g : ℕ → P) (ε : ℕ → ℝ)
    (hεpos : ∀ n, 0 < ε n)
    (hε0 : Tendsto ε atTop (𝓝 0))
    (hgnorm : ∀ n, ‖g n‖ = 1) :
    (∀ n,
      ‖negativeNormalizedRepresentative g ε n‖ = (ε n)⁻¹)
      ∧
    Tendsto
      (fun n => ‖negativeNormalizedRepresentative g ε n‖)
      atTop atTop := by
  have hnorm :
      ∀ n,
        ‖negativeNormalizedRepresentative g ε n‖ = (ε n)⁻¹ := by
    intro n
    unfold negativeNormalizedRepresentative
    rw [norm_smul, hgnorm n, mul_one]
    simp [Complex.norm_real, abs_of_pos (hεpos n)]
  have hεWithin : Tendsto ε atTop (𝓝[>] (0 : ℝ)) := by
    refine tendsto_nhdsWithin_iff.mpr ⟨hε0, ?_⟩
    exact Eventually.of_forall hεpos
  have hinv :
      Tendsto (fun n => (ε n)⁻¹) atTop atTop :=
    tendsto_inv_nhdsGT_zero.comp hεWithin
  refine ⟨hnorm, ?_⟩
  exact hinv.congr' (Eventually.of_forall fun n => (hnorm n).symm)

/--
P3-N3 in an exact limsup-style form: if the selected normalized signature
converges to -kappa and the full normalized form subtracts a background norm
square, then every positive tolerance eventually bounds the full form by
-kappa + tolerance.
-/
theorem wd_t37_normalized_full_weil_negativity
    {B : Type*}
    [NormedAddCommGroup B]
    (selected full : ℕ → ℝ)
    (background : ℕ → B)
    (κ : ℝ)
    (hselected : Tendsto selected atTop (𝓝 (-κ)))
    (hfull :
      ∀ n,
        full n = selected n - ‖background n‖ ^ 2) :
    ∀ δ : ℝ, 0 < δ →
      ∀ᶠ n in atTop, full n ≤ -κ + δ := by
  intro δ hδ
  have hev :
      ∀ᶠ n in atTop, selected n < -κ + δ :=
    hselected.eventually (Iio_mem_nhds (by linarith))
  exact hev.mono fun n hn => by
    rw [hfull n]
    have hsquare : 0 ≤ ‖background n‖ ^ 2 := sq_nonneg _
    linarith

/--
P3-N4 source bridge: a finite analytic residue vector that represents the
canonical WD-T26 raw pair list inherits both zero total residue and
nontriviality.
-/
theorem wd_t37_zero_moment_source_of_pair_data
    (xs : List ℂ)
    (hxs : ∃ α ∈ xs, α ≠ 0)
    {m : ℕ}
    (v : Fin m → ℂ)
    (hsum :
      (∑ i : Fin m, v i)
        =
      (rawResiduesOfNegativePairs xs).sum)
    (hcontains :
      ∀ r : ℂ,
        r ∈ rawResiduesOfNegativePairs xs →
        ∃ i : Fin m, v i = r) :
    (∑ i : Fin m, v i) = 0
      ∧ ∃ i : Fin m, v i ≠ 0 := by
  have hpair := wd_t26_selected_zero_moment_residue xs
  have hv0 :
      (∑ i : Fin m, v i) = 0 := by
    calc
      (∑ i : Fin m, v i)
          = (rawResiduesOfNegativePairs xs).sum := hsum
      _ = 0 := hpair.1
  rcases hpair.2 hxs with ⟨r, hrmem, hr0⟩
  rcases hcontains r hrmem with ⟨i, hir⟩
  have hvi : v i ≠ 0 := by
    intro hzero
    apply hr0
    rw [← hir, hzero]
  exact ⟨hv0, ⟨i, hvi⟩⟩

/--
P3-N5/N6/N7 arithmetic morphology package.

The selected-preserving condition is carried explicitly.  WD-T26 supplies the
raw zero-moment source, WD-T31 removes the distant divisor, WD-T32 identifies
the finite near field with the completed-Xi next-jet field, and WD-T33 rules
out an adaptive prime bypass.
-/
theorem wd_t37_arithmetic_negative_morphology
    (xs : List ℂ)
    (hxs : ∃ α ∈ xs, α ≠ 0)
    {m : ℕ}
    (rho v : Fin m → ℂ)
    (hsum :
      (∑ i : Fin m, v i)
        =
      (rawResiduesOfNegativePairs xs).sum)
    (hcontains :
      ∀ r : ℂ,
        r ∈ rawResiduesOfNegativePairs xs →
        ∃ i : Fin m, v i = r)
    (Csel : (ℂ → ℂ) →ₗ[ℂ] ℂ)
    (psi : ℂ → ℂ)
    (hSelected : Csel psi = 0)
    {count : ℕ → ℕ}
    (farMu : FarShellIndex count → ℂ)
    (M C : ℝ)
    (hCount : ZetaLogShellCountData count C)
    (hM : 0 ≤ M)
    (hPsi : ∀ gamma, ‖psi (farMu gamma)‖ ≤ M)
    (hShellNorm :
      ∀ gamma,
        ((gamma.1 : ℝ) + 1) ≤ ‖farMu gamma‖)
    (hSelectedFar :
      ∀ gamma i,
        2 * ‖rho i‖ ≤ ‖farMu gamma‖)
    (Rcut : ℕ) (hRcut : 1 ≤ Rcut)
    {ι : Type*} [DecidableEq ι]
    (s : Finset ι)
    (mult : ι → ℕ)
    (nearMu : ι → ℂ)
    (Xi : ℂ → ℂ)
    (g : ι → ℂ → ℂ)
    (hXi :
      ∀ i ∈ s,
        Xi =ᶠ[𝓝 (nearMu i)]
          (fun z : ℂ =>
            (z - nearMu i) ^ (mult i) * g i z))
    (hg :
      ∀ i ∈ s,
        ContDiffAt ℂ (mult i) (g i) (nearMu i))
    (hRlocal :
      ∀ i ∈ s,
        ContDiffAt ℂ (mult i)
          (rationalResponse rho v) (nearMu i))
    (hg0 :
      ∀ i ∈ s,
        g i (nearMu i) ≠ 0)
    (N F P A : ℂ)
    (hBalance : N + F = P + A)
    (hCancel : N = A) :
    Csel psi = 0
      ∧ (∑ i : Fin m, v i) = 0
      ∧ (∃ i : Fin m, v i ≠ 0)
      ∧
        ‖∑' k : ℕ,
            farShellResponse
              (zeroMomentShellTerm rho v farMu psi)
              (k + Rcut)‖
          ≤
        ((M * zeroMomentResponseConstant rho v) * C)
          * ((Real.log Rcut + 2) / Rcut)
      ∧
        nearComplementaryResponse
            s mult nearMu psi (rationalResponse rho v)
          =
        weightedNearNextJetField
            s mult nearMu psi Xi (rationalResponse rho v)
      ∧ P = F := by
  rcases
      wd_t37_zero_moment_source_of_pair_data
        xs hxs v hsum hcontains with
    ⟨hv0, hvNonzero⟩
  refine ⟨hSelected, hv0, hvNonzero, ?_, ?_, ?_⟩
  · exact wd_t31_zero_moment_zero_count_far_tail
      rho v hv0 farMu psi M C
      hCount hM hPsi hShellNorm hSelectedFar
      Rcut hRcut
  · exact wd_t32_weighted_near_next_jet_representation
      s mult nearMu psi Xi (rationalResponse rho v) g
      hXi hg hRlocal hg0
  · exact wd_t33_adaptive_cocancellation N F P A hBalance hCancel

/--
WD-T30 is the selected-preserving scalarization input consumed before the
WD-T37 arithmetic package.
-/
theorem wd_t37_selected_preserving_scalarization
    {V : Type*}
    [AddCommMonoid V] [Module ℂ V]
    (Csel : V →ₗ[ℂ] ℂ)
    (psi₁ psi₂ : V)
    (h : Csel psi₁ ≠ 0 ∨ Csel psi₂ ≠ 0) :
    ∃ β₁ β₂ : ℂ,
      (β₁ ≠ 0 ∨ β₂ ≠ 0)
      ∧ Csel (β₁ • psi₁ + β₂ • psi₂) = 0 :=
  wd_t30_two_mode_kernel_combination Csel psi₁ psi₂ h

end WeilDefect
