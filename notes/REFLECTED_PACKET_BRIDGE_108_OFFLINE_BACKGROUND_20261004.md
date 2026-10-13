# RPB108: actual off-line negative background

Base: research `d9458f042ae281dd7fa37bc49cf96c286e5a76e0`.

## Concrete same-vector formula

For a source graph vector f, set h to its actual physical representative and write
\[
F_h(z)=\int_{-a}^a h(x)e^{izx}\,dx,\quad
p_q=\tfrac12(F_h(\bar z_q)+F_h(z_q)),\quad
n_q=\tfrac12(F_h(\bar z_q)-F_h(z_q)).
\]
These are the normalized actual positive and negative coordinates. The factor 1/2 is the product of the pair normalization \(1/\sqrt2\) and the full-divisor normalization \(1/\sqrt2\). The window integral is a lawful compact evaluation; no arbitrary point value of an L2 Fourier representative is used.

For the actual finite selected set s, the background negative coordinate is zero when q belongs to s, and is n_q otherwise. Every coordinate comes from the unchanged physical/source graph vector. Analytic multiplicity copies remain in the squared-norm sums.

## Critical-line elimination (Lean proof)

If the actual point underlying q satisfies Re(rho)=1/2, its complex ordinate is real: \(\bar z_q=z_q\). The actual negative source and negative sample are therefore zero. This is a pointwise implication for each actual coordinate; no assertion that all zeros lie on the critical line is made.

Hence
\[
B_s f=0\iff
n_q=0\quad\text{for every unselected off-line copy }q.
\]
The five formal theorems give ordinate conjugation at a critical point, negative source/sample vanishing, the exact unselected normalized coordinate formula, and this zero-background equivalence.

## Exact remaining unit budget

The coefficient norm identity yields
\[
\|B_s f\|^2=\tfrac14\sum_{\substack{q\notin s\\\operatorname{Re}\rho_q\ne1/2}}
|F_h(\bar z_q)-F_h(z_q)|^2,\qquad
\|S_+f\|^2=\tfrac14\sum_q|F_h(\bar z_q)+F_h(z_q)|^2.
\]
These series converge on the actual source graph by its defining lp2 custody. Discarding the critical-line negative coordinates is lawful because every discarded summand is zero; it is not a tail truncation.

Thus the WD-T10 arithmetic obligation is exactly
\[
\sum_{\substack{q\notin s\\\operatorname{Re}\rho_q\ne1/2}}
|F_h(\bar z_q)-F_h(z_q)|^2
\le
\sum_q|F_h(\bar z_q)+F_h(z_q)|^2
\]
on the intended Green range. Kernel inclusion alone asks that vanishing of all plus samples force vanishing of these unselected off-line minus samples. The unit estimate is stronger.

Critical-line copies provide only nonnegative energy. Off-line copies may still have zero negative sample on an individual vector; the theorem does not infer a nonzero negative coordinate from being off line. No off-line zero is presumed to exist.

## Orbit accounting (analytic identity)

For an off-line conjugate-ordinate orbit {rho,1-conj(rho)} with common multiplicity m, write A=F_h(z), C=F_h(conj z). Let k be the number of selected raw copies across the two fibers, so 0<=k<=2m. Its background contribution is exactly
\[
\frac m2|A+C|^2-\frac{2m-k}{4}|A-C|^2.
\]
The two fibers have identical plus coordinates and opposite minus coordinates; their squared magnitudes agree. Selection of a single copy removes only one copy's negative energy. It does not remove the entire multiplicity fiber or partner orbit. A critical-line point is a fixed orbit and contributes m|F_h(z)|^2.

This bookkeeping identity identifies the arithmetic sign problem without treating repeated copies as independent observations. It is not a proof that any off-line orbit contribution is nonnegative or negative on the actual Green vectors.

## Independent input still missing

If every unselected point were critical, B_s would vanish and the zero contraction would close the background factor. That premise is not available and is not adopted. Likewise, source-mode independence does not compare plus and minus energy, and the negative scalar multiplier at zero does not produce a supported negative packet.

The next substantive task is to prove the displayed sum-minus/sum-plus comparison on actual Green vectors, or find a lawful finite packet violating it. An actual off-line paired evaluation estimate with an adequate summed budget could supply the former. No such summed budget or negative certificate is asserted here.

No new carrier is introduced. No retained-mode membership, full graph density, zero simplicity, spectral operator-domain membership or background positivity is assumed. Same-vector WD-T38 source/null attachment remains separate.

## Formalization boundary and validation

The five critical-line/source-coordinate lemmas are Lean certified. The full norm-series formulas and orbit regrouping above are analytic identities derived from the source graph definitions and existing norm identities; they are not newly Lean formalized in this module.

Lean 4.34.0; exact tested head `cb92c1b4dfca298cbc79d5b7d25598ea370236bf`. [Actions run 37236113125](https://github.com/monocap-tech/weil-lab/actions/runs/37236113125) / job `111535430775` passed isolated 9178/full 9205 build jobs. All five theorem audits depend exactly on `[propext, Classical.choice, Quot.sound]`; unfinished/project-axiom and sorryAx gates passed. Tested module and root fetched and matched byte-for-byte. Restored distinct-observation cache and saved `rpb108-actual-offline-background-verified-v1`. Norm-series and orbit regrouping are recorded analytic identities, not new Lean formalizations.

## Updated cursor/residue

At d9458f0, the actual negative background is isolated to unselected off-critical-line divisor copies. Five Lean lemmas prove critical ordinate conjugation, negative source/sample zero at critical points, exact normalized unselected coordinate formula, and B_s f=0 iff every unselected off-line negative sample vanishes. Actual normalized coordinates are half of the compact evaluation sum/difference at z and conj z. The exact remaining unit budget compares the summed off-line unselected evaluation differences to all evaluation sums, keeping all multiplicity copies and the same physical/source vector. Analytic orbit accounting gives m/2 |A+C|^2 - (2m-k)/4 |A-C|^2; selecting one copy removes only one copy's negative energy. Full series/orbit formulas are recorded analytic identities, not new Lean formalizations. No off-line zero existence, whole-background criticality, retained witness membership or positivity is assumed. Next substantive input is a same-vector actual Green-range sum-minus/sum-plus estimate with verified summed budget, or a lawful finite negative packet. Carrier refinements and finite independence do not establish that inequality. WD-T38 source/null attachment remains separate. FULL TRANSPORT CLOSED remains open; SOURCE stays off the critical path.
