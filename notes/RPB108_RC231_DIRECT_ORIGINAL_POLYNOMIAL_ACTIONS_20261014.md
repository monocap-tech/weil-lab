# RPB108 — RC231: direct original polynomial actions in both parities

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC230: `5abf4006352a7def7aebd9c00e865e9a957aa56e`. Branch: research/rpb108-route-consolidation.

RC231 certifies finite polynomial approximations to the **actual original Weil D-energy action** on P0 and P1. It includes the original archimedean kernel, all seven active prime-power pairs, both signed poles, the actual D constant, and all omitted output. It also proves an exact cancellation that removes the canonical Poisson remainder from the direct original/augmented action formula.

| Exact input | Output cutoff | Complete squared D-error upper | Error norm / input D-norm upper |
|---|---:|---:|---:|
| P0, even | 64 | 0.002963 | 1.883% |
| P1, odd | 64 | 0.004071 | 3.400% |

Displayed bounds are rounded outward. The certificate stores exact rational bounds. Opposite parity errors pair to zero, giving a diagonal two-input error Gram and a uniform relative squared error below 0.001156 on every complex linear combination of P0 and P1. These are two polynomial operator tests, not the two RC115 auxiliary adjoint sources, an exhaustive 639-channel calculation, or an augmented inverse-response certificate. RC228's canonical inverse width 0.485647 remains separate and preserved.

## Exact cancellation and full-domain identity

Use the physical supported L2 space, canonical metric action L, D=J+sI, s=c_R+log2+r and r=789/125. Put h(x)=-(1/2)log(1-(x/B)^2). RC118 and RC121 give on polynomials and then on the common form domain V:

\[
 L=D+h-rI+\mathcal R,
 \quad \mathcal R=\chi\mathcal F^{-1}
       \log(1+e/|\xi|)\mathcal F\chi.
\]

Here R is the bounded supported-input extension; it is not claimed to be a bounded ambient Fourier multiplier. RC46 supplies the **original** archimedean identity

\[
 L_{\rm arch}=D+h-rI-K_{\rm reg},
 \quad (K_{\rm reg}q)(x)=\int_{-B}^B r_{\rm reg}(|x-y|)q(y)\,dy,
\]

with r_reg(t)=exp(-t/2)/(1-exp(-2t))-1/(2t), continuously extended at zero. Subtracting the two forms gives exactly

\[
 \boxed{K_{\rm arch}=-K_{\rm reg}-\mathcal R.}
\]

The singular harmonic, endpoint, and constant pieces cancel in the bounded remainder. Both remaining operators are bounded on physical supported L2: R by its inherited supported-input estimate, K_reg by its continuous compact kernel. The equality extends from the dense polynomial form core by continuity. It has no fitted constant or new frequency normalization.

Let G0 be the physical original Weil form and N0 its D-Riesz representative. With the original prime and signed-pole operators,

\[
 \boxed{N_0=I+D^{-1}[h-rI-K_{\rm reg}+K_{\rm prime}+K_{\rm pole}],}
\]

and RC230's fixed rational augmentation has

\[
 N=N_0+\lambda D^{-1}\widehat F^*\widehat F.
\]

These are bounded form operators on V. The endpoint term is bounded in D energy by RC121's h<=D; every physical bounded term maps to V through its D-Riesz representative. On polynomial inputs the displayed physical actions exist in L2, including the endpoint logarithms. No physical unbounded composition is assumed on arbitrary vectors.

The direct formula needs neither a canonical M action nor a Poisson approximation to R: R cancels exactly when M and the original archimedean remainder are assembled. Computing them separately would introduce avoidable numerical errors into this representation. This changes the action implementation, not the original operator or the augmentation. It does not establish a runtime advantage or transfer RC228's M inverse to N.

## Regular convolution and endpoint action

RC46 pins the degree-192 polynomial r_192(t)=sum_(p=0)^192 a_(p+1)t^p and its uniform error epsilon_reg=(375/4)(11/15)^193. Its physical convolution error is at most 2B epsilon_reg. The validator independently regenerates all coefficients by the alternative exact division

\[
 z j(z)=\frac{e^{-z/2}}{2[(1-e^{-2z})/(2z)]}.
\]

For t=x/B and c_p=a_(p+1)B^(p+1), the exact model actions are

\[
 K_{192}P_0=\sum_p\frac{c_p}{p+1}
 [(1+t)^{p+1}+(1-t)^{p+1}],
\]

\[
 K_{192}P_1=\sum_p c_p\left\{
 \frac{t[(1+t)^{p+1}+(1-t)^{p+1}]}{p+1}
 +\frac{(1-t)^{p+2}-(1+t)^{p+2}}{p+2}\right\}.
\]

The code evaluates their complete Legendre expansions exactly. It uses the rational moment

\[
 \int_{-1}^1t^kP_n(t)dt
 =\frac{2k!}{(k-n)!!(k+n+1)!!}
\]

when k>=n and k-n is even, and zero otherwise. Direct polynomial integration independently checks the first twelve projected coefficients. The omitted regular-source physical norm is the exact mass-weighted sum of every expansion coefficient beyond degree 64, rounded outward. It is below the stored 10^-60 grid allowance for both tests. The actual kernel error is paid separately.

For q=P_j, j=0,1, the nonnormalized endpoint coefficients are

\[
 [P_n](hP_j)=\frac{2n+1}{|n-j|(n+j+1)}\quad(n\ne j, n\equiv j\pmod2),
\]

and the diagonal is 2H_(2j)-2H_j+1/(2j+1)-log2. Opposite parity coefficients vanish. The positive 100-term atanh series supplies an independent rational log2 enclosure. Above K=64, using 2n+1<=3(n-j), H_n+s>=s_lower and the integral bound for sum (n-j)^-3 gives

