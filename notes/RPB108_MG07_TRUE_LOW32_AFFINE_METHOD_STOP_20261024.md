# NF — Whole-original low-frequency 2,240-cell signed affine stopping test

**October 24, 2026; W-ODD-NEG OPEN.** The focus is a method-specific necessary gate for the original **J-only** 470-source Ritz/SM40-cap sufficient proof method. This note distinguishes a *new implemented exact-rational attempt* from a certified pass. Acceptance requires SUCCESS of [the dedicated exact low32 workflow](../.github/workflows/rpb108-mg07-original-low32-method-stop.yml), including a strict positive final rational lower bound. The full 470-source positive/negative Loewner, augmented SI29 484-trial, signed odd operator and even/RH are **not** certified by this calculation.

## Scalar inequality

On the original odd physical carrier \(H=L^2([-B,B])_{\rm odd}\) with \(B=11/10\), keep the inherited actual signed seven-prime/digamma multiplier \(m(\xi)\), the real full-negative \(K_-=(\kappa-m)_+\), the pole-free \(A_o=\max(\kappa,m)\), and the pole-conditioned \(A_\star=A_o-2ss^*\). Thus for any original physical coefficient ray \(f\),
\[
\begin{aligned}
\langle f,(K_--\theta A_\star)f\rangle
=&\ 2\int_0^{32}w_\theta(m(\xi))|T_f(\xi)|^2d\xi\\
 &+\underbrace{2\int_{32}^{\infty}w_\theta(m(\xi))|T_f(\xi)|^2d\xi}_{\ge -\theta T_{\rm high}}+
 \theta\,2|\langle f,s\rangle|^2,
\end{aligned}
\]
where \(T_f(\xi)=\int_{-B}^Bf(x)\sin(2\pi\xi x)\,dx\) and
\[
w_\theta(z)=(\kappa-z)_+-\theta\max(\kappa,z)
=\begin{cases}(1-\theta)\kappa-z,&z\le\kappa,\\-\theta z,&z\ge\kappa.\end{cases}
\]
Set \(\theta=97/100\), a strictly stronger rational comparison than the passing original SM40 \(\theta_{\rm SM40}=0.96991358\ldots<0.97\). The \(\xi>32\) negative penalty is bounded by the **previously certified TRUE physical** two-source endpoint-cancelled original SM41 positive tail. The exact physical pole correction is the previous SI12/SI18 rational interval.

A strict **positive** result certifies
\[
 \langle f,K_-f\rangle>\frac{97}{100}\langle f,A_\star f\rangle
 >\theta_{\rm SM40}\langle f,A_\star f\rangle
\]
assuming \(A_\star(f)>0\), established from SI29's inherited coercivity. Since \(K_{\rm cap}^{\rm SM40}\succeq K_-\), it excludes the source-only J470-Ritz/SM40-cap criterion \(\theta A_J-C_J\succeq0\): congruence through the full invertible source-only Ritz map would force the opposite inequality on every actual source ray. It **does not** establish \(\langle f,(A_\star-K_-)f\rangle<0\), exclude other trial spaces, or speak to RH.

## Original signed multiplier enclosure at rational endpoints

