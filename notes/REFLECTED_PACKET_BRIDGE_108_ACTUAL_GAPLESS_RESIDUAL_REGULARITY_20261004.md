# RPB108: actual gapless residual and derived logarithmic regularity

Base: research d4dd68fb9df79636ceec9433bb12909ed3079db4.

## Result

Let h in D_a be an actual full-native endpoint weak-null vector:
\[
Q_a(v,h)=0\quad(v\in D_a).
\]
Then the genuine multiplier core
\[
T_h=\mathcal F^{-1}(m_a\widehat h)
\]
is represented globally by an L2 function, with
\[
\|T_h\|_2\le K_a\|h\|_2.
\tag{1}
\]
In particular physical multiplier-domain membership is derived from endpoint nullity, not assumed.

With w(xi)=log(e+|xi|) and the certified |m_a-w|<=C_a,
\[
\|w\widehat h\|_2\le(K_a+C_a)\|h\|_2.
\tag{2}
\]
Thus the endpoint mode has squared-logarithmic Fourier energy.

The actual residual q=T_h+p_h is locally L2, zero a.e. on (-a,a), exponentially weighted L1 for every weight rate sigma>1/2, and represents the genuine action on all compact smooth tests. Its support gap is zero: the source window and central cancellation window both have radius a.

This is an actual residual constructor on the same physical vector. It does not instantiate a record requiring a strict larger central window.

## Terminology before use

**Gapless actual residual:** q=T_h+p_h, zero on the actual endpoint interior, with c=a. No strict separation between source support and residual support is asserted.

**Squared-logarithmic energy:** the finite integral int w(xi)^2|Fourier(h)(xi)|^2 dxi. It is not H1 regularity.

**Exterior multiplier core:** the L2 function obtained from the actual off-support archimedean kernel and finite prime translations on |x|>a.

**Derived physical multiplier-domain membership:** m_a Fourier(h) in L2, proved by the interior/exterior equation and endpoint-removability argument below.

## Actual off-support kernel

The certified Euler series is
\[
\psi(z)=-\gamma+\sum_{n\ge0}
 \left(\frac1{n+1}-\frac1{n+z}\right).
\]
For b=n+1/4,
\[
\mathcal F^{-1}\left[\Re\frac1{b+i\pi\xi}\right](v)
 =e^{-2b|v|}.
\]
Indeed express the reciprocal as int_0^infinity exp(-bt-i pi xi t) dt, take the symmetric real part, and use physical shifts t/2 in the fixed Fourier convention.

Constant terms are supported at v=0 and contribute nothing when the test support is separated from h. Summing the geometric series gives the off-diagonal archimedean kernel
\[
k_{\rm arch}(v)=-\frac{e^{-|v|/2}}{1-e^{-2|v|}},
\qquad v\ne0.
\tag{3}
\]
The -log pi term is likewise local and absent off support.

For completeness, passage from finite Euler sums to the multiplier action is legitimate. Their values at xi=0 are uniformly bounded, and their increments from zero are the nonnegative sums
\[
\sum_{n=0}^N
 \frac{\pi^2\xi^2}{b(b^2+\pi^2\xi^2)}.
\]
These are bounded by the full increment, hence by C+w. Weighted Cauchy-Schwarz dominates their pairing with h and a Schwartz test. On separated compact supports the summed physical kernels converge absolutely, giving (3) there. Arbitrary compact exterior tests have positive separation from [-a,a].

This normalization also agrees with the official digamma integral DLMF 5.9.16:
https://dlmf.nist.gov/5.9.E16
The off-support kernel and the estimates here are derived in this note, not quoted as a zeta-specific theorem.

With the finite right-limit prime cutoff unchanged, the exterior core is
\[
v_{\rm ext}(x)=
-\int_{-a}^a
 \frac{e^{-|x-y|/2}}{1-e^{-2|x-y|}}h(y)\,dy
-\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
 \bigl(h(x-\log n)+h(x+\log n)\bigr),
\quad |x|>a.
\tag{4}
\]
The sum uses the actual prime-power set, including equality thresholds. This is the multiplier core; the pole is added separately.

## Exterior L2 bound by weighted Schur

