# MG07 — SI29-feature-augmented original Galerkin space eliminates reference inversion on the residual

**October 23, 2026. Active W-ODD-NEG OPEN.** This changes only the finite *trial space for approximating the original full inverse*. It does not change the original SM34 source/test space \(E_0=\operatorname{ran}J\) (470 genuine odd b9 generators) nor the complete signed operators \(A_\star\), \(K_-\), the SM40 890-column negative upper or the original exact corrected Schur. No claimed RH or odd positivity.

## 1. Choose exactly the SI29 positive-reference directions as added trials

Under the inherited original SI29/SM19 result,
\[
 B_{14}=\kappa I+G\Gamma G^*-2|s\rangle\langle s|
 \succeq\kappa_\star I,\qquad
 A_\star\succeq B_{14},\quad
 \kappa=1/1000,\quad \kappa_\star=33621/10^9 .
\]
Here \(G:\mathbb R^{14}\to H_o\) synthesizes the **actual** SI29 supported odd positive Jensen features, and the genuine sinh pole \(s\) is a column of the original physical source map \(J:\mathbb R^{470}\to H_o\). Assume these finite physical feature vectors belong to the same original \(A_\star\)-form and strong domains needed for the residual calculation; their sine-kernel provenance does not substitute for the required original domain audit.

Choose the finite trial space
\[
 \boxed{V=\operatorname{span}(\operatorname{ran}J,\operatorname{ran}G)},
 \qquad 470\le\dim V\le484 .
\]
If any SI29 feature is dependent on the original 470 columns, use an independent basis of the **same span**; never invert a singular synthesis Gram. Let \(T:\mathbb R^n\to V\) be full rank. Define
\[
 H_T=T^*T,\quad A_T=T^*A_\star T,\quad
 L=T^*J,\quad Q=A_T^{-1}L,\quad Z=TQ,\quad
 R=J-A_\star Z .
\]
The exact original \(A_\star\)-Galerkin normal equation gives \(T^*R=L-A_TQ=0\), hence
\[
 J^*R=0,\qquad G^*R=0,\qquad s^*R=0 .
\]
Because \(B_{14}R=\kappa R+G\Gamma G^*R-2s\langle s,R\rangle=\kappa R\), **every residual column lies in the scalar-\(\kappa\) eigenspace of the entire pole-conditioned reference \(B_{14}\)**. Since \(B_{14}\) is strictly positive,
\[
 \boxed{B_{14}^{-1}R=\kappa^{-1}R,\qquad
 R^*B_{14}^{-1}R=\kappa^{-1}R^*R.}
\]
All fourteen positive Woodbury corrections **and** the exceptional pole-inverse correction vanish here by exact Galerkin orthogonality, not by dropping either term. In contrast, with \(V=\operatorname{ran}J\) alone only \(J^*R=s^*R=0\); the feature and reference pole inverse corrections can survive.

## 2. Full 470-source MG07 inequality with a *plain* residual Gram

Let \(H_\infty=871887/70000\) be the verified SI06 exact **whole-original all-real negative multiplier** operator-norm ceiling, subject to the inherited physical Fourier identification; let \(K_{\rm cap}^{\rm SM40}\succeq K_-\) be the selected 890-column/107-block complete original SM40 negative cap (including its matched \(\eta I\)). MG07's valid noncommutative Young/resolvent estimate now becomes
\[
 N\preceq(1+t)Z^*K_{\rm cap}^{\rm SM40}Z
 +(1+t^{-1})\frac{H_\infty}{\kappa_\star\kappa}
 R^*R,\qquad t>0.
\]
The sufficient **full ORIGINAL 470-source** odd-positivity condition, for a single \(t>0\) and any valid Schur threshold \(\theta\) (the conservative paid \(51/56\), or rigorously replayed sharper \(\theta=1-\varepsilon/\kappa\)), is exactly
\[
\boxed{ (1+t)Z^*K_{\rm cap}^{\rm SM40}Z
 +(1+t^{-1})\frac{H_\infty}{\kappa_\star\kappa}R^*R
 \preceq\theta Z^*A_\star Z. }
\]
The enormous explicit factor is \(H_\infty/(\kappa_\star\kappa)\approx3.70468712\times10^8\), double at \(t=1\). There is **no numerical assertion** that its residual is small enough. Although this avoids the reference inverse altogether, it is not pointwise smaller than the old \(R^*B_{14}^{-1}R\) for an arbitrary fixed residual: indeed \(B_{14}^{-1}\preceq\kappa^{-1}I\). Trial enlargement changes both \(Z\) and \(R\); only a complete computation can say which method gives a better acceptance margin.

Define the complete original \(n\)-trial first and second action matrices
\[
 C_T=T^*K_{\rm cap}^{\rm SM40}T,\quad
 S_T=T^*A_\star^2T,\quad
 W=J^*A_\star T,\quad H_J=J^*J.
\]
All 470 source cross terms stay. The residual Gram is reconstructed entirely from these original strong-action moments:
\[
\boxed{D:=R^*R=H_J-WQ-Q^*W^*+Q^*S_TQ.}
\]
Moreover \(G_0=Q^*A_TQ\), \(N_{0,\rm cap}=Q^*C_TQ\); hence the complete test is equivalently
\[
 \boxed{(1+t)Q^*C_TQ
 +(1+t^{-1})\frac{H_\infty}{\kappa_\star\kappa}
   D\preceq\theta\,Q^*A_TQ.}
\]
This is a **470-by-470 Loewner gate** assembled from at most 484 trial columns; unlike the old source-only case, the rectangular \(Q\) cannot be inverted to get \(\theta A_J-C_J\) by congruence. Accordingly, a certified SM40 **source-only** cap-ray obstruction does not automatically reject this enriched trial. Nor does it establish that enrichment is beneficial.

## 3. An adversarial exact-rational regression

The new self-contained Fraction test, \`scripts/validate_rpb108_mg07_augmented_si29_trial.py\`, constructs a 4D physical SPD \(A\), positive pole-conditioned SI29-style \(B=I+gg^*-2ss^*\) with \(A\succeq B\), and two original source columns \(J\) containing \(s\). On the **old** trial \(V=\operatorname{ran}J\), the nonzero Galerkin residual is orthogonal to \(s\) but **not** to \(g\); the exact \(R^*B^{-1}R\) differs from \(R^*R\). On the enriched trial \(V=\operatorname{span}(J,g)\), the nonzero strong residual is orthogonal to both, and the equality \(R^*B^{-1}R=R^*R\) holds *entrywise* exactly. The test independently reconstructs \(R^*R\) from \(H_J,W,Q,S_T\). This is a finite rational structural regression, not a certificate of any original real 470-column Fourier moment.

## 4. Acceptance and next original calculation

This branch needs exactly: (i) original physical SI29 feature/strong-domain registration into the same Hilbert carrier as \(J\); (ii) rigorous at-most-484 trial \(A_T,L,W,S_T,C_T\) enclosures, with the real pole and arch/log tail; (iii) one uniform \(t>0\) positive 470-source Loewner margin, not just selected ray checks. The geometry is deliberately *aligned with the already-certified SI29 reference*, instead of arbitrarily adding more MG source dimensions. An inverse/reference weighted residual is no longer a separate numerical calculation.

Do **not** promote W-ODD-NEG, even E1–E4, CC27, Weil or RH until the whole operator criterion, including original domain and signed transfer obligations, passes.
