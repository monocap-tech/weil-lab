# RC204 terminology — signed marginal action-error envelope

- **Response family:** unchanged RC203 ordered (P0,P2,f0,psi0,w14,v10).
- **Inverse trial family:** unchanged RC203 eight raw directions (P0,P2,f0,psi0,w14,q185,v10,q202); q185 and q202 are auxiliary inverse trials, not new response sources.
- **Column-error envelope:** for true action errors e_i^vec with norm at most epsilon_i and fixed rational trial map Y, the full mixture error is bounded by sum_i epsilon_i |(Yx)_i|.
- **Signed controls:** 128 rank-one outer products z_sigma z_sigma^T, fixing the first sign positive since a simultaneous reversal preserves each product.
- **Gram floor:** downward entrywise 10^-20 rounding of RC203's certified response Gram lower, with six further grid units subtracted from every diagonal. The exact difference is strictly diagonally dominant and PSD; the floor is not a replacement of the actual Gram.
- **Accepted squared-error factor:** 473/200000 = 0.002365 for the same six-source D Gram lower, certified by all 768 positive integer principal minor tests.
- **Rejected preceding grid factor:** 591/250000 = 0.002364 fails this particular conservative signed matrix test (mask 12, sixth minor); not an impossibility theorem about a smaller true error bound.
- **Scope:** error-envelope precision only; no inverse response width or Stage I acceptance is transferred without fresh full-matrix calculation.
