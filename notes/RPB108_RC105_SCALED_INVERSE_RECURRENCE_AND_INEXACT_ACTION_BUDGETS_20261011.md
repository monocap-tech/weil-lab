# RC105 — scaled inverse recurrence and inexact-action budgets

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.

RC105 makes RC103's complement inverse polynomial usable with certified inexact actions. It supplies an exact scaled recurrence, an error-propagation theorem allowing fully correlated step errors, and rational accuracy budgets for the original even and odd complement brackets. It performs no arithmetic operator actions and certifies no strong lower floor or lifted-response Gram.

## Inherited setting

Let H be the complete sufficient 1,250-feature head, E its canonical orthogonal complement, and W the six certified positive directions (three per parity). Write

\[
D=P_E A_Q P_E|_E,\quad B=P_H A_Q P_E,\quad R=P_E A_QW,\quad F=A_H-BD^{-1}B^*.
\]

RC103 supplies \(\alpha I\le D\le bI\), with \(\alpha=247/2500\), even \(b=2067533/500000\) and odd \(b=3239591/1000000\). Its actual source covariance enclosure is \(R^*R\le G\), and its correction enclosure is \(V=(g/\alpha^2)G\le\lambda L\), where L is the proved weak-block lower. These are common column Grams: all error inequalities below refer to the same weak-coordinate system, not unrelated scalar errors in six columns.

RC104 proves only *upper* restrictions on a positive strong floor: even at most approximately \(2.57011\times10^{-5}\), odd at most \(1.94550\times10^{-4}\). Neither upper ceiling is a proved positive lower. The smaller targets in this pass also remain hypothetical.

## An exact scaled inverse recurrence

Put

\[
Z=\frac{b+\alpha-2D}{b-\alpha},\qquad
c=\frac{b+\alpha}{b-\alpha}>1,\qquad t_k=T_k(c).
\]

The spectral bracket makes Z a selfadjoint contraction. Define

\[
Y_0=0,\qquad Y_1=\frac{2R}{(b-\alpha)t_1},
\]

\[
Y_{k+1}=2\frac{t_k}{t_{k+1}}ZY_k
-\frac{t_{k-1}}{t_{k+1}}Y_{k-1}
+\frac{4t_k}{(b-\alpha)t_{k+1}}R.
\]

Then \(Y_n=q_{n-1}(D)R\) for the RC103 inverse polynomial. To see this, let

\[
s_k(z)=\frac{T_k(c)-T_k(z)}{c-z}.
\]

This is a polynomial, with \(s_0=0,s_1=1\). Subtracting the two Chebyshev recurrences gives

\[
s_{k+1}(z)=2zs_k(z)-s_{k-1}(z)+2t_k.
\]

Since \(D=(b-\alpha)(cI-Z)/2\), the inverse polynomial applied to R is \(2s_n(Z)R/((b-\alpha)t_n)\), exactly the recurrence above. Thus evaluation does not require expanding the inverse polynomial into monomial coefficients. The recurrence coefficient of the Z action is below 2, and the backward coefficient is below 1.

## Correlated local errors have a rigorous bound

Let an implemented recurrence add total error \(E_j\) after step j, including its initial step. Each error is measured relative to the displayed exact recurrence on the *actual preceding iterates*. This definition includes errors from complement projection, operator actions, source representation, coefficients and arithmetic; it does not assume those errors are independent.

Multiplying the difference recurrence at step k by \(t_k\) gives the unscaled recurrence with forcing \(t_jE_j\). Its exact solution is

\[
\widehat Y_n-Y_n
=\sum_{j=1}^n\frac{t_j}{t_n}U_{n-j}(Z)E_j,
\]

where U is the Chebyshev polynomial of the second kind. On \([-1,1]\), \(|U_m|\le m+1\). For example, from the finite exponential-sum formula for \(U_m(\cos\theta)\), there are m+1 unit-modulus terms; the endpoint values follow by continuity. Spectral calculus therefore gives \(\|U_m(Z)\|\le m+1\).

If \(E_j^*E_j\le\eta_j^2G\), apply the triangle inequality to each weak coefficient vector v. It yields

\[
\mathrm{Gram}(\widehat Y_n-Y_n)\preceq H_\eta^2G,
\quad H_\eta=\sum_{j=1}^n(n-j+1)\frac{t_j}{t_n}\eta_j.
\]

This proof also handles singular G and adversarially correlated errors. With a uniform allowance \(\eta_j\le\eta\), set

