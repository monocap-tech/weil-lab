import WeilDefect.Morphology.NeutralFourierCarrier

namespace WeilDefect

noncomputable section

open MeasureTheory
open scoped FourierTransform

/-- The named scalar source identity accepts zero density for any symbol.
This does not identify that density with a physical carrier. -/
theorem wd_t38_zero_density_sourceIdentity (symbol : ℝ → ℝ) (shift : ℝ) :
    0 + shift * spectralMass (fun _ => 0) =
      shiftedCompactWeilForm symbol (fun _ => 0) shift 0 := by
  simp [spectralMass, shiftedCompactWeilForm]

/-- The existing arithmetic output permits zero density and zero scalar Q,
independently of the physical vector or its Fourier density. -/
theorem wd_t38_zero_density_arithmetic
    (c shift lowerC upperC poleC : ℝ) (primeCoeff : ℕ → ℝ) :
    NeutralArithmeticMorphology c 0 shift lowerC upperC poleC
      (fun _ => 0) primeCoeff := by
  have hp := wd_t38_p3_u3_right_limit_prime_support_finite c
  refine {
    densityIntegrable := integrable_zero ℝ ℝ volume
    logEnergyIntegrable := ?_
    rightPrimeSupportFinite := hp.1
    thresholdSubsingleton := hp.2
    logarithmicOrder := ?_
    noPositiveSobolevCoercivity := ?_
    globalCancellationScope := wd_t38_p3_u6_global_cancellation_not_termwise
  }
  · simp only [mul_zero]
    exact integrable_zero ℝ ℝ volume
  · simp [logarithmicFourierEnergy, spectralMass]
  · intro eps heps
    exact wd_t38_p3_u5_finite_prime_translations_no_smoothing heps c primeCoeff

section Reindex

variable
    {Kpos M H Hext EndpointObs RightObs : Type*}
    [NormedAddCommGroup Kpos] [InnerProductSpace ℂ Kpos] [CompleteSpace Kpos]
    [NormedAddCommGroup M] [InnerProductSpace ℂ M] [CompleteSpace M]
    [NormedAddCommGroup H] [InnerProductSpace ℂ H] [CompleteSpace H]
    [NormedAddCommGroup Hext] [NormedSpace ℂ Hext]
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    {A : ℝ → ClosedSubmodule ℂ (WeilDefect.WDT16.CoeffSpace Kpos M)}
    {c : ℝ}
    {aSeq : ℕ → Kpos} {uSeq : ℕ → M}
    {phi : ℕ → ℕ} {aLim : Kpos} {uLim : M}
    {P : Kpos →L[ℂ] H} {C : M →L[ℂ] Kpos} {k : H}
    {Q shift lowerC upperC poleC : ℝ}
    {density : ℝ → ℝ} {primeCoeff : ℕ → ℝ}
    {extend : H →L[ℂ] Hext}

/-- A custody countercheck: every typed WD-T38 output can be reindexed to
zero named density and Q while preserving its actual physical/null data.
This is an audit construction, not a new source realization. -/
def NeutralDefectMorphology.zeroDensityReindex
    (d : NeutralDefectMorphology (EndpointObs := EndpointObs) (RightObs := RightObs) A c aSeq uSeq phi aLim uLim
      P C k Q shift lowerC upperC poleC density primeCoeff extend) :
    NeutralDefectMorphology (EndpointObs := EndpointObs) (RightObs := RightObs) A c aSeq uSeq phi aLim uLim
      P C k 0 shift lowerC upperC poleC (fun _ => 0) primeCoeff extend where
  subsequence_strictMono := d.subsequence_strictMono
  attainedNeutral := d.attainedNeutral
  endpointRight := d.endpointRight
  endpointNonzero := d.endpointNonzero
  selectedCoordinateNonzero := d.selectedCoordinateNonzero
  coefficientCarrier := d.coefficientCarrier
  unitGain := d.unitGain
  physicalAdjoint := d.physicalAdjoint
  physicalNull := d.physicalNull
  arithmetic := wd_t38_zero_density_arithmetic c shift lowerC upperC poleC primeCoeff
  nullExtension := d.nullExtension
  nullExtensionVector := d.nullExtensionVector

/-- Reindexing does not change the endpoint vector, operators or restrictions. -/
theorem NeutralDefectMorphology.zeroDensityReindex_nullExtension
    (d : NeutralDefectMorphology (EndpointObs := EndpointObs) (RightObs := RightObs) A c aSeq uSeq phi aLim uLim
      P C k Q shift lowerC upperC poleC density primeCoeff extend) :
    d.zeroDensityReindex.nullExtension = d.nullExtension := rfl

end Reindex

/-- A nonzero concrete physical carrier cannot have zero Fourier norm-square
density almost everywhere. This uses L2 Fourier injectivity, not form energy
or spectral operator-domain membership. -/
theorem neutralPhysicalFourierDensity_ne_zero
    {c : ℝ} {EndpointObs RightObs : Type*}
    [NormedAddCommGroup EndpointObs] [NormedSpace ℂ EndpointObs]
    [NormedAddCommGroup RightObs] [NormedSpace ℂ RightObs]
    (carrier : NeutralPhysicalFourierCarrier c EndpointObs RightObs) :
    ¬ ((fun ξ : ℝ => ‖(𝓕 carrier.l2Mode : RealComplexL2) ξ‖ ^ 2) =ᵐ[volume]
      (fun _ => (0 : ℝ))) := by
  intro hdensity
  have hfourier : (𝓕 carrier.l2Mode : RealComplexL2) = 0 := by
    apply Lp.ext
    filter_upwards [hdensity, Lp.coeFn_zero ℂ 2 volume] with ξ hξ hzero
    have hv : (𝓕 carrier.l2Mode : RealComplexL2) ξ = 0 := by
      apply norm_eq_zero.mp
      nlinarith [norm_nonneg ((𝓕 carrier.l2Mode : RealComplexL2) ξ)]
    exact hv.trans hzero.symm
  have hmode : carrier.l2Mode = 0 := by
    calc
      carrier.l2Mode = (𝓕⁻ (𝓕 carrier.l2Mode : RealComplexL2) : RealComplexL2) :=
        (FourierTransform.fourierInv_fourier_eq _).symm
      _ = 0 := by rw [hfourier, FourierTransform.fourierInv_zero]
  exact carrier.l2Mode_ne_zero hmode

end

end WeilDefect
