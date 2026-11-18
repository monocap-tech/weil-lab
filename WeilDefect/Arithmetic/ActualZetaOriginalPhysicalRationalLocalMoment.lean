import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedExp
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSharedEndpointCache

namespace WeilDefect

/-! NF648: independent established rational path for a complete local
moment table. No full indexed bank, integer-rounding transfer, or
optional tail theorem is needed. Four local leaf identities and one
actual shared residual gate suffice. -/

noncomputable section

theorem neutralNF648Moment_of_local (p : NF591Ball) (R P : ℚ → NF591Rect)
    (t : NF624KeyTable)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hr : R t.key.h=neutralNF621RealEndpoint t.key.h neutralNF616Q neutralNF616ExpN)
    (hrn : R (-t.key.h)=neutralNF621RealEndpoint (-t.key.h) neutralNF616Q neutralNF616ExpN)
    (hp : P (neutralNF592Reduced t.key.f)=
      neutralNF634PhaseReduced p (neutralNF592Reduced t.key.f) neutralNF616Q neutralNF616ExpN)
    (hpn : P (neutralNF592Reduced (-t.key.f))=
      neutralNF634PhaseReduced p (neutralNF592Reduced (-t.key.f)) neutralNF616Q neutralNF616ExpN)
    (hg : neutralNF634SharedKeyCheck p R P t=true)
    (n : ℕ) (hn : n < t.rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) t.key.value n-
      (neutralNF617MomentRead t.rows n).value‖ ≤
      (neutralNF617MomentRead t.rows n).rad := by
  have hc := neutralNF634SharedCache_eq p R P t.key hr hrn hp hpn
  have ht := neutralNF634SharedKeyCheck_eq p R P t hc
  rw [ht] at hg
  rw [← hpi] at hg
  exact neutralNF621FastHighPrecision_sound t.key t.rows hg n hn

end
end WeilDefect
