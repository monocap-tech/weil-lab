# RPB108: exactly r full negative modes near hypothetical contact

2026-10-07. Recovered head 48b9ba15df5d57e2925db55a30e5490057042537. Definitions: [full contact cluster](../docs/TERMINOLOGY_RPB108_FULL_CONTACT_CLUSTER.md). Conditional actual analytic theorem; not Lean-certified.

## Result

Suppose Q_a is nonnegative with nonzero actual kernel K of dimension r. Then for EVERY sufficiently small positive epsilon,

    n_-(Q_(a+epsilon))=r,
    ker L(a+epsilon)={0},
    lambda_(r+1)(a+epsilon)>=delta/2>0,             (1)

where delta=lambda_(r+1)(a) is the positive physical spectral gap at contact. The translated trial hierarchy supplies the r negative directions; the full resolvent argument below excludes additional negative or zero modes nearby.

The r-dimensional full negative spectral subspace converges to K in physical projection norm. Suitable physical orthonormal cluster frames converge in the canonical domain, and therefore in the COMPLETE original actual source norm. This closes the distinction between the finite translated trial index and the full nearby index. It does not turn trial upper rates into matching full branch asymptotics, provide a numerical gap, or exclude the starting contact.

## 1. Existing form continuity and the physical resolvent dictionary

The pinned ACTUAL_FIRST_CONTACT_CONSTRUCTOR already proves that after mass-unitary dilation U_b:D_1->D_b, q_b has a norm-continuous bounded canonical Riesz family A(b)=I+compact. Its finite prime threshold activations are continuous: zero overlap at the threshold gives a zero compressed form. No new prime is omitted here.

On a fixed compact positive aperture neighborhood, the full native Gårding estimate is uniform. The dilated logarithmic norm is uniformly equivalent to the registered D_1 norm, and the finite prime/pole physical corrections are uniformly bounded. Choose beta>0 large enough that

    B(b)=A(b)+beta J^*J>=kappa I_D1,
    kappa>0,                                      (2)

throughout this neighborhood. This is a positive shifted FORM norm. The shift is beta times PHYSICAL mass, not beta times the canonical identity.

For physical f in L2(-1,1), the weak equation B(b)u=J^*f says q_b(u,v)+beta<Ju,Jv>=<f,Jv> for every v in D_1. Therefore its physical solution Ju is exactly the shifted physical resolvent applied to f:

    R(b)=J B(b)^(-1)J^*.

The compact inclusion makes R(b) compact, positive and self-adjoint. Smooth core density makes the physical operator well-defined with dense form domain. This dictionary does not impose physical operator-domain membership on an arbitrary canonical vector.

The inverse identity and (2) give

    ||R(b)-R(a)||_L2
      <=||J||^2 kappa^(-2)||A(b)-A(a)||_D1 ->0.     (3)

Thus the already established bounded FORM continuity now has an explicit norm-continuous PHYSICAL resolvent attachment. These are different operators and inner products; the mass factor M is indispensable.

## 2. Isolated full physical cluster and exact nearby negative index

At contact, the compact positive resolvent's largest r eigenvalues equal 1/beta; the next is 1/(beta+delta), with delta>0. The gap is positive because compact physical inclusion gives a discrete native spectrum tending upward to infinity, while the zero eigenspace is exactly K.

Compact self-adjoint min-max bounds each ordered resolvent eigenvalue difference by ||R(b)-R(a)||. Using (3) and converting lambda=1/rho-beta proves continuity of each fixed low physical eigenvalue. In particular lambda_j(b)->0 for j<=r and lambda_(r+1)(b)->delta as b->a. Therefore lambda_(r+1)(b)>delta/2 for b sufficiently close to a.

NF51/NF53 already construct r strict negative directions for every b>a, using changed translated physical trials. Thus lambda_r(b)<0 for those b. Monotonic ordering and the positive (r+1)st value give exactly (1): no additional negative modes and no zero eigenvalue in this sufficiently small right neighborhood.

The constants and neighborhood are conditional and non-effective. This is not a new aperture certificate or a computed gap. For apertures farther from a, more spectral modes can cross zero; no global index bound is asserted.

## 3. Physical spectral projection convergence

The r largest eigenvalues of R(b) stay separated from the rest by a fixed positive gap near a. Norm convergence (3) implies norm convergence of their finite-rank spectral projections to the 1/beta eigenspace projection. One can verify this directly by compactness and the gap: bounded vectors in the cluster have subsequential physical limits in K, and dimensions remain r; applying the same statement to orthogonal complements excludes a projection defect. Equivalently the usual isolated finite spectral contour inverse identity gives the same result.

