# RC318 — Complete signed prime Parseval tail gives a strictly positive original P0 Schur diagonal

**Parent:** RC317 merge \`69de93f053014810f5a8554e202130f9a0025bcb\`.  
**Native object:** the unaugmented CC27 signed Weil form at aperture $B=11/10$, identified on the completed $D$-energy carrier by RC313.  
**Standing:** the **P0 diagonal of the rank-317 even Schur complement is strictly positive**. The full $122\times122$ even Schur block, the $195\times195$ odd block, Stage I, F4, RH and Lean remain **OPEN**.

## Why RC317's coarse residual was insufficient

RC317 constructed a nonzero signed one-high-mode trial, but only paid its entire residual via the global operator norm $\|N_0\|\le M$. This gave an unusably large Schur correction. RC318 directly reconstructs the complete high-source action of the original signed form on the normalized constant Legendre mode and pays its entire infinite tail by signed Parseval cancellation.

Let $u_n(x)=\sqrt{(2n+1)/(2B)}P_n(x/B)$ be physically orthonormal, $D_n=H_n+s$, and $v_n=u_n/\sqrt{D_n}$. The buffered rank-317 low reference has 122 even modes $n=0,2,\dots,242$ and an even high complement beginning at $n=244$. RC283/314 certify its **original unaugmented signed** high restriction $C\succeq\mu_e I$, $\mu_e>0$.

On $u_0$, the original operator is

$$
Q u_0=(J+W_B+c_R I-K_{\rm reg}+K_{\rm prime}+K_{\rm pole})u_0.
$$

The $J$ and scalar terms have zero high projection. Every degree $n\ge244$ is also orthogonal to the degree-at-most-193 polynomial obtained by applying RC46's degree-192 regular-kernel Taylor polynomial to $u_0$. Only the rigorously bounded analytic remainder of $K_{\rm reg}$ survives.

## Signed original prime source: a complete Parseval audit

The physical signed prime output is a *fourteen-step piecewise constant function*, two opposite, zero-extended translations for each $m\in\{2,3,4,5,7,8,9\}$. Write $\ell_m=\log m$ and $c_m=\Lambda(m)/\sqrt m$, retaining the sign and the base-prime coefficient.

The **exact** full physical source energy, including all interference terms, is

$$
\|K_{\rm prime}u_0\|_2^2
=\frac1B\sum_{m,k}c_mc_k
\left[
 2B-\max(\ell_m,\ell_k)
 +\max(0,2B-\ell_m-\ell_k)
\right].
$$

RC318 evaluates an outward rational upper interval using certified log and square-root bounds. No nonsigned triangle estimate replaces these cross terms.

For even $n\ge2$, the exact scaled physical coefficient is

$$
A_n:=\sqrt{2n+1}\,\langle u_n,K_{\rm prime}u_0\rangle
=-\sum_m c_m
 \left[
  P_{n+1}(1-\ell_m/B)
 -P_{n-1}(1-\ell_m/B)
 \right].
$$

The constant coefficient is

$$
A_0=-\sum_m c_m(2-\ell_m/B).
$$

The validator independently evaluates **256 coefficients** $n=0,2,\dots,510$ by exact rational Legendre recurrence. Arguments and prime coefficients are enclosed using positive rational atanh and integer-square-root intervals. It pays the evaluation-center uncertainty without propagating unstable interval recurrence, instead using $\sup|P_n'|\le n(n+1)/2$. The independently derived $n=232,244$ scaled *full signed original* entries re-enclose RC316's certified values.

Parseval now gives a completely paid upper estimate for the **remaining 512-to-infinity prime source**:

$$
E_{\rm prime}^{\ge512}
\le
(\text{outward full physical source mass})
-\sum_{\substack{0\le n<512\\ n\text{ even}}}
(\text{certified lower projection energy at }n).
$$

All terms on the right are rational and reproduce in reverse evaluation order.

## Endpoint and infinite high-output accounting

For even $n\ge244$ the physical endpoint coefficient is known in closed form:

$$
\langle u_n,W_Bu_0\rangle
=\frac{\sqrt{2n+1}}{n(n+1)}.
$$

The complete signed endpoint+prime coefficient is computed **together** for $244\le n\le510$ and weighted by the exact $D$-denominator. The endpoint output beyond 512 has an independent telescoping bound

$$
\sum_{n\ge512}\frac{2n+1}{n^2(n+1)^2}
=\frac1{512^2},
$$

an upper bound also valid for the even subsequence. The native RC46 analytic regular residual and the exponentially decaying signed even pole are separately paid in full physical $L^2$ and therefore in the high $D$ response.

The resulting exact-rational enclosure is a true **whole-high-space** bound for

$$
\|Tv_0\|_D^2
=\sum_{\substack{n\ge244\\n\text{ even}}}
\frac{|\langle u_n,Qu_0\rangle|^2}
{s\,(H_n+s)}.
$$

This is **not** a finite projection presented as a complete infinite action.

## First strict original scalar Schur lower bound

Write the full original $D$-Riesz block matrix (even sector)

$$
N_0=\begin{pmatrix}\mathsf B&T^*\\ T&C\end{pmatrix},
\qquad C\succeq\mu_e I.
$$

The exact Schur quadratic on the *constant low mode* is

$$
\langle v_0,Sv_0\rangle
=\mathsf B_{00}-\langle Tv_0,C^{-1}Tv_0\rangle.
$$

Using $C^{-1}\preceq \mu_e^{-1}I$ and RC315's original positive low diagonal,

$$
\boxed{
\langle v_0,Sv_0\rangle
\ge\mathsf B_{00}^{\rm lower}
-\frac{\|Tv_0\|_{D,\rm upper}^2}{\mu_e}
>0.
}
$$

The validator checks this strict inequality in rational arithmetic, with **certified normalized scalar margin at least 0.0009150876542712128** (rounded downward) and a rigorously upper-bounded full high-response squared norm of **0.00005249300408810548** (rounded upward). It is a genuinely **positive lower** Schur certificate for this **single** low vector, unlike RC317's upper Schur contraction. The trial $Y=0$ in RC314's exact residual formula already suffices once the *original full native source tail* is paid sharply. The nonzero RC317 trial remains separately valid but is not needed for this lower-bound proof.

**Do not infer $S>0$ from $\langle v_0,Sv_0\rangle>0$**: the untested 121 remaining even low coordinates, 195 odd coordinates, and their cross-covariances may still obstruct positivity.

## Next cursor — RC319

Transport this rigorous signed native Parseval machinery to $P_2$ and selected *mixed even* inputs, paying the full original two-source signed cross-covariance. Then grow a proven-positive subspace inside the rank-317 Schur block. Establishing all positive principal pivots (with coupling paid) and the odd counterpart is still necessary for full Stage I closure.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc318_p0_signed_schur.py --output certificates/rpb108_rc318_p0_signed_schur.json
python scripts/validate_rpb108_rc318_p0_signed_schur.py --output certificates/rpb108_rc318_p0_signed_schur.json --replay
\`\`\`

The result is a certificate within the existing CC27–RC313 mathematical definitions, not independent peer review or a proof of RH.
