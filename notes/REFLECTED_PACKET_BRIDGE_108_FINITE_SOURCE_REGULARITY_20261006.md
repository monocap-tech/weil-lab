# RPB108: finite source reconstruction has a strict regularity flag

Date: 2026-10-06. Source base: `b0ab19f34a9e2f6cb006e4db0ab6399e1fd2e54e`.
Definitions: [finite source regularity](../docs/TERMINOLOGY_RPB108_FINITE_SOURCE_REGULARITY.md).
Lane: global/F4, with no aperture calculations.

## Result

At any hypothetical nonnegative actual null window with r=dim K>0, the finite source regularity flag satisfies
\[
\dim E_j\le\max(r-j,0),\qquad j=0,1,2,\ldots.
\tag{1}
\]
In particular at most r-1 independent unit-gain coefficient modes can reconstruct globally H1 vectors. In a minimal r-row selection, at least one reconstructed coordinate column is not globally H1. For r=1 every nonzero null coefficient reconstructs a non-H1 vector.

Consequently, H1 membership for the entire reconstructed null coefficient space would exclude contact immediately. A single H1 attached vector need not suffice when r>1. Bounded invertibility of G, finite analytic interior source densities, and the WD-T10 covariance identities do not establish the missing H1 mapping property. An exact rank-one archimedean control below has all those operator features and a non-H1 inverse image of constant interior forcing.

## Strict descent before finite reconstruction

Set K_j=K intersect H^j(R), for the global zero extensions. The supported-L2 promotion theorem proves that if h in K is globally H1, its derivative belongs to K. Hence differentiation maps K_j into K_(j-1) for j>=1, and K_j is a subspace of K_(j-1).

If dim K_j=dim K_(j-1)>0, finite dimension makes these subspaces identical. Differentiation would then be an endomorphism of their common nonzero finite-dimensional space. For any nonzero h there, iterating supplies arbitrarily many global L2 derivatives in that space. A linear relation would give P(2 pi i xi) Fourier(h)=0 for a nonzero polynomial P, impossible for a nonzero L2 Fourier transform. Thus
\[
K_j\ne0\quad\Longrightarrow\quad
\dim K_j<\dim K_{j-1}.
\tag{2}
\]
Starting at dim K_0=r yields (1) for K_j; once a flag member is zero all later ones are zero. This strengthens the preceding K intersect H^r={0} statement by bounding every intermediate regularity subspace. No endpoint trace or derivative of a non-H1 vector is invoked.

## Exact selected coefficient custody

The established reconstruction B=-G^(-1)R* maps E=ker D bijectively onto K, with inverse h -> -Rh. This preserves the same physical vector. Pulling K_j back by B proves (1) for E_j. The induced derivative map, defined only on E_1, is
\[
T u=-R\,\partial_x(Bu),\qquad B(Tu)=\partial_x(Bu).
\tag{3}
\]
It maps E_j into E_(j-1). It is not an everywhere-defined derivative endomorphism on E unless the missing whole-space H1 property holds; equation (3) must not be used on arbitrary unit-gain coefficients.

For a minimal selection |s|=r the finite matrix at contact is D=0, so E=M. The r independent columns B e_i span K. If every one were H1, all K would be H1 and (2) would force K=0, contradicting r>0. Thus at least one column fails H1. For a larger partner-closed selection, the assertion applies to a basis of ker D, not to every coordinate of M.

Actual selected rows have analytic exponential forcing densities: in the source convention their evaluations are one half of the difference F_h(conjugate z_q)-F_h(z_q), with the retained actual normalization weights. Their Hilbert adjoints use the logarithmic norm. Thus the equation G h=R*v supplies analytic densities against physical interior tests, but does not identify R*v with the analytic function as a global physical vector. This distinction remains after applying a bounded inverse on D_a.

No dilation occurs in (1)-(3). Changing aperture by U_t changes the physical vector, and cannot turn this same-window coefficient flag into same-vector enlarged/null transport. Actual full native nullity is used throughout; effective G-nullity would give only the zero vector because G is coercive.

## Exact coercive inverse control with constant interior forcing

Reuse the already proved shifted actual-archimedean control at any a>0: its nonnegative form operator A0 on H=D_a has one-dimensional kernel spanned by a real nonnegative physical-mass-one groundstate h0. Its global zero extension is not H1. This is a comparison form with tuned scalar mass, with the prescribed primes/pole absent.

