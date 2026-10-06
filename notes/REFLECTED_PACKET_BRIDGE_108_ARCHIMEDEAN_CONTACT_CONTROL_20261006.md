# RPB108: exact archimedean contact control blocks boundary-only endpoint exclusion

Date: 2026-10-06 (America/Los_Angeles).
Source base: 42b2abf9985a4eeede2ab2e781d77c5114f98b0e.
Definitions: docs/TERMINOLOGY_RPB108_ARCHIMEDEAN_CONTACT_CONTROL.md.
Lane: global/F4; no fixed-aperture computations.

## Result

For every a>0 the actual quarter-line archimedean symbol admits a scalar-shift comparison form on the same supported logarithmic domain with:

- nonnegative whole-domain form and a nonzero attained kernel;
- logarithmic Riesz operator I+compact and one-dimensional complex kernel;
- the unchanged actual half-Carleman exterior kernel;
- supported-L2 null-domain promotion and derivative commutation;
- every finite logarithmic order and every global H^s order s<1/2;
- a nonzero groundstate whose zero extension is not global H1;
- failure of every eventual positive-frequency real-action upper bound C exp[-n/log(e+n)]||h||^2.

Thus the exact archimedean boundary equation, subcritical regularity, finite nullity and nonnegative contact do not force the H1 or action-decay input sought by the preceding global lane.

This is an analytic comparison construction. The scalar shift is tuned, the primes/pole of the full actual form are absent, and no actual-zeta null vector is constructed. It identifies the arithmetic information a successful actual exclusion proof must use, rather than falsifying that possible proof.

## Exact positive-kernel energy identity

Put b_j=j+1/4 and alpha_j=2j+1/2. The actual digamma Euler series gives
\[
m0(\xi)-m0(0)
 =\sum_{j\ge0}\frac{\pi^2\xi^2}{b_j(b_j^2+\pi^2\xi^2)}.
\]
For alpha>0,
\[
\int_0^\infty e^{-\alpha s}(1-\cos(2\pi\xi s))\,ds
 =\frac{(2\pi\xi)^2}{\alpha[\alpha^2+(2\pi\xi)^2]}.
\]
Substitution alpha_j=2b_j makes each summand twice this integral. The summands and integrands are nonnegative, so Tonelli gives
\[
m0(\xi)-m0(0)
 =2\int_0^\infty k(s)(1-\cos(2\pi\xi s))\,ds,\quad
k(s)=\sum_{j\ge0}e^{-\alpha_j s}
     =\frac{e^{-s/2}}{1-e^{-2s}}.
\tag{1}
\]
Plancherel and Tonelli then give, for every supported logarithmic h,
\[
E0(h)=m0(0)\|h\|_2^2+
 \int_0^\infty k(s)\|\tau_s h-h\|_2^2\,ds.
\tag{2}
\]
The integral is also one half of the double integral over all ordered physical pairs with kernel k(|x-y|). The factor one half is essential.

Equation (2) recovers precisely the actual exterior kernel, not a bounded replacement. Since |m0-w|<=C0, finite mass and finite energy in (2) are equivalent to the canonical logarithmic domain.

## The first physical eigenvalue is attained

The infimum lambda_a from the terminology is finite below because m0>=w-C0, and finite above by any nonzero compact smooth test. Let a minimizing sequence have physical mass one. Its logarithmic energy is bounded by E0+C0, hence it is bounded in D_a.

Weak Hilbert compactness supplies a subsequence converging weakly in D_a. Compact physical inclusion makes that subsequence converge strongly in L2, so its limit h retains physical mass one. Choose L>C0+1. The positive shifted symbol m0+L is comparable to w; its energy is an equivalent squared Hilbert norm and is weakly lower semicontinuous. Strong physical convergence subtracts the added L mass correctly. Thus E0(h)<=lambda_a, attaining the infimum.

Consequently Qcontrol_a>=0 on D_a, h!=0 and Qcontrol_a(h)=0. Hermitian positivity turns the zero diagonal into full mixed nullity against all D_a tests; variation yields the same conclusion. The logarithmic Riesz operator is I+compact because the difference m0-lambda_a-w is bounded and the physical inclusion is compact. Its kernel is finite.

No eigenvalue or groundstate is computed numerically. The contact is produced by tuning only the comparison mass shift.

## The kernel has dimension one

For real u, replacing u by |u| leaves mass fixed and can only decrease the positive-kernel energy (2). It also keeps |u| in D_a: the lowered energy is finite and (1) supplies its logarithmic membership.

If the positive and negative sets of u both have positive measure, the decrease is strict. In the double-integral description,
\[
|u(x)-u(y)|^2-\bigl||u(x)|-|u(y)|\bigr|^2
 =4|u(x)u(y)|
\]
on opposite-sign pairs. The kernel is strictly positive at every nonzero separation. Both sign sets have positive measure, so their integral is strictly positive. Finiteness follows by domination by the original finite energy.

A real minimizing eigenfunction therefore has one sign. If two linearly independent real groundstates existed, they could be chosen nonnegative. A real combination of them changes sign: choose a ratio level between two distinct essential ratios, with zero denominator handled as infinite ratio. This contradicts the preceding strict decrease. Thus the real groundstate space is one-dimensional. The symbol and support domain commute with complex conjugation, so real and imaginary parts of any complex kernel vector are real groundstates. The complex kernel is one-dimensional as well.

