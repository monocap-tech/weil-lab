import WeilDefect.Arithmetic.ActualZetaOriginalEndpointBoundedSeedGraph
import WeilDefect.Arithmetic.ActualZetaOriginalEndpointLiteralStrip
import WeilDefect.Arithmetic.ActualZetaOriginalNF407SourceBinding

namespace WeilDefect
noncomputable section
open MeasureTheory Filter Set
open scoped SchwartzMap ComplexConjugate

/-! NF596: numerical smallness is not needed for qualitative
graph convergence. Normalize a C1 amplitude only for applying
the certified strip estimate, then undo the scale at the level of
the actual Fourier transform. The target and seed functions are
NEVER changed. Quantitative signed margins remain separate. -/

theorem neutralNF596Half_const_mul (U : ℝ → ℝ) (c : ℝ) (x : ℝ) :
    neutralNF575OriginalEndpointHalf (fun t => c*U t) x =
      c*neutralNF575OriginalEndpointHalf U x := by
  unfold neutralNF575OriginalEndpointHalf
  split_ifs <;> ring

theorem neutralNF596Raw_const_mul (h : ℝ → ℝ) (c : ℝ) (z : ℂ) :
    neutralNF579RawTransform (fun t => c*h t) z =
      (c:ℂ)*neutralNF579RawTransform h z := by
  unfold neutralNF579RawTransform
  simp_rw [Complex.ofReal_mul,mul_assoc]
  exact integral_const_mul _ _

theorem neutralNF596C1_commonBound (U V : ℝ → ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hV : ContinuousOn V (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B)) :
    ∃ A : ℝ, 0 ≤ A ∧
      (∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B, |U x| ≤ A) ∧
      (∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B, |V x| ≤ A) := by
  obtain ⟨a,ha⟩ := isCompact_Icc.bddAbove_image hU.abs
  obtain ⟨b,hb⟩ := isCompact_Icc.bddAbove_image hV.abs
  refine ⟨max 0 (max a b),le_max_left _ _,?_,?_⟩
  · intro x hx
    exact (ha (mem_image_of_mem _ hx)).trans ((le_max_left a b).trans (le_max_right _ _))
  · intro x hx
    exact (hb (mem_image_of_mem _ hx)).trans ((le_max_right a b).trans (le_max_right _ _))

