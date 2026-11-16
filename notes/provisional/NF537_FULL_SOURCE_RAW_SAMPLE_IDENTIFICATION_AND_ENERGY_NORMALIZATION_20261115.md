# NF537 — Raw true-zero samples to complete P/N graph and the full-graph quadratic identity

**November 15, 2026 PT. Draft PR #565. Source graph preservation: exact; new Lean modules compiler status: PENDING.** The original U400 SHA256 remains `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`. No original 400-source source coefficient replay; the original 242 selected moments and all actual zero multiplicities/copies are unchanged.

## I. Full raw-sample to source-graph admission, with no Green density

Let \(\phi=\mathrm{neutralLogPhysical}(f)\) for an actual \(f\in\mathrm{NeutralLogHilbertCarrier}(a)\), and let \(D_\zeta=\coprod_\rho\mathrm{Fin}(m_\rho)\) be the actual full divisor. Define
\[
 A_q=F_\phi(\overline{z_q}),\qquad B_q=F_\phi(z_q),\qquad
 P_q=\frac{A_q+B_q}{\sqrt2},\quad
 N_q=\frac{A_q-B_q}{\sqrt2}.
\]
These are precisely the *existing* `neutralLogPositivePairSource_inner` and `neutralLogNegativePairSource_inner` identities, with the full original multiplicity coordinate.

If \(A,B\in\ell^2(D_\zeta)\), then \(P,N\in\ell^2(D_\zeta)\), because \(\ell^2\) is closed under scalar multiplication and addition/subtraction. Therefore \((f,P,N)\) is an element of the EXISTING closed complete source graph. Its physical coordinate is exactly \(f\). **No Green span, approximation, arbitrary background choice or separate zero-density estimate is involved.**

New target `ActualZetaRawSamplesToFullSourceGraph.lean` formalizes this via the authentic `lp G 2` space and `lp.hasSum_norm`, and constructs the full source-domain element from NF536's generic P/N lift. A second theorem composes the imported literal EF, real-odd frequency symmetry and raw-to-P/N argument. Its obligations **are not hidden**: true C² correlation, the actual real-odd Fourier identity, and \(f\) already in the logarithmic carrier. All new modules remain UNCOMPILED until the focused run accepts them.

## II. A new complete-source quadratic identity (rigorous algebra, Lean formalization OPEN)

There is a stronger point: on **EVERY** element \(g=(f,P,N)\) of the authentic full source graph, not merely Green lifts or real-odd tests, the two actual raw sample sequences are AUTOMATICALLY square summable. The exact sampling equations imply
\[
 A_q=\frac{P_q+N_q}{\sqrt2},\qquad
 B_q=\frac{P_q-N_q}{\sqrt2}.
\]
Since \(P,N\in\ell^2\) by definition of the graph, both \(A,B\in\ell^2\). Thus the mixed raw product series converges absolutely by Cauchy–Schwarz.

Careful *double normalization* is essential: the raw sources already carry a factor \(1/\sqrt2\) and the source quadratic applies a further factor \(1/\sqrt2\) to each source vector, because the authentic multiplicity-preserving divisor includes partner copies twice. With \(Q(g)=\frac12(\|P\|_2^2-\|N\|_2^2)\), the polarization identity gives
\[
\begin{aligned}
\|P\|_2^2-\|N\|_2^2
&=\frac12\sum_{q\in D_\zeta}
  (|A_q+B_q|^2-|A_q-B_q|^2)\\
&=2\operatorname{Re}\sum_{q\in D_\zeta}\overline{A_q}B_q.
\end{aligned}
\]
Therefore
\[
\boxed{
 Q(g)=\operatorname{Re}\sum_{q\in D_\zeta}
  \overline{F_\phi(\overline{z_q})}F_\phi(z_q)
 }\qquad(g\in\text{FULL ACTUAL SOURCE GRAPH}).
\]
This is a **general algebraic identity** based only on the existing source-graph definition; it is NOT a Green-only comparison and does not assume RH. For any graph vector \(g\) whose genuine physical autocorrelation \(C_{\phi,\phi}\) is \(C^2\), the imported literal EF then implies analytically
\[
\boxed{Q(g)=\operatorname{Re}\left[\operatorname{Zeta23.EF.literatureRHS}(C_{\phi,\phi})\right]}.
\]
The explicit formula preserves both poles, the actual arithmetic prime sum and complete archimedean gamma term.

