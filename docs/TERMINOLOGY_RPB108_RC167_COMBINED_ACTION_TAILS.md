# RC167 terminology additions

Historical vectors, trials, and certificates remain unchanged.

**Combined inverse action tail.** For each fixed inverse-source coefficient column Y, first sum the four native action contributions and the three separate q_t, q_psi, q_delta contributions as rational coefficients of the common eta tail polynomial. Only then form signed polynomial-product bounds for pairings. This preserves cancellations lost when separate pairing tail intervals are transported through Y afterward.

**Combined nominal residual tail.** The residual approximation is y-s+q(y), with native coefficients W(Y-X)+T4Y[0..3] and separate action coefficients Y4, Y5, Y6. Its entire eta polynomial is summed before bounding its Gram. The true action-error map is still paid separately; combining nominal tails does not assume a favorable mixed-error sign.

**Whole-enclosure selection.** Compare complete valid endpoint or residual matrix enclosures and retain one complete enclosure. Entrywise minima or matrix minima are not asserted to preserve Loewner bounds. The prior inverse enclosure is retained if sharper than every new tested candidate.
