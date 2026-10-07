# RPB108: density and compact good rows do not kill the logarithmic coefficient

Date: 2026-10-07 UTC. Recovered live head 77f7c144cd0385e10e19e0f1356296da2d353a5d.
Definitions: [compact rows at logarithmic scale](../docs/TERMINOLOGY_RPB108_COMPACT_ROW_LOG_SLOPE.md).
Category: endpoint exclusion / arithmetic transfer obstruction. Analytic control, not Lean-certified.

## Result and exact failed implication

The new actual endpoint target is sublogarithmic growth of the complete signed height trace. The older compact-row control proved divergence but did not show failure at this weaker scale. Here one supported physical vector and fourfold symmetric sinh/cosh observation rows give

    A_tau^art(h)/log(1/tau) -> 2Delta/log q>0,
    A_tau,negative^art(h)/log(1/tau) -> 2N^2/log q>0,
    S^art_h(T)/log T -> 2Delta/log q>0.

All rows are GOOD, their unweighted negative analysis is compact on the supported logarithmic domain, and their cumulative transverse second count is only O(log T), much smaller than the available actual density upper bound. The physical vector belongs to every subcritical logarithmic Sobolev space but fails H^(1/2).

Thus the failed inference is

    averaged transverse sparsity + compact good negative rows
    + coherent supported physical sampling + all subcritical regularity
       -> negative or signed Abel contribution o(log(1/tau)).

The locations are ARTIFICIAL and do not obey the actual full-native equation. This does not refute a zero-specific theorem using that equation. It isolates why neither discarding the exceptional rows nor improving unweighted compactness supplies the needed logarithmic estimate.

Separately, on the ACTUAL source dictionary every fixed finite row deletion/restoration contributes zero to the logarithmically normalized height trace. The endpoint coefficient therefore cannot be removed merely by passing to the already coercive effective background with a fixed finite actual selection.

## 1. The one physical vector and exact profile bounds

Use q,H_j,c_j,f,h from the registry. Sum_j c_j=1/255, so the series converges uniformly and in L2. The triangle is compactly supported in [1/16,3/16]. For every 0<=s<1/2,

    ||f exp(-iH_j x)||_(H^s_log)<=C_s H_j^s sqrt(log(e+H_j)),

and sum_j H_j^(s-1/2) sqrt(log(e+H_j)) is finite. Hence h is canonical and has all the subcritical regularity used in the actual null bootstrap. This is a property of the control, not its nullity.

The previously audited product-variation calculation applies unchanged: for g_p=f cosh(Bx) and g_n=f sinh(Bx), TV(g_p''),TV(g_n'')<100. Thus their angular Fourier transforms have modulus <=100/|omega|^2 away from zero. Also

    1/16<=P<=9/128,
    3/2048<=N<=1/128,
    Delta>=63/16384>0.

At a positive height H_j the resonant term is P c_j or N c_j. Every other gap is at least H_j/2, and sum c_k=1/255, giving the explicit interference bound

    |p_(H_j)-P c_j|, |n_(H_j)-N c_j|
       <=(400/255)H_j^(-2)<2H_j^(-2).

For larger indices the gap is also at least half their own height; the displayed looser bound is sufficient. At a negative height -H_j all frequencies are nonresonant: H_j+H_k>=H_j, so both observations have modulus <H_j^(-2). The beta sign partner preserves p and flips n, so it doubles norm weight without providing another independent observation.

Squaring the positive-height estimates proves, for either channel and for the signed difference,

    | |p_(H_j)|^2-P^2/H_j |<=H_j^(-5/2),
    | |n_(H_j)|^2-N^2/H_j |<=H_j^(-5/2),
    | d_(H_j)-Delta/H_j |<=H_j^(-5/2).

Indeed the signed error is at most 4(P+N)H_j^(-5/2)+8H_j^(-4), whose coefficient is less than one for H_j>=q. These bounds retain cross-frequency cancellation rather than assuming it absent. After multiplication by H_j every error is absolutely summable. Negative-height squared observations also have summable first-height weight.

## 2. Exact logarithmic scale, not just divergence

Put k(x)=(1-exp(-x))/x and B_tau=sum_j k(tau q^j). For each tau>0 the sum converges. Let m=floor(log(1/tau)/log q), for sufficiently small tau so m>=1. Since 0<=1-k(x)<=x/2 and k(x)<=1/x,

    -q/[2(q-1)] <= B_tau-m <= q/(q-1).

The left inequality sums the deficits for j<=m; the right bounds the geometric tail j>m. Therefore

    B_tau=log(1/tau)/log q+O(1).

Because alpha_tau(H)<=H, all weighted interference errors have a uniform tau-independent absolute bound. The two positive-height beta partners contribute the leading term, and negative-height partners contribute only a bounded term. Thus the signed, positive and negative Abel slopes are respectively

    2Delta/log q, 2P^2/log q, 2N^2/log q.

