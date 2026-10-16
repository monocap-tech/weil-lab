# RC323 — A rigorous no-go witness for the scalar high-coercivity Schur strategy

**Parent:** integrated RC322, \`99eb1d3ce26ec10bbf612fbbd21c9fd5d46b8349\`.  
**Object:** the **original**, nonaugmented CC27 signed Weil $D$-Riesz model identified by RC313, with the rank-317 even low/high split.  
**Standing:** a strict mathematical obstruction to proving the entire original $P_0/P_2/P_4$ Schur block positive **using only the uniform inherited lower floor of the high complement**. This is **NOT** a negative direction of the actual Weil form or its actual Schur operator; the genuine $C^{-1}$ inverse response and Stage I remain open.

## Why do this instead of tightening another upper residual?

RC322 certified that the complete original low $P_0/P_2/P_4$ principal matrix is positive, while a conservative full high-eliminated $3\times3$ Schur determinant estimate remained inconclusive. The standard bound

$$
C\succeq\mu_eI\quad\Longrightarrow\quad
S=B_{\rm low}-T^*C^{-1}T
\succeq B_{\rm low}-\mu_e^{-1}T^*T
$$

is valid but potentially too weak. Until RC323, we had not ruled out the possibility that recomputing $T$ sufficiently precisely would make that same global-floor test succeed.

**RC323 now rules that out** on the three-dimensional subspace. Its proof uses a lower bound for the **actual signed** $T$ source, not a repeated coarse upper estimate.

## Fixed rational test vector

Use RC322's $D$-normalized boundary-compatible low basis

$$
v_0=\frac{u_0}{\sqrt{s}},\qquad
w_2=\frac{u_2-\sqrt5u_0}{\sqrt{s+H_2}},\qquad
w_4=\frac{u_4-\frac3{\sqrt5}u_2}{\sqrt{s+H_4}},
$$

and its rational linear combination

$$
\boxed{x=\frac3{25}v_0-\frac{23}{8}w_2+w_4.}
$$

The already certified original **low** Gram provides a strict rational upper bound

$$
0<\langle x,B_{\rm low}x\rangle
\le 7.984476150566631\times10^{-5}.
$$

The inherited original-even full high floor is

$$
\mu_e=0.005128787479000777.
$$

Thus the scalar-floor surrogate can only be nonnegative at $x$ if

$$
\|Tx\|_D^2\le
\mu_e\langle x,B_{\rm low}x\rangle
\le4.095068130740646\times10^{-7}.
$$

## Compute a rigorously enclosed *lower* high response

RC323 evaluates **278 actual original signed even high modes** $n=244,246,\dots,798$ in the same $D$ normalization. For each mode, it computes the **joint** $P_0$, $P_2-P_0$, and $P_4-P_2$ signed source **before squaring the combination**. This preserves the source interference that triangle estimates obscure.

The seven native original prime powers and their two signed zero-extended translates contribute the finite scaled coefficients

$$
A_n^{(j)}=-(2n+1)\sum_m
\frac{\Lambda(m)}{\sqrt m}
\int_{-1}^{1-\log(m)/B} P_n(t)f_j(t+\log(m)/B)\,dt,
$$

with $f_j\in\{P_0,P_2-P_0,P_4-P_2\}$. Every endpoint coefficient is added with its original sign: $E_{n0}$, $E_{n2}-E_{n0}$, $E_{n4}-E_{n2}$. The three outputs are rescaled by their **different** positive $D$ input factors, combined with the rational coefficients of $x$, and squared at each individual mode.

To keep a high-degree calculation both rigorous and economical, RC323 introduces a **new rational fixed-point interval Legendre recurrence**, independent of the huge exact-fraction recurrences in RC318–321:

- Each recurrence step is rounded *outward* on a grid with denominator $10^{520}$, including all negative-coefficient interval multiplications.
- The resulting enclosing intervals remain narrower than $10^{-25}$ at the audited high degrees.
- All prime input $\log m$ and $\Lambda(m)/\sqrt m$ uncertainties are subsequently charged in the **full original $L^2$ source**, through RC319's jump-aware translation bound and RC320/RC321's $H^1$ boundary-cancelled translation bounds.
- The original regular-kernel high remainder and signed even-pole tail are subtracted by a complete $D$-norm reverse-triangle bound. The retained RC46 polynomial has zero projection on all $n\ge244$, so no regular-polynomial contribution is silently dropped.

Crucially, **we need only a lower bound from finitely many genuinely native high modes**. Whatever the infinite remainder does, it cannot reduce the squared norm of the already measured orthogonal high projection.

The resulting certified inequalities are

$$
\begin{aligned}
\|P_{\{244,\ldots,798\}}Tx\|_{D,\mathrm{center}}^2
&\ge4.605508452890089\times10^{-7},\\
\text{complete original-source perturbation norm}
&<1.279938\times10^{-18},\\
\boxed{\|Tx\|_D^2
\;\ge\;\|P_{\{244,\ldots,798\}}Tx\|_D^2
&\ge4.605508452890072\times10^{-7}.}
\end{aligned}
$$

Both source and $D$-energy inequalities have exact rational representations in the stored certificate.

## Structural consequence: the global-floor surrogate is indefinite

Combining the strict rational *lower* high-response energy with the strict original low quadratic *upper* bound yields

$$
\boxed{
\|Tx\|_D^2-\mu_e\langle x,B_{\rm low}x\rangle
>5.10440322149\times10^{-8}>0.
}
$$

Consequently

$$
\boxed{
\langle x,(B_{\rm low}-\mu_e^{-1}T^*T)x\rangle
<-9.95245609687\times10^{-6}<0.
}
$$

This is a **proved negative Rayleigh value for the lower comparison operator**. It demonstrates that **even an infinitely precise evaluation of the native $T$ source would not allow the inherited *single uniform floor* $\mu_e$ to prove the complete three-dimensional Schur block positive.** The method fails structurally, not from numerical convergence noise.

The finite signed high-source energy already imposes a necessary *effective scalar-floor-only* threshold

$$
\mu_{\rm scalar\ test}>
\frac{\|Tx\|^2_{\mathrm{certified\ lower}}}
     {\langle x,B_{\rm low}x\rangle_{\mathrm{certified\ upper}}}
>0.00576807841,
$$

at least **12.46% higher** than the currently imported $\mu_e$. Improving the global high floor may help, but merely refining its use at the old value cannot.

### What this does **not** prove

The actual Schur form uses

$$
S=B_{\rm low}-T^*C^{-1}T,
$$

not $B_{\rm low}-\mu_e^{-1}T^*T$. Because $C^{-1}\preceq\mu_e^{-1}I$, the actual correction can be **smaller** along this source. The surrogate's negative Rayleigh value is **not** evidence that the actual Weil quadratic form has a negative direction, does **not** refute full positivity, and does not close the 3D gate.

There is also no positivity claim for the remaining even and odd low modes, Stage I, F4, Lean or RH.

## RC324 — necessary change of method

The next productive frontier is now specifically to compute a **mode-sensitive original high inverse response**, such as an explicit high trial $Y\approx C^{-1}T$ with paid residual $R=T-CY$, or a finite principal high-block inversion plus rigorously controlled infinite complement, using RC314's *correct minus-sign* correction

$$
S\succeq B-T^*Y-Y^*T+Y^*CY-\mu_e^{-1}R^*R.
$$

The relevant objective is a signed **inverse-weighted** covariance, not another large batch of high Legendre coefficients followed by division by the same global $\mu_e$.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc323_coercivity_nogo.py --output certificates/rpb108_rc323_coercivity_nogo.json
python scripts/validate_rpb108_rc323_coercivity_nogo.py --output certificates/rpb108_rc323_coercivity_nogo.json --replay
\`\`\`

This checkpoint is conditional on the inherited CC27/RC313 completed-model identification and has not received independent mathematical peer review.
