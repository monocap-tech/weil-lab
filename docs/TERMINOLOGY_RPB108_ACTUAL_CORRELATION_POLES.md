# RPB108 correlation pole terminology

Defined before load-bearing use in the companion proof note.

- **Window evaluation** E_a(z,f) is the integral of f(x) exp(i z x) over [-a,a], in the existing positive-exponent convention.
- **Source window moment** M_a(s,f) is the existing integral of f(x) exp(s x) over [-a,a].
- **Mixed correlation** K_a(f,g)(t) is the full-line integral of W_a(g)(s) conj(W_a(f)(s-t)); W_a is the exact window indicator representative. The first input is conjugated.
- **Raw transform** H(k,z) is the full-line integral of k(t) exp(i z t).
- **Pole samples** use z=i/2 and z=-i/2, written in Lean as I times the real scalars ±1/2. These are the two pole terms in the external explicit-formula convention; no external theorem is imported here.
- **Cross-pole operator** is the existing neutralLogPoleOperator on the complete logarithmic Hilbert carrier. Its mixed form is conj(M_a(-1/2,f)) M_a(1/2,g) + conj(M_a(1/2,f)) M_a(-1/2,g).
- **Exact constructed canonical image** is neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v). Its physical reconstruction equals G_a(v) exactly, by the previously certified theorem. This name does not identify the retained WD-T38 mode.
