import WeilDefect.Filtration.FiniteNegativeSector
import WeilDefect.Screening.FinitePositiveShadows
import WeilDefect.Screening.BackgroundCustody

namespace WeilDefect

open Filter
open scoped Topology InnerProduct

/-- The full negative coefficient carrier: selected finite packet plus background. -/
abbrev FullNegativeSpace
    (M B : Type*)
    [NormedAddCommGroup M] [InnerProductSpace ℂ M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B] :=
  WithLp 2 (M × B)

/-- Assemble selected and background negative coordinates in the Hilbert L2 product. -/
def fullNegativeCoeff
    {M B : Type*}
    [NormedAddCommGroup M] [InnerProductSpace ℂ M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B]
    (u : M) (b : B) : FullNegativeSpace M B :=
  WithLp.toLp 2 (u, b)

/-- Assemble the positive coordinate with the entire negative sector. -/
def fullCoeff
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B]
    (a : Kpos) (u : M) (b : B) :
    WeilDefect.WDT16.CoeffSpace Kpos (FullNegativeSpace M B) :=
  WeilDefect.WDT16.coeff a (fullNegativeCoeff u b)

/-- Full coefficient signature for selected plus background negative coordinates. -/
def fullJValue
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [NormedSpace ℂ Kpos]
    [NormedAddCommGroup M] [NormedSpace ℂ M]
    [NormedAddCommGroup B] [NormedSpace ℂ B]
    (a : Kpos) (u : M) (b : B) : ℝ :=
  ‖a‖ ^ 2 - ‖u‖ ^ 2 - ‖b‖ ^ 2

/-- Strong convergence of both negative coordinates gives strong convergence
of the assembled full negative coordinate. -/
theorem tendsto_fullNegativeCoeff
    {M B : Type*}
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]
    {u : ℕ → M} {b : ℕ → B} {uLim : M} {bLim : B}
    (hu : Tendsto u atTop (𝓝 uLim))
    (hb : Tendsto b atTop (𝓝 bLim)) :
    Tendsto
      (fun n => fullNegativeCoeff (u n) (b n))
      atTop
      (𝓝 (fullNegativeCoeff uLim bLim)) := by
  have hpair :
      Tendsto (fun n => (u n, b n)) atTop (𝓝 (uLim, bLim)) :=
    hu.prodMk_nhds hb
  have hmap :=
    ((WithLp.prodContinuousLinearEquiv 2 ℂ M B).symm.continuous.tendsto
      (uLim, bLim)).comp hpair
  simpa [fullNegativeCoeff] using hmap

/-- B-2 custody: weak convergence of the positive coordinate together with
strong convergence on the entire negative sector gives a full weak limit. -/
theorem weaklyTendsto_fullCoeff
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]
    {a : ℕ → Kpos} {u : ℕ → M} {b : ℕ → B}
    {aLim : Kpos} {uLim : M} {bLim : B}
    (ha : WeilDefect.WDT16.WeaklyTendsto a aLim)
    (hu : Tendsto u atTop (𝓝 uLim))
    (hb : Tendsto b atTop (𝓝 bLim)) :
    WeilDefect.WDT16.WeaklyTendsto
      (fun n => fullCoeff (a n) (u n) (b n))
      (fullCoeff aLim uLim bLim) := by
  have hneg :=
    tendsto_fullNegativeCoeff (u := u) (b := b)
      (uLim := uLim) (bLim := bLim) hu hb
  simpa [fullCoeff] using
    (WeilDefect.WDT16.weaklyTendsto_coeff ha hneg)

