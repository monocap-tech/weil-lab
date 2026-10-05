# RPB108: stable observation on the actual near-null range

Base: research c0ae3b6608ac6793d835e87e2f4b77c6b8205539.

## Theorem

At every fixed actual window a, let H=D_a with its logarithmic norm and A its bounded native form operator. Write K=ker A and r=dim K. There are r bounded, independent actual exterior point observations O:H -> complex^r such that
\[
\|h\|_H\le C_A\|Ah\|_H+C_O\|Oh\|.
\tag{1}
\]
Consequently joint observation (Ah,Oh) is bounded below on H, and O alone is bounded below on any sufficiently small native-residual cone.

This removes the need for a bounded inverse of the compact tail observation on the entire carrier. It derives stability on the relevant near-null vectors. It does not show that the observations vanish on a null vector.

## Terminology before use

**Native residual norm:** ||Ah||_H, equivalently the dual norm of the full native mixed functional g -> Q_a(g,h).

**Near-null cone:** vectors satisfying ||Ah||_H<=epsilon||h||_H. It is not asserted to be a linear subspace.

**Joint native/exterior observation:** (Ah,Oh), with Ah on the original logarithmic carrier and O actual far residual evaluations of that same h.

**Full-source defect operator:** I-T* T on the actual positive-analysis range, where T=N P^(-1).

A small indefinite diagonal Q_a(h) is not the same as a small native residual.

## Actual finite observations

The actual operator is self-adjoint I+compact. K is finite-dimensional, and its restriction A_E to E=K^perp is boundedly invertible. Let
\[
\delta=\|A_E^{-1}\|^{-1}>0.
\]
No positivity of A_E is assumed.

The preceding actual exterior theorem makes q_h real analytic for x>3a and proves that vanishing on an open exterior interval forces h=0. Each point evaluation h -> q_h(x) there is a bounded physical L2 functional, hence a bounded logarithmic functional.

On K, these evaluations separate every nonzero vector. Their span equals K^*, so choose r distinct points in any fixed open interval I contained in (3a,infinity) such that
\[
Oh=(q_h(x_1),\ldots,q_h(x_r))
\]
has O|K invertible. Define
\[
\alpha=\|(O|_K)^{-1}\|,\qquad M=\|O\|.
\]
The constants depend on the fixed actual form, points and norm. No numerical kernel basis or actual nonzero kernel is asserted.

If r=0, no exterior observations are needed: A is invertible and (1) holds with C_O=0 and C_A=||A^(-1)||.

## Explicit stability proof

For r>0 decompose the unchanged vector h=k+u, with k in K and u in E. Since Ah=A_E u,
\[
\|u\|\le\delta^{-1}\|Ah\|.
\]
Also
\[
\|k\|\le\alpha\|Ok\|
\le\alpha\|Oh\|+\alpha M\|u\|.
\]
Therefore
\[
\|h\|\le
\frac{1+\alpha M}{\delta}\|Ah\|+\alpha\|Oh\|.
\tag{2}
\]
This proves (1) with explicit C_A and C_O.

In particular if ||Ah||<=epsilon||h|| and C_A epsilon<1, then
\[
\|Oh\|\ge\frac{1-C_A\epsilon}{C_O}\|h\|.
\tag{3}
\]
For epsilon<=1/(2C_A), the lower bound is ||h||/(2C_O). When r=0, the corresponding sufficiently small cone contains only zero.

Thus the compact-observation obstruction on unrestricted vectors does not imply unstable observation on this near-null cone. The native Fredholm residual already controls the infinite-dimensional complement.

If the fixed form is nonnegative, positivity additionally gives
\[
\|Ah\|^2\le\|A\|Q_a(h).
\]
Then (1) supplies a diagonal-energy version with C_A sqrt(||A||) sqrt(Q_a(h)). This implication is conditional on actual nonnegativity at the named window; it is not applied to indefinite windows.

## A lawful bounded reconstruction

