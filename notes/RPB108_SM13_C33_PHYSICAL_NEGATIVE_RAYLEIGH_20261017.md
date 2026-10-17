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