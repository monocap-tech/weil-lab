# RPB108: full contact multiplicity opens into negative directions on enlargement

2026-10-07. Recovered head 2ae3bc383d38bf245ab137cbcb6799cd59ee0dba. Definitions: [translated kernel index](../docs/TERMINOLOGY_RPB108_TRANSLATED_KERNEL_INDEX.md). Conditional actual analytic result, not Lean-certified.

## Result

If a hypothetical actual nonnegative contact kernel at aperture a has dimension r, EVERY strictly larger window has negative index at least r. This improves the previously recorded existence of one translated negative trial. The actual derivative chain gives the exact small-translation cross determinant

    det C(t)=(-1)^r |c|^(2r)
                 [product_(j=0)^(r-1) j!/(r+j)!] t^(r^2)
                    +o(t^(r^2)),                    c!=0. (1)

Consequently the complete translated kernel Gram has precisely r positive and r negative directions for all sufficiently small t>0. These are original actual native/source pairings, not selected-background or artificial comparison rows.

The same construction gives the quantitative ONE-SIDED physical Rayleigh bound

    lambda_min(a+epsilon)<=-Lambda_K epsilon+o(epsilon),
    Lambda_K>0.                                      (2)

No equality, differentiability, lower spectral bound or effective numerical floor for Lambda_K is proved. The actual lowest positive eigenspace has the corresponding shifted statements, with lambda_min(a+epsilon)<=mu-Lambda_(K^mu)epsilon+o(epsilon). This is a domain-enlargement consequence, not arithmetic contact exclusion or same-vector null transport.

## 1. Integrate the already proved terminal correlation through the chain

The pinned NULL_ABEL_LOG_SLOPE theorem proves for the terminal vector e_(r-1)

    Q(e_(r-1),tau_t e_(r-1))=-|c|^2 t+o(t), t down to0. (3)

Let F(t)=Q(h_*,tau_t h_*), defined for t in a fixed small interval using a fixed larger canonical window. Since h_* has lawful canonical derivatives through r-1, F has derivatives through 2r-2. Derivatives can be distributed between the two arguments by the established full-native skew identity; translation differentiation contributes -D on the second argument. Hence

    C_jk(t)=(-1)^k F^(j+k)(t), 0<=j,k<r.          (4)

For every order m<=2r-2, choose j+k=m with both indices below r. The original full mixed nullity yields F^(m)(0)=0. The highest derivative is

    F^(2r-2)(t)=(-1)^(r-1) C_(r-1,r-1)(t)
               =(-1)^r |c|^2 t+o(t).              (5)

Repeated ordinary integration from zero, using these zero initial derivatives, gives

    C_jk(t)=(-1)^(r+k) |c|^2
                  t^(2r-1-j-k)/(2r-1-j-k)!
                      +o(t^(2r-1-j-k)).           (6)

The differentiations here never differentiate the rough terminal vector. They use only the regular generator's canonical derivatives up to r-1 in each form argument. Equation (3) supplies the final one-sided Lipschitz asymptotic. No unproved pointwise endpoint expansion or derivative beyond the chain is used.

## 2. Nonzero reciprocal-factorial determinant

Factor t^(r-1-j) from row j, t^(r-1-k) from column k, and one further t from the matrix. The total determinant power is r^2. The remaining leading matrix has entries (-1)^(r+k)|c|^2/(2r-1-j-k)!.

Reversing both row and column orders reduces its unsigned reciprocal-factorial part to H_ij=1/(i+j+1)!, 0<=i,j<r. Its determinant is

    det H=(-1)^(r(r-1)/2) product_(j=0)^(r-1) j!/(r+j)!. (7)

To verify (7) without an outside determinant theorem, multiply column j by (r+j)!. Row i becomes the polynomial product_(ell=i+2)^r (j+ell), of degree r-1-i and leading coefficient one. Reverse the row order to ascending degrees and evaluate at j=0,...,r-1. The determinant is the Vandermonde product product_(j=0)^(r-1) j!. Reversing rows gives the displayed sign. Include the signs (-1)^(r+k) in (6); their combination gives (-1)^r. This proves (1).

Entrywise remainders in the factored matrix tend to zero, so the determinant leading coefficient is genuinely nonzero. No uniform conditioning as r varies is asserted.

## 3. Complete translated Gram and r negative physical directions

