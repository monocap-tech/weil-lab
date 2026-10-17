# SM21 — original SI29 source-specific energy, replacing SM20's scalar Ritz damping

**Active:** W-ODD-NEG OPEN. **Parent:** SM20 (the actual first SM10 negative-frequency Taylor source, center \(c_0=37/64\)), SI29 (exact original 14-feature supported positive Jensen/Bessel minorant), SM18–SM19 (forward residual and pole-conditioned Woodbury). **Standing:** first-source, all-original physically supported rational computation; *not* a whole-890-column inverse certificate. Acceptance of a quantitative gain depends on focused final-head Actions output.

## 1. Actual original source and stronger positive-energy lower bound

Keep \(u_0(x)=\sin(2\pi(37/64)x)\) on the original interval \(I=[-11/10,11/10]\), \(s(x)=\sinh(x/2)\), the full original seven-prime \(m(\xi)\), \(a=\max(m,\kappa)\), and the physically supported \(A_*=A_o-2|s\rangle\langle s|\). The earlier uniform pole-conditioned floor \(\kappa_*=33621/10^9\) supplied only
\[
\langle u_0,A_*u_0\rangle\ge\kappa_*n_-,\quad
0<n_-\le\|u_0\|^2\le n_+.
\]

SI29 establishes the *true original entire-window* lower operator
\[
A_o \succeq C_{14}=\kappa I+\sum_{j=0}^{13}\gamma_j|g_j\rangle\langle g_j|,
\quad \kappa=1/1000,\quad
\gamma_j=\frac{4r_j\delta_j}{3^{d_j}}.
\]
Here \(g_j\) is the actual continuous-band supported Jensen mean (\(d_j=0\)) or first normalized Legendre moment (\(d_j=1\)) and \(r_j,\delta_j\) are SI29's original certified radius and signed-positive multiplier margin. These are genuine original physical functions; Simpson terms are used only to enclose their overlaps.

Let \(I_j=[\ell_j,u_j]\) rigorously enclose \(\langle g_j,u_0\rangle\), including the true SI29 composite-Simpson error \(2B\tau_j\). Define \(s_j^2=\min_{z\in I_j}z^2\), with zero if \(I_j\ni0\), and let \([q_-,q_+]\) enclose \(\langle s,u_0\rangle\). Then
\[
P_L=\kappa n_-+\sum_{j=0}^{13}\gamma_js_j^2,\qquad
Q_L=P_L-2\max(|q_-|,|q_+|)^2
\]
is a completely original, supported, full-source **Rayleigh lower**:
\[
\boxed{\langle u_0,A_*u_0\rangle\ge
q_L:=\max\{\kappa_*n_-,Q_L\}>0.}
\]
This is not a claim that \(C_{14,*}\) dominates the full negative-frequency operator: SM03/SM13 forbid that shortcut. We exploit its genuine positive energy **on one actual source** to choose a better forward trial.

## 2. Original graph-domain Ritz trial and improvement formula

SM20 certified the squared graph bound, with full original a-squared high-frequency exterior already paid:
\[
\|A_*u_0\|^2<M_0=1360n_++\frac{785}{1152}.
\]
For any \(0<\lambda\), the exact true original physical residual \(E_0(\lambda)=u_0-\lambda A_*u_0\) obeys
\[
\|E_0(\lambda)\|^2
=\|u_0\|^2-2\lambda\langle u_0,A_*u_0\rangle+
\lambda^2\|A_*u_0\|^2
\le n_+-2\lambda q_L+\lambda^2M_0.
\]
Take the *actual nonzero, exact-rational* source trial
\[
\boxed{\lambda_{\rm new}=q_L/M_0.}
\]
Then
\[
\boxed{\|E_0(\lambda_{\rm new})\|^2\le
n_+-q_L^2/M_0.}
\]
SM20 used \(\lambda_{\rm old}=\kappa_*n_-/M_0\), giving only the guaranteed reduction \((\kappa_*n_-)^2/M_0\). The exact certified improvement factor is
\[
\boxed{\mathfrak G=\left(\frac{q_L}{\kappa_*n_-}\right)^2.}
\]
No floating-point approximation or independent artificial test source is used in the acceptance. The rational validator reports both strict reductions and \(\mathfrak G\), with an explicit **diagnostic-only** status if the original SI29 energy does not materially improve on the uniform floor.

The original forward residual also yields a complete **single-column** pole interval, fourteen signed source interactions (using all the same original true continuous SI29 means/moments), and the forward-energy diagonal
\[
H_{00}=2\lambda_{\rm new}\|u_0\|^2
-\lambda_{\rm new}^2\langle u_0,A_*u_0\rangle,
\]
including a rigorous upper and lower interval. These are an actual \(D_{00},F_{\cdot0},t_0,H_{00}\) compatible with the SM19 finite-data formulas. The single-column enclosure includes the full Fourier a-squared graph tail inherited from SM20.

## 3. Sign discipline and limitations

The SI29 inequality is a **positive reference** \(C_{14}\preceq A_o\), so it bounds the *actual* source energy from below. The original odd pole \(2|\langle s,u_0\rangle|^2\) is subtracted using its upper interval. The \(\gamma_j\) sources must retain all fourteen signs and true Simpson/Legendre errors. None of these estimates bounds the inverse \(A_*^{-1}\) from above on the entire negative-frequency carrier.

The source-specific reduction can still be insufficient for W-ODD-NEG even if the improvement factor is large. The first column does not measure the worst singular direction of the 890-column synthesis, and the conservative original graph \(M_0\) may remain wasteful. The correct next numerical step is to evaluate the **SM19 pole-correct 14-source residual inverse upper** on this first improved column, including all signed finite Grams and uncertainties; then improve source-local graph tails / Ritz features if the upper is uncompetitive.

**Not proved here:** the other 889 original forward columns, any 890-by-890 residual PSD gate, the full conditioned negative Birman–Schwinger spectral bound, even/whole Weil positivity, the global original-zeta attachment, independent mathematical review, Lean completion, or RH.

Replay: python scripts/validate_rpb108_sm21_native_source_rayleigh.py
