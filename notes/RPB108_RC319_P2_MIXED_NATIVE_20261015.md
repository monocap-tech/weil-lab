# RC319 — Complete native P2 source, signed mixed low Gram, and full high response bound

**Parent:** merged RC318 at \`6b7a605542b765a6555810098fca86d6610a6d13\`.  
**Object:** the unaugmented signed CC27 Weil form at aperture $B=11/10$, identified on the completed $D$-energy carrier by RC313.  
**Standing:** the *original low $P_0/P_2$ principal form* is rigorously positive, and the **complete** native $P_2$ high source is paid. The high-eliminated $P_0/P_2$ Schur subspace, full rank-317 Schur matrix, Stage I, F4, RH, and Lean are **OPEN**.

## 1. The missing second native source

Let $u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)$, with $P_2(t)=(3t^2-1)/2$. Unlike RC318's piecewise-constant prime source $K_{\rm prime}u_0$, the original *signed* $K_{\rm prime}u_2$ is a **piecewise quadratic** profile built from all fourteen supported translations

$$
K_{\rm prime}u_2(x)=
-\sum_{m\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(m)}{\sqrt m}
\left[\widetilde u_2(x+\log m)+\widetilde u_2(x-\log m)\right].
$$

The validator constructs its exact rational-center pieces on all fifteen support segments. Its complete physical $L^2$ source mass is computed by integrating the square *with all prime/principal interference terms retained*. There is no replacement by a loose sum of seven individual norms.

## 2. Rational projection onto 256 even Legendre modes

Set

$$
A_n^{(2)}=
\sqrt{\frac{2n+1}{5}}\,
\langle u_n,K_{\rm prime}u_2\rangle.
$$

Using zero extension and parity for even $n$,

$$
A_n^{(2)}
=-(2n+1)\sum_m\frac{\Lambda(m)}{\sqrt m}
\int_{-1}^{1-\log m/B}
P_n(t)P_2\!\left(t+\frac{\log m}{B}\right)\,dt.
$$

The integral is reduced to $J_{n-2},\ldots,J_{n+2}$, where $J_k(z)=\int_{-1}^zP_k(t)dt=[P_{k+1}(z)-P_{k-1}(z)]/(2k+1)$ for $k\ge1$; the two initial degrees are integrated directly. The degree-$511$ Legendre recurrence is evaluated at independent rational centers for each prime displacement.

This produces all **256 even coefficients $n=0,2,\ldots,510$**. The independent selfadjoint mixed-source identity is checked exactly:

$$
\boxed{5A_0^{(2)}=A_2^{(0)}.}
$$

RC318's $A_2^{(0)}$ is computed anew, rather than trusting a frozen mixed coefficient.

## 3. The *complete* infinite tail, not an extrapolation

The exact rational-center source norm and Parseval give

$$
E^{(2)}_{\ge512,\mathrm{center}}
=\|K_{\rm prime}^{\mathrm{center}}u_2\|_2^2
-\sum_{\substack{0\le n<512\\n\text{ even}}}
\frac{5\,|A_n^{(2)}|^2}{2n+1}
\ge0.
$$

The actual logarithms and prime coefficients are enclosed by rational atanh and integer-square-root intervals. Their effect on the *entire translated function* is paid in physical $L^2$, including the moving support boundaries:

$$
\|T_{\ell+\delta}u_2-T_\ell u_2\|_2
\le\sqrt{\frac{5|\delta|}{2B}}
+\frac{\sqrt{15}}B|\delta|.
$$

The first term is the jump at the truncated support edge; the second pays the interior polynomial displacement. Both signed directions and coefficient uncertainties are included. If $\varepsilon_2$ is the resulting global native source defect, then

$$
\boxed{
\|P_{\ge512}K_{\rm prime}u_2\|_2
\le\sqrt{E^{(2)}_{\ge512,\mathrm{center}}}+\varepsilon_2 .
}
$$

This is an infinite-dimensional certified bound, not a claim that 256 projections exhaust the source.

## 4. A new positive original $P_0/P_2$ principal matrix

The original physical low diagonal and mixed entry are reconstructed from **all** source terms: $J$, actual logarithmic endpoint, regular archimedean convolution, signed seven-prime source, and positive even pole.

The full regular-kernel Taylor polynomial is integrated *symbolically* using the overlap polynomials

$$
C_{00}(h)=2-h,\quad
C_{02}(h)=-\frac{h(h-2)(h-1)}2,\quad
C_{22}(h)=\frac25-h+\frac{h^3}2-\frac{3h^5}{40}.
$$

The inherited RC46 **uniform analytic error** is charged to each physical operator entry.

The pole matrix is computed from positive rational cosh moments $M_j=\int_{-1}^{1}P_j(t)\cosh(Bt/2)dt$ with an explicit Taylor remainder:

$$
K_{\rm pole}|_{\{0,2\}}
=B\begin{pmatrix}
M_0^2&\sqrt5M_0M_2\\
\sqrt5M_0M_2&5M_2^2
\end{pmatrix}.
$$

The normalized original physical low quadratic matrix is

$$
Q_{\{0,2\}}=
\begin{pmatrix}
Q_{00}&Q_{02}\\Q_{02}&Q_{22}
\end{pmatrix}.
$$

Its determinant and second Schur pivot are tested with **outward rational intervals**, not sampling. The resulting certificate establishes **determinant (>0.0001538789640705221)** and **second physical low pivot (>0.0038226828652162424)**; the original (Q_{22}) is enclosed approximately in ([0.1992600091,0.1992650954]). The script verifies strict positivity of the principal block and explicitly separates that from the high-eliminated Schur block.

## 5. Whole-space high action and remaining obstruction

RC283/314's buffered even cut begins at degree 244. For $244\le n\le510$ the exact original endpoint contribution in P2-scaled coordinates is

$$
E_{n2}=\frac{2n+1}{(n-2)(n+3)}.
$$

The validator combines $E_{n2}$ with the signed original prime $A_n^{(2)}$ **before** squaring each finite high coefficient and applying its proper $D$ denominator. The remaining $n\ge512$ output is paid using the Parseval prime tail and the independent telescope

$$
\sum_{n\ge512}
\frac{5(2n+1)}{(n-2)^2(n+3)^2}
<\frac6{512^2}.
$$

The complete RC46 analytic regular-kernel defect and the even-pole high tail are paid in $L^2$. The resulting $D$-high norm $\|Tv_2\|_D$ is a bound for the **actual original action**, not a finite sample.

The RC314 high floor $\mu_e>0$ gives the conservative diagonal Schur test

$$
\langle v_2,Sv_2\rangle
\ge B_{22}^{\rm lower}-\frac{\|Tv_2\|_{D,\rm upper}^2}{\mu_e}.
$$

**The resulting conservative lower bound is negative:** about (-0.03747761095816). This is an **inconclusive bound**, not a proof that the Schur diagonal is negative. The completely paid (|Tv_2|_D) upper bound is approximately **0.02018211569324**. Thus RC318's successful (P_0) scalar technique does **not** simply transfer to (P_2) with the same global high coercivity floor. The mixed high-response Gram is bounded by Cauchy–Schwarz, but its *signed covariance* and the actual correction through $C^{-1}$ are not yet evaluated.

**No full $2\times2$ Schur positivity claim is made from a positive $2\times2$ original low matrix.** This distinction is essential because the low determinant is small and coupling to the high complement may alter its inertia.

## RC320 — next cursor

Use the joint P0/P2 finite and infinite native source profiles to compute their **signed high-response covariance**, then construct a useful multi-mode $Y$ and a sharper corrected Schur Loewner bound. The ordinary physical original low matrix and the high-eliminated Schur matrix are different objects. Even if that two-input Schur test succeeds, 120 additional even low coordinates and 195 odd coordinates remain.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc319_p2_mixed_native.py --output certificates/rpb108_rc319_p2_mixed_native.json
python scripts/validate_rpb108_rc319_p2_mixed_native.py --output certificates/rpb108_rc319_p2_mixed_native.json --replay
\`\`\`

No unproved global positivity, Stage I, F4, Lean or Riemann Hypothesis conclusion is imported from these tests.
