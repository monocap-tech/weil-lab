import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerTableClosure
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIndexedEndpoints

namespace WeilDefect

/-! NF647: attach a certified integer moment table to its four local
endpoint receipts. The other 1277+ endpoint slots are not needed.
Avoid mistaking full-bank validity for a prerequisite of one key.
All reference comparisons are literal rectangular equalities. -/

def neutralNF647CacheCheck (c : NF638Cache) (p : NF591Ball)
    (R P : NF635EndpointBank) (k : NF616Frequency) : Bool :=
  let b := neutralNF634SharedCache p R.lookup P.lookup k
  neutralNF633RectEq (c.z.denote neutralNF616Q) b.z &&
    (neutralNF633RectEq (c.pos.denote neutralNF616Q) b.pos &&
      neutralNF633RectEq (c.neg.denote neutralNF616Q) b.neg)

theorem neutralNF647CacheCheck_sound (c : NF638Cache) (p : NF591Ball)
    (R P : NF635EndpointBank) (k : NF616Frequency)
    (h : neutralNF647CacheCheck c p R P k=true) :
    c.denote neutralNF616Q=neutralNF634SharedCache p R.lookup P.lookup k := by
  let b := neutralNF634SharedCache p R.lookup P.lookup k
  change (neutralNF633RectEq (c.z.denote neutralNF616Q) b.z &&
    (neutralNF633RectEq (c.pos.denote neutralNF616Q) b.pos &&
      neutralNF633RectEq (c.neg.denote neutralNF616Q) b.neg))=true at h
  simp only [Bool.and_eq_true] at h
  have hz := neutralNF633RectEq_sound _ _ h.1
  have hp := neutralNF633RectEq_sound _ _ h.2.1
  have hn := neutralNF633RectEq_sound _ _ h.2.2
  change c.denote neutralNF616Q=b
  cases c
  cases b
  simp_all [NF638Cache.denote]

theorem neutralNF647LocalLookup (b : NF635EndpointBank)
    (ref : ℚ → NF591Rect) (q : ℚ)
    (hc : neutralNF635ParamCheck b.keys q=true)
    (hs : b.read (neutralNF635Index b.keys q)=
      ref (neutralNF635ParamRead b.keys (neutralNF635Index b.keys q))) :
    b.lookup q=ref q := by
  have h : neutralNF635Index b.keys q < b.keys.size ∧
    neutralNF635ParamRead b.keys (neutralNF635Index b.keys q)=q :=
    of_decide_eq_true hc
  unfold NF635EndpointBank.lookup
  rw [hs,h.2]

theorem neutralNF647LocalCache (c : NF638Cache) (p : NF591Ball)
    (R P : NF635EndpointBank) (k : NF616Frequency)
    (hg : neutralNF647CacheCheck c p R P k=true)
    (hr : R.lookup k.h=neutralNF635RealRef k.h)
    (hrn : R.lookup (-k.h)=neutralNF635RealRef (-k.h))
    (hp : P.lookup (neutralNF592Reduced k.f)=neutralNF635PhaseRef p (neutralNF592Reduced k.f))
    (hpn : P.lookup (neutralNF592Reduced (-k.f))=neutralNF635PhaseRef p (neutralNF592Reduced (-k.f))) :
    c.denote neutralNF616Q=neutralNF621Cache p k neutralNF616Q neutralNF616ExpN :=
  (neutralNF647CacheCheck_sound c p R P k hg).trans
    (neutralNF634SharedCache_eq p R.lookup P.lookup k hr hrn hp hpn)

theorem neutralNF647Moment_of_local (t : NF638Table) (p : NF591Ball)
    (R P : NF635EndpointBank)
    (hpi : neutralNF592PiBall neutralNF616Q neutralNF616AtanN=p)
    (hc : neutralNF647CacheCheck t.cache p R P t.key=true)
    (hr : R.lookup t.key.h=neutralNF635RealRef t.key.h)
    (hrn : R.lookup (-t.key.h)=neutralNF635RealRef (-t.key.h))
    (hp : P.lookup (neutralNF592Reduced t.key.f)=neutralNF635PhaseRef p (neutralNF592Reduced t.key.f))
    (hpn : P.lookup (neutralNF592Reduced (-t.key.f))=neutralNF635PhaseRef p (neutralNF592Reduced (-t.key.f)))
    (hg : t.check neutralNF616Q neutralNF616ExpN=true)
    (n : ℕ) (hn : n < (t.keyTable neutralNF616Q).rows.size) :
    ‖neutralNF606ExpMoment (-(11/10:ℝ)) (11/10:ℝ) t.key.value n-
      (neutralNF617MomentRead (t.keyTable neutralNF616Q).rows n).value‖ ≤
      (neutralNF617MomentRead (t.keyTable neutralNF616Q).rows n).rad := by
  have h := t.to_original p hpi
    (neutralNF647LocalCache t.cache p R P t.key hc hr hrn hp hpn) hg
  exact neutralNF621FastHighPrecision_sound t.key
    (t.keyTable neutralNF616Q).rows h n hn

end WeilDefect