Put Ck=1/(1-e^(-2)). For v>0,
\[
\frac{e^{-v/2}}{1-e^{-2v}}\le\frac{C_k}{v}.
\tag{5}
\]
For v<=1 use concavity 1-e^(-2v)>=(1-e^(-2))v. For v>=1 use v e^(-v/2)<=2/e<=1 and the lower bound 1-e^(-2) on the denominator.

At the right boundary write x=a+d and y=a-r. Then d>0, 0<=r<=2a, and the absolute kernel is bounded by Ck/(d+r). Extend h(a-r) by zero to r>2a.

The Carleman operator with kernel 1/(d+r) is L2 bounded by pi. Here is the weighted Schur proof:
\[
\int_0^\infty\frac{r^{-1/2}}{d+r}\,dr
 =\pi d^{-1/2},\qquad
\int_0^\infty\frac{d^{-1/2}}{d+r}\,dd
 =\pi r^{-1/2}.
\]
Weighted Cauchy-Schwarz followed by Tonelli gives operator norm at most pi. Applying it to |h| proves the right exterior archimedean norm is at most pi Ck ||h||_2. The left exterior is identical, giving combined bound sqrt(2) pi Ck ||h||_2.

Translations preserve L2 norm. If
\[
S_a=2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n},
\]
the finite prime part in (4), restricted to the exterior, has norm at most S_a||h||_2. Therefore
\[
\|v_{\rm ext}\|_{L^2(|x|>a)}
 \le(\sqrt2\pi C_k+S_a)\|h\|_2.
\tag{6}
\]
This includes arbitrarily close approach to the boundary; no support gap is used.

## Interior equation and endpoint removability

The actual compact-action dictionary and endpoint nullity give, as distributions on (-a,a),
\[
T_h=-p_h,
\qquad
p_h(x)=M_-(h)e^{x/2}+M_+(h)e^{-x/2}.
\tag{7}
\]
The pole moments obey the supported bounds already proved, so
\[
\|p_h\|_{L^2(-a,a)}\le4a e^a\|h\|_2.
\tag{8}
\]

Define v globally by -p_h on (-a,a) and v_ext on the exterior. Equations (6)--(8) show v is L2, with norm at most
\[
K_a\|h\|_2,\qquad
K_a=\sqrt2\pi C_k+S_a+4a e^a.
\]
The distributions T_h and v agree away from the two endpoints. It remains to exclude an endpoint-supported difference.

The symbol envelope implies T_h belongs to H^(-1/4): the supremum of |m_a(xi)|^2/(1+xi^2)^(1/4) is finite. This fact follows already from h in L2 and logarithmic symbol growth. Since v is L2, S=T_h-v is also in H^(-1/4), and its support is contained in {-a,a}.

For any fixed compact smooth phi, choose a smooth chi_epsilon equal to one near these points and supported in collars of width O(epsilon). Scaling gives
\[
\|\phi\chi_\epsilon\|_2\le C_\phi\epsilon^{1/2},
\qquad
\|\phi\chi_\epsilon\|_{H^1}\le C_\phi\epsilon^{-1/2}.
\]
Fourier Holder interpolation yields
\[
\|\phi\chi_\epsilon\|_{H^{1/4}}
 \le\|\phi\chi_\epsilon\|_2^{3/4}
       \|\phi\chi_\epsilon\|_{H^1}^{1/4}
 \le C_\phi\epsilon^{1/4}\longrightarrow0.
\]
Because S is supported at the endpoints, S(phi)=S(phi chi_epsilon). H^(-1/4) continuity now forces S(phi)=0. Hence S=0.

This excludes hidden endpoint point masses without assuming boundary traces or importing a point-supported distribution decomposition. We have proved T_h=v globally, and therefore (1). Fourier unitarity proves m_a Fourier(h) in L2. The symbol envelope then proves (2).

## The actual residual constructor

Set q=T_h+p_h. The proved equations give
\[
q(x)=
\begin{cases}
0,&|x|<a,\\
v_{\rm ext}(x)+p_h(x),&|x|>a.
\end{cases}
\tag{9}
\]
Endpoint values can be chosen arbitrarily without changing its function class. Since T_h is globally L2 and the pole is smooth, q is locally L2.

For every sigma>1/2,
\[
\int_{\mathbb R}|q(x)|e^{-\sigma|x|}\,dx
 \le C_{a,\sigma}\|h\|_2<\infty.
\]
For T_h use L2 Cauchy-Schwarz against the weight. For the pole use its exp(|x|/2) bound. Thus the residual is also locally integrable and has lawful exponential growth control.

