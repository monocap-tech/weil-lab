# RC334 — Original signed five-mode high Ritz repair

**Parent:** RC333 merged at \`472088bcfd39fa374b9fed2d0c960d976ef5af48\`.  
**Operator:** original signed CC27/RC313 Weil \(D\)-Riesz high block at \(B=11/10\), with original low witness \(x=\frac3{25}v_0-\frac{23}8w_2+w_4\).

## Mathematical question

The RC330 four-mode rational high Ritz trial on \(\{244,246,248,250\}\) encounters a strictly adverse original signed source/high-action covariance at degree \(254\) (RC333). Unlike refining interval precision for the *same* trial, adding this degree can change its optimization geometry. Determine whether a genuine original five-mode compression is positive and whether the resulting **reoptimized** trial strictly beats the *optimal* original four-mode Ritz gain.

## Genuine original five-mode extension

Pin all ten RC330 original signed \(C_4\) intervals, plus all four original RC333 native \(C_{254,m}\) intervals (not a proxy positive operator). Reconstruct the missing diagonal \(C_{254,254}\) from **seven original rational-center Legendre prime-translation overlaps** with complete real log/weight/support perturbations. Include the exact logarithmic endpoint diagonal, refined original scalar, RC324 complete regular high-kernel error, even-pole contribution, and canonical physical-to-\(D\) factor.

Form \(C_5\) on degrees \(244,246,248,250,254\). A strictly positive all-row Gershgorin floor is a valid original signed \(5\times5\) Loewner certificate. Use RC330's original \(b_{244},b_{246},b_{248},b_{250}\), RC333's independently reconstructed \(b_{254}\), and the original \(C_5\) midpoint to compute a rational Ritz vector \(Y_5x\).

For the unchanged previous \(Y_4x\), bound the *best possible* four-mode gain using its rigorously certified finite-coordinate residual and minimum \(C_4\) eigenvalue:

\[
\Delta_{4,\max}\le \Delta_4(Y_4x)+
\frac{\|b_4-C_4Y_4x\|^2}
{\lambda_{\min}(C_4)}.
\]

Then calculate \(\Delta_5(Y_5x)=2\langle b_5,Y_5x\rangle-\langle C_5Y_5x,Y_5x\rangle\) with interval-certified original signed entries. A strict excess beyond \(\Delta_{4,\max}\) is a **genuine finite-dimensional Ritz improvement** over *every* original four-mode trial. It is only an **upper** Schur witness for one low vector.

## Exact replay result

GitHub's initial exact-rational replay established an ORIGINAL signed five-mode Gershgorin floor
(C_5 \succeq 0.26935368866 I_5), with
(0.43457576695246<C_{254,254}<0.44026160101705).

The new rational fifth Ritz coefficient is
(y_{254}=146963997313/625000000000000>0).
The original five-mode gain is rigorously
(\Delta_5>2.93365510561\times10^{-8});
the certified optimal four-mode bound is
(\Delta_{4,\max}<6.20012098224\times10^{-9}).
Therefore
(\boxed{\Delta_5-\Delta_{4,\max}>2.313643007386\times10^{-8}}).
All original signed matrix intervals, five-mode rational coefficients,
gain endpoints and full error data are pinned in the RC334 JSON
certificate and replayed without decimal floating-point arithmetic.

**Important full-space limitation:** The changed five-mode trial has
a conservative whole-infinite residual bound (<0.003754193) and
a corrected-sign penalty bound (<0.002597304), *worse* than the
separate RC333 four-mode bounds (<0.001150649) and (<0.000243992).
The certified gain is a finite Ritz gain, not an improved full
Schur lower estimate. Native outside-space coupling must be
recomputed for Y5.

## Residual custody

The RC333 complete infinite residual belongs to **Y4**, not the reoptimized **Y5**; it must not be carried across the change. RC334 therefore constructs an independent conservative complete \(Y_5\) residual from RC328's original signed whole \(Tx\) norm plus the native complete original high \(C\) operator norm. The exact newer five-input interface into the omitted degree 252 and 256 through infinity belongs to **RC335**, not this finite compression.

The validator prints full exact rational diagonal, five-mode floor, Ritz gain, strict gain difference, and full residual bounds. These are to be frozen in the JSON certificate only after an independent Actions replay reports their values. No sign or full-space Schur lower result is inferred from the finite high block.

**Open:** full 278-high head and its far-tail coupling, original full \(C^{-1}\), original three-dimensional low Schur **lower** positivity, remaining low sectors, Stage I, F4, Lean, and RH.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc334_original_high_five_ritz.py --output certificates/rpb108_rc334_original_high_five_ritz.json --replay
\`\`\`

This exact-rational input replay is conditional on the inherited original-operator identification, not an independently reviewed RH proof.
