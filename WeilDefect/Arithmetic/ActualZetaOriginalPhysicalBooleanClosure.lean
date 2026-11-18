import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRationalPayments
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalBankIndex
import WeilDefect.Arithmetic.ActualZetaOriginalCollarStrictMargin

namespace WeilDefect

/-! NF625: the independently generated entry centers need not be
identical to those of the internal interval evaluator. A rational
widening comparison must explicitly pay the difference. -/

def neutralNF625EntryHCheck (M : NF622Moments) (p : NF625PaymentData)
    (i j : Fin 242) : Bool :=
  let b := neutralNF624HBall M neutralNF616Q i j
  decide (|b.mid-p.H0 i j| + b.rad ≤ p.eH)

def neutralNF625EntryVCheck (M : NF622Moments) (p : NF625PaymentData)
    (i : Fin 242) (j : Fin 4) : Bool :=
  let b := neutralNF624VBall M neutralNF616Q i j
  decide (|b.mid-p.V0 i j| + b.rad ≤ p.eV)

def neutralNF625EntryCheck (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  ((List.finRange 242).all (fun i =>
    (List.finRange 242).all (neutralNF625EntryHCheck M p i))) &&
  ((List.finRange 242).all (fun i =>
    (List.finRange 4).all (neutralNF625EntryVCheck M p i)))

noncomputable section
open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

theorem neutralNF625EntryCheck_sound (M : NF622Moments) (p : NF625PaymentData)
    (hM : neutralNF624AllMomentsSound M)
    (hc : neutralNF625EntryCheck M p = true) :
    (∀ i j, |neutralNF606PhysicalH i j-p.HR i j| ≤ (p.eH:ℝ)) ∧
    (∀ i j, |neutralNF606PhysicalV i j-p.VR i j| ≤ (p.eV:ℝ)) := by
  unfold neutralNF625EntryCheck at hc
  simp only [Bool.and_eq_true] at hc
  constructor
  · intro i j
    have hi := (List.all_eq_true.mp hc.1) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hh := neutralNF624HBall_sound M neutralNF616Q neutralNF616Q_pos hM i j
    have hw : (neutralNF624HBall M neutralNF616Q i j).Widens
        ⟨p.H0 i j,p.eH⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true hj
    exact NF591Ball.contains_widen hh hw
  · intro i j
    have hi := (List.all_eq_true.mp hc.2) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hh := neutralNF624VBall_sound M neutralNF616Q neutralNF616Q_pos hM i j
    have hw : (neutralNF624VBall M neutralNF616Q i j).Widens
        ⟨p.V0 i j,p.eV⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true hj
    exact NF591Ball.contains_widen hh hw

/-- Four explicit Boolean receipts suffice. Their actual truth
remains a finite verification obligation, not an axiom. -/
theorem neutralNF625OriginalPhysical_of_checks
    (bank : Array NF624KeyTable) (p : NF625PaymentData)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (hentry : neutralNF625EntryCheck (neutralNF624Lookup bank (neutralNF624Index bank)) p = true)
    (hpay : p.check = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hm := neutralNF624AllMoments_of_bank bank (neutralNF624Index bank) hbank
    (neutralNF624Index_coverage bank hcov)
  have he := neutralNF625EntryCheck_sound _ p hm hentry
  exact p.check_sound hpay he.1 he.2

theorem neutralNF625OriginalPhysical_strict_of_checks
    (bank : Array NF624KeyTable) (p : NF625PaymentData)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (hentry : neutralNF625EntryCheck (neutralNF624Lookup bank (neutralNF624Index bank)) p = true)
    (hpay : p.check = true) :
    ∃ (a : Fin 242 → ℝ)
      (hLp : MemLp (neutralNF575OriginalEndpoint
        (neutralNF587Source a neutralNF604OriginalCritical)) 2 volume)
      (K : NeutralActualZetaSourceDomain (11/10:ℝ))
      (f : ℕ → 𝓢(ℝ,ℂ)),
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical ∧
      neutralNF598GraphPhysical (11/10) K =
        hLp.toLp (neutralNF575OriginalEndpoint
          (neutralNF587Source a neutralNF604OriginalCritical)) ∧
      0 < (2/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 ∧
      (2/5:ℝ)*‖neutralNF598GraphPhysical (11/10) K‖^2 <
        neutralNF598GraphWeil (11/10) K ∧
      (∀ n x, conj (f n x) = f n x) ∧
      (∀ n x, f n (-x) = -f n x) ∧
      (∀ n x, x ∉ neutralNF543OriginalCollars → f n x = 0) ∧
      (∀ n, neutralNF546OriginalSelectedMoments ((f n).toLp 2 volume) =
        neutralNF546OriginalSelectedMoments (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, (2/5:ℝ)*‖(f n).toLp 2 volume‖^2 < neutralNF598SmoothWeil (f n)) := by
  obtain ⟨a,⟨ha,hbox⟩,_⟩ := neutralNF625OriginalPhysical_of_checks bank p hbank hcov hentry hpay
  obtain ⟨hLp,K,f,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩ :=
    neutralNF610OriginalCorrectedMargin a neutralNF604OriginalCritical hbox
  exact ⟨a,hLp,K,f,ha,hbox,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩

end
end WeilDefect
