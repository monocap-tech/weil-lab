# NF518 — Complete original 242D exterior Galerkin coefficient a posteriori, and a universal local residual error budget

**2026-11-14 PT. ORIGINAL SOURCE-EXACT INTEGER LOCAL PASS; independent alternate-scale full source integer replay LOCAL PASS. Dedicated GitHub CI OPEN.** Stacked on NF517 draft PR #546, no merge into main. The full original selected-source local \(e_D\), physical kernel spectral gap \(\delta_D\), unconditional NF404 named physical support result, Weil multiplier image/graph domain, W-ODD-NEG, entire signed Weil even/odd form and RH remain **OPEN**.

## What NF517 established versus what NF518 closes

NF517 established the exact Fredholm/Schur support-liberation identity and source-anchored *conditional* sufficient no-go conditions for the genuine original physical cells \(H_{4094}\), \(H_{4095}\) and their union. A 550-digit real-source full J242 numerical scout suggested local \(e_D\approx 6.94\cdot10^{-28}, 6.13\cdot10^{-28},1.31\cdot10^{-27}\), and \(\delta_D\approx0.429,0.00334,0.0000689\). **These are not rigorous source interval results.** NF517 did not establish the exact historical 4096-bit \(D\) physical frame, source-integral quadrature error, or Fredholm gap.

The present increment closes a distinct major piece: the **complete genuine original exterior selected global-fit coefficient vector in the historical \(D\) frame**.

Let \(N_O=D^\top G_OD\), \(d_O=D^\top b_O\), where the same exact original NF401 dyadic selected physical frame \(D\) is the one SHA-locked into NF505 native, and let

\[
a_O=N_O^{-1}d_O,\qquad p_O(x)=(JD)(x)^\top a_O.
\]

Do not confuse the capital \(D\) original selected frame with a support patch; below we use \(H\subset O\) for the patch. The genuine original selected-space rank is 242 including the pole; no source/basis/projector/gamma replacement is made.