/-- Whole full-coefficient strong convergence requires positive-coordinate
strong convergence in addition to strong convergence of both negative parts. -/
theorem tendsto_fullCoeff_of_strong_positive
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]
    {a : ℕ → Kpos} {u : ℕ → M} {b : ℕ → B}
    {aLim : Kpos} {uLim : M} {bLim : B}
    (ha : Tendsto a atTop (𝓝 aLim))
    (hu : Tendsto u atTop (𝓝 uLim))
    (hb : Tendsto b atTop (𝓝 bLim)) :
    Tendsto
      (fun n => fullCoeff (a n) (u n) (b n))
      atTop
      (𝓝 (fullCoeff aLim uLim bLim)) := by
  have hneg :=
    tendsto_fullNegativeCoeff (u := u) (b := b)
      (uLim := uLim) (bLim := bLim) hu hb
  have hpair :
      Tendsto
        (fun n => (a n, fullNegativeCoeff (u n) (b n)))
        atTop
        (𝓝 (aLim, fullNegativeCoeff uLim bLim)) :=
    ha.prodMk_nhds hneg
  have hmap :=
    ((WithLp.prodContinuousLinearEquiv
      2 ℂ Kpos (FullNegativeSpace M B)).symm.continuous.tendsto
        (aLim, fullNegativeCoeff uLim bLim)).comp hpair
  simpa [fullCoeff, WeilDefect.WDT16.coeff] using hmap

/-- A nonzero selected negative coordinate makes the assembled full
coefficient vector nonzero, independently of the background. -/
theorem fullCoeff_ne_zero_of_selected_ne
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B]
    (a : Kpos) (u : M) (b : B)
    (hu : u ≠ 0) :
    fullCoeff a u b ≠ 0 := by
  intro hzero
  have hneg :
      fullNegativeCoeff u b = 0 := by
    have hsnd :=
      congrArg
        (fun z : WeilDefect.WDT16.CoeffSpace
          Kpos (FullNegativeSpace M B) => z.snd)
        hzero
    simpa [fullCoeff] using hsnd
  have hsel :=
    congrArg (fun z : FullNegativeSpace M B => z.fst) hneg
  apply hu
  simpa [fullNegativeCoeff] using hsel

/--
P3-B3 / WD-T39 fixed-packet custody in operational form.

A bounded sequence in a finite selected sector that carries a fixed positive
amount of selected mass frequently has a strongly convergent subsequence with
nonzero limit.  This is the exact subsequential content used by the audited
"limsup > 0" statement.
-/
theorem wd_t39_p3_b3_fixed_packet_custody
    {M : Type*}
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [FiniteDimensional ℂ M]
    (u : ℕ → M) (R δ : ℝ)
    (hbound : ∀ n, ‖u n‖ ≤ R)
    (hδ : 0 < δ)
    (hfreq : ∃ᶠ n in atTop, δ ≤ ‖u n‖) :
    ∃ φ : ℕ → ℕ, StrictMono φ ∧
      ∃ uLim : M,
        uLim ≠ 0 ∧
        Tendsto (fun n => u (φ n)) atTop (𝓝 uLim) := by
  rcases Filter.extraction_of_frequently_atTop hfreq with
    ⟨φ₁, hφ₁, hlower⟩
  have hbound₁ : ∀ n, ‖u (φ₁ n)‖ ≤ R :=
    fun n => hbound (φ₁ n)
  rcases
      WeilDefect.WDT16.exists_tendsto_subseq_finiteDimensional
        (fun n => u (φ₁ n)) R hbound₁ with
    ⟨φ₂, hφ₂, uLim, huLim⟩
  let φ : ℕ → ℕ := φ₁ ∘ φ₂
  have hφ : StrictMono φ := hφ₁.comp hφ₂
  have huLim' :
      Tendsto (fun n => u (φ n)) atTop (𝓝 uLim) := by
    simpa [φ, Function.comp_def] using huLim
  have hδle : δ ≤ ‖uLim‖ := by
    apply le_of_tendsto' huLim'.norm
    intro n
    exact hlower (φ₂ n)
  have hu0 : uLim ≠ 0 := by
    intro hzero
    rw [hzero, norm_zero] at hδle
    linarith
  exact ⟨φ, hφ, uLim, hu0, huLim'⟩

