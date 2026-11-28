# Weil-Lab — IV050
## Uniform dense-mode mixed Gamma bound, energy-relative Schur convergence, and controlled submission gate

**Standing:** Classical/source-aligned mathematical proof with a locally executed exact-Fraction checker. **NONKERNEL**. No source commits, new research branches, PRs, workflow dispatches, reruns, or new GitHub Actions jobs. User has authorized controlled reopening, but the existing IV023 lineage does not yet demonstrate bounded PR fan-out. The preceding original numerical frontier stays **692/968 kernel-passed**, with canonical registry-body reconciliation distinct; **neither value changes through IV050**.

## 1. Source object and theorem statement

Use the **actual** original signed Weil form on the fixed physical logarithmic window
\(I=(-11/10,11/10)\), retaining the true NF599 quarter-digamma Gamma multiplier, authentic von Mangoldt two-sign correlations at \(n\in\{2,3,4,5,7,8,9\}\), and **both** crossed Mellin poles:

\[
W=\Gamma-P+|h\rangle\langle h|-|k\rangle\langle k|,\quad
h=\sqrt2\,1_I\cosh(x/2),\quad k=\sqrt2\,1_I\sinh(x/2).
\]

The *classical* Gamma physical dictionary from NF599 and PI007/PI008, whose original-source Lean Fourier-inversion bridge is still **unaccepted**, reads

\[
\Gamma=\gamma(0)I+L_K,\qquad
K(s)=\frac{e^{-s/2}}{1-e^{-2s}},\quad
(L_Kf)(x)=\int_{\mathbb R}K(|x-y|)(f(x)-f(y))\,dy.
\]

Let \(M\ge2200\), partition \(I\) into \(M\) equal cells \(J_j\) of width \(w=11/(5M)\le1/1000\). Set \(\Pi_M\) the \(L^2(I)\) cell-average projection and \(Q_M=1-\Pi_M\). For all low vectors (including *dense* combinations using **all** cell averages), the **new classical theorem** is

\[
\boxed{\|Q_M\Gamma\Pi_M\|_{L^2\to L^2}<22,\qquad
\|Q_MW\Pi_M\|<\frac{341}{10}<35.}\tag{IV050-A}
\]

The operator is initially defined on the finite indicator span (which lies in the source logarithmic Gamma operator domain), and the output is projected onto the physical window. This is a **uniform-in-\(M\)** bound on the *entire dense low space*, not a column bound or an abstract replacement for the original source.

If the genuine high-mode signed Weil compression has the IV047 lower bound \(C_M=Q_MWQ_M\ge c_MQ_M>0\), then

\[
\boxed{0\le B_M^*C_M^{-1}B_M < \frac{1225}{c_M}\Pi_M,\qquad B_M=Q_MW\Pi_M.}\tag{IV050-B}
\]

In particular, because IV049/IV047 mathematically prove \(c_M\to\infty\) as \(M\to\infty\),

\[
\boxed{\|C_M^{-1/2}B_M\|\to0}
\]

on the **entire** dense low cell-average space. This answers the asymptotic dense-vector norm question raised by IV049. It is consistent with IV048's bare mixed norm lower bound \(\|B_M\|>1/4\): the normalizations are different.

**Limitation:** On the IV047 100,000-cell mesh, the existing *only proved* coarse \(c_M>1/100\) gives the useless finite bound \(B_M^*C_M^{-1}B_M<122500I\). The near-zero low-energy margins from IV046 are below \(0.01\). Consequently IV050 does **not** certify the actual finite Schur complement, any global-window signed Weil positivity, equivalence with another spectral construction, or RH. A **quantitative, energy-adapted local Schur certificate** is still needed.

## 2. Source kernel derivative and mean-subtracted cell blocks