Let L:H->C be Lh=integral_(-a)^a h(x) dx, with adjoint in H, and rho=Lh0>0. Positivity follows because h0 is nonnegative and nonzero; boundedness follows from physical L2 inclusion. Define
\[
G0=A0+L^*L.
\]
The existing nonnegative Fredholm/finite-selection argument makes G0 coercive: L separates its one-dimensional kernel. Since A0 h0=0,
\[
G0 h0=\rho L^*1,\qquad
G0^{-1}L^*1=h0/\rho,\qquad
L G0^{-1}L^*=1.
\tag{4}
\]
The exact one-by-one response D0=1-LG0^(-1)L*=0, and its reconstructed physical vector -h0/rho is non-H1. Setting S0=G0^(1/2), C0=-G0^(-1/2)L* gives S0 C0=-L*, S0 S0*-L*L=A0, and C0*C0=1. These are comparison covariance/unit-gain identities on the fixed logarithmic coefficient carrier, not an identification with actual positive source synthesis or a historical packet. The right-hand side L*1 represents constant forcing against interior physical tests. On such tests the equation reads
\[
(m0(D)-\lambda_a)h0+\rho=\rho,
\]
with the constant rank-one term and forcing cancelling exactly. The constant density is analytic up to both endpoints; its zero extension is not asserted smooth. Equation (4) disproves a general smoothing claim for a coercive effective inverse of analytic interior forcing, even with the same actual archimedean kernel and logarithmic carrier.

This is not an actual selected zeta divisor coordinate and not an actual full-native contact. It controls the functional-analytic implication only. An actual arithmetic-specific regularity theorem remains possible.

## Sharpness of the flag under derivative invariance alone

For integer r>=1 let h_r be the r-fold convolution of 1_[0,1], and let V_r span h_r,h_r',...,h_r^(r-1). These r vectors are compactly supported L2 vectors and are independent by the Fourier-polynomial argument. Its last vector is a step function; all vectors belong to the logarithmic domain. On this abstract space,
\[
\dim(V_r\cap H^j)=\max(r-j,0),\qquad
\partial_x(V_r\cap H^1)\subset V_r.
\tag{5}
\]
Indeed h_r has degree r-1 between consecutive integers. Its r-th derivative is sum_(k=0)^r (-1)^k binom(r,k) delta_k. For a combination whose highest derivative index is q, applying j derivatives is L2 exactly when q+j<r: otherwise its nonzero highest delta derivative at x=0 cannot be cancelled by lower derivative indices. For q+j<r it is a compact piecewise polynomial L2 function. This proves (5).

For r>1 this provides nonzero globally H1 vectors in a finite-dimensional derivative-closed-on-H1 space. It shows (1) is sharp for the derivative-invariance information alone. V_r is not asserted to be an actual native kernel or to satisfy actual prime/pole equations.

## Remaining theorem and validation

The failed implication is: coercive effective covariance plus finitely many analytic interior forcing densities -> all reconstructed unit-gain modes have global H1 zero extensions. Equation (4) blocks that general inference. This belongs to endpoint exclusion, not retained attachment or null transport.

A precise sufficient remaining theorem is that G_s^(-1)R_s* maps ker D_s into global H1 for every actual nonnegative window with a kernel-separating selection. The finite flag would then exclude every nonzero contact. This mapping property is not proved here; in a minimal selection it asks for the r named inverse-source columns, while for a larger selection it asks only for null coefficient combinations. Actual source arithmetic must supply it or an independent exclusion argument.

If a historical retained H1 Green vector is attached to full actual nullity, the flag bounds that one vector's possible location. It excludes it immediately only with r=1, or with sufficient additional derivatives or enough independent H1 attached vectors to fill K. Existential finite selection, bounded synthesis, and unit-gain identities do not supply those inputs.

Pinned sources and blob custody are in the manifest: L2_NULL_DOMAIN_PROMOTION_20261006; FINITE_SELECTION_EFFECTIVE_POSITIVE_REALIZATION_20261006; LOCAL_FINITE_SOURCE_MATRIX_20261006; ARCHIMEDEAN_CONTACT_CONTROL_20261006; DERIVATIVE_CHAIN_REGULARITY_CEILING_20261006. Analytic verification covers strict subspace descent, domain of (3), both inverse signs, constant forcing custody and delta-order sharpness. Rational controls check the scalar response algebra and spline delta coefficients; they are not a Lean proof or an actual null computation. No Lean/workflow edits or new CI/axiom certificate. Historical records preserved; F4 and FULL TRANSPORT CLOSED remain open.
