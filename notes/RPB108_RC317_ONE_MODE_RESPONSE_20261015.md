# RC317 — First nonzero original signed high-response trial, with a full but coarse residual payment

**Parent:** RC316 merge \`eb58711cc46bb1df6d15d219cd5e033150a091de\`.  
**Carrier:** original CC27 Weil form identified on the completed $D$-energy space by RC313; $B=11/10$.  
**Standing:** **not a full inverse response and not a positive Schur witness**. Stage I, F4, RH and full Lean formalization remain OPEN.

## Recast the signed RC316 high-cross into the canonical $D$ metric

Let $u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)$, and write $D_n=H_n+s$ with the pinned RC129 bounds on $s$. In the $D$-orthonormal representation put $v_n=u_n/\sqrt{D_n}$. RC315 gives a positive enclosure for the *physical* original $Q(u_0,u_0)$, and RC316 gives a rigorously **positive** enclosure for

$$
A_{244}:=\sqrt{489}\,Q(u_{244},u_0)>0.
$$

The relevant normalized $D$-Riesz matrix entries are thus

$$
\mathsf B_{00}=Q(u_0,u_0)/s,\qquad
b=\langle v_{244},N_0v_0\rangle_D
=\frac{A_{244}}{\sqrt{489\,s(H_{244}+s)}}>0.
$$

The validator uses exact rational harmonic sums and outward integer-square-root enclosures; no floating-point interpolation enters these rescalings.

## A 2x2 original signed principal block actually survives the coupling

RC283/314 certify the positive *even* high complement of the rank-317 split, with lower floor $\mu_e>0$ starting at degree 244. Therefore

$$
a_{244}:=\langle v_{244},N_0v_{244}\rangle_D\ge\mu_e.
$$

The pinned interval inequalities establish

$$
\mathsf B_{00}^{\rm lower}\mu_e-(b^{\rm upper})^2>0.
$$

Hence the **original**, nonaugmented $2\times2$ principal quadratic form on $\mathrm{span}\{v_0,v_{244}\}$ is strictly positive. This is a nontrivial extension of RC315's positive low-only block: it explicitly retains RC316's signed cross. It cannot certify the whole 317-mode principal block, much less its Schur complement.

## A real, nonzero, one-mode high-response trial

RC292's augmented even reference satisfies $N_0\preceq G_{\rm aug}\preceq\nu I$. Crucially, this makes $\nu$ an **upper quadratic-form bound** for the *original* $N_0$; it does not make it an absolute operator-norm bound.

Choose the explicitly positive rational

$$
\alpha=b_{\rm lower}/\nu>0,\qquad
Yv_0=\alpha v_{244},\quad Yv_j=0\text{ for other low coordinates}.
$$

This is an actual finite-support high-response **trial**, not a computed inverse $C^{-1}T$. For $N_0=\begin{psmallmatrix}\mathsf B&T^*\\T&C\end{psmallmatrix}$, completing the square with the test vector $v_0-\alpha v_{244}$ yields

$$
S_{00}=\mathsf B_{00}-\langle Tv_0,C^{-1}Tv_0\rangle
\le\mathsf B_{00}-2\alpha b+\alpha^2a_{244}
\le\mathsf B_{00}-\frac{b_{\rm lower}^2}{\nu}
<\mathsf B_{00}.
$$

This is a **strict upper bound** on the *actual* full Schur quadratic form at one low input. It demonstrates that eliminating the high modes really lowers the effective low quadratic value. It is emphatically **not** a positive *lower* bound on $S_{00}$.

The projected residual along $v_{244}$ is paid using $\mu_e\le a_{244}\le\nu$:

$$
0\le b-\alpha a_{244}\le b_{\rm upper}-\alpha\mu_e.
$$

The complete high residual is $R=T-CY$. RC313's independent absolute norm bound $\|N_0\|\le M$ pays **all other high directions**, albeit very conservatively:

$$
\|Rv_0\|_D\le M(1+\alpha),\qquad
\|Rv_0\|_D^2\le M^2(1+\alpha)^2.
$$

This is a valid whole-space **residual upper bound**, not an explicitly calculated residual Gram or a useful enough margin for RC314's $-\mu^{-1}R^*R$ correction. The negative correction overwhelms any hoped-for strict lower Schur certificate with this coarse estimate.

## Boundary and next cursor

This checkpoint adds an explicit signed high-response trial, proves positivity of one coupled $2\times2$ original principal block, pays the full high residual in the $D$ norm by an admittedly weak analytic inequality, and quantifies a strict Schur **upper** contraction. **No full positive Schur lower bound, signed inverse, or Stage I closure is established.**

**RC318:** compute the actual original high response on additional high modes, evaluate $CY$ and $T$ via source actions, and replace the global residual-norm bound with a sharp Parseval/source-tail residual Gram. Until that work is done, there is no claim that the rank-301/317 Schur operator is positive.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc317_one_mode_response.py --output certificates/rpb108_rc317_one_mode_response.json
python scripts/validate_rpb108_rc317_one_mode_response.py --output certificates/rpb108_rc317_one_mode_response.json --replay
\`\`\`
