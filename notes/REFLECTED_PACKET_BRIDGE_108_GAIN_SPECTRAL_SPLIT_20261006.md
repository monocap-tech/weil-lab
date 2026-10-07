# RPB108: exact quadratic gain spectral split and a sequencewise endpoint target

Date: 2026-10-06 (America/Los_Angeles). Source `98113d6a145a04e0ff9b9a60adcdc745478a80fd`.
Definitions: [quadratic gain spectral split registry](../docs/TERMINOLOGY_RPB108_GAIN_SPECTRAL_SPLIT.md).
Global/F4 lane. No aperture computation or actual contact existence assertion.

## Stronger actual conditional conclusion

At a hypothetical nonnegative actual contact, let E be the finite null coefficient space, r=dim E>0 and Ereg the coefficients reconstructing globally H1 vectors. Write d=dim Ereg<=r-1. For the positive normalized finite gain matrix Gamma_s, ordered eigenvalues satisfy
\[
\boxed{\lambda_i(s)\longrightarrow0\ (1\le i\le d),\qquad
\lambda_i(s)\longrightarrow\infty\ (d<i\le r).}
\tag{1}
\]
The empty regular group when d=0 is allowed. In particular trace_E Gamma_s tends to infinity at every nonzero actual contact.

For every **fixed** non-H1 actual null vector h, the earlier limsup statement strengthens to a limit:
\[
\frac{e_s(h)}{s^2}\longrightarrow\infty,
\qquad
\frac{M_s(h)}{s^2\log(1/s)}\longrightarrow\infty.
\tag{2}
\]
For every H1 null vector, e_s/s^2 tends to zero and M_s/s^2 tends to zero. There is no fixed nonzero null mode with a finite positive limiting quadratic gain ratio.

Consequently, a bounded ratio along just one sequence of collars suffices to force regularity:
\[
h\in H^1(\mathbb R)
\Longleftrightarrow\liminf_{s\downarrow0}e_s(h)/s^2<\infty
\Longleftrightarrow\liminf_{s\downarrow0}M_s(h)/(s^2\log(1/s))<\infty.
\tag{3}
\]
This is a strictly weaker input condition than an all-small-s upper bound, although the null equation then promotes it to the full estimates already proved. Historical statements are preserved; this note adds a strengthening rather than changing their proofs or claims.

## Positive Fourier defect forces limit divergence

Use the actual gain/translation inequality already proved, with finite observation constant B_R and multiplier-envelope constant Z_c:
\[
D_w(s;h)/s^2
\le4Y_s+2B_R\|h\|_2\sqrt{Y_s}+2Z_c\|h\|_2^2,
\qquad Y_s=e_s(h)/s^2.
\tag{4}
\]
If h is not globally H1, integral xi^2 w(xi)|Fourier h|^2 is infinite. For each fixed bounded frequency cutoff N, the elementary bound 1-cos u>=u^2/4 for |u|<=1 gives, whenever s<=1/(2 pi N),
\[
D_w(s;h)/s^2\ge\pi^2\int_{|\xi|\le N}
\xi^2w(\xi)|\widehat h(\xi)|^2d\xi.
\tag{5}
\]
Let N tend to infinity after fixing any desired lower level. The right side becomes arbitrarily large and the lower bound holds for **all** sufficiently small s. Thus D_w(s;h)/s^2 tends to infinity, not merely along a sequence. Equivalently one can apply Fatou along every sequence tending to zero.

The right side of (4) is an increasing finite function of Y_s; hence Y_s must tend to infinity. COLLAR_GAIN gives e_s<=10 M_s/(beta log(1/s)), which proves the second limit in (2). Conversely globally H1 gives both little-o estimates by derivative promotion and zero-trace collar control. This proves (2)-(3).

An H1 vector with an infinite logarithmic derivative energy is not an escape here: derivative promotion makes h' itself full-null and therefore gives its finite logarithmic energy. The distinction between actual nullity and general carrier regularity is essential.

## Uniform rough complement and the finite spectral split

Let W be the fixed coefficient-orthogonal complement of Ereg in E, and let h=B_c u. For N>0 define the positive truncated quadratic form
\[
T_N(u)=\int_{|\xi|\le N}\xi^2w(\xi)|\widehat{B_cu}(\xi)|^2d\xi
\quad(u\in W).
\]
It is finite and continuous on W, increases with N, and tends to infinity for every nonzero u in W, since B_c u is not H1. The convergence of its minimum on the unit sphere is also to infinity. To prove this, suppose unit u_N exist with T_N(u_N)<=C along N tending to infinity. Compactness of the finite-dimensional unit sphere supplies a subsequence u_N tending to unit u. For every fixed N0, monotonicity and continuity give T_(N0)(u)<=C. Monotone convergence then yields a finite weighted derivative energy for B_c u, contradicting u in W.