**Formal acceptance distinction:** the algebra above is a complete mathematical derivation; the corresponding **universal Lean graph-to-zero-sum equality has NOT yet been compiled**. The earlier `neutralActualZetaGreenSourceQuadratic_eq_zeroForm` remains Green-specific. The NF537 new `ActualZetaRawPairNormalizedEnergy.lean` isolates and formalizes the central scalar/Hilbert identity
\[
\boxed{\|c(c(A+B))\|^2-\|c(c(A-B))\|^2=\operatorname{Re}\langle A,B\rangle},\quad c=1/\sqrt2.
\]
This theorem source is in GitHub with a new focused Lake build but its compilation is **PENDING**. A later theorem must combine it with the generic graph sampling equations and `lp.inner_eq_tsum` to certify the full universal identity in Lean. Do not claim this bridge source-certified until then.

## III. Rechecked exact arithmetic

NF537 locally reran the unchanged NF526, NF527, NF528 exact-rational scripts: all PASS. NF526 isolates *only* the true prime-power \(n=9\) geometrically in the original two collars; NF527 obtains the strict sufficient lower margin \(Q(f)>\frac1{10}\|f\|_2^2\) for the genuine supported smooth tests by gamma gain \(133/250\), prime loss \(<2/5\) and pole loss \(<4/125\), under its stated analytic original-test and source-identity hypotheses. NF528 again checks exact two-source partner-copy normalization in 10 symbolic rational tests. These replays DO NOT recompute NF494 U400 and DO NOT create a Lean proof of true digamma coercivity.

Local receipts for this NF: `nf537_replay_nf526.json`, `nf537_replay_nf527.json`, `nf537_replay_nf528.json` (stored outside GitHub in the conversation sandbox).

## IV. Strict acceptance ledger

- **NF529:** closed full-source quadratic continuity/inequality-transfer, Lean PASS.
- **NF532:** generic true-divisor physical correlation EF with C² + summability, Lean PASS.
- **NF533:** redundant summability hypothesis elimination, original CI FAILED at index-type conversion; NF535 committed the proper exact `Equiv.summable_iff` repair. NO later PASS yet.
- **NF534:** a.e.-invariant physical convolution C², Lean proof candidate, CI unresolved.
- **NF535:** real original-collar smooth C² to exact physical L² a.e. lift, Lean proof candidate, CI unresolved.
- **NF536:** original real-odd EF implies actual full divisor raw ℓ²; generic full P/N source lift from ℓ², Lean candidates, CI unresolved.
- **NF537:** raw ℓ² -> full P/N ℓ² and real-odd smooth-log graph entry; two-sqrt2 Hilbert energy identity, Lean candidates, CI unresolved.
- **Full graph identity \(Q=\operatorname{Re}\sum\overline{A}B\):** analytically proved by the exact 2×2 source algebra; universal Lean graph theorem OPEN.
- **Original smooth test in logarithmic carrier:** for compact C∞ smooth tests this follows analytically from Fourier rapid decay, but source-exact Lean weighted-energy construction remains OPEN. A plain \(C_c^2\) test is NOT asserted to have the log weighted carrier norm by the L² embedding alone.
- **NF527** true digamma/prime9/pole strict 1/10 coercivity: analytic exact-rational framework, Lean OPEN.
- **NF523/NF524/NF528** original \(\ell_U\) complete graph convergence/nonzero sign, Lean OPEN. General RH, global odd-sector W_ODD_NEG: OPEN.

## V. Next NF538

First inspect focused NF535–NF537 CI for real compiler errors and repair upstream targets rather than claiming work that has not typechecked. Next compile the UNIVERSAL full source graph quadratic identity (via `lp.inner_eq_tsum` and actual sampling), then build the genuine compact smooth test's weighted logarithmic physical-domain membership and its a.e. real-odd sample symmetry. Only afterward attach the original NF527 arithmetic coercivity and original NF528 singular graph limit.

**Disposition: NEW SOURCE-GRAPH ALGEBRAIC REDUCTION, NF537 LEAN CHECK PENDING; RH remains OPEN.**
