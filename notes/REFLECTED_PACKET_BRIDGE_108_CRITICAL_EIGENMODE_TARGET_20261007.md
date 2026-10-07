# RPB108: actual positive eigenmode fails the critical moment and signed target

Date: 2026-10-07 UTC. Recovered live head 41c6f32cd24b17fbc89c992d965988e047df21f8.
Definitions: [critical eigenmode and signed contact target](../docs/TERMINOLOGY_RPB108_CRITICAL_EIGENMODE_TARGET.md).
Category: endpoint exclusion / actual critical source obstruction.
Analytic shifted promotion and actual-control consequence. No independent arithmetic bound or Lean certificate.

## Result

The new reciprocal critical promotion is stable under a real scalar eigenvalue shift:

    K_a^mu intersect Xcrit=K_a^mu intersect H1(R),
    h in that intersection -> h' in the same K_a^mu.        (1)

Consequently the previously established physical mass-one rough positive eigenmode at a=24/25, mu>=3e-29>0, has

    M_(+,1)(h)=+infinity,
    I_(epsilon,1)(h)->+infinity.                           (2)

Its genuine critical exterior flux integral diverges to -infinity. This settles the critical order-one moment of that same actual control, previously left undecided. It is an actual full native eigenmode with all prime, pole and divisor custody, not the cusp control or an artificial coordinate sequence.

For the actual zero-contact route, the sufficient signed target can now be taken at the exact critical order:

    liminf_(epsilon down to 0) I_(epsilon,1)^K<infinity
        -> K_a=0.                                        (3)

Neither the premise in (3) nor whole-contact-kernel critical membership has been proved. The lower translation-scale weight may be easier to estimate, but on the actual kernel it has the same logical exclusion strength as the older supercritical criterion. This pass does not call that reduction an arithmetic estimate.

## 1. Audit and exact scalar shift of reciprocal promotion

The zero proof was audited at the recovered head for finite-jump domination, canonical Dirichlet form custody, boundedness before boundary-theorem use, exact pole convolution, both unprojected reciprocal pairings, full exterior strips and critical endpoint removal. No defect was identified in those steps.

For mu real, the shifted form is the actual Riesz operator A-mu J*J, self-adjoint I+compact. Its physical kernel K_a^mu is finite-dimensional. Choose smooth compact forcing f physically orthogonal to this entire eigenspace. The Fredholm inverse solves

    q_u-mu u=f on I_a.

The pole-free operator in the previous proof becomes B_a-mu. Its nonnegative jump symbol is unchanged; only the constant in its semigroup is mu_a-mu. The forced equation is

    (B_a-mu)u=f-p_u,

with bounded right side, so the same time-one semigroup argument proves boundedness of u. No norm-uniform statement as mu or a varies is made.

Localization gives

    m0(D)(chi u)=chi[f+T_full u-p_u+mu u]+[m0(D),chi]u.

All terms are bounded. The same pinned logarithmic boundary theorem therefore gives inverse-square-root-log physical decay. The exterior shifted residual equals the unshifted exterior residual and has at most square-root-log growth.

For h in K_a^mu intersect Xcrit, the critical interior gain has the additional bounded-on-Xcrit term mu h. Thus the earlier interior log^3 and endpoint conclusions hold. The localized shifted residual belongs to Ecrit and is zero on I_a. The critical dual Hardy estimate and signed Carleman matching proof are unchanged; at the boundary h tends to zero. Hence q_h^mu extends continuously to zero there, while the physical critical Hardy tail tends to zero.