\[
H_n=\sum_{j=1}^n(n-j+1)\frac{t_j}{t_n}.
\]

Since \(1\le t_j\le t_n\), \(H_n\le n(n+1)/2\). The actual exact rational sums in the reported budgets are much smaller: approximately 13.95 even and 11.31 odd.

The ideal residual satisfies \(\mathrm{Gram}(R-DY_n)\preceq\epsilon_n^2G\), where \(\epsilon_n=1/t_n\). Since \(\|D\|\le b\), the implemented residual has the common-Gram upper

\[
\boxed{\mathrm{Gram}(R-D\widehat Y_n)
\preceq(\epsilon_n+b\eta H_n)^2G.}
\]

A separate certified posterior residual can replace this bound and may be sharper.

## Reserved error budgets

For each conditional target beta, choose the smallest n satisfying

\[
\epsilon_n^2\lambda\le\beta/32,
\qquad \eta=\epsilon_n/(bH_n).
\]

Then the total residual is at most \(2\epsilon_n\) in the common source-Gram norm, so its transported cross correction is at most \(\beta L/8\), exactly RC103's reserved correction budget. The certificate verifies the preceding degree fails the *reserved ideal scalar enclosure*. This is not a lower bound on actual solver effort.

Rounded display values (acceptance uses exact rationals):

| Parity | Conditional beta | Steps n | H_n upper | Total local norm allowance eta |
|---|---:|---:|---:|---:|
| Even | RC104 upper ceiling, 2.57011e-5 | 38 | 13.94749 | 2.49395e-7 |
| Odd | RC104 upper ceiling, 1.94550e-4 | 28 | 11.30815 | 2.79212e-6 |
| Even | 1e-6 | 43 | 13.94782 | 5.24983e-8 |
| Odd | 1e-6 | 35 | 11.31022 | 2.36076e-7 |
| Even | 1e-9 | 54 | 13.94791 | 1.70346e-9 |
| Odd | 1e-9 | 45 | 11.31044 | 6.92574e-9 |
| Even | 1e-12 | 65 | 13.94792 | 5.52739e-11 |
| Odd | 1e-12 | 55 | 11.31045 | 2.03184e-10 |

Each allowance means \(E_j^*E_j\preceq\eta^2G\); it is not a raw entry tolerance or ordinary absolute norm threshold. If the only error at a recurrence step comes from its Z action, an action-error common norm factor \(\eta/2\) suffices because its multiplier is below 2. Additional errors must fit inside the same total allowance, with their correlations retained or paid by a triangle inequality. Accuracy of an approximate Z representation itself must be assessed on the actual current iterate.

If an actual strong floor \(F|_S\ge\beta I\) and the actual implemented lifted-response Gram

\[
\mathrm{Gram}(P_S A_Q(W-\widehat Y_n))\preceq\beta L/4
\]

are certified, RC103's exact residual identity gives corrected cross Gram at most \(3\beta L/4\) and positive Schur margin \(\beta L/4\). This is a conditional completion theorem, not its completed arithmetic certificate.

## Validation and scope

The validator binds the exact RC104 and RC103 input bytes by SHA-256. Rational checks include the reserved budgets and preceding-degree exclusions, the polynomial quotient versus scaled recurrence on a noncommuting two-dimensional D and R, signed inexact steps and their final residual Grams, and an endpoint control at \(Z=I\). In that endpoint control, identical local errors attain exactly \(\eta H_nR\), verifying the error amplification rather than just an overestimate of an unrelated matrix.

Independent replay uses the positive binomial expression for \(T_n(c)\), reverses the amplification sum, and evaluates the control polynomials by explicit powers rather than Horner evaluation. The operator error theorem is proved above; finite controls illustrate it and are not arithmetic source computations.

Reproduction in the repository:

```sh
python scripts/validate_rpb108_rc105_inexact_inverse_recurrence.py > /tmp/rc105.json
python scripts/validate_rpb108_rc105_inexact_inverse_recurrence.py --replay /tmp/rc105.json
```

Published artifacts are the validator, `certificates/rpb108_rc105_inexact_inverse_recurrence.json`, and this note. Local replay reports PASS.

The certified positive span remains six; the original nonpositive spectral dimension upper remains 1,244. The strong lower or a more refined mode-coverage argument, actual arithmetic lifts, and their six fused responses remain open. Whole-aperture positivity, RH and Global/F4 are not proved. RC105 resolves an implementation error-propagation obligation for the inverse route; it does not resolve those structural obligations.
