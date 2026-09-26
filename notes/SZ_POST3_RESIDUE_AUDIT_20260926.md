# SZ-POST3-RESIDUE-AUDIT-20260926 — Post-SZ-3 reconciliation

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Operation:** audit / reconciliation only  
**Canonical head before audit:** SZ-CROSS-COLLAR-3  
**Public promotion:** forbidden  
**Traversal movement:** none

## 0. Scope

This audit reviews the post-ratification Suzuki residue created after the
canonical head

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}
\]

and separates:

1. mathematically clean auxiliary lemmas/no-go results;
2. dependency-gated bridge results;
3. superseded exploratory formulations;
4. source/proof obligations that must remain open before any later
   ratification.

The audit does **not** itself ratify later residue and does not change the
canonical cursor.

Suzuki v3 was rechecked during this audit.  The paper explicitly supplies:

- the continuous even screw function \(g\), with prime-power hinge term in
  (1.3);
- \(G_a=P_aGP_a\);
- \(B_a=D^*G_aD\), \(\mathfrak D(B_a)=H_0^1(-a,a)\);
- Theorem 1.1: \(A_a\) is the Friedrichs extension of \(B_a\);
- discreteness of the spectrum of \(A_a\);
- Theorem 1.3: continuity of the lowest eigenvalue \(\lambda_a\).

These source facts support the regular screw-carrier and finite-kernel parts
of the later residue.

---

## 1. High-level disposition

The post-SZ-3 work contains a valid structural spine, but it should not be
ratified as one undifferentiated block.

The strongest audit-safe compression is

\[
\boxed{
\begin{aligned}
&\text{raw selected-coordinate naturality}\\
&\longrightarrow
\text{regular Suzuki derivative bridge}\\
&\longrightarrow
\text{regular zero-side channel decomposition}\\
&\longrightarrow
\text{logarithmic-form Bessel extension}\\
&\longrightarrow
\text{same-source correction}\\
&\longrightarrow
\text{exact affine-fiber margin law}.
\end{aligned}
}
\]

The later rough-endpoint / edge-quasi-analyticity chain is useful
reconnaissance, but part of it still depends on source pinning or an
auxiliary complex-analysis construction that should remain explicitly
non-load-bearing.

---

## 2. Clean auxiliary results — recommend RATIFIABLE after editorial normalization

### 2.1 SZ-CROSS-COLLAR-4R

**Disposition:** CLEAN / RATIFIABLE AUXILIARY.

The identity

\[
S_c=E^*S_b
\Longrightarrow
S_b^*E=S_c^*
\]

is exact, and the compact-window realization by restriction of fixed global
modes is straightforward.

Its conclusion is correctly limited to raw selected-coordinate/source
naturality and does not infer sign custody.

This is the correct replacement for the overstrong use of SZ-CROSS-COLLAR-4.

---

### 2.2 SZ-BACKGROUND-ELIMINATION-COLLAR-0

**Disposition:** CLEAN ABSTRACT AUXILIARY.

The strict-gap stability statement

\[
K_B(c)\succeq\eta I,
\qquad
K_B(b)\to K_B(c)\text{ in operator norm}
\]

implies persistence of background admissibility on a right collar.

The note also correctly records that mere semidefinite endpoint admissibility
is not open.

The later global-gap no-go means this theorem is not the actual native route,
but the abstract statement itself is sound.

---

### 2.3 SZ-BG-COV-CONT-0

**Disposition:** CLEAN ON ITS STATED NATIVE AUXILIARY CARRIER.

The columnwise support-continuity plus inverse-height-square majorant gives
Hilbert-Schmidt continuity of the native zero-side synthesis family; the
covariances then vary in trace norm, hence operator norm.

The carrier warning is essential:

