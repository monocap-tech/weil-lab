# RC327 — A native cross-to-infinite-high operator bound and a sharper full residual

**Parent:** integrated RC326 at \`99316d9eda3f74323603c9f6da2a6cfd34bec022\`.  
**Object:** original CC27 signed Weil quadratic form, on the completed RC313 $D$-carrier at $B=11/10$.  
**Verified result:** a genuine **original-operator** cross norm from the selected high degrees $244,246,248$ into **every other even high degree $n\ge250$**, with a separate certified infinity-tail estimate beyond $n=800$. Together with RC326's exact rational Ritz vector, this yields a rigorously sharper full-space residual and a **2.87-fold reduction** in the conservative residual penalty.  
**Not proved:** positive full low $P_0/P_2/P_4$ Schur, invertibility estimates for the full 278-mode head, complete head-to-tail cross norm, Stage I, F4, Lean or RH.

## 1. Replace RC326's global-norm payment by the actual off-block operator

The original high compression $C=P_{\ge244}^{\mathrm{even}}N_0P_{\ge244}^{\mathrm{even}}$ is decomposed as

$$
\mathcal H_{\ge244}^{\mathrm{even}}
=
\underbrace{\operatorname{span}\{v_{244},v_{246},v_{248}\}}_{\mathcal K_3}
\oplus
\underbrace{\mathcal H_{\ge250}^{\mathrm{even}}}_{\mathcal K_\perp}.
$$

RC326 already computed the exact original signed $C|_{\mathcal K_3}$ and certified its positive determinant. It bounded the omitted source $P_{\mathcal K_\perp}CY$ using the completed operator's global norm $\|N_0\|<9.921$. That paid the entire infinite carrier but was far too loose.

RC327 instead computes a valid norm for the **actual cross block**

$$
E=P_{\mathcal K_\perp}CP_{\mathcal K_3}.
$$

Because the scalar, identity and harmonic $J$ terms are **diagonal in the original Legendre carrier**, their cross block is exactly zero. The only remaining native contributors are the true logarithmic endpoint $W_B$, the signed seven-prime translations, the RC46 regular convolution and the even-pole rank-one term. No off-diagonal interaction of these latter terms is assumed zero.

## 2. Logarithmic endpoint: exact finite Hilbert–Schmidt and infinite tail

For even $n>m$, the original logarithmic endpoint has a known off-diagonal Legendre coefficient. On the canonical $D$-normalization its square is

$$
\left|\langle v_n,W_Bv_m\rangle\right|^2
=\frac{(2n+1)(2m+1)}
{(n-m)^2(n+m+1)^2(H_n+s)(H_m+s)}.
$$

RC327 sums this *exact rational expression with the certified lower $s$ enclosure* for all three inputs $m=244,246,248$ and every even $n=250,252,\ldots,798$. Its entire squared Hilbert–Schmidt norm satisfies

$$
\boxed{\|E_W|_{250\le n\le798}\|_{\rm HS}^2
<0.006790376281.}
$$

The infinite tail is not sampled or extrapolated. For $n\ge800$,

$$
n-m\ge n\left(1-\frac m{800}\right),\quad
n+m+1\ge n,\quad
2n+1\le\left(2+\frac1{800}\right)n.
$$

Together with $H_n+s\ge H_{800}+s_{\min}$, these imply a rational majorant proportional to $n^{-3}$. The whole remaining squared sum is controlled by

$$
\sum_{\substack{n\ge800\\n\text{ even}}}\frac1{n^3}
\le\sum_{n=800}^{\infty}\frac1{n^3}
\le\int_{799}^{\infty}t^{-3}dt
=\frac1{2\cdot799^2}.
$$

The certified result is

$$
\boxed{\|E_W|_{n\ge800}\|_{\rm HS}^2
<0.000044196695.}
$$

Consequently, the complete logarithmic endpoint cross operator obeys $\|E_W\|<0.082671477$.

## 3. Remaining *original* signed cross-action

The native physical seven-prime source has the pinned original operator norm $\|P\|_{L^2}<4.103149$. Input and output are independently $D$-normalized: for inputs in $\mathcal K_3$ and outputs $n\ge250$,

$$
\|P_{\ge250}D^{-1/2}PD^{-1/2}P_{\mathcal K_3}\|
\le\frac{\|P\|_{L^2}}
{\sqrt{(H_{244}+s_{\min})(H_{250}+s_{\min})}}.
$$

This estimate pays all prime overlaps, including original zero-extension edges, without falsely claiming they vanish.

The RC324 **high/high** operator estimate pays the regular kernel using the same two $D$ denominators. For the even pole, Legendre orthogonality to the Taylor polynomial of $\cosh(x/2)$ gives a geometric bound on all cosine coefficients in the represented and unrepresented modes; the complete rank-one cross norm is paid, with no finite truncation assumption.

Adding these four native source contributions yields the following **operator**, not just coordinate, estimates:

| Actual original signed $C$ cross block | Certified operator norm upper |
|---|---:|
| Three high inputs $\{244,246,248\}\to$ degrees 250–798 | $0.497281829$ |
| Three high inputs $\to$ all degrees 800–$\infty$ | $0.399135320$ |
| **Three high inputs $\to$ all degrees 250–$\infty$** | **$0.497549566$** |

The last bound is calculated directly over the entire orthogonal output as the endpoint Hilbert–Schmidt budget plus a single original prime operator budget. The finite and infinite estimates are **separate restrictions**, not additive components of an alleged block-diagonal operator.

In particular, for RC326's fixed exact rational Ritz vector $Yx$,

$$
\boxed{\|P_{\ge250}CYx\|_D<0.000054131166}
$$

and independently

$$
\boxed{\|P_{\ge800}CYx\|_D<0.000043424137}.
$$

These are **whole-space** bounds on the omitted high responses, including every mode, not just the first finite 278-mode head.

## 4. Entire signed residual and its correct negative Schur penalty

RC326's represented three-mode signed residual obeys

$$
\|P_{\mathcal K_3}(Tx-CYx)\|_D
<8.226009\times10^{-7}.
$$

RC327 also uses Parseval orthogonality to remove the already certified nonzero energy in the three represented original $Tx$ coordinates from the inherited full original high-source upper norm. The remaining original signed source is enclosed by

$$
\|P_{\ge250}Tx\|_D
\le
\sqrt{\|Tx\|^2_{\rm upper}
-\sum_{n\in\{244,246,248\}}|b_n|^2_{\rm lower}}.
$$

Paying the genuine native cross-to-infinite action of the rational $Yx$, and then combining the represented and unrepresented residuals **orthogonally**, yields

$$
\boxed{\|R_x=Tx-CYx\|_D<0.001477654156.}
$$

For comparison, RC326 could only show $\|R_x\|_D<0.002503414246$ with the global $\|N_0\|$ approach.

Under the inherited original even high-complement coercivity, the full correct-sign RC314 residual correction now satisfies

$$
\boxed{
\mu_{244}^{-1}\|R_x\|_D^2
<0.000402379011.
}
$$

The previous correction was $<0.001154928658$. Thus **the upper bound falls by a factor exceeding 2.87**.

**This is not yet a positive full Schur lower bound.** The original low quadratic upper is only around $7.98\times10^{-5}$, so the certified negative residual payment remains too large. Any positivity claim would require a more precise signed source norm and especially the covariance of $Tx$ with $CYx$. The RC327 certificate intentionally records Stage I and full three-mode Schur positivity as open.

## 5. RC328 — the remaining cancellation

The original selected three-mode $C$ cross action is now bounded across *every* unrepresented high mode, with separate finite and far-infinite estimates. The chief source of slack has shifted from the old global $\|N_0\|$ norm to the crude independent triangle bounds on $\|P_{\ge250}Tx\|$ and $\|P_{\ge250}CYx\|$.

RC328 should reconstruct the original signed **combined** low witness source $Tx$ and the high-trial source $CYx$ on a common Legendre/Parseval carrier, preserving mixed source covariance before taking norms. It should also obtain a sharper original signed prime cross norm for the specific three-coordinate $Yx$, rather than use the full unrestricted prime operator norm.

An actual full-rank-317 Schur theorem would still need all 122 even and 195 odd low dimensions, and certification of the complete 278-coordinate high head/Feshbach interface.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc327_high_interface_residual.py --output certificates/rpb108_rc327_high_interface_residual.json
python scripts/validate_rpb108_rc327_high_interface_residual.py --output certificates/rpb108_rc327_high_interface_residual.json --replay
\`\`\`

All mathematical statements inherit the pinned CC27–RC313 operator identification. Reproducible Actions checks are not independent peer review and are not proof of the Riemann hypothesis.
