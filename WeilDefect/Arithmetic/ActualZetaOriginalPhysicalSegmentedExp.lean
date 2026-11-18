import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalFastMomentTable
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalSegmentedPi

namespace WeilDefect

/-! Carry both the current rounded Taylor jet and the sum preceding it.
A segment starts at an independently proposed state. Local equality
checks and prefix composition retain the exact reference evaluator. -/

structure NF633ExpState where
  jet : NF591Rect
  partial : NF591Rect

def neutralNF633State (a : NF591Rect) (Q n : ℕ) : NF633ExpState :=
  ⟨neutralNF592ExpJetBall a Q n,neutralNF592ExpPartial a Q n⟩

def NF633ExpState.step (s : NF633ExpState) (a : NF591Rect) (Q n : ℕ) :
    NF633ExpState :=
  ⟨(s.jet.mulQ a Q).divQ (n+1:ℚ) Q,s.partial.add s.jet⟩

theorem neutralNF633State_step (a : NF591Rect) (Q n : ℕ) :
    (neutralNF633State a Q n).step a Q n = neutralNF633State a Q (n+1) := rfl

def neutralNF633Segment (a : NF591Rect) (Q start : ℕ) (s : NF633ExpState) :
    ℕ → NF633ExpState
  | 0 => s
  | n+1 => (neutralNF633Segment a Q start s n).step a Q (start+n)

theorem neutralNF633Segment_reference (a : NF591Rect) (Q start len : ℕ) :
    neutralNF633Segment a Q start (neutralNF633State a Q start) len =
      neutralNF633State a Q (start+len) := by
  induction len with
  | zero => rfl
  | succ n ih =>
    rw [neutralNF633Segment,ih,neutralNF633State_step,Nat.add_succ]

def neutralNF633RectEq (a b : NF591Rect) : Bool :=
  neutralNF632BallEq a.re b.re && neutralNF632BallEq a.im b.im

theorem neutralNF633RectEq_sound (a b : NF591Rect)
    (h : neutralNF633RectEq a b=true) : a=b := by
  have h' := h
  simp only [neutralNF633RectEq,Bool.and_eq_true] at h'
  have hr := neutralNF632BallEq_sound _ _ h'.1
  have hi := neutralNF632BallEq_sound _ _ h'.2
  cases a
  cases b
  simp_all

def neutralNF633StateEq (s t : NF633ExpState) : Bool :=
  neutralNF633RectEq s.jet t.jet && neutralNF633RectEq s.partial t.partial

theorem neutralNF633StateEq_sound (s t : NF633ExpState)
    (h : neutralNF633StateEq s t=true) : s=t := by
  have h' := h
  simp only [neutralNF633StateEq,Bool.and_eq_true] at h'
  have hj := neutralNF633RectEq_sound _ _ h'.1
  have hp := neutralNF633RectEq_sound _ _ h'.2
  cases s
  cases t
  simp_all

theorem neutralNF633Prefix_extend (a : NF591Rect) (Q start len : ℕ)
    (s t : NF633ExpState) (hs : neutralNF633State a Q start=s)
    (hc : neutralNF633StateEq (neutralNF633Segment a Q start s len) t=true) :
    neutralNF633State a Q (start+len)=t := by
  rw [← neutralNF633Segment_reference,hs]
  exact neutralNF633StateEq_sound _ _ hc

theorem neutralNF633SmallExp_of_state (a : NF591Rect) (Q N : ℕ)
    (s : NF633ExpState) (b : NF591Rect)
    (hs : neutralNF633State a Q N=s)
    (hc : neutralNF633RectEq (s.partial.expand (1/(Q:ℚ))) b=true) :
    neutralNF593SmallExp a Q N=b := by
  rw [neutralNF593SmallExp_eq]
  unfold neutralNF592SmallExpBall
  have hp := congrArg NF633ExpState.partial hs
  change neutralNF592ExpPartial a Q N=s.partial at hp
  rw [hp]
  exact neutralNF633RectEq_sound _ _ hc

theorem neutralNF633RealEndpoint_of_small (h : ℚ) (Q N : ℕ)
    (b e : NF591Rect)
    (hb : neutralNF593SmallExp (NF591Rect.realQ (h*11/20) Q) Q N=b)
    (he : neutralNF633RectEq (b.mulQ b Q) e=true) :
    neutralNF621RealEndpoint h Q N=e := by
  unfold neutralNF621RealEndpoint
  rw [hb]
  exact neutralNF633RectEq_sound _ _ he

theorem neutralNF633Phase_of_small (p : NF591Ball) (f : ℚ) (Q N : ℕ)
    (b e : NF591Rect)
    (hb : neutralNF593SmallExp (neutralNF592PhaseArg p f Q) Q N=b)
    (he : neutralNF633RectEq ((b.mulQ b Q).mulQ (b.mulQ b Q) Q) e=true) :
    neutralNF593Phase p f Q N=e := by
  unfold neutralNF593Phase
  rw [hb]
  exact neutralNF633RectEq_sound _ _ he

end WeilDefect
