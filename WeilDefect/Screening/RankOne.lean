import Mathlib.Analysis.InnerProductSpace.Adjoint
import Mathlib.Analysis.InnerProductSpace.LinearMap

namespace WeilDefect

open scoped InnerProduct
open ContinuousLinearMap
open InnerProductSpace

variable {𝕜 H : Type*}
variable [RCLike 𝕜]
variable [NormedAddCommGroup H] [InnerProductSpace 𝕜 H] [CompleteSpace H]

/--
Native operator identity in WD-T05:
the covariance of the one-dimensional synthesis α ↦ α • g
is the rank-one operator g ⊗ g.
-/
theorem wd_t05_rank_one_covariance (g : H) :
    (toSpanSingleton 𝕜 g) ∘L (toSpanSingleton 𝕜 g)†
      = rankOne 𝕜 g g := by
  rw [adjoint_toSpanSingleton]
  rfl

/-- Pointwise form of the WD-T05 rank-one covariance. -/
theorem wd_t05_rank_one_covariance_apply (g h : H) :
    (((toSpanSingleton 𝕜 g) ∘L (toSpanSingleton 𝕜 g)†) h)
      = inner 𝕜 g h • g := by
  rw [wd_t05_rank_one_covariance]
  rfl

end WeilDefect
