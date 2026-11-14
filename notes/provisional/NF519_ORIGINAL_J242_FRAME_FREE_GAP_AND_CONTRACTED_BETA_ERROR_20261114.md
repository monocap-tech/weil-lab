# NF519 — Frame-free original J242 Fredholm gap and certified physical-frame error budgets

**2026-11-14 PT. ORIGINAL NF505/NF518 SHA-pinned exact Fraction local PASS; independent original raw pointwise evaluator PASS; synthetic big-dyadic contractor arithmetic PASS. Dedicated GitHub focused CI not accepted.** Stacked on NF518 draft PR #547; no merge to main. **The actual original historical D matrix has NOT been reconstructed, the full original physical-cell residuals e_H are NOT interval-certified, and the kernel gaps are NOT interval-certified.** No named physical NF404 sign, Weil multiplier image/domain, W-ODD-NEG or RH promotion.

## Prior mathematical and source standing

NF517 established the exact localized Schur/Fredholm gain
\[
R(O)-R(O\setminus H)=\langle r_H,(I-\mathcal K_H)^{-1}r_H\rangle,
\qquad \mathcal K_H(x,y)=J(x)^T G_O^{-1}J(y).
\]
Its 550-digit source-grounded numerical scout suggested \(e_H\sim10^{-27}\) and positive gaps, but with no rigorous quadrature/source interval receipt.

