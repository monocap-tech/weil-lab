# RPB108: actual native Legendre matrix pilot

Base: research 2baadf8626a4295b0e614be1a788cbfd94616310.

## Outcome and status

An eight-vector actual native matrix was evaluated at a=1/4,1/2,3/4,1. The truncated numerical matrices have positive smallest Rayleigh values, some very small. This supplies no negative witness, exact null vector or whole-domain positivity certificate.

The finite computation is exploratory. Quadrature, special-function evaluation, floating-point accumulation and eigenvalue errors are not rigorously enclosed. Repeating quadrature at twice the node count is a diagnostic, not an error certificate.

The omitted Fourier tail has a proved analytic expression below. Its conservative floating evaluations exceed the reported smallest gaps. A separate one-sided positive-tail condition is available, but it does not validate the finite computation or extend positivity beyond the chosen trial space.

Script: scripts/explore_native_legendre_matrix.py.
Recorded output: notes/data/RPB108_LEGENDRE_MATRIX_PILOT_20261005.json.

## Terminology before use

**Legendre trial vector:** supported, physical L2-normalized polynomial vector v_n below, with actual native form-domain membership.

**Truncated native matrix:** actual native multiplier pairing integrated only to a frequency cutoff, plus the native pole pairing.

**Pilot Rayleigh value:** numerical eigenvalue in the physical L2-orthonormal trial basis. It is not an eigenvalue of the full logarithmic Riesz operator.

## Lawful physical basis and Fourier coordinates

Let P_n be the ordinary Legendre polynomial. Define
\[
v_n(x)=\sqrt{\frac{2n+1}{2a}}P_n(x/a)1_{[-a,a]}(x),
\quad 0\le n\le m.
\]
These are orthonormal in physical L2. With Fourier convention exp(-2pi i x xi),
\[
\widehat v_n(\xi)=\sqrt{2a(2n+1)}(-i)^n j_n(2\pi a\xi),
\tag{1}
\]
where j_n is the spherical Bessel function. This follows by integrating the Legendre polynomial against the exponential on [-1,1].

For fixed n, j_n(z)=O(1/|z|). Hence integral w|Fourier(v_n)|^2 is finite; v_n belongs to D_a even though its boundary jumps need not give H1 regularity. Trial vectors and their linear combinations therefore have lawful actual P,N analyses. No raw synthesis preimage or physical unbounded-operator domain is required.

## Actual matrix formula

Write
\[
m_a(\xi)=\Re\psi(1/4+i\pi\xi)-\log\pi
-2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
\cos(2\pi\xi\log n).
\]
The matrix is
\[
Q_{ij}=\int_{\mathbb R}
m_a(\xi)\overline{\widehat v_i(\xi)}\widehat v_j(\xi)\,d\xi
+M_-(v_i)M_+(v_j)+M_+(v_i)M_-(v_j).
\tag{2}
\]
For this real basis,
\[
M_+(v_n)=\sqrt{2a(2n+1)}i_n(a/2),\quad
M_-(v_n)=(-1)^nM_+(v_n),
\]
where i_n is the modified spherical Bessel function. These are the exact native pole formulas; their numerical evaluations are not certified intervals.

The computation uses z=2pi a xi, integrates the positive frequency side and doubles it, retaining the phase cos(pi(i-j)/2). Opposite parities have zero mixed pairing. The prime-power lists at the four apertures are respectively empty; {2}; {2,3,4}; and {2,3,4,5,7}.

## Proved omitted-tail bound

For real z>0, the spherical Hankel identity is
\[
h_n^{(1)}(z)=\frac{(-i)^{n+1}e^{iz}}z
\sum_{k=0}^n
\frac{i^k(n+k)!}{k!(n-k)!(2z)^k}.
\]
It is verified from n=0 and n=1 using the three-term spherical recurrence. Pairing the numerator factors gives
(n+k)!/(n-k)!<=[n(n+1)]^k, so
\[
|j_n(z)|\le|h_n^{(1)}(z)|
\le z^{-1}\exp(n(n+1)/(2z)).
\]
For z>=max{1,m(m+1)}, every n<=m therefore has |j_n(z)|<=2/z. Equation (1) yields
\[
|\widehat v_n(\xi)|\le b_n/|\xi|,\quad
b_n^2=\frac{2(2n+1)}{\pi^2a},
\]
when 2pi a|xi| exceeds that threshold.