This argument applies to the comparison form only. The actual full pole contributes a different physical kernel and cannot be discarded to assert a one-dimensional actual K_a.

## Supported-L2 promotion and the H1 obstruction survive this control

For a supported L2 solution of the control's interior equation, the off-support mass term is zero. Its exterior multiplier remains -H_k h and has the already proved Carleman L2 norm bound 4||h||_2. On the interior the shifted multiplier is zero. The shifted symbol has logarithmic growth and hence the global distribution belongs to H^{-1/4}.

The existing endpoint cutoff removability proof therefore applies unchanged: subtract the piecewise L2 representative, then remove the endpoint-supported H^{-1/4} defect. The multiplier is globally L2, and w<=|m0-lambda_a|+C derives h in D_a and full mixed nullity. This is promotion for the comparison equation, not an invocation of a theorem with the wrong actual pole input.

Now suppose its nonzero groundstate were globally H1. Its global derivative h' is supported L2, with no boundary deltas. The constant-coefficient multiplier commutes with differentiation, so h' solves the same interior equation. Promotion puts h' in the same one-dimensional kernel, hence h'=zh for some complex z. Fourier transformation gives
\[
(2\pi i\xi-z)\widehat h(\xi)=0.
\]
The multiplier has at most one real root; it cannot support a nonzero L2 Fourier transform. This contradicts ||h||_2=1. Therefore the groundstate is not globally H1.

The recovered logarithmic and fractional commutator proofs also apply with T_a=lambda_a I and p=0. The scalar operator commutes with every capped Fourier weight and has norm |lambda_a|; the same projection and archimedean commutator estimates yield every finite logarithmic order and H^s for s<1/2. Thus that entire regularity package is compatible with a non-H1 nonnegative null mode.

## Gaussian endpoint decay is genuinely additional information

Define the control's genuine action using m0-lambda_a, with no pole. The same log envelope and moving-Gaussian split give
\[
\Re A^{control}_n\ge
 (\log n-C')M_n-D(1+\log n)e^{-n/4}\|h\|_2^2.
\]
The preceding one-sided Gaussian logarithmic mass theorem applies to this compact supported nonzero groundstate. Hence, for every finite C>0 and every n0, some integer n>=n0 satisfies
\[
\Re A^{control}_n>
 C e^{-n/\log(e+n)}\|h\|_2^2.
\tag{3}
\]
Otherwise the proved lower-estimate/budget implication would force h=0. This is an exact analytic obstruction to obtaining the desired decay from the listed boundary/regularity properties alone.

The control does not include actual complete zeta divisor analyses or the prescribed prime/pole normalization. No claim is made that it satisfies those independent source constraints.

## Exact sign-defect control

In the physical window [-2,2], take u=1_I-1_J,
I=[-3/2,-1/2], J=[1/2,3/2]. Both u and |u| have physical mass 2 and belong to D_2; indicators have Fourier decay O(1/|xi|), giving finite logarithmic energy.

On I times J, 1<=y-x<=3. Thus k(y-x)>=exp(-3/2)>1/5, and (2) gives
\[
E0(u)-E0(|u|)=4\int_I\int_J k(y-x)\,dy\,dx>4/5.
\tag{4}
\]
The constant follows from e<11/4 and (11/4)^3<25, so e^{3/2}<5. Any scalar mass shift cancels in (4). The accompanying rational script checks the exponential ceiling via its series remainder, the coefficient four, and the lower constant. These are comparison vectors, not actual-zeta null modes.

## Failed implication and next theorem

Failed implication:
  exact actual archimedean boundary kernel + supported full interior equation
  + nonnegative Fredholm contact + finite kernel + all subcritical regularity
  -> global H1 or the nearly exponential real-action upper estimate.

The shifted actual-archimedean control disproves that implication. It belongs to endpoint exclusion. It neither supplies nor substitutes a retained historical packet and does not use same-vector enlarged transport.

The smallest remaining actual theorem must use the prescribed arithmetic combination m0-T_a plus the exact pole/source constraints to exclude the nonnegative contact kernel. The existing all-window contact dichotomy, finite response, and Gaussian budget consume such an input immediately. Additional estimates from the archimedean edge singularity alone are not that input.

## Custody and validation

Inputs read at the pinned source:
- BOUNDARY_SCALING_20261005 and ENDPOINT_BOUNDARY_REGULARITY_20261005;
- LOGARITHMIC_BOOTSTRAP_20261005 and FRACTIONAL_NULL_REGULARITY_20261005;
- L2_NULL_DOMAIN_PROMOTION_20261006;
- ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004;
- ONE_SIDED_GAUSSIAN_BUDGET_20261006;
- GLOBAL_F4_ENTRY_AUDIT_20261006.

Analytic validation includes the Euler/Laplace normalization, both compactness norms, modulus-domain preservation, groundstate simplicity, comparison-specific endpoint promotion, global derivative equation, and the separation of the actual arithmetic source constraints. Exact controls are not a Lean proof or an eigenvalue computation.

No Lean/workflow changes, new CI or axiom certificate, actual endpoint existence or aperture advance. Historical records preserved. F4 and FULL TRANSPORT CLOSED remain open. Cursor: arithmetic-specific nonnegative-contact exclusion; boundary-only H1/Gaussian regularity bootstrapping has this explicit obstruction.
