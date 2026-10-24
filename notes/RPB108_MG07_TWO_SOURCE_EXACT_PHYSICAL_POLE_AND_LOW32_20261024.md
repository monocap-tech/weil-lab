# NF — Two original odd source rays: exact physical pole and endpoint-cancelled positive Fourier tail

**October 24, 2026. Research obligation W-ODD-NEG OPEN.** This note proves *genuine original-operator inputs*, not a complete cap-vs-positive-energy stopping inequality and not full signed positivity.

## A. Distinguish the archived original rays

The passing GitHub numerical-only SM40 scout run 40071136256 produced two different ORIGINAL physical candidates using the same 470-dimensional SI10/SM35 source synthesis \(J\), namely the cluster-0 degree-zero sine \(u(x)=1_{[-B,B]}\sin(2\pi c x)\), \(c=37/64\), and actual odd sinh pole \(s(x)=1_{[-B,B]}\sinh(x/2)\), \(B=11/10\):
\[
 f_{\rm direct}=12001u+16384s,\qquad
 f_{\rm cap}=3013u+4096s.
\]
The direct ray was chosen for high sampled \(K_-/A_\star\). The distinct cap ray was chosen for the sampled SM40 \(K_{\rm cap}/A_\star\) criterion. Neither is a certified obstruction until the complete same-ray original multiplier and cap energies are rigorously enclosed.

## B. Complete exact physical Gram and pole subtraction

The original SI18 trig/pi enclosures and SI12 exact sinh Taylor envelopes give
\[
 G_{uu}=\int_{-B}^B\sin^2(2\pi cx)\,dx,\quad
 q=\int_{-B}^B\sin(2\pi cx)\sinh(x/2)\,dx,\quad
 G_{ss}=\sinh B-B.
\]
The exact rational interval validation confirms \(0.963<G_{uu}<0.965\), \(0.140<q<0.141\), \(0.235<G_{ss}<0.236\), with the full 2-by-2 determinant \(G_{uu}G_{ss}-q^2>0.1\). These are **true original physical** values; no sample grid, Galerkin surrogate, or Fourier approximation appears.

For either genuine physical coefficient ray \(f=au+bs\):
\[
 \|f\|^2=a^2G_{uu}+2abq+b^2G_{ss},\quad
 \langle f,s\rangle=aq+bG_{ss},\quad
 \boxed{\langle f,A_\star f\rangle
 =\langle f,A_o f\rangle-2(aq+bG_{ss})^2.}
\]
The source-specific exact Fraction checker, [physical pole input](../scripts/validate_rpb108_mg07_two_source_original_physical_pole_input.py), encloses **every** term, preserving all physical sine–pole cross terms. Approximate display only:
- \(f_{\rm direct}\): \(\|f\|^2\approx257{,}270{,}711\), true pole payment \(\approx61{,}520{,}772\).
- \(f_{\rm cap}\): \(\|f\|^2\approx16{,}167{,}970\), true pole payment \(\approx3{,}854{,}985\).

The complete pole subtraction is less than \(1/4\) of each positive physical \(L^2\) norm. This is a genuine **input certificate**, not yet an \(A_\star\)-energy upper.

## C. Structural property: the original two-source rays nearly cancel at the physical endpoints

For the TRUE physical ray, exactly
\[
 f(B)=a\sin(2\pi cB)+b\sinh(B/2),\quad
 f'(B)=2\pi ca\cos(2\pi cB)+\frac b2\cosh(B/2).
\]
Both are rigorously enclosed by SI14's **rational phase-reduced trigonometric Taylor bounds**, SI06's original rational \(\pi\) interval, and SI12's hyperbolic Taylor bounds. The *signed* sine/sinh cancellation is retained in the interval, rather than taking separate absolute values. Exact rational strict bounds:
\[
 |f_{\rm direct}(B)|<425,\quad |f'_{\rm direct}(B)|<19200,\qquad
 |f_{\rm cap}(B)|<97,\quad |f'_{\rm cap}(B)|<4850.
\]
These are much smaller than the unaligned triangle bound on the two source coefficients.

