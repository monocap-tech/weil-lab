import WeilDefect.Arithmetic.ActualZetaOriginalFixedpointPhase
import WeilDefect.Arithmetic.ActualZetaOriginalNF407CanonicalJetRecurrence

namespace WeilDefect
noncomputable section
open Finset

/-! NF592: per-mode rounded finite convolution, using the exact
all-order recurrence. A separate finite table evaluator can cache
these results; the soundness lemma is independent of the cache. -/

def NF591Rect.scaleQ (a : NF591Rect) (b : NF591Ball) (Q : ℕ) : NF591Rect :=
  ⟨(a.re.mul b).round Q,(a.im.mul b).round Q⟩

theorem NF591Rect.contains_scaleQ {a : NF591Rect} {b : NF591Ball}
    {z : ℂ} {x : ℝ} (ha : a.Contains z) (hb : b.Contains x)
    (Q : ℕ) (hQ : 0 < Q) : (a.scaleQ b Q).Contains (z*(x:ℂ)) := by
  constructor
  · simpa [scaleQ,Complex.mul_re] using NF591Ball.contains_rounded_mul ha.1 hb Q hQ
  · simpa [scaleQ,Complex.mul_im] using NF591Ball.contains_rounded_mul ha.2 hb Q hQ

def NF591Rect.rotateMinusI (a : NF591Rect) : NF591Rect :=
  ⟨a.im,a.re.neg⟩

theorem NF591Rect.contains_rotateMinusI {a : NF591Rect} {z : ℂ}
    (h : a.Contains z) : a.rotateMinusI.Contains (-Complex.I*z) := by
  constructor
  · simpa [rotateMinusI,Complex.mul_re] using h.2
  · simpa [rotateMinusI,Complex.mul_im] using NF591Ball.contains_neg h.1

def neutralNF592RectSum (a : ℕ → NF591Rect) : ℕ → NF591Rect
  | 0 => NF591Rect.zero
  | n+1 => (neutralNF592RectSum a n).add (a n)

theorem neutralNF592RectSum_sound (a : ℕ → NF591Rect) (z : ℕ → ℂ) (N : ℕ)
    (h : ∀ n < N, (a n).Contains (z n)) :
    (neutralNF592RectSum a N).Contains (∑ n ∈ range N, z n) := by
  induction N with
  | zero => simpa [neutralNF592RectSum] using NF591Rect.contains_zero
  | succ N ih =>
    rw [neutralNF592RectSum,sum_range_succ]
    exact NF591Rect.contains_add (ih (fun n hn => h n (by omega))) (h N (by omega))

def neutralNF592PolyQ (k m : ℕ) : ℚ :=
  (k.choose m:ℚ)*(11/10:ℚ)^(k-m)*(-1/500:ℚ)^m

def neutralNF592ModeBall (a : NF591Rect) (Q k n : ℕ) : NF591Rect :=
  neutralNF592RectSum (fun m =>
    (neutralNF592ExpJetBall a Q (n-m)).scaleQ
      (NF591Ball.exactQ (neutralNF592PolyQ k m) Q) Q) (min k n+1)

theorem neutralNF592ModeBall_sound (a : NF591Rect) (lam : ℂ) (Q k n : ℕ)
    (hQ : 0 < Q) (ha : a.Contains lam) :
    (neutralNF592ModeBall a Q k n).Contains
      (neutralNF590ModeJet (11/10) (-1/500) lam k n) := by
  rw [neutralNF590ModeJet_truncate]
  apply neutralNF592RectSum_sound
  intro m hm
  have h := NF591Rect.contains_scaleQ
    (neutralNF592ExpJetBall_sound a lam Q hQ ha (n-m))
    (NF591Ball.contains_exactQ (neutralNF592PolyQ k m) Q hQ) Q hQ
  convert h using 1
  unfold neutralNF590PolyTerm neutralNF592PolyQ
  push_cast
  ring

def neutralNF592FrequencyBall (p : NF591Ball) (f : ℚ) (Q : ℕ) : NF591Rect :=
  ⟨⟨0,0⟩,((p.mul (NF591Ball.exactQ (2*f/500) Q)).round Q).neg⟩