\[
 \|D^{-1}(I-\Pi_K)hP_j\|_D^2
 \le\frac{3B}{s_{\rm lower}(K-j)^2}.
\]

The whole infinite endpoint output is paid; a finite projected source alone is not treated as an actual action.

## Complete prime action, including moving support errors

RC43's pinned active powers are exactly 2,3,4,5,7,8,9. For each n=p^k, ell=log n and c=log p/sqrt n, the actual paired source is

\[
 -c[\widetilde q(x+\ell)+\widetilde q(x-\ell)],
\]

where q tilde is zero extended. The validator uses the midpoint of each certified rational ell and c interval as a nominal source. Fourteen oriented terms produce fifteen physical segments. It integrates their **sum**, retaining all cross-prime terms, to obtain the exact nominal source norm and all Legendre coefficients through degree 64. It verifies the reflected parity relation on every segment and independently checks each segment's squared norm by affine integration on [0,1].

The omitted physical squared norm is the total exact nominal squared norm minus the mass-weighted sum of all retained exact coefficients. This difference is checked nonnegative before outward rounding. Since D is diagonal,

\[
 \|D^{-1}(I-\Pi_K)f\|_D^2
 \le\frac{\|(I-\Pi_K)f\|_2^2}{H_{n_{\rm first}}+s_{\rm lower}},
\]

where n_first is the first omitted degree of the correct parity.

Moving the translation changes its zero-extension boundary. For a polynomial with support supremum A and physical derivative supremum C, a shift uncertainty delta gives

\[
 \|\tau_\ell\widetilde q-\tau_{\ell_0}\widetilde q\|_2^2
 \le2\delta A^2+2B\delta^2C^2.
\]

The first term pays the two boundary strips; the second pays the shared interior by the mean-value estimate. Here A=1 and C=j/B. Each orientation contributes at most delta_c||q||_2+c_upper sqrt(2 delta A^2+2B delta^2 C^2). The code sums both orientations and all seven powers in norm. It does not treat support endpoints as exact or silently replace log n by a rational number.

The complete prime arithmetic error is below 1.317e-39 in squared D energy after division by s_lower. The dominant prime cost in these tests is finite output truncation, approximately 0.001590 even and 0.002402 odd in squared D energy. These are upper enclosure costs, not lower bounds on actual error.

## Signed poles and full error assembly

In even parity K_pole q=+2 cosh(x/2)<cosh(x/2),q>_2; in odd parity K_pole q=-2 sinh(x/2)<sinh(x/2),q>_2. Both signs are retained. The validator replaces each function by its degree-40 Taylor polynomial, computes its moment against P_j exactly, and projects the resulting polynomial source exactly.

With exp(B/2)<2 and tau=2(B/2)^41/41!, each function error has supremum at most tau, and the actual versus model rank-one operator norm is at most 16B tau. Thus the physical action error is at most 16B tau||P_j||_2. Both the Taylor proof and the model coefficient supremum use positive rational series bounds. No negative odd pole is dropped from the action.

For each retained coefficient the actual s interval comes from RC129's P0 D-Gram divided by 2B. The code encloses division by H_n+s using all endpoint quotients and handles negative numerators explicitly. Its finite rational center is rounded downward on a 10^-60 grid; its radius and finite D-energy error are paid with the upper D weights. The identity contribution P_j is added exactly.

The error assembly contains seven squared components: finite arithmetic/constant rounding, infinite endpoint output, regular polynomial output, prime output, regular kernel approximation, prime parameter/support uncertainty, and pole Taylor approximation. It adds their upward norm bounds before squaring. No unproved component orthogonality is assumed. Physical errors are squared and divided by the exact positive s_lower before taking an upward square root; dividing by an upward square root of s_lower would underpay the error.

Parity is the one proved orthogonality used: both actual and trial actions preserve reflection, so the even and odd **complete errors** have zero D pairing. Their full two-input error Gram is therefore bounded by the diagonal of the two total squared errors. Dividing by the corresponding exact input D-energy lower bounds proves the all-combinations relative contract.

## Boundary and next action

The certified map is N0 on span{P0,P1}. Its approximations are physical polynomial vectors interpreted in the actual D metric. They are neither canonical Riesz images nor responses to the full frequency source map. The exact identities apply to the whole form domain, but numerical execution covers only these two polynomial inputs.

For arbitrary polynomial inputs, the same direct formula uses exact polynomial convolution, paired shifted polynomials on the complete prime partition, signed exponential moments, and RC121's general endpoint tail. Every new input and output truncation must receive its own error certificate. The present two-column errors cannot serve as a full 639-channel or iterative action bound.

RC232 should add a paid action of lambda D^-1 Fhat*Fhat and extend this original action interface to actual response trials/full-range residual contracts. RC230's exact rank and solver bridge remain available. The chosen augmented inverse response, its full frequency metric/norm below one, and Stage I assembly are still open. No original positivity, Stage I, F4, Lean or RH conclusion is made.

```bash
python scripts/validate_rpb108_rc231_original_polynomial_action.py --output certificates/rpb108_rc231_original_polynomial_action.json
python scripts/validate_rpb108_rc231_original_polynomial_action.py --output certificates/rpb108_rc231_original_polynomial_action.json --replay
```

Replay reverses pin and segment accumulation order, checks alternate exact kernel division and direct projection controls, and requires exact equality with the complete certificate. Publication adds only the validator, certificate and this note. Expected-head non-force update, remote comparison and recursive tree readback must preserve every existing blob and check the new additions for conflict markers; this is not a whole-repository content scan.