theorem neutralNF596C1_strip (U U' : ℝ → ℝ)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hder : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt U (U' x) x) :
    ∃ C : ℝ, 0 ≤ C ∧ ∀ z : ℂ, |z.im| ≤ 1/2 →
      ‖neutralNF579RawTransform (neutralNF575OriginalEndpointHalf U) z‖ ≤
        C*neutralNF575StripEnvelope z.re := by
  obtain ⟨A,hA,h0,h1⟩ := neutralNF596C1_commonBound U U' hU hU'
  let c : ℝ := 1+10^7*A
  have hc : 0 < c := by dsimp [c]; positivity
  let V : ℝ → ℝ := fun x => U x/c
  let V' : ℝ → ℝ := fun x => U' x/c
  have hV : ContinuousOn V (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B) :=
    hU.div_const c
  have hV' : ContinuousOn V' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B) :=
    hU'.div_const c
  have hd : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt V (V' x) x := fun x hx => (hder x hx).div_const c
  have hsmall : A/c ≤ (1/10^7:ℝ) := by
    apply (div_le_iff₀ hc).mpr
    dsimp [c]
    linarith
  have hv0 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |V x| ≤ neutralNF578C0 := by
    intro x hx
    dsimp [V]
    rw [abs_div,abs_of_pos hc]
    exact ((div_le_div_of_nonneg_right (h0 x hx) hc.le).trans hsmall).trans
      (by unfold neutralNF578C0; norm_num)
  have hv1 : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      |V' x| ≤ (7/10^4:ℝ) := by
    intro x hx
    dsimp [V']
    rw [abs_div,abs_of_pos hc]
    exact ((div_le_div_of_nonneg_right (h1 x hx) hc.le).trans hsmall).trans (by norm_num)
  have hUV : U = fun x => c*V x := by
    funext x
    dsimp [V]
    field_simp [hc.ne']
  have hhalf : neutralNF575OriginalEndpointHalf U =
      fun x => c*neutralNF575OriginalEndpointHalf V x := by
    funext x
    calc
      neutralNF575OriginalEndpointHalf U x =
          neutralNF575OriginalEndpointHalf (fun t => c*V t) x := congrArg
            (fun W => neutralNF575OriginalEndpointHalf W x) hUV
      _ = _ := neutralNF596Half_const_mul V c x
  refine ⟨c/40000,by positivity,?_⟩
  intro z hz
  rw [hhalf,neutralNF596Raw_const_mul,norm_mul,Complex.norm_real,Real.norm_eq_abs,abs_of_pos hc]
  calc
    _ ≤ c*((1/40000:ℝ)*neutralNF575StripEnvelope z.re) :=
      mul_le_mul_of_nonneg_left
        (neutralNF585LiteralHalf_strip V V' hV hV' hd hv0 hv1 z hz) hc.le
    _ = _ := by ring

/-- No sharp numerical bound, coefficient enclosure, or original
solve-box membership occurs in the qualitative seed graph theorem. -/
theorem neutralNF596OriginalEndpoint_actualSeedGraph_of_C1
    (U U' : ℝ → ℝ) (hm : Measurable U)
    (hU : ContinuousOn U (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hU' : ContinuousOn U' (Icc (neutralNF578B-neutralNF578Delta) neutralNF578B))
    (hder : ∀ x ∈ Icc (neutralNF578B-neutralNF578Delta) neutralNF578B,
      HasDerivAt U (U' x) x) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint U) 2 volume)
      (g : ℕ → 𝓢(ℝ,ℂ))
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      (∀ n x, g n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf U) n) x:ℂ)) ∧
      (∀ n x, conj (g n x) = g n x) ∧
      (∀ n x, g n (-x) = -g n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → g n x = 0) ∧
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val =
        hLp.toLp (neutralNF575OriginalEndpoint U) ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val =
        (g n).toLp 2 volume) ∧ Tendsto G atTop (nhds K) := by
  obtain ⟨A,hA,h0,_⟩ := neutralNF596C1_commonBound U U' hU hU'
  have ho : ∀ x ∈ Ioo ((11/10:ℝ)-1/500) (11/10:ℝ), |U x| ≤ A :=
    fun x hx => h0 x ⟨hx.1.le,hx.2.le⟩
  obtain ⟨C,hC,hstrip⟩ := neutralNF596C1_strip U U' hU hU' hder
  obtain ⟨g,K,G,hh⟩ := neutralNF596OriginalEndpoint_actualSeedGraph_bounded
    U hm A hA ho (neutralNF585LiteralHalf_integrable U hU) C hC hstrip
  exact ⟨neutralNF575OriginalEndpoint_memLp U hm A hA ho,g,K,G,hh⟩

/-- The same literal 246-generator source admits the qualitative
graph approximation for EVERY choice of its real coefficients. -/
theorem neutralNF596NF407SeedGraph (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) :
    ∃ (hLp : MemLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) 2 volume)
      (g : ℕ → 𝓢(ℝ,ℂ))
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (G : ℕ → NeutralActualZetaSourceDomain (11/10:ℝ)),
      (∀ n x, g n x = (neutralNF583Odd
        (neutralNF582HalfSequence (neutralNF575OriginalEndpointHalf (neutralNF587Source a b)) n) x:ℂ)) ∧
      (∀ n x, conj (g n x) = g n x) ∧
      (∀ n x, g n (-x) = -g n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → g n x = 0) ∧
      neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) K).val =
        hLp.toLp (neutralNF575OriginalEndpoint (neutralNF587Source a b)) ∧
      (∀ n, neutralLogPhysical (neutralActualZetaSourcePhysical (11/10:ℝ) (G n)).val =
        (g n).toLp 2 volume) ∧ Tendsto G atTop (nhds K) := by
  apply neutralNF596OriginalEndpoint_actualSeedGraph_of_C1
    (neutralNF587Source a b) (deriv (neutralNF587Source a b))
    (neutralNF587Source_measurable a b)
  · exact (neutralNF587Source_contDiff a b).continuous.continuousOn
  · exact (neutralNF587Source_derivative_continuous a b).continuousOn
  · intro x _
    exact neutralNF587Source_hasDerivAt a b x

end
end WeilDefect