\[
\boxed{
\text{this is not continuity of Suzuki's unbounded }A_a.
}
\]

Retain as auxiliary H1/Problem-1 information, not as the Suzuki bridge.

---

### 2.4 SZ-BG-GAP-0

**Disposition:** CLEAN ABSTRACT AUXILIARY.

Two conclusions survive audit:

1. a global positive covariance gap is impossible for a compact/trace-class
   covariance defect on an infinite-dimensional carrier;
2. under the joint budget,
   \[
   Z_B:=\ker(I-X_BX_B^*)
   \subseteq\ker X_M^*,
   \]
   so \(R_B=I-X_BX_B^*\) is strictly positive on the finite-dimensional
   selected-active range \(\operatorname{Ran}X_M\).

The finite-dimensional compactness step giving a positive relative gap is
valid.

---

### 2.5 SZ-BG-RELATIVE-GAP-0

**Disposition:** CLEAN NO-GO, WITH SCOPE CLARIFICATION.

The diagonal compact-synthesis example correctly proves that norm-continuous
physical channels/covariances need not produce norm-continuous Douglas
solutions or transport the selected-active relative gap.

Important scope point:

the nearby example does **not** preserve the endpoint joint budget; indeed the
selected/background screens coincide there.  That is not a defect in the
counterexample because the note only aims to show that physical continuity
plus individual background admissibility does not preserve the endpoint
relative gap.  The collapse is itself a selected-residual defect.

The note should not be cited as a counterexample under a maintained nearby
joint nonnegativity hypothesis.

---

### 2.6 SZ-COLLAR-BRANCH-CLASSIFICATION-0

**Disposition:** CLEAN CONDITIONAL TAXONOMY.

At each strict support:

- background admissible \(\Rightarrow\) eliminate it and classify selected
  residual failure as SR-R or SR-B;
- background inadmissible \(\Rightarrow\) classify the background as BG-R or
  BG-B.

This is a pointwise WD-T10 / WD-A4 classification.

The note correctly refuses to infer WD-T37 or WD-T39 from a single support.

---

### 2.7 SZ-PRECOND-FORM-BRIDGE-1

**Disposition:** SOURCE-BACKED / RATIFIABLE.

Suzuki supplies the regular derivative bridge

\[
D=i\,d/dx,
\qquad
Q_W(v_1,v_2)=\langle G_aDv_1,Dv_2\rangle
\]

on the regular carrier, and \(A_a\) is the Friedrichs extension of
\(D^*G_aD\).

The distinction between

- Suzuki \(G_a\);
- Suzuki \(K_a=(-\Delta_N)^{-1}\);
- the repo auxiliary Dirichlet resolvent

is correct and should be retained.

This pass supersedes the speculative preconditioner framing of
SZ-CARRIER-METRIC-COMPAT-0.

---

### 2.8 SZ-SAME-SOURCE-MARGIN-0

**Disposition:** CLEAN ABSTRACT VARIATIONAL LEMMA, DEPENDENCY-GATED FOR ZETA.

Once a bounded selected-coordinate map \(\sigma_b\) is available, the affine
fiber

\[
\widetilde k+\ker\sigma_b
\]

and the exact margin law are correct.

In the finite nonnegative case,

\[
\mathfrak m_b(u)
=
\sup_{\substack{h\in\ker\sigma_b\\q_b(h)>0}}
\frac{|q_b(\widetilde k,h)|^2}{q_b(h)},
\]

with \(+\infty\) correctly covering negative or coupled-null directions.

The MF/MV subsequence dichotomy is also valid.

---

### 2.9 finite-kernel and variance-growth parts of SZ-MV-ROUGH-ENDPOINT-0

**Disposition:** CLEAN AUXILIARY.

For \(u\in\ker G_c\), \(v=D^{-1}u\) lies in the domain of \(B_c\), satisfies
\(B_cv=0\), and hence belongs to \(\ker A_c\) because \(A_c\) extends \(B_c\).
Since \(A_c\) has discrete finite-multiplicity spectrum,

\[
\boxed{\dim\ker G_c<\infty.}
\]

The variance identity

\[
\frac d{db}\Delta_{c,b}(u)^2
=
|F_u(b)-m(b)|^2+|F_u(-b)-m(b)|^2
\]

is also correct.

---

### 2.10 SZ-KERNEL-ENDPOINT-QA-0 finite-dimensional filtrations

**Disposition:** CLEAN AUXILIARY.

The nested exact-persistence spaces stabilize near \(c\) because they are
nested subspaces of the finite-dimensional space \(\ker G_c\).

Likewise

\[
F_N
=
\{u:\Delta_{c,c+\varepsilon}(u)=o(\varepsilon^N)\}
\]

is a descending chain of finite-dimensional subspaces and therefore
stabilizes at a finite index.

Thus

\[
\mathcal E_c:=F_\infty/P_c^+
\]

is a legitimate finite-dimensional obstruction space.

No quasi-analyticity is implied merely by this reduction.

---

### 2.11 finite-dimensional separation in SZ-KERNEL-EDGE-QA-2

**Disposition:** CLEAN GIVEN SZ-KERNEL-EDGE-QA-1.

Once the prior localization theorem is granted, the restriction/moment and
finite collar-sample separation arguments are ordinary finite-dimensional
linear algebra.

The existing note can actually be strengthened slightly:

if every nonzero \(u\in E_c\) is locally nontrivial near at least one point of
\(\Sigma_c\), then restriction to the union of radius-\(r\) neighborhoods of
\(\Sigma_c\) is injective for **every** \(r>0\), not merely one sufficiently
small radius.

This strengthening is optional and does not invalidate the weaker statement
currently recorded.

---

## 3. Dependency-gated results — mathematically plausible/clean, but do not ratify before their bridge inputs

### 3.1 SZ-PRECOND-FORM-BRIDGE-2

**Disposition:** CONDITIONAL RATIFIABLE.

The integration-by-parts estimate

\[
|z_\gamma(D^{-1}u)|
\lesssim_a
(1+|\gamma|)^{-1}\|u\|_2
\]

combined with unit-height zero counting does give a bounded regular
zero-coordinate analysis map into \(\ell^2\).

Given the Horizon-1 zero-side Hermitian identity and its Fourier
normalization, the operator decomposition

\[
G_a
=
S_{+,a}S_{+,a}^*
-
S_{M,a}S_{M,a}^*
-
S_{B,a}S_{B,a}^*
\]

then follows by polarization and bounded-operator equality.

**Audit gate:** before ratification, explicitly pin the exact H1 zero-side
normalization used here, including multiplicity weighting / quotient
conventions.  The mathematics is consistent with the H1 specialization, but
the note presently treats that specialization as an already-normalized
identity without repeating the exact source interface.

---

### 3.2 SZ-CHANNEL-CUSTODY-FORMDOMAIN-0 / LOG-BESSEL

**Disposition:** STRONG / RECOMMEND RATIFICATION AFTER ONE SOURCE-NORMALIZATION PASS.

The Paley-Wiener reproducing-kernel argument is sound:

\[
\sum_{\gamma}|F(\gamma)|^2
\lesssim_a
\int_{\mathbb R}
\log(e+|t|)|F(t)|^2dt.
\]

The ingredients are:

- compact support;
- a smooth cutoff reproducing kernel with rapid decay uniformly in the fixed
  zero strip;
- the \(O(\log T)\) unit-shell zero count;
- discrete convolution with the logarithmic weight.

Horizon 1 already records the shifted two-sided logarithmic form estimate

\[
Q_c(f)+C_c^{(0)}\|f\|_2^2
\asymp_c
\int\log(e+|t|)|F(t)|^2dt.
\]

So extension of the zero-coordinate map to the closed shifted form domain is
legitimate.

**Audit gate:** same as PFB-2: pin the exact zero-side multiplicity and Fourier
normalization before making the final polarized channel identity canonical.

No positive-Sobolev bootstrap is hidden here.

---

### 3.3 SZ-CROSS-COLLAR-SAME-SOURCE-0

**Disposition:** CLEAN ON THE UNRESTRICTED COMPLEX FORM CARRIER, DEPENDS ON
LOG-BESSEL.

Surjectivity of

\[
\sigma_c:\mathcal F_c\to M_\Pi
\]

follows already on \(C_c^\infty(-c,c)\): an annihilating nonzero finite
coefficient vector would produce a finite distinct-frequency exponential sum
vanishing distributionally on an interval, hence identically.

The old-domain correction

\[
h^\circ=h-E\phi_h
\]

therefore preserves the quotient cross functional while killing selected
coordinate variation.

This proves same-source full negativity when \(\Lambda\ne0\).

**Scope gate:** if a later application imposes a parity/reality subspace, the
surjectivity statement must be rechecked in that restricted sector.  The
current proof is for the unrestricted complex carrier.

The note correctly does not infer selected sign ownership.

---

### 3.4 SZ-MARGIN-MV-FIRST-ORDER-0

**Disposition:** CLEAN ON THE REGULAR SCREW CARRIER, DEPENDENCY-GATED.

The corrected residual

\[
d_b=r_b-JR_c(\sigma_br_b)
\]

satisfies

\[
\sigma_b(d_b)=0,
\qquad
q_b(Ju,d_b)=\Delta_b^2.
\]

For \(b\) in a fixed compact right collar, uniform boundedness of the finite
selected-coordinate maps and of \(G_b\) gives

\[
\|d_b\|=O(\Delta_b),
\]

hence

\[
\boxed{
\mathfrak m_b(u)\gtrsim\Delta_b^2.
}
\]

A matching upper bound requires the additional coercivity of
\(q_b|_{\ker\sigma_b}\), exactly as stated.

Before ratification, add the short explicit proof of uniform boundedness of
\(\sigma_b\) on the compact \(b\)-collar; for a fixed finite packet it follows
directly from the bounded exponential columns.

---

## 4. Superseded residue — retain for provenance, do not ratify as theorem units

### 4.1 SZ-CROSS-COLLAR-5 (20260925)

**Disposition:** SUPERSEDED.

Its useful raw-coordinate content is recovered more cleanly by
SZ-CROSS-COLLAR-4R and the later same-source theorem.

Any wording that risks identifying coordinate preservation with sign custody
should remain noncanonical.

---

### 4.2 SZ-CROSS-COLLAR-6 (20260925)

**Disposition:** SUPERSEDED / HISTORICAL.

Its important correction — that collar negativity does not automatically
satisfy WD-T37 — remains valid.

The later same-source and margin passes give the cleaner formulation of what
survives.

Do not ratify SZ-6 as a current bridge theorem.

---

### 4.3 SZ-CARRIER-METRIC-COMPAT-0

**Disposition:** PARTIAL RETENTION ONLY.

Retain the structural observation that a boundedly invertible/unitary
congruence cannot identify the compact auxiliary Problem-1 covariance
realization with Suzuki's unbounded localized operator.

Do **not** ratify its provisional PFB architecture as the final bridge:
SZ-PRECOND-FORM-BRIDGE-1 replaces it with Suzuki's exact derivative map.

---

### 4.4 SZ-CROSS-COLLAR-5R

**Disposition:** SUBSUMED CONDITIONAL LEMMA.

The pointwise statement

\[
\text{full negativity}
+
\text{legitimate background elimination}
\Rightarrow
\text{negative residual selected defect}
\]

is correct, but the later branch-classification note packages it more cleanly.

Keep for provenance; no need to make it a separate canonical milestone.

---

## 5. Open/illustrative residue — keep explicitly non-load-bearing

### 5.1 superflat Stieltjes construction in SZ-MV-ROUGH-ENDPOINT-0

**Disposition:** RETAIN AS AUXILIARY ILLUSTRATION; DO NOT MAKE LOAD-BEARING
WITHOUT AN EXPANDED COMPLEX-ANALYSIS PROOF OR SOURCE PIN.

The conformal-map construction is plausible and internally consistent:

- analytic off the finite slit;
- bounded boundary values;
- superflat positive-axis approach;
- \(O(z^{-2})\) decay enforcing zero mean.

However the step from those boundary values to an \(L^2\) jump density and the
exact Stieltjes representation currently invokes the Cauchy jump theorem in
one sentence.

That is enough for reconnaissance but below the project's usual standard for
a load-bearing theorem.

The downstream finite-dimensional kernel reductions do not require this
example.

---

### 5.2 SZ-KERNEL-EDGE-PROP-0

**Disposition:** MIXED AUXILIARY.

The finite delay geometry is sound:

- away from threshold, all already-active prime shifts sample a compact
  interior set separated from the endpoints;
- at \(2c=\log n_0\), exactly one new prime-power shift directly couples the
  two endpoint germs.

The generic smooth-kernel example correctly warns that a compact smooth
integral operator can possess a rough zero mode.

The comparisons with logarithmic-Laplacian UCP are contextual and should stay
non-load-bearing: open-set UCP is logically weaker than the required
flatness-to-vanishing statement for this delay operator.

---

### 5.3 SZ-KERNEL-EDGE-QA-1

**Disposition:** PROMISING / SOURCE-PIN GATE.

The first-difference identity

\[
F_u(c+\delta)-C_u
=
\int_0^{2c}
[g(s+\delta)-g(s)]u(c-s)\,ds
\]

is exact.

Suzuki (1.3) confirms the prime-power hinge structure

\[
(t-\log n)_+.
\]

The local Volterra formula for one hinge is correct, as is the threshold
opposite-edge specialization.

The analytic-gap argument is also correct **provided** the remaining
archimedean part of \(g\) is source-pinned as real-analytic on compact
subsets of \((0,\infty)\).

Before ratification, add an exact source pin to Suzuki §2.2 / the explicit
archimedean formula establishing:

\[
a_\infty\in C^\omega((0,\infty))
\]

and the stated origin expansion.

Until that pin is recorded, the finite singular-set localization should
remain residue rather than canonical theorem.

---

### 5.4 SZ-KERNEL-EDGE-QA-2

**Disposition:** CONDITIONAL ON QA-1.

The finite-dimensional separation arguments are correct once the QA-1
analytic-gap localization is accepted.

No additional analytic theorem is hidden in QA-2.

---

## 6. Corrections / normalization required before ratification

The audit found no contradiction requiring deletion of the post-SZ-3 branch,
but it found several places where the status should be narrowed.

### C1 — zero-side normalization pin

Before ratifying PFB-2 / LOG-BESSEL channel custody, explicitly record the
zero-side Hermitian formula with:

- Fourier convention;
- multiplicities;
- repeated-ordinate quotient/null convention;
- pair normalization.

This is normalization/custody work, not a new theorem.

### C2 — sector scope on same-source surjectivity

The current same-source surjectivity theorem is valid on the unrestricted
complex form carrier.

Do not silently reuse it in an even/odd/real sector without proving
surjectivity in that sector.

### C3 — compact-collar uniformity lemma

Before ratifying the residual-square margin lower law, record explicitly that
for a fixed finite packet

\[
\sup_{c<b\le A}\|\sigma_b\|<\infty
\]

and

\[
\sup_{c<b\le A}\|G_b\|<\infty.
\]

Both are elementary from finite exponential columns / continuous kernel on a
fixed compact square.

### C4 — Stieltjes superflat example remains illustrative

Do not use the conformal jump example as a canonical no-go until its Cauchy
jump representation is fully proved or source-pinned.

The weaker conclusion actually needed downstream is only:

\[
\text{generic }L^2\text{ endpoint structure alone has not supplied a lower
jet}.
\]

### C5 — archimedean analyticity source pin

Before promoting the finite singular-set theorem, pin the exact part of
Suzuki's explicit formula proving that, away from \(0\), the non-prime
archimedean component is real-analytic.

---

## 7. Proposed ratification batches

The residue should be ratified in dependency order, not by chronology.

### Batch A — safe auxiliary algebra / no-go package

Candidate contents:

- SZ-CROSS-COLLAR-4R;
- SZ-BACKGROUND-ELIMINATION-COLLAR-0;
- SZ-BG-COV-CONT-0, with native-carrier label;
- SZ-BG-GAP-0;
- SZ-BG-RELATIVE-GAP-0, with scope clarification;
- SZ-COLLAR-BRANCH-CLASSIFICATION-0.

This batch does not move the canonical Suzuki head beyond SZ-3; it merely
certifies auxiliary structure.

### Batch B — Suzuki channel bridge

After C1:

- SZ-PRECOND-FORM-BRIDGE-1;
- SZ-PRECOND-FORM-BRIDGE-2;
- SZ-CHANNEL-CUSTODY-FORMDOMAIN-0.

This is the important bridge batch.

### Batch C — same-source / margin package

After Batch B and C2/C3:

- SZ-CROSS-COLLAR-SAME-SOURCE-0;
- SZ-SAME-SOURCE-MARGIN-0;
- SZ-MARGIN-MV-FIRST-ORDER-0.

### Batch D — endpoint/edge reconnaissance

Ratify only the internally closed pieces first:

- finite-dimensionality of \(\ker G_c\);
- variance-growth identity;
- finite persistence/flatness filtrations.

Leave the generic superflat Stieltjes example and the QA-1 singular-set
theorem auxiliary until C4/C5 are discharged.

---

## 8. Current mathematical horizon after audit

The branch has **not** discovered a contradiction or invalidated the ratified
SZ-3 cross-collar theorem.

The strongest dependency-clean unresolved target remains:

\[
\boxed{
\mathcal E_c
=
F_\infty/P_c^+
\stackrel{?}=0.
}
\]

But the audit changes how that target should be approached.

Before further edge traversal, the highest-value work is to certify the
bridge batches above, especially:

\[
\boxed{
\text{C1: zero-side normalization}
}
\]

and

\[
\boxed{
\text{C5: exact Suzuki archimedean analyticity pin}.
}
\]

The proposed canonical edge matrix is downstream of those normalization
obligations and should not yet be promoted as the immediate canonical target.

---

## 9. Audit determination

\[
\boxed{
\text{POST-SZ-3 RESIDUE: STRUCTURALLY SOUND, PARTIALLY DEPENDENCY-GATED,
NO BULK ROLLBACK REQUIRED.}
}
\]

The main corrections are status/custody corrections, not mathematical
retractions.

Canonical head remains:

\[
\boxed{
\text{SZ-CROSS-COLLAR-3}.
}
\]

**No canonical cursor movement is asserted by this audit.**
