# RPB108 RC74 — actual projected archimedean transfer

RC74 certifies a physical-to-canonical norm upper for the archimedean remainder after the actual rank-38 native projection. The previous full-operator allowance 6.43 times sqrt(rho) is replaced, after projection only, by at most 1.0633270724 times sqrt(rho), with rho=252/257.

Keeping the existing 22 source inputs, RC71's nominal source residual, RC67's Riesz error enclosure, and RC73's projected pole allowance, the actual rank-38 residual upper improves from 4961/1024 to 4379/2048, approximately 2.13818359375. This is a further 5543/9922, approximately 55.8658%, tightening of the certified upper.

## Actual operator and projection interface

Use the established Fourier convention exp(-2 pi i xi x), interval I=[-B,B] with B=11/10, and canonical weight w(xi)=log(e+|xi|). RC66 identifies the bounded physical archimedean remainder with the compression to I of

\[
m(\xi)=\operatorname{Re}\psi(1/4+i\pi\xi)-\log\pi-\log(e+|\xi|).
\]

Its global modulus is at most K=643/100. Let J extend a physical input by zero to the real line. For u in L2(I),

\[
K_{\mathrm{arch}}u=\left.\mathcal F^{-1}(m\,\mathcal F Ju)\right|_I.
\]

Let i be the physical embedding from the canonical carrier. Its adjoint satisfies ||i*||<=sqrt(rho). The actual projection Pi38 contains i*p for every physical polynomial p of degree at most 37. Consequently, an arbitrary polynomial approximation to the physical output can be subtracted before applying (I-Pi38)i*. No actual projection coefficients need to be evaluated.

The **frequency-split polynomial subtraction** below means approximating the low-frequency physical output by a degree-37 polynomial, while bounding the remaining high-frequency multiplier. Its coefficients can depend linearly on the unknown input; their existence is enough for the projection norm estimate.

## High-frequency multiplier modulus

RC66's analytic Euler cell estimate gives, for x=|xi|>0 and z=1/4+i pi x,

\[
|\psi(z)-\log z|\le1/(2x).
\]

Also pi x <= |z| <= pi(e+x). Therefore

\[
-\log(1+e/x)\le\log|z|-\log\pi-\log(e+x)\le0.
\]

Taking absolute values, rather than only the lower estimate used in RC66, gives

\[
|m(\xi)|\le\log(1+e/|\xi|)+1/(2|\xi|).
\]

This upper decreases with |xi|. For a frequency cut L>0, define

\[
h_L=\log(1+e/L)+1/(2L).
\]

The restricted high-frequency output has physical norm at most h_L times the L2 norm of the high-frequency Fourier input. Directed upper enclosures replace e and the logarithm in the executable calculation.

## Low-frequency polynomial subtraction

For real t, the integral Taylor remainder gives

\[
\left|e^{it}-\sum_{n=0}^{37}\frac{(it)^n}{n!}\right|
\le\frac{|t|^{38}}{38!}.
\]

Indeed the 38th derivative of exp(it) has modulus one, and integrating the absolute Taylor remainder kernel gives 1/38!. No exp(|t|) factor is needed.

On the band |xi|<=L, substitute this polynomial for exp(2 pi i xi x) in the inverse Fourier output. The resulting output

\[
p_u(x)=\sum_{n=0}^{37}\frac{(2\pi i x)^n}{n!}
\int_{-L}^{L}\xi^n m(\xi)\widehat{Ju}(\xi)\,d\xi
\]

is a physical polynomial of degree at most 37. Every coefficient exists by Cauchy-Schwarz on the finite band. For real inputs the conjugate symmetry gives a real polynomial; parity is preserved as well. Thus (I-Pi38)i*p_u=0 exactly.

The difference between the low-frequency output and this polynomial has kernel

\[
m(\xi)\left(e^{2\pi i\xi x}
-\sum_{n=0}^{37}\frac{(2\pi i\xi x)^n}{n!}\right).
\]

Its operator norm is bounded by its Hilbert-Schmidt norm. Integrating the squared remainder over x in [-B,B] and xi in [-L,L] yields

