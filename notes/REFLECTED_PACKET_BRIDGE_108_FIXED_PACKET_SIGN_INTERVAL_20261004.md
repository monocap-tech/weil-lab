# RPB108: fixed-packet signed cutoff intervals

Base: research 461001d9d53110be19262975d9908bc98a40d68e.

## Theorem

Fix a>0, any lawful finite actual Green graph packet w, its unchanged physical coordinate h, and its unchanged raw-copy selection s. The packet need not be an interpolation packet. Let q range over all actual divisor copies and put
\[
p_q=(F_h(\bar z_q)+F_h(z_q))/2,\quad
n_q=(F_h(\bar z_q)-F_h(z_q))/2,\quad
d_q=|p_q|^2-\mathbf1_{q\notin s}|n_q|^2.
\]
The full background is Q_B,s(w)=sum_q d_q.

Use the certified dyadic partition b(q)=floor(log_2(floor(abs(Im rho_q))+1)). Define
\[
Q_N(w)=\sum_{q:\,b(q)<N}d_q,\qquad N\ge1.
\]
These finite raw-copy prefixes include all low-height points and are partner invariant. The certified theorem neutralActualZetaDivisorDyadicBand_card_bound supplies an A>0 such that band n has at most A(n+2)2^n copies.

Then
\[
\boxed{|Q_{B,s}(w)-Q_N(w)|
 \le\varepsilon_N(w)
 =8ae^a\|h'\|_2^2\,A(2N+6)2^{-N}.}
\]
This is a two-sided signed error estimate on one fixed packet. No background positivity is assumed.

## Proof

Write u=F_h(bar z_q) and v=F_h(z_q). The parallelogram identity gives
\[
|p_q|^2+|n_q|^2=(|u|^2+|v|^2)/2.
\]
Whether q is selected or unselected,
\[
|d_q|\le |p_q|^2+|n_q|^2.
\]
For tail bands n>=N>=1, height >=2^n-1>=1. The certified high-height Green sample estimate and partner symmetry therefore give
\[
|d_q|\le 8ae^a\|h'\|_2^2(1+|\operatorname{Im}\rho_q|)^{-2}.
\]
The weight in band n is at most 2^{-2n}; multiplying by the certified band count bounds its total by A(n+2)2^{-n}. Finally
\[
\sum_{n=N}^{\infty}(n+2)2^{-n}
 = (2N+6)2^{-N}.
\]
For example this follows by putting n=N+j, using sum_j 2^-j=2 and sum_j j 2^-j=2. Absolute summability permits subtraction of the finite prefix and bounds the absolute tail by the displayed epsilon. Both partner samples, the gradient and selected-copy indicator belong to w throughout.

The same estimate is uniform over lawful finite packets with a common derivative norm bound. No such uniform bound was established for the earlier varying interpolation family.

## Complete finite sign tests for a fixed strict sign

The certified enclosure is
\[
Q_N(w)-\varepsilon_N(w)\le Q_{B,s}(w)
 \le Q_N(w)+\varepsilon_N(w).
\]
Thus Q_N+epsilon_N<0 certifies a finite actual negative packet. Q_N-epsilon_N>0 certifies strict positivity on this packet only; it does not establish global positivity.

Since epsilon_N->0 and Q_N->Q_B,s for fixed w:
- If Q_B,s(w)<0, some finite N has Q_N+epsilon_N<0.
- If Q_B,s(w)>0, some finite N has Q_N-epsilon_N>0.
- If Q_B,s(w)=0, neither strict test can succeed.

For the first implication, choose epsilon_N < -Q_B,s(w)/2; the upper endpoint is at most Q_B,s(w)+2epsilon_N<0. The second is analogous. This proves completeness for strict signs, not numerical termination at nullity.

With interval-evaluated finite sums [L_N,U_N] and a rigorous tail upper bound epsilonHat_N, the sufficient tests are U_N+epsilonHat_N<0 and L_N-epsilonHat_N>0. Eventual detection additionally requires interval errors tending to zero and certified finite zero data. The abstract theorem does not supply these computational inputs.

## Concrete next arithmetic work

Keep the original two-column packet from the pairwise construction fixed. Its coefficients and derivative energy then remain fixed while N grows. Inspect all actual zeros in the finite prefix, retaining every multiplicity copy and its selection, and compute the signed contribution including zeros outside the target orbit. Do not re-interpolate to zero the newly inspected samples.

The earlier orbit formula Q=-r+Q_rest still holds. The present cutoff interval certifies Q_rest<r if the complete upper endpoint is negative. It does not presume a deficit, and positive compensation may persist.

The repo's dyadic count theorem supplies existence of A, not a certified numerical value in this record. A reviewable numerical certificate additionally needs an explicit verified A, complete verified prefix data (including zero-free exclusions and multiplicities), and rigorous evaluation of the fixed packet and its derivative energy. No numerical certificate or actual off-line orbit has been produced here.

## Validation and limits

This cutoff theorem, closed-form tail and strict-sign completeness are analytic proofs applying existing certified Lean sampling/count results. No Lean source/workflow changed; no new CI claim. Latest certified Lean head remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

No actual off-line existence, simplicity, full graph density, operator-domain membership, retained source/null attachment or background positivity is assumed. No endpoint-null or WD-T38 witness is created. FULL TRANSPORT CLOSED remains open.

## Cursor/residue

At 461001d, a fixed-packet two-sided signed cutoff theorem is proved analytically from certified high-height sampling and dyadic actual-divisor counts. For raw-copy dyadic prefix n<N (N>=1), |Q_B,s(w)-Q_N(w)| <= epsilon_N(w)=8a exp(a)||h'||^2 A(2N+6)2^-N, where the certified dyadic count supplies some A>0. The same unchanged finite Green packet is used at every cutoff. Any strictly negative or strictly positive fixed-packet sign is eventually certified by the corresponding finite prefix interval; zero sign need not terminate. No actual signed prefix, off-line orbit or numerical A has been certified here; effectiveness needs a certified A, complete finite actual zero data and rigorous interval evaluation. This avoids inverse-Gram growth from changing interpolation packets and identifies the next arithmetic computation: use the original two-column packet, evaluate finite signed samples, and bound the remaining tail. New theorem analytic, Lean/workflow unchanged. No density, simplicity, retained source/null membership, operator-domain or background positivity assumed. WD-T38 remains independent and FULL TRANSPORT CLOSED is open; SOURCE stays off the critical path.
