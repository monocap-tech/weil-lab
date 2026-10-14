# RPB108 — RC235: actual frequency metric and coupled auxiliary response

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC234: `1426c6461d22ba2f570695fda5683801b352df64`. Branch: research/rpb108-route-consolidation.

RC235 certifies the actual frequency metric and the compressed auxiliary response on two explicit frequency test vectors. This advances the metric interface before adding trial directions. The below-one criterion is now tested in the correct frequency normalization on this two-dimensional span, rather than inferred from RC234's moment-source inverse numbers.

| Actual frequency test vector | Frequency squared-norm enclosure, outward | Auxiliary Rayleigh enclosure, outward |
|---|---|---|
| y0=Fhat P0, even | [2.1898173906, 2.2070209593] | [0.9968918272, 2.1670121727] |
| y1=Fhat P1, odd | [0.7263585508, 0.7383351857] | [0.9902476048, 5.3125892776] |

The compressed-response upper bound **5.312590 does not certify the threshold below one**. It is not a proof that the actual norm exceeds one: it is an upper enclosure. There is no negative original Weil witness or Stage I closure. The two-vector metric is certified; the full rank-639 frequency metric and full response bound remain open.

The pass also establishes a shared source/action residual cancellation. At t=1/lambda, the augmentation approximation error disappears entirely from the residual payment. The original-action error remains paid. This follows from an exact operator identity, not presumed statistical correlation or orthogonality.

## Correct test vectors, sources and metric

In each parity use the unchanged RC115 rational Fhat and its corresponding lambda and rational bandwidth. The full auxiliary space is the direct sum of the even and odd frequency carriers; lambda is applied separately in each block. Set

\[
 y_j=\widehat F P_j,\quad
 q_j=\widehat F^*\widehat F P_j,\quad
 R_j=D^{-1}q_j,\quad j=0,1.
\]

These are exact rational-kernel frequency polynomials specified by the existing lazy kernel recipe. Dense degree-2400 coefficient multiplication is not performed. Their actual canonical source is

\[
 \widehat X^*y_j=i^*\widehat F^*\widehat F P_j.
\]

This source is **different** from RC233–234's r_j=i*P_j. Those moment-source inverse upper numbers therefore cannot be reused as auxiliary Rayleigh quotients. The difference is now represented and paid with the already certified actual augmentation action.

The actual frequency Gram is

\[
 g_j=\|y_j\|_{\rm freq}^2
     =\langle P_j,\widehat F^*\widehat F P_j\rangle_2.
\]

RC234 materializes the actual band Gram G_jj, and RC232 bounds the full physical adjoint-product difference by epsilon. Thus

\[
 G_{jj,\rm lower}-\epsilon m_j
 \le g_j\le G_{jj,\rm upper}+\epsilon m_j,
 \quad m_j=2B/(2j+1).
\]

Both lower bounds are strictly positive. The rational-to-band error is paid in the frequency metric as well as in the source action. The frequency vectors and canonical sources are specified by exact operators; no approximate physical polynomial is silently identified with a canonical Riesz image.

Reflection makes the two frequency vectors orthogonal, including their symmetric unequal support bands. The augmented inverse also preserves parity, so their response pairing vanishes exactly. Consequently the Gram bounds and Rayleigh intervals cover all complex combinations of y0 and y1.

The operator being bounded on this span is the **orthogonal compression** P_Y Bhat P_Y, where Y=span{y0,y1}. No invariance of Y is claimed, and the bound is not an upper bound for Bhat on its complete frequency carrier.

## Shared source/action residual cancellation

Let N0 be the original Weil D-Riesz action, and A=D^-1 Fhat*Fhat. The same exact rational augmented operator satisfies

\[
 N=N_0+\lambda A,\qquad R_j=AP_j.
\]

For the polynomial response trial Y_j=tP_j, the exact residual is

\[
 \boxed{e_j=R_j-NY_j
       =(1-\lambda t)R_j-tN_0P_j.}
\]

RC231 supplies the original action center O_j with squared D-error E0,j. RC234 supplies a finite augmentation center lambda Rhat_j with complete squared error Eaug,j. The new source center is exactly the difference of the complete augmented and original action centers, divided by lambda. This uses their constructed component identity, rather than subtracting two independent error envelopes.

The residual center is (1-lambda t)Rhat_j-tO_j, and its error norm is at most

\[
 \delta_j(t)
 =\frac{|1-\lambda t|}{\lambda}\sqrt{E_{{\rm aug},j}}
   +|t|\sqrt{E_{0,j}}.
\]

At t=1/lambda the first term vanishes exactly and e_j=-N0 P_j/lambda. All original endpoint, prime, signed pole and omitted-output errors remain paid. The direct original formula from RC231 already canceled the canonical Poisson remainder; no new Poisson action is introduced.

