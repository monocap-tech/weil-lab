# RC329 — First native original outside-high covariance, with an adverse sign

**Parent:** RC328 integrated at \`c6a25abccb7ee8ec1b36c27016abbaebc571fbaf\`.  
**Original operator:** the unaugmented signed CC27 Weil $D$-Riesz operator (identified in RC313), $B=11/10$.  
**Certified result:** an exact-rational, fully error-paid **signed mixed covariance** between the low witness response $Tx$ and the existing three-mode high Ritz action $CYx$ in the first omitted even high mode $n=250$. **Its sign is strictly negative**, so the old Ritz vector increases the original residual in that mode. The previous RC328 complete infinite residual bound remains stronger than the one-mode split bound. **No full three-dimensional Schur or Stage I closure is claimed.**

## 1. The question left open by RC328

RC328 carried out the original signed combination of the three low-source columns on 278 even output modes, cutting the whole high residual penalty to about $0.000225252475$. That calculation did **not** directly measure the mixed inner product in

$$
\|Tx-CYx\|_D^2
=\|Tx\|_D^2+\|CYx\|_D^2
-2\,\operatorname{Re}\langle Tx,CYx\rangle_D.
$$

The sign matters: a positive mixed term reduces the residual, while a negative mixed term increases it. RC329 tests that sign for the first output coordinate *outside* RC326's native three-mode high Ritz trial.

Keep the low vector and high trial unchanged:

$$
x=\frac3{25}v_0-\frac{23}{8}w_2+w_4,\qquad
Yx=y_{244}v_{244}+y_{246}v_{246}+y_{248}v_{248},
$$

where the three exact rational $y$ coordinates are pinned in RC326.

## 2. Compute the actual original signed high cross

The new required native matrix elements are

$$
C_{250,244},\qquad C_{250,246},\qquad C_{250,248}.
$$

For all three input modes, RC329 evaluates the **21 original signed seven-prime translation overlaps** in rational arithmetic at controlled logarithmic centers:

$$
-\sum_{m\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(m)}{\sqrt m}
\int_{-1}^{1-\log(m)/B}
P_i(t)P_{250}(t+\log(m)/B)\,dt.
$$

The true logarithms and prime weights, support shifts and clipped boundary movement are charged by rigorous Leibniz/Markov bounds; no displacement is treated as an exact decimal.

The original logarithmic endpoint off-diagonal is inserted through its exact Legendre formula. Original $J$, identity and scalar terms vanish across different Legendre degrees, while the **full high/high regular-kernel compression** from RC324 and the tiny signed even-pole rank-one tail are paid by outward intervals. All entries are converted using the canonical $D$ input/output denominators.

The resulting original signed high matrix entries obey:

| Original signed high entry | Certified interval |
|---|---:|
| $C_{250,244}$ | $[0.0073436799825,\;0.0128882468034]$ |
| $C_{250,246}$ | $[0.0226175969021,\;0.0281825004129]$ |
| $C_{250,248}$ | $[0.0346759941176,\;0.0402611455428]$ |

Their widths include the original regular kernel and all signed prime source uncertainties. These are genuine operator cross entries, not a diagonal positivity proxy.

## 3. The decisive sign: finite Ritz response is adverse

RC328 independently certified the actual original signed $Tx$ source amplitude at $n=250$, with complete actual-source error charged:

$$
\boxed{
2.5160514756777\times10^{-5}
<b_{250}=\langle v_{250},Tx\rangle_D
<2.5160514756780\times10^{-5}.
}
$$

Contracting the new native cross entries against RC326's **unchanged rational Ritz trial** gives a rigorously **negative** high action:

$$
\boxed{
-2.002860905\times10^{-6}
<
(CYx)_{250}
<
-1.046089174\times10^{-6}.
}
$$

Thus the actual original signed mixed covariance has the opposite sign from a beneficial residual cancellation:

$$
\boxed{
-5.039302\times10^{-11}
<
\langle P_{250}Tx,P_{250}CYx\rangle_D
<
-2.632014\times10^{-11}<0.
}
$$

No statistical extrapolation or model assumption is used to fix that sign.

Because $b_{250}>0$ and $(CYx)_{250}<0$,

$$
\boxed{
(b_{250}-(CYx)_{250})>b_{250}>0.
}
$$

The represented original residual in this *first omitted output direction* therefore **increases** when applying the old three-mode Ritz correction. The entire interval for its actual coefficient is enclosed by

$$
2.6206603931\times10^{-5}
<(Tx-CYx)_{250}
<2.7163375662\times10^{-5}.
$$

This is a local **adverse high-residual sign**, **not** a negative actual Schur quadratic or a counterexample to Weil positivity.

## 4. Pay the rest of the complete infinite high residual—and report the failure honestly

RC328 already certified upper bounds on the true original source $P_{\ge250}Tx$, and RC327 independently bounded $P_{\ge250}CYx$ using the original native cross operator, including every infinite mode. RC329 subtracts the **known positive $n=250$ squared energies** from each original outside norm, and evaluates the new signed $n=250$ residual separately:

$$
\|R\|^2
= \|P_{\{244,246,248\}}R\|^2
  + |R_{250}|^2 + \|P_{\ge252}R\|^2.
$$

For the remaining infinite $n\ge252$ complement the certified (still conservative) triangle bound is applied, preserving all modes. The resulting full residual penalty upper is

$$
\boxed{
\mu_e^{-1}\|R\|^2_{\rm new\ split}
<0.000225261662.
}
$$

This is **slightly larger** than the earlier RC328 upper bound $0.000225252475$. RC329 **does not claim an improvement**. The valid stronger bound is retained by taking the minimum of both rigorously certified expressions.

The adverse signed mode cannot be made helpful by more accurate measurement of that same unchanged Ritz direction. Its source and trial action have demonstrably opposite signs.

## 5. A structural redirection for RC330

This result suggests that further progress requires **reoptimization of $Y$**, not merely tighter residual arithmetic on the existing three-mode response.

The most direct next move is to extend the **actual original finite high block** from $\{244,246,248\}$ to $\{244,246,248,250\}$, certify the real $C_{250,250}$ diagonal and the coupled $4\times4$ Sylvester minors, and construct a new four-coordinate rational Ritz trial. The newly certified source $b_{250}$ and original off-block matrix entries become direct inputs to that calculation.

Afterwards, the signed outside covariance must be continued across degrees $252,254,\ldots$ and the remaining infinite tail fully charged. Even a positive finite $4\times4$ high block and improved Ritz correction are only upper Schur witnesses unless the true full inverse/residual yields a **positive lower** bound on the complete low Schur block.

The remaining low dimensions, full rank-317 Schur positivity, Stage I, F4, Lean and RH are all **OPEN**.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc329_native_outside_covariance.py --output certificates/rpb108_rc329_native_outside_covariance.json
python scripts/validate_rpb108_rc329_native_outside_covariance.py --output certificates/rpb108_rc329_native_outside_covariance.json --replay
\`\`\`

The certificate pins eight upstream Git blobs and is conditional on the inherited RC313 identification of the completed original CC27 Weil operator. Actions replay confirms the arithmetic and internal source custody, **not independent mathematical peer review or a proof of the Riemann hypothesis**.
