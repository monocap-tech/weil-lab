# RPB108: the actual finite kernel is one exact derivative chain

Date: 2026-10-07 UTC. Recovered head 7bda747090cb1db301b605d1f93bf2ef80636a57.
Definitions: [actual kernel derivative chain](../docs/TERMINOLOGY_RPB108_KERNEL_DERIVATIVE_CHAIN.md).
Category: endpoint exclusion / actual regularity structure. Analytic, not Lean-certified.

## Result

If the full actual K at a fixed window is nonzero of dimension r, then its global Sobolev flags have EXACT dimensions

    dim F_j=r-j, 0<=j<=r; F_r={0}.                  (1)

There is one chain generator h_* in H^(r-1) such that

    K=span{h_*,Dh_*,...,D^(r-1)h_*}.                (2)

Every vector in this ordered chain is a full-native null on the SAME window. The terminal g_*=D^(r-1)h_* has nonzero actual averaged boundary trace; the other chain vectors have zero trace. Thus the trace is injective on the one-dimensional rough quotient but is not injective on K when r>1.

This closes the exact chain morphology left undetermined by the earlier regularity ceiling and rank-one rough quotient. It does not eliminate the chain. A supported-function control shows that all these regularity, parity, moment and trace features can coexist in a finite physical carrier without satisfying the actual null equation. The remaining arithmetic trace-vanishing gate is unchanged.

## 1. Each critical trace removes exactly one dimension

The proved actual endpoint trace theorem gives

    F_1=ker(kappa_R|_K), dim F_1=r-1,

with left/right trace balance. Global derivative promotion puts Dh in the SAME K for every h in F_1.

Inductively, for h in F_(j-1), D^(j-1)h belongs to K and is L2. The trace criterion says that this derivative belongs to H1 exactly when its right trace vanishes. Therefore

    F_j=ker ell_j within F_(j-1),
    ell_j(h)=kappa_R(D^(j-1)h).                     (3)

This is an exact domain identity, not differentiation of a rough trace before it is defined. If F_(j-1) is nonzero, ell_j cannot vanish identically. Otherwise F_j=F_(j-1), and differentiation would map that finite nonzero subspace into itself: every h in F_j has Dh in K intersect H^(j-1)=F_(j-1).

That would contradict the existing compact-support Fourier-polynomial argument. A finite derivative endomorphism has a nonzero characteristic polynomial p with p(D)h=0 globally. Fourier transformation forces the nonzero L2 Fourier profile of a compact physical h to be supported on the finite real roots of p(2pi i xi), impossible. Thus ell_j is nonzero and its scalar kernel has codimension one. Iteration proves (1).

## 2. One generator spans the whole actual kernel

Choose nonzero h_* in the one-dimensional F_(r-1). Repeated lawful derivative promotion gives D^j h_* in K for 0<=j<=r-1. These r physical vectors are independent: any linear relation is another nonzero polynomial(D) equation on a nonzero compact L2 h_*, excluded by the same Fourier argument. They form a basis, proving (2).

For j<=r-2 these vectors are H1 and have zero right and left trace. The last cannot be H1, since h_* would then be in F_r={0}. Thus kappa_R(g_*) is nonzero, and its left trace is sigma times it, sigma=+1 or -1 from the actual reflection balance.

The flags can also be read directly from this basis:

    F_j=span{h_*,Dh_*,...,D^(r-1-j)h_*}.

No coefficient carrier has been identified with a historical packet. The equalities refer to actual physical vectors and full mixed nullity. A derivative is a different physical vector, so (2) supplies no same-vector enlarged/null transport.

## 3. The chain fixes the regular endpoint asymptotics

Let c=kappa_R(g_*)!=0. The proved strong scaled L2 trace of g_* is enough to integrate its primitives. For n>=1, all relevant intermediate global H1 derivatives have zero endpoint traces. Hence

    D^(r-1-n)h_*(a-v)
       =(-1)^n/(n-1)! integral_0^v
                        (v-t)^(n-1)g_*(a-t)dt.

Rescale t=vz and use strong L2 convergence of sqrt(log(1/v))g_*(a-vz) to c. Pairing with (1-z)^(n-1) gives

    D^(r-1-n)h_*(a-v)
       =(-1)^n c v^n/[n! sqrt(log(1/v))]
             +o(v^n/sqrt(log(1/v))).                (4)

These are ordinary primitive-value asymptotics for n>=1. The n=0 terminal vector still has the proved AVERAGED/L2 trace; no unproved pointwise terminal asymptotic is inserted.

