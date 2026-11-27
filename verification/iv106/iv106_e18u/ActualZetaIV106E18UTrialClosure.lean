import WeilDefect.Arithmetic.ActualZetaIV106E18UGraphObservation

namespace WeilDefect
noncomputable section
open MeasureTheory Set Metric Filter
open scoped SchwartzMap Topology

/-- The derivative of a supported Schwartz test vanishes on the open
exterior of its support window. -/
theorem neutralIV106E18UDeriv_outside (s : 𝓢(ℝ,ℂ)) (A B : ℝ)
    (hs : ∀ x ∉ Icc A B, s x = 0) (x : ℝ) (hx : x ∉ Icc A B) :
    SchwartzMap.derivCLM ℂ ℂ s x = 0 := by
  have h : HasDerivAt (s : ℝ → ℂ) 0 x := by
    apply (hasDerivAt_const x (0:ℂ)).congr_of_eventuallyEq
    filter_upwards [isClosed_Icc.isOpen_compl.mem_nhds hx] with y hy
    exact hs y hy
  exact h.deriv

/-- A uniform error bound on one fixed finite window gives the same
L2 bound for the function and its derivative. -/
theorem neutralIV106E18UTrial_graph
    (l h ε : ℝ) (hh : 0 < h) (hε : 0 < ε)
    (ρ : 𝓢(ℝ,ℂ))
    (hρout : ∀ x, x ≤ l-ε ∨ l+h+ε ≤ x → ρ x = 0)
    (hρmass : (∫ x in (l-ε)..(l+h+ε), ρ x) = 1)
    (M : ℝ) (hM : 0 ≤ M) (hρbound : ∀ x, ‖ρ x‖ ≤ M) :
    ((neutralIV106E18JTrial_memLp l h hh).toLp _,
      (neutralIV106E18SDTrial_memLp l h hh).toLp _) ∈
      neutralIV106E18UGraphSpace (l-ε) (l+h+ε) := by
  let A := l-ε
  let B := l+h+ε
  let c := l+h/2
  let R := h/2+ε
  let I := closedBall c R
  let W : RealComplexL2 := (neutralIV106E18JIndicator_memLp c R).toLp _
  have hI : I = Icc A B := by
    ext x
    change x ∈ closedBall c R ↔ x ∈ Icc A B
    rw [mem_closedBall,Real.dist_eq,abs_le,mem_Icc]
    dsimp [c,R,A,B]
    constructor <;> intro hx <;> constructor <;> linarith [hx.1,hx.2]
  have hsmall : Icc l (l+h) ⊆ Icc A B := by
    intro x hx
    dsimp [A,B]
    exact ⟨by linarith [hx.1],by linarith [hx.2]⟩
  let L : ℝ := B-A
  let C : ℝ := 1+L*M
  have hL : 0 < L := by dsimp [L,A,B]; linarith
  have hC : 0 < C := by dsimp [C]; positivity
  change _ ∈ closure (neutralIV106E18UGraphCore A B : Set neutralIV106E18UGraphAmbient)
  apply Metric.mem_closure_iff.mpr
  intro δ hδ
  let η : ℝ := δ/((‖W‖+1)*C*(L+1))
  have hden : 0 < (‖W‖+1)*C*(L+1) := by positivity
  have hη : 0 < η := div_pos hδ hden
  obtain ⟨s,hs,hf,hd⟩ := neutralIV106E18TTrial_approx l h ε hh hε
    ρ hρout hρmass M η hM hη hρbound
  change ∀ x ∉ Icc A B, s x = 0 at hs
  change ∀ x, ‖s x-neutralIV106E18ITrial l h x‖ ≤ η*C*L at hf
  change ∀ x, ‖SchwartzMap.derivCLM ℂ ℂ s x-neutralIV106E18SDTrial l h x‖ ≤ η*C at hd
  have hw : ∀ᵐ x ∂volume, W x = I.indicator (fun _ : ℝ => (1:ℂ)) x :=
    (neutralIV106E18JIndicator_memLp c R).coeFn_toLp
  have hfb : ∀ᵐ x ∂volume, ‖s x-neutralIV106E18ITrial l h x‖ ≤ (η*C*L)*‖W x‖ := by
    filter_upwards [hw] with x hx
    rw [hx]
    by_cases hi : x ∈ I
    · simpa [Set.indicator_of_mem hi] using hf x
    · have hout : x ∉ Icc A B := by rwa [← hI]
      rw [hs x hout,neutralIV106E18ITrial_outside l h hh x
        (fun hm => hout (hsmall hm))]
      simp [Set.indicator_of_notMem hi]
  have hdb : ∀ᵐ x ∂volume,
      ‖SchwartzMap.derivCLM ℂ ℂ s x-neutralIV106E18SDTrial l h x‖ ≤ (η*C)*‖W x‖ := by
    filter_upwards [hw] with x hx
    rw [hx]
    by_cases hi : x ∈ I
    · simpa [Set.indicator_of_mem hi] using hd x
    · have hout : x ∉ Icc A B := by rwa [← hI]
      rw [neutralIV106E18UDeriv_outside s A B hs x hout,
        neutralIV106E18SDTrial_outside l h hh x (fun hm => hout (hsmall hm))]
      simp [Set.indicator_of_notMem hi]
  have hfn := neutralIV106E18IL2_error _ (neutralIV106E18JTrial_memLp l h hh)
    s W (η*C*L) hfb
  have hdn := neutralIV106E18IL2_error _ (neutralIV106E18SDTrial_memLp l h hh)
    (SchwartzMap.derivCLM ℂ ℂ s) W (η*C) hdb
  have hscale : δ = η*((‖W‖+1)*C*(L+1)) := by
    dsimp [η]
    field_simp [hden.ne']
  have hstrictF : η*C*L*‖W‖ < δ := by
    rw [hscale]
    have hpos : 0 < η*C*(L+‖W‖+1) := by positivity
    nlinarith only [hpos]
  have hstrictD : η*C*‖W‖ < δ := by
    rw [hscale]
    have hpos : 0 < η*C*(L+1) := by positivity
    have hn : 0 ≤ η*C*L*‖W‖ := by positivity
    nlinarith only [hpos,hn]
  refine ⟨(s.toLp 2 volume,(SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume),
    ⟨s,hs,rfl⟩,?_⟩
  rw [dist_comm]
  change max (dist (s.toLp 2 volume) _) (dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) _) < δ
  rw [max_lt_iff,dist_eq_norm,dist_eq_norm]
  exact ⟨hfn.trans_lt hstrictF,hdn.trans_lt hstrictD⟩

#print axioms neutralIV106E18UDeriv_outside
#print axioms neutralIV106E18UTrial_graph
end
end WeilDefect
