# RPB108: full-native order obstruction and pole-free index bound

Date: 2026-10-07 UTC. Recovered head: 6181af027e43e05d758ec06ea037e7704cb95311.
Lane: global/F4. Analytic theorem; no Lean certification or aperture computation.

## Exact objects and result

Let A_a be the physical operator associated to the COMPLETE actual native form Q_a on the supported logarithmic domain. Write H_a for the pole-free operator E0-T_a. This H_a is the operator called B_a in CRITICAL_RECIPROCAL_PROMOTION; it is NOT the bounded correction B_a in ACTUAL_LOG_OPERATOR_ATTACHMENT. With c(x)=cosh(x/2), s(x)=sinh(x/2) on I_a,

    A_a=H_a+P_a,  P_a=2|c><c|-2|s><s|.

The existing killed-jump construction proves that H_a has a positivity-preserving semigroup. The following exact smooth witness proves that A_a does not, for every a>51/100, including every possible future contact beyond the certified frontier. Its sufficiently far shifted resolvents are not positivity preserving either. This extends the earlier parity-modulus obstruction to explicit heat/resolvent order failure; it does not reopen that audit.

Separately, if Q_a>=0, the negative index of H_a is at most one; every negative spectral vector is even. On the odd sector H_a>=2|s><s|>=0. These are actual unshifted sign restrictions, not an endpoint-exclusion theorem.

## Smooth witness with the entire actual arithmetic retained

Choose arbitrary nonzero nonnegative h,v in C_c^infinity, respectively supported in (-51/100,-49/100) and (49/100,51/100). Every pair separation d=y-x lies in (49/50,51/50). The exact inequalities

    log(2)<49/50<51/50<log(3)

exclude ALL actual prime translations from this cross pairing: n=2 lies below it, and every n>=3 lies above it, regardless of how many frozen primes the window contains. Mass pairing is zero. Polarizing the native Euler jump formula, with k(d)=exp(-d/2)/(1-exp(-2d)), gives

    Q_a(h,v)=integral integral [2cosh(d/2)-k(d)]h(x)v(y) dx dy.

No source deletion, selected background, approximate pole, or assumed zeta symmetry is used. Since exp(2d)>1+2d>74/25, we have exp(-2d)<25/74 and k(d)<74/49. Since 2cosh(d/2)>=2,

    Q_a(h,v)>(24/49)(integral h)(integral v)>0.

The compact smooth packets are in dom(A_a): their full-line archimedean multiplier is L2, and compressed primes and pole are bounded physical L2 operators. Thus this is also <A_a h,v>, not merely a form calculation.

## Heat and resolvent consequences without an imported comparison theorem

A_a is self-adjoint and bounded below. At t=0, disjoint supports and strong differentiation on dom(A_a) give

    <exp(-t A_a)h,v>=-t Q_a(h,v)+o(t)<0

for every sufficiently small positive t. A positivity-preserving operator would have nonnegative pairing on these two nonnegative packets, so the actual full semigroup fails that property.

For real b tending to positive infinity, use the resolvent identity on h and b(A_a+b)^(-1)->I strongly:

    b^2 <(A_a+b)^(-1)h,v>
       =-<b(A_a+b)^(-1)A_a h,v> -> -Q_a(h,v)<0.

Hence every sufficiently large resolvent shift fails positivity preservation as well. For u=h-v, |u|=h+v gives Q_a(|u|)-Q_a(u)=4Q_a(h,v)>0, the corresponding global lattice-energy failure. All statements survive any scalar shift A_a-mu I: disjoint-support cross pairings are unchanged, and the heat operator changes only by a positive scalar factor. They therefore also survive the actual positive-eigenmode control.

This does NOT assert negative energy, a sign-changing null vector, or a failure of the certified positive forms. A positive definite self-adjoint operator need not have an order-preserving heat operator. It does not contradict the previously proved small-window comparison (a<=1/32), which cannot contain these packets. Nor does it rule out a kernel-specific sign theorem using extra arithmetic.

## What nonnegative unshifted contact DOES say about the base

At hypothetical actual Q_a>=0,

    H_a=A_a-2|c><c|+2|s><s|.

On c-perpendicular vectors its form is nonnegative. Any negative definite subspace of dimension at least two intersects this codimension-one space, a contradiction. Thus n_-(H_a)<=1. Reflection commutes with H_a and A_a. On the odd sector c is orthogonal and H_a=A_a+2|s><s|>=2|s><s|. Consequently the entire negative spectral subspace, if present, is even. This is a rank-one sign argument on the common form domain; it presumes neither invertibility of H_a nor simplicity of its zero eigenspace.

The actual mixed-null equations remain

    H_a h=-2c<c,h>+2s<s,h>.

They can have pole-free zero directions or inhomogeneous responses. Neither the index bound nor positivity preservation of H_a alone forces their endpoint trace to vanish. Applying a Hopf/groundstate theorem to A_a by transferring the order property of H_a is now explicitly invalid. Resolving the displayed compatibility with the complete actual source range remains necessary.

## Controls and dependency status

| Control | Audit |
|---|---|
| Actual rough positive eigenmode | Order obstruction is scalar-shift invariant. Its mixed equation has the extra mu h; a shift does not satisfy the unshifted contact premise. No terminal-defect exclusion follows. |
| Artificial compact-good-row logarithmic control | Its bounded rows are not the prescribed prime/pole split. The cross witness is actual; no sampling identification is inferred. |
| Fixed finite source restoration | This proof uses the complete native form. Existing o(1) normalized sharp-head restoration is unchanged; modified forms require their own order audit. |
| Two-row comparison contact | Its auxiliary rows change the displayed operator identity; its nonnegative contact cannot be substituted for actual Q_a>=0. |

No bounded-return/oscillation mechanism is obtained, and the global dependency graph does not shorten. The smallest remaining exclusion theorem is still actual unshifted full mixed-null source range -> liminf S_K(T)/log(T)<=0 (or a bounded/sublogarithmic sharp subsequence). The present advance is an exact failed transfer and a usable sign restriction on the pole-free base. It eliminates a global comparison-principle shortcut while preserving kernel-specific compatibility research. F4 and FULL TRANSPORT CLOSED remain open.

## Source custody and validation

Inputs at recovered head, Git blob pins:

- NATIVE_PARITY_MODULUS_20261006: 0a8eda427afd008ff95b76ad98dc93ee62c76db5 (closed parity audit consumed).
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0 (pole-free jump semigroup consumed).
- ACTUAL_LOG_OPERATOR_ATTACHMENT_20261007: 5b9fedd77956f6ba3e2efc0a71be14f673596fd1 (complete operator/pole/domain custody).

certify_native_order_obstruction.py checks the rational log enclosures, separation bounds, pole-minus-jump constant and polarization factor. It does not numerically simulate a semigroup, certify an eigenvalue, check actual zero sampling, or formalize the analytic argument. Historical records and certificates retained.
