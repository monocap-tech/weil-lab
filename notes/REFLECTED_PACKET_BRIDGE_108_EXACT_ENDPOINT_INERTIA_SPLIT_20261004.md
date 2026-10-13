# RPB108: exact endpoint coupling and enlarged-window inertia

Base: research 848a83d7a5ec44ae51ed9ec718462fa1b3554fee.

## Exact theorem

Suppose the actual native form is nonnegative on D_a and has kernel K of finite dimension r>0. For every b>a there is an explicitly defined reduced bounded form R0 such that
\[
n_-(Q_b)=r+n_-(R_0),\qquad
\dim\ker Q_b=\dim\ker R_0.
\tag{1}
\]
The reduced operator is I+compact. The r negative directions contributed by endpoint-kernel coupling are exact and cannot be removed by proving R0 nonnegative.

This strengthens the previous lower bound n_-(Q_b)>=r. It does not assert an actual nonzero endpoint or positivity of R0.

## Terminology before use

**Old positive complement:** H0=K^\perp inside D_a, in the canonical logarithmic inner product.

**New-test complement:** Z=D_a^\perp inside D_b, in that same logarithmic norm. Z is not asserted to consist of physically collar-supported functions; logarithmic orthogonality is nonlocal.

**Kernel coupling range:** F=Ran B inside Z, where B is the actual enlarged form coupling of K to Z.

**Reduced new-test remainder:** R0, obtained after removing the old strictly positive block and the finite kernel-coupling block as below.

All operators are bounded form Riesz operators on the already attached actual logarithmic carrier. No physical unbounded-operator domain is assumed.

## Lawful actual block decomposition

The inclusion D_a into D_b is isometric in the logarithmic norm and has closed image: convergence retains the physical support condition. Thus
\[
D_b=H_0\oplus K\oplus Z.
\]
The endpoint Riesz operator is nonnegative I+compact. Its restriction A0 to H0 is strictly positive and has a bounded inverse. Otherwise a unit minimizing sequence and compactness would yield an additional kernel vector in H0.

Source/native support custody and the old mixed kernel equation give the enlarged operator block form
\[
A_b=
\begin{pmatrix}
A_0&0&V\\
0&0&B^*\\
V^*&B&C
\end{pmatrix}.
\tag{2}
\]
Here C is self-adjoint on Z and V:Z->H0.

For k in K, A_b k has zero pairing with all of D_a, so it lies in Z and equals Bk. If Bk=0, k would be weak-null on D_b. Strict-enlargement rigidity implies k=0. Hence B is injective.

Because K is finite-dimensional, F=Ran B is closed, dim F=r, and D=B:K->F is a bounded isomorphism. This is actual form coupling, not a supplied observation or raw multiplicity count.

## Removing only the strictly positive old block

Complete the square with u'=u+A0^(-1)Vz. The resulting bounded invertible change of coordinates yields the direct sum of A0 and the form
\[
2\Re\langle z,Bk\rangle+\langle z,C_{\rm eff}z\rangle,
\qquad
C_{\rm eff}=C-V^*A_0^{-1}V.
\tag{3}
\]
No positivity of Ceff is assumed.

Since the full enlarged form is I+compact, its cross block V is compact and C is I_Z+compact. Therefore Ceff is also I_Z+compact.

This inverse is on the old positive bounded form block. It is derived from its proved coercivity and has no implication of physical spectral-domain membership.

## The finite coupling block has inertia (r,r)

Write
\[
Z=F\oplus Z_0,\qquad Z_0=F^\perp=\ker B^*.
\]
Relative to K, F, Z0, the remaining operator is
\[
\begin{pmatrix}
0&D^*&0\\
D&C_{11}&C_{12}\\
0&C_{12}^*&C_{22}
\end{pmatrix},
\]
where the Cij are the compressions of Ceff.

