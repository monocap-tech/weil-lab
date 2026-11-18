import WeilDefect.Arithmetic.ActualZetaOriginalNF407DiscTableBounds
import Mathlib.Analysis.Complex.ExponentialBounds

namespace WeilDefect
noncomputable section
open Finset
set_option maxRecDepth 100000
set_option maxHeartbeats 4000000

/-! NF603: strict source nonvanishing does not need the highly
cancelled endpoint value. The genuine real sinh pole dominates
every polynomially bounded oscillator at a remote point of the
SAME entire source. This point is used only for uniqueness,
never as an extra support point of the physical carrier. -/

def neutralNF603PoleIndex : Fin 242 := ⟨241,by decide⟩

theorem neutralNF603Pole_upper_rat :
    neutralNF589DyadicQ neutralNF587SelectedDyads[241]!.1+
      |neutralNF589DyadicQ neutralNF587SelectedDyads[241]!.2| < -(10:ℚ)^140 := by
  decide +kernel

theorem neutralNF603CriticalPole_small_rat :
    ∀ j : Fin 4, |neutralNF587CriticalPoles[j.val]!| ≤ (1/10^6:ℚ) := by
  decide +kernel

theorem neutralNF603Pole_upper (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    a neutralNF603PoleIndex < -(10:ℝ)^140 := by
  have hr : ((neutralNF589DyadicQ neutralNF587SelectedDyads[241]!.1+
    |neutralNF589DyadicQ neutralNF587SelectedDyads[241]!.2|:ℚ):ℝ) <
    ((-(10:ℚ)^140:ℚ):ℝ) := Rat.cast_lt.mpr neutralNF603Pole_upper_rat
  rw [Rat.cast_add,Rat.cast_abs,neutralNF589Dyadic_cast,neutralNF589Dyadic_cast,
    Rat.cast_neg,Rat.cast_pow,Rat.cast_ofNat] at hr
  have h := (le_abs_self (a neutralNF603PoleIndex-neutralNF587SelectedMid neutralNF603PoleIndex)).trans
    (hbox.1 neutralNF603PoleIndex)
  change a neutralNF603PoleIndex-neutralNF587Dyadic neutralNF587SelectedDyads[241]!.1 ≤
    |neutralNF587Dyadic neutralNF587SelectedDyads[241]!.2| at h
  linarith only [h,hr]

def neutralNF603PoleCoeff (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) : ℝ :=
  a neutralNF603PoleIndex + ∑ j : Fin 4, b j * (neutralNF587CriticalPoles[j.val]! : ℝ)

theorem neutralNF603PoleCoeff_upper (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    neutralNF603PoleCoeff a b < -(10:ℝ)^139 := by
  have hb := (neutralNF589ScalarBounds_of_box a b hbox).2.1
  have ht (j : Fin 4) : b j * (neutralNF587CriticalPoles[j.val]! : ℝ) ≤ (10:ℝ)^137 := by
    have hh : |(neutralNF587CriticalPoles[j.val]! : ℝ)| ≤ (1/10^6:ℝ) := by
      have h : ((|neutralNF587CriticalPoles[j.val]!|:ℚ):ℝ) ≤
          ((1/10^6:ℚ):ℝ) := Rat.cast_le.mpr (neutralNF603CriticalPole_small_rat j)
      simpa only [Rat.cast_abs,Rat.cast_div,Rat.cast_one,Rat.cast_pow,Rat.cast_ofNat] using h
    calc
      _ ≤ |b j * (neutralNF587CriticalPoles[j.val]! : ℝ)| := le_abs_self _
      _ ≤ (10:ℝ)^143*(1/10^6) := by
        rw [abs_mul]
        exact mul_le_mul (hb j) hh (abs_nonneg _) (by positivity)
      _ = _ := by norm_num
  have hs : (∑ j : Fin 4, b j * (neutralNF587CriticalPoles[j.val]! : ℝ)) ≤ 4*(10:ℝ)^137 := by
    calc
      _ ≤ ∑ _ : Fin 4, (10:ℝ)^137 := sum_le_sum (fun j _ => ht j)
      _ = _ := by simp
  have ha := neutralNF603Pole_upper a b hbox
  unfold neutralNF603PoleCoeff
  calc
    _ < -(10:ℝ)^140 + 4*10^137 := add_lt_add_of_lt_of_le ha hs
    _ ≤ _ := by norm_num

def neutralNF603OscillatorPart (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (x : ℝ) : ℝ :=
  (∑ j : Fin 242, if j=neutralNF603PoleIndex then 0 else
    a j * nf545OriginalSelectedRealGenerator j x) +
  ∑ j : Fin 4, b j * ∑ k : Fin 32,
    (neutralNF587CriticalSines[j.val]!)[k.val]! * Real.sin
      (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*x)

theorem neutralNF603Source_split (a : Fin 242 → ℝ) (b : Fin 4 → ℝ) (x : ℝ) :
    neutralNF587Source a b x =
      neutralNF603OscillatorPart a b x + neutralNF603PoleCoeff a b*Real.sinh (x/2) := by
  have hsel : (∑ j : Fin 242, a j * nf545OriginalSelectedRealGenerator j x) =
      (∑ j : Fin 242, if j=neutralNF603PoleIndex then 0 else
        a j * nf545OriginalSelectedRealGenerator j x) +
      a neutralNF603PoleIndex*Real.sinh (x/2) := by
    have hp : (∑ j : Fin 242, if j=neutralNF603PoleIndex then
        a j*nf545OriginalSelectedRealGenerator j x else 0) =
        a neutralNF603PoleIndex*Real.sinh (x/2) := by
      rw [Finset.sum_ite_eq_of_mem' _ _ _ (Finset.mem_univ _)]
      rw [show nf545OriginalSelectedRealGenerator neutralNF603PoleIndex x =
        Real.sinh (x/2) from nf545OriginalSelectedPole_is_sinh x]
    rw [← hp,← sum_add_distrib]
    apply sum_congr rfl
    intro j _
    by_cases hj : j=neutralNF603PoleIndex <;> simp [hj]
  have hcrit : (∑ j : Fin 4, b j*neutralNF587CriticalGenerator j x) =
      (∑ j : Fin 4, b j * ∑ k : Fin 32,
        ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ)*Real.sin
          (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*x)) +
        (∑ j : Fin 4, b j*(neutralNF587CriticalPoles[j.val]! : ℝ))*Real.sinh (x/2) := by
    rw [sum_mul,← sum_add_distrib]
    apply sum_congr rfl
    intro j _
    unfold neutralNF587CriticalGenerator
    ring
  unfold neutralNF587Source neutralNF569OriginalRealCombination
    neutralNF603OscillatorPart neutralNF603PoleCoeff
  rw [hsel,hcrit,add_mul]
  ring

theorem neutralNF603OscillatorPart_bound (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    |neutralNF603OscillatorPart a b 1000| ≤ (400:ℝ)*10^182 := by
  obtain ⟨ha,hb,hn,hf,hc,hp⟩ := neutralNF589ScalarBounds_of_box a b hbox
  have hterm (j : Fin 242) :
      |if j=neutralNF603PoleIndex then (0:ℝ) else
        a j * nf545OriginalSelectedRealGenerator j 1000| ≤ (10:ℝ)^182 := by
    by_cases hj : j=neutralNF603PoleIndex
    · simp [hj]
    · have hlt : j.val<241 := by
        by_contra! hh
        apply hj
        apply Fin.ext
        change j.val=241
        omega
      let i : Fin 241 := ⟨j.val,hlt⟩
      have hk : (nf545OriginalOscillatorNodeAt i).2 ≤ 13 := (hn i).2.2
      have ht : |if Even (nf545OriginalOscillatorNodeAt i).2 then
          Real.sin (2*Real.pi*(nf545OriginalOscillatorNodeAt i).1*1000) else
          Real.cos (2*Real.pi*(nf545OriginalOscillatorNodeAt i).1*1000)| ≤ 1 := by
        split_ifs
        · exact Real.abs_sin_le_one _
        · exact Real.abs_cos_le_one _
      simp only [if_neg hj,nf545OriginalSelectedRealGenerator,dif_pos hlt]
      change |a j * ((1000:ℝ)^(nf545OriginalOscillatorNodeAt i).2 * _)| ≤ _
      rw [abs_mul,abs_mul,abs_of_nonneg (show 0 ≤ (1000:ℝ)^(nf545OriginalOscillatorNodeAt i).2 by positivity)]
      have hk' : (1000:ℝ)^(nf545OriginalOscillatorNodeAt i).2 ≤ (1000:ℝ)^13 :=
        pow_le_pow_right₀ (by norm_num) hk
      calc
        _ ≤ (10:ℝ)^143*((1000:ℝ)^13*1) :=
          mul_le_mul (ha j) (mul_le_mul hk' ht (abs_nonneg _) (by positivity))
            (by positivity) (by positivity)
        _ = _ := by
          rw [mul_one,show (1000:ℝ)=10^3 by norm_num,← pow_mul,← pow_add]
  have hcrit (j : Fin 4) : |b j * ∑ k : Fin 32,
      ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ) * Real.sin
        (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*1000)| ≤
          32*(10:ℝ)^143 := by
    rw [abs_mul]
    have hk (k : Fin 32) :
        |((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ) *
          Real.sin (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*1000)| ≤ 1 := by
      rw [abs_mul]
      have hh : |((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ)| ≤ 1 := by
        exact_mod_cast hc j k
      exact (mul_le_mul hh (Real.abs_sin_le_one _) (abs_nonneg _) (by norm_num)).trans_eq (one_mul _)
    have hs : |∑ k : Fin 32,
        ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ) *
          Real.sin (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*1000)| ≤ 32 := by
      apply (abs_sum_le_sum_abs _ _).trans
      calc
        _ ≤ ∑ _ : Fin 32, (1:ℝ) := sum_le_sum (fun k _ => hk k)
        _ = _ := by simp
    exact (mul_le_mul (hb j) hs (abs_nonneg _) (by positivity)).trans_eq (mul_comm _ _)
  unfold neutralNF603OscillatorPart
  apply (abs_add_le _ _).trans
  have hs : |∑ j : Fin 242, if j=neutralNF603PoleIndex then (0:ℝ) else
      a j*nf545OriginalSelectedRealGenerator j 1000| ≤ 242*(10:ℝ)^182 := by
    apply (abs_sum_le_sum_abs _ _).trans
    calc
      _ ≤ ∑ _ : Fin 242, (10:ℝ)^182 := sum_le_sum (fun j _ => hterm j)
      _ = _ := by simp
  have ht : |∑ j : Fin 4, b j * ∑ k : Fin 32,
      ((neutralNF587CriticalSines[j.val]!)[k.val]! : ℝ) * Real.sin
        (2*Real.pi*(neutralNF587CriticalFrequencies[k.val]! : ℝ)*1000)| ≤ 4*(32*(10:ℝ)^143) := by
    apply (abs_sum_le_sum_abs _ _).trans
    calc
      _ ≤ ∑ _ : Fin 4, 32*(10:ℝ)^143 := sum_le_sum (fun j _ => hcrit j)
      _ = _ := by simp
  exact (add_le_add hs ht).trans (by norm_num)

theorem neutralNF603Sinh500_lower : (10:ℝ)^60 < Real.sinh 500 := by
  have he : (2:ℝ)<Real.exp 1 := (by norm_num : (2:ℝ) < 2.7182818283).trans Real.exp_one_gt_d9
  have hpow : (2:ℝ)^500 < Real.exp 500 := by
    rw [show (500:ℝ)=(500:ℕ)*1 by norm_num,Real.exp_nat_mul]
    exact pow_lt_pow_left₀ he (by norm_num) (by decide)
  have hneg : Real.exp (-500) ≤ 1 := by
    rw [← Real.exp_zero]
    exact Real.exp_le_exp.mpr (by norm_num)
  rw [Real.sinh_eq]
  have hnat : (2:ℕ)*10^60+1 < 2^500 := by decide +kernel
  have hnum : (2:ℝ)*10^60+1 < 2^500 := by exact_mod_cast hnat
  have hE := hnum.trans hpow
  linarith only [hE,hneg]

theorem neutralNF603Source_remote_negative (a : Fin 242 → ℝ) (b : Fin 4 → ℝ)
    (hbox : neutralNF587SourceInFrozenBox a b) :
    neutralNF587Source a b 1000 < 0 := by
  have hp := neutralNF603PoleCoeff_upper a b hbox
  have ht := neutralNF603Sinh500_lower
  have hs : 0 < Real.sinh 500 := (by positivity : 0 < (10:ℝ)^60).trans ht
  have ho := (le_abs_self _).trans (neutralNF603OscillatorPart_bound a b hbox)
  have hprod : neutralNF603PoleCoeff a b*Real.sinh 500 < -(10:ℝ)^199 := by
    calc
      _ < -(10:ℝ)^139*Real.sinh 500 := mul_lt_mul_of_pos_right hp hs
      _ < -(10:ℝ)^139*10^60 := mul_lt_mul_of_neg_left ht (neg_lt_zero.mpr (by positivity))
      _ = _ := by norm_num
  rw [neutralNF603Source_split,show (1000:ℝ)/2=500 by norm_num]
  calc
    _ < (400:ℝ)*10^182-10^199 := by linarith only [ho,hprod]
    _ < _ := by norm_num

end
end WeilDefect
