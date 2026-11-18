import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalTriangularEntries
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalChunkedClosure

namespace WeilDefect

/-! Each proof obligation has a row-local Boolean interface.
Composition uses the individual equalities, not a second execution
of the full transformed matrix arithmetic. -/

def neutralNF629CacheRow (c : NF626CenterCache) (s : NF626ScaledInputs)
    (i : Fin 242) : Bool :=
  (List.finRange 242).all (c.HDGate s i) &&
  ((List.finRange 242).all (c.AGate s i) && c.vectorGate s i)

def neutralNF629Parameters (s : NF626ScaledInputs) : Bool :=
  decide (0<s.S ∧ 0<s.Q ∧ 0<s.T ∧ 0<s.U ∧ 0≤s.r ∧ 0≤s.eH ∧ 0≤s.eV)

theorem neutralNF629Cache_of_rows (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hw : s.wCheck = true)
    (hc : ∀ i, neutralNF629CacheRow c s i = true) :
    c.check s = true := by
  have hr (i : Fin 242) :
      (List.finRange 242).all (c.HDGate s i) = true ∧
      (List.finRange 242).all (c.AGate s i) = true ∧
      c.vectorGate s i = true := by
    have h := hc i
    simpa only [neutralNF629CacheRow,Bool.and_eq_true] using h
  unfold NF626CenterCache.check
  simp only [Bool.and_eq_true]
  exact ⟨hw,List.all_eq_true.mpr (fun i _ => (hr i).1),
    List.all_eq_true.mpr (fun i _ => (hr i).2.1),
    List.all_eq_true.mpr (fun i _ => (hr i).2.2)⟩

theorem neutralNF629Payments_of_rows (c : NF626CenterCache) (s : NF626ScaledInputs)
    (hp : neutralNF629Parameters s = true)
    (hr : ∀ i, c.fastPayGate s i = true) : c.fastPayCheck s = true := by
  unfold NF626CenterCache.fastPayCheck
  exact Bool.and_eq_true.mpr ⟨hp,List.all_eq_true.mpr (fun i _ => hr i)⟩

/-- A finite set of per-row truths can be packaged as a universal
statement without rerunning a large numerical check. -/
theorem neutralNF629Rows_of_list (f : Fin 242 → Bool)
    (h : (List.finRange 242).all f = true) :
    ∀ i, f i = true := by
  intro i
  exact (List.all_eq_true.mp h) i (by simp)

noncomputable section

theorem neutralNF629OriginalPhysical_of_rows
    (chunks : List (Array NF624KeyTable)) (metadata : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hchunks : chunks.all neutralNF628ChunkCheck = true)
    (hshape : neutralNF627ShapeCheck (neutralNF628Join chunks) metadata = true)
    (hcov : neutralNF624CoverageCheck metadata (neutralNF624Index metadata) = true)
    (hentry : ∀ i, neutralNF629EntryRow
      (neutralNF624Lookup (neutralNF628Join chunks) (neutralNF624Index metadata))
      s.payment i = true)
    (hw : s.wCheck = true)
    (hcache : ∀ i, neutralNF629CacheRow c s i = true)
    (hparam : neutralNF629Parameters s = true)
    (hpay : ∀ i, c.fastPayGate s i = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hb := neutralNF628Bank_of_chunks chunks hchunks
  have hm := neutralNF627AllMoments_of_metadata
    (neutralNF628Join chunks) metadata hb hshape hcov
  have he := neutralNF629EntryRows_sound _ s.payment hm hentry
  have hc := c.check_sound s (neutralNF629Cache_of_rows c s hw hcache)
  exact s.payment.check_sound
    (c.payment_of_fast s hc (neutralNF629Payments_of_rows c s hparam hpay))
    he.1 he.2

end
end WeilDefect
