# RPB108: sharp collar-majorant ceiling and regularity obstruction

Base: research cf98cc77fc7405202e34bc915b50d671aa1a2230.

## What is being bounded

The actual shrinking-collar theorem proves, for an endpoint weak-null vector and every sufficiently small delta,
\[
M_R\le \|h\|_2^2
\left[
 \frac{A}{L_R^2\log(1/\delta)^2}
 +\frac{B\sqrt R}{L_R}e^{-R\delta^2/16}
 +E_R
\right],
\tag{1}
\]
where A,B are fixed positive finite constants, L_R=log R-C'_a and E_R=O((1+log R)e^(-R/4)/L_R). Constants can be enlarged to make A,B strictly positive.

The sharp result here is
\[
\inf_{0<\delta<\delta_0}
\left[
 \frac{A}{L_R^2\log(1/\delta)^2}
 +\frac{B\sqrt R}{L_R}e^{-R\delta^2/16}
\right]
\asymp(\log R)^{-4}
\quad(R\to\infty),
\tag{2}
\]
for any fixed 0<delta0<1.

Thus changing the collar schedule cannot improve the asymptotic order of this existing upper-bound envelope. This is not a lower bound on M_R or a claim that its actual decay is sharp.

## Terminology before use

**Collar majorant:** the bracketed upper-bound expression in (1), after the actual residual and coercivity estimates have been proved.

**Bound-optimization ceiling:** an asymptotic lower bound on the infimum of that majorant over allowable collar widths. It limits what these estimates prove, not what the actual endpoint mode might do.

**Uncontrolled smooth regularity:** smoothness or finiteness of all logarithmic moments without quantitative growth control of the corresponding constants. It is distinct from analytic regularity.

## Proof of the sharp optimization ceiling

For large R, 0<L_R<=log R and L_R>=(log R)/2.

If delta>=1/R, then log(1/delta)<=log R, and the first term is at least
\[
\frac{A}{(\log R)^4}.
\]
If delta<1/R, then R delta^2<1/R, and the second term is at least
\[
\frac{B\sqrt R}{\log R}e^{-1/(16R)}.
\]
For sufficiently large R this also exceeds a positive constant times (log R)^(-4). This proves the lower bound in (2) for every collar schedule, including schedules depending irregularly on R.

For the matching upper bound, choose delta=R^(-1/4), which is eventually below delta0. The first term is
\[
\frac{16A}{L_R^2(\log R)^2}
 =O((\log R)^{-4}),
\]
and the second is
\[
\frac{B\sqrt R}{L_R}e^{-\sqrt R/16}
 =o((\log R)^{-4}).
\]
This proves (2). The independent E_R term is exponentially smaller and cannot alter the leading order.

The proof does not assert that the pointwise action or residual has a matching lower bound. A stronger inequality using signed cancellation or different endpoint information might improve on (1); it would be new input, not optimization of the same envelope.

## Any fixed logarithmic power has the same limitation

The same elementary proof applies to an envelope
\[
\frac{A}{L_R^2\log(1/\delta)^{2p}}
+\frac{B\sqrt R}{L_R}e^{-R\delta^2/16},
\qquad 0<p<\infty.
\]
Its optimized order is (log R)^(-2p-2). This is a mathematical statement about such an envelope; only p=1 has been obtained from the actual residual in the preceding theorem.

Consequently proving another finite logarithmic collar power would improve the logarithmic exponent but would not, by itself, activate the one-sided exponential zero theorem. No iteration to arbitrary p or uniform control as p grows is asserted.

## A concrete regularity obstruction

Choose the nonzero compact smooth function
\[
h_0(x)=
\begin{cases}
\exp(-1/(1-x^2)),&|x|<1,\\
0,&|x|\ge1.
\end{cases}
\]
Repeated differentiation inside the interval gives rational powers of 1-x^2 multiplied by the exponential; every derivative tends to zero at the endpoints. Thus h0 is compact smooth and nonzero.

Its Fourier transform is rapidly decreasing, by integration by parts. It has every logarithmic Fourier moment:
\[
\int w(\xi)^k|\widehat h_0(\xi)|^2d\xi<\infty
\quad(k\ge0).
\]
Let M_R(h0) use the same exact moving-Gaussian multiplier as the actual project.

On |xi|<R/(4pi), beta_R<=exp(-R/4). On the complement, rapid Fourier decrease gives, for every N,
\[
\int_{|\xi|\ge R/(4\pi)}|\widehat h_0(\xi)|^2d\xi
 \le C_N R^{-N}.
\]
Therefore
\[
M_R(h_0)\le e^{-R/4}\|h_0\|_2^2+C_N R^{-N},
\]
and hence M_R(h0)=O_N(R^(-N)) for every finite N.

Nevertheless h0!=0, so the already proved one-sided Gaussian theorem rules out an eventual bound M_R(h0)<=C exp(-delta R) for any delta>0. Constants C_N cannot be optimized over N without a proved quantitative growth law.

This example is not claimed to be an endpoint weak-null vector, nor to satisfy the native endpoint equation. It certifies only that compact smoothness, all logarithmic moments and every polynomial Gaussian rate do not alone imply the exponential condition or zero. Any exclusion theorem for actual endpoint modes must use their additional native structure.

## Consequence for the current frontier

The actual residual exists and is regular enough for the near/far estimates. The current collar schedule is already optimal in asymptotic order for those estimates. Another choice of delta cannot close the missing exponential step.

More regularity can remain useful, but a finite logarithmic improvement or uncontrolled all-orders smoothness must not be presented as exponential control. Additional actual endpoint information must improve the inequality itself, with its quantitative constants.

Candidate forms of genuinely new input include a signed collar-cancellation theorem, an analytic bound with controlled constants, or an exclusion argument independent of Gaussian exponential decay. None is proved in this note, and no claim is made that these are the only possible routes.

This is a precise limitation of the existing argument, not proof that endpoint null exclusion is impossible. No actual endpoint, global unit domination or RH conclusion is asserted. FULL TRANSPORT CLOSED remains open.

## Validation and cursor

Analytic proof by a two-case optimization estimate and a direct compact smooth Fourier example, using the already proved one-sided Gaussian theorem. No new external input, Lean source/workflow change or CI result. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf; Actions run 37236113125/job 111535430775.

At cf98cc7, the actual near/far Gaussian inequality has a sharp bound-optimization ceiling. For fixed positive coefficients and L_R=log R-C'_a, the infimum over 0<delta<delta0 of A/(L_R^2 log(1/delta)^2)+B sqrt(R)/L_R exp(-R delta^2/16) is comparable to (log R)^(-4). If delta>=1/R the near term has that floor; if delta<1/R the separated-tail envelope is large. The proved choice delta=R^(-1/4) attains the matching order. This is a ceiling on the existing majorant, not a lower bound on actual M_R. An explicit nonzero compact smooth bump has every logarithmic Fourier moment and M_R=O_N(R^(-N)) for every N, yet no eventual exponential Gaussian decay by the proved one-sided theorem. It is not an endpoint-null example. Thus neither optimizing the current collar nor finite-power/logarithmic or unrestricted C-infinity regularity alone supplies null exclusion. The independent next input must exploit additional actual endpoint structure, such as signed collar cancellation, quantitative analytic control, or a different exclusion argument. No such input, actual endpoint existence, RH conclusion or new Lean/CI result is asserted. FULL TRANSPORT CLOSED remains open.