On K plus F, set
\[
W=
\begin{pmatrix}0&D^*\\D&C_{11}\end{pmatrix}.
\]
Its quadratic is 2 Re<f,Dk>+<f,C11 f>. Define k'=k+(1/2)D^(-1)C11 f. In the new coordinates the quadratic is 2 Re<f,Dk'>. Then x=Dk' gives 2 Re<f,x>, which equals
\[
\left\|\frac{x+f}{\sqrt2}\right\|^2-
\left\|\frac{x-f}{\sqrt2}\right\|^2.
\]
Thus W is nonsingular and has exactly r positive and r negative directions.

Its inverse is explicitly
\[
W^{-1}=
\begin{pmatrix}
-D^{-1}C_{11}(D^*)^{-1}&D^{-1}\\
(D^*)^{-1}&0
\end{pmatrix}.
\tag{4}
\]
The zero bottom-right block is decisive.

## No further Schur correction on the uncoupled remainder

The coupling from Z0 to K plus F is
\[
Jz_0=(0,C_{12}z_0).
\]
Equation (4) gives
\[
J^*W^{-1}J=0.
\]
Completing the square in the nonsingular finite block W therefore leaves precisely C22 on Z0, with no subtraction term:
\[
R_0=C_{22}=P_{Z_0}C_{\rm eff}|_{Z_0}.
\tag{5}
\]

We have constructed a bounded invertible congruence
\[
Q_b\ \sim\ A_0\oplus W\oplus R_0.
\tag{6}
\]
A0 is strictly positive, W has inertia (r,r) and no kernel, and R0 is I_Z0+compact. Negative index and kernel dimension are invariant under this change of coordinates. Equation (6) proves (1).

The congruence does not identify its new coordinates with unchanged physical vectors or raw source samples. Original-vector custody is the actual map (2) on D_b; no retained witness is silently renamed after completing a square.

## Consequences for the unit-bound interface

If R0 is nonnegative, the enlarged native form still has exactly r negative directions. If R0 has further negative directions, their count adds to those r. Later enlarged-window kernels are exactly the kernel of R0 under the congruence and may exist even though the window is indefinite.

Thus proving positivity of an uncoupled new-test remainder cannot repair full-source unit domination at b. The endpoint coupling already forces its failure. A projection that removes those directions changes the observation problem and must carry new source custody.

For actual full positive and negative analyses, the derived isomorphism P_b onto its closed range identifies the same negative index with that of the quadratic
\[
\|k\|^2-\|N_bP_b^{-1}k\|^2.
\]
This is the full-source interface. A selected-background projection changes the negative energy and is not included by this theorem.

The independent global task remains exclusion of the finite endpoint itself, or lawful construction of such an endpoint from actual negative input. No block factorization proves either alternative.

## Validation and cursor

Analytic proof by explicit bounded block completion, finite matrix inversion and actual compact-form/strict-enlargement facts. No new external input, Lean source/workflow change, assumed background positivity or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At 848a83d, for an actual nonnegative endpoint form with kernel K of dimension r>0 and any b>a, split D_b=H0 orthogonal-sum K orthogonal-sum Z in the canonical logarithmic norm, where H0 is the old positive complement and Z the new-test complement (not literal physical collar support). The actual bounded form operator has blocks [A0,0,V;0,0,B*;V*,B,C], with A0 strictly positive and B injective by strict-enlargement rigidity. Eliminating H0 gives Ceff=C-V*A0^(-1)V. On F=Ran B, the finite kernel/coupling block has exactly r positive and r negative directions and inverse with zero F-F block. Therefore its elimination introduces no correction on Z0=ker B*. A bounded congruence yields Q_b equivalent to A0 plus an (r,r) block plus R0=P_Z0 Ceff|Z0. Hence n_-(Q_b)=r+n_-(R0) and nullity(Q_b)=nullity(R0); R0 is I+compact. Positivity of the remainder cannot remove the r forced negative directions. These are derived bounded form inverses, not assumed physical operator domains, raw synthesis or null transport. This closes an exact inertia/factorization obstruction, not endpoint exclusion or global full-source unit domination. No actual finite endpoint, background positivity, RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
