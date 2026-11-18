import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalResidualReceipts
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalDenominatorGuard

namespace WeilDefect

/-! NF617: one exact frequency key, one cached pair of endpoint
exponentials, one ascending table of candidate moments. The
checker uses only rational arithmetic. Full table soundness is
a subsequent obligation; the recurrence lemmas have the required
local statement shape. -/

structure NF617MomentRow where
  re : ℚ
  im : ℚ
  rad : ℚ
  deriving Inhabited, Repr

def NF617MomentRow.rect (r : NF617MomentRow) (Q : ℕ) : NF591Rect :=
  ⟨NF591Ball.exactQ r.re Q,NF591Ball.exactQ r.im Q⟩

structure NF617MomentCache where
  z : NF591Rect
  pos : NF591Rect
  neg : NF591Rect

def neutralNF617Cache (p : NF591Ball) (k : NF616Frequency) (Q N : ℕ) :
    NF617MomentCache :=
  ⟨neutralNF615LambdaRect p k.h k.f Q,
   neutralNF615Endpoint p k.h k.f Q N,
   neutralNF615Endpoint p (-k.h) (-k.f) Q N⟩

def NF617MomentCache.boundary (c : NF617MomentCache) (Q n : ℕ) : NF591Rect :=
  ((NF591Rect.realQ ((11/10:ℚ)^n) Q).mulQ c.pos Q).add
    (((NF591Rect.realQ ((-11/10:ℚ)^n) Q).mulQ c.neg Q).neg)

theorem neutralNF617Cache_boundary_eq (p : NF591Ball) (k : NF616Frequency)
    (Q N n : ℕ) :
    (neutralNF617Cache p k Q N).boundary Q n =
      neutralNF615BoundaryRect p k.h k.f Q N n := rfl

def neutralNF617MomentRead (rows : Array NF617MomentRow) (n : ℕ) : NF617MomentRow :=
  rows[n]?.getD default

def neutralNF617MomentRowCheck (c : NF617MomentCache) (δ : ℚ)
    (Q : ℕ) (rows : Array NF617MomentRow) (n : ℕ) : Bool :=
  let q := neutralNF617MomentRead rows n
  match n with
  | 0 =>
    decide (0 ≤ q.rad) &&
    neutralNF615RectBelow (neutralNF615BaseResidualRect (c.boundary Q 0) c.z (q.rect Q) Q)
      (δ*q.rad)
  | m+1 =>
    let prev := neutralNF617MomentRead rows m
    decide (0 ≤ q.rad) &&
    neutralNF615RectBelow
      (neutralNF615ResidualRect (c.boundary Q (m+1)) c.z (prev.rect Q) (q.rect Q) Q m)
      (δ*q.rad-(m+1:ℚ)*prev.rad)

def neutralNF617NonzeroTableCheck (p : NF591Ball) (k : NF616Frequency)
    (Q N : ℕ) (rows : Array NF617MomentRow) : Bool :=
  let δ := k.lower
  let c := neutralNF617Cache p k Q N
  decide (0<Q ∧ 0<N ∧ |k.h| ≤ 1 ∧ 0<δ ∧ 0<rows.size) &&
    (List.range rows.size).all (neutralNF617MomentRowCheck c δ Q rows)

/-- Zero exponent: use the exact polynomial primitive, rather than
running a singular recurrence. -/
def neutralNF617ZeroMoment (n : ℕ) : ℚ :=
  ((11/10:ℚ)^(n+1)-(-11/10:ℚ)^(n+1))/(n+1:ℚ)

end WeilDefect
