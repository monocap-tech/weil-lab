# RPB108: finite-kernel collar observability and degeneration

Base: research 0e7661f8079d7fbb02752a0fb633c23cb3fd7a1f.

## The theorem

Fix a>0 and suppose the actual endpoint weak-null space
\[
K_a=\{h\in D_a:Q_a(v,h)=0\text{ for every }v\in D_a\}
\]
has dimension r>0. Its dimension is finite by the proved I+compact form theorem.

For every fixed b>a:

1. The genuine shell-corrected residual map from K_a to the newly admitted physical collars is bounded below.
2. Exactly r smooth collar tests suffice to give injective complex-linear observations on K_a, with a strictly positive stability floor. Fewer than r cannot suffice.
3. A single linear physical correction and one common positive scalar construct an r-dimensional strictly negative subspace in D_b. Thus the native negative index at b is at least r.

As b decreases to a, the unscaled physical residual map tends to zero in operator norm. Its lower floor therefore tends to zero too. Observers with uniformly bounded total physical test norm cannot maintain a fixed observation floor.

This is genuine observability on the actual finite-dimensional null range, not independence manufactured by counting divisor copies. No nonzero actual K_a is asserted to exist.

## Terminology before use

**Kernel collar map:** B_a,b h=q_b(h)|Omega_a,b, where Omega_a,b=(-b,-a) union (a,b), and q_b uses the unchanged h with the exact multiplier cutoff b.

**Physical observation budget:** the square root of the sum of the squared L2 norms of the chosen smooth tests. Rescaling tests without a uniform bound does not preserve this budget.

**Fixed-enlargement stability floor:** a positive lower bound for an observation map at fixed a,b. It does not mean a uniform bound as b approaches a.

**Negative index:** the maximal complex dimension of a subspace on which the native quadratic is strictly negative. No globally finite defect index is assumed.

## Genuine bounded injective residual map

Give K_a its physical L2 norm. Since it is finite-dimensional and its physical inclusion is injective, this is a Hilbert norm equivalent to its logarithmic and positive-energy norms.

The actual residual theorem and exact finite prime-shell correction give a linear locally L2 residual
\[
q_b(h)=q_a(h)-
 \sum_{2a<\log n\le2b}\frac{\Lambda(n)}{\sqrt n}
 \bigl(h(\,\cdot-\log n)+h(\,\cdot+\log n)\bigr).
\]
The pole is unchanged. Derived global L2 control of the core and bounded local pole moments imply B_a,b is bounded in the physical norm.

The direct physical constructor already proved that B_a,b h!=0 whenever h!=0 in K_a: otherwise the genuine mixed pairing makes h weak-null on D_b, contradicting strict-enlargement rigidity. Therefore B_a,b is injective.

Compactness of the physical unit sphere of K_a supplies
\[
\|B_{a,b}h\|_2\ge\eta_{a,b}\|h\|_2,\qquad\eta_{a,b}>0.
\tag{1}
\]
This is a derived finite-range floor. It is not a bound on the entire source domain.

## One common cutoff and smoothing scale

Write B=B_a,b and eta=eta_a,b. Choose a real compact smooth collar cutoff chi, with 0<=chi<=1, for which
\[
\|(1-\chi)B\|_{K_a\to L^2}\le\eta/4.
\]
Such a common cutoff exists: compact collar exhaustion converges strongly in L2, and convergence is uniform on the compact image of the finite-dimensional unit sphere.

It follows that ||chi B h||_2>=(3eta/4)||h||_2. Extend chi^2 B h by zero and mollify with one common sufficiently small compact smooth kernel. Define the linear map
\[
Lh=\rho_\epsilon*(\chi^2 B h).
\]
Its values are smooth and compactly supported in the collars if epsilon is below the fixed cutoff support margin.

Finite-dimensional uniform approximate-identity convergence allows the common choice
\[
\|L-\chi^2B\|_{K_a\to L^2}
 \le\frac{\eta^2}{8\|B\|}.
\]
Using the genuine mixed pairing Q_b(g,h)=int conjugate(g)q_b(h),
\[
\Re Q_b(Lh,h)
\ge\|\chi B h\|_2^2-
 \|Lh-\chi^2B h\|_2\|B h\|_2
\ge\frac{\eta^2}{4}\|h\|_2^2.
\tag{2}
\]
Set sigma=eta^2/4. This constructs one smooth linear detecting map for the whole kernel, not separately chosen tests for individual modes.

## Minimal independent smooth observations

Choose a physical-orthonormal basis e_1,...,e_r of K_a, and put g_i=L e_i. Define
\[
M_{ij}=Q_b(g_i,e_j),\qquad
O(h)=(Q_b(g_i,h))_{i=1}^r.
\]
For h=sum c_i e_i, O(h)=M c and (2) gives
\[
\Re(c^*Mc)\ge\sigma\|c\|^2.
\]
Thus the Hermitian part of M is bounded below by sigma I. In particular M is invertible and
\[
\|O(h)\|_{\mathbb C^r}\ge\sigma\|h\|_2.
\tag{3}
\]

