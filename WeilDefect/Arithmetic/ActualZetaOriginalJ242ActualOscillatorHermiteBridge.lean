import WeilDefect.Arithmetic.ActualZetaOriginalJ242HermiteSignedOscillatorSum
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualOscillatorOddDerivatives
import WeilDefect.Arithmetic.ActualZetaOriginalJ242MonomialTrigOddJets
import WeilDefect.Arithmetic.ActualZetaOriginalJ242ActualPoleOddDerivatives
import Mathlib.Tactic

namespace WeilDefect
noncomputable section
open Polynomial

/-!
NF566 — connect the exact signed finite 242-term frequency
Hermite derivative sums to the *actual* unchanged original
NF545 oscillator analytic functions.

Two parity branches represent the authentic source families:
  k=2r: x^(2r) sin(freq*x)
  k=2r+1: x^(2r+1) cos(freq*x).
The descending factorial convention includes k>2n+1
without separate division-by-zero cases. Each theorem is
a genuine iteratedDeriv of the true source function.

The source-indexed theorem is the crucial missing analytic
bridge. Its correctness must be judged by pinned Lean CI,
not inferred from earlier SHA symbolic source audits.
-/

/-- The authentic even-order sine oscillator analytic odd jet
equals the exact signed descending-factorial source coefficient,
including derivative orders below its monomial degree. -/
theorem neutralNF566EvenOriginalOscillator_analyticSignedJet
    (freq : ℝ) (n r : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r) * Real.sin (freq * x))) 0 =
        neutralNF566OriginalSignedOscillatorJetCoefficient n (2 * r) freq := by
  by_cases hr : r ≤ n
  · rw [neutralNF562EvenMonomialSine_originalOddJet freq n r hr]
    unfold neutralNF566OriginalSignedOscillatorJetCoefficient
    rw [neutralNF566OriginalDescendingFactorial_choose]
    have hdiv : (2 * r) / 2 = r := by omega
    have hsub : 2 * n + 1 - 2 * r = 2 * (n - r) + 1 := by omega
    rw [hdiv, hsub]
    have hsign : (-1 : ℝ) ^ (n - r) = (-1 : ℝ) ^ (n + r) := by
      have hnat : n + r = (n - r) + 2 * r := by omega
      rw [hnat, pow_add]
      norm_num [← pow_mul]
    rw [hsign]
    ring
  · have hlt : n < r := by omega
    rw [neutralNF562EvenMonomialSine_originalOddJet_below freq n r hlt,
      neutralNF566OriginalSignedOscillatorJetCoefficient_highOrder_zero
        n (2 * r) freq (by omega)]

/-- The authentic odd-order cosine oscillator analytic odd jet
equals the exact signed descending-factorial source coefficient,
including derivative orders below its monomial degree. -/
theorem neutralNF566OddOriginalOscillator_analyticSignedJet
    (freq : ℝ) (n r : ℕ) :
    (iteratedDeriv (2 * n + 1)
      (fun x : ℝ => x ^ (2 * r + 1) * Real.cos (freq * x))) 0 =
        neutralNF566OriginalSignedOscillatorJetCoefficient n (2 * r + 1) freq := by
  by_cases hr : r ≤ n
  · rw [neutralNF562OddMonomialCosine_originalOddJet freq n r hr]
    unfold neutralNF566OriginalSignedOscillatorJetCoefficient
    rw [neutralNF566OriginalDescendingFactorial_choose]
    have hdiv : (2 * r + 1) / 2 = r := by omega
    have hsub : 2 * n + 1 - (2 * r + 1) = 2 * (n - r) := by omega
    rw [hdiv, hsub]
    have hsign : (-1 : ℝ) ^ (n - r) = (-1 : ℝ) ^ (n + r) := by
      have hnat : n + r = (n - r) + 2 * r := by omega
      rw [hnat, pow_add]
      norm_num [← pow_mul]
    rw [hsign]
    ring
  · have hlt : n < r := by omega
    rw [neutralNF562OddMonomialCosine_originalOddJet_below freq n r hlt,
      neutralNF566OriginalSignedOscillatorJetCoefficient_highOrder_zero
        n (2 * r + 1) freq (by omega)]

