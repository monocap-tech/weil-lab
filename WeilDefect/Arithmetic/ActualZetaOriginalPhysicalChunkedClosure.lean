import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalChunkedBank
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMetadataCoverage
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerClosure

namespace WeilDefect
noncomputable section

/-! The numerical data, metadata, entry radii and integer products
are separate proposals. Only checked propositions connect them. -/

theorem neutralNF628OriginalPhysical_of_chunked_checks
    (chunks : List (Array NF624KeyTable)) (meta : Array NF624KeyTable)
    (s : NF626ScaledInputs) (c : NF626CenterCache)
    (hchunks : chunks.all neutralNF628ChunkCheck = true)
    (hshape : neutralNF627ShapeCheck (neutralNF628Join chunks) meta = true)
    (hcov : neutralNF624CoverageCheck meta (neutralNF624Index meta) = true)
    (hentry : neutralNF625EntryCheck
      (neutralNF624Lookup (neutralNF628Join chunks) (neutralNF624Index meta))
      s.payment = true)
    (hcache : c.check s = true)
    (hpay : c.fastPayCheck s = true) :
    ∃! a : Fin 242 → ℝ,
      neutralNF606Apply neutralNF606PhysicalH a = neutralNF612RHS ∧
      neutralNF587SourceInFrozenBox a neutralNF604OriginalCritical := by
  have hb := neutralNF628Bank_of_chunks chunks hchunks
  have hm := neutralNF627AllMoments_of_metadata
    (neutralNF628Join chunks) meta hb hshape hcov
  have he := neutralNF625EntryCheck_sound _ s.payment hm hentry
  exact s.payment.check_sound
    (c.payment_of_fast s (c.check_sound s hcache) hpay) he.1 he.2

end
end WeilDefect
