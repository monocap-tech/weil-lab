# RPB108 NF61: exact continuous kernel and the relative-margin obstruction

Date: 2026-10-08 UTC. Recovered head: c077a9d0f27bd1b1acb51f7b47d31327d5c33455.

No independent arithmetic inequality was found in this step. The new usable result is an exact original-form representation and a countercontrol for a tempting certification shortcut. The complete source gain remains unproved beyond the established interval. Fixed-width smearing stays retired.

## External result and its precise scope

Primary source checked: Masatoshi Suzuki, [Weil's quadratic form via the screw function, arXiv:2606.09096v3](https://arxiv.org/html/2606.09096v3), September 23, 2026. Theorems 1.1 and 1.3 give a Friedrichs realization and lowest-level continuity; Theorem 1.4 gives positivity and simplicity for sufficiently small windows. Sections 8.1–8.5 relate the original form to a continuous compact kernel, with inverse Neumann mass and a generalized eigenvalue problem. Theorem 1.5 constructs real-zeroed characteristic functions after choosing a shift below the original lowest level. Corollary 1.6 requires a conjectural locally uniform limit to infer RH. Section 7 uses positive unshifted forms for its limiting heuristics. These results provide no all-window unshifted lower bound. The shifted real-zeroed function is not the original zeta divisor. The previously audited shifted-inner Suzuki family is a different construction.

The following calculations use our physical Fourier convention and original prime/pole dictionary. They independently derive the representation, the transfer criterion and the error obstruction; the external paper's spectral-limit conjecture is not adopted.

## Exact integration without changing arithmetic

Write m0(xi)=Re psi(1/4+i pi xi)-log pi, w(xi)=log(e+|xi|), and |m0-w|<=C0 as established. Define

    k_arch(t)=integral_R m0(xi)(cos(2 pi xi t)-1)/(2 pi xi)^2 dxi,
    k(t)=k_arch(t)+sum_{n>=2} Lambda(n)/sqrt(n) (|t|-log n)_+
                       -8(cosh(t/2)-1).

The archimedean integral is absolutely convergent: near zero the cosine numerator cancels xi^2, while at infinity the integrand is O(log(e+|xi|)/xi^2). Dominated convergence on bounded t proves continuity. The prime sum is locally finite and continuous. Thus k is real, even and continuous. Distributionally,

    -k'' = archimedean multiplier m0
           -sum_n Lambda(n)/sqrt(n)[delta_(log n)+delta_(-log n)]
           +2 cosh(t/2).

The prime hinge has derivative jumps +1 at each of +/-log n; the factor -8 in the pole therefore matters. On [-a,a]^2 only log n<=2a can enter, including the equality case, whose hinge and supported correlation are both zero. These are the original active prime powers, with their original weights. No averaging, continuum prime replacement or pole rescaling occurs.

Define the **mean-zero derivative carrier** U_a={u in L2(-a,a): integral u=0}. Let Pi_a be its orthogonal projection. The **integrated original kernel operator** is

    C_a=Pi_a [integral_-a^a k(x-y)u(y)dy] Pi_a.

It is self-adjoint and Hilbert–Schmidt. The projection is not the positive source map P_a. For h in H0^1(-a,a), u=Dh=i h' belongs to U_a. Integration by parts gives the EXACT identity

    <C_a u,u>=Q_a(h,h)=||P_a h||^2-||N_a h||^2.

For the arch term, first truncate the xi integral; mean zero kills the subtracted constant and uhat=-2 pi xi hhat. Passage to the limit is justified by H0^1 and |m0|=O(w). Each prime hinge yields -2 Lambda(n)/sqrt(n) Re C_h(log n). The pole yields the original kernel 2cosh((x-y)/2). This also proves the identity for complex h by polarization. No claim that every canonical h has an L2 derivative is made.

## Keep the primitive mass

The inverse of D on U_a is J_a u(x)=-i integral_-a^x u(t)dt. Define the **primitive mass operator** M_a=J_a*J_a. On mean-zero vectors its kernel can be written as -|x-y|/2, or as the projected Neumann kernel

    (x^2+y^2)/(4a)-|x-y|/2+a/6.

Indeed, the raw primitive kernel a-max(x,y) differs from -|x-y|/2 only by separate functions of x and y, which vanish in the mean-zero quadratic form. Consequently

    ||J_a u||_2^2=<M_a u,u>,
    Q_a(J_a u)/||J_a u||_2^2=<C_a u,u>/<M_a u,u>.

M_a is compact, positive and injective; its eigenvalues are (2a/(n pi))^2, n>=1. It has no positive lower bound in the U_a L2 norm.

The **relative kernel margin** C_a>=gamma M_a with gamma>0 is equivalent to Q_a>=gamma||h||_2^2 on the full canonical domain. One direction is restriction. For the other, use the existing form-core density of C_c^infinity in the canonical logarithmic domain, rather than asserting that D maps that whole domain into U_a. Similarly, C_a>=0 is equivalent to nonnegativity of the full original form. The infimum of the displayed generalized quotient is the original attained physical lowest level, but the infimum over U_a need not be attained in U_a.

With the original Garding estimate Q_a>=E_log-B_a||h||_2^2, B_a>=0, a relative margin gives

    Q_a>=gamma/(gamma+B_a) E_log.

Combining this with the bounded complete positive source map gives the NF55 strict original gain bound. This is an exact criterion, not a newly proved margin.

If a positive original eigenvector has level mu and happens to lie in H0^1, then

    <C_a Dh,Dh>=mu<M_a Dh,Dh>,
    <(C_a-mu M_a)Dh,Dh>=0.

For rough eigenvectors these statements are read through smooth form-core approximants. Their derivatives need not converge in L2. Dropping mu M_a would repeat the positive-level/null confusion. Injectivity of C_a on U_a alone does not exclude a kernel in the larger form completion.

## A continuous-kernel control defeats absolute-tail certification

This control is artificial, not an actual zeta form. Set a=pi/2 and let e_n be the normalized mean-zero Neumann cosine basis. Then M e_n=n^-2 e_n. For fixed mu>0 set ell_n=mu+H_n-1, where H_n=sum_{j<=n}1/j. Define

    C^+ e_n=(ell_n/n^2)e_n.

Its cosine-series kernel is continuous because sum ell_n/n^2 converges absolutely and the basis functions are uniformly bounded. The associated generalized physical levels are ell_n: the lowest is mu>0, and the levels tend to infinity logarithmically. At e_1 the shifted form C^+-mu M vanishes although the original form is positive.

For any n, subtract the continuous rank-one kernel

    E_n=-(ell_n+1)/n^2 |e_n><e_n|.

Both its operator norm and Hilbert–Schmidt norm are (ell_n+1)/n^2 ->0. Its uniform kernel norm also tends to zero. Yet

    <(C^++E_n)e_n,e_n>/<M e_n,e_n>=-1.

Every finite prefix below n is unchanged and positive. Thus arbitrarily accurate ABSOLUTE continuous-kernel approximations can conceal a negative original physical level, even with logarithmic growth, compact resolvent in the physical problem, and a strictly positive comparison form. Absolute kernel smoothness or a vanishing Hilbert–Schmidt tail does not supply the relative margin.

An upper/lower certificate must instead control the error relative to M_a, for example |<E u,u>|<=epsilon<M_a u,u>, or use an original canonical-energy complement estimate. Such control reintroduces differentiation/preconditioning and must retain the complete prime arithmetic. No such independent all-window estimate was obtained here.

## Decision and validation

Adopt the exact representation as an available arithmetic formulation. Do not activate the conjectural real-zeroed spectral limit as a proof route, and do not interpret finite positive kernel matrices plus absolute tail bounds as source-gain certificates. The concrete unresolved task is a relative margin for this EXACT kernel beyond a=1, with a mechanism applicable to every finite a. Repackaging the same sign as a compact operator is not progress toward global positivity by itself.

The validator checks exact polynomial primitive/hinge identities, prime-boundary equality, positive-level residuals and rational logarithmic-spectrum rank-one controls. It does not verify an actual zeta spectral bound, external certificate or infinite-dimensional proof. No new certified aperture, original negative vector, RH, F4, full transport or Lean claim. Concurrent aperture/coupled work is preserved.
