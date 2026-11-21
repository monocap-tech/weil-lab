# PI030 — Generic transversality of three live n=3 prime/Gamma cancellations

**Weil-Lab Potential Interface. ANALYTIC FIRST / controlled research reopening.** Parent: research/pi029-unbounded-first-prime-cancellation-crossings. Existing PI027–PI029 theorems, source coefficients and uncertainty boundaries are unchanged. This stage proves a classical one-dimensional parameter-transversality theorem, plus exact rational sign-budget regression; it does **not** claim a Lean theorem, independently certified smooth integral, operator trace formula, complete spectral equivalence, global Weil positivity, or RH.

## 1. Exact fixed two-bump family and source quantities

Retain PI027's width d=log(10/9), gamma modes nu_n=2n+1/2, original von Mangoldt coefficient kappa=log3/sqrt3, physical kernel K(t)=exp(-t/2)/(1-exp(-2t)), and the pole-minus-prime-plus-Gamma signed form.

Take ell=d/100, Delta=d/2, x0=d/5, and the **explicit nonnegative** smooth flat bump
\[
b(x)=\begin{cases}
\exp\bigl(-1/[(x/\ell)(1-x/\ell)]\bigr),&0<x<\ell,\\
0,&\mathrm{otherwise}.
\end{cases}
\]
For each amplitude parameter \(u>0\), put
\[
\rho_u(x)=b(x-x_0)+u\,b(x-x_0-\Delta),\qquad
L_m=D\prod_{j=0}^{m-1}(D^2-\nu_j^2),\quad \eta_m=L_m b,\quad\phi_{m,u}=L_m\rho_u.
\]
Here \(m\ge1\), \(\nu_j=2j+1/2\), \(q_m=\int|\eta_m|^2>0\), and \(Q_m(t)=\int\eta_m(x)\eta_m(x-t)\,dx\). Since Q_m is compactly supported inside [-ell,ell], and Delta>2ell,
\[
\boxed{C_{m,u}(t)=(1+u^2)Q_m(t)+uQ_m(t-\Delta)+uQ_m(t+\Delta),\quad
J_{m,u}=(1+u^2)q_m.}
\]
Thus \(C_{m,u}(0)=J_{m,u}\), \(C_{m,u}(\Delta)=u q_m\); the correlation is exactly zero at \(t=\ell\) and \(t=\Delta\pm\ell\). The original pole moments are zero because each \(L_m\) has roots 0 and ±1/2. Source test autocorrelation, Hermitian conjugations and Fourier conventions are **unchanged** from PI027.

The translated physical tests may be placed inside the original full IV support [-11/10,11/10] by translating both constituents together by -1/2. This is **not** a claim that they occupy IV's narrow old collars, or that an IV finite certificate applies.

## 2. Exact positive gamma quadratic and isolated true prime window

Set \(R_b(v)=\int b(x)e^{vx}dx>0\) for real v and, for \(n\ge m\), define the strictly positive mode weight
\[
w_{m,n}(a)=e^{-\nu_n a}\,\nu_n^2
\prod_{j<m}(\nu_n^2-\nu_j^2)^2
R_b(\nu_n)R_b(-\nu_n)>0.
\]
For \(a>d\), absolute convergence and termwise smooth differentiation on compact a-intervals follow from spatial support separation \(a>\Delta+\ell\) and the original PI027 Gamma-mode expansion. Define
\[
G_m(a)=\sum_{n=m}^\infty w_{m,n}(a)>0,\qquad
H_m(a)=\sum_{n=m}^\infty w_{m,n}(a)\cosh(\nu_n\Delta)>0.
\]
The actual Gamma amplitude for \(\rho_u\) is the **exact** polynomial
\[
\boxed{B_{m,u}(a)=(1+u^2)G_m(a)+2uH_m(a)>0.}
\]
This follows from \(R_{\rho_u}(v)R_{\rho_u}(-v)=R_b(v)R_b(-v)(1+u^2+2u\cosh(v\Delta))\). It is not a numerical model.

For \(a=\log3-t\), \(0\le t\le d\), PI027's rational strict window inequalities \(3/(10/9)^2=243/100>2\) and \(3(10/9)=10/3<4\) show that **only** the literal original \(n=3\) von Mangoldt term may occur:
\[
\boxed{P_{m,u}(\log3-t)=\kappa C_{m,u}(t),\qquad \kappa=\frac{\log3}{\sqrt3}>\frac13.}
\]
No pole, contact, or other-prime edits are made. The original phase law is
\[
W(h_{\beta,m,a})=W(C_{m,u})+\Theta_{m,u}(a)\Re\beta,\qquad
\Theta_{m,u}=B_{m,u}-P_{m,u}.
\]

### A strictly uniform three-crossing sign budget

