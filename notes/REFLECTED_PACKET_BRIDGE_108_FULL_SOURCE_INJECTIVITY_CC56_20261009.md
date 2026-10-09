# RPB108 CC56 — Full original source separates finite polynomials; quantitative norm recovery remains open

Date 2026-10-09 UTC / 2026-10-08 Pacific. Starting Coupled CC55 `51f03a68ae57c10442c2042526207f3b637bf51f`; read-only source head `fb040acc4ceb06af9ad6bcb7c9d2db966ad39e38`. No NF20 source/action handoff was available at recovery. [Definitions](../docs/TERMINOLOGY_RPB108_FULL_SOURCE_INJECTIVITY_CC56.md) precede load-bearing use. This examines the existing finite native action, not general endpoint regularity or a restarted paused front.

**Analytic result from the exact original identities:** for every fixed a>0 and finite N, the complete physical high source map B(a,N)=Pi_(E(a,N)^perp)L_a on supported polynomials E(a,N) is injective. Consequently it has a positive qualitative finite-carrier lower frame constant. In particular the54-dimensional kernel of the TWO measured columns in CC55 is not a kernel of the COMPLETE source on E112.

**Limit:** no numerical lower frame constant, uniform degree bound or critical defect-relative rate is certified. Endpoint-log coefficient independence alone cannot give an L2 source norm lower bound; an exact analytic-remainder cancellation control proves why. No new original Schur sign or whole-domain aperture follows.

## 1. Actual finite-polynomial action and physical source

Use CC27's exact original symbol a_arch(xi)=Re psi(1/4+i pi xi)-log pi and off-diagonal kernel

\[
j(d)=\frac{e^{-d/2}}{1-e^{-2d}},\quad d>0,
\qquad a_0=\psi(1/4)-\log\pi.
\]

For a supported polynomial p and -a<x<a, the archimedean action is

\[
(L_{\rm arch}p)(x)=a_0p(x)
+\int_{-a}^{a}j(|x-y|)(p(x)-p(y))\,dy
+p(x)[J(a-x)+J(a+x)],
\tag{CC56.1}
\]

where the absolutely convergent tail primitive is

\[
J(t)=\int_t^\infty j(d)\,dd
=\operatorname{atanh}(e^{-t/2})+\arctan(e^{-t/2}).
\tag{CC56.2}
\]

To derive (CC56.1), subtract the digamma multiplier's value at xi0 in its inherited integral representation, use the cosine/translation formula with a positive lower cutoff, and split the zero-extended polynomial into inside/outside support. Inside, p(x)-p(y) cancels the1/d singularity. The outside contribution is precisely the two J tails. Formula (CC56.2) follows by integrating the positive geometric series, or differentiating it and checking the limit at infinity. There is no omitted local counterterm.

Add the complete original finite prime sum and the two signed poles:

\[
(L_ap)(x)=(L_{\rm arch}p)(x)
-\sum_{\log n<2a}\frac{\Lambda(n)}{\sqrt n}
 [\widetilde p(x+\log n)+\widetilde p(x-\log n)]
+e^{x/2}m_-(p)+e^{-x/2}m_+(p),
\tag{CC56.3}
\]

with tilde p the supported zero extension and m_plus/minus the original exponential moments. At log n=2a, translations vanish almost everywhere and may be included or omitted. Both orientations and both poles remain; positivity of the pole term is not assumed.

The inside integral is bounded for fixed polynomial p because |p(x)-p(y)|<=||p'||_infinity|x-y| and integral_0^infinity d j(d)dd is finite. J(t)=-(1/2)log t+analytic(t) near t0, hence J is locally square integrable. The translations and poles are also in physical L2. Thus L_a p is an actual supported L2 source. Equivalently the supported zero extension has bounded variation, so its Fourier transform is O(1/|xi|); multiplication by the logarithmic arch symbol remains in L2. This justification is restricted to these polynomial inputs.

The formula pairs with the inherited smooth form core and extends to all supported form tests by core density and form continuity. Therefore Q_a(p,k)=<L_a p,k>_2 on that full form domain. No bounded physical representation of Q on arbitrary inputs, unrestricted critical-vector domain, H1 trace, or null regularity is inferred.

## 2. Exact endpoint coefficient and full-source injectivity

Write j(d)=1/(2d)+r(d), with r real analytic at d0 and along the positive real axis. Splitting the inside integral at y=x shows that its1/(2d) part is a polynomial in x: polynomial differences divide by x-y exactly. Its r part is real analytic near either endpoint, by integrating finitely many polynomial factors against analytic primitives of r.

Near x=a, J(a+x) is analytic and J(a-x)+(1/2)log(a-x) is analytic across the endpoint. The finite prime translation panels have an endpoint collar with fixed support indicators, so each prime term there is polynomial or zero. The signed pole terms are analytic. Consequently

\[
L_a p(x)=-\frac12p(x)\log(a-x)+R_p(x)
\tag{CC56.4}
\]

on a positive-width right-endpoint collar, where R_p is real analytic across a. This uses the COMPLETE native action; the prime or pole terms cannot cancel its nonanalytic coefficient.

If B(a,N)p=0, then L_a p belongs to E(a,N) physically, and is equal almost everywhere to a polynomial q. The two analytic expressions on the open collar are continuous, so equality holds there pointwise. If p is nonzero, it has a finite endpoint vanishing order k. In s=a-x coordinates, the k-th derivative of p(a-s)log s contains a nonzero multiple of log s and diverges as s tends to0. The derivative of q-R_p stays bounded. This is impossible. Therefore p=0 and B(a,N) is injective.