The source archive \`nf504-original-J8-physical-support-saturated-exterior-source-native.json\` is actual original NF505 native 4096-bit source output, SHA256 \`ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec\`. It contains **every** original 242×242 outward Gram box \(N_O\), **all** original outward mixed moments \(d_O\), its source residual \(\mathcal R(O)\), and the historical original \(D\)-frame SHA256 \`18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e\`.

## NEW exact-integer verified full source posterior

**Primary verifier:** \`scripts/local_replay/verify_nf518_original_source_242D_posterior_fit_exact.py\`. The locally executed companion \`verify_nf518_original_242D_a_posteriori_coefficients.py\` uses identical exact matrix/source acceptance inequalities and emits the complete 242-vector, with all 242 rational trial coefficients serialized as integers over \(10^{105}\).

1. Read and SHA-pin the original 78MB NF505 raw source, unchanged original NF407 SHA256 \`0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce\`, original NF406 prime seams SHA256 \`c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675\`, all source 242 Gram/moment intervals and original historic \(D\) SHA.
2. Quantize original \(N_O\) at exact integer scale \(10^{120}\) with each individual original Gram interval fee \(<2\cdot10^{-120}\). Enclose every genuine source \(d_O\) interval with its **actual** independent full-width error. The maximal original-source mixed-moment quantization/error fee is approximately \(2.446186271509085\times10^{-94}\), which is **not rounded away**.
3. Generate an untrusted binary64 inverse candidate at integer scale \(10^{35}\), and independently certify it with exact integer 242×242 multiplication against an \(N_O\) quantization at \(10^{70}\). The Neumann residual and **complete exact row-sum inverse estimate** pass strictly:
\[
\boxed{\|I-N_O B\|_\infty <5.194\times10^{-6}<1,\quad
\|N_O^{-1}\|_\infty <8.022697\times10^9<9\times10^9.}
\]
The displayed decimals merely abbreviate exact rational checked values. They are **not** floating-point acceptance conditions. This independently reproduces the NF506 kind of source inverse verification in a new efficient fully vectorized exact-integer operation, without relying on the old NF506 receipt.
4. Generate a 242-vector trial from a binary64 seed and apply exact-big-integer fixed-point preconditioned residual refinement until its trial integer corrections vanish; no high-precision floating solve enters acceptance. The 242 trial coordinates have common exact rational denominator \(10^{105}\). The independent original source moment/Gram normal-equation residual, **including every input interval fee**, obeys
\[
\boxed{
\|d_O-N_Oa_*\|_\infty<2.446187\times10^{-94}.
}
\]
5. By the rigorous source inverse inequality,
\[
\boxed{
\|a_O-a_*\|_\infty
\le\|N_O^{-1}\|_\infty \|d_O-N_Oa_*\|_\infty
<1.962502\times10^{-84}<2\times10^{-84}.
}
\]
This is a **complete original 242D, source-certified, historical-\(D\)-coordinate Galerkin fit**. It is not merely a 23D/rank-one selected witness or a numerical conditioning guess.

### Independent original-source re-evaluation

The second script \`scripts/local_replay/verify_nf518_independent_242D_source_posterior_exact.py\` uses **different** original source Gram/moment integer scale \(10^{125}\), a new independent 242×242 inverse test with Gram scale \(10^{68}\) and inverse trial scale \(10^{38}\), and recomputes the residual of the primary's **fixed** 242-vector against the full original NF505 source boxes. Its independent exact Neumann bound is approximately \(3.556309\times10^{-6}\), independent full source inverse bound approximately \(8.022688037\times10^9\), and the independently certified maximum original 242-vector error is \(<1.962500\times10^{-84}<2\times10^{-84}\). All exact arithmetic assertions **PASS locally**, without using the primary inverse/trial residual. This is independent *posterior auditing of the archived original source intervals*, not independent reintegration of the original 242×242 physical Gram.

## NEW universal physical local residual error certificate

This supplies more than a global coefficient norm.

From the **actual** source-certified archived original exterior Gram,
\[
\sum_{i,j=1}^{242}|(N_O)_{ij}|<443.
\]

Thus with \(a_*\) the fixed rational 242-vector above, \(p_*(x)=(JD)(x)^\top a_*\), and \(\eta=\|a_O-a_*\|_\infty\),

\[
\|p_O-p_*\|_{L^2(O)}^2
=(a_O-a_*)^\top N_O(a_O-a_*)
\le 443\eta^2.
\]

The exact rational comparison proves

\[
\boxed{\|p_O-p_*\|_{L^2(O)}<5\times10^{-83}.}
\]

Crucially, this bound **automatically holds on every interior measurable physical patch** \(H\subset O\), without requiring any new cell quadrature or separately rounded 242 raw local moments.

The original NF505 already source-certified the whole exterior residual energy \(0<\mathcal R(O)<1.6060\times10^{-22}\), hence \(\|W-p_O\|_{L^2(O)}<1.3\times10^{-11}\). The polarization/triangle inequality now yields, uniformly for **every** \(H\subset O\),

\[
\begin{aligned}
\big|\|W-p_*\|^2_{L^2(H)}-\|W-p_O\|^2_{L^2(H)}\big|
&\le 2\|W-p_O\|_O\|p_O-p_*\|_O+\|p_O-p_*\|_O^2\\
&<\boxed{2\times10^{-93}.}
\end{aligned}
\]

This error is from **original global Galerkin coefficient uncertainty only**. It is far below the NF517 full J242 local residual numerical-scour scale \(10^{-27}\), by more than 66 decimal orders. It means the archived original 242D source moment uncertainty and normal-equation inversion are **not** what blocks physical cell certification here.

**Important limitation:** This does **not** mean \(\|W-p_*\|^2_H\) itself is source-certified. The huge original raw selected frame \(D\) has NOT been reconstituted in original exact 4096-bit dyadic form; the complete fitted physical \(p_*(x)\), original W-subtracted local residual quadrature and local true restricted kernel gap \(\delta_H\) still lack outward envelopes. A 550-digit numerical source scout is not an acceptable substitute. The universal \(2\times10^{-93}\) bound applies **only after** a new original physical source evaluator certifies the trial local energy.

## Standing and acceptance target

| Obligation | Standing |
| --- | --- |
| Actual original 242D exterior \(N_O,d_O\), old NF505 | SOURCE ORIGINAL SHA PINNED |
| New exact 242D inverse and Galerkin trial posterior | **LOCAL EXACT PASS** |
| Independent alternate-scale exact 242D inverse/coefficients | **LOCAL EXACT PASS** |
| All 242 historic-\(D\)-coordinate errors \(<2\times10^{-84}\) | **SOURCE-CERTIFIED LOCAL PASS** |
| Any-cell fitted squared residual coefficient-only uncertainty \(<2\times10^{-93}\) | **SOURCE-CERTIFIED LOCAL PASS** |
| Entire original \(D\) raw 242×242 frame numerical/remainder reconstruction | OPEN |
| Original true \(H_{4094},H_{4095}\), union complete \(e_H\) physical source enclosures | OPEN |
| Actual original restricted Fredholm kernel \(\delta_H\) source enclosures | OPEN |
| Unconditional named physical NF404 support NO-GO | OPEN |
| Weil multiplier image/graph-domain, W-ODD-NEG, full signed Weil, RH | OPEN |
| Dedicated GitHub CI | OPEN; no main merge |

Local proof pack: \`NF518_original_source_242D_Galerkin_posterior_exact_pack.zip\`, containing both fully executed source-independent exact posterior verifiers, their complete 242-vector source receipts and checksum README. It intentionally omits the original ~78MB NF505 native source, which remains pinned to original successful Actions run #43352403600, artifact #14004781980. Local proof checksums:
- Primary verifier SHA256 \`f525ac76878367d558d528e006cf9d9d1c96ebb4bac9bd4263225a9d0be1eddf\`.
- Primary output SHA256 \`926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438\`.
- Independent verifier SHA256 \`ad845f06c9a287694f4d1373553609d1f1e9aa45fc59b7e79ae2e64e0f47c7ce\`.
- Independent output SHA256 \`6791b52960e19c64c665c805de610a8d88951c5ad1ac04917d0f19d652572728\`.

**Next NF519 bold:** Recover and certify original historic exact 4096-bit physical \(D\) selected frame (preserving its SHA) and its complete locally contracted \(p_*\) at authentic H4094/H4095, with W correlation retained. Then rigorously enclose \(e_H^{(*)}\); add the already source-certified coefficient fee \(<2\times10^{-93}\); separately validate the selected local Fredholm spectral gaps required by NF517, especially \(>1/20000\) for union. If the frame cannot be reconstructed under current CI/Arb constraints, record that precise environment/condition obstruction rather than promoting a 550-digit midpoint scout. Whole original Weil/RH remain OPEN.
