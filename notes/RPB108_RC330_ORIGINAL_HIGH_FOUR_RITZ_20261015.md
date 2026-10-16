# RC330 — Original signed four-mode high block and reoptimized Ritz after the adverse degree-250 covariance

**Parent:** live route-consolidation integration \`f5b1f41d3c5fb8147a7db277a166cbb4463f3abe\` (includes RC329 and separate SI05).  
**Operator:** original signed CC27 Weil form on the completed RC313 $D$-Riesz carrier at $B=11/10$.  
**Verified result:** the original high compression on degrees **244,246,248,250** is strictly positive and its exact-rational four-coordinate high Ritz trial **strictly exceeds the best possible** old three-coordinate correction.  
**Not proved:** complete high $C^{-1}$, positive original low three-dimensional Schur, positive full 278-mode high head, Stage I, F4, Lean, RH.

## 1. The issue inherited from RC329

The previous three-coordinate original high Ritz vector

$$
Y_3x = y_{244}v_{244}+y_{246}v_{246}+y_{248}v_{248}
$$

had a **provably adverse** original signed covariance with the first omitted high output $n=250$:

$$
b_{250}=\langle v_{250},Tx\rangle_D>0,\qquad
(CY_3x)_{250}<0.
$$

The actual original residual $R_{250}=b_{250}-(CY_3x)_{250}$ was therefore larger than $b_{250}$. Increasing accuracy on the unchanged trial would not reverse that certified sign. RC330 addresses the structural issue by **including degree 250 among the high trial coordinates**, not by assuming a positive covariance.

## 2. Certify the missing original signed diagonal

RC329 already supplied the genuine original signed high cross entries $C_{250,244}$, $C_{250,246}$ and $C_{250,248}$. RC330 computes their missing companion

$$
C_{250,250}=\langle v_{250},N_0v_{250}\rangle_D
$$

from the original CC27/RC313 definition, preserving the full logarithmic endpoint, original scalar, **all seven prime powers with both signed zero-extended translations**, RC324's full high/high regular kernel operator norm, and the signed even hyperbolic pole.

In particular the original prime diagonal is obtained through the seven exact rational-center integrals

$$
-\sum_{m\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(m)}{\sqrt m}
\int_{-1}^{1-\log(m)/B}
P_{250}(t)P_{250}(t+\log(m)/B)\,dt,
$$

with rigorous outward payment for real logarithms, square-root prime coefficients, **moving support endpoints** and Legendre polynomial derivatives through the Leibniz/Markov bound. This uses the original signed translations, not a supplementary matrix.

The exact rational certificate establishes the original prime diagonal interval

$$
0.0001792261375920<\mathrm{Prime}_{250,250}<0.0001792942819436,
$$

and the complete original signed $D$-normal high diagonal

$$
\boxed{0.43883606531229<C_{250,250}<0.44444137698004.}
$$

All other nine high entries are pinned unchanged to the verified RC326/329 certificates.

## 3. Positive original four-mode high compression

The resulting original signed high block has approximate center

$$
C_{\{244,246,248,250\}}\approx
\begin{pmatrix}
0.421570&0.062385&0.031093&0.010116\\
0.062385&0.437884&0.043360&0.025400\\
0.031093&0.043360&0.432347&0.037469\\
0.010116&0.025400&0.037469&0.441639
\end{pmatrix}.
$$

These are explanatory centers; all theorem inequalities use the exact outward rational **entry intervals**, not decimal rounding.

The Sylvester determinant of the original signed four-coordinate block satisfies

$$
\boxed{\det C_{\{244,246,248,250\}}>0.03256054223448>0.}
$$

Even stronger, interval Gershgorin estimates certify for **every** vector in the four-coordinate subspace

$$
\boxed{
C_{\{244,246,248,250\}}\succeq0.29566952834492\,I.
}
$$

This is a genuine finite original-operator Loewner bound, **not** a lower bound on the entire original infinite high complement, or on its 278-coordinate finite head.

## 4. A reoptimized four-coordinate native Ritz response

Retain RC323's exact original low rational test input

$$
x=\frac3{25}v_0-\frac{23}{8}w_2+w_4.
$$

Use the separately certified original signed sources $b_{244},b_{246},b_{248}$ from RC325/326 and $b_{250}$ from RC329. Form the complete signed four-vector $b$ and solve the rational-centered $4\times4$ high Ritz system, rounding its output to explicitly frozen rational numbers.

The new original rational trial is approximately

$$
\boxed{
Y_4x=
0.0000886365037852\,v_{244}
-0.0000590372126143\,v_{246}
-0.0000317232422490\,v_{248}
+0.0000610273565907\,v_{250}.
}
$$

The fourth coefficient is **positive**, correcting the degree-250 adverse behavior of the old omitted-mode response.

For a finite original high trial define

$$
\Delta_4(y)=2b^\top y-y^\top C_4y.
$$

The exact interval calculation certifies

$$
\boxed{\Delta_4(Y_4x)>5.8741460325558\times10^{-9}.}
$$

### Comparison with the **optimal**, rather than approximate, three-mode response

The inherited old three-mode trial $Y_3$ is not assumed exactly optimal. For its native original block $C_3\succ0$, the exact quadratic variational identity is

$$
\max_z\{2b_3^\top z-z^\top C_3z\}
=
\Delta_3(Y_3)+
(b_3-C_3Y_3)^\top C_3^{-1}(b_3-C_3Y_3).
$$

RC326 independently supplies a rigorous complete **represented** three-mode residual norm, and a positive Gershgorin floor $\lambda_{\min}(C_3)>0.3198352$. Therefore the extra optimization gap is bounded above, with all signed original source intervals paid, by $\|b_3-C_3Y_3\|^2/\lambda_{\min}(C_3)$.

This proves

$$
\Delta_{3,\mathrm{optimal}}<4.4893886781607\times10^{-9}
$$

and hence the strict nontrivial improvement

$$
\boxed{
\Delta_4(Y_4x)-\Delta_{3,\mathrm{optimal}}
>1.3847573543951\times10^{-9}>0.
}
$$

The new coordinate improves the native inverse Ritz trial even compared with the **globally optimal correction on the old three-dimensional high subspace**.

## 5. Complete infinite-space residual: paid, but not improved

A finite positive compression with a larger Ritz upper correction does **not** by itself provide a smaller full-space residual.

RC330 independently pays the complete source $\|Tx\|$ using RC328's signed 278-mode computation and infinite Parseval tails, and the entire actual high action $\|CY_4x\|$ using the inherited genuine completed original operator norm $\|N_0\|<9.921$. This accounts for **all unrepresented modes**, without pretending the finite Ritz inverse is the full $C^{-1}$.

The resulting valid but coarse whole-space bounds are

$$
\|Tx\|_D<0.001052229,\quad
\|CY_4x\|_D<0.001257707,\quad
\boxed{\|Tx-CY_4x\|_D<0.002309935.}
$$

The corresponding correct-sign RC314 residual penalty is

$$
\boxed{\mu_{244}^{-1}\|Tx-CY_4x\|_D^2<0.000983307.}
$$

This is **larger** (worse) than RC328's full residual-penalty bound $\approx0.000225252475$ for the **different** old three-coordinate Ritz vector. It would be mathematically improper to reuse the old trial's small full residual on the new four-mode vector. The script records this change of vector and its whole-space penalty explicitly.

The strict four-mode Ritz gain gives only a stronger Schur **upper** bound along the single original low direction. It is **not** a positive three-dimensional Schur **lower** bound.

## 6. RC331: use the new trial's native outside-high action

The next necessity is to certify the actual original high cross action from **all four** Ritz directions, especially the newly added degree 250, into every omitted even high output degree $n\ge252$. This should recover RC327's endpoint Hilbert–Schmidt and original signed prime/regular/pole cross estimates for the expanded input subspace, while preserving its genuine signed covariance with $Tx$.

The full 278-mode finite high head and the strongly coercive infinite far tail must still be coupled in a provably valid inverse framework. All 119 untested even and 195 odd low coordinates remain unproved; Stage I/F4/Lean/RH are **open**.

### Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc330_original_high_four_ritz.py --output certificates/rpb108_rc330_original_high_four_ritz.json
python scripts/validate_rpb108_rc330_original_high_four_ritz.py --output certificates/rpb108_rc330_original_high_four_ritz.json --replay
\`\`\`

This is a reproducible exact-rational certificate **conditional on the inherited CC27–RC313 identification**, not an independently peer-reviewed proof of the Riemann hypothesis.