/--
P3-B5 / WD-T39: an anchored selected negative ray survives every bounded
background weak limit.  The full coefficient ray is nonzero and its signature
can only become more negative.
-/
theorem wd_t39_p3_b5_fixed_selected_ray_stability
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [NormedSpace ℂ Kpos]
    [NormedAddCommGroup M] [NormedSpace ℂ M]
    [NormedAddCommGroup B] [NormedSpace ℂ B]
    (a : Kpos) (u : M) (b : B)
    (κ : ℝ) (hκ : 0 < κ)
    (hselected :
      WeilDefect.WDT16.jValue a u ≤ -κ) :
    u ≠ 0
      ∧ fullJValue a u b ≤ -κ - ‖b‖ ^ 2
      ∧ fullJValue a u b < 0 := by
  have hu0 : u ≠ 0 := by
    intro hu
    have hsq : 0 ≤ ‖a‖ ^ 2 := sq_nonneg _
    simp [WeilDefect.WDT16.jValue, hu] at hselected
    linarith
  constructor
  · exact hu0
  constructor
  · unfold fullJValue WeilDefect.WDT16.jValue at *
    linarith
  · unfold fullJValue WeilDefect.WDT16.jValue at *
    have hb : 0 ≤ ‖b‖ ^ 2 := sq_nonneg _
    linarith

/--
P3-B6 / WD-T39: if the unselected background converges strongly, then the
entire negative sector converges strongly while the full coefficient vector
has a fixed weak limit.  No positive-coordinate strong convergence is claimed.
-/
theorem wd_t39_p3_b6_fixed_full_divisor_negative_weak_limit
    {Kpos M B : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [NormedAddCommGroup B] [InnerProductSpace ℂ B] [CompleteSpace B]
    {a : ℕ → Kpos} {u : ℕ → M} {b : ℕ → B}
    {aLim : Kpos} {uLim : M} {bLim : B}
    (κ : ℝ) (hκ : 0 < κ)
    (ha : WeilDefect.WDT16.WeaklyTendsto a aLim)
    (hu : Tendsto u atTop (𝓝 uLim))
    (hb : Tendsto b atTop (𝓝 bLim))
    (hselected :
      WeilDefect.WDT16.jValue aLim uLim ≤ -κ) :
    WeilDefect.WDT16.WeaklyTendsto
        (fun n => fullCoeff (a n) (u n) (b n))
        (fullCoeff aLim uLim bLim)
      ∧ Tendsto
          (fun n => fullNegativeCoeff (u n) (b n))
          atTop
          (𝓝 (fullNegativeCoeff uLim bLim))
      ∧ fullCoeff aLim uLim bLim ≠ 0
      ∧ fullJValue aLim uLim bLim
          ≤ -κ - ‖bLim‖ ^ 2
      ∧ fullJValue aLim uLim bLim < 0 := by
  have hstable :=
    wd_t39_p3_b5_fixed_selected_ray_stability
      aLim uLim bLim κ hκ hselected
  have hweak :=
    weaklyTendsto_fullCoeff ha hu hb
  have hneg :=
    tendsto_fullNegativeCoeff hu hb
  have hfull0 :=
    fullCoeff_ne_zero_of_selected_ne
      aLim uLim bLim hstable.1
  exact ⟨hweak, hneg, hfull0,
    hstable.2.1, hstable.2.2⟩

/--
P3-B7 / WD-T39 finite-shadow separation.

Finite positive-coordinate shadows preserve the selected algebraic negative
margin, while graph admissibility remains a separate condition controlled by
the discarded positive component.
-/
theorem wd_t39_p3_b7_finite_shadow_separation
    {Kpos M : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    (X : M →L[ℂ] Kpos)
    (U : Submodule ℂ Kpos) [U.HasOrthogonalProjection]
    (a : Kpos) (u : M) (κ : ℝ)
    (hmargin : WeilDefect.WDT14.shadowMargin a u = κ)
    (hκ : 0 < κ)
    (hgraph : u = -((X†) a)) :
    WeilDefect.WDT14.shadowMargin (U.starProjection a) u ≥ κ
      ∧
    (u = -((X†) (U.starProjection a))
      ↔ (X†) (a - U.starProjection a) = 0) := by
  constructor
  · exact
      (WeilDefect.WDT14.wd_t14_positive_shadow_preserves_negative_margin
        U a u κ hmargin hκ).1
  · exact
      WeilDefect.WDT14.wd_t14_graph_shadow_admissible_iff
        X U a u hgraph

end WeilDefect
