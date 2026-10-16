# RC324 — Smooth regular-kernel compression and a genuine two-tier original high operator

**Parent:** integrated RC323, \`15665091da594ffa73cdfa63f62bcc133939c779\`.  
**Operator:** the original CC27 signed Weil $D$-Riesz model, identified through RC313/314, supported on $[-B,B]$ with $B=11/10$.  
**Standing:** **a certified positive original even high *tail operator* for every degree at least 800**, a first original 278-coordinate even high **diagonal profile**, and an explicit signed *one-coordinate Ritz trial* for RC323's nearly-null low witness. **Neither a positive finite high head nor a positive three-dimensional Schur restriction is yet certified.** Stage I, F4, full Lean and RH remain open.

## 1. Why a second high cutoff is useful

The rank-317 Schur split has 122 even low modes, ending at degree 242; the original even high complement begins at degree 244. RC323 proved that the inherited global coercivity floor on that whole complement, approximately

$$
\mu_{244}\simeq0.005426380968,
$$

is too small to certify the entire $P_0/P_2/P_4$ Schur restriction by the naive global-floor comparison.

We should no longer regard all infinite high modes as having the same effective stiffness. RC324 begins the required *native mode-sensitive* high-operator investigation by proving that the **far even tail** beginning at degree 800 is substantially better conditioned.

Partition the original even high carrier orthogonally as

$$
\mathcal H_{\ge244}^{\mathrm{even}}
=\operatorname{span}\{u_{244},u_{246},\dots,u_{798}\}
\oplus\mathcal H_{\ge800}^{\mathrm{even}}.
$$

The first component has **278 physical/D orthogonal high modes**, and the second has infinitely many.

**This is not a block-diagonalization of the Weil operator:** its off-diagonal coupling across the split must still be computed and paid. A lower floor on each diagonal block cannot be combined into a weighted Loewner bound on the full $C$ without that interface.

## 2. Prove the regular kernel is tiny on *every* high/high restriction

Let $k_{192}(r)=\sum_{j=0}^{192}a_jr^j$ be the exact rational RC46 Taylor polynomial for the original even archimedean regular kernel, with full uniform remainder $\varepsilon_{46}$. Here $a_0=1/4$ and $a_1=-1/48$.

For an arbitrary physical high Legendre combination $f=\sum_{n\ge N}c_nu_n$ with $N\ge2$, let

$$
F(x)=\int_{-B}^{x}f(y)\,dy.
$$

Every high $u_n$ is orthogonal to constants, so $F(-B)=F(B)=0$. The exact Legendre antiderivative formula gives

$$
F_n(x)=
\frac{B}{\sqrt{(2n+1)(2n+3)}}\,u_{n+1}(x)
-
\frac{B}{\sqrt{(2n+1)(2n-1)}}\,u_{n-1}(x).
$$

Two shifts by neighboring Legendre degrees and the triangle inequality imply the **whole-subspace operator bound**

$$
\boxed{\|F\|_2\le \frac{2B}{2N-1}\|f\|_2.}
$$

For the even kernel $k_{192}(|x-y|)$, the **distributional** identity is

$$
\partial_x\partial_y k_{192}(|x-y|)
=-k_{192}''(|x-y|)-2k_{192}'(0)\delta(x-y).
$$

The diagonal Dirac term is necessary: omitting it would incorrectly discard the cusp in the absolute-distance kernel. Integrating by parts twice (with no boundary contributions) yields the original regular-form estimate

$$
|\langle f,K_{\rm reg}f\rangle|
\le
\left(2|a_1|+2B\sup_{0\le r\le2B}|k_{192}''(r)|\right)
\left(\frac{2B}{2N-1}\right)^2\|f\|_2^2
+2B\varepsilon_{46}\|f\|_2^2,
$$

where the polynomial derivative is bounded by the **exact rational coefficient majorant**

$$
\sup|k_{192}''|
\le\sum_{j=2}^{192}j(j-1)|a_j|(2B)^{j-2}.
$$

Crucially, the above holds for **every finite or completed high combination**, not just diagonal Legendre entries. It establishes a genuine high **operator norm** bound for $K_{\rm reg}$.

The stored outward rational certificate gives

$$
\boxed{
\|P_{\ge244}K_{\rm reg}P_{\ge244}\|<5.536047\times10^{-5}
}
$$

and

$$
\boxed{
\|P_{\ge800}K_{\rm reg}P_{\ge800}\|<5.135240\times10^{-6}.
}
$$

These operator bounds pay the full RC46 analytic remainder; they do not presume that the absolute-distance polynomial convolution annihilates high Legendre modes.

## 3. A strict, substantially stronger *full even far-tail* coercivity

RC314 supplies the original decomposition

$$
N_0=I+D_s^{-1/2}hD_s^{-1/2}
+D_s^{-1/2}(P-K_{\rm reg}+K_{\rm pole}-rI)D_s^{-1/2},
\quad
h=-\frac12\log(1-t^2)\ge0,\quad r=\frac{789}{125}.
$$

The original signed even pole $K_{\rm pole}|_{\rm even}\succeq0$. The pinned RC313 bound $\|P\|_{L^2}\le4.103149$ applies to the genuine signed original prime translations.

For any even input **entirely supported in Legendre degrees $n\ge800$**, these facts give

$$
\langle f,N_0f\rangle_D\ge
\left[
1-\frac{r+\|P\|+\|P_{\ge800}K_{\rm reg}P_{\ge800}\|}
{H_{800}+s_{\rm lower}}
\right]\|f\|_D^2.
$$

All components are rational, including the harmonic sum $H_{800}$ and the pinned enclosure on $s$. The certificate passes

$$
\boxed{
P_{\ge800}^{\rm even}N_0P_{\ge800}^{\rm even}
\succeq0.05864904241368\,I.
}
$$

This is **more than 10.8 times** the certified global *even* floor for the original rank-317 complement beginning at $n=244$.

The conclusion is a real **infinite-dimensional lower bound** on the original far-tail compression, not a claim of positivity for the coupling between the finite head and far tail.

## 4. First 278-mode original signed high *diagonal* profile

For an individual physically normalized even Legendre mode $u_n$, the original diagonal endpoint is the exact harmonic expression

$$
W_{nn}=2(H_{2n}-H_n)+\frac{1}{2n+1}.
$$

Hence, using RC322's refined original $c_R$ interval, the complete original even high coordinate has a lower and upper enclosure via

$$
\frac{H_n+W_{nn}+c_R^{\rm lower}
-\|P\|-\|K_{\rm reg}|_{\ge n}\|}
{H_n+s_{\rm upper}}
\;\le\;
\langle v_n,N_0v_n\rangle_D
\;\le\;
\frac{H_n+W_{nn}+c_R^{\rm upper}
+\|P\|+\|K_{\rm reg}|_{\ge n}\|+\operatorname{pole}_n^{\rm upper}}
{H_n+s_{\rm lower}}.
$$

The even pole is nonnegative for the lower bound, and a rigorous Taylor/Legendre orthogonality bound $\operatorname{pole}_n\le100B(B/2)^{2n}$ pays the upper bound.

RC324 tests **every even degree from 244 through 798**, with the minimum lower bound attained at degree 244:

$$
\boxed{0.01578960501460<\langle v_{244},N_0v_{244}\rangle_D<0.846563391291.}
$$

Individual high-mode diagonal values are larger than the inherited full-operator floor. **The diagonal profile is not a matrix-level high-head coercivity estimate**: off-diagonal entries can still change the smallest eigenvalue.

## 5. Explicit nonzero *native* one-coordinate Ritz response

RC323 previously evaluated the original signed high cross between its rational nearly-null low witness

$$
x=\frac3{25}v_0-\frac{23}{8}w_2+w_4
$$

and the first even high coordinate $v_{244}$.

In the exact completed $D$ normalization, RC324 converts that pinned signed source into a strictly positive cross enclosure

$$
b=\langle v_{244},N_0x\rangle_D
>3.3314401457719\times10^{-5}.
$$

The original high diagonal upper bound above makes the **explicit rational, nonzero high trial**

$$
Yx=\alpha v_{244},
\qquad
\alpha=\frac{b_{\rm lower}}{(C_{244,244})_{\rm upper}}>0,
$$

well-defined. It satisfies

$$
\langle x-\alpha v_{244},N_0(x-\alpha v_{244})\rangle_D
\le B[x,x]-\frac{b_{\rm lower}^2}{(C_{244,244})_{\rm upper}},
$$

with a certified strict improvement

$$
\boxed{
\frac{b_{\rm lower}^2}{(C_{244,244})_{\rm upper}}
>1.311005597342\times10^{-9}.
}
$$

Because the true Schur quadratic is the **infimum over all high responses**, the trial provides a rigorous **upper bound** on the actual high-eliminated value. This is an actual *mode-sensitive original signed Ritz trial*, not an evaluated $C^{-1}$ action or a positive lower Schur certificate. No whole-high residual $T-CY$ has been evaluated at this checkpoint.

## 6. Exactly what becomes possible next

RC324 produces a useful rigorously certified two-tier high architecture:

| Part | Dimension | Certified information |
|---|---:|---|
| Original high head $244\le n\le798$ | 278 even modes | 278 positive **diagonal intervals** and a signed one-mode Ritz trial |
| Original far even high tail $n\ge800$ | Infinite | **Entire compression** coercive with floor $>0.0586490424$ |
| **Cross action between the two** | Infinite by 278 | **Not yet computed** |

The next frontier, **RC325**, is therefore not to run another undifferentiated approximation of $T$ or reuse the weak $\mu_{244}$ uniform inverse. We must calculate a **native finite high-head matrix** $A$, the **head-to-tail coupling** $E$, and a paid residual response into the improved far-tail operator $D$. The exact high inverse would then be reduced by a second Schur/Feshbach transformation,

$$
C=\begin{pmatrix}A&E^*\\ E&D\end{pmatrix},
\qquad
D\succeq0.0586490424I,\qquad
A-E^*D^{-1}E,
$$

with the **correct negative correction**. No finite-head positivity, useful full inverse estimate, 3D Schur positivity, Stage I/F4/Lean or RH follows until that coupling is certified.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc324_high_tail_smoothing.py --output certificates/rpb108_rc324_high_tail_smoothing.json
python scripts/validate_rpb108_rc324_high_tail_smoothing.py --output certificates/rpb108_rc324_high_tail_smoothing.json --replay
\`\`\`

All numerical certificates are conditional on the inherited CC27–RC313 original Weil operator identification; successful GitHub Actions replay is reproducibility evidence, not independent mathematical peer review.
