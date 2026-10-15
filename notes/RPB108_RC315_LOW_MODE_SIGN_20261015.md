# RC315 — Original signed Weil P0/P1 low-mode sign audit

**Parent:** RC314 merge \`f63b5a6e85edb6d2fedf111a5a9f133db3c05c3e\`.  
**Object:** the *original* CC27 signed Weil form at $B=11/10$, identified with the native operator at RC313.  
**Standing:** positive on the particular $P_0/P_1$ subspace only; full Schur positivity, Stage I, F4, RH and Lean remain OPEN.

## Actual source and physical normalization

Write $u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)$; these are physically $L^2[-B,B]$-orthonormal, **not** $D$-normalized. RC312/313 identify the original quadratic form with

$$
Q=J+W_B+c_R I-K_{\rm reg}+K_{\rm prime}+K_{\rm pole},
\qquad c_R=-\gamma-\log(2\pi\cdot2B).
$$

Here $JP_n=H_nP_n$, $W_B=\log2-\tfrac12\log(1-t^2)$, the prime term uses both zero-extended signed translations for each active prime power, and the pole is positive rank-one on even inputs but negative rank-one on odd inputs. There is **no additional** Poisson contact mass.

The independent closed formulas for the first two modes are:

| Term | $u_0$ | $u_1$ |
|---|---|---|
| $J$ | $0$ | $1$ |
| $\langle W_B\rangle$ | $1$ | $4/3$ |
| normalized prime overlap at $\ell>0$, $d=\ell/B$ | $1-d/2$ | $1-3d/2+d^3/4$ |
| full prime | $-2\sum\Lambda(n)C_{00}(\log n)/\sqrt n$ | same with $C_{11}$ |
| pole | $16\sinh^2(B/2)/B$ | $-3(4\cosh(B/2)-8\sinh(B/2)/B)^2/B$ |

The sum runs over $n\in\{2,3,4,5,7,8,9\}$. Each degree-$k$ regular-kernel monomial contributes $2r_k(2B)^{k+1}\int_0^1v^kC_{ii}(2Bv)\,dv$. The independent rational recurrence for the 193 inherited RC46 coefficients is checked against the pinned Git blob; the RC46 analytic uniform remainder is fully paid using $|C_{ii}(t)|\le1$.

The validator encloses $\gamma$ using the harmonic-number bound $H_{128}-\log128-1/256<\gamma<H_{128}-\log128-1/256+1/(12\cdot128^2)$. Logarithms use positive rational atanh series with upper remainder, pi uses Machin's identity with alternating arctangent remainder, and hyperbolic moments use positive Taylor series. No floating-point sampling or quadrature is needed.

## Result

The rational outward enclosures are approximately:

$$
0.040254 <\langle u_0,Qu_0\rangle<0.040260,\qquad
0.132385 <\langle u_1,Qu_1\rangle<0.132391.
$$

Reflection symmetry gives $\langle u_0,Qu_1\rangle=0$ **exactly**. Thus the *original* $2\times2$ principal quadratic form is positive. This sharpens RC46's much wider intervals for these two original-form entries, but it does not imply a positive Schur complement.

**Open:** no original $301/317$ principal block, high coupling $T$, signed inverse response $Y$, residual Gram, or strict full Schur lower bound has been certified. Even a positive principal block can have a negative Schur complement; RH, F4, Stage I and Lean remain open.

## Next cursor — RC316

Compute an actual nonzero original signed cross-block entry $T=QN_0P$ with a rigorously bounded high tail, then construct $Y$ and pay the signed residual $R=T-CY$ in RC314's **minus-sign** Schur formula. No positivity transfer is allowed from the two low-mode diagonals alone.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc315_low_mode_sign.py --output certificates/rpb108_rc315_low_mode_sign.json
python scripts/validate_rpb108_rc315_low_mode_sign.py --output certificates/rpb108_rc315_low_mode_sign.json --replay
\`\`\`