Scalar mass, all actual prime translations and the Hermitian pole commute with convolution and distributional differentiation. With h_epsilon the same compact mollification test as before,

    <q_(h_epsilon')^mu,u>=<h_epsilon',q_u^mu>.

The left side tends to zero by the matched shifted residual modulus and bounded u. The right exterior part tends to zero by the critical physical Hardy tail times the square-root-log upper residual. Its interior part tends to -<h,f'>. The finite-codimension annihilator of smooth tests orthogonal to K_a^mu identifies h' with a vector of that eigenspace on I_a; Zcrit excludes the remaining endpoint-supported distribution globally. This proves (1).

This is genuine use of the shifted full homogeneous equation, not the assertion q_h=0 for a positive eigenmode. The forcing inverse need not be Xcrit. The zero proof's rejected generic critical inverse premise is not restored.

## 2. Critical divergence of the retained actual positive control

The pinned actual supercritical control already supplies the mass-one physical h outside H1 at a=24/25 with mu>=3e-29. It is one actual member of the lowest physical eigenspace, chosen through the established finite-dimensional derivative obstruction. No eigenvector coordinates are computed here.

If its order-one positive source moment were finite, the general actual source/Fourier comparison would put h in Xcrit. Equation (1) would then put the same h in H1, contradicting that control's custody. Thus M_(+,1)(h)=+infinity.

All source orders below one, both channels, remain finite from the shifted subcritical bootstrap. The critical trace of its full finite lowest eigenspace is also infinite: whole-eigenspace critical finiteness would put every basis vector in H1; differentiation would be an endomorphism and polynomial-Fourier independence would force the eigenspace to be zero. We do not assert critical divergence for every vector of a degenerate eigenspace.

More generally, every nonzero actual finite eigenspace has infinite critical positive trace by this same argument. This does not imply that an actual zero eigenspace exists.

## 3. The transverse remainder is integrable at r=1, including the actual control

Take B=3/8 and s=1/4 in the pinned joint source bound. Write V=||p||^2+||n||^2 and M_+,M_- for the two half-height subcritical moments. Then

    integral_0^t0 |R_h(t)|dt/t^2
       <= exp(3t0/8)[(9/128)V t0
                         +(3/2)sqrt(M_+ M_-)sqrt(t0)]
       <infinity.                                        (4)

All inputs are derived for the actual shifted eigenmode or hypothetical full-null vector. The cross exponent leaves margin 1/2. The sharper transverse strip improves these constants; it does not control the critical ordinate moment.

At every fixed epsilon the two source sums are finite, since

    0<=J_(epsilon,1)(theta)<=2(epsilon^(-1)-t0^(-1)).

The complete diagonal-subtracted identity is independent of the eigenvalue:

    E_h(t)=D_m(t)-(cosh(t/2)-1)Ppole(h)+R_h(t).

The native symbol comparison therefore still gives a finite L_h with

    I_(epsilon,1)(h)>=W_(epsilon,1)(h)/2-L_h,
    |I_(epsilon,1)(h)|<=(1+C_a)W_(epsilon,1)(h)+L_h.         (5)

Tonelli identifies bounded W_(epsilon,1) with Xcrit. The control in section 2 is not Xcrit, so W diverges and (5) gives (2). This is divergence of legal finite signed cutoff sums; it is not a subtraction of two divergent unregularized height sums.

For this fixed rough control, the earlier mass/log comparison gives D_mass=o(D_w) and bounded multiplier corrections are also o(D_w). Integrating after a small fixed cutoff, then sending that cutoff to zero, and using (4), proves

    I_(epsilon,1)(h)/W_(epsilon,1)(h)->1,
    B_(epsilon,1)^mu(h)/W_(epsilon,1)(h)->-1.

Here the genuine eigenmode flux includes mu D_mass. Its relative integral is o(W), so it cannot cancel this fixed-vector leading divergence. There is no moving-eigenvector or aperture-uniform limit.

## 4. The exact minimal critical signed target at contact

For a physical orthonormal basis of the full zero kernel, sum (4)-(5). The finite-dimensional trace remainder is finite. Finite liminf I_(epsilon,1)^K forces every basis vector into Xcrit, by monotonicity of the nonnegative W trace. Zero critical promotion then puts the entire K in H1, and the already proved derivative endomorphism contradiction gives K=0.

Conversely, if this hypothetical K were nonzero, its critical positive trace and W trace must be infinite. Equation (5) then forces

    I_(epsilon,1)^K->+infinity.

Because exact zero-nullity gives I^K=-B^K+bounded transverse remainder, the alternative sufficient boundary statement is now

    limsup_(epsilon down to 0) B_(epsilon,1)^K>-infinity.

This is the critical signed complete-residual target, replacing the older sufficient order-3/2 target in this route. It is not supplied by ordinary source localization, finite dimension, native norm balance, bounded prime/pole corrections, or the transverse strip. No estimate for it is claimed.

Exact failed generic implication: complete actual source/prime/pole custody + finite eigenspace + all subcritical moments + |beta_rho|<=3/8 + shifted homogeneous regularity and diagonal subtraction -> finite critical moment or signed cutoff. The positive actual mode in (2) refutes it.

Thus an independent critical moment estimate must be confined to the actual zero-contact geometry and use information that fails in that positive control. The scalar-shift-stable promotion machinery alone cannot supply such an estimate. This conclusion leaves intact the actual zero promotion theorem, which is a regularity implication under the moment premise.

## Custody, controls and standing

Read at the recovered head:

- CRITICAL_RECIPROCAL_PROMOTION_20261007, blob 9983be22ab58e926b5e15127f8feaf53d43329e0.
- ACTUAL_SUPERCRITICAL_SOURCE_CONTROL_20261007, blob 1d1157c7257ada74d1a42c02245243b4d2edd364.
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7.
- FRACTIONAL_POSITIVE_SOURCE_MOMENTS_20261006, blob 955ff7b4bd0d7f58221c300a962a803824232fd6.
- LEADING_ROUGH_FLUX_20261006, blob 9982daabb0e22a666c13ef83b74bc21e235c0ef8.

The shifted proof inherits the already read arXiv:2401.18033v2 Theorem 1.1 upper boundary dependency. No new external theorem is imported. Analytic audit explicitly tracks mu through the Fredholm inverse, positive jump shift, bounded forcing, local regularity, mass-subtracted boundary matching and reciprocal identity. The rational companion checks the critical exponents, exact remainder coefficients and a rejected loss of the cross margin. It does not compute an actual eigenvector, certify analytic divergence, formalize the proof or establish the missing moment estimate.

Historical wording remains unchanged, including earlier statements that the critical control was then undecided. This additive note settles that question. Whole-domain positivity through 973/1000, all historical certificates and accepted external strip preserved. No aperture marching, retained historical packet attachment, same-vector enlarged cancellation, Lean build/axiom/workflow change, endpoint exclusion, RH, F4 or FULL TRANSPORT CLOSED. The new critical signed criterion is a target reduction, not arithmetic closure.
