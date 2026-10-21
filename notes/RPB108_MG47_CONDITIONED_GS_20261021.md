# MG47 — Independent original whole-minus-measured first/second moments conditioned on the genuine omitted spectrum

October 21, 2026. Stacked on MG46 [PR #295](https://github.com/monocap-tech/weil-lab/pull/295), whose original complete-frequency exact-rational 256-case calculation [Actions #39638393721](https://github.com/monocap-tech/weil-lab/actions/runs/39638393721) and final-head [Actions #39641040044](https://github.com/monocap-tech/weil-lab/actions/runs/39641040044) both PASSED. MG46 retained genuine original first-moment G and second-moment S cross terms over ALL omitted frequencies, strictly improving MG32's old measured-plus-missing sufficient source matrix bounds, but still weaker than MG43's independent whole-frequency source enclosures.

## True original moment subtraction

Keep the same physical SI10 catalog of 25 true generators, MG11 original 23 boundary-adapted + TRUE odd sinh pole 24D source, signed seven-prime/digamma multiplier, and all original real frequencies. Let C=[-4,4] denote the actual 32-cell MG29/MG32 measured positive-frequency prefix plus its negative-frequency reflection and D its omitted complement. The true original unpoled moments satisfy, as genuine SAME-operator identities:

\[
G_{\mathbb R}=G_C+G_D,\quad S_{\mathbb R}=S_C+S_D.
\]

MG29's original Fourier source-affine integration rigorously encloses G_C and S_C, including all 24×24 physical source cross terms:
\[
L_{G_C}\preceq G_C\preceq U_{G_C},\qquad L_{S_C}\preceq S_C.
\]

Two independently accepted COMPLETE-frequency estimates, MG24 and MG29, enclose the SAME original UNPOLED moments, before rank-one sinh-pole algebra:
\[
L_{G,\mathrm{MG24}}\preceq G_{\mathbb R}\preceq U_{G,\mathrm{MG24}},
\quad S_{\mathbb R}\preceq U_{S,\mathrm{MG24}},
\]
\[
L_{G,\mathrm{MG29}}\preceq G_{\mathbb R}\preceq U_{G,\mathrm{MG29}},
\quad S_{\mathbb R}\preceq U_{S,\mathrm{MG29}}.
\]

Therefore, with NO newly assumed Fourier information, actual omitted moments independently obey
\[
L_{G,j}-U_{G_C}\preceq G_D\preceq U_{G,j}-L_{G_C},
\qquad S_D\preceq U_{S,j}-L_{S_C},
\]
for j∈{MG24,MG29}. Also preserve MG46's independently valid positivity/mass multiplier bounds: κ(Hlo-HCup)≤G_D≤M(Hup-HClo)+τ1 I and S_D≤M²(Hup-HClo)+τ2I. All bounds concern the true original same omitted set; any valid pair of lower/upper G and any valid S upper may be used together without assuming the matrices commute. It is NOT valid to invent their entrywise max/min as a Loewner matrix; MG47 never does.

## Full 24D original coupled residual

For every genuine original nonscalar B, C0=I+2 e_p b0ᵀB, and any valid G_D lower/upper L≤G_D≤U and S_D upper V, take E=(U-L)/2≥0, Gc=(U+L)/2. Retain the true omitted-frequency first-moment CROSS terms:
\[
U_{D,\mathrm{base}}=C_0^\mathsf T H_{D,\mathrm{up}} C_0
-C_0^\mathsf T G_c B-B^\mathsf T G_c C_0+B^\mathsf T V B
+\eta C_0^\mathsf T E C_0+\eta^{-1}B^\mathsf T E B.
\]
The MG40 block-PSD covariance lemma certifies the mixed-G fee. The original true pole coefficient error is paid with either MG46's independently justified isotropic or new sourcewise diagonal PSD matrix W:
\[
U_D=(1+\gamma)U_{D,\mathrm{base}}+(1+\gamma^{-1})W.
\]
This is a separately valid true physical omitted-frequency 24×24 LOEWNER covariance upper for EACH parameter combination. Summing exactly once with MG32's accepted original [0,4] full24 direct source residual upper gives a simultaneous full original-frequency residual upper.

There are three independently certified G lower profiles (MG46 mass/κ, MG24 whole-minus-measured, MG29 whole-minus-measured), three G upper profiles, three S upper profiles, two rational η choices (1/4,1), two γ choices (1/4,1) and two physical-pole PSD error profiles, for 3×3×3×2×2×2=216 per scenario, **864** candidates over original 16/32-cell × k12/16 cases. (The executable enumerates its exact array length and fails closed; do not infer acceptance from an unexecuted plan.) To avoid overclaim, the implementation's enumerated grid count and schema are authoritative if this written expectation differs.

Independently, original MG43's full-real-frequency moment residual Loewner upper is valid for the SAME original B/source operator. Thus ANY true convex blend
\[
U_\theta=(1-\theta)U_{\mathrm{MG43}}+\theta(U_C+U_D), \quad \theta\in[0,1],
\]
is itself a valid whole-source Loewner upper, without an unjustified matrix minimum. MG47 checks rational θ∈{0,1/32,1/16,1/8,1/4,1/2,1}, compares MG43, MG46 and MG47 candidate whole matrices, and requires a full exact-rational 24-pivot LDL or a genuine negative rational Rayleigh witness to classify the selected conservative lower matrix. A negative certificate does not imply negativity of the true Weil operator.

## Reconstruction and independent source custody

MG29's archived accepted artifact contains the pole-corrected Gstar/Sstar matrices but intentionally omits intermediate unpoled whole-real G/S matrices and raw measured [0,4] G/S matrices. MG47 RECONSTRUCTS both 16- and 32-cell original source moment integrations using MG29's actual archived formula/third derivative/fourth drift, then verifies exact equality with every archived whole Gstar/Sstar 24D matrix and source trace-width summary before using the reconstructed unpoled moments. The independently written Actions verifier repeats this entire reconstruction without importing MG47's candidate-construction module, recomputes all new full24 matrix candidates/rational signs and replays 12 anchored exact MG45 source rays. Previous source artifacts pinned: MG24 #39378465438, MG29 #39440914565, MG32 #39459624082, MG43 #39522608989, MG45 #39544081287, MG46 #39638393721.

**Scope:** This constructs no new physical Fourier generator measurements and proves no exact full original spectral negative index. Even if a finite source certificate became positive it would NOT prove 470D strong inverse, signed odd 51/56 cap, independent Fourier/form/domain identification, even/Weil/CC27/RH. All remain OPEN.

**Computation-bearing Actions and independent full-matrix replay PENDING.**
