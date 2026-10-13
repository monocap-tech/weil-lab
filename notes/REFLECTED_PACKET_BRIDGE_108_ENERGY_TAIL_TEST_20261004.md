# RPB108: quantitative interpolation energy-tail test

Base: research 4a6c605367feb8f8c5555cf2ae2b7ec3e0761844.

## Actual tail bound

Fix a>0 and a supplied actual off-line orbit with r>0 unselected raw copies. Let Lambda be a finite partner-closed set of actual zero points containing that orbit and every actual point of height at most 1. Low-height finiteness is supplied by the actual divisor counting results. Let w_Lambda be the unchanged finite actual Green graph packet constructed by finite interpolation, with physical coordinate h, target evaluations +/-1 and zero evaluations elsewhere in Lambda.

Define the raw-copy tail
\[
\eta_\Lambda=\sum_{q:\,\mathrm{point}(q)\notin\Lambda}
 (1+|\operatorname{Im}\rho_q|)^{-2},\qquad
C_a=8a e^a.
\]
Multiplicity copies are counted in eta. Distinct points, rather than copies, index the interpolation Gram matrix.

The existing Lean high-height sample bound in ActualZetaRawGreenSampling.lean states, on this same synthesis and gradient,
\[
|F_h(z_q)|^2\le C_a\|h'\|_2^2
 (1+|\operatorname{Im}\rho_q|)^{-2}
\]
when the height is at least 1. It follows from the endpoint-zero derivative identity and the strip bound |Im z_q|<=1/2. Partner sampling satisfies the same bound: partner height is identical and the actual conjugate ordinate is the partner ordinate.

For p_q=(F_h(bar z_q)+F_h(z_q))/2, the elementary inequality
\[
|p_q|^2\le (|F_h(\bar z_q)|^2+|F_h(z_q)|^2)/2
\]
therefore gives
\[
\|P_{\Lambda^c}w_\Lambda\|^2
 \le C_a\eta_\Lambda\|h'\|_2^2.
\]
Subtracting the nonnegative unselected minus-tail energy yields
\[
Q_{\mathrm{tail},\Lambda}(w_\Lambda)
 \le C_a\eta_\Lambda\|h'\|_2^2.
\]
The certified theorem neutralActualZetaDivisorQuadraticWeight_summable in ActualZetaDyadicSummability.lean makes eta finite and eta->0 along any increasing finite point exhaustion. This is an unconditional actual-divisor upper bound; no simplicity or positivity premise is used.

## Concrete sufficient negative test

The preceding finite-interpolation result gives exactly
\[
Q_{B,s}(w_\Lambda)=-r+Q_{\mathrm{tail},\Lambda}(w_\Lambda).
\]
Write H_Lambda for the positive Dirichlet-energy Gram matrix and t for the prescribed evaluation vector. Since c=H_Lambda^{-1}t,
\[
E_\Lambda=\mathcal E(h,h)=t^\ast H_\Lambda^{-1}t,\qquad
\|h'\|_2^2\le E_\Lambda.
\]
Consequently
\[
Q_{B,s}(w_\Lambda)
 \le -r+C_a\eta_\Lambda E_\Lambda.
\]
The strict, same-packet inequality
\[
\boxed{8a e^a\,\eta_\Lambda\,
 t^\ast H_\Lambda^{-1}t<r}
\]
is sufficient for a lawful finite actual negative certificate.

A sharper sufficient test uses the exact gradient energy c* J_Lambda c, where J_ij=int conjugate(g_i')g_j', in place of E_Lambda. Neither test is necessary, since discarding the negative tail loses favorable cancellation.

No actual off-line point or successful strict inequality is established here. Evaluating or bounding the product requires actual ordinate data and a rigorous weighted-tail bound as well as inverse-Gram control. A non-effective summability assertion alone does not provide an effective numerical certificate.

## Necessary conditioning growth under global domination

If WD-T10 global unit domination holds, then Q_B,s(w_Lambda)>=0. Hence
\[
r\le Q_{\mathrm{tail},\Lambda}(w_\Lambda)
 \le C_a\eta_\Lambda\|h'\|_2^2
 \le C_a\eta_\Lambda E_\Lambda.
\]
If eta_Lambda=0, this is impossible for r>0. Otherwise
\[
E_\Lambda\ge \|h'\|_2^2
 \ge \frac{r}{8a e^a\eta_\Lambda}.
\]
Thus, conditionally on global domination and the supplied unselected off-line orbit, interpolation energy diverges along every such finite exhaustion. This is a proved necessary growth rate in terms of the actual weighted tail, rather than a vague conditioning warning.

It does not prove that the product eta_Lambda E_Lambda tends to zero or is ever below r/C_a. The inverse-Gram energy may grow at least as fast as the reciprocal tail. This precisely explains why certified pointwise source summability does not settle the varying-packet sign.

## Custody and validation

All bounds are on the same physical h, its actual derivative, and the full positive/unselected negative coordinates of w_Lambda. The Dirichlet-energy estimate does not identify this energy with the source quadratic or create an endpoint-null witness.

This application and its energy-growth conclusion are analytic proofs, not new Lean formalizations. They use the existing certified high-height sample bound, quadratic-weight summability, finite actual interpolation and normalized coordinate dictionary. No Lean source/workflow changed; no new CI certification is claimed. Latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

No actual off-line existence, global background positivity, simplicity, full graph density, retained source/null membership or spectral operator-domain membership is assumed. WD-T38 remains independent. FULL TRANSPORT CLOSED is open.

## Cursor/residue

At 4a6c605, the certified high-height Green sampling bound yields a quantitative same-packet complementary positive-tail estimate: Q_tail <= ||P_tail w||^2 <= 8a exp(a) eta_Lambda ||h'||^2 <= 8a exp(a) eta_Lambda t* H_Lambda^-1 t. Lambda contains all actual points of height <=1 and the target off-line orbit; eta_Lambda is the full raw-copy quadratic height-weight tail. A strict bound 8a exp(a) eta_Lambda t* H_Lambda^-1 t < r is sufficient for an actual finite negative certificate, but no actual instance is established. If global unit domination holds and r>0, interpolation energies are at least r/(8a exp(a) eta_Lambda), hence diverge along a finite exhaustion. Certified summability gives eta->0, not a rate overcoming inverse-Gram growth. Next arithmetic test is this energy-tail product or a sharper signed tail estimate on a fixed packet. Analytic application, no new Lean source/workflow or CI claim. No actual off-line existence, background positivity, retained source/null attachment, density or operator-domain assumptions. WD-T38 is independent; FULL TRANSPORT CLOSED is open; SOURCE stays off the critical path.