This also excludes a finite supported polynomial eigenfunction of L_a at ANY physical eigenlevel mu: (L_a-mu)p=0 would imply Bp=0. Actual infinite supported eigenvectors need not be polynomials, so no original contact exclusion follows.

## 3. Finite phase independence and the qualitative frame

For unnormalized Legendre tests P_n(x/a), the coefficient of s^k in P_n(1-s/a) is

\[
t_{kn}=\frac{(-1)^k(n+k)!}{2^k(k!)^2(n-k)!a^k}
=\frac{(-1)^k}{2^k(k!)^2a^k}
\prod_{j=0}^{k-1}[n(n+1)-j(j+1)],
\tag{CC56.5}
\]

with value0 for k>n. For56 distinct same-parity n values and rows k0..55, this is a polynomial evaluation matrix in lambda_n=n(n+1). Its determinant is

\[
\left[\prod_{k=0}^{55}\frac{(-1)^k}{2^k(k!)^2a^k}\right]
\prod_{i<j}(\lambda_{n_j}-\lambda_{n_i})\ne0.
\tag{CC56.6}
\]

Multiplication by the native log coefficient -1/2 and by physical normalization factors preserves nonsingularity. Thus the full endpoint-log coefficient functions retain all56 parity coordinates; the limited measured columns do not exhaust that information. The [exact validator](../scripts/validate_native_full_source_injectivity_cc56.py) checks6272 factorial/product identities,14 smaller exact determinant replays, and the nonzero full Vandermonde products. These are algebraic checks, not evaluations of an infinite source Gram.

Since B(a,N) is a continuous linear map on a finite-dimensional carrier and is injective, compactness of its physical unit sphere gives

\[
\gamma(a,N):=\min_{\|p\|_2=1}\|B(a,N)p\|_2^2>0.
\tag{CC56.7}
\]

This constant is defined using the actual source and the fixed carrier, not an inverse retained Weil gap. For any fixed nonnegative finite defect/energy form D with D<=beta||.||_2^2, it implies ||Bp||_2^2>=(gamma/beta)D(p). At the positive E112 target one may also use beta=||A|| to obtain a qualitative A-relative full-source frame. No value of gamma is computed and no uniform bound as N grows is claimed. A finite-dimensional existence statement is not the requested quantitative uniform critical-frame theorem.

At53/50, the inherited C>=207/1000 on F112 gives a form Riesz inverse response. Injectivity also makes the corresponding FULL response Gram positive definite on E112, qualitatively. This supplies a lower sign, not its numerical eigenvalue and not the upper response estimate needed for A-Gfull>0.

## 4. Precise failure of endpoint-only norm recovery

Let ell(t)=log t on0<t<1 and Pi_M its physical projection onto polynomials of degree at most M. Its shifted Legendre moments are exactly

\[
\int_0^1\log t\,P_n(2t-1)\,dt=
\frac{(-1)^{n+1}}{n(n+1)}\quad(n\ge1),
\qquad\int_0^1\log t\,dt=-1.
\]

The original logarithm has squared L2 norm2. Exact orthogonal projection and telescoping yield

\[
f_M=\log t-\Pi_M\log t,\qquad
\|f_M\|_2^2=
2-\left[1+\sum_{n=1}^{M}\frac{2n+1}{n^2(n+1)^2}\right]
=\frac1{(M+1)^2}.
\tag{CC56.8}
\]

Every f_M has the SAME endpoint log coefficient1 and an entire polynomial analytic remainder, yet its source norm tends to0. The validator proves116 exact log moments and six norm controls through M1000. Therefore extraction of the singular coefficient alone is not a bounded L2 norm-recovery procedure, even with an analytic remainder. These controls are not original Weil source replacements; they isolate the inference failure when the arithmetic remainder is left uncontrolled.

Fixed-carrier injectivity is not contradicted: the actual finite-dimensional family has its particular arithmetic remainders. Quantitative certification must use those actual remainders or an adequate bound on their correlation; it cannot use only the endpoint determinant or the word 'analytic'.

## 5. Positive-level controls and remaining work

Subtracting mu times the WHOLE physical form changes L_a p by -mu p and does not change B(a,N)p, since p belongs to the retained carrier. It also does not change the endpoint-log coefficient. The validator uses actual NF18 pairings Q(e110,e112)>2/5 and Q(e111,e113)>1/2 and verifies eight exact native cross-pairing shift controls. The mechanism applies to shifted positive levels as well as level0; it cannot distinguish an original null by itself. Earlier genuine positive-eigenmode controls remain dependencies, not new arithmetic sign claims.

The next load-bearing task is a quantitative source/action or form-dual residual Gram estimate: after two high modes, Trest<A-G2 for the original Schur sign, together with the specified critical/defect uniformity for the lower-frame question. No numerical gamma, full inverse response, critical-space alignment or CC52 moment-carrier transfer is furnished here. Whole supported positivity stays21/20; target53/50 whole sign, all-cap leakage/frame bound, original contact exclusion, RH/F4 and Lean remain open.

[Validation](data/RPB108_FULL_SOURCE_INJECTIVITY_CC56_VALIDATION_20261009.json) distinguishes the analytic theorem from its exact algebraic and mechanism controls. No GitHub Actions or Lean proof is claimed. Historical finite-source and null-domain results are preserved; this is not a general endpoint-regularity restart.
