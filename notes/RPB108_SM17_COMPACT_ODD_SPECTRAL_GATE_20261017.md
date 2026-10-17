# SM17 — compact conditioned odd spectral gate and high-frequency-extension diagnostic

**Active:** W-ODD-NEG OPEN. **Parent:** SM16 (PR #154), strict original signed odd positivity on a physically supported 2D span. **Standing:** analytic operator argument and exact-rational *conditional* finite-cap budget only. No original 890-source inverse bound is certified.

## 1. Original odd form

Let \(H_o=L^2([-B,B])_{\rm odd}\), \(B=11/10\), \(Z\) be physical zero extension, and \(\mathcal F\) the unitary Fourier transform. Retain the original seven-prime signed multiplier \(m(\xi)\), \(\kappa=1/1000\),
\[
a(\xi)=\max(m(\xi),\kappa),\qquad r(\xi)=(\kappa-m(\xi))_+.
\]
Define the physically supported *form* operator \(A_o=Z^*\mathcal F^{-1}a\mathcal F Z\), negative analysis \(R_of(\xi)=\sqrt{r(\xi)}\,\widehat{Zf}(\xi)\), and \(s(x)=\sinh(x/2)\). The odd pole-conditioned operator \(A_*=A_o-2|s\rangle\langle s|\) satisfies, by SI29/SM01,
\[
A_*\succeq\kappa_* I,\qquad \kappa_*=\frac{33621}{10^9}>0.
\]
The *original signed* odd quadratic is \(Q_o[f]=\langle f,A_*f\rangle-\|R_of\|^2\) on \(\operatorname{Dom}A_o^{1/2}\). No whole-line reciprocal replaces the supported inverse.

## 2. Compact conditioned Birman–Schwinger and adversarial witness

**SM17-A (analytic).** The operator
\[
T=R_oA_*^{-1}R_o^*
\]
on the negative-frequency observation space is positive trace-class. Full odd signed positivity holds if and only if \(\lambda_{\max}(T)\le1\). If \(Tu=\lambda u\), \(\|u\|=1\), \(\lambda>1\), the original supported odd vector \(f=A_*^{-1}R_o^*u\) satisfies the *actual original form* identity
\[
\boxed{Q_o[f]=\lambda(1-\lambda)<0.}
\]
Thus a strict top-eigenvalue excess gives a genuine physical odd counter-witness, not merely a failure of a chosen positive reference.

**Proof.** SI06/SI10 certify \(r=0\) outside \([-896,896]\); boundedness of \(r\) on this compact set makes \(R_o\) Hilbert–Schmidt:
\[
\|R_o\|_{\rm HS}^2\le 2B\int_{\mathbb R}r(\xi)\,d\xi.
\]
Hence \(T=(R_oA_*^{-1/2})(R_oA_*^{-1/2})^*\) is positive trace-class. The positivity equivalence is the full pole-correct SM01 Schur identity. Given \(Tu=\lambda u\), \(A_*f=R_o^*u\), so \(\langle f,A_*f\rangle=\lambda\) and \(\|R_of\|^2=\lambda^2\). Positive compact operators attain each nonzero maximal eigenvalue. No numerical value of \(\lambda_{\max}(T)\) is certified here.

SM10's all-973-leaf envelope bounds the original full \(\int r<38\). Thus
\[
\operatorname{tr}(T)<\frac{(11/5)\,38}{\kappa_*}<2{,}486{,}542.
\]
This trace bound only establishes finiteness and is **not** close to an adequate top-eigenvalue inequality.

## 3. Explicit full original finite-cap acceptance criterion

SM10's original physically supported 890-column sine-Taylor synthesis \(U\), exact rational positive moment matrix \(C\), and \(K_{\rm cap}=UCU^*\) satisfy the one-sided Loewner bound
\[
K_{\rm neg,o}=R_o^*R_o\preceq(1+\tau)K_{\rm cap}+\eta I,\quad
\tau=1/1024,\quad 0\le\eta<302/10^{12}.
\]
Define the real **missing** pole-conditioned supported inverse matrix
\[
G=C^{1/2}U^*A_*^{-1}UC^{1/2},\qquad\mu=\lambda_{\max}(G).
\]
Congruence by \(A_*^{-1/2}\) and the nonzero spectrum identity imply
\[
\boxed{\lambda_{\max}(T)\le(1+\tau)\mu+\eta/\kappa_*.}
\]
Thus **if the real 890-source \(\mu\) is certified** to obey
\[
\boxed{\mu\le 999/1000,}
\]
the full odd signed original form is positive: exact rational arithmetic gives
\[
(1+1/1024)(999/1000)+(302/10^{12})/\kappa_*<1.
\]
The sharper certified sufficient threshold using only the conservative displayed \(\eta\) upper is
\[
\mu<\frac{1-(302/10^{12})/\kappa_*}{1+1/1024}
=\frac{4303449344}{4307690625}
\approx0.9990154165261.
\]
Neither inequality on \(\mu\) is established by SM16 or this SM17 pass. A failure against the **one-sided cap** does not furnish a negative witness to the original operator; actual \(T\) must be evaluated for that.

## 4. Positive-subspace dimension is not an operator-closure metric

**SM17-B (analytic).** If a finite-dimensional subspace \(V\subset\operatorname{Dom}(A_*)\) is strictly \(Q_o\)-positive, it can be extended to a strictly positive supported odd subspace of dimension \(\dim V+1\) using a sufficiently high-frequency physical odd test. This can be repeated to produce arbitrarily large finite-dimensional positive subspaces even when full odd positivity has not been proved.

**Proof.** Take a bounded nonzero even envelope \(w\) on \([-B,B]\), smooth in the interior, e.g. \(w(x)=\operatorname{sinc}(2\pi x/100)\), and \(g_N(x)=w(x)\sin(2\pi Nx)\). By Riemann–Lebesgue, \(g_N\rightharpoonup0\) in \(H_o\) while \(\|g_N\|_2^2\to\|w\|_2^2/2>0\). Compactness of \(R_o\) implies \(\|R_og_N\|_2\to0\). Consequently \(\liminf_NQ_o[g_N]\ge\kappa_*\|w\|_2^2/2>0\). For every fixed \(v\in V\), \(\langle A_*v,g_N\rangle\to0\) because \(A_*v\in H_o\), and \(\langle R_ov,R_og_N\rangle\to0\); all mixed \(Q_o(v,g_N)\to0\). The fixed positive \(V\)-block, a positive diagonal \(g_N\)-block and vanishing cross terms give strict positivity on \(V+\mathbb Rg_N\) by finite Schur complement for sufficiently large \(N\). For each fixed \(N\), the original multiplier grows at most logarithmically and the finite-interval smooth-envelope cut has Fourier decay \(O(1/|\xi|)\), giving \(g_N\in\operatorname{Dom}(A_*)\).

This is an **existence** statement, not an explicit all-rational SM17 3D certificate. It exposes why growing from one to two to three favorable directions is not monotonically approaching W-ODD-NEG. A strategically selected direction in the actual negative packet carrier may still be informative.

## 5. Custody and next action

**Analytic-only result:** conditioned compact spectral reduction, exact adversarial-witness extraction, positive-dimension diagnostic. **Exact-rational result:** the conditional cap threshold and its conservative margin. No new 890-column eigenvalue, original whole odd positivity, whole Weil-form theorem, global bridge, Lean RH theorem, or independent mathematical review.

**Next actionable calculation:** bound the true supported \(G=C^{1/2}U^*A_*^{-1}UC^{1/2}\) on **all 890 columns**, pole conditioned and coupled, or rigorously improve the SM10 cap. Seek a certified \(\mu\) lower than the displayed sufficient threshold (or directly bound top spectrum of \(T\)). Do not prioritize arbitrary 3D witness inflation over that obligation.

Exact arithmetic replay: \`python scripts/validate_rpb108_sm17_compact_spectral_gate.py\`. This replay does not formalize the analytic proofs.