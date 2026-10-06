# RPB108: Bessel tail damping resolves the 41/50 estimator obstruction

Base: `3a5b8b5360d1a899eb651846267f568dde6103ce`.
Definitions: [damped actual complement](../docs/TERMINOLOGY_RPB108_DAMPED_COMPLEMENT_082.md).

## Result

At a=41/50, the actual 84-moment complement has physical coercivity c=3/5. With beta=5/3, the pinned complete actual residual Gram certifies corrected margin tau=10^-18. The complete native domain therefore satisfies

\[
Q_a(h)\ge \frac{3}{246000000000000000005}\|h\|_2^2
>10^{-20}\|h\|_2^2,
\]

and

\[
Q_a(h)\ge \frac{3}{56580000000000000001180}E_{\log}(h)
>5\cdot10^{-23}E_{\log}(h).
\]

The actual whole-domain positivity frontier advances from 81/100 to 41/50. Fixed-aperture weak null modes are excluded and the existing WD-T10 full-source unit-domination consequence applies there. This supplies no global endpoint exclusion, historical selected-packet attachment, or F4 closure.

## A proved damping bound before the Bessel turning region

Let j_n be the regular spherical Bessel function and D_n=(2n+1)!!. Its series gives j_n(x)~x^n/D_n at zero. Put w_n=x*j_n(x). The spherical Bessel differential equation gives

\[
w_n''=(n(n+1)/x^2-1)w_n.
\]

For n>=1, w_n and w_n' are initially positive. While x<=sqrt(n(n+1)) and w_n>0, this equation makes w_n''>=0. Its derivative stays positive, so a first zero of w_n in that interval is impossible. This proves positivity of j_n throughout the required region; it is not a conjectural zero-location assumption.

Set F_n(x)=D_n*j_n(x)/x^n, with F_n(0)=1. Direct substitution gives

\[
F_n''+\frac{2n+2}{x}F_n'+F_n=0,
\qquad
-F_n'(x)=x^{-2n-2}\int_0^x t^{2n+2}F_n(t)\,dt.
\]

The origin boundary term is zero by the regular series. Positivity makes F_n' negative. Hence F_n(t)>=F_n(x) for t<=x, and

\[
-F_n'(x)/F_n(x)\ge x/(2n+3).
\]

Integrating from zero proves

\[
0<j_n(x)\le \frac{x^n}{D_n}
\exp\!\left(-\frac{x^2}{2(2n+3)}\right),
\quad 0<x\le\sqrt{n(n+1)}.
\]

