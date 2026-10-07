# RPB108: first prime-7 aperture preflight

Additive definitions, 2026-10-07 UTC. Historical prime-5 definitions and certificates remain unchanged.

- The target aperture is 973/1000. It lies strictly above log(7)/2 and below log(8)/2, so the actual nonzero supported prime-power translations are 2,3,4,5,7. Equality at log(7)/2 has zero overlap and contributes no physical L2 translation.
- The prime-7 interaction is the self-adjoint sum of the two supported log(7) translations with amplitude log(7)/sqrt(7). Its two edge strips are disjoint here. Its physical operator norm equals that amplitude for every strictly positive overlap, even when the strip width is small; no small operator norm follows from small support.
- Eleven-panel source geometry means the actual normalized support cuts at 0,1 and ell_n,1-ell_n for n=2,3,4,5,7, where ell_n=log(n)/(2a). It is distinct from the finer partition used for the weighted prime bound.
- The joint prime bound is a positive weighted Schur majorant verified on every support/source-weight/translated-target cell of the full five-term operator. The numerical weight search supplies candidates; rational inequalities supply the proof.
- A 96-moment complement preflight at 973/1000 certifies only the complement and the degree-95 diagonal truncation budget. It does not certify the new native restriction, source map, residual Gram or corrected Schur sign. Whole-domain positivity remains certified through 97/100 until all those checks pass.
- The new remainder constants are exp(4a)<50 and 4a/(1-exp(-4a))<5a=973/200, proved by log(5)<4a<log(50). The historical exp(4a)<49 guard fails at this target and cannot be reused.
