# Weil-Lab — CP028
## Coarse finite original (A_{6,256}) boxes and exact Hardy-(Z) error slack: a smaller, falsifiable numerical-to-Lean interface

**Independent CP### source track.** Stacked on CP027 draft PR #849 → CP026 #848 → CP025 #847 → CP024 #846 → CP023 #845. No source changes to Phase IV original signed Weil support-extension, Phase III NF physical numerical certification, or independent PI### prime/pole/Gamma work.

**Precise acceptance status:** A mathematically exact rational **implication** has been checked externally. The user-supplied CP025 directed-interval receipt independently passes the new **coarse-box rational consistency check**. Two new grouped finite box obligations appear as hypotheses of four CP028 Lean source theorem CANDIDATES. This is **not** a genuine original Lean4.35 compile; the original finite numerical boxes, pointwise Borwein source lemmas, and full chain have **no new kernel acceptance**. No RH, global signed Weil positivity, entire spectral (3\times3) dictionary, zero ordinal #53, or uniqueness claim.

### 1. CP027 has reduced the task to numerical finite signs, but they need not be 55-digit goals

The actual original published `zetaApproximant` is

[
A_{6,256}(s)
=\sum_{n=1}^{255}n^{-s}
+\frac{256^{1-s}}{s-1}
+\tfrac12 256^{-s}
+\sum_{k=1}^6 \frac{B_{2k}}{(2k)!}(s)_{2k-1}256^{-s-(2k-1)}.
]

This exact original source finite approximant, NOT the alternative Riemann–Siegel 52-term approximation, was evaluated by CP025's actual (10^{55})-fixed integer outward interval engine.

Use (s_t=1/2+it), true rational heights (t_L=150.05352), (t_R=150.05353) and published genuine theta-Stirling (\widetilde\theta_{2,0}). Put

[
\widetilde Z_A(t)=\Re\left[e^{i\widetilde\theta_{2,0}(t)}A_{6,256}(s_t)\right].
]

CP026's true original-Hardy-(Z) comparison (conditional local Lean source candidate) uses

[
E(t)=\frac{12}{t^4}|A_{6,256}(s_t)|+\frac3{10^{13}}.
]

The first error component is the **genuine published original theta-Stirling theorem**, the second requires the NEW original CP027 center-point Borwein source theorem to compile. There is **no differentiated scalar error inequality** anywhere in this sign/zero existence route.

### 2. New exact rational budget: theta and Borwein error smaller than (10^{-10})

Since both original endpoints satisfy (t\ge150), if the genuine finite source satisfies just (\|A_{6,256}(s_t)\|\le1/1000) then simple exact positive arithmetic gives

[
\begin{aligned}
E(t)
&\le\frac{12}{150^4}\frac1{1000}+\frac3{10^{13}}\\
&=\boxed{\frac{6481}{270000000000000}}\\
&\approx2.4003703703703704\times10^{-11}
<\frac1{10^{10}}.
\end{aligned}
]

This is a completely exact rational fact; negative controls rule out a fictitious (10^{-11}) error cap.

Therefore the **two** original finite-sign lemmas, which formerly appeared as opaque transcendental inequalities, follow from two much simpler **grouped boxes**:

[
\boxed{
\begin{cases}
\|A_{6,256}(s_{t_L})\|\le10^{-3},\\
\widetilde Z_A(t_L)<-10^{-7},
\end{cases}}
qquad
\boxed{
\begin{cases}
\|A_{6,256}(s_{t_R})\|\le10^{-3},\\
\widetilde Z_A(t_R)>10^{-7}.
\end{cases}}
]

Indeed (10^{-7}-10^{-10}>0): each finite sign has strictly more than 1000× slack against the *conservatively rounded error ceiling*, and over 4100× slack against the exact (6481/270000000000000) error bound. This is no longer a task of proving transcendental values to fifty decimal places; an interval arithmetic kernel certificate can target much coarser rational boxes.

**These four component inequalities have not yet been attached to the original Lean definitions by kernel-checked interval arithmetic.** Two grouped box hypotheses are easier interfaces; grouping does not magically pay them.

### 3. A concrete exact external crosscheck of the actual user CP025 receipt

The original uploaded user receipt at `/mnt/data/cp025_external_interval_preflight.json` is SHA-256

`09c7b1935df3c19c7393a6e34ad47d7095206a1fd184fe498e67c8796795f8ec`.

It contains the exact rational finite-phase intervals and the original symmetric outward error intervals for both source heights, with the source error rule used by CP025:

[
Z_{mathrm{lower}}=\widetilde Z_{A,\mathrm{lower}}
-(\delta_\theta\,A_{\mathrm{norm,upper}}+R_{\mathrm{cap}}),
]

[
Z_{mathrm{upper}}=\widetilde Z_{A,\mathrm{upper}}
+(\delta_\theta\,A_{\mathrm{norm,upper}}+R_{\mathrm{cap}}).
]

The source-published (\delta_\theta=12/t^4) and candidate (R_{\mathrm{cap}}=3/10^{13}) are both explicit rational receipt fields. The exact equality of the two reconstructed error widths and their subtraction/inversion give the **exact original outward-norm upper already encoded in that receipt**, not a new approximate norm guess:

| Original height | Encoded original `A.normup()`, numerical preview | Finite rotated real, preview | CP028 coarse box |
|---|---:|---:|---|
| (t_L=150.05352) | (6.817408670122472\cdot10^{-7}) | (-6.817408670122472\cdot10^{-7}) | 2/2 external PASS |
| (t_R=150.05353) | (1.5519759813026856\cdot10^{-5}) | (+1.5519759813026856\cdot10^{-5}) | 2/2 external PASS |

