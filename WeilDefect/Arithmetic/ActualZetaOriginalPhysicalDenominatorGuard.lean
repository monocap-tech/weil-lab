import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFrequencyKeys

namespace WeilDefect
noncomputable section

/-! NF616: exact denominator guard. No approximation to π is
needed for a nonzero rational imaginary frequency. -/

def NF616Frequency.lower (k : NF616Frequency) : ℚ :=
  max |k.h| (6*|k.f|)

theorem NF616Frequency.re_value (k : NF616Frequency) :
    k.value.re = (k.h:ℝ) := by
  simp [NF616Frequency.value,neutralNF615Lambda,← Complex.ofReal_ratCast]

theorem NF616Frequency.im_value (k : NF616Frequency) :
    k.value.im = 2*Real.pi*(k.f:ℝ) := by
  simp [NF616Frequency.value,neutralNF615Lambda,← Complex.ofReal_ratCast]

theorem NF616Frequency.lower_sound (k : NF616Frequency) :
    (k.lower:ℝ) ≤ ‖k.value‖ := by
  have hr := Complex.abs_re_le_norm k.value
  have hi := Complex.abs_im_le_norm k.value
  rw [k.re_value] at hr
  rw [k.im_value,abs_mul,abs_mul,abs_of_nonneg Real.pi_pos.le,
    abs_of_nonneg (by norm_num : (0:ℝ)≤2)] at hi
  have hp : 6*|(k.f:ℝ)| ≤ 2*Real.pi*|(k.f:ℝ)| := by
    have h := mul_le_mul_of_nonneg_right Real.pi_gt_three.le (abs_nonneg (k.f:ℝ))
    linarith
  unfold NF616Frequency.lower
  have hh : (|(k.h:ℝ)|:ℝ) ≤ ‖k.value‖ := hr
  have hf := hp.trans hi
  push_cast
  exact max_le hh hf

theorem NF616Frequency.lower_pos (k : NF616Frequency)
    (hk : k.h ≠ 0 ∨ k.f ≠ 0) : 0<k.lower := by
  unfold NF616Frequency.lower
  rcases hk with hh|hf
  · exact (abs_pos.mpr hh).trans_le (le_max_left _ _)
  · exact (mul_pos (by norm_num) (abs_pos.mpr hf)).trans_le (le_max_right _ _)

theorem NF616Frequency.zero_value (k : NF616Frequency)
    (hh : k.h=0) (hf : k.f=0) : k.value=0 := by
  simp [NF616Frequency.value,neutralNF615Lambda,hh,hf]

theorem NF616Frequency.nonzero_guard (k : NF616Frequency)
    (hk : k.h ≠ 0 ∨ k.f ≠ 0) :
    0<(k.lower:ℝ) ∧ (k.lower:ℝ)≤ ‖k.value‖ :=
  ⟨by exact_mod_cast k.lower_pos hk,k.lower_sound⟩

end
end WeilDefect
