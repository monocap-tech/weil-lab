# RPB108 RC26 — exact metric scalar and rational trial enclosure

Date: 2026-10-10. Independent route-consolidation branch:
research/rpb108-route-consolidation.
Parent: 26e00ca8a1a945839ce34118384f8b735a04134b (RC25).
No other research branch is changed.

## Result

The scalar left open in RC25 is exactly

\[
c_R=-\gamma-\log(2\pi R).
\]

At B=11/10 and R=2B=11/5, exact rational arithmetic certifies

\[
-3.203794213 \le c_R \le -3.203306050.
\]

The width is 488163/10^9 < 1/2000. This evaluates the scalar component of the actual physical polynomial trial metric. It does not evaluate the compact kernel component, invert the metric, or certify the canonical Riesz head.

## Normalization and proof

Keep the RC24 Fourier convention exp(-2 pi i xi x). Define

\[
\ell(r)=2\int_0^\infty \frac{e^{-et}}{t^2+4\pi^2r^2}\,dt,\quad
k(r)=\frac1{2r}-\ell(r),\quad
F_R=\int_R^\infty\ell(r)\,dr,\quad K_R=\int_0^R k(r)\,dr.
\]

RC25 established local integrability of k and integrability of the tail of ell. Its scalar is c_R=1+2F_R-2K_R. Consequently

\[
c_R=1+\lim_{\epsilon\downarrow0}
\left[2\int_\epsilon^\infty\ell(r)\,dr-\log(R/\epsilon)\right].
\]

Tonelli's theorem and the elementary arctangent integral give, with q=2 pi epsilon,

\[
2\int_\epsilon^\infty\ell(r)\,dr
=\frac2\pi\int_0^\infty\frac{e^{-et}}t\arctan(t/q)\,dt
=\int_0^\infty\frac{e^{-eq u}}u A(u)\,du,
\quad A(u)=\frac2\pi\arctan u.
\]

Subtract E_1(eq)=integral_1^infinity exp(-eq u)/u du. The resulting integrand is dominated independently of q by an integrable function: A(u)/u <= 2/pi on (0,1), and (1-A(u))/u <= 2/(pi u^2) on (1,infinity). Since A(u)+A(1/u)=1, substitution u=1/v shows

\[
\int_0^\infty [A(u)-\mathbf1_{u\ge1}]\frac{du}{u}=0.
\]

Dominated convergence therefore yields
2 integral_epsilon^infinity ell = E_1(2 pi e epsilon)+o(1).

The external special-function input is NIST DLMF 6.2.1, 6.2.3 and 6.2.4:
https://dlmf.nist.gov/6.2.E4.
They give E_1(z)+log z -> -gamma for positive z -> 0.
Thus the limit above is -gamma-log(2 pi e R), and the initial 1 cancels log e=1. The result retains the Fourier factor 2 pi.

## Exact rational enclosure

The validator uses no floating-point arithmetic:

* Pi: Machin's identity pi=16 atan(1/5)-4 atan(1/239), with 32 alternating-series terms and next-term bounds. The tangent identity gives tan(4 atan(1/5)-atan(1/239))=1; the angle lies in (0,1), hence in (0,pi/2).
* Logarithms: for t=(x-1)/(x+1), x>=1, the first n terms of 2 sum t^(2j+1)/(2j+1) give a lower bound. The omitted tail is at most 2 t^(2n+1)/((2n+1)(1-t^2)).
* Euler's constant: H_N-log(N+1) < gamma < H_N-log N at N=2048. Integral comparison shows these sequences respectively increase and decrease to gamma. Compute log N=11 log 2 and log(N+1)=11 log 2+log(1+1/N).
* Combine the bounds monotonically for -gamma-log(2 pi R), then round outward to rational endpoints with denominator 10^9.

The harmonic bounds dominate the reported width. Greater accuracy can be obtained by improving the gamma enclosure; it is not needed for this milestone.

## Trial matrix consequence

Let D, S, W be the physical Legendre mass, singular metric and endpoint metric matrices assembled exactly in RC25. Define K to be the still unevaluated trial matrix of the integral kernel k(|x-y|). Then the complete physical trial metric is

\[
G=S+W+c_R D+K.
\]

The script constructs exact eight-dimensional matrices L=S+W+c_lower D and U=S+W+c_upper D. Since D is positive diagonal,

\[
L\preceq S+W+c_R D\preceq U,\qquad
U-L=\frac{488163}{10^9}D.
\]

Equivalently the complete metric lies between L+K and U+K. No positivity assertion is made for L or K. Positive pointwise kernel density alone does not imply a positive integral operator.

These matrices are physical polynomial trial components. They are not the canonical Riesz Gram M in RC22/RC23. Small weak Riesz residuals, actual native head and source matrices, and the whole-tail coupling gate remain unevaluated.

## Validation and standing

Run:

python scripts/validate_rpb108_rc26_metric_scalar.py

Result: PASS, 18 exact rational checks. Checks cover the Machin normalization, log and harmonic enclosures, scalar width, cutoff change, matrix symmetry and parity, and the positive semidefinite enclosure gap. The validator imports the previously committed RC25 assembler and RC23 exact PSD routine.

The original 1.06 certificate remains pinned at CC119, 5df347d3808ac3282864a657b7380e0f54bf4daa. This milestone neither extends that centered aperture nor establishes RH, F4, or a Lean theorem.
