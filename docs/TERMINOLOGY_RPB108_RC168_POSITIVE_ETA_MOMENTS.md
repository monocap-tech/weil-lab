# RC168 terminology additions

Historical vectors, action trials, and certificates remain unchanged.

**Positive eta tail moment.** For even n>=16384, eta_n=(2n+1)/(n(n+1)D_n), D_n=s+H_n, and x_n=16384*16385/[n(n+1)]. Define M_k=sum_n 2a(2n+1)/(n^2(n+1)^2 D_n) x_n^k. These are moments of the actual positive D-energy measure of the common eta feature, not sampled approximations to the endpoint operator.

**Paid moment block.** Directed arithmetic encloses all even degrees 16384..65534. The complete remaining eta energy is bounded analytically by a/[D_65534_lower*65533*65534]. Its kth moment is at most this energy times [16384*16385/(65536*65537)]^k. The finite block supplies a positive lower bound for every full moment.

**Same-degree product combination.** Multiply two signed eta polynomials and sum every coefficient with the same monomial degree before applying the corresponding moment interval. A negative coefficient uses the upper moment for the lower pairing bound, and vice versa. This retains cancellations between terms that share one positive moment.

**Fixed-weight prefix recovery.** The interval-to-Loewner map is linear in its lower and upper entry matrices when its weights are fixed. RC168 subtracts the exact analytic tail interval that was used in RC167's construction, leaving a valid finite-prefix enclosure with its outward rounding margins intact. This is not permission to subtract an arbitrary upper bound from another upper bound.

**Paid reference half-Gram gate.** The reference inverse enclosure passes when (1/2)G_lower-(U-L) is PSD on the full seven-source space. This component certificate does not by itself close Stage I's separately required tolerance or original Weil/augmented source transport.