For b>a these projections are precisely the full negative physical spectral subspace projections. This is first a statement on the fixed dilated mass carrier L2(-1,1).

On the ambient physical line the projection is U_b P_tilde(b) U_b^*. Dilation is strongly continuous but is not presumed operator-norm continuous on the full physical space. Its action is norm-continuous on the finite-dimensional image of the limit projection; combine that fact with convergence of P_tilde(b) to obtain ambient physical projection-norm convergence to P_K. No norm continuity of the entire dilation group is assumed.

## 4. Canonical-domain and complete actual-source convergence of frames

Choose physical orthonormal eigenvectors from the r-mode cluster in the fixed dilated carrier along any sequence b_n down to a. Their eigenvalues tend to zero. The uniform shifted coercivity (2) bounds their D_1 norms. Pass to a weak D_1 subsequence; compact J makes their mass limits strong and preserves physical orthonormality. Form continuity implies q_a(f_n,f_n)->0.

Since q_a>=0, its bounded-form Cauchy-Schwarz forces every weak limit into ker A(a). The limit has physical mass one. Moreover

    q_a(f_n,f_n)+beta||Jf_n||^2 -> beta
       =q_a(f,f)+beta||Jf||^2.

Weak convergence together with convergence of this positive equivalent Hilbert norm proves strong D_1 convergence. Simultaneously for the finite frame, the limits form an orthonormal basis of the entire contact kernel. This proves convergence in the canonical topology, not just in physical mass.

Individual eigenvectors need not have a unique limit when the contact is degenerate. To get a full-neighborhood frame, project a fixed kernel basis into the nearby negative subspace and orthonormalize its physical Gram. Projection convergence makes that Gram nonsingular; the preceding compactness argument gives strong D_1 convergence after this unitary alignment. The aligned frame may not diagonalize the physical operator.

Return to a common fixed larger D_B on the physical line. Dilation is strongly continuous in the logarithmic norm, as follows from smooth density and the uniform compact-aperture logarithmic weight bounds. Thus these actual frames converge in D_B to their contact basis. Bounded complete analysis Gamma on D_B gives convergence of ALL original source coordinates in the complete positive source metric. Divisor copies and normalization weights are unchanged on support inclusion.

In an aligned physical orthonormal frame v_i(b), the exact full signed source Gram is

    <Gamma(v_i(b)),J_source Gamma(v_j(b))>=E_ij(b),

where E(b) is the negative Hermitian compression of the native physical operator and E(b)->0. It need not be a scalar or diagonal matrix. This residual is retained before taking the limit; the nearby vectors are negative modes, not zero-null vectors at their own apertures.

## 5. Shifted actual positive-eigenmode control

At a positive lowest level mu of multiplicity r, apply the argument to Q_mu. The isolated cluster consists of r eigenvalues near mu, all below mu in every sufficiently close strict enlargement by NF53. Continuity also keeps them above mu/2>0 for sufficiently small enlargement. Thus they open downward RELATIVE to mu while remaining positive in the original actual form.

The next full level stays separated above mu by a positive gap. A cluster frame's original full source Gram is mu I+E_mu(b), with E_mu(b) negative and tending to zero, not E_mu(b) alone. This actual control confirms that the local cluster and convergence arguments are not zero-specific arithmetic exclusion theorems.

## Standing and validation

The complete nearby index is now exactly the contact multiplicity; the uncontrolled complement cannot supply an extra near-zero negative mode in the small neighborhood. Trial Ritz upper bounds remain the only established odd-order rate bounds on the full negative cluster. Matching lower rates and an exact full domain derivative remain unproved.

Canonical and complete-source convergence does not give height-uniform signed sharp estimates; NF50's nonuniform height limit audit remains in force. No arithmetic sign bound, initial actual contact exclusion, same-vector enlarged full-null transport, F4 or full transport is established. Whole-domain aperture-one positivity and historical work are preserved.

The exact finite checker validates mass-shifted inverse resolvent identities, isolated-cluster eigenvalue gap budgets, exact r-mode counting in independent finite controls and the original shifted source residual. It does not certify the analytic compactness/convergence theorem, compute actual native eigenvalues or supply a numerical spectral gap. Dependencies are pinned in the companion manifest; no new external theorem, Lean file/build or axiom is added.
