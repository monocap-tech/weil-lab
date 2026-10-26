# Complete original prime-power mixed coupling on J470 and normalized SI29

**October 26, 2026. W-ODD-NEG remains OPEN.** This computes one complete original operator component of the missing mixed matrix. It is not the complete Astar mixed matrix, an energy projection, or a matched Schur response value.

## GitHub custody and unchanged trial

Base: PR #336 at b24e57ed4bd9eb687008ea03aa73f42f6dcbc180, successful focused Actions 40419084302. Its normalized actual 14D energy-Schur enclosure (99/100001)I <= T_A <= 44I remains conditional original inverse information, not an evaluated response. The canonical manifest still selects W-ODD-NEG, OPEN.

Reuse the physical projection X=(J*J)^-1 J*F and exact dyadic C from successful native Actions 40385192745, builder ab41a96861c9e5d0623807e40d53482985d143bc, artifact 12679609974. Archive SHA256 243d40e1fc7d7ce349a0c16c809f06eea0593cd91635d6966241e4f5f478cf33; JSON si29_full_J_L2_normalization.json SHA256 c9ee487f8abe7b633c47d2ef7d72e2cc4f7289bc794b2d8fc02bb61520b25e60. The focused workflow verifies run/source/artifact/archive/JSON custody before computation.

The original 470 sources include all 469 original b9 sine/polynomial-cosine generators and the pole. F contains all fourteen ACTUAL continuous SI29 means/first moments. With Phi=[J,F], use

    W=(I-P_J)FC=Phi Qc,   Qc=[-X;I]C.

Here X denotes the exact physical projection solve enclosed by its native balls. It is not an independent uncertain change of problem. W is unaligned and is not the Astar-energy-projected representative. No new full physical projection solve is performed.

## Eliminate the entire frequency quadrature for this component

The retained prime-power multiplier is

    p(xi)=-2 sum_(n,p) log(p)/sqrt(n) cos(2*pi*xi*log(n)),
    (n,p)=(2,2),(3,3),(4,2),(5,5),(7,7),(8,2),(9,3).

These are seven retained terms, including powers of the same prime. For a=log(n), Fourier translation and physical zero extension give

    P_n g(x)=-log(p)/sqrt(n) [g(x+a)+g(x-a)],

where g is zero outside [-B,B], B=11/10. Since 0<a<2B and every original source/feature is odd, BOTH translation overlaps have the same integral. Reflection x -> -a-x also interchanges the two odd factors. Therefore the COMPLETE physically supported mixed block is

    (J*Pprime W)_ij
       =-2 sum_(n,p) log(p)/sqrt(n)
                    integral_(-B)^(B-log(n)) W_j(x) J_i(x+log(n)) dx.

The factor 2 pays the two translations; it is not an extra Fourier-frequency symmetry factor. The clipped endpoints enforce the original support exactly. No frequency cutoff or Fourier tail payment is needed for this entire component.

The orientation is chosen deliberately: translate J, whose generators have nonnegative polynomial powers, and leave the actual continuous F unshifted. Translating its Laurent representation would introduce different removable denominators. Instead expand each translated original polynomial sine/cosine/pole by the exact binomial and trigonometric addition identities.

## Closed-form clipped integrals and regularization

Use product-to-sum with its factor 1/2 on the ASYMMETRIC physical interval. Unlike a reflected full-interval Gram, this factor does not disappear. Nonnegative polynomial trigonometric moments follow ordinary integration-by-parts recurrences with exact zero-frequency branches.

The inherited actual continuous features have Laurent powers down to -2, with removable singularities at zero. Define entire regularized primitives consistently:

    integral (sin(wx)/x) dx = Si(wx),
    integral ((cos(wx)-1)/x) dx = H(wx),
    H(t)=Ci(t)-log(t)-EulerGamma,
    integral ((cos(wx)-1)/x^2) dx = (1-cos(wx))/x-w Si(wx),
    integral ((sin(wx)-wx)/x^2) dx = (wx-sin(wx))/x+w H(wx).

H is ENTIRE and EVEN; evaluate the individual Ci/log expressions on the half-plane with nonnegative real argument, using |x| and canonical frequency sign, to avoid a negative-real branch cut. All endpoint intervals are separated from zero, including the small B-log(3) endpoint. The sum defining each actual feature times a translated source is entire, so all subtracted negative Laurent coefficients cancel EXACTLY in the complete expression. Linearity of these consistently regularized integrals consequently gives the ordinary integral of that entire product. No divergent term is numerically integrated across zero.

The prototype and workflow evaluate at 4096 bits with pinned python-flint 0.8.0. For each of the seven shifts:

- Independent degree-255 entire-power integrals check both trigonometric kinds at powers -2,-1,0,1,5,15, with complex frequency and explicit tail payment. This checks the new Ci primitives and both asymmetric endpoint signs.
- Direct binomial/trigonometric translation identities check the first source, order-14 source, last original source and the pole. Odd clipped-reflection symmetry is checked independently before exploiting it on J/J.
- Independent degree-255 ENTIRE Taylor products check ALL fourteen actual continuous feature integrals against the translated original first sine and pole on the WHOLE clipped interval. Explicit product-tail bounds cover the entire interval. These checks use no Laurent primitives and retain the first-moment features.
- Compute the whole 470x484 clipped raw matrix, using exact odd reflection to fill its symmetric J/J block. Multiply by the SAME Qc and sum all seven weighted 470x14 matrices. No source column, feature column or offdiagonal mixed entry is dropped.

## Joint mixed-matrix uncertainty and replay

Retain all 6580 final matrix-entry balls. Their dyadic centers form an exact matrix M0; if r_ij are their outward radii, then

    ||J*Pprime W-M0||_2 <= ||entrywise radius||_F
                         <= epsilon,
    epsilon^2 >= sum_ij r_ij^2.

The final sum and a dyadic epsilon are composed with exact Fractions. This is a COUPLED bilinear error: for arbitrary coefficient vectors u,v it bounds the mixed error by epsilon ||u|| ||v||. Entrywise intervals are not silently treated as a PSD matrix. The source-side coefficient norm is that of the ORIGINAL raw J coordinates; any later source preconditioner must propagate this error through its actual congruence. The full balls and exact radius sum are retained for that purpose.

A separate standard-library checker verifies all dimensions, all seven prime powers, each native log/weight ball against inherited exact SI06 rational enclosures, all 6580 radii, the joint error composition and scope flags. Native input validity, the analytic translation/regularization proof, arithmetic CI, and independent original analytic/domain review remain separate.

## Remaining mixed terms and proof standing

For the original positive multiplier a=max(kappa,m), a=m+Kminus pointwise. Thus, on this physical residual family,

    J*Astar W = J*H_arch W + J*Pprime W + J*Kminus W,

because s*W=0 EXACTLY and the pole belongs to J. The constant -log(pi) part of H_arch also has zero mixed action since J*W=0. Only the COMPLETE middle term is computed here. The archimedean and original negative-multiplier mixed blocks remain uncomputed. No negative action is claimed invariant under adding J functions.

This result supplies actual full-source covariance information needed by the normalized energy-projection/forcing calculation. It does not test or infer positivity from another finite source count. Actual complete Astar entries, its energy projection, matched forcing, the 14D inverse response value, full signed exceptional Schur and infinite-operator transfer remain OPEN. W-ODD-NEG, independent original domain/analytic review, even/CC27/Weil/RH remain OPEN. Draft/unmerged, stacked on PR #336.