For each rational \(q\in[0,32]\), compute exact outward endpoint intervals for **all seven original signed prime powers** by SI06's already established phase-certified \`prime_interval(q)\`. Reconstruct the original quarter-digamma archimedean term
\[
 a(q)=-C+\sum_{k=0}^{\infty}
 \frac{y^2}{(k+\frac14)((k+\frac14)^2+y^2)},\quad
 y=\pi q,\quad C=\gamma+\frac{\pi}{2}+3\log2+\log\pi .
\]
Do **not** reuse the very loose \(\gamma\) bound \(57/100<\gamma<29/50\). An elementary harmonic-integral enclosure at \(N=1024\) proves
\[
 H_N-\log(N+1)<\gamma<H_N-\log N.
\]
The original SI06 exact rational \(\pi\), \(\log2\), and \`log_rational_bounds\` arithmetic outwardly encloses all four constant terms. For a point \(q\), sum the first \(64\) positive digamma terms, rounding each individual summand outward in rational arithmetic. The remaining decreasing positive summand tail obeys
\[
 \frac12\log\left(1+\frac{y_{\rm lo}^2}{(64+\frac14)^2}\right)
 \le\sum_{k=64}^{\infty}g_y(k+\tfrac14)
 \le\frac12\log\left(1+\frac{y_{\rm hi}^2}{(63+\frac14)^2}\right).
\]
No numerical digamma value enters acceptance. All endpoint \(m(q)\) enclosures are SI06 all-seven-prime plus this true archimedean bound.

## Interval-affine multiplier and physical Fourier

Partition \([0,1]\) into \(256\) cells of width \(1/256\); partition \([1,32]\) into \(1,984\) cells of width \(1/64\). This yields exactly **2,240 rational real cells** covering the complete low band, with a finer mesh where the original source's Fourier mass matters most.

For a cell \(I=[l,r]\), let \(m_*(\xi)\) interpolate the **rational midpoint values of the two certified endpoint intervals**. SI43A's inherited full-real signed second-derivative bound and original SM40 all-seven-prime \(D_2\) prove
\[
 |m(\xi)-m_*(\xi)|\le
 \varepsilon_I:=
 \max(\text{true endpoint interval radii})+
 (D_2+D_{\rm arch}(l))(r-l)^2/8.
\]
The kink map \(w_\theta\) is **1-Lipschitz** since \(\theta=0.97\). On cells where the whole certified affine interval stays below or above \(\kappa\), \(w_\theta(m_*(\xi))=w_0+w_1t\), \(t=\xi-(l+r)/2\). If a cell might cross the kink, no smoothness is assumed: use the rigorous global cell lower \(w_\theta(\max(m_*(l),m_*(r))+\varepsilon_I)\), combined with sign-appropriate lower/upper squared-source amplitude.

For the two true SI10 physical rays, not arbitrary substituted Fourier packets,
\[
 T_f(\xi)=
 \frac{a}{2}(F_0(c-\xi)-F_0(c+\xi))
 +b\operatorname{pole\_sin}(\xi),\quad
 c=37/64,
\]
and
\[
 T_f'(\xi)=
 a\pi[F_1(c-\xi)+F_1(c+\xi)]
 +2\pi b\operatorname{pole\_xcos}(\xi).
\]
Each term is the **existing SM42 analytic original sine/pole Fourier integral**, evaluated by original rational phase-Taylor enclosures. The global whole-frequency true physical second derivative satisfies
\[
 |T_f''(\xi)|\le
 4\pi_{\rm up}^2\left(a\frac{2B^3}{3}
 +b\frac{2B^3}{3}\sinh(B/2)_{\rm up}\right)=:M_2 .
\]
On \(I\), the true Fourier packet differs from the linear Taylor polynomial \(T_*(t)=v+dt\) by \(\le E_I\), where \(E_I\) pays the midpoint value radius, derivative radius times half-cell width, and \(M_2(r-l)^2/8\). Let \(h=r-l\). The exact affine-times-linear-square integral is
\[
\boxed{\int_I (w_0+w_1t)(v+dt)^2d\xi
 =h w_0v^2+\frac{h^3}{12}(w_0d^2+2w_1vd).}
\]
Deduct both \(\varepsilon_I\int_I T_*^2\) and
\[
 \left(\sup_I|w_0+w_1t|+\varepsilon_I\right)
  h E_I(2\sup_I|T_*|+E_I)
\]
for the multiplier and true Fourier-product errors. Every cell lower is **rounded downward**, then summed and reflected across signed frequencies. This produces a genuine rational lower for the entire original \([0,32]\) signed combination.

## Numerical design feasibility, not a proof

A separate float64 evaluation of the *same proposed analytical lower formulas* (using true numerical multiplier endpoints and a deliberately conservative \(5.5\times10^{-4}\) digamma-point-radius reserve) gave lower margins of approximately
\(+3.55\times10^6\) and \(+2.24\times10^5\) on the two rays, after the previously certified conservative high-tail and pole payments. The result is **not** a certificate: it neither uses the exact rational digamma endpoint series nor interval Fourier matrix. It only establishes that the 2,240-cell proof architecture plausibly fits the percent-scale method obstruction and avoids wasting an enormous 8,192-cell full-frequency computation. If the true exact script fails or is too slow, its failure must be reported and fixed; no float lower is accepted.

The full exact Python script [original low32 affine stop](../scripts/validate_rpb108_mg07_two_source_original_low32_affine_stop.py) was committed with a dedicated [90-minute verification workflow](../.github/workflows/rpb108-mg07-original-low32-method-stop.yml) and two modes. \`--quick\` is an **inconclusive smoke test** and cannot set the stop flag; full mode requires every original rational cell and **strictly positive** exact final lower for the selected original rays. Failure leaves method obstruction and all theorem obligations OPEN.

**Next: inspect the focused exact workflow log; if it passes, record the rational positive margin and open a review of the inherited SI06/SM42 Fourier/domain identities, instead of declaring Weil or RH. If it fails, tighten only the independently identified failing finite-frequency bounds and leave the canonical signed odd theorem OPEN.**
