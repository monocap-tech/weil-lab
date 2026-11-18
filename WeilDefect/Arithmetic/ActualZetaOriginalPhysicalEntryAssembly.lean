import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentTableSound
import WeilDefect.Arithmetic.ActualZetaOriginalPhysicalMomentParity

namespace WeilDefect
noncomputable section

/-! NF622: turn a signed, non-default-valued moment enclosure
into a rectangular input to the actual physical term dictionary.
Only the required keys/degrees are premises. -/

def NF617MomentRow.enclosure (q : NF617MomentRow) : NF591Rect :=
  ⟨⟨q.re,q.rad⟩,⟨q.im,q.rad⟩⟩

theorem NF617MomentRow.enclosure_sound (q : NF617MomentRow) (z : ℂ)
    (h : ‖z-q.value‖ ≤ (q.rad:ℝ)) : q.enclosure.Contains z := by
  have hr := (Complex.abs_re_le_norm (z-q.value)).trans h
  have hi := (Complex.abs_im_le_norm (z-q.value)).trans h
  constructor
  · simpa [NF617MomentRow.enclosure,NF591Ball.Contains,NF617MomentRow.value,
      Complex.sub_re,Complex.add_re,Complex.mul_re] using hr
  · simpa [NF617MomentRow.enclosure,NF591Ball.Contains,NF617MomentRow.value,
      Complex.sub_im,Complex.add_im,Complex.mul_im] using hi

def NF616Frequency.opposite (k : NF616Frequency) : NF616Frequency :=
  ⟨-k.h,-k.f⟩

def NF616Frequency.flip (k : NF616Frequency) : Bool :=
  decide (k.f<0 ∨ (k.f=0 ∧ k.h<0))

def NF616Frequency.canonical (k : NF616Frequency) : NF616Frequency :=
  if k.flip then k.opposite else k

theorem NF616Frequency.opposite_value (k : NF616Frequency) :
    k.opposite.value = -k.value :=
  neutralNF615Lambda_neg k.h k.f

def neutralNF622Restore (k : NF616Frequency) (n : ℕ) (a : NF591Rect) : NF591Rect :=
  if k.flip && decide (n%2=1) then a.neg else a

