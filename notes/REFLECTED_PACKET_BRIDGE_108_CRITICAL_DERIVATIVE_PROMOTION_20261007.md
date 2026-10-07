# RPB108: critical source regularity does not yet permit derivative promotion

Date: 2026-10-07 UTC. Recovered live head b78b4813c416ab17197cbfae994247c8a5ed51a8.
Definitions: [critical derivative registry](../docs/TERMINOLOGY_RPB108_CRITICAL_DERIVATIVE_PROMOTION.md).
This is an endpoint-exclusion audit, not a new aperture estimate.

## Exact implication under audit

The preceding actual source theorem identifies the positive height moment of order one with Xcrit. The attempted shortcut is

    full native nullity + Xcrit -> global L2 derivative -> derivative in K_a.

The second arrow is already proved by supported-L2 null-domain promotion. The first arrow is not established. A critical moment bound on the entire kernel would therefore require one further theorem before yielding endpoint exclusion.

## What critical regularity actually gives

For h in Xcrit, g=h' is a compactly supported distribution in Zcrit: multiplying Fourier(h) by 2 pi i xi and the Zcrit weight is bounded by a constant times the base log energy plus the Xcrit energy.

The exact frozen native multiplier, including finite prime translations, commutes with distributional differentiation. Pole moments can be evaluated on compactly supported distributions by pairing with exponentials and a smooth cutoff equal to one near the support. The distributional integration-by-parts signs remain

    M_-(g)=M_-(h)/2,   M_+(g)=-M_+(h)/2.

Thus if h is full-native null, the differentiated equation is lawfully

    m_a(D)g+p_g=0 on (-a,a),

and g is supported in [-a,a]. No physical dilation or enlarged null equation is used.

This does NOT place g in the canonical form kernel: g is not yet known to be L2, so the full form and the finite-dimensional kernel operator cannot be applied to it. Finite dimension of K_a does not establish finite dimension or equality of a larger distributional solution space.

No nonzero distribution supported on finitely many endpoints belongs to Zcrit. Its Fourier transform is a finite sum of polynomial times phases; even a delta has a divergent integral log(e+|xi|)/(1+|xi|). For combinations, frequency averaging leaves a nonzero diagonal leading term, while distinct-phase cross terms have lower integrated growth. This fact alone does not repeat the L2 promotion proof. That proof first constructs a globally L2 exterior candidate using the Carleman bound on an L2 input. Such a candidate for g has not been constructed; excluding a point-supported defect does not supply its exterior L2 norm.

## Compactly supported physical control

Choose a smooth cutoff chi supported in (-1,1), equal to one on [-1/4,1/4], and set

    h(x)=x^(1/4) chi(x) for x>0, and h(x)=0 for x<=0.

For 0<t<1/8, split the translated difference into an edge region of length O(t), the region x>=t near zero, and the smooth cutoff region. On the edge, squared amplitude is O(t^(1/2)); in the interior, the mean-value bound gives

    ||tau_t h-h||_2^2 <= C [t^(3/2)+t^2 integral_t^(1/4) x^(-3/2) dx+t^2]
                       <= C' t^(3/2).

The usual Fourier/Tonelli difference formula therefore gives h in global H^beta for every beta<3/4. In particular h is in H^(5/8). Since |xi| log(e+|xi|) is bounded by C(1+|xi|)^(5/4), this same physical function lies in Xcrit and D_a for any support window containing [0,1].

Nevertheless on (epsilon,1/4),

    integral |h'|^2 dx = (epsilon^(-1/2)-2)/8 -> infinity.

There is no endpoint delta in this derivative; the control is continuous and vanishes at zero. Even the logarithmically weighted boundary budget integral_0^(1/4) |h(x)|^2 log(e/x)/x dx is finite. Neither that boundary budget, critical fractional regularity nor exclusion of endpoint deltas yields an L2 derivative.

This refutes Xcrit -> H1 for supported physical functions. It does NOT refute promotion for actual zero-null vectors; the control is not assigned any actual null equation or arithmetic source neutrality.

## Why the existing null bootstrap cannot simply cross the threshold

The audited fractional-null proof uses weighted support projection and commutator budgets U_s=4+4/(1/2-s)^2 and a cutoff-pole Fourier tail budget proportional to 1/(1-2s). They apply only for s<1/2. The critical premise concerns h, not a separately smooth cutoff pole or a bounded support projection on an unrestricted critical space. A jump function still fails the critical norm.

One would need a joint estimate on the actual combined equation, retaining cancellation between its terms. Replacing their separately divergent norms by the finite norm of h is an unjustified implication. No arithmetic cancellation theorem at s=1/2 is proved here, and no limit of the subcritical constants is taken.

## Smallest remaining theorem and closure path

Category: endpoint exclusion. The additional gate is precisely

    h in actual K_a intersect Xcrit -> h' in global L2.

After this gate, supported-L2 promotion automatically gives h' in D_a and K_a. If the entire hypothetical contact kernel has finite order-one positive source moment AND the gate holds on that kernel, differentiation becomes an endomorphism of K_a: each resulting derivative is again in K_a, hence has the assumed critical moment, so promotion iterates. Fourier-polynomial independence then contradicts finite dimension unless K_a=0.

For one critically regular vector alone, the two gates do not establish regularity of every later derivative or eliminate a higher-dimensional kernel. The whole-kernel quantifier is essential.

The alternative single order-two source trace theorem from the prior pass remains sufficient without this additional critical gate. Neither order-one finiteness nor critical promotion has been supplied by actual arithmetic. This pass rules out the regularity-only shortcut and isolates what must use the exact zero interior equation.

## Custody and standing

Read at the recovered head:
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006: actual source/Fourier equivalence and critical moment.
- FRACTIONAL_NULL_REGULARITY_20261005, blob f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff: actual bootstrap identity and divergent critical budgets.
- L2_NULL_DOMAIN_PROMOTION_20261006, blob b8ef9607e6823444a887ac71d8ec08bc21242510: L2 exterior candidate, endpoint removal, automatic derivative promotion and finite-dimensional chain.

Repeated rational controls check exponent budgets and exact truncated derivative growth. They do not certify the analytic difference estimate, an actual source bound or a null vector. No Lean build or axiom audit is claimed. Whole-domain positivity through 24/25 and the concurrent aperture cursor are preserved. Prescribed retained attachment, same-vector enlarged full-null cancellation, global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain unproved. Historical records unchanged.
