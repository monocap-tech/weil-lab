# RPB108: physical contact trials open at odd orders after positive remainder elimination

2026-10-07. Recovered head e23adbbc8ceebac5b67d359dcf6dd88cd0d477c9. Definitions: [contact trial hierarchy](../docs/TERMINOLOGY_RPB108_CONTACT_TRIAL_HIERARCHY.md). Conditional actual analytic result; not Lean-certified.

## Result

For a hypothetical r-dimensional actual nonnegative contact kernel, finite Taylor translation remainders give a positive r-dimensional physical trial space whose mass-normalized Ritz values are all log(1/t)[1+o(1)]. Eliminating that space leaves an r-dimensional negative graph trial space converging in physical mass to K. Its negative Ritz values, ordered from most negative to least negative, satisfy

    rho_j(t)=-Theta(t^(2j-1)), 1<=j<=r.             (1)

After centering, these changed physical trials fit aperture a+t/2. Hence the corresponding enlarged full eigenvalues obey upper bounds lambda_j(a+t/2)<=-b_j t^(2j-1) for fixed conditionally positive b_j and small t. No matching lower bounds or full spectral branch asymptotics are proved. Constants depend on the actual kernel; none is numerically computed.

The negative effective energy matrix has the explicit scaled limit

    E_negative(t)=-(|c|^2 t/2) D_t[U+o(1)]D_t.      (2)

This upgrades the preceding determinant/inertia result to physical trial rates. It remains a consequence of contact, not an exclusion of contact. The shifted actual positive-eigenmode control has the same hierarchy relative to mu and retains its physical mass residual.

## 1. Taylor subtraction stays within the actual chain

Use the real derivative-chain basis and T_t,R_j from the registry. The actual form vanishes on K against K. Thus Q(e_j,R_k)=C_jk(t), where C is the original translated cross matrix, and Q(T_t e_j,T_t e_k)=0. Simultaneous translation also gives Q(tau_t e_j,tau_t e_k)=0. Consequently the exact remainder Gram is

    B(t)=-(T_t C(t)+(T_t C(t))^T).                 (3)

All matrices are real for the chosen real chain. Complexification gives the same Hermitian identities and dimensions. The source interpretation retains every original actual row and weight.

The pinned NF51 formula is C(t)=|c|^2 t D_t[A+o(1)]D_t. Its multiplication by the finite Taylor matrix is exact at each scale. The elementary partial-binomial identity

    sum_(q=0)^n (-1)^q/[q!(m-q)!]
                         =(-1)^n/[m n!(m-n-1)!], n<m,

applied with n=n_j and m=n_j+n_k+1 gives

    T_t C(t)=-|c|^2 t D_t[H+o(1)]D_t,
    B(t)=2|c|^2 t D_t[H+o(1)]D_t.                 (4)

H is the positive L2(0,1) Gram matrix of the independent polynomials (-1)^j s^n_j/n_j!. Therefore B(t)>0 for every sufficiently small t. The scaled remainders tend to zero entrywise for fixed r; no dimension-uniform bound is claimed.

## 2. Exact physical mass of all remainders

Let g=e_(r-1). For n=n_j>=1, lawful repeated translation differentiation through the regular primitives gives the global physical identity

    R_j(t)=(-1)^n/(n-1)! integral_0^t
                           (t-s)^(n-1)(tau_s g-g)ds. (5)

For n=0 it is simply tau_t g-g. This is an L2 Bochner integral. No derivative of g is taken.

On the common support overlap [-a+t,a], every difference in (5) is restricted to a subset of its own overlap [-a+s,a]. NF52 proved that the squared mass of tau_s g-g on that overlap is o(s/log(1/s)). Minkowski and the uniform small-s bound imply that R_j has overlap norm o(t^(n+1/2)/sqrt(L)). For instance replace the little-o factor by any fixed eta below a sufficiently small t and integrate s^(1/2)(t-s)^(n-1)/sqrt(L); then send eta to zero. This makes the error uniform enough for (5), without a pointwise trace assumption.

On the two nonoverlap strips, strong rescaled terminal traces and their regular primitive consequences give in L2(0,1)

    sqrt(L) R_j(a+t u)/t^n
                  ->(-1)^n c(1-u)^n/n!,
    sqrt(L) R_j(-a+t u)/t^n
                  ->-sigma(-1)^n c(1-u)^n/n!,

where sigma is the terminal left/right parity sign. The left formula follows by the exact finite polynomial Taylor sum; its terminal term uses strong L2 trace, and the others use the integrated primitive traces. There is no asserted pointwise expansion of the terminal g.

Taking pairings on the two strips, and using the lower-order overlap norms, proves the physical remainder mass matrix

    M_R(t)=(2|c|^2 t/L) D_t[H+o(1)]D_t.           (6)

