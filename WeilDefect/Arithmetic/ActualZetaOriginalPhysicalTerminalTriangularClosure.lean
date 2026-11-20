import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalRowClosure
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularCacheAssembly
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalExecutableEntryChecks

namespace WeilDefect

/-!
NF712: the exact terminal original-physical certificate contract.

There is no new numerical oracle here. NF707 physical row receipts have the
NF674 form, while the accepted NF629 analytical soundness bridge consumes
NF629 row gates. The first theorem transfers the actual former to the latter.

The second theorem packages only the independent finite gates still required:
bank truth, coverage, original physical rows, every HD identity, the lower
A triangle, vector gates, and fast integer payment rows. NF704 proves the
redundant upper A triangle from symmetry. No complete cache or payment truth
is introduced as a hypothesis.

The strict corrected carrier theorem is conditional on the same finite gates.
The hypotheses must be discharged on the actual NF690/NF702/NF703 objects
by subsequent source-bound Lean certificates.
-/

theorem neutralNF712EntryRow_of_original
    (M : NF622Moments) (p : NF625PaymentData) (i : Fin 242)
    (h : neutralNF674OriginalRowCheck M p i = true) :
    neutralNF629EntryRow M p i = true := by
  unfold neutralNF674OriginalRowCheck at h
  simp only [Bool.and_eq_true] at h
  unfold neutralNF629EntryRow
  simp only [Bool.and_eq_true]
  constructor
  · apply List.all_eq_true.mpr
    intro j hj
    by_cases hle : j.val ≤ i.val
    · have hlo :
          (List.finRange 242).all
            (fun k => if k.val ≤ i.val
              then neutralNF625EntryHCheck M p i k else true) = true := by
        exact h.1.1
      have hgate := (List.all_eq_true.mp hlo) j hj
      change (if j.val ≤ i.val then
        neutralNF625EntryHCheck M p i j else true) = true at hgate
      simpa only [neutralNF629HGate, if_pos hle] using
        (show neutralNF625EntryHCheck M p i j = true by
          simpa only [if_pos hle] using hgate)
    · have hsym :
          (List.finRange 242).all
            (fun k => decide (p.H0 i k = p.H0 k i)) = true := by
        exact h.1.2
      have hgate := (List.all_eq_true.mp hsym) j hj
      simpa only [neutralNF629HGate, if_neg hle] using hgate
  · exact h.2

noncomputable section

/-- Source-independent composition of the actual original payment row
certificates, the reduced triangular cache, and all 242 fast payments.
The original center cache is never equated to an unproved result oracle. -/
theorem neutralNF712OriginalPhysical_of_triangular
    (bank : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (hentry : ∀ i, neutralNF674OriginalRowCheck
      (neutralNF624Lookup bank (neutralNF624Index bank))
      s.payment i = true)
    (hH : ∀ i j, s.H i j = s.H j i)
    (hA : ∀ i j, c.A i j = c.A j i)
    (hw : s.wCheck = true)
    (hHD : ∀ i j, c.HDGate s i j = true)
    (hLower : ∀ i j, j.val ≤ i.val → c.AGate s i j = true)
    (hVec : ∀ i, c.vectorGate s i = true)
    (hparams : neutralNF629Parameters s = true)
    (hpay : ∀ i, c.fastPayGate s i = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hm : neutralNF624AllMomentsSound
      (neutralNF624Lookup bank (neutralNF624Index bank)) :=
    neutralNF624AllMoments_of_bank bank (neutralNF624Index bank)
      hbank (neutralNF624Index_coverage bank hcov)
  have he := neutralNF629EntryRows_sound
    (neutralNF624Lookup bank (neutralNF624Index bank))
    s.payment hm (fun i => neutralNF712EntryRow_of_original _ _ i (hentry i))
  have hc : c.check s = true :=
    neutralNF704Cache_of_triangular s c hH hA hw hHD hLower hVec
  have hvalid : c.Valid s := c.check_sound s hc
  have hp : c.fastPayCheck s = true :=
    neutralNF629Payments_of_rows c s hparams hpay
  exact s.payment.check_sound (c.payment_of_fast s hvalid hp) he.1 he.2

open MeasureTheory Filter
open scoped SchwartzMap ComplexConjugate

/-- The same finite source-specific gates recover the already-established
original strictly corrected carrier. This asserts no global Weil positivity
and is conditional until every numerical gate is proved on original data. -/
theorem neutralNF712OriginalStrict_of_triangular
    (bank : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hbank : neutralNF624BankCheck bank = true)
    (hcov : neutralNF624CoverageCheck bank (neutralNF624Index bank) = true)
    (hentry : ∀ i, neutralNF674OriginalRowCheck
      (neutralNF624Lookup bank (neutralNF624Index bank))
      s.payment i = true)
    (hH : ∀ i j, s.H i j = s.H j i)
    (hA : ∀ i j, c.A i j = c.A j i)
    (hw : s.wCheck = true)
    (hHD : ∀ i j, c.HDGate s i j = true)
    (hLower : ∀ i j, j.val ≤ i.val → c.AGate s i j = true)
    (hVec : ∀ i, c.vectorGate s i = true)
    (hparams : neutralNF629Parameters s = true)
    (hpay : ∀ i, c.fastPayGate s i = true) :
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
        neutralNF546OriginalSelectedMoments
          (neutralNF598GraphPhysical (11/10) K)) ∧
      (∀ᶠ n in atTop, (2/5:ℝ)*‖(f n).toLp 2 volume‖^2 <
        neutralNF598SmoothWeil (f n)) := by
  obtain ⟨a, ⟨ha,hbox⟩, _⟩ :=
    neutralNF712OriginalPhysical_of_triangular
      bank s c hbank hcov hentry hH hA hw hHD hLower hVec hparams hpay
  obtain ⟨hLp,K,f,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩ :=
    neutralNF610OriginalCorrectedMargin a neutralNF604OriginalCritical hbox
  exact ⟨a,hLp,K,f,ha,hbox,hK,hpos,hstrict,hreal,hodd,hsupp,hmom,hevent⟩

end

#print axioms neutralNF712EntryRow_of_original
#print axioms neutralNF712OriginalPhysical_of_triangular
#print axioms neutralNF712OriginalStrict_of_triangular

end WeilDefect