At the left endpoint the sign from taking a primitive is positive and c is replaced by sigma c. The one-dimensional top flag is reflection invariant, so h_* has parity sigma*(-1)^(r-1); its derivative chain alternates parity. Endpoint moments, traces and regularity are all attached to the same actual chain, without dilation.

## 4. A physical chain control prevents an unjustified exclusion

The implication one-dimensional rough quotient -> total kernel dimension one is false for supported physical carriers. For any r>=1, take on (-1,1) a bounded continuous real g_0 with smooth interior and logarithmic edge profiles 1/sqrt(log(1/v)), with equal or opposite left/right coefficients sigma. Choose short edge cutoffs so g_0 has that reflection parity. This vector has all H^s_log norms for s<1/2, but not H^(1/2), by the exterior Hardy term integral dv/[v log(1/v)].

Correct its first r-1 polynomial moments by subtracting interior functions. For example take the even interior cutoff

    chi_r(x)=(1-4x^2)^(r+2) on |x|<1/2, zero otherwise.

The moment matrix M_jk=integral chi_r(x)x^(j+k)dx, 0<=j,k<=r-2, is positive definite: it is the positive weighted Gram form of independent monomials. It has exact rational entries. Solve this finite system and put g=g_0-sum_k b_k chi_r(x)x^k, so integral x^j g=0 for j<=r-2. The even cutoff makes the parity blocks independent and preserves sigma. The correction is sufficiently smooth and leaves both edge profiles unchanged.

Take the (r-1)-fold primitive h from the left endpoint, with zero initial constants. The moment equations make h and all its intermediate primitives vanish outside (-1,1). Then h is globally H^(r-1), and h^(r-1)=g is rough. The carrier

    V_r=span{h,Dh,...,D^(r-1)h}

has exactly the flags (1), a one-dimensional rough quotient, balanced endpoint trace Gram forms, the parity alternation, and the primitive asymptotics (4). Nonzero trace is confined to the terminal coordinate. This is a single supported physical construction, not freely assigned coefficient vectors.

It is NOT asserted to satisfy the actual full-native mixed-null equation, actual divisor synthesis or a nonnegative native contact. Its purpose is narrow: neither chain morphology nor its ordinary compact-support moment conditions contradict functional analysis. They cannot replace the missing arithmetic condition. The actual rough positive eigenspace also has the same exact chain theorem, since its derivative/trace results hold after a fixed mass shift; it supplies the existing actual shifted control.

## Remaining theorem and standing

To exclude an unshifted actual first contact, prove that its whole-kernel right trace vanishes, equivalently exclude its nonzero terminal trace c. No new argument here makes c zero. Finding one zero-trace regular vector only produces a longer chain, not contact exclusion.

The smallest unresolved theorem remains endpoint exclusion, not retained attachment or null transport. The exact actual equation has now forced a single chain with prescribed averaged rough endpoint profile and all regular primitive asymptotics. The last unshifted arithmetic step must rule out that terminal profile/trace; generic finite dimension, boundary balance, compact source tails, regularity ceilings and polynomial moment corrections cannot do it.

## Source custody and validation

Pinned inputs at recovered 7bda747090cb1db301b605d1f93bf2ef80636a57:
- ACTUAL_ENDPOINT_TRACE_20261007: 1996d3fb3358965c5468481c31252f3dda440e69.
- ENDPOINT_STRIP_MATCHING_20261007: 3ba5f3a36fde17ce90d58dfcede20b93b07778e8.
- ENDPOINT_MASS_PROMOTION_20261007: 6bae812597a46f52e110ecea4a150cfa7c369d80.
- CRITICAL_RECIPROCAL_PROMOTION_20261007: 9983be22ab58e926b5e15127f8feaf53d43329e0.
- FINITE_SOURCE_REGULARITY_20261006: 03b6f5a9d6cb9caa6044d3fd247156606703e91b.

No new external theorem imported. Analytic audit: trace defined only after lawful derivative promotion; exact scalar flag kernels; nonzero-functional proof through derivative endomorphism; global polynomial independence; H1 endpoint values before primitives; terminal averaged trace versus regular pointwise asymptotics; moment-corrected physical control without native-null claims. Companion rational Gram audits verify eight moment systems and both parity blocks, while finite flag/trace controls reject the dimension-one inference. These certify control algebra, not the actual analytic theorem. No Lean build/axiom audit, new aperture estimate, actual trace-vanishing proof, RH or F4. Definitions and cursor updated additively. Historical certificates and concurrent aperture work preserved; retained attachment and FULL TRANSPORT CLOSED remain open.
