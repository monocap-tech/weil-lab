# RPB108 terminology: actual translation-panel order

Introduced with the panel-order audit after the certified 22/25 result. This registry adds a geometry interface; historical aperture definitions remain unchanged.

- **Normalized physical coordinate:** t=(x+a)/(2a), with t in [0,1] and d=2a.
- **Actual prime-power shift:** ell_n=log(n)/d. The current geometry interface covers log(5)<d<log(7), whose active prime powers are exactly 2,3,4,5. Lambda(4)=log(2); Lambda(6)=0.
- **Forward support cutoff:** 1-ell_n. The supported translation p(t+ell_n) is active to its left.
- **Backward support cutoff:** ell_n. The supported translation p(t-ell_n) is active to its right.
- **Certified cut order:** all eight support cutoffs plus 0 and 1, sorted only after exact rational interval enclosures certify strict separation. Unresolved or coincident cutoff intervals reject; no midpoint sort alone proves order.
- **Panel active set:** on the open interval between consecutive true cutoffs, include each forward shift whose cutoff is to the right and each backward shift whose cutoff is to the left. Signs +1 and -1 denote argument shifts, not the sign of the source coefficient.
- **Actual source translation coefficient:** -Lambda(n)/sqrt(n) for each active argument shift. The source endpoint logarithms, smooth core, poles and remainder budgets are separate unchanged terms.
- **Cross-prime panel collision:** d=log(6)=log(2)+log(3), equivalently a=log(6)/2. Here ell_2=1-ell_3 and ell_3=1-ell_2. Passing this boundary reorders two reflected pairs of cutoffs and changes two active sets; the number of open panels remains nine on either strict side.
- **Geometry audit aperture:** a=9/10, d=9/5. It is beyond the collision and below log(7)/2. Geometry certification alone does not certify the complete source, native finite sign, residual Gram or whole-domain positivity at this aperture.

The certified full-domain positivity frontier remains 22/25 until fresh matching native/source/Gram and corrected sign data establish a larger window. Global endpoint exclusion, historical packet attachment and F4 remain open.