They are positive, and their difference agrees with the signed slope. Likewise the sharp signed head is 2Delta floor(log T/log q)+O(1), proving its positive normalized limit. No unregularized difference of divergent moments is used.

For completeness the physical vector itself is not H^(1/2). On disjoint angular intervals |theta-H_j|<=1/4, the main triangle transform has modulus at least c_j/32, while the same cross estimate is at most 2H_j^(-2). Thus |F_h(theta)|>=c_j/64 there. Each interval contributes a fixed positive amount to integral |theta||F_h(theta)|^2 dtheta, so that integral diverges. It is not necessary to invoke an actual positive-source equivalence for these artificial rows.

## 3. All occupied bins are good, with much stronger density

Each occupied positive or negative unit bin has two beta partners, with transverse second mass 2B^2=9/32. Its normalized mass is

    mu_(+/-H_j)=(9/32)/log(e+H_j)->0.

The local sampling/sinh-series proof from the pinned compactness note applies to these explicit profiles, so their unweighted negative map is compact D_a->ell2. No arbitrary coefficient-space inversion is used.

In fact every occupied bin satisfies the existing good-bin threshold. Since H_j>=q>e^e and log(2H_j)/log H_j<=17/16,

    2B^2 log log(e^e+H_j)/log(e+H_j)
       <=(9/32)(17/16)=153/512<1.

Empty bins are good automatically. There is no exceptional contribution to hide here. Counting all four sign partners gives Z2^art(T)=4B^2 floor(log T/log q)=O(log T), and unit-bin count is at most two. These meet the upper-statistical hypotheses used in the density/compactness route. No total actual zero-count asymptotic, explicit formula or actual divisor identity is claimed.

The support of h lies within the certified actual 49/50 window. Its actual native energy is strictly positive by that certificate, since h is nonzero. Thus the same physical vector is explicitly NOT actual null. Its artificial height sums cannot replace the actual ones in a full-native null test.

## 4. Actual finite restorations leave the logarithmic coefficient unchanged

Let F be ANY fixed finite subset of actual divisor coordinates. For fixed h, or a finite physical kernel basis, alpha_tau(|theta|)<=|theta| gives

    sum_(q in F) alpha_tau(|theta_q|)(|p_q(h)|^2+|n_q(h)|^2)
       <=sum_(q in F) |theta_q|(|p_q(h)|^2+|n_q(h)|^2)<infinity.

Consequently deletion or restoration of these coordinates changes A_tau/log(1/tau) by a quantity tending to zero. The same holds for sharp heads divided by log T. For the fresh actual finite negative selection R, its effective positive form Q+R*R has the same leading signed height coefficient after reinstating the selected rows as positive contributions. On original actual K, Q+R*R is coercive and has diagonal value ||Rh||^2; h is NOT an effective-background null vector. No conclusion is drawn by substituting its equation for q_h=0.

This statement concerns the fixed finite source observations only; a compensator's complete physical analysis still has infinitely many rows and is not erased by this argument. No historical retained packet is identified with R, and no prescribed morphology is replaced. A packet varying with tau would require a new uniform estimate; the fixed-packet bound supplies none.

## 5. The exact actual equation and remaining theorem

At a hypothetical actual contact the full equation remains

    <P0 h,P0 v>=<N_good h,N_good v>+<N_exc h,N_exc v>

for EVERY canonical same-window v. The complete graph projector Pi gives the lawful Abel identity

    A_tau(h)=<Jsrc Gamma h,[M_(alpha_tau),Pi]Gamma h>.

Its logarithmic normalization is now exactly (2/pi)|kappa_R(h)|^2 by the preceding actual slope theorem. This control does not satisfy that actual equation and does not prove the graph error is nonpositive. The actual rough positive eigenmode, which shares the imported density estimates, also has a positive actual logarithmic slope; its interior residual is mu<h,v>, not zero.

The smallest remaining theorem on this route is still a nonpositive liminf of the WHOLE actual contact's logarithmically normalized graph-error/Abel trace. A proof must use the unshifted full mixed equation together with additional actual source-range information. The average transverse estimate and good-row compactness alone do not provide that information. Controlling only the exceptional negative rows is insufficient, even if one were to remove every exceptional row.

This obstruction belongs to endpoint exclusion. Derivative promotion remains closed analytically; actual trace vanishing, retained attachment, same-vector enlarged full-null transport and F4 remain open. Certified frontier 49/50 and the newer aperture-lane 99/100 preflight are preserved; no new aperture estimate is requested or derived.

## Validation and custody

The companion script checks the exact triangle/profile ceilings, positive signed margin, squared interference budgets, good-bin margin, summable error budgets and independent finite geometric Abel bounds. These are analytic controls, not actual zero data, a global arithmetic certificate, Lean build or axiom audit. Five source pins are recorded in the manifest, including the actual positive-eigenvalue control and the new actual Abel slope. No new external theorem is imported; the accepted beta bound and density source retain their previous custody.