These r tests are independent functionals on the actual kernel. Any complex-linear map from an r-dimensional space to C^m with m<r has nonzero kernel, so the count r is minimal.

The tests are physical collar observations with actual mixed-form custody. Their independence is not a statement that raw multiplicity copies give distinct observations.

## A common negative subspace

Because L has finite-dimensional smooth range, there is a finite D>=0 with
\[
|Q_b(Lh,Lh)|\le D\|h\|_2^2.
\]
For all h in K_a, unchanged support inclusion gives Q_b(h,h)=0. Choose the common scalar
\[
t=\frac{\sigma}{\sigma+D}>0.
\]
Hermitian expansion and (2) yield
\[
Q_b(h-tLh)\le-2t\sigma\|h\|_2^2+t^2D\|h\|_2^2
 \le-t\sigma\|h\|_2^2.
\tag{4}
\]

The source h is supported in [-a,a], while Lh is supported in the disjoint outer collars. Hence
\[
\|h-tLh\|_2^2=\|h\|_2^2+t^2\|Lh\|_2^2.
\]
The map h->h-tLh is injective. Its image is an r-dimensional negative subspace, proving the index claim.

Actual source custody is linear:
\[
P_b(h-tLh)=P_bh-tP_bLh,\qquad
N_b(h-tLh)=N_bh-tN_bLh.
\]
Every nonzero vector in that subspace has negative energy with the uniform bound (4), and therefore strict full-negative gain. Selected-background energy is not inferred.

## Why the floor degenerates at the endpoint

The actual prime-power logarithms are discrete on every bounded interval. Thus there is a delta_*>0 for which no newly activated prime power lies in 2a<log n<=2(a+delta_*). Old equality-threshold terms remain in the old cutoff.

For a<b<a+delta_*, q_b(h)=q_a(h). The preceding shrinking-collar theorem applies uniformly to all h in K_a, because its derived squared-logarithmic bound has a constant depending only on a. It gives
\[
\|B_{a,b}\|_{K_a\to L^2}
 \le\frac{C_a}{\log(1/(b-a))}
 \longrightarrow0.
\tag{5}
\]
The lower singular value in (1) is at most the operator norm, so no uniform positive residual floor persists as b decreases to a.

For any finite test family u_i in the newly admitted collars,
\[
\left(\sum_i|Q_b(u_i,h)|^2\right)^{1/2}
 \le\left(\sum_i\|u_i\|_2^2\right)^{1/2}
       \|B_{a,b}h\|_2.
\tag{6}
\]
If the physical observation budget is uniformly bounded, equations (5)--(6) make the observation operator norm tend to zero. A fixed lower floor is therefore impossible under that budget.

Tests may be rescaled with norms tending to infinity, but that is not uniform stable observability. The theorem distinguishes this cost from the existence of an invertible matrix at each fixed enlargement.

The positive norm on K_a is fixed under source inclusion and equivalent to its physical norm. Thus the same degeneration holds in the lawful positive-energy carrier. No raw coefficient duplication can remove it.

## What this closes

The actual finite null range has enough independent physical observations at each fixed enlargement, with an explicit smooth-test construction and a negative-index consequence. This closes a genuine finite-range observability constructor.

It does not preserve the endpoint null equation in the larger carrier; the observations detect exactly its failure. Their shrinking-collar conditioning degenerates rather than furnishing a uniform transport floor.

The independent frontier remains exclusion of the actual endpoint kernel, or another argument supplying the missing boundary cancellation. This theorem does not assert that K_a is nonzero, establish RH, or close FULL TRANSPORT CLOSED.

## Validation and cursor

Analytic proof using the actual residual and prime-shell constructor, finite fixed-window nullity, compactness of finite-dimensional spheres, uniform mollification, the shrinking-collar estimate and explicit mixed-form matrices. No new external input, Lean source/workflow change or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At 0e7661f, for any nonzero finite-dimensional actual endpoint kernel K_a of dimension r, the prime-shell-corrected collar map B_a,b:h->q_b(h)|Omega_a,b is injective and bounded below at each fixed b>a. Compact collar cutoff and uniform finite-dimensional mollification construct a linear smooth-test map L:K_a->C_c^infinity(Omega_a,b) with Re Q_b(Lh,h)>=sigma_a,b||h||_2^2. For a physical-orthonormal basis e_i, the r tests g_i=L e_i give an invertible mixed observation matrix with positive Hermitian part; r is the minimal count of complex-linear observations needed on K_a, independent of divisor-copy multiplicity. One common t produces an r-dimensional strictly negative physical subspace {h-tLh}, so fixed-window negative index at b is at least r. As b decreases to a, the actual discrete prime cutoff is locally constant; the collar residual operator norm is <=C_a/log(1/(b-a)) and tends to zero. Thus its stability floor degenerates; any observer family with uniformly bounded total physical L2 test norm also loses its observation floor. Rescaling tests without bound is not uniform stability. Positive-energy norms on K_a are equivalent and retain this conclusion. This proves genuine fixed-enlargement kernel observability and its conditioning obstruction, not endpoint null exclusion or global unit domination. No actual endpoint existence, RH conclusion or new Lean/CI result. FULL TRANSPORT CLOSED remains open.
