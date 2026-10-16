# RC331 — Four-mode original high interface and complete residual recovery

**Parent:** merged RC330 \`447774a91c3898d317dc1383f8500ae6354f1bae\`.  
**Operator:** original CC27/RC313 signed Weil \(D\)-Riesz high block, \(B=11/10\).  
**Scope:** all four RC330 input degrees \(244,246,248,250\), every omitted even high output \(n\ge252\), including \(n\ge800\). The RC330 exact-rational high trial is unchanged.

## What RC330 left open

RC330 certified the actual signed four-coordinate positive high compression and a strictly larger Ritz gain, but its entire infinite residual estimate was built using the original global bound \(\|N_0\|<9.921\). Thus it gave the rather coarse original residual penalty \(<0.000983307\), larger than the independently certified earlier RC328 *three-vector* penalty. This was a change-of-vector issue, not a contradiction.

RC331 extends RC327's *native* off-block Hilbert–Schmidt/operator estimate to the new four-coordinate trial, with the first omitted degree now \(252\), not \(250\). Unlike a finite \(4\times4\) matrix argument, this bounds the original complete coupling into **infinitely many** outputs.

## Rigorous native cross decomposition

Let \(H=\operatorname{span}\{v_{244},v_{246},v_{248},v_{250}\}\), \(K=\overline{\operatorname{span}}\{v_{252},v_{254},\ldots\}\), and \(C\) denote the original signed high block. The script bounds the genuine cross operator

\[
\|P_KCP_H\|
\le \|P_K W_B P_H\|_{\mathrm{HS}}
+\frac{\|\mathcal P_{\rm prime}\|_{\rm phys}+\|\mathcal R\|_{\rm phys}}
{\sqrt{D_{244}D_{252}}}
+\|P_K\mathcal P_{\rm even}P_H\|.
\]

Here \(D_n=H_n+s\), with \(s\) enclosed by the pinned actual RC129 \(D\)-Gram. The diagonal/scalar portions vanish across disjoint Legendre degrees. No original signed prime interaction is discarded: its complete physical operator norm is paid, along with RC324 regular and even-pole components.

The endpoint squared Hilbert–Schmidt part is the **exact rational sum** over \(n=252,254,\ldots,798\), \(m\in H\):

\[
\sum_{n,m}
\frac{(2n+1)(2m+1)}
{(n-m)^2(n+m+1)^2 D_nD_m}.
\]

For \(n\ge800\), every integer \(n\ge800\) upper-bounds the even-only sum, and the monotone comparison

\[
\sum_{n=800}^{\infty}n^{-3}\le\frac1{2\cdot799^2}
\]

pays the **whole** far tail. The original seven-prime physical \(L^2\) bound and regular norm pay every remaining mode, while the even-pole rank-one term is charged through a four-input geometric Taylor envelope.

## Correct-sign complete residual, same four-mode vector

RC331 retains **RC330's new exact rational four-mode trial** \(Y_4x\) and RC328's independently certified complete original signed \(\|Tx\|\). The original four represented signed \(Tx\) source intervals from RC330 allow Parseval subtraction:

\[
\|P_K Tx\|^2\le \|Tx\|^2-\sum_{m\in H} b_{m,\min}^2.
\]

With RC330's existing certified represented residual \(\|P_H(Tx-CY_4x)\|\), the outside residual is paid by the genuine original native cross:

\[
\|Tx-CY_4x\|^2 \le
\|P_H(Tx-CY_4x)\|^2+
\bigl(\|P_KTx\|+\|P_KCP_H\|\|Y_4x\|\bigr)^2.
\]

The Python exact-rational validator requires and reverse-replays the following **strict caps** rather than storing unchecked decimal approximations:

| Original complete quantity | Required strict certificate |
|---|---:|
| Native high interface operator norm | \(<3/5\) |
| Whole omitted \(CY_4x\), \(n\ge252\) | \(<10^{-4}\) |
| Whole \(\|Tx-CY_4x\|\), represented and infinite omitted | \(<0.0012\) |
| Correct-sign RC314 residual penalty on the same \(Y_4\) | \(<0.00025\) |

This improves **RC330's bound on this same four-coordinate vector** by more than a factor of three. It does **not** assert improvement over RC328's stronger three-coordinate residual penalty: those bounds apply to *different Ritz vectors*. The four-coordinate Ritz gain is still only a Schur **upper** estimate along one original low witness.

## Exact limitation and next gate

**No full original signed covariance between the outside source \(Tx\) and the new high action \(CY_4x\) has yet been computed**; the prime cross is rigorously paid by an operator norm and the outside residual still uses a triangle inequality. Full positivity of the 278-mode high head, the 119 other even and 195 odd low coordinates, original three-dimensional Schur lower positivity, full \(C^{-1}\), Stage I, F4, Lean and RH remain **OPEN**.

**RC332:** evaluate actual original signed \(C_{252,m}\) for \(m=244,246,248,250\) and the independent native \(b_{252}\), measure that first omitted signed covariance, then continue toward the full \(252\ldots798\) source-sensitive covariance without discarding the \(800+\) tail.

## Replay

\`\`\`bash
python scripts/validate_rpb108_rc331_native_four_interface.py --output certificates/rpb108_rc331_native_four_interface.json --replay
\`\`\`

This arithmetic regression is conditional on the pinned inherited original-operator identifications and is **not** an independently peer-reviewed proof of RH or Stage I closure.
