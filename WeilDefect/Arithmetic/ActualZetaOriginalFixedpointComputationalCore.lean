import Mathlib
import WeilDefect.Arithmetic.ActualZetaOriginalNF407FrozenData
import WeilDefect.Arithmetic.ActualZetaOriginalJ242SourceFunctions
import WeilDefect.Arithmetic.ActualZetaOriginalU400NormalizedBudget
import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointParameters

namespace WeilDefect
noncomputable section
open Finset

/-! NF595: computational definitions moved verbatim from NF591–NF594.
No analytic soundness theorem is imported here. The executable and
the proof modules use these SAME constants; no parallel implementation
is substituted. Real/complex containment predicates are non-executable
specifications and are not used by the numeric evaluator. -/

structure NF591Ball where
  mid : ℚ
  rad : ℚ
  deriving Repr

def NF591Ball.Contains (b : NF591Ball) (x : ℝ) : Prop :=
  |x-(b.mid:ℝ)| ≤ (b.rad:ℝ)

def NF591Ball.add (a b : NF591Ball) : NF591Ball :=
  ⟨a.mid+b.mid,a.rad+b.rad⟩

def NF591Ball.neg (a : NF591Ball) : NF591Ball :=
  ⟨-a.mid,a.rad⟩

def NF591Ball.mul (a b : NF591Ball) : NF591Ball :=
  ⟨a.mid*b.mid,|a.mid| * b.rad+|b.mid| * a.rad+a.rad*b.rad⟩

def NF591Ball.divPos (a : NF591Ball) (d : ℚ) : NF591Ball :=
  ⟨a.mid/d,a.rad/d⟩

def NF591Ball.Widens (a b : NF591Ball) : Prop :=
  |a.mid-b.mid|+a.rad ≤ b.rad

structure NF591Rect where
  re : NF591Ball
  im : NF591Ball

def NF591Rect.Contains (a : NF591Rect) (z : ℂ) : Prop :=
  a.re.Contains z.re ∧ a.im.Contains z.im

def NF591Rect.add (a b : NF591Rect) : NF591Rect :=
  ⟨a.re.add b.re,a.im.add b.im⟩

def NF591Rect.neg (a : NF591Rect) : NF591Rect :=
  ⟨a.re.neg,a.im.neg⟩

def NF591Rect.mul (a b : NF591Rect) : NF591Rect :=
  ⟨(a.re.mul b.re).add (a.im.mul b.im).neg,
    (a.re.mul b.im).add (a.im.mul b.re)⟩

def NF591Rect.divPos (a : NF591Rect) (d : ℚ) : NF591Rect :=
  ⟨a.re.divPos d,a.im.divPos d⟩

def NF591Rect.Widens (a b : NF591Rect) : Prop :=
  a.re.Widens b.re ∧ a.im.Widens b.im

def NF591Ball.round (a : NF591Ball) (Q : ℕ) : NF591Ball :=
  ⟨(⌊a.mid*Q⌋:ℚ)/Q,((⌈a.rad*Q⌉:ℚ)+1)/Q⟩

def NF591Ball.exactQ (q : ℚ) (Q : ℕ) : NF591Ball :=
  if (⌊q*(Q:ℚ)⌋:ℚ) = q*Q then ⟨q,0⟩ else (NF591Ball.mk q 0).round Q

def NF591Ball.expand (a : NF591Ball) (r : ℚ) : NF591Ball :=
  ⟨a.mid,a.rad+r⟩