\[
\ell_L^2\le
\frac{K^2(2\pi)^{76}}{(38!)^2}
\frac{2B^{77}}{77}\frac{2L^{77}}{77}
=\frac{4K^2BL(2\pi BL)^{76}}{(38!)^2\,77^2}.
\]

This integrated bound is substantially sharper than replacing both variables by their maximum magnitudes over the rectangle. The executable uses a rational upper enclosure for pi and evaluates the resulting rational expression exactly.

## Combining the two frequency regions

The low- and high-frequency Fourier inputs are orthogonal in L2. If their norms are a and b, the physical remainder norm is at most ell_L a+h_L b, and hence at most sqrt(ell_L^2+h_L^2) times sqrt(a^2+b^2). Plancherel identifies sqrt(a^2+b^2) with ||u||_phys. Consequently,

\[
\|(I-\Pi_{38})i^*K_{\mathrm{arch}}u\|_{\mathrm{can}}
\le\sqrt{\rho}\,\beta_L\|u\|_{\mathrm{phys}},
\qquad\beta_L\ge\sqrt{\ell_L^2+h_L^2}.
\]

There is no assumption that the two output errors are orthogonal. The combination uses orthogonality of the input frequency regions and Cauchy-Schwarz.

The validator checks the rational frequency cuts 2, 41/20, 21/10, 43/20, and 11/5. The selected cut is 43/20. Its certified components are:

| Quantity | Certified upper, approximately |
|---|---:|
| High-frequency multiplier modulus h_L | 1.049831364941 |
| Low-frequency remainder norm squared ell_L^2 | 0.0285185679073 |
| Projected archimedean norm divided by sqrt(rho) | 1.0633270723163 |

The exact selected projected factor is 531663536158121118803181942413 / 500000000000000000000000000000. It is an outward root ceiling. No continuous optimization or optimality claim is made. The global physical archimedean norm bound remains 6.43; only the actual projected operator is sharpened.

## Projected source transfer and residual

The combined projected transfer norm divided by sqrt(rho) is now beta_arch+k_prime+beta_pole,p. RC73's projected pole bounds remain paid. The full paired-prime physical operator bound remains unchanged. The correlated physical Riesz error Gram, nominal operator approximation error, and trial physical Gram are unchanged.

The validator recomputes the projected canonical transfer Gram using the same source-transfer Young parameter 1/65536. Exact PSD checks prove a whole-matrix improvement over RC73's projected allowance. Retaining RC73's residual Young parameters also gives a whole-matrix residual-upper improvement.

A new rational parameter grid then gives:

| Parity | Selected residual Young parameter | Certified relative residual upper |
|---|---:|---:|
| Even | 1 | 4379/2048 |
| Odd | 1 | 1045/512 |

After final outward rounding, exact PSD comparisons with RC67's actual canonical 22-input Gram lower certify

\[
\Gamma_{38}^{(22\text{ inputs})}\le(4379/2048)M_{22}.
\]

The optimized upper is certified through parity factors. Whole-matrix dominance is claimed for the version with unchanged parameters and is not assumed for all reoptimized candidates.

## Independent replay and evidence boundary

Replay verifies e through a rational Taylor series, pi through independent Machin arctangent bounds, and every logarithm through a positive atanh series with an explicit tail. It reconstructs the low-frequency squared remainder through the separate exact x and xi moments, checks the root ceilings, reconstructs trial physical masses by weighted sums, and verifies transfer and residual comparisons after inverse Chebyshev-to-Legendre congruences. The certificate is reproduced exactly.

The analytic projection argument is supplied above, with the RC66 multiplier lemma as its dependency. No new Lean formalization is asserted.

The remaining paired-prime transfer is the next component whose projection-sensitive behavior is uncertified. The polynomial subtraction proved for the archimedean multiplier and the finite-rank pole does not by itself supply such a bound for paired translations. The nominal source residual is also still paid. The large remaining upper factor does not prove actual scalar-budget failure.

RC74 certifies no scalar source-budget success, rank-38 source-budget failure, enlarged positive Weil floor, complete 38-input covariance, complement floor at rank 38, negative Weil direction, full 1250 projection, aperture positivity, RH, or F4. The existing 22-input scope and actual 38-feature projection are retained. Historical milestone files remain unchanged.
