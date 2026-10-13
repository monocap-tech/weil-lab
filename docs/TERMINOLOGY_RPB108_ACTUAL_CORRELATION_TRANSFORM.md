# RPB108 compact correlation transform terminology

Definitions precede load-bearing use. The earlier [partner registry](TERMINOLOGY_RPB108_ACTUAL_WEIL_ZERO_FORM.md) defines the actual divisor, gamma(q), G_a(v), E_a and Z_a.

| Term | Exact meaning | Certified scope |
| --- | --- | --- |
| W_a(f) | neutralWindowRepresentative a f = indicator of [-a,a] times the physical L² representative | Pointwise compact support; equals G_a(v) almost everywhere when f = G_a(v) |
| K_a(f,g)(t) | neutralWindowCorrelation a f g t = integral_s W_a(g)(s) conj(W_a(f)(s-t)) | First argument conjugated; support in [-2a,2a] |
| H(k,z) | neutralRawTransform k z = integral_t k(t) exp(i z t) | Positive exponent, entire complex parameter used in the dictionary |
| Twisted input | W_a(f)(x) exp(i z x) | Integrable for every complex z, by compact-window L² to L¹ and bounded compact exponential weighting |
| Mixed transform dictionary | H(K_a(f,g),z) = conj(E_a(conj z,f)) E_a(z,g) | Every compact-window physical L² pair, including the constructed actual Green pair |
| Actual correlation zero sum | tsum_q H(K_a(G_a(v),G_a(w)),gamma(q)) = Z_a(v,w) | Absolutely convergent for a > 0; includes every actual multiplicity copy |

Compact support and integrability do not establish C² regularity. The external EF_lit theorem requires a compact C² test; that regularity/approximation step remains open. Arithmetic symbol/pole transport, retained WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. SOURCE stays off the critical path; threshold stays closed; residue preserved; RH remains open.