The physical support measure of \(\phi_{m,u}\) is at most \(2\ell=d/50\), though its diameter is larger. PI027's kernel/Cauchy–Schwarz estimate therefore gives, throughout the entire first-prime window,
\[
\boxed{0<B_{m,u}(a)<2\ell J_{m,u}<\frac{J_{m,u}}{450}.}
\]
The sign controls for **every u in [1/2,2] and every m≥1** are:

- At \(t=0\), \(P=\kappa(1+u^2)q_m>(1+u^2)q_m/3\), hence \(\Theta<-(149/450)(1+u^2)q_m<0\).
- At \(t=\Delta\), \(P=\kappa u q_m>u q_m/3\ge q_m/6\), while \(B<(1+u^2)q_m/450\le q_m/90\), hence \(\boxed{\Theta<-7q_m/45<0}\).
- At \(t=\ell,\Delta\pm\ell\), \(P=0\) exactly, so \(\Theta=B>0\).

The intermediate value theorem gives **at least three distinct roots** in the original PI028 brackets
\[
(\log3-\Delta-\ell,\log3-\Delta),\quad
(\log3-\Delta,\log3-\Delta+\ell),\quad
(\log3-\ell,\log3).
\]
All have \(B=P>0\). No numerical quadrature is used.

## 3. The new generic transversality theorem

**Theorem PI030 (classical).** For each fixed \(m\ge1\), for Lebesgue-almost every \(u\in(1/2,2)\), **every** zero \(a\) of \(\Theta_{m,u}\) in the first-prime window is simple:
\[
\boxed{\Theta_{m,u}(a)=0\ \Longrightarrow\
\partial_a\Theta_{m,u}(a)\ne0.}
\]
There are finitely many such zeros for a generic u, with at least three and an odd total count. Moreover, there exists one set \(U\subset(1/2,2)\) of **full Lebesgue measure** such that for every \(u\in U\), the conclusion holds **simultaneously for all integer orders \(m\ge1\)**. In particular one non-explicit positive amplitude u gives at least three live, transversal first-prime cancellations for every m≥1. No explicit rational u is certified by this theorem.

**Proof.** The only possible first-prime roots lie in two separated smooth sectors. Outside these sectors the prime correlation is exactly zero and \(\Theta=B>0\).

1. **Central sector** \(0\le t<\ell\): the satellite correlations vanish and
\[
\Theta_{m,u}(a)=(1+u^2)(G_m(a)-\kappa Q_m(t))+2uH_m(a).
\]
At any zero, elementary substitution gives the exact **parameter derivative at that zero**
\[
\boxed{(\partial_u\Theta_{m,u})(a)=
\frac{2H_m(a)(1-u^2)}{1+u^2}.}
\]
For every \(u\ne1\) this is nonzero because \(H_m>0\).

2. **Satellite sector** \(\Delta-\ell<t<\Delta+\ell\): only the shifted correlation survives,
\[
\Theta_{m,u}(a)=(1+u^2)G_m(a)+u(2H_m(a)-\kappa Q_m(t-\Delta)).
\]
At any zero, solve \(\kappa Q_m(t-\Delta)-2H_m(a)=(u+1/u)G_m(a)\). Then
\[
\boxed{(\partial_u\Theta_{m,u})(a)=G_m(a)(u-u^{-1}).}
\]
Again, for every \(u\ne1\) this is nonzero because \(G_m>0\).

