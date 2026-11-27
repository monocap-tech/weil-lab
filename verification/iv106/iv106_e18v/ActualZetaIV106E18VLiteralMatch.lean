import WeilDefect.Arithmetic.ActualZetaIV106E18VLogGraph

namespace WeilDefect
noncomputable section
open MeasureTheory Set FourierTransform
open scoped SchwartzMap FourierTransform

/-- The normalization constant is precisely the frozen Fourier convention. -/
theorem neutralIV106E18VScale_sq :
    ‖neutralIV106E18VScale‖^2 = 1/(4*Real.pi^2) := by
  unfold neutralIV106E18VScale
  rw [norm_inv,norm_mul,norm_mul,Complex.norm_I,mul_one,
    Complex.norm_real,Real.norm_eq_abs,abs_of_pos Real.pi_pos]
  norm_num
  field_simp [Real.pi_ne_zero]

/-- Actual clipped trial, full IV105C observation, and quantitative
logarithmic error, on the same fixed buffered cell. -/
theorem neutralIV106E18VLiteral_match (k : ℕ) (hk : 0 < k)
    (l h b : ℝ) (hh : 0 < h) (hb : 0 < b) (ε : ℝ) (hε : 0 < ε) :
    let f := (neutralIV106E18JTrial_memLp l h hh).toLp _
    let d := (neutralIV106E18SDTrial_memLp l h hh).toLp _
    ∃ s : 𝓢(ℝ,ℂ), (∀ x ∉ Icc (l-b) (l+h+b), s x = 0) ∧
      neutralIV106E18RObserve k hk (s.toLp 2 volume) =
        neutralIV106E18RObserve k hk f ∧
      dist (s.toLp 2 volume) f < ε ∧
      dist ((SchwartzMap.derivCLM ℂ ℂ s).toLp 2 volume) d < ε ∧
      (∫ ξ, logarithmicFourierWeight ξ *
        ‖(𝓕 (s.toLp 2 volume-f) : RealComplexL2) ξ‖^2) ≤
        (Real.exp 1+1+1/(4*Real.pi^2))*ε^2 := by
  dsimp only
  simpa only [neutralIV106E18VScale_sq] using
    neutralIV106E18VMatch (l-b) (l+h+b) (neutralIV106E18RObserve k hk)
      ((neutralIV106E18JTrial_memLp l h hh).toLp _)
      ((neutralIV106E18SDTrial_memLp l h hh).toLp _)
      (neutralIV106E18VTrial_graph l h b hh hb) ε hε

/-- The rough physical trial itself is now admitted to the original
logarithmic carrier, provided its literal cell is in the source window. -/
theorem neutralIV106E18VLiteral_admission (a l h b : ℝ)
    (hh : 0 < h) (hb : 0 < b) (hw : Icc l (l+h) ⊆ Icc (-a) a) :
    ∃ p : NeutralLogHilbertCarrier a,
      neutralLogPhysical p.val = (neutralIV106E18JTrial_memLp l h hh).toLp _ := by
  apply neutralIV106E18VAdmission (l-b) (l+h+b) a _
    ((neutralIV106E18SDTrial_memLp l h hh).toLp _)
    (neutralIV106E18VTrial_graph l h b hh hb)
  filter_upwards [(neutralIV106E18JTrial_memLp l h hh).coeFn_toLp] with x hx hxo
  rw [hx]
  exact neutralIV106E18ITrial_outside l h hh x (fun hi => hxo (hw hi))

#print axioms neutralIV106E18VScale_sq
#print axioms neutralIV106E18VLiteral_match
#print axioms neutralIV106E18VLiteral_admission
end
end WeilDefect
