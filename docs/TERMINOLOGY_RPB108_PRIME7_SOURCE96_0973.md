# RPB108: eleven-panel actual source at 973/1000

Additive definitions, 2026-10-07 UTC.

- The source surrogate is the smooth/piecewise polynomial part of the actual native source on 96 physical Legendre coordinates. The universal endpoint-log part remains exact and is added when constructing the residual Gram.
- Eleven source panels retain all supported translations 2,3,4,5,7. The coefficient at prime power 4 is log(2)/2; prime 7 has amplitude log(7)/sqrt(7). Every new edge-panel term and its interval radius is retained.
- Source orders are exponential 90, Bernoulli pairs 102 and gamma 50, with 400-digit outward arithmetic and 40-digit coefficient quantization. The two extra Bernoulli pairs repair the changed target's truncation budget.
- eta is the upper bound on the complete normalized source-map error, including analytic truncation, interval coefficients and quantization, aggregated over all 96 source columns. It does not certify the Gram or Schur sign.
- A repeat of aggregation or archive decoding is distinct from a second complete source construction. Whole-domain positivity remains certified through 97/100 while the new matched Gram and corrected sign are pending.
