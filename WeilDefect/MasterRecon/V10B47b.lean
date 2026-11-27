import WeilDefect.MasterRecon.V10B34a
import WeilDefect.MasterRecon.V10B47a
import Mathlib.Algebra.Polynomial.Degree.Operations

/-! V10B47b: polynomial Rodrigues pairing, orthogonality, and
the exact diagonal norm. Completeness is not assumed here. -/
namespace WeilDefect.MasterRecon.V10B47b
open MeasureTheory Set Polynomial
open WeilDefect.MasterRecon.V10B33a
open WeilDefect.MasterRecon.V10B34a
open WeilDefect.MasterRecon.V10B47a

noncomputable def w (x : ℝ) := x*(1-x)

theorem polynomial_pairing (p : ℤ[X]) (j : ℕ) :
    (j.factorial:ℝ)*(∫ x in (0:ℝ)..1, aeval x p*legendre j x) =
      ∫ x in (0:ℝ)..1, aeval x ((Polynomial.derivative^[j]) p)*w x^j := by
  let q : ℤ[X] := Polynomial.X^j*(1-Polynomial.X)^j
  let u : ℕ → ℝ → ℝ := fun k x => aeval x ((Polynomial.derivative^[k]) p)
  let v : ℕ → ℝ → ℝ := fun k x => aeval x ((Polynomial.derivative^[k]) q)
  have hu (k : ℕ) : Continuous (u k) :=
    ((Polynomial.derivative^[k]) p).differentiable_aeval.continuous
  have hv (k : ℕ) : Continuous (v k) :=
    ((Polynomial.derivative^[k]) q).differentiable_aeval.continuous
  have hdu (k : ℕ) (x : ℝ) : HasDerivAt (u k) (u (k+1) x) x := by
    dsimp only [u]
    rw [Function.iterate_succ_apply']
    exact ((Polynomial.derivative^[k]) p).hasDerivAt_aeval x
  have hdv (k : ℕ) (x : ℝ) : HasDerivAt (v k) (v (k+1) x) x := by
    dsimp only [v]
    rw [Function.iterate_succ_apply']
    exact ((Polynomial.derivative^[k]) q).hasDerivAt_aeval x
  have hz (k : ℕ) (hk : k < j) : v k 0=0 ∧ v k 1=0 :=
    rodrigues_endpoints j k hk
  have hp := repeated_parts j u v hu hv hdu hdv hz
  have hfun : (fun x : ℝ => (j.factorial:ℝ)*(aeval x p*legendre j x)) =
      fun x => (-1:ℝ)^j*(u 0 x*v j x) := by
    funext x
    dsimp [u,Function.iterate_zero_apply]
    calc
      _ = aeval x p*((j.factorial:ℝ)*legendre j x) := by ring
      _ = aeval x p*((-1:ℝ)^j*v j x) := by rw [rodrigues_eval]
      _ = _ := by ring
  have hzero : (fun x => u j x*v 0 x) =
      fun x => aeval x ((Polynomial.derivative^[j]) p)*w x^j := by
    funext x
    simp [u,v,q,w,mul_pow]
  have hsign : (-1:ℝ)^j*(-1:ℝ)^j=1 := by rw [← mul_pow]; norm_num
  calc
    _ = ∫ x in (0:ℝ)..1, (j.factorial:ℝ)*(aeval x p*legendre j x) :=
      (intervalIntegral.integral_const_mul _ _).symm
    _ = ∫ x in (0:ℝ)..1, (-1:ℝ)^j*(u 0 x*v j x) :=
      congrArg (fun f : ℝ → ℝ => ∫ x in (0:ℝ)..1, f x) hfun
    _ = (-1:ℝ)^j*(∫ x in (0:ℝ)..1, u 0 x*v j x) :=
      intervalIntegral.integral_const_mul _ _
    _ = _ := by rw [hp,← mul_assoc,hsign,one_mul,hzero]

theorem lower_degree_pairing_zero (p : ℤ[X]) (j : ℕ) (hp : p.natDegree < j) :
    (∫ x in (0:ℝ)..1, aeval x p*legendre j x) = 0 := by
  have h := polynomial_pairing p j
  rw [Polynomial.iterate_derivative_eq_zero hp] at h
  simp only [map_zero,zero_mul,intervalIntegral.integral_zero] at h
  exact (mul_eq_zero.mp h).resolve_left (by exact_mod_cast Nat.factorial_ne_zero j)

theorem legendre_orthogonal_lt (i j : ℕ) (hij : i < j) :
    (∫ x in (0:ℝ)..1, legendre i x*legendre j x) = 0 := by
  have h := lower_degree_pairing_zero (shiftedLegendre i) j (by simpa using hij)
  have he : (fun x : ℝ => legendre i x*legendre j x) =
      fun x => (-1:ℝ)^i*(aeval x (shiftedLegendre i)*legendre j x) := by
    funext x
    unfold legendre
    ring
  rw [he,intervalIntegral.integral_const_mul,h,mul_zero]

theorem legendre_orthogonal (i j : ℕ) (hij : i ≠ j) :
    (∫ x in (0:ℝ)..1, legendre i x*legendre j x) = 0 := by
  rcases lt_or_gt_of_ne hij with h | h
  · exact legendre_orthogonal_lt i j h
  · simpa only [mul_comm] using legendre_orthogonal_lt j i h

theorem top_derivative (j : ℕ) :
    (Polynomial.derivative^[j]) (shiftedLegendre j) =
      C ((j.factorial:ℤ)*(-1:ℤ)^j*((j+j).choose j:ℤ)) := by
  have hd := Polynomial.natDegree_iterate_derivative (shiftedLegendre j) j
  rw [natDegree_shiftedLegendre,Nat.sub_self] at hd
  rw [Polynomial.eq_C_of_natDegree_le_zero hd]
  congr 1
  rw [Polynomial.coeff_iterate_derivative,zero_add,Nat.descFactorial_self,
      Polynomial.coeff_shiftedLegendre,Nat.choose_self]
  simp [nsmul_eq_mul]

theorem legendre_diagonal (j : ℕ) :
    (∫ x in (0:ℝ)..1, legendre j x*legendre j x) = 1/(2*(j:ℝ)+1) := by
  have h := polynomial_pairing (shiftedLegendre j) j
  rw [top_derivative] at h
  have he : (fun x : ℝ => legendre j x*legendre j x) =
      fun x => (-1:ℝ)^j*(aeval x (shiftedLegendre j)*legendre j x) := by
    funext x
    unfold legendre
    ring
  have hf : (j.factorial:ℝ) ≠ 0 := by exact_mod_cast Nat.factorial_ne_zero j
  have hB : (∫ x in (0:ℝ)..1, w x^j) = beta j j := by
    simp [w,beta,mul_pow]
  have hsign : (-1:ℝ)^j*(-1:ℝ)^j=1 := by rw [← mul_pow]; norm_num
  have hR : (fun x : ℝ => aeval x (C ((j.factorial:ℤ)*(-1:ℤ)^j*((j+j).choose j:ℤ)))*w x^j) =
      fun x => ((j.factorial:ℝ)*(-1:ℝ)^j*((j+j).choose j:ℝ))*w x^j := by
    funext x
    simp
  rw [hR,intervalIntegral.integral_const_mul,hB] at h
  have hpair := mul_left_cancel₀ hf (show
      (j.factorial:ℝ)*(∫ x in (0:ℝ)..1, aeval x (shiftedLegendre j)*legendre j x) =
      (j.factorial:ℝ)*((-1:ℝ)^j*((j+j).choose j:ℝ)*beta j j) by
      rw [h]; ring)
  rw [he,intervalIntegral.integral_const_mul,hpair]
  calc
    _ = ((j+j).choose j:ℝ)*beta j j := by rw [← mul_assoc,← mul_assoc,hsign,one_mul]
    _ = _ := by
      have hc := Nat.add_choose_mul_factorial_mul_factorial j j
      have hc' : ((j+j).choose j:ℝ)*(j.factorial:ℝ)*(j.factorial:ℝ) =
          ((j+j).factorial:ℝ) := by exact_mod_cast hc
      rw [beta_closed,Nat.factorial_succ]
      push_cast
      have hp : (0:ℝ)<((j+j).factorial:ℝ) := by exact_mod_cast Nat.factorial_pos (j+j)
      have hj : (0:ℝ)<(j:ℝ)+(j:ℝ)+1 := by positivity
      calc
        _ = (((j+j).choose j:ℝ)*(j.factorial:ℝ)*(j.factorial:ℝ))/
            (((j:ℝ)+(j:ℝ)+1)*((j+j).factorial:ℝ)) := by ring
        _ = _ := by rw [hc']; field_simp [hp.ne',hj.ne']

end WeilDefect.MasterRecon.V10B47b

#print axioms WeilDefect.MasterRecon.V10B47b.polynomial_pairing
#print axioms WeilDefect.MasterRecon.V10B47b.lower_degree_pairing_zero
#print axioms WeilDefect.MasterRecon.V10B47b.legendre_orthogonal_lt
#print axioms WeilDefect.MasterRecon.V10B47b.legendre_orthogonal
#print axioms WeilDefect.MasterRecon.V10B47b.top_derivative
#print axioms WeilDefect.MasterRecon.V10B47b.legendre_diagonal
