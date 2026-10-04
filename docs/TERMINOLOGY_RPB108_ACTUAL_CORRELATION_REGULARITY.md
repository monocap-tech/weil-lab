# RPB108 inverse correlation regularity terminology

Defined with first load-bearing use in the companion proof note.

- **Physical Fourier coordinate** F_a(v) is the existing L² Fourier transform of G_a(v), using Mathlib's negative-exponent 2π normalization.
- **Mixed Fourier product** S_a(v,w)(ξ) := conj(F_a(v)(ξ)) F_a(w)(ξ), defined by neutralActualZetaGreenCorrelationSpectrum. This definition alone does not identify it with the Fourier transform of the previously defined compact correlation.
- **Absolute moment of order n** is the integrability of ξ ↦ ‖ξ‖^n ‖S_a(v,w)(ξ)‖. Orders 0, 1, 2 are the hypotheses used by Mathlib's C² Fourier regularity theorem.
- **Derived frequency factor** ξ F_a(v)(ξ) has L² membership already proved from the constructed gradient and actual-divisor summability. It is not retained WD-T38 spectral/operator-domain membership.
- **Inverse spectral integral** J_a(v,w) := FourierInv(S_a(v,w)), defined by neutralActualZetaGreenCorrelationInverse as an actual function ℝ → ℂ.
- **C² inverse regularity** means ContDiff ℝ 2 J_a(v,w), on the full real line. This does not by itself prove compact support or equality with K_a(G_a(v),G_a(w)).
- **Remaining representative identity** is the proof that this inverse integral agrees almost everywhere, or pointwise where lawful, with the exact compact mixed correlation. This must be derived before transporting the previously certified all-complex samples, poles, and zero sum.