The true supported zero extension is odd, including both endpoint jumps. Two genuine integrations by parts yield for every real \(|\xi|\ge L>0\)
\[
 |\widehat f(\xi)|\le
 \frac{|f(B)|}{\pi|\xi|}
 +\frac{2|f'(B)|+\|f''\|_{L^1[-B,B]}}{4\pi^2|\xi|^2},
\]
where the ENTIRE original physical second-derivative integral is rigorously covered by
\[
 \|f''\|_1\le 2B a(2\pi_{\rm up}c)^2
 +b(\cosh(B/2)-1),\quad \pi_{\rm up}=22/7 .
\]
No physical high-frequency sine/sinh cancellation is assumed beyond the proved endpoint.

Consequently, for \(|\xi|\ge L\) with rational \(\pi_{\rm lo}=333/106\),
\[
 |\widehat f(\xi)|\le\frac{\beta_L}{|\xi|},\quad
 \beta_L=\frac{|f(B)|_{\rm up}}{\pi_{\rm lo}}
 +\frac{2|f'(B)|_{\rm up}+\|f''\|_{1,\rm up}}
 {4\pi_{\rm lo}^2L}.
\]
Original SM41 proves, conditional on the full original Fourier/domain identification, \(0\le a_o(\xi)=\max(\kappa,m(\xi))\le17+\log|\xi|\) on the COMPLETE real \(|\xi|\ge1\). With \(L=2^p\), \(\log L<p\,347/500\), so for the original whole high frequency:
\[
\boxed{
 \int_{|\xi|\ge L}a_o(\xi)|\widehat f(\xi)|^2\,d\xi
 \le\frac{2\beta_L^2}{L}
 \big(18+p\,347/500\big)
}
\]
and, without skipping the logarithm,
\[
\boxed{
 \int_{|\xi|\ge L}a_o(\xi)^2|\widehat f(\xi)|^2\,d\xi
 \le\frac{2\beta_L^2}{L}
 \left[
 (17+p\,347/500)^2+2(17+p\,347/500)+2
 \right].
}
\]
These are exact Fractions from the [endpoint log-tail checker](../scripts/validate_rpb108_mg07_two_source_endpoint_log_tail.py).

### Whole-original positive-form tail bounds (unscaled ray quadratic units)

| Original ray | \(L=32\) | \(L=2048\) |
|:--|--:|--:|
| \(12001u+16384s\) | \(<264{,}000\) | \(<500\) |
| \(3013u+4096s\) | \(<15{,}700\) | \(<26\) |

For cutoff 2048, each certified positive tail is less than \(1/500000\) of its TRUE physical norm, and its squared strong-action tail less than \(1/20000\) of that norm. On the exact-rational endpoints these are over **7000-fold improvements** on the original independent-source triangle-bound form-tail at 2048. For cutoff 32, the positive-form tails are already less than \(11/10000\) of the TRUE ray norm (about one part in a thousand).

**Important benefit:** the unresolved decisive original scalar frequency quadrature can restrict itself to \([0,32]\), NOT \([0,2048]\). That reduces the required low-band coverage by a factor **64** at any fixed mesh and leaves a modestly larger but rigorously paid high-tail fee.

## D. Exactly which low-frequency scalar inequality remains

The passed Oct 24 original SM40 3892-cell/107-cluster exact arithmetic gives
\(\theta_{\rm SM40}\approx0.969913581956<97/100\);
the sharp-threshold validator now asserts the strict rational upper. Since the complete original SM40 cap dominates \(K_-=(\kappa-m)_+\), to **reject the fixed source-only Ritz with this exact cap** it is ENOUGH to prove on one of these rational original source rays:
\[
 \langle f,K_-f\rangle >
 \frac{97}{100}\langle f,A_\star f\rangle.
\]
This is a *stronger benchmark* than necessary, but avoids importing a giant rational \(\theta\) into every frequency-cell proof. It would not prove the real signed form negative because \(97/100<1\), and it would not reject enriched trial spaces.

Split \(A_o\) into complete original \(|\xi|\le32\) and \(|\xi|>32\). The nonnegative true \(K_-\) tail can be **dropped when taking a lower bound**. For exact certified quantities \(K_{\rm low,lo}\), \(A_{o,\rm low,hi}\), genuine pole payment \(P_{\rm lo}=2|\langle f,s\rangle|_{\rm lo}^2\), and the newly proved \(A_{o,\rm high,hi}=T_{\rm hi}\), the entire original method-obstruction implication reduces to the SINGLE strict rational finite low-band obligation
\[
 \boxed{
 K_{\rm low,lo}-\frac{97}{100}A_{o,\rm low,hi}
 >
 \frac{97}{100}(T_{\rm hi}-P_{\rm lo}) .
 }
\]
The [exact low-band stopping reduction](../scripts/validate_rpb108_mg07_two_source_stop_low_band_reduction.py) reports the true rational right-hand threshold for EACH archived ray, checks all pole/high-tail components, and fails closed with both actual low-band entries set OPEN. No sampled digamma integral is smuggled into the inequality.

The next mathematical work is therefore **not another general tail lemma**. It is a rigorous original signed-multiplier and original two-source analytic Fourier whole-cell enclosure **only on \([0,32]\)**, using SI06/SM39/SM40 end-point curvature for the seven-prime multiplier, SI43A crossing-safe affine \(a_o=\max(\kappa,m)\), and SM42 exact original physical Fourier \(F_0,F_1,\sinh\) transforms and cell-wise remainder. Rigorously outward enclose simultaneously the \(\max(\kappa,m)\) low energy ABOVE and \((\kappa-m)_+\) low energy BELOW. One rigorous ray inequality is enough to reject the source-only Ritz sufficient method, not odd positivity.

**STOP discipline:** The at-most-484-dimensional true SI29-augmented Galerkin response is a different trial, and source-only cap failure is not its failure. Odd, even, global Weil and RH remain OPEN.
