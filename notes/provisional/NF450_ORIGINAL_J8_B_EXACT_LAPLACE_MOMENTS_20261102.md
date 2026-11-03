# Weil-Lab — NF450 original J8 +B endpoint through exact physical-source Laplace moments

**2026-11-02 PT. New analytic scheme and source-native implementation, pending focused GitHub verification and inspection of the actual output.** Do not promote sign, J7/J8 whole integrals, or RH from implementation alone.

## Previous cursor → current circle → next bold

NF449 **ACCEPTED** complete true original compact J8 B endpoint interval \(I_B\in(-0.898539855169746522,-0.897056442188713196)\) and \(z(B)\in(-0.000741706943258307,+0.000741706037775019)\). Width is entirely governed by a conservative physical-source \(H^2\) composite-midpoint error, not the native Arb precision. The tiny diagnostic center near \(-4.5\times10^{-10}\) is *not* a sign certificate.

NF450 exploits a different **exact** property of the same original kernel, without enlarging the physical source support, invoking non-original images, or requiring \(10^7\) midpoint nodes.

Let \(B=11/10\), \(a=1/10\), \(b=22/5\), \(v=U(B)\), and
\[
K(t)=\frac{e^{-t/4}}{1-e^{-t}}
=\sum_{m=0}^{\infty}e^{-(m+1/4)t}\quad(t>0).
\]
The original remaining endpoint integral is
\[
I_{\rm rem}=\frac12\int_a^b K(t)[v-U(B-t/2)]\,dt.
\]
As in NF448/NF449, this is original NF407 **242 selected + four critical exact dyadic 4096-bit source coefficients**, 32 critical sine frequencies, all **273** consolidated frequency/order groups, and the original odd sinh pole; unchanged NF406 genuine support and NF447 all true prime-power shifts/center. Here the physical arguments \(B-t/2\in[-B,21/20]\subset[-B,B]\). There is no exterior physical \(U_{\rm ent}\).

## Exact integrated oscillator source, not a discretized shadow

The original source generator is \(c_{f,k}y^k \sin(2\pi fy)\) for even \(k\), or \(c_{f,k}y^k\cos(2\pi fy)\) for odd \(k\). The physical substitution \(y=B-t/2\) sends \(a\mapsto y_a=21/20\) and \(b\mapsto y_b=-11/10\).

For a fixed authentic \(f>0\), \(m\ge0\), put \(\lambda=m+1/4\), \(\omega=2\pi f\) and \(\zeta=2\lambda+i\omega\). Define the exact polynomial recurrence
\[
P_0(y;\zeta)=\frac1\zeta,\qquad
P_k(y;\zeta)=\frac{y^k-kP_{k-1}(y;\zeta)}{\zeta}.
\]
Then \((d/dy+\zeta)P_k=y^k\), and thus the complete fixed-source finite moment is
\[
\boxed{
\int_a^b e^{-\lambda t}(B-t/2)^k e^{i\omega(B-t/2)}\,dt
=2\left[
e^{-\lambda a+i\omega y_a}P_k(y_a;\zeta)
-e^{-\lambda b+i\omega y_b}P_k(y_b;\zeta)
\right].
}
\]
Real/imaginary parts recover the genuine cosine/sine source, with each original source coefficient multiplied *before the full source sum*. Each term has an outward 4096-bit Acb/Arb interval. The original \(c_{\rm pole}\sinh(y/2)\) is included exactly by the difference of exponential integrals with rates \(\lambda\pm1/4\); the \(m=0\), \(\lambda-1/4=0\) case is the exact primitive \(b-a\). The shared \(v=U(B)\) term has the exact primitive \((e^{-\lambda a}-e^{-\lambda b})/\lambda\). No empirical Gauss rule or formal limiting interchange is needed: the m-series is uniformly absolutely convergent on \([a,b]\) after the original compact-source derivative bound.

## Independent analytic tail and radius charge

The already accepted NF413 full original \(\|U''\|_2<256\) and NF445 exact native \(|U'(B)|<1\) imply
\[
\|U'\|_{\infty,[-B,B]}<400,\qquad
|v-U(B-t/2)|<200t.
\]
For any integer \(M\ge1\), with \(\lambda_M=M+1/4\), the **uncomputed original-source geometric tail** obeys
\[
|I_{\rm rem}-I_{\rm rem}^{(M)}|
\le100\sum_{m=M}^\infty\int_a^b t e^{-\lambda_m t}\,dt
<\frac{100e^{-\lambda_M a}}{1-e^{-a}}
\left(\frac a{\lambda_M}+\frac1{\lambda_M^2}\right).
\]
Use the strict rational facts \(e>8/3\) (first four exponential terms) and \((1-e^{-a})^{-1}<1+a^{-1}=11\). Since \(e^{-\lambda_M a}\le e^{-\lfloor\lambda_M a\rfloor}<(3/8)^{\lfloor\lambda_M a\rfloor}\), this produces the *exact rational, no floating transcendental* bound
\[
\boxed{
R_M=1100(3/8)^{\lfloor\lambda_M/10\rfloor}
\left(\frac{1}{10\lambda_M}+\frac1{\lambda_M^2}\right).
}
\]
\(M=320\) gives \(R_{320}<8.29\times10^{-15}\); \(M=384\) gives \(R_{384}<1.92\times10^{-17}\).

Original dyadic coefficient-radius uncertainty is separately overcharged by \(10^6S_0\). This is justified on the true physical interval because source basis differentiation satisfies \(|\delta U'(y)|<10000S_0\) for \(|y|\le B\), whence \(|\delta v-\delta U(B-t/2)|<5000tS_0\), and \(tK(t)<1+t\le27/5\); integrating over length \(43/10\) yields \(<58050S_0<10^6S_0\). All 273 authentic sources remain correlated until final Arb summation, prior to this independent input-radius charge.

The original NF448 rigorously certified \([0,a]\) Taylor/Cauchy prefix and NF447 certified all known physical nonintegral terms are SHA-pinned and added with outward exact rationals. The *already ACCEPTED* original NF449 full \(I_B\) and \(z(B)\) enclosures are used as independent real-axis Sobolev cross-checks (neither used to tune the method).

## Verification and promotion conditions

1. Native archive SHA-256 for original NF445, NF447, NF448, NF449 must match immutable receipts; original NF407/NF406 exact source/seam hashes and NF413 curvature must agree.
2. The exact complex polynomial recurrence must pass rational differential-identity checks through \(k=13\).
3. The 384-series and independent shorter 320-series enclosures, including their distinct exact rational tails and original-source radius, must overlap; complete 384 result must overlap independent accepted NF449 real Sobolev enclosure.
4. The resulting full source \(z(B)\) interval width must be \(<10^{-14}\), with sign classified **only by its endpoints** (not the approximate midpoint, not a numerical extrapolation).
5. Original \(D_7,D_8\), physical \(\int pz\) and \(\int z^2\), principal \(E_p\), original NF410/NF404 global scalar, W-ODD-NEG, even/whole Weil and RH remain **OPEN** regardless of endpoint sign.

The immutable focused CI and raw JSON custody will determine whether the method meets these conditions. No main merge. The canonical machine-readable active_obligation remains **W-ODD-NEG**, with this NF work only a scoped physical-response dependency.
