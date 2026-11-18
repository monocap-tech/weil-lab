import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedExp
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIndexedEndpoints

namespace WeilDefect

/-! NF642: finish one shared slot from a certified segmented Taylor
prefix. The proposed argument, small exponential and final endpoint
are all bound by exact rectangle checks. The phase uses the reduced
parameter itself (not a guessed original frequency representative).
Pi attachment remains a separate hypothesis of the NF635 bank closure. -/

def neutralNF642PhaseArg (p : NF591Ball) (u : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨⟨0,0⟩,(p.mul (NF591Ball.exactQ (u/2) Q)).round Q⟩

theorem neutralNF642RealSlot (h : ℚ) (a b e : NF591Rect)
    (s : NF633ExpState)
    (ha : neutralNF633RectEq (NF591Rect.realQ (h*11/20) neutralNF616Q) a=true)
    (hs : neutralNF633State a neutralNF616Q neutralNF616ExpN=s)
    (hb : neutralNF633RectEq (s.sumState.expand (1/(neutralNF616Q:ℚ))) b=true)
    (he : neutralNF633RectEq (b.mulQ b neutralNF616Q) e=true) :
    neutralNF635RealRef h=e := by
  unfold neutralNF635RealRef
  apply neutralNF633RealEndpoint_of_small h neutralNF616Q neutralNF616ExpN b e
  · rw [neutralNF633RectEq_sound _ _ ha]
    exact neutralNF633SmallExp_of_state a neutralNF616Q neutralNF616ExpN s b hs hb
  · exact he

theorem neutralNF642PhaseSlot (p : NF591Ball) (u : ℚ) (a b e : NF591Rect)
    (s : NF633ExpState)
    (ha : neutralNF633RectEq (neutralNF642PhaseArg p u neutralNF616Q) a=true)
    (hs : neutralNF633State a neutralNF616Q neutralNF616ExpN=s)
    (hb : neutralNF633RectEq (s.sumState.expand (1/(neutralNF616Q:ℚ))) b=true)
    (he : neutralNF633RectEq ((b.mulQ b neutralNF616Q).mulQ
      (b.mulQ b neutralNF616Q) neutralNF616Q) e=true) :
    neutralNF635PhaseRef p u=e := by
  let z := neutralNF593SmallExp (neutralNF642PhaseArg p u neutralNF616Q)
    neutralNF616Q neutralNF616ExpN
  have hz : z = b := by
    dsimp only [z]
    rw [neutralNF633RectEq_sound _ _ ha]
    exact neutralNF633SmallExp_of_state a neutralNF616Q neutralNF616ExpN s b hs hb
  change ((z.mulQ z neutralNF616Q).mulQ
    (z.mulQ z neutralNF616Q) neutralNF616Q) = e
  rw [hz]
  exact neutralNF633RectEq_sound _ _ he

/-- Assemble explicit slot identities into the certified indexed-bank
interface. No reference computation is performed by the shape gate. -/
theorem neutralNF642Bank_of_slots (b : NF635EndpointBank) (ref : ℚ → NF591Rect)
    (hsize : decide (b.values.size=b.keys.size)=true)
    (hslots : ∀ i : Fin b.keys.size,
      b.read i.val=ref (neutralNF635ParamRead b.keys i.val)) :
    b.Valid ref := by
  refine ⟨of_decide_eq_true hsize,?_⟩
  intro i hi
  exact hslots ⟨i,hi⟩

/-- A single exact key match and exact value comparison attach a
proved literal endpoint to the stored slot. The comparisons do not
rerun the exponential or the Taylor prefix. -/
theorem neutralNF642AttachSlot (b : NF635EndpointBank) (ref : ℚ → NF591Rect)
    (i : ℕ) (q : ℚ) (v : NF591Rect)
    (hk : decide (neutralNF635ParamRead b.keys i=q)=true)
    (hv : neutralNF633RectEq (b.read i) v=true)
    (he : ref q=v) :
    b.read i=ref (neutralNF635ParamRead b.keys i) := by
  rw [of_decide_eq_true hk,he]
  exact neutralNF633RectEq_sound _ _ hv

end WeilDefect
