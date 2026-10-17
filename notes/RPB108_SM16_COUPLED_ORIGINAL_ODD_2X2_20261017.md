# SM16 — coupled original signed physical odd 2×2 witness audit

**Active:** W-ODD-NEG OPEN. **Parent:** SM15's strict one-direction original signed odd Rayleigh lower >0.047879961.

SM16 tests strict positivity on the *entire* physical odd two-dimensional span of
\[
g_1(x)=\sin(2\pi(721/50)x)\operatorname{sinc}(2\pi x/100),\quad
g_2(x)=\sin(34\pi x)\operatorname{sinc}(2\pi x/100)
\]
on the original physical support \([-11/10,11/10]\).

For the true original signed operator \(Q_o=A_o-K_{\rm neg,o}-2|s\rangle\langle s|\) with \(s(x)=\sinh(x/2)\), form the physically supported symmetric matrix \(M_{ij}=\langle g_i,Q_og_j\rangle\). Acceptance requires a **rigorous exact-rational** lower on both diagonals and
\[
\underline M_{11}\underline M_{22}
-\max(|\underline M_{12}|,|\overline M_{12}|)^2>0.
\]
Merely proving both diagonals positive is not sufficient.

## Original positive frequency source response

Combine SM14's 13 disjoint whole-original signed-positive bands near 14.42 with 14 additional original signed-positive whole bands of radius \(1/100\) at centers 16.60, 16.65, 16.70, 16.75, 16.80, 16.85, 16.90, 16.95, 17.00, 17.05, 17.10, 17.15, 17.60, 17.65. Every new band's prescribed margin is certified at *every real frequency*, with eight exact rational original arch+seven-prime signed phase subdivisions. Frequency interiors are pairwise disjoint, so each Jensen source contributes genuinely unused original positive mass. The physical positive matrix uses **all 27 signed source vector outer products** and the scalar original \(\kappa\) physical Gram, retaining both cross entries with exact outward sinc errors.

## Every negative-frequency Fourier interaction

SI10/SM10's original 973 uncertain positive-frequency dyadic leaves in 107 clusters, and the full original sign-protected infinite exterior, are retained. Each physical Fourier vector \( (\langle g_1,h_\xi\rangle,\langle g_2,h_\xi\rangle) \) is bounded continuously across its leaf by the original SI18 sine Gram plus an analytically integrated derivative and sinc physical truncation error. Distant leaves retain the rigorous analytic sine-frequency-distance envelope. For strictly original-negative whole leaves, SM15's **second-order integrated** multiplier upper replaces the wasteful first-order pointwise envelope; on other leaves the global original signed cap remains. The code reports two entire-negative diagonal upper bounds and an actual **signed mixed interval**, never falsely orthogonalizing the two physical witnesses.

The odd pole contributes two rigorous diagonal upper bounds and a signed mixed magnitude upper via original SI18 \(\langle \sinh(x/2),\sin(2\pi cx)\rangle\) and Jensen sinc error. All terms appear in the two-by-two determinant.

The script reports either exact positive definiteness of this **specific 2D physical subspace** or an inconclusive rigorous interval diagnostic. It must never promote a failed determinant bound to positivity.

**Scope:** Even if SPD is proved, operator-wide W-ODD-NEG, SM10's full 890-source coupled carrier, the even/whole signed form, global original-zeta bridge, independent peer review and RH remain OPEN.

Replay: python scripts/validate_rpb108_sm16_coupled_original_odd_2x2.py


## Directed-rounding contract for 2×2 interval accumulators

All 27 original sign-positive source cross terms, and all 973 original negative-frequency leaf terms, are accumulated in rational interval bounds with fixed denominator \(10^{24}\), rounding every positive diagonal upper **up**, every positive diagonal lower **down**, every mixed interval lower **down** and upper **up** at each step. Per-step rounding has absolute error \(<10^{-24}\) and the accumulated errors are already included by the repeated outward rounding. This avoids explosive growth of exact rational denominators without treating any negative-frequency leaf or physical cross coupling as zero.

The separate already-merged SM15 exact 973-leaf replay is not redundantly recomputed inside the focused SM16 job; its strict one-direction certificate remains preserved in the canonical governance ledger. The SM16 test independently runs the full 973-leaf two-direction enclosure.
