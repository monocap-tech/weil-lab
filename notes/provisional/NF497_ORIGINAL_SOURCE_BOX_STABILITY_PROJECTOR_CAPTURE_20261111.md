# NF497 — Original source-interval stability and the necessary projector enlargement capture

**November 11, 2026 PT. Standing: exact original-source theorem / proposed independent focused verification. Do not promote numerical claims until GitHub CI SUCCESS.** Stacked research draft on source-accepted NF496 [PR #524](https://github.com/monocap-tech/weil-lab/pull/524). No main merge.

## Precise question

NF496 source-certified the actual unchanged original physical full \(J_{242}^{\perp}\) response

\[
\boxed{
\|Q_J w\|^2> L=1.57806\times 10^{-22}>3076\,\gamma^2
}
\]

with the same accepted original \(242\)-dimensional space \(J=J_{242}\) and original NF403/404 sufficient budget \(\gamma^2<5.13\times10^{-26}\). The accepted full original physical NF495 \(D_8\), NF478 genuine whole \(D_7\), NF479 original \(K\) and NF404 original *pole-centered* 242D Gram, not the \(\approx0.494\) uncentered Gram power, were used to obtain this source-specific **full** residual. NF496 also showed any **genuinely different physical supported response** \(w+h\) satisfying the *same* \(J,\gamma\) criterion must have \(\|h\|>1.2333\times10^{-11}\).

NF497 answers two independent follow-ups:

**(A)** Could the result change merely because original NF407's 4096-bit dyadic source coefficients are certified intervals rather than exact points? We now give a direct whole-source operator stability bound, not an argument from numerical coincidence.

**(B)** If the source and \(\gamma\) are fixed but the selected projection is enlarged by genuine new directions, how much of the already certified original entire residual must the new space capture? We give an exact dimension-free necessary condition and compare it to accepted NF456's two original exterior rays.

Both are source-specific necessity results; neither proves new sources are admissible, that a projector meeting the condition exists, or RH.

## A. The *entire* original source input box cannot rescue the fixed projector

The original NF407 immutable source retains 242 selected generator coefficient midpoint/radius dyadics, plus **four original critical generator coefficient balls**, all 273 grouped \((f,k)\) modes and 32 critical sine frequencies, the original odd sinh \(m=0\) pole, and the seven unchanged original NF406 physical n9-active source translations. SHA256 source:

\`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`.

Original NF406 support SHA:

\`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`.

From NF492's **actual original raw coefficient/critical shape exact-Fraction evaluator**, with every dyadic input radius paid, the complete weighted radius sum is

\[
\mathcal E=\sum_{\text{all original generators}}
\varepsilon_i\left(B+\tfrac15\right)^{k_i}
+\text{the four critical sine/pole shape-radius contributions}
<10^{-650}.
\]

It is the **actual certified source radius**, not the enormous absolute source amplitude sum \(<10^{160}\). Any **two** selections of real generator coefficients *inside the identical original certified NF407 balls* differ coefficientwise by at most **twice** the corresponding original radius. Such selections must preserve the original odd-generator carrier and the authentic unchanged physical support/seam and center. They are not entirely new candidate source functions.

Each original frequency satisfies \(f<883\), monomial order \(k\le13\); the original \(\sinh\) pole and four critical blocks are included in \(\mathcal E\). At every real \(|x|\le B=11/10\), take the complex Cauchy disk \(|\zeta-x|\le1/25\). Its entire generator arguments satisfy \(|\zeta|\le B+1/25<B+1/5\) and \(|\Im\zeta|\le1/25\). With exact rational \(\pi<22/7\) and \(e<11/4\),

\[
\frac{2(22/7)883}{25}<223,\qquad
(11/4)^{223}<10^{100}.
\]

Each exponential oscillator on this disk is therefore bounded by \(10^{100}\), with a further factor \(2\) for the original true sinh carrier. Thus for the **difference** \(\Delta U\) between any two unchanged original coefficient-ball realizations,

\[
\boxed{
\sup_{|x|\le B,\ |\zeta-x|\le1/25}
|\Delta U(\zeta)|
\le4\mathcal E(11/4)^{223}<10^{-540}.
}
\]

Cauchy's derivative inequalities with the same disk immediately imply

\[
\boxed{
\max_{|x|\le B,\ r=0,1,2}
|\Delta U^{(r)}(x)|<m,\quad
m=10^{-530}.
}
\]

There is **no large 10^142 isolated analytic-continuation image error** here: it is the original complete physical joint compact Weil response and the original input source uncertainty is summed *before any image decomposition*.

### Whole physical source-to-response stability

Now evaluate the genuine original NF446 **joint compact** physical source formula for every real \(0\le x<B\), not just \(J_8\). Let \(a=2(B-x)\), \(b=2(B+x)\), \(T=4B\), \(K(t)=e^{-t/4}/(1-e^{-t})\), \(Q(t)=K(t)-1/t\), and \(v=U(B)\). The original source bracket identities are

\[
A_x(t)=U(x)-\tfrac12(U(x+t/2)+U(x-t/2)),\quad 0\le t\le a,
\]
\[
M_x(t)=U(x)-\tfrac12(U(x-t/2)+v),\quad a\le t\le b.
\]

Both brackets involve **only the true original physical source** on \([-B,B]\). For \(\Delta U\), the real derivative bounds above give the exact Lipschitz estimates

\[
|\Delta A_x(t)|\le\tfrac18m t^2,\qquad
|\Delta M_x(t)|\le\tfrac14m(t+a).
\]

The second inequality is the decisive authentic **joint source cancellation** at the endpoint: it prevents the false logarithmic divergence that would appear if the four original source components were bounded independently.

For \(0<t\le T\), the elementary exponential inequalities \(1-e^{-t}\ge t/(1+t)\), \(1-e^{-t}\le t\), \(e^{-t/4}\ge1-t/4\) prove

\[
\frac1t-\frac14\le K(t)\le\frac1t+1,\qquad
-\tfrac14\le Q(t)\le1.
\]

Since \(b\ge2B=11/5\), the upper tail obeys

\[
\int_b^\infty K(t)\,dt
\le \frac{4}{1-e^{-b}}
<\frac{16}{3}<6.
\]

The original digamma constant \(c_0=\psi(1/4)-\log\pi\) satisfies the previously accepted \(|c_0|<10\); the NF446 scalar \(\log((B+x)/B)\) obeys \(0\le\log((B+x)/B)<\log2<1\), while \(b-a=4x\le4B\). Genuine original regular prime weights are all \(0<c_n<1\), at most seven n9-active translations, and the original dyadic NF404 pole center is held fixed.

The complete source-linear \(\Delta z\) is therefore bounded by independently exact rational contributions:

\[
\begin{aligned}
\left|\int_0^a K(t)\Delta A_x(t)dt\right|
&<m\left(\frac{(2B)^2}{16}+\frac{(2B)^3}{24}\right)<m,\\
\left|\int_a^b K(t)\Delta M_x(t)dt\right|
&<\frac m4\left(8B+\frac{T^2}{2}+8B^2\right)<8m,\\
|\text{original NF446 scalar }Q\text{ term}|&<3m,\\
|\text{full compact }K\text{-tail}|&<6m,\\
|\text{all authentic regular prime differences}|&<14m,\\
|c_0\Delta U(x)|&<10m.
\end{aligned}
\]

Consequently

\[
\boxed{|\Delta z(x)|<42m.}
\]

The original physical principal uses at most seven original weights and a single endpoint logarithm, so with \(L(x)=\log(2B/(B-x))\),

\[
|\Delta p(x)|\le m(7+L(x)).
\]

For the **whole actual supported physical response** \(\Delta w=\Delta p+\Delta z\) on each positive original cell,

\[
\boxed{|\Delta w(x)|<m(50+L(x)),\quad 0\le x<B.}
\]

This bound is *global across the true seven prime seams*. No smooth Taylor approximation is taken across a seam. Oddness of the original source/response doubles the positive support \(L^2\) energy. The endpoint logarithm, although unbounded pointwise at \(B\), is integrable:

\[
\int_0^B L(x)\,dx=B(1+\log2)<2B,\qquad
\int_0^B L(x)^2dx=B(2+2\log2+\log^22)<5B.
\]

As \(2B(50^2+200+5)=5951<100^2\), one obtains the true global physical norm stability certificate

\[
\boxed{\|\Delta w\|_{L^2([-B,B])}<100m=10^{-528}.}
\]

**Compare:** the accepted NF496 necessary change to reach the same fixed \(J_{242},\gamma\) sufficient bound is \(>1.2333\times10^{-11}\). The complete original certified coefficient-radius box is therefore more than **\(10^{517}\)** times too small to repair that complement criterion. No choice inside those old uncertainty intervals, no mere reassessment of 4096-bit source rounding, no selected-space coordinate change or pole shear can rescue the fixed certificate.

**This is NOT an exclusion of genuinely different source coefficients outside the original accepted dyadic balls.** The user-selected witness source is a specific finite object, not an entire global admissible Weil-source family, and the valid source-to-response norm transfer proved here only concerns perturbations inside *its original certified input intervals*.

## B. Any enlarged projector must capture almost the entire actual original residual

Let \(q=Q_Jw\), with accepted NF496 \(\|q\|^2>L=1.57806\times10^{-22}\), and let \(E\subset J^\perp\) be an arbitrary **new orthogonally additional selected subspace**. If the enlarged original selected space \(J'=J\oplus E\) and the unchanged \(\gamma\) are to pass the **same** sufficient complement criterion,

\[
\|(1-\Pi_E)q\|^2\le\gamma^2.
\]

By exact Pythagoras,

\[
\boxed{\|\Pi_E q\|^2>\,L-5.13\times10^{-26}
=1.577547\times10^{-22}.}
\]

Its relative necessary capture fraction is therefore

\[
\boxed{
\frac{\|\Pi_Eq\|^2}{\|q\|^2}>
1-\frac{5.13\times10^{-26}}{1.57806\times10^{-22}}
>0.9996749,
}
\]

that is, **more than 99.96749% of the entire original perpendicular response energy**. Equivalently the residual principal-angle sine must satisfy

\[
\sin\angle(q,E)<0.0181.
\]

By contrast the accepted NF456 two original exterior rays \(q_{512},q_{513}\), whose entire power is \(<1.85\times10^{-26}\), capture less than \(0.000118=0.0118\%\) of the now measured original \(q\)-energy. Any successful enlarged space must capture **more than 8,527 times** the already accepted two-ray upper. Those two previously examined rays are extremely poor *in this new quantitative sense* at accounting for the source-specific actual residual.

**No theorem about necessary rank follows.** A single new vector proportional to \(q\) could, abstractly, capture all the energy; whether such a vector belongs to a genuinely admissible new selected direction or is available from the infinite exterior operator is *not* settled. The verifier checks exact rational finite-dimensional countermodels preventing this inference. The result is a strict *capture/angle* specification for prospective source-preserving projector redesigns, not a claim that no finite enlargement can work.

## Relevance to W-ODD-NEG, full Weil/domain and RH

The accepted original NF404 sufficient physical residual gate is only one certificate strategy toward the odd-sector lowband requirement. Its source-specific failure, even strengthened by this independent full response stability and projector-capture obligation, is **not** itself a negative vector of the Weil quadratic form and not a failure of W-ODD-NEG. NF402 demonstrated that support restriction and Fourier bandlimiting do not commute. Source perturbations outside the original dyadic input balls, projectors that change geometry, and proofs of the full infinite Weil operator/domain remain *OPEN*; a source family must be independently shown admissible before being substituted into the original witness.

**Next bold NF498:** instantiate a genuinely admissible alternative original Weil source direction or a concrete new exterior selected vector and compute its actual full physical source/projection response and eligibility. On the same \(J,\gamma\), a replacement must change supported response by \(>1.2333\times10^{-11}\); for enlarged \(J'=J\oplus E\), a source-validated \(E\) must capture \(>99.96749\%\) of original \(q\)-energy. Avoid merely increasing original coefficient precision or adding the same two NF456 rays. W-ODD-NEG, exterior full J242, even/whole Weil operator/domain and RH still OPEN.