The global undamped bound |j_n(x)|<=|x|^n/D_n follows independently from the positive-weight integral representation, by taking the absolute value inside its integral. The differential equation, regular series and Legendre integral normalization are recorded in NIST DLMF [10.47.1](https://dlmf.nist.gov/10.47.E1), [10.53.1](https://dlmf.nist.gov/10.53.E1), and [10.54.1–2](https://dlmf.nist.gov/10.54). The damping inequality above is derived here from them, rather than quoted as a numerical black box.

## Attachment to the actual physical complement

For the physical orthonormal Legendre basis on [-a,a], the squared plane-wave tail norm is

\[
\|P_{W_k}e^{2\pi itu}\|_2^2
=2a\sum_{n\ge k}(2n+1)j_n(2\pi at)^2.
\]

Cauchy–Schwarz therefore bounds the Fourier low-band mass of every f in the actual moment complement W_k by the integrated tail norm times ||f||_2^2. Integrating the undamped bounds over [-T,T] gives

\[
4aT\sum_{n\ge k}\frac{(2\pi aT)^{2n}}{D_n^2}.
\]

With pi<=22/7, consecutive terms have ratio at most Y^2/(2k+3)^2, which is bounded by the slightly larger existing ratio Y^2/[(2k+1)(2k+3)], Y=2a(22/7)T. Thus the existing rational B(a,k,T) remains a valid integrated majorant.

Use a=41/50, k=84, T=67/5, q=87/100 and N=16. Exact pi bounds verify (2a*pi_upper*T)^2<84*85, so all degrees 84 through 99 lie in the proved positive region over the whole frequency band. On the outer band qT<=|t|<=T their squared damping factor is at most exp(-z), where

\[
z=(2a\pi_{\rm lower}qT)^2/201.
\]

The positive 61-term Taylor sum for exp(z) gives an exact reciprocal upper bound for exp(-z), rounded outward to E. Splitting the frequency band and the degrees yields the complete bound

\[
\rho_{\rm damp}
\le B(a,84,qT)+E B(a,84,T)+B(a,100,T).
\]

The first term covers all degrees in the inner band; the second covers degrees 84–99 in the outer band; the third covers every remaining degree in the outer band. None of the infinite tail is omitted. The bound is approximately 0.001900178170772948 and is strictly below 1/500. This pass certifies the fixed aperture; it does not assert a uniform damping factor for a varying aperture.

The existing actual archimedean bounds, signed pole estimate and joint prime-2/4 and prime-3/5 operator bounds now give

\[
c_{\rm raw}=\log(T)-\frac{7}{216T^2}
-\left(\frac{27}{5}+\log(T)-\frac{7}{216T^2}\right)\rho_{\rm damp}
-\text{pole loss}-\text{joint prime loss}>3/5.
\]

Its displayed value is approximately 0.6029670153703083. All load-bearing bounds are exact rational endpoints. The logarithmic complement bound 9/100 and prime graph controls remain checked by the original complement constructor. Four invalid damping parameter/domain controls reject.

## Reuse of the complete actual Gram and whole-domain conversion

The complete source, outward native matrix and full Gram from the base commit are pinned by SHA256. All original endpoint logarithms, nine panels, 7,056 source/native pairings, 84-coordinate projection and mixed terms are retained. The same exact delta=eta(2M+eta) is deducted; it is not discarded when changing beta.

All 84 outward pivots of Q84-(5/3)Rhat84-((5/3)delta+10^-18)I are positive on the 160-digit grid. The lift squared norm bound is beta^2*(trace_upper(Rhat84)+delta), below 9^2. With J=9, c=3/5 and tau=10^-18, the inherited exact scalar norm conversion gives mu=tau*c/[tau+c(1+J^2)]. Its comparison matrix has nonnegative diagonal entries and determinant mu^2>0. Twice this coefficient has a negative determinant and is rejected. The actual Garding conversion gives kappa=mu/[10(mu+23)].

The earlier beta=2 certificate remains intact: its negative estimator direction and positive native energy were correct. A stronger complement bound changes the sufficient estimator and resolves that obstruction. No actual negative native vector was inferred from it.

## Validation and reproduction

Two fresh complement runs and two fresh 160-digit sign/conversion runs each agree byte for byte. The independent validator checks all four input hashes and rechecks all 84 positive pivots after widening to an 80-digit grid. A negative diagonal control rejects.

Independent exact alternating-series enclosures for F_n at n=84,99 and x=60,70 verify the squared damping bound. Their tail terms are decreasing after the retained finite partial sum, giving valid signed remainder enclosures even though the early terms need not decrease. All 644 checked differential-equation coefficient identities hold. A factor-two overly strong damping exponent is rejected in each case. These finite controls verify arithmetic and conventions; the analytic differential inequality is proved above, not mechanically formalized by the controls. The full-domain and logarithmic conversions also pass independent checks. Two validation reports agree byte for byte.

From the repository root:

```sh
python scripts/certify_native_prime5_damped_complement84_082.py > notes/data/RPB108_PRIME5_DAMPED_COMPLEMENT84_082_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_damped_schur84_082.py > notes/data/RPB108_PRIME5_DAMPED_SCHUR84_082_CERTIFICATE_20261006.json
python scripts/certify_native_prime5_damped_schur84_082.py > /tmp/damped-schur082-repeat.json
python scripts/validate_native_prime5_damped_082.py /tmp/damped-schur082-repeat.json
```

The complete original source and Gram need no reconstruction for this pass. Constructors, both new certificates, validation report, definitions, proof and current cursor are committed together and read back exactly. Historical notes remain immutable. No Lean, axiom or workflow changes and no requested CI run. Global endpoint exclusion, historical packet attachment, F4 and FULL TRANSPORT CLOSED remain open.
