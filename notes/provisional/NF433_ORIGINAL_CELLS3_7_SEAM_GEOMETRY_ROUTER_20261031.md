# Weil-Lab NF433 — Original cells 3 and 7: exact prime-support routing and ellipse feasibility

**2026-10-31 PT.** Original `W-ODD-NEG` canonical OPEN; RH OPEN. Stacked on NF432 draft PR #442, unchanged exact original NF405 physical action, NF406 irrational support seams, NF407 242 selected + 4 critical source dyadics, and original NF404 centering. The NF432 true original continuous signed **cell 6** remains accepted; it does not logically transfer to cells 3 or 7.

## Previous cursor / current circle / next bold

**Previous NF432:** Complete physical original cell6 true signed `D6=4∫p z+2∫z²` is rigorously negative, with `||z-P511||_∞<7e-23`. Seven other positive x cells still OPEN.

**NF433 current:** Independently reconstruct exact NF406 physical original positive cell3 and cell7 prime translate support and establish *which sourcewise Chebyshev ellipses remain valid* before porting any source-native coefficient or image remainder. This is an analytic-boundary/branch gate, NOT a signed integration certificate. A focused [GitHub Actions #41258715260 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41258715260) passes all exact-rational source/branch/geometry checks.

## Original NF405 prime action — both signs matter

The exact physical action retained is

`-Σ_{n∈{2,3,4,5,7,8,9}} (Λ(n)/sqrt(n)) [u4(x+log n)+u4(x-log n)]`, with `u4` supported on `(-B,B)`, `B=11/10`.

For positive x∈(0,B), the **minus translate** `u4(x-log n)` is active iff `x>log n-B`; the **plus translate** `u4(x+log n)` is active iff `x<B-log n`. At a cell's *exact seam*, use the symbolic algebraic identity of the knot label, not a noisy comparison of enclosing rational endpoints; seams themselves are measure-zero for integration. The first attempt's overly strict rational-interval branch test failed at the n2 right seam; the revised script tests exact seam equality first, then strict rational disjointness. This correction is retained in CI history, with no silent data replacement.

| Original positive cell | True open x interval | Minus translates | Plus translates | Neither |
|---|---|---|---|---|
| **3** | `(log 4−B, B−log 2)` | 2,3,4 | **2** | 5,7,8,9 |
| **7** | `(log 8−B, log 9−B)` | 2,3,4,5,7,8 | none | 9 |

This is the crucial difference from cell6's five one-sided translates: cell3 has **two simultaneously active directions for n2**, while cell7 has six one-sided negative-shift terms. Thus an unchanged NF428/NF431 cell6 polynomial formula would be **arithmetically wrong** if applied to cell3 or 7.

## Two source-correlated Chebyshev geometries

Cell 3 is strictly covered by `x=C+Ht`, `C=347/1000`, `H=61/1000`, `t∈[-1,1]`, with genuine original source seams inside `[.286,.408]`. The E2/E3/E4/E5 ellipses stay strictly inside `0<Re x<B`; even E5 has exact rightmost `316/625=.5056`, so distance from the endpoint singularity `B-x` is ≥`743/1250=.5944`.

Cell 7 is strictly covered by `C=1039/1000`, `H=60/1000`, `[.979,1.099]`. The same E2/E3/E4/E5 ellipses CROSS `x=B` and are invalid. Only narrow ellipses, e.g. `rho∈{11/10,9/8,7/6}`, retain strict `Re x<B` with exact endpoint clearances `1/1375,7/12000,1/3500` respectively. This makes naive high-degree geometric decay weak and dramatically reduces the reliable 2048-image decay near the original endpoint.

## Actual original-source frequencywise feasibility test — scoped as candidate, NOT true z certificate

The exact NF407 242+4 dyadic source is recomposed into 273 frequency/order groups (all 32 critical sine modes + original pole) with original raw source triangle below `10^160` and source radius below `10^-700`. For each original source generator, choose the minimal exact rational n≥512 Bernstein-series tail over each geometrically admissible ellipse:

`4e8·|c_{f,k}|·k!·8^k·3^{ceil((2·(22/7) f+1/8) H(rho−rho^{-1})/2 +1)} · rho^{-512}`.

The deliberately larger `1e8` transfer overhead allows cell-dependent prime terms, but this source-generator triangle *by itself* does NOT prove that the full cell's physical regularized digamma+image transfer, both translated n2 prime modes and original endpoint subtraction have been completely reconstructed and revalidated. The original NF432 cell6 finite-image error was certified on the *cell6* real interval, so it must not be inherited automatically.

- **Cell 3** best source-generator tail: approximately **1.2377129705×10^-39**, which is promising for decision-quality with 512 genuinely source-correlated cell3 coefficients, *conditional on* cell-specific original image/pole/end-log and both-sided prime-transfer verification.
- **Cell 7** best source-generator tail: approximately **2.1393216962×10^132**, explicitly useless (not a certified error). Its near-B right support endpoint demands an adaptive reparameterization, more rigorous image resummation, a different aperture collar or much higher mode order, not blind reuse of NF432 degree511.

Do not infer that cell7 has enormous actual error; only this broad sourcewise ellipse triangle is too weak.

## Evidence, standing and next acceptance gates

- Exact original source / NF405 physical support / NF406 seams / complex ellipse and candidate source-tail audit: `scripts/local_replay/nf433_original_cell3_cell7_branch_ellipse_router_exact.py`.
- Focused [Actions #41258715260 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41258715260), source-pinned output artifact #13063434427, ZIP SHA256 `fc8d1576f7fd8c5dc99774cd5df904da9eb1ed5759332976fe0556b73581062e`, expires 2027-01-30.
- Two earlier runs on initial incorrect strict rational seam comparison failed and then were corrected by symbolically matching seam labels. **Do not promote failed preliminary runs.**
- **ACCEPTED:** Exact true original prime-support branch classifications for cells3/7; strict admissible and inadmissible ellipse geometry; exact source-specific triangle comparison establishing a *route* for cell3 and a **method-specific obstruction** for direct cell7 512-mode carryover.
- **OPEN:** Both new original native coefficient sets, source/image remainder bound per respective physical cell, signed principal p moments, original `z²` moments, complete true cell3/cell7 signed integrals, five other positive cells, global `E_p` and NF410/NF404 full centered scalar, original fourth J242 exterior upper, W-ODD-NEG/even/whole Weil/domain/inverse/RH.

**Next NF434:** instantiate and verify original cell3 native *both-sided n2* transfer, with independent source-level physical response and genuine cell3 log-seam endpoint; certify one first correlated coefficient block and the original cell3 2048-image remainder before constructing its signed p and dx moment vectors. In parallel only if needed, design an endpoint-aware cell7 resummation, not unverified NF432 reuse.