Equation (5) now holds uniformly on that unit sphere, so its Fourier defect divided by s^2 has minimum tending to infinity. Physical norms ||B_cu||_2 are uniformly bounded there. Applying (4) uniformly therefore gives
\[
\min_{u\in W,\ \|u\|=1}\langle u,\Gamma_su\rangle\longrightarrow\infty.
\tag{6}
\]
On the d-dimensional Ereg, each fixed basis vector has gain o(s^2). Gamma_s is positive, so the trace of its compression to Ereg tends to zero, bounding that compression's operator norm. Hence
\[
\max_{u\in Ereg,\ \|u\|=1}\langle u,\Gamma_su\rangle\longrightarrow0
\quad(d>0).
\tag{7}
\]
Finite-dimensional min-max gives lambda_d(s)<=the maximum in (7), and lambda_(d+1)(s)>=the minimum in (6). Positivity and eigenvalue order prove every assertion in (1). No convergence of individual eigenvectors or diagonalization common to all s is presumed. The same proof gives a uniform collar-mass divergence on the fixed unit sphere in W.

This is not uniform divergence over all unit vectors outside Ereg: varying vectors can approach Ereg as s decreases. The distinction is required for a correct min-max argument.

## Controls for cross terms and moving vectors

For 0<s<1 and a rational |a|<1, consider the positive matrix
\[
H_s=\begin{pmatrix}s&a\\a&1/s\end{pmatrix}.
\]
Its determinant is 1-a^2>0. On the fixed regular line its form tends to zero; on the orthogonal rough line it diverges. Its smaller eigenvalue is bounded between determinant/trace and s, and its larger between 1/s and trace, reproducing (1). Off-diagonal entries need not tend to zero and eigenvectors need not be fixed.

The vector (1,s), outside the regular line for every s>0, has H_s energy 2(1+a)s tending to zero. This rejects the false upgrade from fixed-mode divergence to divergence over every varying rough vector. These matrices and vectors are algebra controls, not actual source responses or contact examples.

The elementary cosine floor in (5) follows from 1-cos u>=u^2/2-u^4/24>=11u^2/24>=u^2/4 for |u|<=1. The accompanying rational controls check that coefficient floor and the matrix determinant, discriminant and moving-vector identities. They do not certify the Fourier/compactness argument.

## Smallest new sufficient endpoint theorem

The prior all-small-s quadratic matrix bound can now be weakened to the sequencewise arithmetic claim
\[
\liminf_{s\downarrow0}\operatorname{trace}_E
\frac{\Pi_E[\Lambda(c+s)-\Lambda(c)]\Pi_E}{s^2}<\infty
\tag{8}
\]
at every hypothetical nonnegative actual contact. By (1), (8) is impossible for any nonzero contact; proving it from the actual arithmetic would exclude first contact and give all-window domination via the established dichotomy. Equivalently it suffices, for a basis of the actual full kernel, to prove a bounded collar-mass ratio in (3) along a sequence for each basis vector. Their sequences may differ: (3) puts every basis vector in H1, and finite-dimensional derivative invariance then excludes the whole kernel.

**Neither sequencewise arithmetic theorem is proved.** The available inverse-logarithmic estimates allow divergence in (2); strict Loewner monotonicity is also consistent with it. The trace in (8) covers the full finite null coefficient space. It is not the single averaged inverse-boundary moment previously shown noninjective on the general carrier.

Thus the exact failed implication remains all finite logarithmic boundary estimates -> even sequencewise polynomial-scale boundedness. The remaining theorem belongs to **endpoint exclusion**. Prescribed retained attachment and same-vector enlarged full mixed-null transport keep their separate scopes; no equation on the larger support is inferred. The physical vector is unchanged throughout, with no dilation.

## Custody and standing

Pinned source blobs and repeat exact controls: notes/data/RPB108_GAIN_SPECTRAL_SPLIT_20261006.json. This is analytic conditional actual research, not Lean certified. No Lean/compiler/workflow changes or new axiom/CI claim. Historical wording and certificates preserved. Whole-domain aperture remains 23/25 with independent 93/100 corrected sign pending. F4 and FULL TRANSPORT CLOSED remain open.
