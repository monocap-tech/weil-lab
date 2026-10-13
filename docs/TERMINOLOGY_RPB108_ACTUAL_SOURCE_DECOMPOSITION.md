# RPB108 actual source decomposition terminology

Definitions precede load-bearing use. The earlier [partner registry](TERMINOLOGY_RPB108_ACTUAL_WEIL_ZERO_FORM.md) supplies the actual divisor coordinate q, its multiplicity-preserving pair p(q), raw evaluation E_a, physical Green synthesis G_a(v), and partner zero-side form Z_a(v,w).

| Term | Exact meaning | Certified scope |
| --- | --- | --- |
| L_a(v) | neutralCanonicalToLogHilbert (neutralActualZetaGreenCanonical a ha v) | Its physical realization is exactly G_a(v), with a > 0 |
| P_q(v) | inner complex (neutralLogPositivePairSource a gamma(q)) L_a(v) | (sqrt 2)⁻¹ (E_a(conj gamma(q),G_a(v)) + E_a(gamma(q),G_a(v))) |
| N_q(v) | inner complex (neutralLogNegativePairSource a gamma(q)) L_a(v) | (sqrt 2)⁻¹ (E_a(conj gamma(q),G_a(v)) - E_a(gamma(q),G_a(v))) |
| Positive source form | neutralActualZetaGreenPositiveForm a ha v w = tsum_q conj(P_q(v)) P_q(w) | Absolutely convergent on the constructed carrier |
| Negative source form | neutralActualZetaGreenNegativeForm a ha v w = tsum_q conj(N_q(v)) N_q(w) | Absolutely convergent on the same constructed carrier |
| Source decomposition | 2 Z_a(v,w) = positive source form - negative source form | Full divisor sums count both partner members; no orbit representative selection |
| Source energy identity | 2 Re Z_a(v,v) = tsum_q norm(P_q(v))² - tsum_q norm(N_q(v))² | Both real energies are summable; the difference need not be positive |

The two source forms sum every actual analytic multiplicity copy. Multiplicity is already included; no extra multiplicity factor is inserted. The factor 2 follows from partner reindexing, including partner-fixed points. This diagonalization is not the arithmetic explicit formula or the retained WD-T38 null identity.

WD-T38 source/null attachment, central cancellation, background completion and F-4 remain open. Retained-mode spectral L²/operator-domain membership is unproved and unassumed. SOURCE stays off the critical path; threshold stays closed; earlier residue is preserved; RH remains open.