/-- For EACH of the exact 241 frozen NF407 original oscillator
columns and each of the 242 odd initial jet rows, prove the
literal source analytic higher derivative equals its certified
signed factorial coefficient. The original rational f_i, k_i
and parity are not altered or resampled. -/
theorem neutralNF566OriginalEachOscillator_analyticSignedJet
    (i : Fin 241) (n : Fin 242) :
    (iteratedDeriv (2 * n.val + 1)
      (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0 =
      neutralNF566OriginalSignedOscillatorJetCoefficient
        n.val (neutralNF562OriginalOscillatorOrder i)
          (neutralNF562OriginalOscillatorOmega i) := by
  set k : ℕ := neutralNF562OriginalOscillatorOrder i
  set freq : ℝ := neutralNF562OriginalOscillatorOmega i
  rw [neutralNF562OriginalOscillator_exactSource i]
  change (iteratedDeriv (2 * n.val + 1)
    (fun x : ℝ => x ^ k *
      (if Even k then Real.sin (freq * x) else Real.cos (freq * x)))) 0 =
    neutralNF566OriginalSignedOscillatorJetCoefficient n.val k freq
  by_cases he : Even k
  · have hmod : k % 2 = 0 := Nat.even_iff.mp he
    have hk : k = 2 * (k / 2) := by omega
    simp only [if_pos he]
    simpa only [hk] using
      (neutralNF566EvenOriginalOscillator_analyticSignedJet
        freq n.val (k / 2))
  · have hmod : k % 2 = 1 := by
      have hne : k % 2 ≠ 0 := by
        intro hz
        exact he (Nat.even_iff.mpr hz)
      omega
    have hk : k = 2 * (k / 2) + 1 := by omega
    simp only [if_neg he]
    simpa only [hk] using
      (neutralNF566OddOriginalOscillator_analyticSignedJet
        freq n.val (k / 2))

/-- THE exact original oscillator analytic odd-jet LEFT-KERNEL
equation is the corresponding formal frequency Hermite derivative
of F_a at the TRUE unchanged real omega_i=2πf_i, up to the
invertible parity sign (-1)^(k_i/2). All 241 original columns,
all their monomial orders and all 242 odd derivative rows. -/
theorem neutralNF566OriginalEachOscillator_dualHermiteDerivative
    (a : Fin 242 → ℝ) (i : Fin 241) :
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) =
      (-1 : ℝ) ^ (neutralNF562OriginalOscillatorOrder i / 2) *
        ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
          (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
            (neutralNF562OriginalOscillatorOmega i) := by
  calc
    (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) =
      ∑ n : Fin 242, a n *
        neutralNF566OriginalSignedOscillatorJetCoefficient n.val
          (neutralNF562OriginalOscillatorOrder i)
          (neutralNF562OriginalOscillatorOmega i) := by
      apply Finset.sum_congr rfl
      intro n hn
      rw [neutralNF566OriginalEachOscillator_analyticSignedJet i n]
    _ = _ := neutralNF566OriginalSignedOddJets_eq_HermiteDerivative a
      (neutralNF562OriginalOscillatorOmega i)
      (neutralNF562OriginalOscillatorOrder i)

/-- A literal original 242×242 analytic odd-jet column
left-kernel equation forces the corresponding order-k
frequency Hermite derivative to vanish at the TRUE source node.
The global block index/multiplicity aggregation remains OPEN. -/
theorem neutralNF566OriginalEachOscillator_kernelForcesHermiteZero
    (a : Fin 242 → ℝ) (i : Fin 241)
    (hkernel : (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0) :
    ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
      (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
        (neutralNF562OriginalOscillatorOmega i) = 0 := by
  rw [neutralNF566OriginalEachOscillator_dualHermiteDerivative] at hkernel
  have hsign :
      (-1 : ℝ) ^ (neutralNF562OriginalOscillatorOrder i / 2) ≠ 0 :=
    pow_ne_zero _ (by norm_num)
  exact (mul_eq_zero.mp hkernel).resolve_left hsign

/-- The literal full 242×242 ORIGINAL analytic odd-jet matrix
left kernel forces ALL 241 original oscillator frequency-side
formal Hermite derivative zero conditions AND the genuine
negative sinh-pole dual root p_a(-1/4)=0.

This is the direct original-source-specific 242-column analytic
to dual-polynomial reduction. It does not yet prove that the
frequencies' source monomial-order blocks combine to root
multiplicities, or that the simultaneous 68-node polynomial
root budget forces a=0. No replacement columns or Gram inverse
hypotheses occur here. -/
theorem neutralNF566OriginalFullActualOddJetKernel_rootObligations
    (a : Fin 242 → ℝ)
    (hker : ∀ j : Fin 242,
      (∑ n : Fin 242,
        a n * neutralNF560ActualOriginalOddJetMatrix n j) = 0) :
    (∀ i : Fin 241,
      ((Polynomial.derivative^[neutralNF562OriginalOscillatorOrder i])
        (neutralNF565OriginalFrequencyHermitePolynomial a)).eval
          (neutralNF562OriginalOscillatorOmega i) = 0) ∧
      (neutralNF557OriginalDualPolynomial a).eval (-(1 / 4 : ℝ)) = 0 := by
  constructor
  · intro i
    apply neutralNF566OriginalEachOscillator_kernelForcesHermiteZero a i
    have hc := hker ⟨i.val, by omega⟩
    change (∑ n : Fin 242, a n *
      (iteratedDeriv (2 * n.val + 1)
        (nf545OriginalSelectedRealGenerator ⟨i.val, by omega⟩)) 0) = 0 at hc
    exact hc
  · exact neutralNF560OriginalMatrixPoleKernelForcesRoot
      a (hker ⟨241, by omega⟩)

end
end WeilDefect
