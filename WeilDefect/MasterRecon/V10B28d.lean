import WeilDefect.MasterRecon.V10B28c
import WeilDefect.MasterRecon.V10B23c

/-! V10B28d: receiving pairing with the literal carrier operator,
and two-sided regular convolution error. No matrix entries or
external digamma-series supply are assumed certified. -/
namespace WeilDefect.MasterRecon.V10B28d

open MeasureTheory Set Complex
open scoped InnerProduct ComplexConjugate
open V08I (logCarrier physicalInclusion FullL2)
open V10B28a (model reflect regular)
open V10B28c (trial)
open V10B21c (actionTerm)
open V10B23b (SeriesSupply archAction)

theorem arch_pairing_model (t : ℝ) (p : ℝ → ℂ) (hp : Measurable p)
    (hd : Measurable V10B8e.residual) (C : ℝ)
    (hC : ∀ u, |V10B8e.residual u| ≤ C) (g k : logCarrier t)
    (hf : (physicalInclusion t g : ℝ → ℂ) =ᵐ[volume] trial t p)
    (hD : IntegrableOn (actionTerm (physicalInclusion t g)) (Ioi 0))
    (hS : SeriesSupply)
    (K : ℝ → ℂ) (hK : StronglyMeasurable K)
    (hKa : (physicalInclusion t k : ℝ → ℂ) =ᵐ[volume] K)
    (hsupp : ∀ᵐ x ∂volume, x+t ∉ Ioo 0 (2*t) → K x = 0)
    (hm : ∀ x ∈ Ioo 0 (2*t),
      (∫ r in Ioi (0:ℝ), V10B24b.physicalTerm (2*t) p x r) = model (2*t) p x) :
    inner ℂ (V10B8e.archOperator t hd C hC g) k =
      conj (∫ x, conj (K x)*model (2*t) p (x+t)) -
        ((Real.log Real.pi+Real.eulerMascheroniConstant:ℝ):ℂ)*
          inner ℂ (physicalInclusion t g) (physicalInclusion t k) := by
  rw [V10B23c.carrier_arch_pairing t hd C hC g k hD hS]
  have h := V10B28c.restricted_pairing t p hp
    (physicalInclusion t g) (physicalInclusion t k) hf hD K hK hKa hsupp hm
  unfold archAction
  rw [inner_sub_left]
  have he : inner ℂ (V10B22b.integratedAction (physicalInclusion t g)) (physicalInclusion t k) =
      conj (inner ℂ (physicalInclusion t k) (V10B22b.integratedAction (physicalInclusion t g))) :=
    (inner_conj_symm _ _).symm
  rw [he,h]
  change _ - inner ℂ (((Real.log Real.pi+Real.eulerMascheroniConstant:ℝ):ℂ) • physicalInclusion t g) (physicalInclusion t k) = _
  rw [inner_smul_left,Complex.conj_ofReal]

noncomputable def approximateRegular (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  ∫ r in Ioc (0:ℝ) x, (V10B27a.q r:ℂ)*p (x-r)

theorem one_side_error (p : ℝ → ℂ) (x B : ℝ) (hx : 0 ≤ x) (hxL : x ≤ 1/2)
    (hB : 0 ≤ B) (hp : ∀ r ∈ Ioc 0 x, ‖p (x-r)‖ ≤ B)
    (ha : IntegrableOn (fun r => (V10B24b.h r:ℂ)*p (x-r)) (Ioc 0 x))
    (hq : IntegrableOn (fun r => (V10B27a.q r:ℂ)*p (x-r)) (Ioc 0 x)) :
    ‖regular p x-approximateRegular p x‖ ≤ x*(1/(2:ℝ)^28)*B := by
  unfold regular approximateRegular
  rw [← integral_sub ha hq]
  have he : (fun r => (V10B24b.h r:ℂ)*p (x-r)-(V10B27a.q r:ℂ)*p (x-r)) =
      fun r => ((V10B24b.h r-V10B27a.q r:ℝ):ℂ)*p (x-r) := by
    funext r
    push_cast
    ring
  rw [he]
  exact V10B27b.frozen_convolution_error x B hx hxL hB p hp (by simpa only [← he] using ha.sub hq)

noncomputable def approximateModel (L : ℝ) (p : ℝ → ℂ) (x : ℝ) : ℂ :=
  model L p x+regular p x+regular (reflect L p) (L-x)-
    approximateRegular p x-approximateRegular (reflect L p) (L-x)

theorem two_side_error (p : ℝ → ℂ) (x B : ℝ)
    (hx : x ∈ Ioo 0 (1/2:ℝ))
    (h₁ : ‖regular p x-approximateRegular p x‖ ≤ x*(1/(2:ℝ)^28)*B)
    (h₂ : ‖regular (reflect (1/2) p) (1/2-x)-
      approximateRegular (reflect (1/2) p) (1/2-x)‖ ≤ (1/2-x)*(1/(2:ℝ)^28)*B) :
    ‖model (1/2) p x-approximateModel (1/2) p x‖ ≤ B/(2:ℝ)^29 := by
  unfold approximateModel
  have he : model (1/2) p x-(model (1/2) p x+regular p x+
      regular (reflect (1/2) p) (1/2-x)-approximateRegular p x-
      approximateRegular (reflect (1/2) p) (1/2-x)) =
      -((regular p x-approximateRegular p x)+
        (regular (reflect (1/2) p) (1/2-x)-
        approximateRegular (reflect (1/2) p) (1/2-x))) := by ring
  rw [he,norm_neg]
  refine (norm_add_le _ _).trans ((add_le_add h₁ h₂).trans ?_)
  apply le_of_eq
  ring

end WeilDefect.MasterRecon.V10B28d

#print axioms WeilDefect.MasterRecon.V10B28d.arch_pairing_model
#print axioms WeilDefect.MasterRecon.V10B28d.one_side_error
#print axioms WeilDefect.MasterRecon.V10B28d.two_side_error
