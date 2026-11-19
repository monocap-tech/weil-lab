import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerClosure
import Mathlib.Tactic

namespace WeilDefect
open Finset MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-!
NF673: reduce the original 242×242 H interval widening gate to
its exact lower triangle using the ALREADY PROVED symmetry of the
original physical integral H. The proposed rational center matrix
must be independently checked symmetric: no untrusted symmetry
assumption is hidden in the compact data.

Only 242*243/2 = 29,403 expensive H-ball widening comparisons remain,
plus 242*4 = 968 mixed V comparisons and inexpensive rational-center
symmetry comparisons. No numerical boolean is asserted true here.
-/

def neutralNF673LowerHEntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 242).all (fun j =>
      if j.val ≤ i.val then neutralNF625EntryHCheck M p i j else true))

def neutralNF673CenterSymmetryCheck (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 242).all (fun j =>
      decide (p.H0 i j = p.H0 j i)))

def neutralNF673MixedVEntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (List.finRange 242).all (fun i =>
    (List.finRange 4).all (neutralNF625EntryVCheck M p i))

/-- The source-specific reduced interval receipt: H lower triangle,
exact symmetry of historical rational H centers, and all four
historical V columns. Its independent truth remains to be checked. -/
def neutralNF673EntryCheck
    (M : NF622Moments) (p : NF625PaymentData) : Bool :=
  (neutralNF673LowerHEntryCheck M p &&
    neutralNF673CenterSymmetryCheck p) &&
    neutralNF673MixedVEntryCheck M p

noncomputable section

/-- The lower triangular source-entry enclosure is enough to bound
every original real H entry, because genuine H symmetry was proved
directly from the original NF606 integral definition. -/
theorem neutralNF673EntryCheck_sound
    (M : NF622Moments) (p : NF625PaymentData)
    (hM : neutralNF624AllMomentsSound M)
    (hc : neutralNF673EntryCheck M p = true) :
    (∀ i j, |neutralNF606PhysicalH i j - p.HR i j| ≤ (p.eH : ℝ)) ∧
    (∀ i j, |neutralNF606PhysicalV i j - p.VR i j| ≤ (p.eV : ℝ)) := by
  unfold neutralNF673EntryCheck at hc
  simp only [Bool.and_eq_true] at hc
  have hLower := hc.1.1
  have hCenter := hc.1.2
  have hMixed := hc.2
  have hsymmetric (i j : Fin 242) : p.H0 i j = p.H0 j i := by
    have hi := (List.all_eq_true.mp hCenter) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    exact of_decide_eq_true hj
  have hLowerBound (i j : Fin 242) (hji : j.val ≤ i.val) :
      |neutralNF606PhysicalH i j - p.HR i j| ≤ (p.eH : ℝ) := by
    have hi := (List.all_eq_true.mp hLower) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hg : neutralNF625EntryHCheck M p i j = true := by
      simpa [hji] using hj
    have hSource :=
      neutralNF624HBall_sound M neutralNF616Q neutralNF616Q_pos hM i j
    have hWiden :
        (neutralNF624HBall M neutralNF616Q i j).Widens
          ⟨p.H0 i j, p.eH⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true hg
    exact NF591Ball.contains_widen hSource hWiden
  constructor
  · intro i j
    by_cases hji : j.val ≤ i.val
    · exact hLowerBound i j hji
    · have hij : i.val ≤ j.val := by omega
      have h := hLowerBound j i hij
      change |neutralNF606PhysicalH i j - (p.H0 i j : ℝ)| ≤ (p.eH : ℝ)
      rw [neutralNF606PhysicalH_symm i j, hsymmetric i j]
      change |neutralNF606PhysicalH j i - (p.H0 j i : ℝ)| ≤ (p.eH : ℝ)
      exact h
  · intro i j
    have hi := (List.all_eq_true.mp hMixed) i (by simp)
    have hj := (List.all_eq_true.mp hi) j (by simp)
    have hSource :=
      neutralNF624VBall_sound M neutralNF616Q neutralNF616Q_pos hM i j
    have hWiden :
        (neutralNF624VBall M neutralNF616Q i j).Widens
          ⟨p.V0 i j, p.eV⟩ := by
      unfold NF591Ball.Widens
      exact of_decide_eq_true hj
    exact NF591Ball.contains_widen hSource hWiden

/-- The accepted NF625 242-solve enclosure follows from the reduced
H-triangle certificate, unchanged full V gate, and EXISTING exact
integer cache and payment gates. No new numerical premise is dropped. -/
theorem neutralNF673OriginalPhysical_of_triangular_fast_checks
    (bank : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (htri : neutralNF673EntryCheck
      (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment = true)
    (hcache : c.check s = true)
    (hpay : c.fastPayCheck s = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hm := neutralNF624AllMoments_of_bank
    bank (neutralNF624Index bank) hbank
    (neutralNF624Index_coverage bank hcov)
  have he := neutralNF673EntryCheck_sound
    (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment hm htri
  have hv : c.Valid s := c.check_sound s hcache
  have hp : s.payment.check = true := c.payment_of_fast s hv hpay
  exact s.payment.check_sound hp he.1 he.2

/-- Conditional Phase III exit, with precisely the same original
carrier and certified 2/5 signed Weil margin as NF625; its only
change is an exact reduction of the numerical H-widening workload.
None of the five original data-dependent Booleans is asserted true. -/
theorem neutralNF673OriginalPhysical_strict_of_triangular_fast_checks
    (bank : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (htri : neutralNF673EntryCheck
      (neutralNF624Lookup bank (neutralNF624Index bank)) s.payment = true)
    (hcache : c.check s = true)
    (hpay : c.fastPayCheck s = true) :
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
      (∀ᶠ n in atTop, (2/5:ℝ)*‖(f n).toLp 2 volume‖^2 <
        neutralNF598SmoothWeil (f n)) := by
  obtain ⟨a, ⟨ha, hbox⟩, _⟩ :=
    neutralNF673OriginalPhysical_of_triangular_fast_checks
      bank s c hbank hcov htri hcache hpay
  obtain ⟨hLp,K,f,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩ :=
    neutralNF610OriginalCorrectedMargin a
      neutralNF604OriginalCritical hbox
  exact ⟨a,hLp,K,f,ha,hbox,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩

#print axioms neutralNF673EntryCheck_sound
#print axioms neutralNF673OriginalPhysical_of_triangular_fast_checks
#print axioms neutralNF673OriginalPhysical_strict_of_triangular_fast_checks

end
end WeilDefect
