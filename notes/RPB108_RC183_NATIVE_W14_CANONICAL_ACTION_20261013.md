# RC183: complete actual canonical action on native w14

Parent: RC182, `b807491342015b78fde263646f74439212714eac`.

RC183 constructs and materializes a complete canonical action carrier for the unchanged native w14 source. It evaluates a finite regular input prefix with all actual input and output tails paid, tightens the inherited endpoint trial by centering the analytic input tail, and preserves the entire negative-r correction. The five-source inverse response remains the next obligation.

## 1. Unchanged native source and historical endpoint coefficients

The source is w14=g+w_tail, where g is RC128's rational polynomial through degree 4094 and

\[
 (w_{tail})_n=\eta_n\sum_{k=0}^{14}\mu_k(\lambda/z_n)^k,
 \quad z_n=n(n+1),\quad\eta_n=\frac{2n+1}{z_n(H_n+s)},
 \quad\lambda=977132,
\]

on even n>=4096. The source retains its historical coefficient centers and exact actual-D analytic definition.

RC130's two finite endpoint columns are reconstructed with the original directed generator, and their combined coefficient digest reproduces exactly. The full historical action errors reproduce as well. The new carrier stores the w14 finite source coefficients and the historical Cg output coefficients through degree 8190. No historical endpoint or source data is overwritten.

## 2. Full actual regular action with a short finite input

Let q be the exact prefix of g through degree M=256. Its D support is disjoint from w14-q. With the full native Gram upper Gamma_w,upper and exact-prefix energy lower Gamma_q,lower,

\[
 \|w14-q\|_D^2\le\Gamma_{w,upper}-\Gamma_{q,lower}=T_{input}.
\]

This difference pays every omitted finite and analytic coefficient. It is not a finite-tail-only estimate. The diagonal D on the omitted support is at least H_258+s_lower. RC174 gives the actual regular high-mode factor phi_256, hence

\[
 \|D^{-1}R(w14-q)\|_D
 \le\sqrt{\frac{\phi_{256}^2T_{input}}
 {s_{lower}(H_{258}+s_{lower})}}.
\]

The exact finite polynomial q is evaluated using RC176/RC179's analytic kernel, Beta convolution, and closed polynomial/log Legendre moments. The kernel degree is 192 and the regular output degree is 768. Its analytic coefficient digest and complete infinite log-tail bounds are retained. The whole actual w14 regular error is the finite-q output error plus the full smoothed input-tail error.

\[
 \|D^{-1}Rw14-\widehat p_R\|_D
 <0.000058323696,
\]

\[
 \frac{\|D^{-1}Rw14-\widehat p_R\|_D}{\|w14\|_D}
 <0.000753268.
\]

The selected local relative norm budget is 0.001. Its certified ratio is below 0.753268. This closes the regular component contract, not a full canonical or inverse accuracy contract.

## 3. Same-source endpoint precision improvement

RC130's finite Qg trial approximates Cg with paid finite rounding and omitted-output errors, C=D^-1 h. The old full w14 action approximated Cw_tail by zero and paid its entire norm. RC183 instead uses

\[
 \widehat Cw14=Q_g+\tfrac12w_{tail}.
\]

The actual full-domain contraction 0<=C<=I gives

\[
 \|(C-I/2)w_{tail}\|_D\le\tfrac12\|w_{tail}\|_D.
\]

No projection commutation is needed. The inherited finite output errors are unchanged; the analytic input-tail contribution is halved. With E_round and E_output from RC130 and the full input-tail energy upper T_w,

\[
 \epsilon_{C,new}=\sqrt{E_{round}}+\sqrt{E_{output}}
                         +\tfrac12\sqrt{T_w}.
\]

| Same Cw14 source/action norm | Certified upper |
|---|---:|
| Historical RC130 endpoint error | 0.000097733461 |
| New centered endpoint error | 0.000067061959 |

The improvement factor is above 1.4573606. This is a comparable precision improvement: the operator, source, domain, and norm are unchanged, while the trial is improved. It is separate from the coverage gains in earlier inverse-family expansions.

## 4. Complete negative-r and canonical action carrier

For every finite g coefficient, -r g_n/(H_n+s) is enclosed and replaced by a rational coefficient center with a paid D-energy radius. On the analytic native tail, the exact coefficient is retained:

\[
 -\frac r{H_n+s}\eta_n
       \sum_{k=0}^{14}\mu_k(\lambda/z_n)^k,
 \qquad n\ge4096\text{ even}.
\]

There is no dropped negative-r input tail or substituted constant diagonal on that tail.

The complete canonical trial for M=D^-1 L=I+C+D^-1 R-rD^-1 is

\[
 \widehat Mw14=w14+Q_g+\tfrac12w_{tail}
   +\widehat p_{-rD^{-1}g}-rD^{-1}w_{tail}+\widehat p_R.
\]

The finite part has maximum degree 8190. Above that cutoff it equals (3/2-r/D_n) times the native w14 analytic tail. Every omitted endpoint output and regular input/output contribution is paid in the full error; the analytic source and negative-r terms remain explicitly present.

Endpoint, negative-r finite rounding, and regular errors may overlap. Their norm bounds add by the triangle inequality:

\[
 \|Mw14-\widehat Mw14\|_D<0.000125385655,
\]

\[
 \frac{\|Mw14-\widehat Mw14\|_D}{\|w14\|_D}
 <0.001619393.
\]

The companion `rpb108_rc183_materialized_w14_canonical_carrier.json` stores the finite source, historical endpoint polynomial, negative-r finite correction, regular polynomial, and native analytic moment data. Its full file SHA256 is bound by the main certificate. The native w14 meaning is unchanged.

## 5. Validation, dashboard, and next cursor

All seven inputs are hashed and cross-linked. Generation/replay reverse the historical endpoint input sums, analytic regular convolution, and finite correction traversal. Both certificates must reproduce exactly. The historical endpoint digest and old action errors are verified before the new midpoint improvement is used.

Run `scripts/validate_rpb108_rc183_w14_canonical_action.py` with `--replay`, `--output certificates/rpb108_rc183_w14_canonical_action.json`, `--carrier-output certificates/rpb108_rc183_materialized_w14_canonical_carrier.json`, and these checkpoint inputs in order: RC182 main inverse certificate, RC130, RC129, RC128, RC127, RC170, RC174. The actual RC130 basename is `rpb108_rc130_remaining_covariance.json`.

The dashboard records the new local regular component acceptance and the separate full canonical action accuracy. The four-source inverse result remains unchanged. No five-source inverse width or acceptance ratio is assigned before evaluating its mixed rows.

Next: extend the actual inverse response to the unchanged native w14 source, paying its nonorthogonal mixed source/action rows and full correlated residuals. The remaining native v10,z_b6,t10 directions still require explicit full canonical action and inverse coverage. Stage I original targets, original whole-aperture positivity, RH, F4, and Lean remain open/unclaimed.