The actual bound |m_a|<=w+10+S_a and
\[
\int_T^\infty\frac{\log(e+t)}{t^2}\,dt
=\frac{\log(e+T)}T+\frac1e\log(1+e/T)
\le\frac{\log(e+T)+1}T
\]
give, for the omitted trial-space multiplier matrix,
\[
\|Q-Q^{(T)}\|\le
\frac{4(m+1)^2}{\pi^2aT}
[\log(e+T)+11+S_a].
\tag{3}
\]
The pole is included in both matrices and has no omitted-tail term.

This is a proved analytic bound. The script's double-precision evaluation of its expression is illustrative, not a directed-rounding interval. The script enforces the required Bessel cutoff condition.

## One-sided tail information

The preceding Euler estimate also gives
\[
\Re\psi(1/4+i\pi\xi)-\log\pi
\ge\log|\xi|-\frac1{2|\xi|}.
\]
Thus, if
\[
\log T-S_a-1/(2T)\ge0,
\tag{4}
\]
the full native multiplier is nonnegative for |xi|>T. The omitted trial matrix is then positive semidefinite:
Q>=Q^(T).

A rigorously positive enclosure of the truncated matrix would consequently certify positivity on this trial space under (4). It would still not certify all of D_a. The general norm bound (3) remains useful for a potential negative certificate, where a negative trial value must dominate both integration and omitted-tail errors.

## Recorded exploratory arithmetic

The cutoff is zmax=8192, degree m=7, and each panel has width at most pi. The reported matrix uses 64 Gauss-Legendre nodes per panel; 32 nodes supplies the repeat diagnostic.

| a | Smallest truncated pilot value | 32/64-node matrix difference | Float evaluation of tail bound |
|---|---:|---:|---:|
| 1/4 | 0.0334082292 | 1.15e-8 | 0.38913 |
| 1/2 | 5.01805e-6 | 6.69e-12 | 0.39485 |
| 3/4 | 1.08252e-6 | 2.93e-14 | 0.42582 |
| 1 | 8.43081e-8 | 1.87e-14 | 0.47801 |

These values describe finite truncated matrices in a physical orthonormal basis. Small values may reflect trial-space cancellation and do not establish approximate native weak-nullity. No inference about the full logarithmic operator's kernel is made.

The positive pilot signs are not promoted to proof. A low-degree search cannot exclude a negative vector outside the trial space. Tiny numerical values are not actual endpoint evidence.

## What is now concrete

Actual finite arithmetic is reproducible on lawful vectors; it is no longer only a representation of unevaluated form entries. The run also identifies the remaining numerical proof work: validated finite-interval integration, special functions, pole moments, rounding and spectral enclosures, plus an adequate whole-domain complement estimate if all-domain positivity is the goal.

The recorded run provides none of those missing sign certificates. It does not instantiate the fresh negative-input constructor, restore enlarged weak-null transport or prove the signed Gaussian upper condition.

## Validation and cursor

Executed under Python with SciPy 1.17.0. Numerical diagnostics are explicitly exploratory. Analytic basis membership and omitted-tail bounds are proved in this note. Lean source/workflow is unchanged; no new Lean/CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 2baadf8, an actual native finite-matrix pilot evaluates eight explicit L2-normalized Legendre vectors supported in [-a,a] at a=1/4,1/2,3/4,1. Their Fourier transforms are sqrt(2a(2n+1))(-i)^n spherical_jn(2pi a xi), proving logarithmic-domain membership without H1 or spectral-domain assumptions. The matrix includes actual digamma, finite prime-power multipliers and unchanged cross-pole moments. At zmax=8192 the smallest truncated numerical Rayleigh values are about .0334082, 5.01805e-6, 1.08252e-6 and 8.43081e-8; all are exploratory. Repeated 32/64-node quadrature agrees but has no validated error enclosure. A proved omitted-tail expression is 4(m+1)^2[log(e+T)+11+S_a]/(pi^2 a T), T=zmax/(2pi a); its floating evaluations are about .389,.395,.426,.478 and exceed the small gaps. The native tail is positive semidefinite whenever log T-S_a-1/(2T)>=0, yielding a one-sided restricted-matrix bound, but finite integration/special-function/roundoff errors are not certified. No actual negative witness, exact null, whole-domain positive certificate or endpoint exclusion was obtained. The pilot supplies reproducible actual matrix arithmetic and identifies the validation gap, not a global sign proof. Same-vector source custody remains lawful; no RH conclusion or new Lean/CI result. FULL TRANSPORT CLOSED remains open.
