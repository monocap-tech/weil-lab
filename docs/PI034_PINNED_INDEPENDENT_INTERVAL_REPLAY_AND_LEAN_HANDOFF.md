# PI034 — Pinned independent replay custody, nine-exact-root proof boundary, and Lean handoff

**Weil-Lab Potential Interface / controlled reopening.** Parent \`research/pi033-exact-nine-first-prime-root-exhaustion\`. This branch adds a reproducibility/acceptance wrapper and this memo **only**. It does not modify the PI027–PI033 mathematical source, the inherited integer enclosure programs, original IV011, any Lean files, workflows, NF artifacts, or actual zeta-zero traces. Original HD/A frontier remains **692/968**, separate from PI arithmetic progress. No PR or Actions dispatch.

## 1. New: the exact PI032 and PI033 programs were independently executed

The two Python sources were fetched directly from the PI033 GitHub research branch, copied byte-for-byte into an independent local container, and checked with Git's actual object calculation \`git hash-object\`. The hashes matched the GitHub-reported **blob** identities exactly:

| Pinned source | Git blob |
|---|---|
| \`scripts/pi032_exact_interval_transversality.py\` | \`76f16e65e5553f36c5dbb3b74a2a01388083d680\` |
| \`scripts/pi033_exact_nine_exhaustive.py\` | \`0a5bf6d9cd928e7f1f68335258699f2cd468e78e\` |

The local environment had Python and Git, but not \`lean\` or \`lake\`; neither file required a Python package installation or invoked GitHub Actions. \`python -m py_compile\` completed for both sources.

**All nine exact committed-source commands passed**, with Python assertions enabled:

| Command \`--part\` | Exact independent local result |
|---|---|
| PI032 \`core\` | PASS; \(\mathcal I(0)\subset[17.637802920,20.015845145]\); \(\int|E'|^2\subset[5475.183216264,8266.966844205]\) (printed rounded endpoints, internal exact intervals) |
| PI032 \`1\` | PASS; \(I(0.106)\subset[0.48848,0.91739]\), \(I(0.115)\subset[-0.75013,-0.35846]\), \(I'(0.111)\subset[-181.12,-95.82]\), derivative margin 45 |
| PI032 \`2\` | PASS; \(I(0.477)\subset[-0.48911,-0.45507]\), \(I(0.490)\subset[0.44863,0.48966]\), \(I'(0.484)\subset[69.82,75.46]\), derivative margin 2 |
| PI032 \`3\` | PASS; \(I(0.692)\subset[0.54392,0.86993]\), \(I(0.704)\subset[-0.83417,-0.50765]\), \(I'(0.698)\subset[-150.96,-79.06]\), derivative margin 21 |
| PI033 \`0\` | PASS; \([0,0.101]\), six adaptive no-root sign leaves |
| PI033 \`1\` | PASS; \([0.121,0.477]\), 31 adaptive no-root sign leaves |
| PI033 \`2\` | PASS; \([0.498,0.690]\), 22 adaptive no-root sign leaves |
| PI033 \`3\` | PASS; \([0.706,0.820]\), 17 adaptive no-root sign leaves |
| PI033 \`bridge\` | PASS; exact interval \(\mathcal I'(0.491)>69\), three derivative-overlap checks, exact positive-tail polynomial |

**Unlike earlier PI033 reports of an "independent equivalent" local pilot, this replay used the exact GitHub-pinned source bytes**, with blob identity independently checked. PI032 root bracket \((0.477,0.490)\) shares the left endpoint of its larger PI033 monotone band \([0.477,0.498]\); this is consistent with the no-gap cover and must not be mislabeled as a strict containment of closed intervals.

## 2. Independent mathematical spot-audit

Independent symbolic differentiation confirms the exact \(\log g\) derivatives through order 5 used by \`envelope\`, and the compact tail identity
\[
\boxed{
E(y)=g'''(y)-\delta g'(y)
=\frac{g(y)(1-2y)}{[y(1-y)]^6}
\left[1-10v+24v^2-12v^3-\delta v^4\right],
\quad v=y(1-y).
}
\]
The program's exact lower evaluation of the bracket polynomial at \(v=369/2500,\ \delta=1/3240000\) is
\[
\boxed{\frac{12923908971113359}{1562500000000000000}>0.}
\]
This yields the analytic sign exclusion \(\mathcal I(\tau)<0\) for \(41/50\le\tau<1\); at \(\tau=1\) the correlation is zero but \(B>0\).

Separately, a new independent \`Fraction\` partition audit checked that the following eight rational intervals have no gaps and exactly cover \([0,1]\):
\[
\begin{gathered}
[0,.101],\ [.101,.121],\ [.121,.477],\ [.477,.498],\\
[.498,.690],\ [.690,.706],\ [.706,.820],\ [.820,1].
\end{gathered}
\]
The three PI032 root brackets are contained in exactly one of the three derivative-monotone bands. Their interiors are disjoint. The four no-root sign atlas sectors and the smooth sign-definite tail exclude roots elsewhere.

This verifies the **classical analytical deduction** from the replayed integer enclosure claims to exactly three positive normalized correlation offsets. The PI032 original Gamma derivative estimate \(\ell^6|B'|<10^{-3}\), together with source \(\kappa_3=\log3/\sqrt3>1/3\), proves that each of the three central and six translated satellite phase roots is simple. Thus, subject to the already documented **PI027 original signed Weil source identification and Gamma positive-mode derivation**, the PI033 conclusion survives byte-exact independent replay:
\[
\boxed{\#\{a\in(\log3-d,\log3):\Theta(a)=0\}=9,\quad
\Theta'(a_*)\ne0,\quad P(a_*)=B(a_*)>0.}
\]

**Audit limits.** A correct integer-interval program is still different from a Lean proof of its numerical enclosure soundness; the independent replayer checked results and sampled mathematical formula identities but did **not** machine-verify every analytic inequality inside the endpoint envelope implementation or re-prove the original full Weil formula inside the PI source branch. The replay does not constitute formal/kernel acceptance, independent spectral validation, global positivity or RH.

## 3. New fail-closed frozen-source replay entrypoint

New file \`scripts/pi034_fixed_source_replay.py\` checks both inherited script **Git blobs** before and after each execution using SHA-1 with the Git \`blob <length>\0<contents>\` preamble. It fails on any source mutation or checksum mismatch, enforces assertions-enabled Python, and verifies exact Fraction partition/tail/Gamma rational gates independently of either imported source.

Examples:
\`\`\`sh
python3 scripts/pi034_fixed_source_replay.py --part manifest
python3 scripts/pi034_fixed_source_replay.py --part 32-core
python3 scripts/pi034_fixed_source_replay.py --part 32-1
python3 scripts/pi034_fixed_source_replay.py --part 33-bridge
python3 scripts/pi034_fixed_source_replay.py --part all
\`\`\`
There are exactly **nine** executable mathematical parts under \`all\`: PI032 core,1,2,3 and PI033 0,1,2,3,bridge. Each runs as an independent process with source pins rechecked, stdout receipt validated, and no action/network/Lean dependency. This wrapper was committed after the manual byte-exact replay and its own \`all\` path is not yet represented as a fresh complete execution receipt; do not claim otherwise.

## 4. Highest-value next task: PI035 source-bound Lean bridge

Do not immediately translate the whole Python interval integrator into trusted Lean. Stage proofs along three **non-axiomatic** interfaces so the original source connection is independently testable.

**A. Minimal finite sign-atlas/root-count abstract theorem (no Weil dependency).** For a twice differentiable real \(I\) on [0,1] and a positive continuous perturbation \(B\), prove in Lean that: (i) four sign-certificate regions have fixed sign; (ii) three protected bands are strictly monotone via one derivative sample and a proven \(C^2\) Lipschitz estimate; (iii) the remaining tail is sign-definite; (iv) every band contains exactly one zero of the appropriate perturbed phase if its original signed endpoint inequalities and derivative dominance hold. A purely correlation-monotone proof needs an additional argument to ensure the *perturbed* function cannot have multiple roots; here PI032 provides the stronger derivative dominance on each nested root bracket.

**B. Physically sourced original Weil bridge.** Re-pin the literal \`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalCrossSupportArithmeticCutoff.lean\` Git blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\`. In the actual co-resident Lean source graph prove (not assume) the \(m=1\) pole cancellations, genuine n=3 prime isolation in \((\log3-d,\log3)\), Hermitian correlation decomposition, and the original off-contact Gamma amplitude's positivity and derivative bound. Retain the compensated diagonal Gamma distribution, exact normalization, test admissibility, and Fourier conventions. Do not infer source equivalence merely from the classical expression in this memo.

**C. Interval enclosure kernel acceptance.** First prove a small, standalone Lean soundness lemma for outward scaled-integer arithmetic and the rational partition, then provide the exponential alternating-series enclosure and derivative endpoint envelope lemmas. Only after those are true theorems (not opaque external sign assertions) should the PI032/PI033 numerical bounds be promoted to kernel acceptance. Require literal source SHA, exact compiled Lean target/module hash, \`.olean\` evidence and \`#print axioms\` with only accepted standard axioms. Source-bound \`native_decide\` or unchecked oracle imports are not substitutes for the strict gate.

These steps are independently useful even if the full real-integral formalization becomes expensive. A minimal \`formal_candidates\` sketch may be prepared on a fresh branch, but no Lean acceptance can be claimed without a genuine compiler and strict axiom audit.

## 5. Controlled submission gate and research boundary

PI033's inherited branch has 12 workflow files; its eight pull-request workflows are path-scoped, four manual-only. PI034 only adds \`docs/PI034_...\` and \`scripts/pi034_fixed_source_replay.py\`; these names are not dependencies of the inherited eight PR workflows. No PR, workflow, dispatch or heavy job was launched. A future PR against \`main\` requires an **independent full stacked-diff comparison and expected fan-out count**, because previous PI source/Lean changes in ancestor commits may activate other workflows. Coordinate any opt-in Lean CI with NF and preserve the 692/968 accepted frontier.

The complete spectral divisor correspondence (CP), canonical test/Haar/cutoff matching, the printed Masullo Chapter 12/13 factor-two real-place discrepancy and global Weil positivity remain outside what the PI032–PI034 classical root-count certificates establish.

**Next — PI035:** stage the smallest non-axiomatic Lean interval/partition/root-count modules, inspect the actual pinned Mathlib version and original source lineage, and run only local/read-only compiler preflights until a narrow source-scoped CI gate is independently justified.
