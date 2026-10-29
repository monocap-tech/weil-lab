# Mittermeier event cells v2 — primary PDF and reproducibility ZIP review

**Audit time:** 2026-10-28 Pacific. **Classification:** informal external-source investigation; **NO method promotion, NO theorem closure**. **Current canonical:** `W-ODD-NEG` OPEN; NF376 original out-of-fit source test remains active. This is an addendum to `docs/EXTERNAL_MITTERMEIER_SOURCE_AUDIT_20261028.md` and `notes/provisional/EXTERNAL_SUZUKI_MITTERMEIER_ODD_SIGNBOX_BRIDGE_TRIAGE_20261028.md`, NOT a change in their historical record.

## Newly obtained and hashed primary artifacts

The user supplied *Compact Weil Event Cells from Suzuki's Screw Function*, v2, dated Oct 25 2026, **41-page PDF**, and the separate **55-entry** reproducibility ZIP. The PDF identifies Rainer Andreas Mittermeier, DOI 10.5281/zenodo.23603376, paper CC BY 4.0, software MIT, and independent researcher in Landshut, Germany.

- Uploaded PDF SHA-256: `8bcb2ce94d04c748790c95280fcc2351e9c00a00e1bf1e8f6ad8f6875efe19ed`
- Uploaded ZIP SHA-256: `5367d90168e062cad7246de5a052fcf1f27eb16d6b73046a58d02982acd60c2e`
- ZIP CRC: PASS; internal `SHA256SUMS.txt` **54/54 digests MATCH** (the final digest covers `MANIFEST_SHA256.txt`), inner `MANIFEST_SHA256.txt` **53/53 MATCH**. This verifies internal integrity, **not** a separately fetched/verified Zenodo release hash.
- ZIP internal top directory names itself `...v29_reproducibility` while the PDF/public record is **version 2**; treat as an internal release label, not evidence of a separate published v29.
- The PDF p.40 explicitly discloses: AI-assisted tools supported research, verification, figures and language editing; the author accepts responsibility. **Which model and exact division of labor are NOT established.** The PDF has a detailed `Table 2` division-of-scientific-roles across the author's papers (p.7), which is about cross-paper dependencies, *not* a human/AI task log.

## Primary-source mathematical claims now locatable precisely

1. **Definition/source identity:** PDF pp.8–10, Eqns. (1)–(4), (9)–(13), **Proposition 3**. Original compact Weil form `Q(f)=W(f*tilde f)`, base-function half-support `L`; exactly the prime powers `log n<2L`. Normalized even boxes `e_t=2^-1/2 1[-t/2,t/2]`, odd sign-boxes `o_t=2^-1/2 sign(x)1[-t/2,t/2]`. Their exact Gram kernels:
   `Ke(s,t)=Psi((s+t)/2)-Psi(|s-t|/2)`,
   `Ko(s,t)=2Psi(s/2)+2Psi(t/2)-Psi((s+t)/2)-Psi(|s-t|/2)`.
   The previous exploratory `K_sign(a,b)=4Psi(a)+4Psi(b)-2Psi(a+b)-2Psi(|a-b|)` is **twice** the paper's normalized `Ko(2a,2b)` because the previous sign-boxes lacked factor `1/sqrt(2)`; this is a normalization difference, **not** a contradiction.
2. **Domain/density supplied in source:** **Theorem 4, pp.10–11** proves that on each fixed `L`, positivity for all smooth complex supported tests is equivalent to PSD of **both** box Gram matrices for **all finite node collections**. It proves the step-function extension using `H^sigma` density for `0<sigma<1/2`, weighted `L2_log` form continuity (Eq. (8)), and mollification. Thus the earlier objection that the *source itself* did not establish box-domain transport is now resolved **for its own W convention and form**. A distinct exact identification of its normalization, pole and source/frequency conventions with the NF376 original operator is still required before promoting it into Weil-Lab.
3. **Fixed sixteen-node family:** **Eqns. (57)–(58), pp.27–28**, 16 varying even box nodes at `L=0.8`; every normalized weighted row margin >0.2109478331, by 320-bit Arb. **Cor. 34**, not Theorem 4 alone, licenses that particular continuous *finite* family. The author explicitly states that the margin is **not** an L2 coercivity constant. At `L=0.8`, prime set `{2,3,4}`; NF376 `B=1.1` original prime set `{2,3,4,5,7,8,9}` by the paper's own support convention.
4. **Odd-sector information:** **Prop. 31 (p.25)** gives only termwise outer interval bounds for the **nonseparable** odd kernel; **Prop. 32 (pp.25–26)** gives strict cellwise Monge mixed-derivative sign, expressly *not* PSD or exact extrema. Their open problem #2 (p.37) asks for exact odd-cell ranges. Thus no certified NF376 odd `q5_perp` norm or signed residual follows from their even sixteen-node certificate.
5. **Other scoped evidence:** **Theorem 37 (pp.29–30)** gives an RH-independent finite-node spectral tail under the *external* published zero-height verification `H0=3e12`; **Cor. 39 (p.31)** certifies two variable-node parity `2x2` matrices. **Theorem 43/Cor. 44 (p.34)** are finite core-shell Schur/inertia statements: negative finite shell witnesses falsify RH, positive finite shell DOES NOT prove complete positivity. **Theorem 8 (p.13)** asserts that global boundedness below of `4Psi(t/2)-Psi(t)` is RH-equivalent; this retains the full infinite quantifier. The paper's Section 9 extrapolation `n~2.3e38` is explicitly a diagnostic **not** a theorem.
6. **External-source division:** p.7 Table 2 states earlier prime-power checkpoint papers supply scalar curvature and wall formulas, the companion zero-side paper supplies 3000 rational ordinate intervals for Cor.38, the conductor-23 paper has *no proof input* to the event-cell paper, and MAT results are not consumed in these proofs.

