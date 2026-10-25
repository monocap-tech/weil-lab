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

## October 24 verification-control repairs (latest branch)

Review of the first exact acceptance implementation exposed two **proof-process** errors, fixed before accepting any stopping result.

First, an original \(J\)-only Ritz/SM40 sufficient gate is universally quantified over **source rays**, so a rigorous **single** counter-ray suffices. The first acceptance code mistakenly required **both** archived source rays to pass. It now uses the existential condition \(\exists f\in\{f_{\rm direct},f_{\rm cap}\}\) with a strictly positive **exact Fraction lower margin**. Every other ray's result remains recorded independently and unpromoted. The CI postcondition now agrees with the logical quantifier.

Second, an inconclusive exact run initially raised before saving its rational output. The corrected code now writes its full result artifact first, with explicit status \`EXACT_ORIGINAL_LOW32_INCONCLUSIVE_NO_STOP\` and the original method status \`OPEN_NOT_CERTIFIED\` when no ray passes, then exits with an assertion failure in full mode. In addition to both final margins, the artifact now preserves five rigorously rounded contribution totals for \([0,1],[1,4],[4,8],[8,16],[16,32]\), whose exact sum is checked against each ray's entire low-band bound. This allows a failed proof to be repaired at the offending original frequency region, without substituting numerical evidence or accumulating unrelated scalar certificates.

An independent \`scipy\` numerical quadrature over the original \([0,32]\) signed multiplier (not used for any theorem) found preliminary \(K_--0.97 A_\star\) signed margins before the small >32 correction of about \(+5.70\times10^6\) on the direct-selected ray and \(+3.58\times10^5\) on the cap-selected ray. This reinforces the *plausibility* of the interval proof but does not say its outward rational lower will succeed.

The repository's critical-path manifest was also independently preflighted after correcting its schema: all 63 declared active-check commands and all 77 evidence records whose entries contain repository paths resolve to actual repository files. The 34 legacy descriptive check roles have valid canonical \`verification\` roles while preserving the original limitation in \`scope_role\`; four case-sensitive/legacy file naming exceptions now pass a restricted allowlist/pattern with new adversarial path-security tests. This is **governance**, not mathematical sign verification.

The exact original 2,240-cell low-band CI remains subject to real GitHub Actions results and independent original Fourier/domain scrutiny; no accepted stop theorem is claimed until those conditions are met.



## Further Oct 24 independent algebra/physical normalization checks

The original 2,240-cell enclosure has a subtle potential failure mode: an algebraic error in the affine integrand or a sign/normalization error in the true sine/sinh transform could produce a spurious strictly positive final margin. These are now explicitly tested before any of the costly original signed-frequency cells run.

The signed-cell lower bound was factored into a pure exact-rational \`cell_affine_exact_lower\` routine. Four deliberately adverse *true* sextic integrands were constructed by multiplying a genuinely curved rational signed multiplier
\(m(t)=m_0+m_1t+\alpha(t^2-h^2/4)\)
by the square of a genuinely curved rational physical proxy
\(T(t)=v+dt+\beta(t^2-h^2/4)\).
The exact integrands were integrated independently, coefficient by coefficient, over symmetric cells. The rational lower bound was below the true result on all four tests, including both signs of the physical weight. A separate test imposes a **real kink \(m=\kappa\) inside the cell**, uses the two different analytic branches of \(w_{97/100}(m)\), and verifies the more conservative kink-cell lower remains valid. All four sextic comparisons were independently reproduced locally with strictly positive gaps; none is an original frequency certificate.

A second exact check holds SI42's supported **odd Fourier normalization** accountable at \(\xi=0\): \(T_u(0)=T_s(0)=0\) and
\[
 T_u'(0)=2\pi F_1(c),\qquad
 T_s'(0)=2\pi\left[4B\cosh(B/2)-8\sinh(B/2)\right],
\]
with \(c=37/64\), using the actual SI42 sine and true original sinh physical integrals. The calculated SI42 analytic \`qbasis\` derivative intervals must overlap these independently stated first moments and have the correct positive sign. This is a check on the Fourier factors, not a numerical sample.

These regressions run in BOTH \`--quick\` and full exact modes; failure halts acceptance. New exact signed/rational proof work therefore remains the **original 2,240 real frequency cells**, not further selected-source sampling.



## NF — Dual original-ray sign diagnostic (independent of the sufficient-method stop)

A crucial distinction deserves an additional **true original signed-form** computation, not merely an explanatory disclaimer. By the exact original whole-frequency definitions,
\[
  A_o=\max(\kappa,m)(D),\quad K_-=(\kappa-m)_+(D),\quad
  A_\star=A_o-2ss^*,
\]
the identity
\[
 \boxed{W_o=A_\star-K_-=m(D)-2ss^*}
\]
holds on the common original form domain. It is an *exact pointwise identity*, including at \(m=\kappa\). The true signed multiplier \(m\) itself has no artificial truncation kink.

The updated same **2240 original real [0,32] cells** now independently enclose \(2\int_0^{32}m(\xi)|T_f(\xi)|^2\,d\xi\) from below using the already certified endpoint-affine \(m\), the same physically exact SI42 sine–sinh Fourier midpoint and first derivative, and the same all-real curvature and source error. This direct signed-energy lower has **no kink-cell branch**, because \(m\) is smooth. It is independently accumulated, saved for each of the same five frequency regions and arithmetically checked against its total.

For all \(|\xi|\ge32\), SI06's full seven-prime-power bound and nonnegative digamma series give the original pointwise
\[
  m(\xi)\ge -M_0,\qquad
  M_0=\frac{4707}{875}+\frac{70751}{10000}.
\]
The original endpoint-cancelled two-source Fourier transform bound \(|T_f(\xi)|\le \beta_{32}/|\xi|\), *already established without FFT sampling*, then implies
\[
 2\int_{32}^\infty m(\xi)|T_f(\xi)|^2d\xi
 \ge -M_0\,\frac{2\beta_{32}^2}{32}.
\]
The exact **upper** original sinh pole subtraction is independently paid. Thus, denoting the certified original signed low-cell lower by \(L_{\rm signed}\) and original physical pole upper by \(P_{\rm hi}\),
\[
 \boxed{\langle f,W_of\rangle\ge
 L_{\rm signed}-\frac{2M_0\beta_{32}^2}{32}-P_{\rm hi}.}
\]
A strictly positive exact rational right side proves the **selected physical ray** is positive under the true signed original odd operator. It does **not** prove odd positivity on all sources, its orthogonal complement, the even sector or RH. A nonpositive lower remains INCONCLUSIVE, not proof of a negative ray.

If a single ray establishes simultaneously
\[
  \langle f,K_-f\rangle>0.97\langle f,A_\star f\rangle
  \quad\text{and}\quad
  \langle f,W_of\rangle>0,
\]
then it gives a rigorous original-operator **false negative for the selected source-only Ritz/SM40-cap sufficient method**: the method fails on a ray whose genuine signed energy is nevertheless strictly positive. This is strictly stronger interpretive evidence about the chosen *proof method*, not an RH resolution.

The implementation makes this signed positivity an **independent optional, fail-closed recorded result**, not an additional mandatory assertion for the original one-ray method STOP. It retains the separate exact lower margin and full five-region decomposition and explicitly verifies the pointwise algebra \(\max(\kappa,m)-(\kappa-m)_+=m\) on adversarial rational values across the kink. The dedicated CI verifies that any positive signed-ray flag is supported by its own strictly positive exact Fraction lower. At time of authoring, the full GitHub exact 2240-cell job is still QUEUED; neither margin is certified as passed.


### Numerical scale warning for the independent signed-positive ray diagnostic

The 0.97 **method-stop** is deliberately separated from the \(1.00\) **true signed positivity** check. An independent noncertifying numerical quadrature of the genuine original signed multiplier \(m(\xi)\), using analytic physical sine/sinh Fourier transforms rather than the truncated SI29 Galerkin response, gives:

| Original rational ray | \(2\int_0^{32} m(\xi)T_f(\xi)^2d\xi-2\langle f,s\rangle^2\) | Sampled additional \(2\int_{32}^{2048}m(\xi)T_f^2d\xi\) |
|---|---:|---:|
| Direct-selected \(12001u+16384s\) | approximately \(+39,605\) | approximately \(+2,403\) |
| Cap-selected \(3013u+4096s\) | approximately \(+2,526\) | approximately \(+124\) |

These are **float/quadrature**, neither original operator certificates nor guaranteed signs. The rigorous universally valid SI06 \(m\ge -M_0\) tail lower beyond \(32\) with the current two-IBP \(\beta_{32}\) costs approximately \(153{,}000\) and \(9{,}100\), respectively. This is larger than the observed signed margins; so the *optional* signed-positive outcome is plausibly INCONCLUSIVE even if the rigorous primary method-stop \(K_--0.97A_\star>0\) succeeds. A more discriminating signed-positive certificate would need its own sharper negative-tail localization or further \(32<\xi<128\) true signed integral work. The current NF **does not** authorize delaying the simpler method-obstruction test for that optional objective.

The script reports each signed-ray result only when its own rational lower is positive and otherwise leaves its sign unknown. It must NEVER interpret failure of that lower bound as a negative original odd direction or an RH claim.


## NF — Global affine minorants remove the ambiguous κ-cell loss

The exact original signed scalar stopping weight satisfies, for every REAL m and 0<theta<1,
\[
w_\theta(m)=(\kappa-m)_+-\theta\max(\kappa,m)
=\boxed{\max\{(1-\theta)\kappa-m,\ -\theta m\}}.
\]
This is the MAXIMUM of two globally affine real-frequency functions, so each is a valid pointwise LOWER bound to the true signed weight on every frequency, including any cell crossing m=kappa. Multiplication by the nonnegative true original sine/sinh Fourier square preserves both lower comparisons.

For a crossing cell with certified endpoint-affine m_*(xi), complete signed interpolation error epsilon and true original Fourier packet linearization error E, the existing cell_affine_exact_lower formula can be applied independently to each affine branch
\[
w_-(m_*)=(1-\theta)\kappa-m_*,\quad
w_+(m_*)=-\theta m_*.
\]
After the COMPLETE multiplier/physical Fourier error payment and exact integration of each branch, take the maximum of the two certified lower values and the old constant-weight kink lower. This cannot weaken the original bound and avoids inferring differentiability of the kink. The same full epsilon is paid for both branches, conservatively since each branch is at most 1-Lipschitz in m.

An exact Fraction regression independently tests the identity on six rational multiplier values including m=kappa, and the genuinely crossing m(t)=kappa+t/50 for t in [-1/8,1/8] with constant physical Fourier value T=2. Its true exact integral is -761/800000; the best affine lower is -97/100000, with positive gap 3/160000. This was independently checked locally; it is NOT a 2240-cell original source-ray proof.

The full source-only MG07/SM40 method-stop is certified only when one true original rational source ray has a strictly POSITIVE complete lower. This improvement does not establish any original odd negative direction, universal odd/even positivity, Weil bridge, or RH.


### Further strengthening: EXACT rational κ crossing inside affine model

The affine-minorant bound is globally valid but still loses the benefit of integrating the maximum **inside** the integral. For every original real-frequency cell \(I=[l,r]\), define \(t=\xi-(l+r)/2\), cell width \(h=r-l\), and the actual certified rational endpoint-affine multiplier \(m_*(t)=m_0+m_1t\). The crossing \(m_*(t)=\kappa\), when \(m_1\neq0\), lies at the **exact rational** location
\[
 t_*=(\kappa-m_0)/m_1.
\]
Split \([-h/2,h/2]\) into one or two rational subintervals at \(t_*\), if it lies strictly inside. On each piece the original signed stopping weight is a known affine polynomial:
\[
 w_\theta(m_*(t))=
 \begin{cases}
 (1-\theta)\kappa-m_0-m_1t,&m_*(t)<\kappa,\\
 -\theta m_0-\theta m_1t,&m_*(t)>\kappa.
 \end{cases}
\]
With the same original physical Fourier linear packet \(T_*(t)=v+dt\), the primitive of \((w_0+w_1t)(v+dt)^2\) is exactly
\[
 F(t)=w_0v^2t+\frac{2w_0vd+w_1v^2}{2}t^2
  +\frac{w_0d^2+2w_1vd}{3}t^3
  +\frac{w_1d^2}{4}t^4.
\]
Thus the **entire modeled kink integral** is determined by at most two exact rational quartic differences. Pay the already certified full original multiplier error \(\varepsilon_I\) using global 1-Lipschitz continuity of \(w_\theta\) and the physical Fourier error \(E_I\) using a global weight envelope:
\[
 \varepsilon_I\int_I T_*^2+
 (\sup_I|w_\theta(m_*)|+\varepsilon_I)
 h E_I(2\sup_I|T_*|+E_I).
\]
Every term is outward and exact. Even if the exact crossing of the TRUE \(m\) differs from \(t_*\), this error envelope remains valid: there is **no assumption** that the true crossing equals the affine model crossing. Keep the best of this whole-real piecewise bound, the two independent globally affine minorants, and the original conservative constant floor.

An independent Fraction check confirms the modeled kink integral is \(-761/800000\) for \(m_*(t)=\kappa+t/50\), \(T_*(t)=2\), \(h=1/4\), including the reverse-slope case. An off-center rational crossing with a nonconstant original Fourier-linear proxy independently matches exact quartic antiderivative assembly: \(-248438569/87480000000\). These are algebraic implementation tests, NOT evaluations of original \([0,32]\) Fourier cells.

The dedicated 2240-cell exact job must still complete with a strictly positive original source-ray lower before we claim any source-only Ritz/SM40 sufficient-method obstruction. Universal signed odd/even positivity and RH remain OPEN.


## NF — Original negative-support mass replaces uniform high signed-tail charge

The independent signed-energy diagnostic uses the exact original form
\[
 W_o=A_\star-K_-=m(D)-2ss^*.
\]
Previously its entire high signed tail was charged with the SI06
uniform lower \(m(\xi)\ge-M_0\), resulting in the coarse negative fee
\(2M_0\beta_{32}^2/32\). This treated every frequency above 32 as
potentially negative, despite already certified original negative support.

The ORIGINAL SI10 signed complement certificate covers the whole
possibly negative frequency set in exactly 973 positive-frequency
leaves forming 107 components. Each leaf [a,b] has a rigorous
pointwise original \(K_-=(\kappa-m)_+\) upper \(h_I+\kappa\).
Outside these intervals the true original m is at least κ>0.
Its exact complete two-sign weighted envelope mass is
\[
 \boxed{M_{\rm SI10}
 =2\sum_I(b_I-a_I)(h_I+\kappa)
 =\frac{1204033883}{32000000}
 =37.62605884375<38.}
\]
The original supported sine-sinh physical endpoint estimate,
including both second-derivative and jump boundary terms, gives
\(|\widehat f(\xi)|\le\beta_{32}/|\xi|\) for all \(|\xi|\ge32\).
Furthermore, \(m_-=(-m)_+\le(\kappa-m)_+=K_-\).
Consequently the ENTIRE signed negative high tail obeys
\[
 \boxed{
  \int_{|\xi|>32}(-m(\xi))_+
      |\widehat f(\xi)|^2d\xi
  \le \frac{M_{\rm SI10}\beta_{32}^2}{32^2}.}
\]
One must NOT multiply by an additional factor of two: SI10's exact
mass already accounts for both positive and negative Fourier
frequencies and their complete original signed prime/digamma support.
The inherited original positive-complement theorem accounts for
every frequency outside the 107 certified components, including
all frequencies beyond 896.

Relative to the original SI06 pointwise fee, the guaranteed EXACT
improvement factor is
\[
 \frac{2M_0\beta_{32}^2/32}
      {M_{\rm SI10}\beta_{32}^2/32^2}
 =\boxed{\frac{64M_0}{M_{\rm SI10}}>20},
 \quad M_0=\frac{4707}{875}+\frac{70751}{10000}.
\]
The new checker at
[signed-support high-tail replay](../scripts/validate_rpb108_mg07_original_signed_supported_tail.py)
recomputes SI10's 107-component/973-leaf true positive-frequency
cover, verifies the exact two-sign rational weighted mass and
reuses the TRUE original supported Fourier endpoint β for BOTH
archived rational sine-sinh source rays. It has been integrated
into the dedicated low32 CI workflow, which remains subject
to exact external replay.

This result applies ONLY to the optional signed-ray positive test
on the original \(W_o=m(D)-2ss^*\). It does NOT loosen, substitute
for or establish the main 2,240-cell source-only MG07 method
STOP test \(K_--0.97A_\star>0\). A strict original ray
sign is accepted only after its own full rational low32 margin
passes. No full 470-dimensional, universal odd/even, Weil or RH
positivity is inferred.


### Sharper still: exact reciprocal Fourier decay integrated leaf by leaf

The first SI10 support-weighted original signed high-tail bound conservatively
replaced \(\xi^{-2}\) by \(32^{-2}\) on the **entire** negative-frequency
support. We can use the true original SI10 rational endpoints instead.

For each of the 973 originally certified positive-half unresolved leaves
\(I=[a_I,b_I]\) with complete original cap weight \(w_I=h_I+\kappa\),
take \(\ell_I=\max(32,a_I)\) and discard \(I\) when \(b_I\le32\).
On the two-sign whole-frequency negative tail, the exact contribution
obeys
\[
 2\int_{\ell_I}^{b_I}
  w_I\,\frac{\beta_{32}^2}{\xi^2}\,d\xi
 = 2\beta_{32}^2w_I
 \left(\frac1{\ell_I}-\frac1{b_I}\right).
\]
Consequently, define the **fully rational SI10 reciprocal envelope**
\[
\boxed{S_{32}:=
  2\!\!\sum_{\substack{I\text{ original SI10}\\b_I>32}}
  (h_I+\kappa)
  \left(\frac1{\max(32,a_I)}-\frac1{b_I}\right).}
\]
Then the complete original physical signed negative high-frequency
contribution satisfies
\[
\boxed{
 \int_{|\xi|>32}(-m(\xi))_+
      |\widehat f(\xi)|^2\,d\xi
 \le \beta_{32}^2 S_{32}.}
\]
This is an EXACT rational sum over the inherited original 973 leaves,
not a quadrature or an invented cap. SI10's two-frequency-sign
reflection is paid by the displayed factor 2 and **must not be paid
again**. Neither the 107 clusters nor their underlying source geometry
changes.

Let \(M_{32}=2\sum_{I:b_I>32}(h_I+\kappa)
(b_I-\max(32,a_I))\). Every counted interval satisfies
\(\ell_I>0\), and so
\[
 0<S_{32}<\frac{M_{32}}{32^2}
  <\frac{M_{\mathrm{SI10}}}{32^2},\qquad
 M_{\mathrm{SI10}}=\frac{1204033883}{32000000}<38.
\]
These are **strict rational checks** in the updated
[original support-tail validator](../scripts/validate_rpb108_mg07_original_signed_supported_tail.py),
which also checks an independent hand-integrated
positive-frequency leaf \([32,64]\) and verifies the two-sign
normalization.

The true original \([0,32]\) signed ray validator now uses
\(\beta_{32}^2S_{32}\) in its optional \(W_o\)-ray-positive margin.
It retains **both** the earlier SI10
\(M_{\mathrm{SI10}}\beta_{32}^2/1024\) and the yet coarser SI06
uniform tail as independent rational comparisons. This yields a
genuine monotone certificate improvement without any additional
original-operator assumptions, spectral approximation, source
truncation or heuristic low-frequency signs.

The dedicated low32 GitHub Actions workflow must still replay the
whole calculation and find an exact positive lower for either
method-obstruction ray; even if it does, **only** the original
source-only \(J\)-Ritz/SM40 sufficient route is rejected.
The independent signed-positivity ray status, universal odd/even
operator and RH remain separately gated.


## NF — Rigorous Euler-gamma and convex digamma remainder sharpening (same 2,240 cells)

**This targets the original low-band multiplier endpoint bottleneck directly.** The first low32 validator used the elementary but loose harmonic bound \(H_N-\log(N+1)\le\gamma\le H_N-\log N\) at \(N=1024\), an almost \(10^{-3}\) uncertainty copied into *every* original archimedean multiplier endpoint. We can improve it by more than 2,000-fold **without evaluating another harmonic summand**.

Let \(E_N=H_N-\log N-\gamma\). The finite positive logarithmic differences satisfy
\[
\begin{aligned}
 E_N&=\sum_{k=N}^{\infty}g_k,\quad
 g_k=\log(1+1/k)-1/(k+1)\\
 &=\frac1{k+1}\int_0^1\frac{1-t}{k+t}\,dt,\\
 \frac1{2(k+1)^2}&\le g_k\le\frac1{2k(k+1)}.
\end{aligned}
\]
The upper sum telescopes. The lower sum dominates its convergent integral, giving
\[
 \boxed{\frac1{2(N+1)}\le E_N\le\frac1{2N}},
 \quad
 \boxed{
 H_N-\log N-\frac1{2N}
 \le\gamma\le
 H_N-\log N-\frac1{2(N+1)}.}
\]
Every \(\log N\) bound comes from the existing rigorous rational SI06 logarithm routine. At \(N=1024\) the resulting true Euler-\(\gamma\) interval width is below \(1/2{,}000{,}000\), instead of roughly \(9.76\times10^{-4}\). This controls the complete original constant \(C=\gamma+\pi/2+3\log2+\log\pi\) to width below \(10^{-6}\).

The remaining original positive quarter-digamma tail is
\[
 \sum_{k=64}^{\infty}g_y(k+\tfrac14),\quad
 g_y(v)=\frac{y^2}{v(v^2+y^2)},\quad y=\pi\xi.
\]
It is nonnegative, decreasing and **strictly convex** for \(y>0\), because
\[
 g_y''(v)=
 \frac{2y^2(6v^4+3v^2y^2+y^4)}
 {v^3(v^2+y^2)^3}>0.
\]
For every decreasing convex integrable function \(g\), trapezoidal comparison and midpoint Jensen give
\[
 \int_K^\infty g(v+\alpha)\,dv+\tfrac12g(K+\alpha)
 \le\sum_{k=K}^\infty g(k+\alpha)
 \le\int_{K-\frac12}^\infty g(v+\alpha)\,dv.
\]
With \(K=64\), \(\alpha=1/4\), and the exact antiderivative
\(\frac12\log(1+(y/v)^2)\), the improved rational bounds are
\[
\boxed{
\begin{aligned}
 \mathrm{Tail}_{\rm lo}
 &=\tfrac12\log_{\rm lo}(1+(y_{\rm lo}/(64+\frac14))^2)
  +\frac{y_{\rm lo}^2}
   {2(64+\frac14)((64+\frac14)^2+y_{\rm lo}^2)},\\
 \mathrm{Tail}_{\rm hi}
 &=\tfrac12\log_{\rm hi}
 (1+(y_{\rm hi}/(64-\frac12+\frac14))^2).
\end{aligned}}
\]
The original SI06 rational \(\pi\) enclosure and monotonicity in \(y\) still pay every transcendental argument error.

A second, independent local Fraction implementation of the SI06 rational \(\pi/\log\) bounds and all 64 original positive terms recovered these original archimedean endpoint interval widths:

| Exact rational \(\xi\) | Old endpoint interval width | New endpoint interval width |
|---|---:|---:|
| \(0\) | \(0.000976085974\) | \(0.000000476373\) |
| \(1\) | \(0.001014092637\) | \(0.000000695026\) |
| \(32\) | \(0.012163960418\) | \(0.000034627522\) |

Independent high-precision summation was used as a **non-proof sanity check** for the convex-tail inequalities, and agreed; *acceptance* uses only the exact Fraction inequalities derived above. The actual low32 script now asserts \(C\)-width below \(10^{-6}\), arch-endpoint width below \(10^{-6}\) at \(\xi=1\), and below \(5\times10^{-5}\) at \(\xi=32\). The original 2,240-cell signed source-ray stop criterion and both genuine physical sources remain unchanged.

**Scope:** This is a substantial exact analytic improvement in every original low32 multiplier endpoint bound. The critical source-only Ritz/SM40 sufficient-method obstruction is still unproved until the full 2,240-cell exact lower sum succeeds. The true signed universal odd operator, even, CC27 and RH remain OPEN.