NF518 subsequently SOURCE-certified the entire authentic original 242D exterior Galerkin coefficient vector in the historical original D frame, with \(\|a_O-a_*\|_\infty<2\times10^{-84}\), \(\|P_J^OW-(JD)^Ta_*\|_{L^2(O)}<5\times10^{-83}\), and squared residual coefficient-only uncertainty \(<2\times10^{-93}\) on **every** measurable original physical patch \(H\subseteq O\). The exact NF518 source input receipt raw SHA256 is \`926f8d00d28212f542351760e0c1d814413e8a36a3367d6a58bf837c53865438\`, itself pinned to original 4096-bit NF505 source SHA256 \`ad4afeaa4c7d8f48dfc270c437362287d8e2a21d9cce5b385c071e358431d2ec\`. Historic D-frame SHA256 \`18ac01bba4de7ec432e419db5ed990fbfabad91c10cbcf2f61cf5666e36b430e\`.

The NF518 coefficient result left an excessively strong-looking engineering instruction: reconstruct the full exact original 4096-bit historical D matrix bit-for-bit before any original named-cell physical or kernel-gap result. NF519 derives **strictly weaker, independently source-exact acceptance conditions** that still suffice.

## NEW source-certified quantitative frame-sensitivity theorem

Use the actual authentic original 242 selected raw physical functions \(J=(j_i)\) on \(O=[-549/500,549/500]\), including the genuine \(j_{241}(x)=\sinh(x/2)\). For the 241 genuine original \(x^k\sin(2\pi f x)\) or \(x^k\cos(2\pi f x)\) generators, \(|j_i(x)|\le B^k\) with \(B=549/500\); for the pole, source-exact positive rational hyperbolic Taylor gives \(\max_O|\sinh(x/2)|<3/5\). Actual original source selected node list and order are SHA-pinned and checked, not synthesized.

Therefore
\[
\boxed{
\sum_{i=0}^{241}\|j_i\|_{L^2(O)}^2
\le 2B\sum_{i<241}B^{2k_i}+2B(3/5)^2
<830.
}
\]
All inequalities are exact rational consequences of the original source basis.

The authentic fully 242D NF518 fixed rational selected coefficient trial \(a_*\) satisfies, **on its actual original source numbers**,
\[
\boxed{\|a_*\|_1=4.109339813897201\ldots\times10^{-8}<5\times10^{-8}.}
\]

Let \(\widetilde D\) be ANY proposed 242×242 approximation to the **same authentic old source frame D**, and suppose a future rigorous source/frame certificate proves
\[
\boxed{\max_{i,j}|\widetilde D_{ij}-D_{ij}|\le10^{-14}.}
\]
No exact dyadic-mantissa equality is needed for the error bound: **a certified absolute entrywise error is sufficient**. For the resulting physical trial \(\widetilde p(x)=J(x)^T\widetilde D a_*\),
\[
\|J(\widetilde D-D)a_*\|_{L^2(O)}
\le \sqrt{830}\sqrt{242}\,\|\widetilde D-D\|_{\max}\|a_*\|_1
<450\cdot10^{-14}\cdot5\times10^{-8}=2.25\times10^{-19}.
\]
Add NF518's already certified source coefficient error \(<5\times10^{-83}\). Since the actual original global exterior true residual obeys \(\|W-P_J^OW\|_{L^2(O)}<1.3\times10^{-11}\), exact polarization gives **uniformly on every measurable original physical \(H\subseteq O\)**:
\[
\boxed{
\left|\|W-\widetilde p\|_{L^2(H)}^2-
\|W-P_J^OW\|_{L^2(H)}^2\right|
<6\times10^{-30}.
}
\]

This is a **conditionally available, source-certified rigorous error budget**. It does **not** assert that the original D has already been reconstructed to \(10^{-14}\). Rather, NF519 proves that the full 242×242 frame recovery need only meet this absolute accuracy—not exact 4096-bit bitwise equality—to safely transfer localized source-squared residuals at the \(10^{-27}\) scale. The error is roughly two orders below the NF517 target local energy.

### Still better: contract the physical raw beta, not the entire D matrix

Define \(\beta_*=Da_*\in\mathbb R^{242}\), and let \(\widetilde\beta\) be a proposed approximate **raw physical coefficient vector**. The single scalar error fee
\[
\varepsilon_\beta=
\sum_{i<241}B^{k_i}|\widetilde\beta_i-\beta_{*,i}|
+\frac35|\widetilde\beta_{241}-\beta_{*,241}|
\]
controls the entire physical function. If a source-authenticated interval evaluation proves
\[
\boxed{\varepsilon_\beta\le10^{-19},}
\]
then
\[
\|\widetilde p-(JD)^Ta_*\|_{L^2(O)}
\le\sqrt{2B}\,\varepsilon_\beta
<\tfrac32\times10^{-19},
\]
and after adding NF518's authentic source coefficient fee:
\[
\boxed{
\left|\|W-\widetilde p\|_{L^2(H)}^2-
\|W-P_J^OW\|_{L^2(H)}^2\right|
<4\times10^{-30}
}
\]
**for every original physical \(H\subset O\)**.

This reduces the physical acceptance to **242 correlated raw coefficients**, not independent interval quadrature of 242 mixed moments or production/reverification of all 58,564 exact original D entries. The actual source raw-beta weighted error is **not yet verified**, but its explicitly scoped threshold is.

A separate NF519 exact-integer source acceptor \`scripts/local_replay/verify_nf519_sha_authenticated_D_raw_beta_exact.py\` provides an additional reproducible option: given an externally recovered original 242×242 D in exact \`[mantissa, exponent]\` dyadic JSON, it checks the **original exact historic SHA** using the *same ordered byte-by-byte serialization* as the original RPB108 frame generator, then calculates the full \(\beta_*=Da_*\) with exact integers and rounds to \(10^{80}\), paying all weighted raw errors without Arb or floating point. This real-source acceptance path remains **UNRUN** because the original serialized D matrix has not been made available; only its synthetic huge-dyadic arithmetic selftest passed. The historical D SHA, original frame and all 242 genuine source generators remain unchanged.

## NEW frame-independent spectral-gap equivalence

The kernel gap is a property of the **original selected subspace**, not of its arbitrary basis. With
\[
G_O=\int_O JJ^T,\quad
G_{O\setminus H}=\int_{O\setminus H}JJ^T,\quad
\delta_H=1-\|\mathcal K_H\|_{\rm op},
\]
for any \(0<g<1\), the exact source-independent matrix implication is
\[
\boxed{
\delta_H\ge g
\quad\Longleftrightarrow\quad
G_{O\setminus H}-gG_O\succeq0.
}
\]

**Proof.** The nonzero spectrum of \(\mathcal K_H=T_H^*G_O^{-1}T_H\) equals the spectrum of \(G_O^{-1/2}C_HG_O^{-1/2}\), where \(C_H=G_O-G_{O\setminus H}\). The stated gap is equivalent to \(I-G_O^{-1/2}C_HG_O^{-1/2}\succeq gI\), and congruence by \(G_O^{1/2}\) gives the claimed inequality. Under ANY invertible original selected change of coordinates \(J\mapsto T^TJ\), the two source matrices transform by the same congruence \(G\mapsto T^TGT\), preserving the inequality and exact physical kernel. **The historical D SHA is not needed at all to certify the kernel spectral gap.**

Original 242-generator raw physical Gram interval integration at the three original patch endpoints is therefore sufficient. A source-native preconditioner may be used to control conditioning, but that preconditioner does **not** need to reproduce the original historical D bit-for-bit for this **frame-invariant** gap obligation. Its positivity proof must still rigorously pay the matrix source/rounding error; no 550-digit midpoint eigenvalue is accepted.

The primary exact script checks **15 distinct finite-dimensional odd polynomial controls** using exact rational Grams, drastic source frame shears of \(10^{30}\) and \(10^{42}\), generalized gap PSD certificates, and equality of each local kernel entry across coordinate changes; some tested trace leverages exceed one. All PASS.

## Exact remaining original NF517 conditional no-go gates

Under either NF519 original frame or beta transport fee above, these are sufficient **IF** future original source-native independent intervals establish both the specified local trial e upper and true frame-free kernel gap:

| Original physical H | Future true source-enclosed trial \(e_H^{\rm trial}\) upper | Future true frame-invariant kernel gap lower | NF519 result **IF BOTH HOLD** |
| --- | ---: | ---: | --- |
| \(H_{4094}\) | \(9.9\times10^{-28}\) | \(2/5\) | Fixed NF404 physical NO-GO |
| \(H_{4095}\) | \(9.9\times10^{-28}\) | \(1/1000\) | Fixed NF404 physical NO-GO |
| \(H_{4094}\cup H_{4095}\) | \(2.9\times10^{-27}\) | \(1/20000\) | Fixed NF404 physical NO-GO |

The exact original NF505 source residual lower, original unchanged NF404 gamma², and BOTH possible transport fees prove strict resulting inequalities. This is **not an unconditional named-cell result**; the actual original local e and gap are STILL UNCOMPUTED AS RIGOROUS INTERVALS. The 550-digit NF517 scout happens to lie below these trial thresholds, but that is not an acceptance argument.

## Verification custody and limitations

Primary full source-exact script \`verify_nf519_original_selected_frame_and_gap_gates_exact.py\`: actual immutable original NF505 SHA, NF518 SHA and 242 integer trial coordinates; hyperbolic pole bound paid by rational Taylor; 242 original generator L² trace; 15 exact polynomial frame/shear and Fredholm gap controls; all source-specific conditional support implications. LOCAL PASS.

Independent source-exact script \`verify_nf519_independent_pointwise_frame_gate_exact.py\`: original full 242 raw generator **pointwise L∞ sum** \(<293\), instead of the primary L² Gram trace \(<830\). Thus an independent error propagation path gives the same \(<6\times10^{-30}\) and \(<4\times10^{-30}\) physical-cell squared error acceptance budgets. It SHA-pins the same original source and NF518 receipt, and independently pays original named NF517 rational conditions. LOCAL PASS.

Third \`verify_nf519_sha_authenticated_D_raw_beta_exact.py\`: independent exact dyadic integer physical coefficient contractor and synthetic giant-frame smoke test PASS. The true full original frame is absent, so **original-source beta certification is still OPEN**.

Local primary and independent source receipts SHA256: \`a31dfe3f80a7b5de6ddd498b5aa86dcbb2a88b88d690b99e52420c66016e7947\`, \`2480c544f8a085ddab78cf2bf49bcfeb94ce8aa1d522797fd93b928bb0c86221\`. The full local proof/replay pack \`NF519_frame_independent_gap_and_physical_beta_gates_pack.zip\` includes the executed exact scripts, both receipts, NF518 full 242 coefficient receipt and a README; original ~78MB NF505 input omitted but is available from verified original NF505 Actions run #43352403600 artifact #14004781980. **No new broad GitHub CI workflow is claimed successful**; original source/GitHub CI fanout maintenance remains open.

**Next NF520:** implement and run the genuine original 242D **raw physical coefficient contractor** with a source-certified \(D a_*\) interval, not necessarily full frame reconstruction; use the exact NF519 weighted target \(10^{-19}\). In parallel, source-certify **frame-invariant generalized positive definiteness** \(G_{O\setminus H}-gG_O\succeq0\) for original H4094/H4095/union with the three stated positive rational gaps, using source-native raw analytic Gram integrals and certified preconditioning. Only with a complete local source W-minus-\(\widetilde p\) squared interval and gap positivity can the existing NF517/NF519 exact implication promote a **named physical NF404 no-go**. Weil multiplier image/domain, W-ODD-NEG, whole RH facing even/odd sign and RH remain strictly OPEN.