For comparison, independently paying source and complete augmented-action errors would cost sqrt(Eaug)/lambda+t sqrt(Ecomplete). At the exact cancellation trial the certified shared fault uppers are approximately 0.004205086 even and 0.004711770 odd, compared with independent payments 0.029950750 and 0.027787745. The code verifies these strict reductions. The residual's nominal original-action part does not vanish, so this cancellation is not an exact inverse solve.

An exact control with a nonidentity D metric and noncommuting N0 and A verifies the source/action identity, cancellation at 1/lambda, and the complete signed response identity. It is a structural control, not an arithmetic original positivity proof.

## Signed response in the actual frequency normalization

Let Bhat=lambda Fhat N^-1 D^-1 Fhat*. The true auxiliary response of y_j is

\[
 b_j=\langle y_j,\widehat{\mathcal B}y_j\rangle_{\rm freq}
     =\lambda\langle R_j,N^{-1}R_j\rangle_D.
\]

The actual original test form is f_j=<P_j,N0 P_j>_D, with RC234's sharp positive interval. Since <R_j,P_j>_D=g_j and <P_j,NP_j>_D=f_j+lambda g_j, the signed center is

\[
 \lambda C_t=\lambda(2t-\lambda t^2)g_j
              -\lambda t^2 f_j.
\]

The inverse residual correction is added:

\[
 \boxed{b_j=\lambda C_t
       +\lambda\langle e_j,N^{-1}e_j\rangle_D.}
\]

RC232's actual global endpoints mu<=N<=nu imply correction bounds lambda ||e_j||_D^2/nu and lambda ||e_j||_D^2/mu. The full residual energy is enclosed by the same forward and reverse norm triangles as RC233, using actual lower/upper D weights. Upward and downward rational square roots are used in the appropriate direction; no finite residual is treated as the full residual.

Dividing by the actual frequency norm keeps the common g_j in the center and denominator:

\[
 \frac{b_j}{g_j}
 =\lambda(2t-\lambda t^2)
 -\lambda t^2\frac{f_j}{g_j}
 +\frac{\lambda\langle e_j,N^{-1}e_j\rangle_D}{g_j}.
\]

This correlated normalization is tighter and mathematically more precise than dividing independently rounded center intervals. The code uses the correct signs for the negative original form term and positive inverse correction. Positivity of N0 on the whole space is not assumed; only the two independently certified positive test forms enter these scalar bounds.

The trial candidates are the exact rationals k/(1000 lambda), k=950,...,1050, together with zero and 1/lambda. Bounds are chosen by exact rational comparison with deterministic ties. This is a finite validated search, not a global optimality claim or an iterative inverse computation.

## Scope of the resulting norm bounds

The actual positive frequency operator has a two-vector compressed norm upper at most 5.312590. The even and odd directional upper bounds are 2.167013 and 5.312590, both above one. Those upper bounds do not certify failure of positivity or prove the actual response exceeds one.

The directional lower bound gives a genuine lower bound on the **full** auxiliary norm:

\[
 \|\widehat{\mathcal B}\|\ge0.9968918272.
\]

If the full norm is below one, its gap is consequently at most about 0.003108173. This is a necessary margin constraint, not an upper estimate of the full norm, proof of convergence to one, or assertion that the remaining bound is nearly complete. The full norm could still exceed one; this pass does not decide it.

The chosen augmentation's exact rank remains 639. Two frequency vectors cannot exhaust its full range. A full-range operator bound or a reduced representation with paid discarded range remains required; no count of mandatory separate solves is asserted. RC228's accepted canonical inverse width is preserved and is not transferred to the different augmented operator or auxiliary metric.

## Reproduction and remaining work

Generation checks every input Git blob pin and uses exact rational acceptance. Replay reverses input and residual accumulation order and reproduces the full certificate. The actual frequency Gram, coupled residual, signed response correction, metric normalization and noncommuting control are all checked.

```bash
python scripts/validate_rpb108_rc235_frequency_metric_response.py --output certificates/rpb108_rc235_frequency_metric_response.json
python scripts/validate_rpb108_rc235_frequency_metric_response.py --output certificates/rpb108_rc235_frequency_metric_response.json --replay
```

Publication adds only the note, validator and certificate, with an expected-head non-force update. Remote comparison/tree readback verifies preservation of existing blobs. Conflict checks cover the additions, not all historical content.

The next focused work is tighter original-action residuals and richer response trials for these actual frequency sources, then a paid extension beyond the two-vector span. The full auxiliary response upper below one and Stage I assembly remain open. No original whole-space positivity, F4, Lean or RH conclusion is made.
