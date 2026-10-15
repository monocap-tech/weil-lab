# RC316 — First nonzero native signed low-to-high cross

**Parent:** merged RC315 \`43e11169dbb14759331e7db0252d7633ba67d030\`.  
**Object:** original CC27 signed Weil form at $B=11/10$, using RC313's all-degree source identification, RC314's high-complement split, and RC46's analytic kernel remainder.  
**Status:** **new signed cross-block information** at both rank-301 and buffered rank-317 cuts. Neither inverse response nor original Schur positivity is established.

## Exact high-cross reduction

Let $u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)$ be physically orthonormal. For even $N\ge194$, the original mixed-form entry $Q(u_N,u_0)$ has no contributions from the harmonic operator $J$ or scalar contact: these are diagonal in the Legendre basis.

The physical endpoint $W_B$ contributes exactly

$$
\sqrt{2N+1}\,\langle u_N,W_Bu_0\rangle
=\frac{2N+1}{N(N+1)}.
$$

For each active prime power $m\in\{2,3,4,5,7,8,9\}$, set $\ell_m=\log m$ and $c_m=\Lambda(m)/\sqrt m$. Both *zero-extended* translations of $u_0$ yield the boundary identity

$$
\sqrt{2N+1}\,\langle u_N,K_{\rm prime}u_0\rangle
=-\sum_m c_m
\left[P_{N+1}(1-\ell_m/B)-P_{N-1}(1-\ell_m/B)\right].
$$

This is the original signed prime action, not a fitted matrix column. The validator encloses every $\ell_m$ and $c_m$ by rational atanh/square-root intervals and computes the *center* Legendre values using an exact degree-$(N+1)$ recurrence. Its input uncertainty is paid via the standard $|P_n|\le1$ and $\sup_{[-1,1]}|P'_n|\le n(n+1)/2$ bounds, not unstable naïve interval recursion.

### The regular and pole tails are exceptionally small here

The RC46 degree-192 polynomial $r_{192}(|x-y|)$ sends the constant $u_0$ to a polynomial of degree at most 193: each monomial integrates to $(B+x)^{k+1}+(B-x)^{k+1}$. The projection onto $P_N$ therefore vanishes **exactly** for $N\ge194$. For the *full* regular convolution, only the inherited uniform remainder $\varepsilon$ survives:

$$
|\langle u_N,K_{\rm reg}u_0\rangle|\le2B\varepsilon.
$$

For the positive even signed pole, Taylor orthogonality of $P_N$ against polynomials of degree below $N$ and $e^B<4$ yield

$$
|\langle u_N,K_{\rm pole}u_0\rangle|
\le 16B(B/2)^N.
$$

This is a deliberately conservative explicit upper bound, not a numerical truncation.

The **scaled** first even high-mode entry is thus rigorously enclosed around the finite rational prime+endpoint center, paying $(N+1)$ times both full-source errors (because $\sqrt{2N+1}\le N+1$).

## Results

| Reference | First even high degree | Certified scaled cross $\sqrt{2N+1}\,Q(u_N,u_0)$ |
|---|---:|---:|
| Minimal rank 301 | $N=232$ | approximately **$-0.1150568790$**, strictly negative |
| Buffered rank 317 | $N=244$ | approximately **$+0.0392669670$**, strictly positive |

The JSON certificate contains rigorous outward rational intervals and individual prime components; decimals above are explanatory only.

Because the D-harmonic metric is strictly positive, scaling to the RC314 $D$-Riesz representation preserves **nonzero** cross action in either reference. Consequently the signed high block $T$ is *not zero*. An assumption that low modes decouple from the high complement would be incorrect.

## Boundary and next operation

These are **two entries**, not the full $T$ action. In particular, the positive $2\times2$ original low block of RC315 and these two certified off-diagonal entries do **not** imply positivity of either finite Schur complement. No $C^{-1}T$, trial high response $Y$, residual Gram, complete rank-301/317 Schur matrix, Stage I, F4 or RH is claimed.

**RC317:** construct a genuine original high response and the complete signed residual $T-CY$ (with all infinite tails), then test the **negative** residual correction from RC314. Avoid assigning a global positivity status from the present finite-dimensional observations.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc316_first_high_cross.py --output certificates/rpb108_rc316_first_high_cross.json
python scripts/validate_rpb108_rc316_first_high_cross.py --output certificates/rpb108_rc316_first_high_cross.json --replay
\`\`\`
