# NF412 — Correlated original source curvature and the near-zero archimedean kernel

**2026-10-31 PT. Canonical W-ODD-NEG, exact same original fourth u4.** Preserves NF370 242 selected+4 original critical source, J242 pole center NF404, original NF407 seven prime seams, true compact real digamma kernel on support B=11/10. No new source family, signed cells, domain transfer or RH claim.

## Previous / current / next

**Previous NF411:** exact original source-native negative u4'(B), seven nonzero prime derivative jumps, endpoint d log d regularity. True continuous z and NF404 full scalar remain OPEN.

**Current NF412:** source-correlated analytic second-derivative Gram for the original *combined* four-critical source, coupled with independently native-certified fourth exterior second derivative. This targets the old NF408 inner t<1e-10 omission, whose error had never been rigorously bounded. It is NOT a new blind Gauss screen.

**Next:** after confirming actual native CI and its computed bound, source-correlation-preserving enclosure of the remaining t∈[h,2(B+x)] physical integral and source cells 6,3,7 first, signed NF410 moments, then all 8 and NF404 C.

## A. Why source correlation is mandatory

Let f4=F*T*e4 be the original combined four critical source and w4=E*(I+Y0)*T*e4 the original exterior. Then u4=f4-w4. The four raw coefficients in f4 individually have magnitude about 1e92 and cannot be bounded separately before summation; an absolute-value triangle before source covariance produces astronomically false engineering bounds. NF412 combines the original 4 coefficients *exactly as dyadic rationals* at each of the 32 physical sine frequencies and at the one odd sinh pole, prior to Arb transcendental evaluation.

Let f4(x)=sum_j a_j sin(2*pi*freq_j*x)+b sinh(x/2). Its true coefficient-midpoint physical second derivative is sum_j -a_j(2*pi*freq_j)^2 sin(2*pi*freq_j*x)+(b/4)sinh(x/2). The full analytic Gram on [-B,B] is computable by:

S(c)=sin(2*pi*c*B)/(2*pi*c), S(0)=B,

int_-B^B sin(2*pi*a*x)sin(2*pi*b*x)dx = S(a-b)-S(a+b),

int_-B^B sin(k*x)sinh(x/2)dx =
 2*((1/2)*cosh(B/2)*sin(k*B)-k*sinh(B/2)*cos(k*B))/(1/4+k^2),

int_-B^B sinh(x/2)^2 dx = sinh(B)-B.

All full quadratic and mixed terms are kept before any upper bound. This is a rigorous analytic source covariance if outward Arb evaluates the complete contraction. The accepted NF374 original fourth exterior w4 second derivative has squared L2 under 9e-12. The NF407 4096-bit original selected/critical radii separately pay the full second derivative with an exact rational source sup S2; prior NF408 first derivative error is NOT silently reused for this stronger derivative order.

## B. Exact omitted tiny-t operator bound

For x∈[0,B], define d=B-x, t1=2d, h=10^-10, and

D_t u(x)=u(x)-[u(x+t/2)+u(x-t/2)]/2.

On t∈(0,min(h,t1)), the entire symmetric translate remains within the physical support. Its exact triangular second derivative representation gives

 ||1_{t<t1} D_t u||_{L2(0,B)}
 <= (t²/8)*||u''||_{L2(-B,B)}.

The original full arch kernel is K(t)=e^(-t/4)/(1-e^(-t)); for 0<t<=h<1/2, 0<K(t)<2/t. Minkowski then proves for the entire omitted physical I0 contribution, including its moving original support boundary:

 || int_0^min(h,t1) K(t)D_t u(x)dt ||_{L2(0,B)}
 <= h²/8 *||u''||_{L2(-B,B)}.

**This inequality is genuinely rigorous independently of Gauss nodes.** Its usefulness on the original source depends on authentic source-correlated f4 curvature, w4 curvature, and the full native coefficient second-derivative uncertainty. The focused native script contracts them and writes its actual bound, with no promotion unless its CI succeeds.

## C. What this does NOT certify

This small-t estimate only handles t<h in the *I0 symmetric kernel* portion of NF408's regularized arch expression. It does not rigorously integrate the remaining arch I0 and I1 integrals, the continuous prime translations, the x dependence on cells 6/3/7, the signed z/p cross, or the exact complete centered norm. It is NOT a z interval or a certified numerical quadrature as a whole. The original NF404 cap remains undecided.

The centered-energy norm budget must pay *both physical halves*: if the original positive-half small-t L2 cost is eta, its full odd support charge is sqrt(2)*eta; do not neglect this factor.

## D. Verification / custody

Code: `scripts/local_replay/nf412_original_correlated_small_t_gram.py`, native focused workflow `.github/workflows/nf412-original-correlated-small-t-arch.yml`. The code refuses to assert original full centered scalar or NF404 threshold. Source hashes and exact second derivative radius are mandatory. The actual source Gram numerical upper and status require inspection of focused Actions execution, not assumptions based on this note.

**Disposition before focused verification:** analytic small-t inequality established; source-native numerical contraction pending. True continuous z, full centered scalar, NF404 C, lowband J242 complement, domain/infinite inverse, W-ODD-NEG and RH OPEN.