To derive the generic conclusion without assuming anything about the sign, unimodality or root count of \(Q_m\), use the **one-dimensional Sard theorem**. On the central sector define
\[
F_c(a)=\frac{\kappa Q_m(\log3-a)-G_m(a)}{H_m(a)},\qquad
r(u)=\frac{2u}{1+u^2}.
\]
The zero equation is \(F_c(a)=r(u)\), and \(\partial_a\Theta=0\) at such a zero iff \(F_c'(a)=0\). The critical values of the smooth scalar function \(F_c\) have measure zero. The map r is a smooth local diffeomorphism on \((1/2,1)\) and \((1,2)\); hence the u-values producing a degenerate central root have measure zero.

Likewise on the satellite sector define
\[
F_s(a)=\frac{\kappa Q_m(\log3-a-\Delta)-2H_m(a)}{G_m(a)},\qquad
s(u)=u+u^{-1}.
\]
The zero equation is \(F_s(a)=s(u)\) and its degeneracy implies \(F_s'(a)=0\). Again Sard and the local diffeomorphism property of s away from u=1 give a measure-zero exceptional parameter set.

The finite union of the two null exceptional sets and \(\{1\}\) is null. No roots occur on the boundary of either sector because \(B>0\); no roots occur at the original first-prime window endpoints either. All roots are therefore contained in a compact interval with nonzero boundary values. For a regular u, the roots are discrete and hence finite. Every simple root reverses sign. Since the entire window starts positive (at a=log3-d) and ends negative (at a=log3), the finite total root count is odd. The three PI028 brackets each require at least one crossing.

Finally, take the countable union of the exceptional parameter sets over m=1,2,...; it remains Lebesgue null. This gives the **one common full-measure set U working for every m**, as claimed. QED.

**Topological stability.** For a fixed m, a parameter with only simple roots has an open amplitude neighborhood on which those roots persist with continuous, indeed differentiable local labels, and no new roots appear on the rest of the compact first-prime window. Thus the generic good parameter set is open dense and of full measure for each fixed m (all three sign brackets also persist uniformly throughout [1/2,2]). The simultaneous-all-m set is a countable intersection of such open dense sets; no uniform common neighborhood over all m is asserted.

## 4. Faithful complex spectral and real-place audit boundary

The exact Fourier transform of the phase difference \(D_a=h_{1,m,a}-h_{-1,m,a}\) is
\[
\boxed{\widehat D_a(z)=2\cos(az)\,\Xi_m(z)\Xi_m(-z)
[1+u^2+2u\cos(\Delta z)],}
\quad
\Xi_m(z)=\int\eta_m(x)e^{izx}dx.
\]
At a nontrivial zero \(\rho=\sigma+i\gamma\), the source argument is \(z_\rho=\gamma-i(\sigma-1/2)\), **not** a real argument unless the zero lies on the critical line. CP's full divisor test, with exhaustive noncentral multiplicities and source-normalization proved, would have to equal \(W(D_{a_*})=0\) on each cancellation. The printed Masullo Ch12/Ch13 matrix from PI027, if both unproved trace identities apply with the same source/Haar/cutoff domain, would instead require \(Z_{12}(D_{a_*})=0\), \(Z_{13,\mathrm{cap}}(D_{a_*})=2B_{m,u}(a_*)>0\). These are **conditional** zero-side fingerprints, not actual evaluations or new theorems about the manuscript.

## 5. Formalization, verified workflow scope, and next research tasks

**Exact regression**: scripts/pi030_transversality_quadratic_preflight.py checks, with Fraction arithmetic, the two C/J peak identities, support windows, uniform Gamma bounds, strict rational margins, the polynomial-elimination formulas for \(\partial_u\Theta\) at a zero, and the derivative/polynomial identities at multiple nonzero rational u and rational positive G,H. It does **not** execute Sard's theorem, compute actual smooth integrals, identify a numerical root, or compile Lean. The analytic theorem is the proof above, not a test output.

**Lean/source obligations, not yet certified**:
1. Re-pin the literal IV011/PI027 source normalization and Hermitian orientation; prove the true two-bump correlation decomposition and pole-moment annihilation in the original source test class.
2. Prove the physical Gamma mode sum with \(G_m,H_m>0\), absolute and C1-local uniform convergence on \(a>d\), the true \(n=3\)-only prime sampling window, and contact-free difference conditions.
3. Prove scalar quadratic identities and derivative-at-root identities as small Mathlib real-algebra lemmas; then bind them to actual PI original functions. Record named theorem targets, source SHA, genuine target .olean and standard-only #print axioms; no compiled assertion is made here.
4. Locate the precise available one-dimensional Sard/critical-values theorem in the frozen Mathlib version, or provide a dedicated classical proof before promising a Lean genericity theorem. The countable intersection of full-measure parameter sets is a separate formal step.
5. For a fixed explicit rational u and fixed m, design interval-certified \(Q_m,Q_m'\), \(G_m,H_m\) and derivatives to prove actual finite root counts and transversality. The present a.e.-u theorem does **not** certify a particular rational u.

**CI lineage and fan-out gate**: the parent PI029 branch has exactly 12 workflows: 8 with PR triggers, all path-scoped (formalization metadata, lean.yml, PI009–PI013 and PI017), plus 4 manual-only (PI014–PI016 and RPB108). The PI030 change introduces a documentation file and a new pi030 Python script, matching none of those 8 PR path filters, and no workflow file. No PR or workflow dispatch is part of PI030. A future PR against main must independently audit the **complete stacked diff** and source-scoped workflow lineage: its fan-out cannot be inferred from the two PI030 files, because the parent PI branch contains earlier Lean/CI history. Coordinate any substantial CI submission with NF and other tracks; preserve accepted numerical frontier 692/968 and strict standard-only axiom auditing.

**Highest-value next task — PI031:** identify a specific rational u and m (begin with m=1, u near 1), build validated derivative enclosures that prove all roots in the two compact sectors are simple, and recover the exact count, without introducing uncontrolled PR workflow fan-out. A local Python interval exploration and a source-only Lean algebra module can be prepared before any isolated, opt-in compilation.
