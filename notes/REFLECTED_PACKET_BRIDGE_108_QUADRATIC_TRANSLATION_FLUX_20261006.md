# RPB108: signed quadratic translation flux and a direct endpoint gate

Date: 2026-10-06 (America/Los_Angeles). Recovered live source: b7f42bb504ca41032f8215f3f5ea966ede44cf12.
Definitions: [signed flux registry](../docs/TERMINOLOGY_RPB108_QUADRATIC_TRANSLATION_FLUX.md).
Analytic conditional actual result; not Lean certified. No new aperture estimate.

## Exact same-vector regularity test

Reuse the established exact translation identity, with its original sign and actual frozen prime/pole terms:
$
 F_h(t)=-D_m(t;h)+(\cosh(t/2)-1)P_0(h),\qquad
 D_m(t;h)=\int m_a(\xi)(1-\cos(2\pi\xi t))|\widehat h(\xi)|^2d\xi.
$
Here h is an actual full mixed-null vector, and F_h is its genuine exterior residual pairing. The support-projected translated test is already lawful; that domain proof is reused.

There is a sharp dichotomy:
$
 h\in H^1(\mathbb R)\quad\Longrightarrow\quad F_h(t)/t^2\longrightarrow0,
 \qquad
 h\notin H^1(\mathbb R)\quad\Longrightarrow\quad F_h(t)/t^2\longrightarrow-\infty.
 \tag{1}
$
In particular, on actual full-null vectors,
$
 h\in H^1(\mathbb R)
 \quad\Longleftrightarrow\quad
 \limsup_{t\downarrow0}F_h(t)/t^2>-\infty.
 \tag{2}
$
A lower bound along one sequence suffices. This requires no selected rows, effective inverse, coefficient normalization, or Gaussian summation. It is a direct actual-source reformulation of the quadratic regularity gate, not a proof of its missing arithmetic input.

## Proof of the rough limit and the regular cancellation

Choose N with m_a>=w/2 on |xi|>=N, using |m_a-w|<=C_a. On the bounded complementary region, the absolute value of D_m/t^2 is uniformly bounded by 2 pi^2 integral_(|xi|<N) |m_a| xi^2 |hhat|^2. For non-H1 h the high-frequency weighted derivative energy is infinite. Fatou, or the existing bounded-frequency cosine floor followed by expanding the cutoff, gives
$
 \int_{|\xi|\ge N} m_a(\xi)
 \frac{1-\cos(2\pi\xi t)}{t^2}|\widehat h(\xi)|^2d\xi
 \longrightarrow+\infty.
$
The pole quotient tends to P_0/8. Hence the rough limit in (1) is negative infinity for all t tending to zero, not merely a subsequence.

For global H1 h, automatic supported-L2 derivative promotion gives g=h' in the same full native kernel and in the logarithmic domain. Thus integral xi^2 w |hhat|^2 is finite, and dominated convergence applies even though m_a can have a negative low-frequency part. The zero global endpoint traces give M_-(g)=M_-(h)/2 and M_+(g)=-M_+(h)/2. Consequently
$
 0=Q_a(g)=4\pi^2\int \xi^2m_a(\xi)|\widehat h(\xi)|^2d\xi-P_0(h)/4.
$
Therefore D_m(t;h)/t^2 tends to P_0/8, exactly cancelling the pole contribution. This proves the regular limit. General H1 carrier membership alone would not guarantee the weighted derivative integrability or this cancellation; full actual nullity and derivative promotion supply both.

The elementary envelope also gives a universal finite upper bound F_h(t)/t^2<=C_a'||h||_2^2. Thus the limsup in (2) cannot be plus infinity. Its finite lower subsequence forces weighted derivative energy by the same high-frequency argument, hence H1 and the exact zero limit.

## One scalar full-kernel source target

For an L2-orthonormal basis of the entire finite actual K,
$
 T_K(t)=-\int m_a(\xi)(1-\cos(2\pi\xi t))\rho_K(\xi)d\xi
 +(\cosh(t/2)-1)P_K.
 \tag{3}
$
Both this formula and the exterior-pairing definition are basis independent: unitary change of basis preserves the sum of the Hermitian quadratic forms. No pointwise sign of the kernel covariance is asserted.

If K is nonzero, the established derivative-chain ceiling prevents all of K from lying in global H1. At least one vector of every basis is rough. Every regular contribution divided by t^2 tends to zero; every rough one tends to negative infinity. With finitely many terms,
$
 \boxed{T_K(t)/t^2\longrightarrow-\infty\quad(K\ne0).}
 \tag{4}
$
The smallest sufficient arithmetic theorem on this route is therefore
$
 \boxed{\limsup_{t\downarrow0}T_K(t)/t^2>-\infty}
 \tag{5}
$
at every hypothetical finite nonnegative actual first contact. Equivalently, prove T_K(t_n)>=-C t_n^2 on one sequence tending to zero. This would contradict (4), exclude contact, and invoke the existing aperture dichotomy to give global all-window domination. Basiswise lower subsequences, possibly different for each basis vector, also suffice through (2) and derivative invariance.

Equation (5) is **unproved**. For a hypothetical nonzero actual kernel, (4) says it is false; its proof from arithmetic would be an endpoint-exclusion argument. This reduction does not independently strengthen the established gain/Gaussian criteria into an unconditional exclusion theorem.

Although (5) is a scalar trace, it is not the previously audited rank-one inverse-boundary observation. It sums an entire physical orthonormal full-kernel basis and depends on t. No injectivity of one averaged inverse moment is used.

## Failed implication and scope

The existing upper bound F_h<=O(t^2), continuity, subcritical bounds, or even a C1 flux with zero first derivative do not give (5). The comparison scalar F(t)=-t^(3/2) has all those rate properties and F(t)/t^2 tends to negative infinity. It is a rate control, not asserted to be an actual residual flux or null vector. The available architecture leaves this exact lower-sign arithmetic theorem open. The earlier actual mass-shift control already rules out using generic native architecture alone to infer actual zero-normalization exclusion; it is not reopened here.

The physical vector h is fixed in every identity. Its translated copy is a test, then projected into the original support; translation changes that test vector. No dilation, same-vector enlarged full-nullity, or enlarged cancellation is obtained. Actual full-nullity is essential throughout; effective-background nullity and a historical selected WD-T38 witness cannot substitute for it.

Remaining category: **endpoint exclusion**. Prescribed historical carrier/row/covariance/separation attachment is still independent. No F4 entry condition involving prescribed retained morphology or enlarged/null transport is discharged.

## Custody and validation

Source blobs and repeat controls are recorded in notes/data/RPB108_QUADRATIC_TRANSLATION_FLUX_20261006.json. The exact source translation identity, derivative promotion, and finite-kernel ceiling are reused. Historical files and certificates are unchanged.

65 pole cancellation, 128 cosine/cosh coefficient, and 128 signed-rate controls check the signs and reject the reversed inequality. They do not verify the analytic limits or an actual arithmetic bound. No Lean executable is present in the recovered mirror; no Lean files, axioms or CI results change. Certified positivity through 47/50 is preserved. F4 and FULL TRANSPORT CLOSED remain open.