def NF591Rect.realQ (q : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨NF591Ball.exactQ q Q,⟨0,0⟩⟩

def NF591Rect.one : NF591Rect := ⟨⟨1,0⟩,⟨0,0⟩⟩

def NF591Rect.zero : NF591Rect := ⟨⟨0,0⟩,⟨0,0⟩⟩

def NF591Rect.mulQ (a b : NF591Rect) (Q : ℕ) : NF591Rect :=
  let p := fun x y : NF591Ball => (x.mul y).round Q
  ⟨(p a.re b.re).add (p a.im b.im).neg,
    (p a.re b.im).add (p a.im b.re)⟩

def NF591Rect.divQ (a : NF591Rect) (d : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨(a.re.divPos d).round Q,(a.im.divPos d).round Q⟩

def NF591Rect.expand (a : NF591Rect) (r : ℚ) : NF591Rect :=
  ⟨a.re.expand r,a.im.expand r⟩

def neutralNF592ExpJetBall (a : NF591Rect) (Q : ℕ) : ℕ → NF591Rect
  | 0 => NF591Rect.one
  | n+1 => ((neutralNF592ExpJetBall a Q n).mulQ a Q).divQ (n+1:ℚ) Q

def neutralNF592ExpPartial (a : NF591Rect) (Q : ℕ) : ℕ → NF591Rect
  | 0 => NF591Rect.zero
  | n+1 => (neutralNF592ExpPartial a Q n).add (neutralNF592ExpJetBall a Q n)

def neutralNF592SmallExpBall (a : NF591Rect) (Q N : ℕ) : NF591Rect :=
  (neutralNF592ExpPartial a Q N).expand (1/(Q:ℚ))

def neutralNF592AtanTerm (x : ℚ) (n : ℕ) : ℚ :=
  (-1:ℚ)^n*x^(2*n+1)/(2*n+1:ℚ)

def neutralNF592AtanPartial (x : ℚ) (Q : ℕ) : ℕ → NF591Ball
  | 0 => ⟨0,0⟩
  | n+1 => (neutralNF592AtanPartial x Q n).add
    (NF591Ball.exactQ (neutralNF592AtanTerm x n) Q)

def neutralNF592AtanBall (x : ℚ) (Q N : ℕ) : NF591Ball :=
  (neutralNF592AtanPartial x Q N).expand (1/(Q:ℚ))

def neutralNF592PiBall (Q N : ℕ) : NF591Ball :=
  (((NF591Ball.exactQ 16 Q).mul (neutralNF592AtanBall (1/5) Q N)).round Q).add
    ((((NF591Ball.exactQ 4 Q).mul (neutralNF592AtanBall (1/239) Q N)).round Q).neg)

def neutralNF592Turns (f : ℚ) : ℤ := ⌊f*(11/10:ℚ)+1/2⌋

def neutralNF592Reduced (f : ℚ) : ℚ :=
  f*(11/10:ℚ)-neutralNF592Turns f

def neutralNF592PhaseArg (p : NF591Ball) (f : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨⟨0,0⟩,(p.mul (NF591Ball.exactQ (neutralNF592Reduced f/2) Q)).round Q⟩

def neutralNF592PhaseBall (p : NF591Ball) (f : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF592SmallExpBall (neutralNF592PhaseArg p f Q) Q N
  let b := a.mulQ a Q
  b.mulQ b Q

def NF591Rect.scaleQ (a : NF591Rect) (b : NF591Ball) (Q : ℕ) : NF591Rect :=
  ⟨(a.re.mul b).round Q,(a.im.mul b).round Q⟩

def NF591Rect.rotateMinusI (a : NF591Rect) : NF591Rect :=
  ⟨a.im,a.re.neg⟩

def neutralNF592RectSum (a : ℕ → NF591Rect) : ℕ → NF591Rect
  | 0 => NF591Rect.zero
  | n+1 => (neutralNF592RectSum a n).add (a n)

def neutralNF592PolyQ (k m : ℕ) : ℚ :=
  (k.choose m:ℚ)*(11/10:ℚ)^(k-m)*(-1/500:ℚ)^m

def neutralNF592ModeBall (a : NF591Rect) (Q k n : ℕ) : NF591Rect :=
  neutralNF592RectSum (fun m =>
    (neutralNF592ExpJetBall a Q (n-m)).scaleQ
      (NF591Ball.exactQ (neutralNF592PolyQ k m) Q) Q) (min k n+1)

def neutralNF592FrequencyBall (p : NF591Ball) (f : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨⟨0,0⟩,((p.mul (NF591Ball.exactQ (2*f/500) Q)).round Q).neg⟩

def neutralNF592OscillatorBall (p : NF591Ball) (f : ℚ) (Q N k n : ℕ) : NF591Ball :=
  let phase := neutralNF592PhaseBall p f Q N
  let phase' := if Even k then phase.rotateMinusI else phase
  (phase'.mulQ (neutralNF592ModeBall (neutralNF592FrequencyBall p f Q) Q k n) Q).re

def neutralNF592PoleBall (Q N n : ℕ) : NF591Ball :=
  let p := neutralNF592SmallExpBall (NF591Rect.realQ (11/20) Q) Q N
  let q := neutralNF592SmallExpBall (NF591Rect.realQ (-11/20) Q) Q N
  let ep := neutralNF592ExpJetBall (NF591Rect.realQ (-1/1000) Q) Q n
  let en := neutralNF592ExpJetBall (NF591Rect.realQ (1/1000) Q) Q n
  (((p.mulQ ep Q).re.add (q.mulQ en Q).re.neg).divPos 2).round Q

def neutralNF592BallSum {ι : Type*} (s : Finset ι) (a : ι → NF591Ball) : NF591Ball :=
  ⟨∑ j ∈ s, (a j).mid, ∑ j ∈ s, (a j).rad⟩

def neutralNF592DyadicQ (p : ℤ × ℤ) : ℚ :=
  (p.1:ℚ)*(2:ℚ)^p.2

def neutralNF592PrimitiveBox (row : (ℤ × ℤ) × (ℤ × ℤ)) (Q : ℕ) : NF591Ball :=
  let a := NF591Ball.exactQ (neutralNF592DyadicQ row.1) Q
  let r := NF591Ball.exactQ (neutralNF592DyadicQ row.2) Q
  a.expand (|r.mid|+r.rad)

def neutralNF592SelectedJetBall (p : NF591Ball) (Q N : ℕ) (j : Fin 242) (n : ℕ) : NF591Ball :=
  if hj : j.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    neutralNF592OscillatorBall p node.1 Q N node.2 n
  else neutralNF592PoleBall Q N n

def neutralNF592CriticalContribution (p : NF591Ball) (Q N : ℕ)
    (b : NF591Ball) (j : Fin 4) (n : ℕ) : NF591Ball :=
  (neutralNF592BallSum univ (fun k : Fin 32 =>
    ((((b.mul (NF591Ball.exactQ ((neutralNF587CriticalSines[j.val]!)[k.val]!) Q)).round Q).mul
      (neutralNF592OscillatorBall p neutralNF587CriticalFrequencies[k.val]! Q N 0 n)).round Q))).add
    ((((b.mul (NF591Ball.exactQ neutralNF587CriticalPoles[j.val]! Q)).round Q).mul
      (neutralNF592PoleBall Q N n)).round Q)

def neutralNF592SourceBall (p : NF591Ball) (Q N n : ℕ) : NF591Ball :=
  (neutralNF592BallSum univ (fun j : Fin 242 =>
    ((neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! Q).mul
      (neutralNF592SelectedJetBall p Q N j n)).round Q)).add
    (neutralNF592BallSum univ (fun j : Fin 4 =>
      neutralNF592CriticalContribution p Q N
        (neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! Q) j n))

def neutralNF592OriginalJetBall (n : ℕ) : NF591Ball :=
  neutralNF592SourceBall (neutralNF592PiBall neutralNF592Q 200)
    neutralNF592Q 220 n

def neutralNF592OriginalFixedpointBudget : Prop :=
  ∀ n : Fin 400, |(neutralNF592OriginalJetBall n.val).mid|+
    (neutralNF592OriginalJetBall n.val).rad ≤ (neutralNF588U400Ceil n.val:ℚ)/10^40

def neutralNF593ReadRect (v : Array NF591Rect) (n : ℕ) : NF591Rect :=
  v[n]?.getD NF591Rect.zero

def neutralNF593ExpTable (a : NF591Rect) (Q : ℕ) : ℕ → Array NF591Rect
  | 0 => #[NF591Rect.one]
  | n+1 =>
    let v := neutralNF593ExpTable a Q n
    v.push (((neutralNF593ReadRect v n).mulQ a Q).divQ (n+1:ℚ) Q)

def neutralNF593SmallExp (a : NF591Rect) (Q N : ℕ) : NF591Rect :=
  let table := neutralNF593ExpTable a Q N
  (neutralNF592RectSum (neutralNF593ReadRect table) N).expand (1/(Q:ℚ))

def neutralNF593Phase (p : NF591Ball) (f : ℚ) (Q N : ℕ) : NF591Rect :=
  let a := neutralNF593SmallExp (neutralNF592PhaseArg p f Q) Q N
  let b := a.mulQ a Q
  b.mulQ b Q

def neutralNF593ModeFromTable (table : Array NF591Rect) (Q k n : ℕ) : NF591Rect :=
  neutralNF592RectSum (fun m =>
    (neutralNF593ReadRect table (n-m)).scaleQ
      (NF591Ball.exactQ (neutralNF592PolyQ k m) Q) Q) (min k n+1)

def neutralNF593OscillatorTable (p : NF591Ball) (f : ℚ) (Q N k K : ℕ) :
    Array NF591Ball :=
  let phase := neutralNF593Phase p f Q N
  let phase' := if Even k then phase.rotateMinusI else phase
  let table := neutralNF593ExpTable (neutralNF592FrequencyBall p f Q) Q K
  Array.ofFn (fun n : Fin K =>
    (phase'.mulQ (neutralNF593ModeFromTable table Q k n.val) Q).re)

def neutralNF593ReadBall (table : Array NF591Ball) (n : ℕ) : NF591Ball :=
  table[n]?.getD ⟨0,0⟩

def neutralNF593PoleTable (Q N K : ℕ) : Array NF591Ball :=
  let p := neutralNF593SmallExp (NF591Rect.realQ (11/20) Q) Q N
  let q := neutralNF593SmallExp (NF591Rect.realQ (-11/20) Q) Q N
  let ep := neutralNF593ExpTable (NF591Rect.realQ (-1/1000) Q) Q K
  let en := neutralNF593ExpTable (NF591Rect.realQ (1/1000) Q) Q K
  Array.ofFn (fun n : Fin K =>
    (((p.mulQ (neutralNF593ReadRect ep n.val) Q).re.add
      (q.mulQ (neutralNF593ReadRect en n.val) Q).re.neg).divPos 2).round Q)

def neutralNF593ReadTable (a : Array (Array NF591Ball)) (j : ℕ) :
    Array NF591Ball := a[j]?.getD #[]

def neutralNF593SelectedTable (p : NF591Ball) (Q N K : ℕ) (j : Fin 242) :
    Array NF591Ball :=
  if hj : j.val < 241 then
    let node := nf545OriginalOscillatorNodeAt ⟨j.val,hj⟩
    neutralNF593OscillatorTable p node.1 Q N node.2 K
  else neutralNF593PoleTable Q N K

def neutralNF593CriticalFromTables (Q : ℕ) (b : NF591Ball)
    (j : Fin 4) (n : ℕ) (sines : Array (Array NF591Ball)) (pole : Array NF591Ball) : NF591Ball :=
  (neutralNF592BallSum univ (fun k : Fin 32 =>
    ((((b.mul (NF591Ball.exactQ ((neutralNF587CriticalSines[j.val]!)[k.val]!) Q)).round Q).mul
      (neutralNF593ReadBall (neutralNF593ReadTable sines k.val) n)).round Q))).add
    ((((b.mul (NF591Ball.exactQ neutralNF587CriticalPoles[j.val]! Q)).round Q).mul
      (neutralNF593ReadBall pole n)).round Q)

def neutralNF593SourceTable (p : NF591Ball) (Q N K : ℕ) : Array NF591Ball :=
  let selected := Array.ofFn (fun j : Fin 242 => neutralNF593SelectedTable p Q N K j)
  let sines := Array.ofFn (fun k : Fin 32 =>
    neutralNF593OscillatorTable p neutralNF587CriticalFrequencies[k.val]! Q N 0 K)
  let pole := neutralNF593PoleTable Q N K
  let a := Array.ofFn (fun j : Fin 242 => neutralNF592PrimitiveBox neutralNF587SelectedDyads[j.val]! Q)
  let b := Array.ofFn (fun j : Fin 4 => neutralNF592PrimitiveBox neutralNF587CriticalDyads[j.val]! Q)
  Array.ofFn (fun n : Fin K =>
    (neutralNF592BallSum univ (fun j : Fin 242 =>
      (( (neutralNF593ReadBall a j.val).mul
        (neutralNF593ReadBall (neutralNF593ReadTable selected j.val) n.val)).round Q))).add
      (neutralNF592BallSum univ (fun j : Fin 4 =>
        neutralNF593CriticalFromTables Q (neutralNF593ReadBall b j.val) j n.val sines pole)))

def neutralNF593OriginalTable : Array NF591Ball :=
  neutralNF593SourceTable (neutralNF592PiBall neutralNF592Q 200) neutralNF592Q 220 400

def neutralNF593CheckTable (t : Array NF591Ball) (K : ℕ) : Bool :=
  (List.range K).all (fun n =>
    let b := neutralNF593ReadBall t n
    decide (|b.mid|+b.rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40))

def neutralNF594BlockCheck (lo count : ℕ) : Bool :=
  let t := neutralNF593SourceTable (neutralNF592PiBall neutralNF592Q 200)
    neutralNF592Q 220 (lo+count)
  (List.range count).all (fun i =>
    let n := lo+i
    let b := neutralNF593ReadBall t n
    decide (|b.mid|+b.rad ≤ (neutralNF588U400Ceil n:ℚ)/10^40))

end
end WeilDefect
