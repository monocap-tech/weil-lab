# RC315 — Actual original signed Weil low-mode diagonals

Parent: RC314 merged at f63b5a6e85edb6d2fedf111a5a9f133db3c05c3e.
Standing: original signed native low-sector necessary test, not full Schur. Stage I, F4 and RH OPEN.

## Operator, physical normalization, and parity

Let B=11/10, R=2B, u_n(x)=sqrt((2n+1)/(2B)) P_n(x/B). Original CC27 form per RC312–314:

\[
Q=J+W_B+c_R I-K_{\rm reg}+K_{\rm prime}+K_{\rm pole},\quad
c_R=-\gamma-\log(2\pi R),\quad
W_B=\log2-\tfrac12\log(1-(x/B)^2).
\]

This is the original signed form, NOT the positive augmented/source auxiliary. The harmonic form has J-diagonals 0 and 1, and the W_B-diagonals are 1 and 4/3 for u_0,u_1 respectively.

The actual zero-extended autocorrelations at shift ell are

\[
C_{00}(\ell)=1-\ell/(2B),\quad
C_{11}(\ell)=1-3\ell/(2B)+\ell^3/(4B^3).
\]

The native prime contribution is minus twice the sum of (log p)/sqrt(n) times these correlations at ell=log n, n in {2,3,4,5,7,8,9}; p is n's base prime. No wrapping and no doubled summand.

The signed rank-two pole contributes

\[
\langle u_0,K_{\rm pole}u_0\rangle=\frac{16}{B}\sinh^2(B/2),\qquad
\langle u_1,K_{\rm pole}u_1\rangle=
-\frac{3}{B}\left(4\cosh(B/2)-8\sinh(B/2)/B\right)^2.
\]

The RC46 regular convolution is exactly integrated as 2 integral_0^R of j_reg(t) C_jj(t) dt using the 193 rational Taylor coefficients and the RC46 uniform remainder bound. The error is paid by at most 2R times that bound because abs(C_jj(t))<=1.

## Actual signed native two-mode witness

Exact outward rational enclosures use Machin pi, Euler harmonic-gamma bounds, atanh logs, certified integer-square-root intervals, and positive hyperbolic Taylor tails.

\[
\boxed{\langle u_0,Qu_0\rangle\approx0.04025418>0,\qquad
\langle u_1,Qu_1\rangle\approx0.13238566>0.}
\]

The off-diagonal u_0,u_1 entry vanishes by reflection parity. Thus the original signed 2-by-2 physical compression is strictly positive. This sharpens RC46's much wider original low-mode enclosure that included zero.

**Limits:** Neither the rank-301 nor the buffered rank-317 original principal block has been certified positive; the signed high response Y and its residual Gram are entirely unevaluated. Low principal positivity also cannot bypass the SUBTRACTED Schur correction. Stage I, F4, RH, and full Lean formalization remain OPEN.

## Next front

Construct original signed high response Y for rank301/rank317, compute T and CY and signed residual R=T-CY with complete tail errors in the D-metric, and test

\[
S=B-T^*Y-Y^*T+Y^*CY-R^*C^{-1}R
\succeq B-T^*Y-Y^*T+Y^*CY-\mu^{-1}R^*R.
\]

The finite Schur positivity witness, NOT these two low diagonals, would close the full original Weil positivity gate. Separate null/zero-divisor synthesis obligations would still require examination.

Reproduce with both standard --output and --replay invocations of scripts/validate_rpb108_rc315_low_mode_sign.py, writing certificates/rpb108_rc315_low_mode_sign.json. The script pins RC46, RC313, RC314 Git blobs and uses rational arithmetic; it is not independent peer review.
