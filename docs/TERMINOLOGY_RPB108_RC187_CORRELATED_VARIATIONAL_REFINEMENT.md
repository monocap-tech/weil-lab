# RC187 terminology: correlated variational refinement

RC186's operator, response family, source Gram, raw trial map, rational trial coefficients, and represented action carriers retain their meanings.

- **U**: the complete trial response map TY, for one of RC186's recorded six-column trial coefficient matrices Y.
- **Rhat**: S-VY, the complete represented response residual; **R**: S-MU, the corresponding actual response residual.
- **E**: a certified simultaneous Gram upper for R-Rhat on every complex response mixture, retained from RC186. It is a squared action-representation error envelope, not an intrinsic error lower bound.
- **Source/trial cross form**: Sym(S*D U). Its correlated enclosure uses the exact identity (G_S+G_U-G_(S-U))/2 and complete source Gram Loewner bounds.
- **Finite trial/residual cross form**: the independently accumulated Hermitian part of U*D Rhat on even Legendre degrees through16382.
- **Matrix Young payment**: for maps A,B with A*D A<=G_A and B*D B<=G_B, the Hermitian cross form satisfies -P<=Sym(A*D B)<=P, where P=t G_A+G_B/(4t), t>0. This is one simultaneous Loewner bound on every complex mixture. It does not assume any error orthogonality.
- **Variational action payment**: matrix Young applied to the full maps U and R-Rhat, using the full trial response Gram upper and E.
- **Variational tail payment**: matrix Young applied to the omitted U and Rhat tails on disjoint output support above16382. Both are complete source/action tails, and their correlated Gram uppers retain the shared eta coefficients.
- **Refined variational enclosure**: the complete source/trial cross form plus the finite trial/residual cross form, minus/plus the two Young payments. It encloses the same exact C=2 Sym(S*D U)-U*D MU used in RC186.

The refinement changes enclosure arithmetic. It does not construct a new action carrier, enlarge response coverage, or change the original Weil or Stage I targets. Width acceptance is reported separately.
