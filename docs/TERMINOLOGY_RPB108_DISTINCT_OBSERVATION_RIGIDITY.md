# Terminology: RPB108 distinct observation rigidity

Additive register; historical wording is unchanged.

| Term | Definition | Scope |
| --- | --- | --- |
| Distinct complex ordinate | z_rho = -i(rho-1/2) at an actual zero point | Injective in rho; real heights alone need not be injective |
| Copy-fiber aggregate | b_rho = sum_j u_(rho,j) | Actual identical-copy packet coefficients add within each point |
| Finite Green kernel | Finite raw families with every b_rho = 0 | Analytic proof via explicit differential source identity and finite independence |
| Weighted point coefficient space | sum_rho abs(b_rho)^2 / m_rho < infinity | Unitary copy-fiber quotient with inherited coefficient norm; analytic proof |
| Infinite distinct-point kernel | ker Gbar on weighted point ell2 | Not excluded by finite independence; actual existence not asserted |
| Distinct-point observation count | N_pt(T), one complex ordinate per point | Different from multiplicity-weighted divisor count; no independent jets supplied |
| Counting-route rigidity input | A sufficient distinct-point lower growth plus the correct entire annihilator and topology | Not established by present upper-bound/summability stack |

Five parameter/source-mode lemmas are Lean certified. The Green kernel and weighted quotient arguments are not yet Lean formalizations.
