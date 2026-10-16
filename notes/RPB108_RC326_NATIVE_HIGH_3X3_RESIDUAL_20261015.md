# RC326 — First positive original signed 3×3 high block and complete Ritz residual

**Parent:** integration RC325 \`477c757619a82d282219832ca448338045150db7\`.  
**Source:** original CC27 signed Weil quadratic form on the completed RC313 $D$-Riesz carrier, at $B=11/10$.  
**Certified result:** original even high restriction on degrees $244,246,248$ is strictly positive; the finite three-mode inverse-Ritz gain strictly exceeds the **best possible** two-mode gain; a *complete* original infinite-high residual is now paid by a valid, intentionally conservative upper bound.  
**Not proved:** positivity of the entire 278-coordinate high head or of the three-dimensional *low* Schur block, a useful full $C^{-1}$ approximation, far-tail cross-operator sharpening, Stage I, F4, Lean, or RH.

## 1. Extend the first genuine original signed high matrix

RC325 established a positive non-diagonal original signed high block on degrees 244 and 246. RC326 computes the three missing original signed entries

$$
C_{244,248},\quad C_{246,248},\quad C_{248,248},
$$

and combines them with the *unchanged pinned intervals* from RC325.

The new entries use **21 additional exact rational-center prime overlap integrals**, with the seven active original prime powers, genuine shifted support edges, signed coefficients, and rigorous Leibniz/Markov derivative bounds paying real logarithms and coefficient uncertainty. The original logarithmic endpoint and scalar contribution are included exactly or by rigorous interval, while RC324's complete regular-kernel compression and even-pole bounds are charged. This is not an augmented positivity proxy.

The interval matrix is

$$
C_{\{244,246,248\}}\in
\begin{pmatrix}
[0.41882734,0.42431167]&[0.05963281,0.06513731]&[0.02833023,0.03385482]\\
[0.05963281,0.06513731]&[0.43512207,0.44064675]&[0.04058790,0.04613274]\\
[0.02833023,0.03385482]&[0.04058790,0.04613274]&[0.42956443,0.43512945]
\end{pmatrix}.
$$

The displayed decimals are only rounded explanatory endpoints; the stored JSON has exact rational intervals.

The validator proves the first and second leading Sylvester minors positive, plus the complete third determinant:

$$
\boxed{\det C_{\{244,246,248\}}>0.07516712427727>0.}
$$

In fact it also proves the **whole three-dimensional Loewner bound**

$$
\boxed{C_{\{244,246,248\}}\succeq0.31983522656747I}
$$

using rigorous rowwise Gershgorin estimates (smallest lower diagonal less the *sum of absolute upper off-diagonals*). This result applies to the finite *compression*, not to the rest of the high operator.

## 2. New native low/high cross and a three-mode Ritz improvement

For RC323's rational low witness

$$
x=\frac3{25}v_0-\frac{23}{8}w_2+w_4,
$$

RC326 independently computes the native original signed cross to degree 248. The new coefficient is enclosed near

$$
\langle v_{248},N_0x\rangle_D\approx-1.1232778794\times10^{-5}.
$$

It uses RC323's 520-digit outward fixed-point Legendre recurrence, full real-log/weight uncertainty, complete original prime and endpoint sources, and inherited original regular/pole high-source error. Previously certified native crosses to 244 and 246 are imported by pinned rational certificate.

A rational three-mode inverse-Ritz trial obtained from the enclosed high-block midpoint is frozen exactly as

$$
\boxed{
y=
(0.0000892987843196,\;
-0.0000560812365094,\;
-0.0000267785010573).
}
$$

Its exact outward rational signed correction is

$$
\Delta_3(y)=2\langle Tx,y\rangle_D-\langle y,Cy\rangle_D,
\qquad
\boxed{\Delta_3(y)>4.32396458376635\times10^{-9}.}
$$

To avoid comparing the new trial with a merely *approximate* old trial, RC326 rigorously upper-bounds the **optimal** two-coordinate correction:

$$
\Delta_{2,\max}
=
b_{\{244,246\}}^*\,C_{\{244,246\}}^{-1}\,b_{\{244,246\}}
<4.20636621346541\times10^{-9}.
$$

Thus

$$
\boxed{\Delta_3(y)-\Delta_{2,\max}>
1.17598370300953\times10^{-10}>0.}
$$

This proves that a third original high coordinate provides a genuinely improved signed inverse response beyond the *optimal* two-coordinate Ritz inverse—not merely beyond a previous rounded trial.

As before, the Ritz correction gives a **strict upper bound** on the actual full high-eliminated quadratic value, and by itself cannot establish its positivity.

## 3. Pay the **entire infinite-dimensional** original residual, honestly

Unlike RC325, this checkpoint includes a rigorous full-space residual certificate for the explicitly chosen $Yx=y_0v_{244}+y_1v_{246}+y_2v_{248}$:

$$
R_x=Tx-CYx.
$$

First, the three represented high coefficients of $R_x$ are explicitly enclosed using the **full native signed 3×3 matrix** and signed source. Their combined norm obeys

$$
\boxed{\|P_{\{244,246,248\}}R_x\|_D
<8.226008034\times10^{-7}.}
$$

This small finite-head residual is **not** the full residual. For the entire original high carrier, the already certified full-source bounds from RC318, RC320, and RC321, combined with RC323's rational low coordinates, give

$$
\|Tx\|_D<0.00142409936114.
$$

The original operator's full completed $D\to D$ norm bound from RC313 satisfies $\|N_0\|<9.921$. Since $C$ is its high compression,

$$
\|CYx\|_D\le\|N_0\|\,\|Yx\|_D
<0.00107931488459.
$$

The latter bound **pays all represented and unrepresented high modes**, including coupling into the full infinite even far tail beyond degree 800. Applying the triangle inequality (with deliberate double payment of the few represented components) gives the strict whole-space upper

$$
\boxed{\|R_x\|_D<0.00250341424572.}
$$

Under the inherited original-even global high coercivity $\mu_{244}$, the RC314 **correct-sign** residual penalty is therefore rigorously bounded:

$$
\boxed{\mu_{244}^{-1}\|R_x\|_D^2
<0.00115492865737.}
$$

**This residual payment is real but currently too conservative.** It is larger than the original nearly-null low quadratic value $\langle x,B_{\rm low}x\rangle$, which was enclosed above by $7.9845\times10^{-5}$. Hence this checkpoint does **not** establish a positive Schur *lower* bound for this witness. The certified native three-mode Ritz gives only an improved Schur **upper** contraction; nothing about the sign of the actual Schur value is assumed.

## 4. Remaining true structural target

We have both an explicit finite high inverse-Ritz approximation and a *valid* full original high residual upper. These are two distinct obligations; only their combination yields RC314's residual-corrected lower expression

$$
S\ \succeq\
B-T^*Y-Y^*T+Y^*CY
-\mu^{-1}(T-CY)^*(T-CY).
$$

The present whole-space residual is too large because we paid the entire $CY$ tail with a global operator norm rather than its genuine signed source and Parseval interference. To improve it, RC327 should evaluate and bound the full native source $C v_{244},C v_{246},C v_{248}$ and their signed covariance with $Tx$, including the precise coupling into the degrees 250–798 and the far tail $800+$.

Importantly, the finite high block remains only three of **278** high-head modes; a positive $3\times3$ compression does **not** certify the whole 278-dimensional head or its coupling to the remaining infinite high space. None of the 119 untested even low modes or 195 odd low modes has been discharged.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc326_native_high_3x3_residual.py --output certificates/rpb108_rc326_native_high_3x3_residual.json
python scripts/validate_rpb108_rc326_native_high_3x3_residual.py --output certificates/rpb108_rc326_native_high_3x3_residual.json --replay
\`\`\`

All calculations refer to inherited original CC27–RC313 mathematical definitions. Passing the exact rational replay and GitHub CI is reproducibility evidence, **not** independent peer review, and is not a proof of RH.