## Focused reproducibility execution — what passed / what did not run

All 55 ZIP entries were inventoried; internal digests/CRC passed. Current inspection runtime has no installed `python-flint`, while the release pins **python-flint 0.9.0**, `mpmath 1.3.0`, `numpy 2.3.5`, `sympy 1.14.0`, `contourpy 1.3.3`. We did **not** run Arb entry/16-node/odd-diagonal/20,000-cell/5.7m-wall stages or complete `reproduce.py`.

We selectively extracted and directly replayed, without network access:

- `code/spectral_tail_rational.py`: exact `Fraction`/Taylor arithmetic **PASS**; `H*S2(H)≤8.917197452253843...<9`, **conditional on the external Rosser zero-counting theorem and elementary pi bound**; produced JSON equals expected.
- `code/certify_parity_bridge_v9.py`: exact `Fraction`/Taylor arithmetic **PASS**; expected JSON exactly reproduced, including variable-node `Ke` lower `0.000623013320286` and `Ko` lower `0.002018563164927`, conditional on declared external Suzuki/Platt–Trudgian/LMFDB/Rosser premises. No external zero-location verification was independently rerun.

These are **author-code replays with checked outputs**, not a separately reimplemented proof, not peer review, and do not independently validate the scientific correctness of external premises.

## Current NF376 information-transfer assessment

This primary-source release establishes an **exact formula-based alternate representation of the fixed compact Weil form** with actual domain/density discussion and a credible, internally consistent partial replay. That materially improves *source inspectability* and refines the initial informal bridge hypothesis. However:

- All-node Theorem 4 is an equivalence of **infinite families**, not a finite positivity proof.
- The successful sixteen-node result is even-sector `L=0.8`, not the original `B=1.1` odd `q5_perp` test, and the paper's exact odd-cell range / unbounded support transfer remain open.
- The original `q5_perp` has `||q||≈2.04636e-89`; the NF375 individual lowband threshold `1.5e-13||q||≈3.06954e-102`. 320-bit precision (~96 decimal digits *nominal* relative) alone does not certify that absolute cancellation. Source-adapted interval correlation, normalization and highband payment must be demonstrated. Form continuity is `L2_log`-based, **not** an L2-boundedness claim for the full log-multiplier operator.
- **No** formula/replay in this source already bounds `I4(q5_perp;2^20)`, `H4`, or the original full infinite `B*C^-1B`. There is not yet a verified imported theorem that settles the active accept/stop gate.

## Separate promotion and closure gates

**Promotion condition (external METHOD / source transfer, not closure):** an exact, hypothesis-preserving identification with the **original NF376** supported signed `W` convention; an actual certified, source-adapted full-frequency signed cross-pairing or norm estimate for an **unfitted** original exterior direction (or a rigorous new exterior information-sufficiency obstruction); independent outward arithmetic with complete error/correlation payments at the relevant scales; and evidence that this changes a live NF376 decision. Version, theorem/equation and source pin must be documented **before** updating the canonical obligation. A computationally certified 2x2/16x16 family elsewhere is not sufficient.

**Closure condition:** accepted complete original odd supported operator inequality with **all** finite/infinite coupling, physical source/form-domain audit and canonical `W-ODD-NEG` O1/O2 terms. The even, whole and global/RH bridges remain open separately. A new external source pin alone cannot close any of them.

**Disposition:** CONTEXTUAL SOURCE REVIEW IMPROVED; **NO PROMOTION**, **NO CLOSURE**, **NO additional NF frontier**. Revisit only if a bound involving the current original unfitted physical response is available or a reproducibility inconsistency arises. This note is itself evidence custody, not a mathematical theorem.