For every compact smooth test u,
\[
\mathcal A_a(h;u)=\int u(x)q(x)\,dx.
\tag{10}
\]
This is a genuine same-vector weak realization derived from the actual multiplier and pole, not a supplied representation field. The identity also holds for the Gaussian cutoff tests with their separately proved pole integrability.

Its central vanishing window is exactly the endpoint window. The historical NeutralIntegralGrowthResidual interface requires strict c<a; this construction has c=a and does not satisfy that field. The canonical aperture theorem shows a nonzero first-contact mode has no smaller physical support radius to substitute.

## What Gaussian upper estimate actually follows

For the exact project g_R=K_R*h,
\[
\|g_R\|_2^2=\int\beta_R^2|\widehat h|^2\le M_R,
\quad \beta_R=e^{-(2\pi\xi-R)^2/R}.
\]
Equation (1) and L2 pairing control the core by K_a||h||_2 sqrt(M_R). The exact Gaussian pole moments give the earlier bound
\[
|\operatorname{pole}_R|
 \le4a e^a e^{-R+1/(4R)}\|h\|_2^2.
\]
Consequently
\[
|\mathcal A_a(h;\overline{g_R})|
 \le K_a\|h\|_2\sqrt{M_R}
 +4a e^a e^{-R+1/(4R)}\|h\|_2^2.
\tag{11}
\]

Combine with actual Gaussian coercivity and put L=log R-C'_a. For L>=1, there is an explicit finite B_a with
\[
L M_R\le K_a\|h\|_2\sqrt{M_R}
 +B_a(1+\log R)e^{-R/4}\|h\|_2^2.
\]
Young's inequality absorbs half of L M_R, giving
\[
M_R\le\frac{K_a^2}{L^2}\|h\|_2^2
 +\frac{2B_a(1+\log R)}{L}e^{-R/4}\|h\|_2^2.
\tag{12}
\]
This is a proved logarithmic upper bound. It is consistent with a nonzero compactly supported mode and does not supply the exponential estimate needed for the one-sided zero theorem.

## Exact frontier after this chunk

The actual residual constructor, local regularity and physical multiplier-domain membership are now derived analytically for endpoint-null vectors. No retained raw-coordinate preimage or prior operator-domain assumption is needed.

The remaining issue is not whether the endpoint action has a lawful function representative. It is whether independent endpoint information supplies much stronger boundary-collar smallness than (11)--(12), enough for exponential decay and null exclusion. The zero support gap prevents automatic use of the old strict-gap residual estimate.

No actual endpoint vector is asserted to exist. These are conditional deductions from its lawful native weak-null equation. No RH conclusion or FULL TRANSPORT CLOSED follows.

## Validation and cursor

Analytic proof from the certified Euler digamma identity, exact Fourier normalization, explicit weighted Schur calculation, finite prime translations, endpoint nullity, and the shrinking-cutoff H^(-1/4) removability argument. DLMF 5.9.16 was checked as the primary normalization reference. No new Lean source/workflow change or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At d4dd68f, the certified digamma Euler series gives the actual off-support archimedean kernel -exp(-|v|/2)/(1-exp(-2|v|)), with the finite native prime translations retained. Weighted Schur on the Carleman kernel 1/(d+r) proves the exterior multiplier core is L2 with norm<=K_a||h||_2. For an actual endpoint weak-null vector, the interior core equals minus the exact pole. The global core lies in H^(-1/4); shrinking endpoint cutoffs of H^(1/4) norm tending to zero exclude any hidden point-supported remainder. Thus the actual core is globally L2, physical multiplier-domain membership is derived rather than assumed, and ||w Fourier(h)||_2<=(K_a+C_a)||h||_2 proves squared-logarithmic energy. The exact residual q=core+pole is locally L2, zero inside (-a,a), exponentially weighted L1 for every rate>1/2, and represents the genuine compact action of the same vector. Its gap is zero (c=a), so the historical strict-gap interface is still unavailable. L2 pairing with the actual Gaussian proves M_R<=K_a^2||h||_2^2/(log R-C'_a)^2 plus explicit exponential error. This constructs the genuine residual and proves regularity/logarithmic decay, not the missing exponential upper estimate. No endpoint existence, RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