theorem neutralNF592FrequencyBall_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (f : ℚ) (Q : ℕ) (hQ : 0 < Q) :
    (neutralNF592FrequencyBall p f Q).Contains
      (-(Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ))/500) := by
  have he : -(Complex.I*((2*Real.pi*(f:ℝ):ℝ):ℂ))/500 =
      ((-(Real.pi*(2*(f:ℝ)/500)):ℝ):ℂ)*Complex.I := by
    push_cast
    ring
  rw [he]
  constructor
  · simp [neutralNF592FrequencyBall,NF591Ball.Contains,Complex.mul_re]
  · have h := NF591Ball.contains_neg (NF591Ball.contains_rounded_mul hp
        (NF591Ball.contains_exactQ (2*f/500) Q hQ) Q hQ)
    simpa [neutralNF592FrequencyBall,Complex.mul_im,Rat.cast_div,Rat.cast_mul] using h

def neutralNF592OscillatorBall (p : NF591Ball) (f : ℚ) (Q N k n : ℕ) : NF591Ball :=
  let phase := neutralNF592PhaseBall p f Q N
  let phase' := if Even k then phase.rotateMinusI else phase
  (phase'.mulQ (neutralNF592ModeBall (neutralNF592FrequencyBall p f Q) Q k n) Q).re

theorem neutralNF592OscillatorBall_sound (p : NF591Ball) (hp : p.Contains Real.pi)
    (f : ℚ) (Q N k n : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592OscillatorBall p f Q N k n).Contains
      (neutralNF590OscillatorJet (f:ℝ) k n) := by
  have hphase := neutralNF592PhaseBall_sound p hp f Q N hQ hN hfee
  have hfreq := neutralNF592FrequencyBall_sound p hp f Q hQ
  have hmode := neutralNF592ModeBall_sound _ _ Q k n hQ hfreq
  unfold neutralNF592OscillatorBall neutralNF590OscillatorJet
  by_cases hk : Even k
  · simp only [if_pos hk]
    exact (NF591Rect.contains_mulQ (NF591Rect.contains_rotateMinusI hphase) hmode Q hQ).1
  · simp only [if_neg hk,one_mul]
    exact (NF591Rect.contains_mulQ hphase hmode Q hQ).1

def neutralNF592PoleBall (Q N n : ℕ) : NF591Ball :=
  let p := neutralNF592SmallExpBall (NF591Rect.realQ (11/20) Q) Q N
  let q := neutralNF592SmallExpBall (NF591Rect.realQ (-11/20) Q) Q N
  let ep := neutralNF592ExpJetBall (NF591Rect.realQ (-1/1000) Q) Q n
  let en := neutralNF592ExpJetBall (NF591Rect.realQ (1/1000) Q) Q n
  (((p.mulQ ep Q).re.add (q.mulQ en Q).re.neg).divPos 2).round Q

theorem neutralNF592PoleBall_sound (Q N n : ℕ) (hQ : 0 < Q) (hN : 1 ≤ N)
    (hfee : 2/(N.factorial:ℝ) ≤ 1/(Q:ℝ)) :
    (neutralNF592PoleBall Q N n).Contains (neutralNF590PoleJet n) := by
  have hp := neutralNF592SmallExpBall_sound _ _ Q N hQ hN
    (NF591Rect.contains_realQ (11/20) Q hQ)
    (by rw [← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs]; norm_num) hfee
  have hq := neutralNF592SmallExpBall_sound _ _ Q N hQ hN
    (NF591Rect.contains_realQ (-11/20) Q hQ)
    (by rw [← Complex.ofReal_ratCast,Complex.norm_real,Real.norm_eq_abs]; norm_num) hfee
  have ep := neutralNF592ExpJetBall_sound _ _ Q hQ
    (NF591Rect.contains_realQ (-1/1000) Q hQ) n
  have en := neutralNF592ExpJetBall_sound _ _ Q hQ
    (NF591Rect.contains_realQ (1/1000) Q hQ) n
  have h1 := (NF591Rect.contains_mulQ hp ep Q hQ).1
  have h2 := (NF591Rect.contains_mulQ hq en Q hQ).1
  have h := NF591Ball.contains_rounded_div
    (NF591Ball.contains_add h1 (NF591Ball.contains_neg h2)) 2 (by norm_num) Q hQ
  simpa [neutralNF592PoleBall,neutralNF590PoleJet,Complex.sub_re,sub_eq_add_neg] using h

end
end WeilDefect
