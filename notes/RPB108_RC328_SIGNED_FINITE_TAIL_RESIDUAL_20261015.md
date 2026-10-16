# RC328 — Signed 278-mode original Weil response and complete infinite residual refinement

**Parent:** merged RC327 at \`dcb33c606b704ba2ec93000c88c56ae340bda8a4\`.  
**Operator:** the unaugmented original CC27 signed Weil quadratic form on RC313's completed $D$-Riesz carrier.  
**Result:** a rigorous **upper and lower** signed combined high-source energy on the entire finite even sector $n=244,246,\ldots,798$, followed by a paid infinite $n\ge800$ tail; the resulting correct-sign full residual penalty is **44.0% smaller** than RC327's. The full $C^{-1}$, exact outside high covariance, positive $3\times3$ low Schur block and Stage I remain **OPEN**.

## 1. What RC327 was still losing

RC327 proved a much sharper complete **$C Y$ outside-high action**, but it bounded the original low source $Tx$ by summing independently certified norms of three high-source columns. This discards their *signed* cancellation.

Retain the exact rational low test direction from RC323,

$$
x=\frac3{25}v_0-\frac{23}{8}w_2+w_4,
$$

with $v_0$ the first $D$-normalized even Legendre coordinate and $w_2,w_4$ the RC320/321 endpoint-vanishing combinations. The original signed response satisfies

$$
Tx=\frac3{25}Tv_0-\frac{23}{8}Tw_2+Tw_4.
$$

Its squared energy is **not** the sum of the separate squared source energies; the mixed covariance can cancel substantially. This checkpoint measures that cancellation *directly on 278 signed output coordinates*, rather than inferring it from separately estimated source norms.

## 2. Exactly reconstruct and bound the finite signed response

RC328 reuses RC323's **independently implemented fixed-point outward rational Legendre recurrence** at $10^{520}$ decimal denominator, rather than trust a floating-point transform. For every even $n=244,246,\ldots,798$, it computes the three original signed prime translation coefficients and the exact canonical endpoint coefficients

$$
e_n^{(0)}=\frac{2n+1}{n(n+1)},\qquad
e_n^{(2)}=\frac{6(2n+1)}{n(n+1)(n-2)(n+3)},
$$

$$
e_n^{(4)}=\frac{14(2n+1)}{(n-4)(n+5)(n-2)(n+3)}.
$$

**All original prime and endpoint source amplitudes are combined with the signed low coefficients before squaring.** The different $D$-input square-root metric factors and each output's denominator $(2n+1)(H_n+s)$ are rigorously interval enclosed. Then the complete original centered finite energy is enclosed from **both sides**:

$$
\boxed{
4.605508452890088\times10^{-7}
<
\sum_{\substack{244\le n\le798\\n\text{ even}}}
|\langle v_n,Tx_{\rm center}\rangle_D|^2
<
4.605508452890090\times10^{-7}.
}
$$

The certificate stores the exact outward rational enclosure, including individual selected source amplitudes, and separately reports the energy contributed by degrees 244–510 and 512–798. The inherited RC323 *whole physical source* error pays the actual, noncentered prime logarithm and coefficients, the moving boundaries, RC46 analytic remainder and the even pole. It is not silently set to zero.

The rigorous actual original finite response therefore satisfies

$$
\boxed{\|P_{244\le n<800}Tx\|_D<0.000678638966.}
$$

## 3. Pay the actual infinite tail

The finite 278-mode computation does not itself enclose all infinitely many original high modes. To avoid extrapolating a finite tail, RC328 imports the independently verified complete $n\ge512$ original source Parseval upper envelopes:

* RC318: full $P_0$ original $D$-high $n\ge512$ squared energy;
* RC320: center infinite tail for the boundary-compatible $P_2-P_0$ direction, plus real prime translation and complete RC46/pole errors;
* RC321: center infinite tail for the boundary-compatible $P_4-P_2$ direction, plus the same independently paid source errors.

Every mode with $n\ge800$ is contained in these already certified $n\ge512$ tails. Each original low-column tail is multiplied by the **absolute value of its rational low coefficient**, and the result is charged via the triangle inequality (no unproved infinite signed tail cancellation):

$$
\boxed{\|P_{n\ge800}Tx\|_D<0.000804135419.}
$$

This envelope deliberately double-counts some output degrees 512–798 *inside the upper bound on the far tail*. That makes the result **conservative, not invalid**. The actual finite $244\le n<800$ sector and the true far $n\ge800$ sector are orthogonal, so their upper energies combine in **quadrature**:

$$
\boxed{\|Tx\|_{D,\mathrm{entire\ high}}<0.001052228406.}
$$

RC327 had only certified $0.001424099362$ from independent whole-column source norms.

## 4. Correctly propagate into the whole-space residual

RC326's native three-mode Ritz vector $Yx$ remains **unchanged**. RC327 had independently bounded its native original outside action,

$$
\|P_{\ge250}CYx\|_D<0.000054131166.
$$

RC328 imports this bound directly rather than substituting the earlier much larger global $\|N_0\|\|Yx\|$ product.

The three represented signed source coefficients $b_{244},b_{246},b_{248}$ are independently enclosed by the pinned RC325/326 certificates, and their **true lower energy** is removed by Parseval from the newly certified whole $Tx$ upper. The unrepresented signed response, still using a *triangle bound* between $Tx$ and $CYx$, is then combined orthogonally with RC326's exact represented three-mode residual. This gives

$$
\boxed{\|Tx-CYx\|_{D,\mathrm{entire\ infinite\ high}}<0.001105579368.}
$$

Using the true inherited original-even high coercivity floor $\mu_e>0$, the **negative-sign** RC314 residual term is rigorously bounded by

$$
\boxed{
\mu_e^{-1}\|Tx-CYx\|_D^2<0.000225252475.
}
$$

The previous bound from RC327 was $0.000402379011$. Therefore the **certified upper** on the residual penalty is reduced by more than $44\%$.

## 5. Precise frontier and limitations

The residual upper remains larger than what can be tolerated from the original nearly-null low-witness quadratic, and its negative Schur correction cannot establish positive $3\times3$ high-eliminated Schur form.

**In particular, this checkpoint directly measures signed covariance between the three LOW source columns inside the 278-mode representation, but it does NOT yet evaluate the unrepresented mixed covariance between $Tx$ and $CYx$:**

$$
\|R\|^2=\|Tx\|^2+\|CYx\|^2-
2\operatorname{Re}\langle Tx,CYx\rangle.
$$

Only the first source combination was improved, and the $CYx$ norm is independently constrained by RC327's native cross-operator certificate. The infinite tail remains rigorously paid rather than assumed to vanish.

**RC329** should compute the *joint signed covariance of $Tx$ with $CYx$ on common finite output coordinates $n=250,\ldots,798$*, then pay the real far-tail covariance using certified high operator/source norms. A principled finite head-to-infinite interface and more 3D low inputs remain open. No Stage I/F4/Lean/RH theorem is inferred.

## Reproduce

\`\`\`bash
python scripts/validate_rpb108_rc328_signed_finite_tail_residual.py --output certificates/rpb108_rc328_signed_finite_tail_residual.json
python scripts/validate_rpb108_rc328_signed_finite_tail_residual.py --output certificates/rpb108_rc328_signed_finite_tail_residual.json --replay
\`\`\`

The result is conditional on inherited RC313's completed original Weil operator identification. Exact rational replay and CI verification provide reproducibility, not independent mathematical peer review.
