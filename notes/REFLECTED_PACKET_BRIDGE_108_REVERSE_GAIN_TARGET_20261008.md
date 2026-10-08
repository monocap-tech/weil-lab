# RPB108 NF55: reverse the search to unconditional source gain

Date: 2026-10-08 UTC. Recovered head: 10c56d50c94024e53360242c8cc410c5787cb011.

This is a research reset and an attempted shortcut audit, not a new positivity theorem. NF51–54 remain valid conditional contact results. Their continuation is suspended as the primary global front. The target below was already open in GLOBAL_POSITIVE_KERNEL on October 4; reactivating it does not shorten the proof dependency graph.

## Start before contact

On each fixed canonical supported domain D_a, keep the complete actual normalized divisor channels P_a and N_a, including multiplicity copies and all ordinates. The original form is

    Q_a(h,h) = ||P_a h||² - ||N_a h||².

Use the established boundedness and positive observability at this fixed aperture:

    c_a ||h||_D <= ||P_a h|| <= C_a ||h||_D,  c_a > 0.

Thus V_a = Ran P_a is closed and P_a has a bounded inverse on V_a. Define the **source gain** as the operator T_a: V_a -> negative source space, T_a(P_a h)=N_a h, and its norm g_a=||T_a||. This uses the full positive range, not a selected finite packet or an extension to the whole positive source space. The constants may depend on a. No uniform bound in a follows.

The direct global target is

    for every finite a, g_a < 1.                         (G)

It is an inequality on every supported vector, before assuming a null vector. It makes no reference to endpoint asymptotics or a height-weighted head. For the present I+compact form family it is equivalent to strict canonical coercivity at every finite aperture. This is the unresolved arithmetic inequality, not a consequence of observability.

## Exact quantitative dictionary

If g_a <= gamma < 1, then

    Q_a(h,h) >= (1-gamma²)c_a² ||h||_D².

Conversely, a bound Q_a(h,h)>=delta_a||h||_D² gives

    ||N_a h||² / ||P_a h||² <= 1-delta_a/C_a²,

so g_a²<=1-delta_a/C_a²<1. Both statements retain the ORIGINAL, unshifted form.

At a nonnegative window g_a<=1. If its canonical Riesz form is I+compact, absence of a kernel implies a positive spectral gap and hence g_a<1. Therefore g_a=1 at such a window is attained by a nonzero null vector. Attainment here follows from the Fredholm form, not from an assertion that T_a is compact. Positive sampling injectivity alone does not imply any of these unit bounds.

For global exclusion it is enough to forbid g_a=1 at every nonnegative window: the existing first-contact constructor then excludes an eventual negative window. Condition (G) is the stronger unconditional statement we will try to prove directly. The certified aperture-one result supplies a starting interval, not an estimate for arbitrary a.

## First direct attempt: use the transverse strip coordinatewise

This fails even before questions of height limits. For one hypothetical actual off-line pair with theta real and beta nonzero, the raw coordinates are

    p(h)=integral h(x) exp(i theta x) cosh(beta x) dx,
    n(h)=integral h(x) exp(i theta x) sinh(beta x) dx.

Choose a smooth, nonnegative, even bump chi supported in (-a,a), positive somewhere away from zero, and h(x)=exp(-i theta x) x chi(x). Then p(h)=0 by oddness, whereas n(h) is nonzero: x sinh(beta x) has the constant sign of beta away from zero. Positive source normalization does not change this conclusion.

Consequently no finite constant can bound |n(h)| by that SAME pair's |p(h)|, even for arbitrarily small nonzero beta. The available |beta|<=3/8 cannot establish a rowwise tanh contraction. This is conditional on a pair being off-line; no existence of an off-line zeta zero is asserted. Other actual positive coordinates of this h remain present and are precisely what a complete-range proof must use.

The viable arithmetic object is therefore the full Gram inequality

    P_a* P_a - N_a* N_a >= delta_a I_D,

not a scalar inequality between individual paired samples. A gain estimate derived just from general strip width and bounded sampling would need an additional quantitative relation between the complete actual rows. None has been established in this pass.

## Positive-eigenmode distinction

Suppose the original form is strictly positive with lowest physical level mu>0. Its ORIGINAL gain satisfies g_a<1. For the shifted form Q_a-mu||h||_2², the negative channel instead becomes (N_a h, sqrt(mu)h). Its squared gain ratio is

    (||N_a h||²+mu||h||_2²)/||P_a h||².

At a lowest eigenvector this ratio is exactly one, while the original ratio is 1-mu||h||_2²/||P_a h||²<1. Thus the reset distinguishes zero from a positive level explicitly. Erasing the mass term would erase that distinction. Endpoint and translated-cluster properties of the shifted eigenmode cannot settle (G).

## What counts as the next result

An admissible advance is an estimate for the ORIGINAL complete-range gain at apertures beyond the certified interval, with a mechanism that can apply to every finite aperture, or a new arithmetic relation implying that estimate. A further conditional description of a hypothetical contact does not count as an advance on this target.

Finite trial subspaces yield lower bounds on g_a; a successful trial calculation cannot certify a global upper bound. A finite negative source prefix also yields a lower bound. Any upper certificate must retain a proved tail bound and the complete positive-range constraint. No finite source cutoff is treated as a physical null test.

The earlier right-line contour calculation bounds the entire prime bulk by O(log log T). It cannot cancel the positive logarithmic gamma term. That cancellation route is retired as the active target. Its historical proof remains intact.

Validation is limited to the quantitative algebra, a finite positive-level control, and the analytic parity countertest above. No actual gain beyond aperture one has been computed, no new arithmetic inequality has been proved, and there is no Lean claim. Actual contact exclusion, RH, F4 and full transport remain open.