All comparisons were executed in the local container with Python `fractions.Fraction` **on the exact uploaded rational strings**, including checking each original rational height, the published theta cap, the exact symmetrically stored CP025 error rule, the positive original source remainder cap, the inferred outward norm against (1/1000), and the signed finite interval endpoints against (\pm10^{-7}).

**Critical trust distinction:** This was a **receipt-structure consistency audit**. It reconstructs the original CP025 engine's bound from its own stored directed endpoints, but is not *by itself* an independent execution of the full 255+6 term calculation or a Lean certificate. CP026 previously ran the full directed engine and compared all 26 exact fields; CP028 has added a separate optional comparison between the uploaded receipt and a **fresh** CP025 engine replay, to detect drift if run. The new CP028 full replay workflow has NOT been dispatched.

The concrete verified local output is:

`/mnt/data/cp028_coarse_original_finite_box_reconciliation_NOT_LEAN.json`

It records the original CP025 source SHA-256, both exact unreduced rational point values and recovered norms, the exact rational phase/remainder budget (6481/270000000000000), and explicit false new-Lean/spectral/RH acceptance flags. It is NOT a kernel receipt.

### 4. Original Lean source attachment and trust boundary

New `cp011_zeta_v435/CP028CoarseFiniteBoxes.lean` imports the exact **conditional** CP027 original narrow-root bridge. It defines two explicit `Prop` interfaces, `FiniteLeftBox` and `FiniteRightBox`, with one norm bound and one strict finite signed inequality each. It adds exactly **four** original source proof CANDIDATES with explicit `#print axioms`:

1. `sourcePointError_lt_ten_billionth` proves pure rational error transfer whenever (t\ge150) and actual original `‖sourceA t‖≤10^{-3}).
2. `original_left_finite_sign_of_coarse_box` gives CP027/26's true left finite sign conditional on the actual left box.
3. `original_right_finite_sign_of_coarse_box` gives the right finite sign conditional on the right box.
4. `original_narrow_zero_of_two_coarse_boxes` supplies those two signs to CP027's original published-HardyZ IVT bridge, yielding an **original zeta critical-line zero in the open narrow bracket, but only conditional on the TWO UNPAID genuine source finite boxes**, on original CP027 pointwise Borwein and all imported Lean proofs compiling.

No numerical value from the user-provided JSON was introduced as a Lean fact, new axiom, `sorry`, or `opaque`. The new Lean source compiles **after** original CP027 and CP026; this is intentionally a small integration theorem, not an independent upstream-only kernel leaf. It has **not** been run through the v4.35 compiler; no `.olean` exists in our custody, and source tactics may require repair.

New `scripts/cp028_original_coarse_finite_boxes_source_gate.py` has:
- Exact `Fraction` scalar error/margin and negative controls.
- Re-execution of CP025's **true original 255+6** 10^55 integer outward engine, including `original_A_and_Ds(t)` complex norm upper and `enclosure(t)` strict finite signed rational bounds, and fail-closed coarse box checks. This full engine path is **COMMITTED and opt-in**, but **not executed in this turn**.
- Optional `--uploaded-cp025` crosscheck of the exact user receipt's original centered 255-term finite phase and norm, optionally against a newly computed fresh engine result.
- Source theorem names, four genuine `#print axioms`, no new admissions, actual original Lake v4.35 target and the same two CP027 grouped box hypotheses.
- Separate fail-closed actual `.olean` + four real standard-only axiom log acceptance gate. **No numerical source-only receipt claims kernel acceptance.**

The existing genuine original v4.35 `lakefile.toml` registers `CP028CoarseFiniteBoxes`. The SAME existing label/manual source-only workflow now includes a CP028 exact finite-box replay and explicitly NOT-LEAN JSON. The SAME existing label/manual Lean kernel workflow compiles CP028 **after** CP027 and checks its four genuine axiom logs. **No new workflow file, no ordinary push/PR-created/synchronize fan-out and no opt-in CP028 job dispatched.**

### 5. Honest remaining proof obligations

The source zero-existence pathway is now:
1. Original published (\zeta=A+R), theta approximation error, Hardy-(Z) continuity, and critical-line zero equivalence already exist in genuine source Lean.
2. CP027 center-point (B_{14}\)/Pochhammer actual zeta remainder bounds are analytically justified and exact-rational preflighted, but new **original v4.35 kernel receipts PENDING**.
3. CP026/CP027/CP028 original narrow root bridges are **Lean source candidates without actual compiler acceptance**.
4. The two finite boxes above are supported by exact external numeric evidence; **the full independently kernel-checkable finite 255-term interval argument is STILL UNPAID**.
5. The original source rank-53 attachment, zero uniqueness/full Hardy-(Z) curvature, spectral-Weil (3\times3) compatibility, global signed Weil positivity and RH remain completely separate and OPEN.

**Next CP029:** prioritize one true original v4.35 compiler pass of the **upstream-only CP027 pointwise Borwein leaf** and fix the first real error before stacking further symbolic proof candidates. For the finite boxes, build a **small outward-rational Taylor/phase manifest at approximately 10^-9 precision** that the Lean kernel can evaluate, paying true original (\|A(s_L)\|≤10^{-3}), (\|A(s_R)\|≤10^{-3}) and (\pm10^{-7}) finite rotated sign bounds. The source proof hypotheses must remain explicit until actual `.olean` and standard axiom receipts exist.

**No RH or signed global Weil positivity claim.**
