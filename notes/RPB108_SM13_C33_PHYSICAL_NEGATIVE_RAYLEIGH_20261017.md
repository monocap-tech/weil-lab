# SM13 — C33 original physically supported negative-packet Rayleigh audit

**Active obligation:** \`W-ODD-NEG\` OPEN.
**Parents:** SM10 merged full 890-source original negative *upper* cap; SM11 merged original 17-packet negative rank obstruction; SM12 merged original C33 positive *lower* reference. SM13 determines whether the latter reference can even dominate a subset of the actual original negative-frequency operator. This test does **not** address the complete \`A_o\` or RH.

## Correct original spectral directions

On \(H_o=L^2([-11/10,11/10])_{\mathrm{odd}}\) let
\[
g_c(x)=\sin(2\pi cx)\operatorname{sinc}(2\pi\rho x), \qquad
\kappa=10^{-3},\quad \rho=10^{-2}.
\]
The original SM11 all-real seven-prime sign enclosures on 17 disjoint rational negative bands prove
\[
K_{\mathrm{neg},o}\succeq \gamma_-\sum_{j=1}^{17}
|g_{c_j}\rangle\langle g_{c_j}|,\qquad
\gamma_-=4\rho\frac25=\frac2{125}.
\]
Consequently, for each **actual supported original** packet \(g_{c_j}\),
\[
\langle g_{c_j},K_{\mathrm{neg},o}g_{c_j}\rangle
\ge \gamma_-\|g_{c_j}\|^4.
\]

The SM12 combined original positive *lower* reference is
\[
C_{33}=\kappa I+\sum_{i=1}^{33}
\gamma_i\,|p_i\rangle\langle p_i|,
\quad p_i(x)=\sin(2\pi d_ix)\operatorname{sinc}(2\pi r_ix),
\]
with sixteen old C16 positive means and seventeen new disjoint all-real sign-positive means. The exact original quadratic comparison on each negative packet is
\[
\langle g_c,C_{33}g_c\rangle=
\kappa\|g_c\|^2+
\sum_{i=1}^{33}\gamma_i|\langle g_c,p_i\rangle|^2.
\]
**All** 33 physical overlaps, old and new, are retained; frequency band disjointness does **not** imply physical orthogonality.

## Rational, correct-sign two-sided bounds

SI18's exact sine Gram interval \(G_{c,d}\ni\langle\sin(2\pi cx),\sin(2\pi dx)\rangle\) and the true sinc error \(e(r)=(2\pi_{\mathrm{hi}}rB)^2/6\) give
\[
\|g_c\|^2\ge (1-e(\rho))^2\,\inf G_{c,c},
\quad
\|g_c\|^2\le\sup G_{c,c},
\]
and, for every positive mean \(p_{d,r}\),
\[
|\langle g_c,p_{d,r}\rangle|
\le \max(|\inf G_{c,d}|,|\sup G_{c,d}|)
  +2B(e(\rho)+e(r)).
\]
Thus the exact-rational signed margin
\[
\boxed{
\mu_c =
\frac2{125}\big[(1-e(\rho))^2\inf G_{c,c}\big]^2
-\kappa\sup G_{c,c}
-\sum_{i=1}^{33}\gamma_i
\big[|G_{c,d_i}|_{\rm up}+2B(e(\rho)+e(r_i))\big]^2
}
\]
is a rigorous **lower** bound for
\(\langle g_c,(K_{\mathrm{neg},o}-C_{33})g_c\rangle\).

If **any** \(\mu_c>0\), that is a rigorous no-go for the **reference C33 alone**: \(C_{33}\not\succeq K_{\mathrm{neg},o}\), even before the original odd pole. The *actual positive operator \(A_o\)* may nevertheless dominate the true entire original \(K_{\mathrm{neg},o}\); C33 is only a lower approximation to it, and a method no-go does not refute original Weil positivity or RH.

If no certified \(\mu_c>0\), the test is inconclusive; this is **not evidence** of positive semidefiniteness or complete 891-source closure. A larger packet subspace, better overlap enclosures, stronger positive reference or direct native RC/actual-\(A_o\) route would remain necessary.

The validator retests both original signs on *whole* rational intervals. Exact \`Fraction\` acceptance uses no floating-point sampled source values. It reports every one of the 17 true odd packet bounds and the best/worst margin.

**Replay:** \`python scripts/validate_rpb108_sm13_c33_physical_negative_rayleigh.py\`.
**Standing:** candidate until focused source/final-head GitHub Actions pass; independent validation of the original explicit-formula Weil reduction is separate.

## Exact result (focused source-head Actions accepted)

[GitHub Actions 39015294106](https://github.com/monocap-tech/weil-lab/actions/runs/39015294106) **PASSED**, evaluating all 17 original negative Jensen witness packets and all \(17\times33=561\) negative/positive true physical overlaps by exact outward-rational Gram enclosures.

The strongest witness is the **original supported odd** \(g_{721/50}\) at signed-negative center \(721/50=14.42\). The actual original full negative operator's quadratic lower bound and C33's entire upper bound are

\[
\langle g_{721/50},K_{\mathrm{neg},o}g_{721/50}\rangle
\ \ge\ 0.019489949720533795\ldots,
\]
\[
\langle g_{721/50},C_{33}g_{721/50}\rangle
\ \le\ 0.003806383032591049\ldots,
\]
\[
\boxed{
\langle g_{721/50},(K_{\mathrm{neg},o}-C_{33})g_{721/50}\rangle
>0.015683566687942744.
}
\]

The winning source's **C16** existing positive feature contribution is bounded above by \(0.0011026411022736343\), and its **17 newly added positive features** contribute at most \(0.0015982968559311464\), with the original \(\kappa \|g\|^2\) accounted separately. These are full physical coupling bounds, not assumptions that disjoint Fourier-frequency windows stay orthogonal on \([-B,B]\).

The original whole-band signed-negative multiplier upper is \(<-0.591662489\); the new original positive-band multiplier lower is \(>3.767671187\). Both original signed statements are replayed continuously on every real frequency within their certified intervals.

**Exact interpretation:** the *specific original signed-positive lower reference* \(C_{33}\) fails the necessary entire-negative domination inequality, even before the odd pole. SM13 does **not** show \(K_{\mathrm{neg},o}\not\preceq A_o\), does **not** show a negative direction of the actual original Weil form, and does **not** establish RH or its negation. Adding a finite number of narrowly chosen Jensen means is not justified as the next terminal strategy merely by increasing feature rank. The next target is a direct, rigorous positive response from the *full* original multiplier on the actual physical carrier, or an explicitly proved transport from native RC high Schur.

The decimal figures above display exact rational bounds, not floating-point acceptance. Repository final-head and independent expert audit remain distinct from this accepted scoped source replay.