theorem neutralNF622Restore_sound (k : NF616Frequency) (n : ℕ) (a : NF591Rect)
    (ha : a.Contains (neutralNF620J k.canonical.value n)) :
    (neutralNF622Restore k n a).Contains (neutralNF620J k.value n) := by
  by_cases hf : k.flip = true
  · have hc : k.canonical.value = -k.value := by
      unfold NF616Frequency.canonical
      rw [if_pos hf,NF616Frequency.opposite_value]
    rw [hc] at ha
    have he : neutralNF620J k.value n = (-1:ℂ)^n *
        neutralNF620J (-k.value) n := by
      simpa only [neg_neg] using neutralNF620J_neg (-k.value) n
    rw [he]
    by_cases hn : n%2=1
    · have hn' : Odd n := ⟨n/2,by omega⟩
      simp only [neutralNF622Restore,hf,of_decide_eq_true (show decide (n%2=1)=true from by
        simp [hn]),Bool.true_and,if_true]
      rw [hn'.neg_one_pow]
      simpa only [neg_one_mul] using NF591Rect.contains_neg ha
    · have hn' : Even n := ⟨n/2,by omega⟩
      simp [neutralNF622Restore,hf,hn,hn'.neg_one_pow,ha]
  · have hc : k.canonical = k := by simp [NF616Frequency.canonical,hf]
    rw [hc] at ha
    simpa [neutralNF622Restore,hf] using ha

theorem neutralNF622ZeroMoment_sound (n Q : ℕ) (hQ : 0<Q) :
    (NF591Rect.realQ (neutralNF617ZeroMoment n) Q).Contains (neutralNF620J 0 n) := by
  have he := neutralNF606ExpMoment_zero_frequency (-(11/10:ℝ)) (11/10:ℝ) n
  unfold neutralNF620J
  rw [he]
  convert NF591Rect.contains_realQ (neutralNF617ZeroMoment n) Q hQ using 1 <;>
    simp [neutralNF617ZeroMoment] <;> push_cast <;> ring

structure NF622TermSpec where
  key : NF616Frequency
  degree : ℕ
  coeffRe : ℚ
  coeffIm : ℚ

def NF622TermSpec.coeff (t : NF622TermSpec) : ℂ :=
  ((t.coeffRe:ℝ):ℂ)+((t.coeffIm:ℝ):ℂ)*Complex.I

def NF622TermSpec.coeffRect (t : NF622TermSpec) (Q : ℕ) : NF591Rect :=
  ⟨NF591Ball.exactQ t.coeffRe Q,NF591Ball.exactQ t.coeffIm Q⟩

def NF622TermSpec.term (t : NF622TermSpec) : NF607Term :=
  ⟨t.coeff,t.degree,t.key.value⟩

theorem NF622TermSpec.coeffRect_sound (t : NF622TermSpec) (Q : ℕ) (hQ : 0<Q) :
    (t.coeffRect Q).Contains t.coeff := by
  constructor
  · simpa [NF622TermSpec.coeffRect,NF622TermSpec.coeff,Complex.add_re,Complex.mul_re]
      using NF591Ball.contains_exactQ t.coeffRe Q hQ
  · simpa [NF622TermSpec.coeffRect,NF622TermSpec.coeff,Complex.add_im,Complex.mul_im]
      using NF591Ball.contains_exactQ t.coeffIm Q hQ

abbrev NF622Moments := NF616Frequency → ℕ → NF591Rect

def neutralNF622PairRect (M : NF622Moments) (Q : ℕ)
    (a b : NF622TermSpec) : NF591Rect :=
  ((a.coeffRect Q).mulQ (b.coeffRect Q) Q).mulQ
    (M (a.key.add b.key) (a.degree+b.degree)) Q

theorem neutralNF622PairRect_sound (M : NF622Moments) (Q : ℕ) (hQ : 0<Q)
    (a b : NF622TermSpec)
    (hM : (M (a.key.add b.key) (a.degree+b.degree)).Contains
      (neutralNF620J (a.key.add b.key).value (a.degree+b.degree))) :
    (neutralNF622PairRect M Q a b).Contains (neutralNF607Pair a.term b.term) := by
  have hc := NF591Rect.contains_mulQ
    (a.coeffRect_sound Q hQ) (b.coeffRect_sound Q hQ) Q hQ
  have h := NF591Rect.contains_mulQ hc hM Q hQ
  rw [NF616Frequency.add_value] at h
  exact h

def neutralNF622BlockRect (M : NF622Moments) (Q : ℕ)
    (a b : Bool → NF622TermSpec) : NF591Rect :=
  (((neutralNF622PairRect M Q (a true) (b true)).add
     (neutralNF622PairRect M Q (a true) (b false))).add
     (neutralNF622PairRect M Q (a false) (b true))).add
     (neutralNF622PairRect M Q (a false) (b false))

def neutralNF622Block (a b : Bool → NF607Term) : ℂ :=
  neutralNF607Pair (a true) (b true)+neutralNF607Pair (a true) (b false)+
  neutralNF607Pair (a false) (b true)+neutralNF607Pair (a false) (b false)

theorem neutralNF622BlockRect_sound (M : NF622Moments) (Q : ℕ) (hQ : 0<Q)
    (a b : Bool → NF622TermSpec)
    (hM : ∀ s t, (M ((a s).key.add (b t).key) ((a s).degree+(b t).degree)).Contains
      (neutralNF620J ((a s).key.add (b t).key).value ((a s).degree+(b t).degree))) :
    (neutralNF622BlockRect M Q a b).Contains
      (neutralNF622Block (fun s => (a s).term) (fun t => (b t).term)) :=
  NF591Rect.contains_add
    (NF591Rect.contains_add
      (NF591Rect.contains_add
        (neutralNF622PairRect_sound M Q hQ _ _ (hM true true))
        (neutralNF622PairRect_sound M Q hQ _ _ (hM true false)))
      (neutralNF622PairRect_sound M Q hQ _ _ (hM false true)))
    (neutralNF622PairRect_sound M Q hQ _ _ (hM false false))

theorem neutralNF622BallSum_sound {ι : Type*} (s : Finset ι)
    (a : ι → NF591Ball) (x : ι → ℝ)
    (h : ∀ j ∈ s, (a j).Contains (x j)) :
    (neutralNF592BallSum s a).Contains (∑ j ∈ s,x j) := by
  unfold neutralNF592BallSum NF591Ball.Contains
  push_cast
  rw [← Finset.sum_sub_distrib]
  exact (abs_sum_le_sum_abs _ _).trans (Finset.sum_le_sum fun j hj => h j hj)

def neutralNF622RectSum {ι : Type*} (s : Finset ι) (a : ι → NF591Rect) : NF591Rect :=
  ⟨neutralNF592BallSum s (fun j => (a j).re),
   neutralNF592BallSum s (fun j => (a j).im)⟩

theorem neutralNF622RectSum_sound {ι : Type*} (s : Finset ι)
    (a : ι → NF591Rect) (z : ι → ℂ)
    (h : ∀ j ∈ s, (a j).Contains (z j)) :
    (neutralNF622RectSum s a).Contains (∑ j ∈ s,z j) := by
  constructor
  · simpa only [neutralNF622RectSum,Complex.re_sum] using
      neutralNF622BallSum_sound s (fun j => (a j).re) (fun j => (z j).re)
        (fun j hj => (h j hj).1)
  · simpa only [neutralNF622RectSum,Complex.im_sum] using
      neutralNF622BallSum_sound s (fun j => (a j).im) (fun j => (z j).im)
        (fun j hj => (h j hj).2)

theorem neutralNF622H_of_specs (M : NF622Moments) (Q : ℕ) (hQ : 0<Q)
    (i j : Fin 242) (a b : Bool → NF622TermSpec)
    (ha : ∀ s, (a s).term = neutralNF607SelectedTerm i s)
    (hb : ∀ t, (b t).term = neutralNF607SelectedTerm j t)
    (hM : ∀ s t, (M ((a s).key.add (b t).key) ((a s).degree+(b t).degree)).Contains
      (neutralNF620J ((a s).key.add (b t).key).value ((a s).degree+(b t).degree))) :
    (neutralNF622BlockRect M Q a b).re.Contains (neutralNF606PhysicalH i j) := by
  have h := neutralNF622BlockRect_sound M Q hQ a b hM
  simp only [neutralNF622Block,ha,hb] at h
  change (neutralNF622BlockRect M Q a b).Contains (neutralNF607SelectedH i j) at h
  rw [neutralNF607SelectedH_eq] at h
  exact h.1

theorem neutralNF622V_of_specs (M : NF622Moments) (Q : ℕ) (hQ : 0<Q)
    (i : Fin 242) (j : Fin 4) (a : Bool → NF622TermSpec)
    (b : Fin 33 → Bool → NF622TermSpec)
    (ha : ∀ s, (a s).term = neutralNF607SelectedTerm i s)
    (hb : ∀ k t, (b k t).term = neutralNF607CriticalTerm j k t)
    (hM : ∀ k s t, (M ((a s).key.add (b k t).key) ((a s).degree+(b k t).degree)).Contains
      (neutralNF620J ((a s).key.add (b k t).key).value ((a s).degree+(b k t).degree))) :
    (neutralNF622RectSum Finset.univ (fun k => neutralNF622BlockRect M Q a (b k))).re.Contains
      (neutralNF606PhysicalV i j) := by
  have h (k : Fin 33) : (neutralNF622BlockRect M Q a (b k)).Contains
      (neutralNF607MixedBlock i j k) := by
    have hs := neutralNF622BlockRect_sound M Q hQ a (b k) (hM k)
    simpa only [neutralNF622Block,ha,hb,neutralNF607MixedBlock] using hs
  have hs := neutralNF622RectSum_sound Finset.univ _ _ (fun k _ => h k)
  change (neutralNF622RectSum Finset.univ (fun k => neutralNF622BlockRect M Q a (b k))).Contains
    (neutralNF607MixedV i j) at hs
  rw [neutralNF607MixedV_eq] at hs
  exact hs.1

end
end WeilDefect
