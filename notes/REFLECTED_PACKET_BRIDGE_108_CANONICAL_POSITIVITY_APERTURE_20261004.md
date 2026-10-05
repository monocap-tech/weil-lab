# RPB108: canonical full-source positivity aperture

Base: research fe4598a0c5be51b3dea2327e6c9fb7cf17e31691.

## The aperture theorem

For the actual native forms on the canonical supported logarithmic domains, define
\[
\mathcal P=\{a>0:Q_a(h)\ge0\text{ for all }h\in D_a\},
\qquad A=\sup\mathcal P\in(0,\infty].
\]
Let T_a=N_a P_a^{-1} be the actual induced map on the closed positive-analysis range.

Exactly one of the following alternatives holds.

| Scope | Native form | Full-source positive-carrier gain |
|---|---|---|
| A=infinity, every finite a | Strictly logarithmically coercive | ||T_a||<1 |
| A finite, 0<a<A | Strictly logarithmically coercive | ||T_a||<1 |
| A finite, a=A | Nonnegative, with nonzero finite-dimensional kernel | ||T_A||=1, attained |
| A finite, a>A | Has a strict actual negative vector | ||T_a||>1 |

If A is finite, every nonzero endpoint kernel vector has nonzero L2 mass in every left and every right endpoint collar. It cannot be supported in a proper shorter interval, even after translating its support.

For finite A, the exact positivity set is (0,A]. For infinite A it is (0,infinity). Positive windows cannot disappear and then reappear.

This proves the architecture of the aperture, not which alternative actual zeta realizes. No finite A or actual nonzero endpoint vector is asserted to exist.

## Terminology before use

**Canonical full-source positivity aperture:** the extended supremum A above, using the complete native/source form and all physical vectors in each D_a. It is not an aperture measured from selected coordinates or a finite sample audit.

**Endpoint collar saturation:** for h supported in [-A,A], every epsilon in (0,2A) satisfies
\[
\int_{-A}^{-A+\epsilon}|h(x)|^2dx>0,\qquad
\int_{A-\epsilon}^{A}|h(x)|^2dx>0.
\]
This is an essential-support conclusion; it does not assert endpoint traces, continuity, H1 regularity or operator-domain membership.

**Attained unit-gain space:** ker(I-T_A^*T_A) inside the closed range Ran P_A, using its inherited coefficient Hilbert norm.

## Actual inputs already proved

The preceding records give:

- Q_a(f,g)=<P_a f,P_a g>-<N_a f,N_a g>, with actual normalized complete samples, bounded sampling and positive-analysis closed range.
- Physical support inclusion preserves both actual coordinates and the mixed form.
- Simultaneous physical translations preserve the full native form.
- Each fixed-window logarithmic Riesz operator is self-adjoint I+compact.
- Physical dilation pulls the family back to one fixed logarithmic Hilbert domain, continuously in operator norm, including prime thresholds.
- A direct sufficiently small positive seed, independent of external short-window positivity.
- No nonzero supported vector can be weak-null on a strictly larger support window.

These are analytic results already established on the correct carrier. They do not assume retained witness membership, simplicity of all zeros or background positivity.

## Positivity is downward closed

If b is in P and 0<a<b, every h in D_a has its unchanged physical/source inclusion in D_b. Hence
\[
Q_a(h)=Q_b(h)\ge0.
\]
Thus a is in P.

The direct positive seed makes P nonempty and A>0. If A=infinity, for every finite a there is a positive b>a, so all finite a are positive. If A is finite, every a<A likewise has a positive b between a and A or above a, by the definition of supremum and downward closure.

In particular, a window above a failed positive window cannot be positive. No oscillation of the lowest form sign is compatible with support inclusion, even though further eigenvalue crossings in indefinite windows are possible.

## Strictness below the aperture

Fix a<A and choose b>a in P. If h is in ker Q_a, then Q_a(h)=0 and support inclusion gives Q_b(h)=0. Nonnegativity of Q_b promotes the zero diagonal to the full mixed weak-null equation on D_b. The strict-enlargement theorem gives h=0.

Thus the nonnegative fixed-window Riesz operator has zero kernel. Since it is I+compact, it is strictly bounded below in the logarithmic norm. To see this directly, a unit sequence with quadratic tending to zero would satisfy A_a h_j->0; compactness of A_a-I would produce a strongly convergent unit subsequence with a kernel limit, contradiction. Therefore
\[
Q_a(h)\ge\eta_a E_{\log}(h),\qquad\eta_a>0.
\tag{1}
\]

Bounded positive sampling gives ||P_a h||^2<=L_a E_log(h) for finite L_a>0. Equation (1) and the exact source identity imply
\[
\|N_a h\|^2
\le\left(1-\frac{\eta_a}{L_a}\right)\|P_a h\|^2.
\]
The ratio lies in (0,1] because Q_a(h)<=||P_a h||^2 for nonzero h. Hence
\[
\|T_a\|\le\sqrt{1-\eta_a/L_a}<1.
\tag{2}
\]
The constants depend on a. There is no uniform strict gain as a approaches a finite endpoint or infinity.

This proves both the infinite-aperture branch and strictness below a finite aperture.

## A finite endpoint is positive and attained

Suppose A is finite. Choose a_j<A tending to A. In the fixed-domain dilated representation, all operators at a_j are nonnegative and converge in norm to the operator at A. The limit is nonnegative. Thus A belongs to P.