Comparison of (4) and (6), after the invertible diagonal scaling, shows that ALL r physical Ritz values on span{R_j} divided by L tend to one. This concerns the positive remainder trial space only. It is not a lower bound on the full enlarged operator's positive spectrum.

## 3. Negative Schur graph with a nondegenerate physical limit

The complete energy Gram in the actual family (e_j,R_j) is

    [[0,C(t)],[C(t)^T,B(t)]].                      (7)

Since B(t)>0, for each real old-kernel coefficient vector x choose the physical trial

    v_t(x)=sum_j x_j e_j+sum_j y_j R_j(t),
    y=-B(t)^(-1)C(t)^T x.

Its exact energy matrix is E_negative=-C B^(-1) C^T. Using (4) gives

    E_negative=-(|c|^2 t/2)
                       D_t[A H^(-1) A^T+o(1)]D_t. (8)

The scaled coefficient relation is D_t y=O(D_t x), and (6) implies the correction's physical norm is O(sqrt(t/L)||D_t x||). In particular it tends uniformly to zero for bounded fixed x. Hence v_t(x) converges to sum x_j e_j in physical L2, and its physical mass Gram tends to the positive definite old-chain mass Gram M_K. The negative graph is r-dimensional and its mass is not degenerate in this basis.

## 4. Reflection identity gives the explicit effective Gram

Let chi_j(s)=s^n_j/n_j!, psi_k(s)=(-1)^k s^n_k/n_k!. The elementary beta polynomial integral gives

    A_jk=(-1)^r integral_0^1 chi_j(1-s)psi_k(s)ds.

The psi_k span all polynomials of degree below r. Reflection s->1-s preserves their L2 space and norm. Expanding the reflected chi_j in that basis and using its positive Gram H gives

    A H^(-1) A^T=U.                               (9)

This is a finite polynomial identity, not an imported transform theorem. Equations (8)-(9) prove (2). Equivalently the leading negative energy is minus |c|^2 t/2 times the L2(0,1) squared norm of sum_j x_j (t s)^n_j/n_j!.

## 5. Physical negative trial rates and min-max scope

U is positive definite, so U+o(1) is bounded above and below by positive fixed multiples of the identity for small t. The negative graph's physical mass tends to M_K>0 and is likewise uniformly comparable to coefficient Euclidean mass. Therefore the positive matrix -E_negative, after physical mass normalization, has ordered eigenvalues comparable to those of t D_t^2. Those orders are t,t^3,...,t^(2r-1), proving (1).

Simultaneously translate the complete family by -t/2; all form and mass pairings are unchanged and the trials fit [-a-t/2,a+t/2]. The physical operator associated to the complete native form has the retained compact embedding/discrete variational spectrum. Min-max applied to the r-dimensional graph gives the stated upper bounds on its first r eigenvalues. It does not show that these are the ONLY negative eigenvalues, identify matching full spectral rates, or provide a quantitative lower bound on any b_j independent of K.

In particular the leading effective matrix is rank one at order t; more regular directions open at higher odd orders after elimination. This is compatible with the rank-one terminal trace and the earlier r-negative-direction inertia. The large positive remainder energies are fully retained during the elimination.

## 6. Shifted control and remaining gate

For the actual lowest positive eigenspace, carry out the same construction with Q_mu. Its physical remainder mass is unchanged and its shifted energy matrices obey (3)-(9). In the original complete source form every trial Gram is Q_mu_Gram+mu times its PHYSICAL mass Gram. Thus the negative graph Ritz levels are mu-Theta(t^(2j-1)) and the positive remainder levels are mu+L[1+o(1)]. The corresponding min-max bounds are relative to mu and do not force negative original energy at small t.

The construction changes the physical vector and support. It supplies neither same-vector enlarged nullity nor actual contact existence. No fixed finite source deletion or selected-background covariance is substituted for the complete actual form. Whole-domain aperture-one positivity and historical records remain preserved.

The local trial hierarchy is now physically normalized, but excluding its hypothetical starting kernel still requires the unproved zero-specific arithmetic estimate. Signed sharp-head exclusion, global endpoint exclusion, F4 and full transport remain open. No RH or Lean closure is claimed.

## Validation

The finite exact checker verifies the partial-binomial sums, positive polynomial Gram minors, A H^(-1) A^T=U, remainder energy matrices and exact negative Schur factorization for rational model scales, with the original shifted mass residual retained. These are algebra audits, not analytic certification of (5)-(6), actual kernel computation, full spectral approximation, or a Lean proof. Actual chain, correlation, strong traces, physical translation scale and variational architecture are pinned in the custody manifest. No new external theorem is imported.
