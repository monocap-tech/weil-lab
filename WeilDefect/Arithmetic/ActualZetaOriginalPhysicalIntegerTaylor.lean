import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalIntegerRounding

namespace WeilDefect

structure NF636Rect where
  re : NF636Ball
  im : NF636Ball
  deriving DecidableEq

def NF636Rect.denote (a : NF636Rect) (Q : ℕ) : NF591Rect :=
  ⟨a.re.denote Q,a.im.denote Q⟩

def NF636Rect.add (a b : NF636Rect) : NF636Rect :=
  ⟨a.re.add b.re,a.im.add b.im⟩

def NF636Rect.mul (a b : NF636Rect) (Q : ℕ) : NF636Rect :=
  ⟨(a.re.mul b.re Q).add (a.im.mul b.im Q).neg,
    (a.re.mul b.im Q).add (a.im.mul b.re Q)⟩

def NF636Rect.mulGate (a b : NF636Rect) (Q : ℕ) : Bool :=
  a.re.mulGate b.re Q &&
    (a.im.mulGate b.im Q && (a.re.mulGate b.im Q && a.im.mulGate b.re Q))

def NF636Rect.div (a : NF636Rect) (d : ℕ) : NF636Rect :=
  ⟨a.re.div d,a.im.div d⟩

def NF636Rect.divGate (a : NF636Rect) (d : ℕ) : Bool :=
  a.re.divGate d && a.im.divGate d

theorem NF636Rect.add_denote (a b : NF636Rect) (Q : ℕ) :
    (a.add b).denote Q=(a.denote Q).add (b.denote Q) := by
  simp only [NF636Rect.add,NF636Rect.denote,NF591Rect.add,NF636Ball.add_denote]

theorem NF636Rect.mul_denote (a b : NF636Rect) (Q : ℕ)
    (hQ : 0<Q) (h : a.mulGate b Q=true) :
    (a.mul b Q).denote Q=(a.denote Q).mulQ (b.denote Q) Q := by
  simp only [NF636Rect.mulGate,Bool.and_eq_true] at h
  simp only [NF636Rect.mul,NF636Rect.denote,NF591Rect.mulQ,
    NF636Ball.add_denote,NF636Ball.neg_denote,
    NF636Ball.mul_denote _ _ Q hQ h.1,
    NF636Ball.mul_denote _ _ Q hQ h.2.1,
    NF636Ball.mul_denote _ _ Q hQ h.2.2.1,
    NF636Ball.mul_denote _ _ Q hQ h.2.2.2]

theorem NF636Rect.div_denote (a : NF636Rect) (Q d : ℕ)
    (hQ : 0<Q) (h : a.divGate d=true) :
    (a.div d).denote Q=(a.denote Q).divQ (d:ℚ) Q := by
  simp only [NF636Rect.divGate,Bool.and_eq_true] at h
  simp only [NF636Rect.div,NF636Rect.denote,NF591Rect.divQ,
    NF636Ball.div_denote _ Q d hQ h.1,NF636Ball.div_denote _ Q d hQ h.2]

structure NF636State where
  jet : NF636Rect
  partial : NF636Rect
  deriving DecidableEq

def NF636State.denote (s : NF636State) (Q : ℕ) : NF633ExpState :=
  ⟨s.jet.denote Q,s.partial.denote Q⟩

def NF636State.step (s : NF636State) (a : NF636Rect) (Q n : ℕ) : NF636State :=
  ⟨(s.jet.mul a Q).div (n+1),s.partial.add s.jet⟩

def NF636State.stepGate (s : NF636State) (a : NF636Rect) (Q n : ℕ) : Bool :=
  s.jet.mulGate a Q && (s.jet.mul a Q).divGate (n+1)

theorem NF636State.step_denote (s : NF636State) (a : NF636Rect) (Q n : ℕ)
    (hQ : 0<Q) (hc : s.stepGate a Q n=true) :
    (s.step a Q n).denote Q=(s.denote Q).step (a.denote Q) Q n := by
  simp only [NF636State.stepGate,Bool.and_eq_true] at hc
  simp only [NF636State.step,NF636State.denote,NF633ExpState.step,
    NF636Rect.div_denote _ Q (n+1) hQ hc.2,
    NF636Rect.mul_denote _ _ Q hQ hc.1,NF636Rect.add_denote,
    Nat.cast_add,Nat.cast_one]

def neutralNF636Segment (a : NF636Rect) (Q start : ℕ) (s : NF636State) :
    ℕ → NF636State
  | 0 => s
  | n+1 => (neutralNF636Segment a Q start s n).step a Q (start+n)

def neutralNF636SegmentGate (a : NF636Rect) (Q start : ℕ) (s : NF636State) :
    ℕ → Bool
  | 0 => true
  | n+1 => neutralNF636SegmentGate a Q start s n &&
    (neutralNF636Segment a Q start s n).stepGate a Q (start+n)

theorem neutralNF636Segment_denote (a : NF636Rect) (Q start : ℕ) (s : NF636State)
    (len : ℕ) (hQ : 0<Q) (hc : neutralNF636SegmentGate a Q start s len=true) :
    (neutralNF636Segment a Q start s len).denote Q =
      neutralNF633Segment (a.denote Q) Q start (s.denote Q) len := by
  induction len with
  | zero => rfl
  | succ n ih =>
    simp only [neutralNF636SegmentGate,Bool.and_eq_true] at hc
    rw [neutralNF636Segment,neutralNF633Segment,
      NF636State.step_denote _ _ _ _ hQ hc.2,ih hc.1]

def neutralNF636TransitionCheck (a : NF636Rect) (Q start len : ℕ)
    (s t : NF636State) : Bool :=
  neutralNF636SegmentGate a Q start s len &&
    decide (neutralNF636Segment a Q start s len=t)

theorem neutralNF636Prefix_extend (a : NF636Rect) (Q start len : ℕ)
    (s t : NF636State) (hQ : 0<Q)
    (hs : neutralNF633State (a.denote Q) Q start=s.denote Q)
    (hc : neutralNF636TransitionCheck a Q start len s t=true) :
    neutralNF633State (a.denote Q) Q (start+len)=t.denote Q := by
  simp only [neutralNF636TransitionCheck,Bool.and_eq_true] at hc
  have he : neutralNF636Segment a Q start s len=t := of_decide_eq_true hc.2
  have h := neutralNF636Segment_denote a Q start s len hQ hc.1
  rw [he] at h
  rw [← neutralNF633Segment_reference,hs]
  exact h.symm

end WeilDefect