If the endpoint operator were strictly coercive, operator-norm continuity would preserve its strict positivity for some b>A. That would put b in P, contradicting the definition of A. Its lower spectral bound is therefore zero.

Since the endpoint operator is nonnegative I+compact, the same minimizing-sequence argument now supplies a nonzero unit kernel vector. Its physical dilation is a nonzero h in D_A with
\[
Q_A(g,h)=0\qquad(g\in D_A).
\tag{3}
\]
The kernel is finite-dimensional by compactness. All source coordinates belong to this actual h; no historical retained vector is renamed to obtain it.

The endpoint induced map is a contraction by positivity. For h in the nonzero kernel, (3) gives ||N_A h||=||P_A h|| with P_A h!=0. Thus ||T_A||=1.

More precisely,
\[
\ker(I-T_A^*T_A)=P_A(\ker Q_A).
\tag{4}
\]
Indeed the contraction defect is nonnegative. Its zero quadratic at k=P_A h is exactly Q_A(h)=0, which is equivalent to weak-nullity for this nonnegative form. Thus its unit-gain space is nonzero and finite-dimensional, canonically carrying the endpoint kernel.

## Both support endpoints must be saturated

Let h!=0 satisfy (3). Suppose its right collar has zero mass for some epsilon in (0,2A). Then its essential support lies in [-A,A-epsilon]. Translate by s=epsilon/2. The vector tau_s h is supported in
\[
[-A+\epsilon/2,A-\epsilon/2],
\]
a strict centered subwindow of D_A.

Logarithmic energy and the full form diagonal are translation invariant, so
\[
Q_A(\tau_s h)=Q_A(h)=0.
\]
Positivity of Q_A makes tau_s h weak-null on D_A. The strict-enlargement theorem, with its strict support margin, then forces tau_s h=0, contradiction.

A zero left collar is handled by the negative translation -epsilon/2. Thus both collar integrals are positive for every allowed epsilon.

More generally, if h were supported in any interval of length strictly less than 2A, translating that interval to the center would give the same contradiction. This proof requires neither a boundary trace nor a derivative.

## Every larger window has an explicit negative vector

For finite A choose any nonzero h in the endpoint kernel and any b>A. Its unchanged inclusion in D_b has Q_b(h)=0. Let
\[
r_b=A_b h
\]
be its logarithmic Riesz residual. The strict-enlargement theorem gives r_b!=0. This is a bounded form operator, not an assertion of an unbounded physical spectral domain.

Set
\[
s=\|r_b\|_{D_b}^2>0,\quad
d=|Q_b(r_b)|,\quad t=\frac{s}{s+d},\quad
v_b=h-t r_b.
\]
By the mixed Riesz identity,
\[
Q_b(v_b)
=-2ts+t^2Q_b(r_b)\le-ts<0.
\tag{5}
\]
Consequently
\[
\|N_b v_b\|>\|P_b v_b\|,
\qquad\|T_b\|>1.
\]
This proves strict failure in every larger window with an explicit actual carrier vector. Both analyses are its complete actual samples. Smooth negative approximants follow from the previously proved fixed-window graph density, if needed.

It does not assert that indefinite windows have no later kernels. A later kernel or unit-gain direction can coexist with ||T_b||>1. The first finite endpoint is the endpoint of positivity, not the only possible zero eigenvalue in the entire family.

## Exact remaining branch question

The original full-source unit interface is now equivalent to A=infinity. If A is finite, the correct carrier already produces an attained, finite-dimensional, support-saturated endpoint kernel and strict negative vectors beyond it. Same-vector inclusion necessarily produces a nonzero residual.

The preceding all-window equivalence shows that proving the lawful endpoint-null Gaussian upper theorem would exclude this finite endpoint and yield A=infinity. Neither this aperture theorem nor a quotient/completion change supplies that estimate.

Thus the remaining independent task is to exclude the finite saturated endpoint, or establish it with a lawful actual negative input. The theorem does not choose between those alternatives.

A selected-background B may have a different positivity aperture; dropping selected negative energy changes the form. No full-form translation covariance, endpoint unit gain or aperture identity is transferred to B silently.

## Validation and cursor

Analytic proof from the already proved actual carrier package, direct positive seed, norm continuity and strict-enlargement theorem. No new external result, numerical endpoint, asserted false-RH zero or RH conclusion. No Lean source/workflow change or new CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At fe4598a, define the canonical full-source positivity aperture A=sup{a>0: Q_a>=0 on D_a}. The direct seed makes A>0. Support inclusion makes positivity downward closed; norm continuity makes a finite endpoint positive and attained. Every a<A has strict logarithmic coercivity and actual positive-carrier gain ||T_a||<1. If A is infinite this holds at every finite window. If A is finite, Q_A has nonzero finite-dimensional kernel, ||T_A||=1 with attained unit-gain space P_A ker Q_A, and each nonzero endpoint mode has positive L2 mass in every collar at both support endpoints. At every b>A, the unchanged endpoint h has nonzero enlarged residual r_b, and h-t r_b is an explicit actual negative vector, so ||T_b||>1. Thus the full-source admissible apertures form exactly (0,A], or all finite windows if A=infinity; there are no later positive islands. This is a proved analytic dichotomy, not determination of whether A is finite. Later kernels in indefinite windows and selected-background variants are not excluded or conflated. Carrier/factorization custody is retained; the independent frontier is exclusion of a finite saturated endpoint, equivalently the global null-to-Gaussian-upper theorem. No RH conclusion, asserted endpoint existence, or new Lean/CI result. FULL TRANSPORT CLOSED remains open.
