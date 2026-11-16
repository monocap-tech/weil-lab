# NF536 — Original real-odd smooth tests: literal EF absolute convergence supplies true-divisor ℓ²

**2026-11-15 PT · Draft PR #564 · FORMALIZATION ADVANCE / NEW LEAN CI PENDING.**
Original NF494 source SHA256 `39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181`, 242 original moment identities, actual zeta zeros and their multiplicity copies are untouched. The full U400 is NOT replayed. No RH/global-positivity or original endpoint certificate claimed.

## 1. A stronger result *specific to real odd smooth test functions*

Let the authentic physical window transform have exactly the convention used in the Lean source:
[
F_f(z)=\int_{-B}^B f(x)e^{izx} dx.
]
For a **real odd** function supported inside this symmetric window, the true all-complex transform obeys
[
F_f(\overline z)=-\overline{F_f(z)} .
]
Indeed for real (f), (overline{F_f(z)}=F_f(-\overline z)); oddness changes sign under (z\mapsto-z).

The *actual zeta zero-side autocorrelation sample*, with no invented RH assumption, is
[
\overline{F_f(\overline{z_q})} F_f(z_q)=-F_f(z_q)^2.
]
Therefore, **pointwise for every authentic zero and multiplicity copy**,
[
\left|\overline{F_f(\overline{z_q})} F_f(z_q)\right|=|F_f(z_q)|^2.
]
The unconditional imported `Zeta23.WeilEF.EF_lit_zeta` gives ABSOLUTE summability of the autocorrelation zero series for compactly supported C² autocorrelations. Hence
[
\boxed{\sum_{q\in\mathcal D_\zeta} |F_f(z_q)|^2<\infty},
qquad
\boxed{\sum_{q\in\mathcal D_\zeta} |F_f(\overline{z_q})|^2<\infty}.
]
These conclusions require neither independent zero-height counting, Green density, nor separately certified high-frequency derivative bounds **for the smooth real odd tests**. They are a qualitative graph-entry mechanism. For **non-odd** complex tests the product may be summable even while either source's square sum diverges, so this argument is intentionally restricted.

This does NOT bypass original NF523/NF524/NF528 uniform source-tail control for the NONSMOOTH endpoint-log original `ell_U` or its convergence in the full source graph.

## 2. Lean modules added

**`WeilDefect/Arithmetic/ActualZetaOddPhysicalSampleSummability.lean`**
- `neutralOddPairSample_sq_summable`: the exact mixed-to-diagonal ℓ² implication for arbitrary sample functions with odd-conjugate symmetry; no zeta-zero enumerations.
- `neutralOddPairPartner_sq_summable`: same for conjugate partner samples.
- `neutralActualZetaOddPhysicalWindowSample_sq_summable`: imports the genuine complete zeta EF's absolute all-multiplicity divisor convergence and the authentic window autocorrelation all-complex transform, with **C² autocorrelation and real-odd sample relation as explicit premises**.

**`WeilDefect/Arithmetic/ActualZetaFullSourceLiftOfSquareSummable.lean`**
- `neutralActualZetaFullSourceLiftOfSquareSummable`: supplies a new **GENERIC** full source-graph lift for any actual `NeutralLogHilbertCarrier` vector whose actual P/N sample families satisfy ℓ². The same physical vector and both real source coordinate families are used; the index is `NeutralActualZetaDivisorCoordinate = Σ_ρ Fin(m_ρ)`, without quotient or multiplicity loss.
- `..._physical`, `..._samples`: physically exact source custody and sampling.
This is stronger than the existing specific Green-packet lift **as a construction criterion**, but is *conditional* on the ℓ² P/N input and does not assert graph membership of arbitrary physical vectors.

The new CI steps in `.github/workflows/nf529-source-graph-closure.yml` build each module separately. **No compilation acceptance is claimed until this specific PR's focused run passes.**

## 3. Remaining proof junction

Even after the modules compile, these obligations remain genuinely OPEN in Lean:

1. **A.e. real-odd window transform symmetry.** For a real odd (\psi\in C_c^2(E)), prove the physical-window `F_f(conj z)=-conj F_f(z)` for the **same** actual L² vector whose a.e. representative is \(\psi\). NF535 creates this physical vector, pending compile; do not assert pointwise smoothness of an arbitrary L² representative.
2. **Positive/negative pair ℓ² analysis.** Express the existing source identities
[
P_q=\frac{F_f(\overline{z_q})+F_f(z_q)}{\sqrt2},\quad
N_q=\frac{F_f(\overline{z_q})-F_f(z_q)}{\sqrt2}.
]
The raw \(\ell^2\) estimates above imply both actual P/N analysis families are in \(\ell^2\). Compose with the generic NF536 full source-graph lift, not a Green span.
3. **Full-graph zero sum = source quadratic.** Existing `neutralActualZetaGreenSourceQuadratic_eq_zeroForm` proves this for constructed Green vectors only. Establish the source identity for the generic NF536 full graph sample class; it is algebraically accessible but remains to be **Lean compiled**, and is not automatic from green density.
4. **Actual arithmetic coercivity**: formalize NF527 complete true digamma/prime-(9)/pole (Q\ge0.1\|\cdot\|_{L²}^2) for smooth supported E-tests.
5. **Original singular graph limit**: compile NF524/NF528 full actual two-source approximation of original \(\ell_U\), and physical nonzero lower. Real-odd smooth EF alone does NOT give uniform full-graph norm control of the singular limit.

**Related GitHub custody:** NF535 PR #563 (multiplicity index repair, actual original smooth L² embedding), NF534 PR #562 (a.e. smooth convolution C²), NF533 PR #561 (automatic divisor summability; its original CI failed in index type conversion, patched NF535). NF532 PR #560 focused CI previously passed generic EF with explicit summability premises. NF536 builds atop these drafts; all stages remain provisional.

**NF536 disposition: ANALYTICALLY VALID ODD-SAMPLE SUMMABILITY REDUCTION AND TWO NEW LEAN PROOF TARGETS; NEW LEAN COMPILATION PENDING.**