Set Lh=(Ah,Oh). Equation (2) and Cauchy-Schwarz yield
\[
L^*L=A^*A+O^*O\ge
(C_A^2+C_O^2)^{-1}I.
\]
The positive bounded operator on the left therefore has a bounded inverse. The map
\[
\mathcal R(z,t)=(A^*A+O^*O)^{-1}(A^*z+O^*t)
\tag{4}
\]
is bounded and satisfies R(Ah,Oh)=h.

All ingredients are derived on the already lawful actual carrier. This is not a raw divisor-copy synthesis inverse or a physical unbounded-operator inverse. Formula (4) only reconstructs a vector from compatible data when that data is actually the residual and observations of the same vector. It does not attach an abstract retained record without proving membership and identities.

At least r scalar observations are necessary for any such joint lower bound: on K the native residual is zero, so the observation map must be injective, which needs rank at least r. The chosen observations achieve that minimum. Identical equal-ordinate copies cannot supply the required rank.

## Transport to the actual positive carrier

Let P:H -> Hplus be the actual bounded isomorphism onto its closed positive-analysis range, and N the complete negative analysis. Put T=N P^(-1). The same-vector source/native mixed identity gives
\[
D:=I-T^*T=P^{-*}A P^{-1},
\qquad A=P^*DP.
\tag{5}
\]
The defect D is bounded self-adjoint; it is not assumed nonnegative.

For k=Ph and Oplus=O P^(-1), (1) implies
\[
\|k\|\le
\|P\|^2 C_A\|Dk\|+
\|P\|C_O\|O_{\rm plus}k\|.
\tag{6}
\]
This is fixed-window stable joint observation on the correct actual positive carrier.

The residual in (6) is ||(I-T* T)k||. Merely having ||k||^2-||Tk||^2 near zero in an indefinite window does not make this residual small. Null-cone cancellation is not silently promoted to weak-nullity.

The theorem uses full N. A selected negative projection changes T and its native defect identity; its custody must be proved separately.

## The exact missing factorization

Fix any injective weighted tail W from the preceding theorem. The following are equivalent at the fixed window:

1. ker A=0;
2. W annihilates ker A;
3. W=F A for some bounded F;
4. ||Wh||<=C||Ah|| for every h and some finite C.

Indeed W is injective, so condition 2 forces the kernel zero. If A has zero kernel, I+compact makes it boundedly invertible, and F=W A^(-1) proves 3 and 4. Either 3 or 4 makes W vanish on the kernel.

This is a precise obstruction: joint stability is derived, but factoring the exterior observation through the native residual alone would already exclude endpoint nullity. No such factorization has been established for actual null vectors.

The same issue remains for the desired Gaussian upper estimate. Observing a null mode stably does not make its nonzero observation disappear or control its signed moving-Gaussian pairing.

## Validation and cursor

Analytic proof from actual Fredholm structure and exterior moment rigidity, with explicit complement estimates and bounded positive-operator inversion. No new external input, uniform-aperture lower bound, endpoint existence, RH conclusion, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At c0ae3b6, fixed-window actual Fredholm structure closes stable observation on the relevant near-null range. For H=D_a, native bounded form operator A=I+compact, and r=dim ker A, actual exterior moment rigidity supplies r independent bounded point observations O with O|ker A invertible. If delta is the invertible-complement gap, alpha=||(O|ker A)^(-1)|| and M=||O||, then ||h||<=((1+alpha M)/delta)||Ah||+alpha||Oh||. Thus joint native-residual/exterior observation is bounded below on the full carrier, and O alone is bounded below on sufficiently small native-residual cones. A bounded left inverse is (A*A+O*O)^(-1)(A*,O*); r observations are minimal. On the actual positive carrier the native defect is I-T*T for full T=N P^(-1), and the same joint estimate transports lawfully. Near-null means a small mixed residual, not merely a small indefinite diagonal. This derives fixed-window stability without a global inverse for compact tail observation or uniform aperture constants. The remaining missing input is annihilation/control of exterior observation on actual null vectors: for a fixed injective weighted tail W, W=R A with bounded R is equivalent to ker A=0. Stability does not supply that factorization. No retained membership, raw preimage, background positivity, actual endpoint/RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