For every \(s>0\), \(e^{2s}\ge1+2s\) implies
\[
\frac{1}{1-e^{-2s}}\le\frac{1+2s}{2s},\qquad
K(s)\le e^{-s/2}\left(\frac1{2s}+1\right)\le\frac1{2s}+1.
\]
Also \(-K'(s)=K(s)(\tfrac12+2/(e^{2s}-1))\). Therefore
\[
-K'(s)\le e^{-s/2}\left(\frac{1}{2s^2}+\frac{5}{4s}+\frac12\right)\le\frac4{s^2},
\]
where the last inequality follows from the **positive Taylor lower polynomial** \(4e^{s/2}\ge4+2s+s^2/2\ge1/2+5s/4+s^2/2\). No numerical derivative approximation is involved.

Write \(e_k=1_{J_k}/\sqrt w\) and \(Q_j\) for mean-zero projection on output cell \(J_j\). For the Gamma difference part the block estimates are:

1. **Same cell** \(j=k\): \(L_Ke_k(x)=w^{-1/2}(H(x-a)+H(b-x))\), where \(H(s)=\operatorname{atanh}(e^{-s/2})+\arctan(e^{-s/2})\). For \(s\le w\), the singular difference \(|K(s)-1/(2s)|\le1\): its upper bound is above and its lower bound follows from \(K(s)\ge e^{-s/2}/(2s)\ge1/(2s)-1/4\). After removing the cell mean, the centered function \(\frac12[-\log u-\log(1-u)]\) has \(L^2\) norm at most 1, and the remainder at most \(2w\). So \(\|Q_jL_Ke_j\|_2\le1+2w<2\).
2. **Adjacent cells** \(|j-k|=1\): the output cell potential has absolute value at most \(\frac12\log(1+1/u)+w\), in the rescaled coordinate \(u\in(0,1)\). Since \(\log2<7/10\) and \(\int_0^1(-\log u)^mdu=m!\),
\[
\int_0^1\log^2(1+1/u)du\le(\log2)^2+2\log2+2<4.
\]
Thus \(\|Q_jL_Ke_k\|_2\le1+w<2\).
3. **Separated cells** \(d=|j-k|\ge2\): all arguments satisfy \(|x-y|\ge(d-1)w\). Derivative control gives an oscillation on output \(J_j\) at most \(4/((d-1)^2\sqrt w)\) for the normalized input e_k. Projection to zero mean and multiplication by \(\sqrt w\) yield
\[
\boxed{\|Q_jL_Ke_k\|_2\le\frac4{(d-1)^2}.}
\]

Every nonnegative scalar block-majorant matrix thus has **row and column sums** strictly below
\[
2+2\cdot2+2\cdot4\sum_{n\ge1}\frac1{n^2}
<2+4+16=\boxed{22}.
\]

The scalar Schur test dominates the Hilbert direct-sum matrix \(Q_ML_K\Pi_M\), giving \(\|Q_M\Gamma\Pi_M\|<22\). The original constant Gamma term \(\gamma(0)I\) vanishes under \(Q_M I\Pi_M\). **No cancellation is assumed to obtain this coarse estimate.**

The authentic two-sign prime operator has norm \(<71/10\) from the real \(\Lambda(n)/\sqrt n\) coefficients. The original two crossed poles equal the **signed parity** rank-two operator \(|h\rangle\langle h|-|k\rangle\langle k|\); since \(h\perp k\), its operator norm is \(\max(\|h\|^2,\|k\|^2)<5\) (source IV044). Thus \(\|Q_MW\Pi_M\|<22+71/10+5=341/10<35\), completing (IV050-A).

## 3. Exact rational checker: scope and results

Executed `IV050_dense_mode_schur_checker.py`, a standard-library integer/Fraction preflight using pinned IV047 and IV049 script SHAs. It verifies the rational Taylor-polynomial comparisons, \(\log2\) enclosure, local cell envelopes, discrete row/column sum bound, pole/prime aggregate constants, 100,000/132,000 mesh widths, and actual finite scalar block-majorant rows for representative dense matrices. It produces `IV050_dense_mode_schur_receipt.json` bound to the script's SHA-256.

**Important verification separation:** Pure Fraction arithmetic does **not** machine-prove the continuum kernel identity, differentiation, Hilbert direct-sum Schur estimate, or source operator-domain extension, and it does not compile a new Lean theorem. The present result is a source-aligned **classical mathematical proof**. It needs a formal source bridge and strict `#print axioms` custody before any new kernel acceptance.

## 4. Operational source audit and next controlled submissions

At read-only GitHub inspection of exact **IV023 head SHA** `17deb63ff227d34bf5e570021d7ec3296179465c` (PR #805; stacked base IV022 SHA `4ecf857661d62d93b1566a9e418cb4599ec4023d`), `.github/workflows` had **611 workflow YAMLs**. The IV018 and IV023 jobs themselves use correctly **source-scoped** pull_request paths and preserve workflow_dispatch. However existing historical `nf456-original-two-ray-residual-budget.yml` and `nf471-original-j7-complete-mean-receipt.yml` still declare unrestricted `pull_request:` triggers in that same effective IV023 source lineage. Therefore **bounded expected PR fan-out is not verified** on this lineage; do not submit a heavy IV050 Actions workflow there merely because the global queue is empty. The `main` branch has just three workflows, which does not establish that the stacked IV branch inherited repairs.

The **actual previously failed IV018/IV023 jobs** both ran the Python preflight `source_preflight()` BEFORE their workflow's `lake update`; their strict source dependency lists explicitly include `Path('lake-manifest.json')`, absent from the checked-out commit. A narrow prospective repair is to install the pinned Lean toolchain and run `lake update` first, assert that `lake-manifest.json` was actually produced, then run the **unchanged** Python source-identity preflight, build the two original Lean modules, and run the unchanged standard-only strict axiom audit. This preserves a real manifest SHA rather than spoofing, ignoring or dropping the dependency. **No repair has been deployed or re-run.** The source manifest creation and actual Lean compiler outcomes require a genuine controlled workflow verification.

### Highest-value controlled next actions (ordered)

**Mathematical IV050 source preparation (no Actions):** Pin the IV043/047/049 exact source conventions; add a Lean candidate expressing \(Q_M\Gamma\Pi_M\) as the actual source mixed form, proving the derivative/neighbor/separated-cell estimates and finite scalar Schur lemma. First certify its mathematical statement and source definitions locally (independent proof review, source file SHA bindings, exact Fraction tests); do not claim Lean acceptance.

**CI lineage prerequisite (no heavy Actions):** Read-only or lightweight source-inventory check across the *effective IV050 branch/base stack*, not just `main`. Enumerate all unrestricted historical pull_request workflows and their actual dependencies; require a bounded expected relevant-workflow fan-out, valid source-scoped YAML, preserved dispatch, and no required-check deadlocks. The currently inspected IV023 lineage **fails this prerequisite** because NF456 and NF471 are demonstrably unscoped.

**First controlled compiler submission (Actions required, after lineage gate):** Recover IV018/IV023 strict source preflights by reordering the Lake environment step before the unmodified dependency audit (or an equivalent strictly verified two-stage setup). Run the source/preflight-only audit first if available, then a **single** original IV018 compiler job; only after authenticated `.olean`, `#print axioms` standard-only audit and immutable hash receipt should IV023 be queued. Do not concurrently launch both or reclassify their existing pre-Lean failures as mathematical ones.

**New IV050 kernel certification (Actions later):** Once those dependencies and bounded triggers are verified, submit only the source-attached Gamma finite-atom/mixed identity plus the general discrete Schur lemma as a small, separately scoped candidate; pin exact upstream source/toolchain SHAs, audit `#print axioms` and compiled `.olean`, check absence of `sorryAx`, and require independent artifact reconciliation. The asymptotic theorem and high-mode source domain should be accepted only after its Lean proof, not from this script.

### Falsifiable future gate

The next mathematics must improve the **finite-mesh** energy-relative Schur correction on all dense vectors, ideally using an exact matrix-weighted or preconditioned bound rather than the ineffective \(1225/c_M\). A source-correct a posteriori full-window gate is
\[
\boxed{L_M-B_M^*C_M^{-1}B_M\ge0,\quad C_M>0.}
\]

At current practical meshes we **have not** certified this inequality. Likewise neither global Weil positivity nor RH has been established; any PI/CP equivalence remains independently unproved.
