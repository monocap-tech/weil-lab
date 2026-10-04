# RPB108 Fourier agreement terminology

Defined with first load-bearing use in the companion proof note.

- **Ordinary Fourier integral** is Mathlib's function transform of an actual ℝ → ℂ representative, with exponent -2π i x ξ.
- **L² Fourier coordinate** is the existing linear isometry transform on RealComplexL2. Its pointwise representative is defined only up to almost-everywhere equality.
- **L¹/L² Fourier agreement** means these two transforms of an integrable L² function agree almost everywhere. The proof uses distributional Fourier agreement, integral duality, and uniqueness from compact smooth test pairings.
- **Normalized raw parameter** is z=-2πξ, so the project's positive-exponent raw transform H(k,z) equals the ordinary Fourier integral at ξ.
- **Window Fourier dictionary** identifies the ordinary transform of W_a(f) with E_a(-2πξ,f), for the same exact indicator representative.
- **Correlation spectrum attachment** identifies the ordinary Fourier transform of K_a(G_a(v),G_a(w)) almost everywhere with the already defined mixed product S_a(v,w). It retains conjugation of the first slot.
- **Inverse identification boundary** is the remaining proof that J_a(v,w)=FourierInv(S_a(v,w)) agrees almost everywhere with K_a(G_a(v),G_a(w)). Fourier agreement and integrability alone are not stated as this identity.