Simultaneous translation preserves the global full native form. Each original chain vector is full-null on its original window, so both within-chain Gram blocks are zero. The cross block is C(t). Thus the full Gram is

    G(t)=[[0,C(t)],[C(t)^*,0]].                    (8)

For small t, C(t) is invertible by (1). The matrix (8) has eigenvalues +sigma_i(C) and -sigma_i(C), hence exactly r of each sign. Equivalently the congruence with an invertible cross block reduces it to [[0,I],[I,0]]. This is a form inertia statement.

The 2r physical vectors are independent: a physical relation would lie in the nullspace of their Gram, but (8) is nonsingular. Consequently their negative coefficient subspace realizes an r-dimensional negative PHYSICAL subspace. The coefficient Gram's eigenvalues must not be described as eigenvalues of the mass-normalized native operator; its physical mass Gram depends on t and degenerates as t->0.

Apply simultaneous translation by -t/2. The entire family is then supported in [-a-t/2,a+t/2], with unchanged Gram. Given any b>a, choose t<2(b-a) sufficiently small. This puts r negative directions in D_b, proving n_-(Q_b)>=r. The existing identity-plus-compact architecture keeps the negative index finite at each fixed window; it is compatible with this lower bound.

Nothing here constructs an actual contact kernel or contradicts its possible existence. Contact followed by strict negativity in larger windows remains logically consistent.

## 4. One-sided linear opening of the lowest Rayleigh quotient

On finite physical K, the trace functional has squared norm Lambda_K. Choose physical mass-one h in K attaining |kappa_R(h)|^2=Lambda_K>0. Let

    w_epsilon=tau_(-epsilon)h+tau_(epsilon)h.

This changes the vector and puts its support in the enlarged symmetric window. Translation invariance and (3), now using the established full-kernel mixed correlation for h, give

    Q(w_epsilon,w_epsilon)
         =2 Re Q(h,tau_(2epsilon)h)
         =-4 Lambda_K epsilon+o(epsilon).

Strong physical translation continuity gives ||w_epsilon||_2^2=4+o(1). Divide to obtain (2) by the variational definition of lambda_min. The remainder is for the fixed maximizing h, not uniform in aperture or kernel dimension.

This is only an upper bound: limsup_(epsilon down to0) lambda_min(a+epsilon)/epsilon<=-Lambda_K. No matching lower bound, full shape derivative or optimized negative trial is asserted. In particular Lambda_K is nonzero conditionally, but no computed numerical transversality floor is supplied.

## 5. Shifted actual positive-eigenmode control

Use Q_mu=Q-mu physical mass on its nonnegative lowest-eigenspace contact. Full translation invariance, derivative skew and the same chain/terminal asymptotics hold for Q_mu. Thus its C_mu(t) has (1), its finite Gram has r negative directions, and every strict enlargement has at least r physical spectral directions BELOW mu, by min-max. They need not be below zero.

For the centered symmetric trial,

    Q(w_epsilon)=Q_mu(w_epsilon)+mu||w_epsilon||_2^2,

so its physical Rayleigh quotient is mu-Lambda_(K^mu)epsilon+o(epsilon). The original full signed actual source Gram on the translated family is G_mu(t)+mu M_physical(t), not G_mu(t). Retain that residual on every block.

The existing actual positive control therefore has the same quantitative opening relative to its positive level. This prevents promoting the opening theorem into a zero-specific arithmetic contradiction. Fixed finite source-coordinate restoration and selected-background forms retain their historical custody; no derivative or translation law is transferred to an altered form.

## Standing and validation

The local enlargement graph gains full multiplicity and an explicit one-sided physical slope. The original same physical vector remains diagonal-zero after enlargement but is not full-null there. The new negative subspace uses translated, changed vectors. The final global obligation remains exclusion of the initial actual contact, through a zero-specific arithmetic bound; it is not supplied by the negative directions after contact.

Whole-domain aperture-one positivity and historical custody remain preserved. No actual negative vector at a certified aperture, computed contact, global positivity, RH, F4, full transport or Lean closure is claimed.

Exact rational checks audit reciprocal-factorial determinants, the r^2 powers, integration signs and invertible-block inertia congruences, plus the shifted mass residual. They certify finite algebra only. The analytic differentiation, trace asymptotics, translation support and variational steps are documented above and pinned separately; no new external theorem is imported.
