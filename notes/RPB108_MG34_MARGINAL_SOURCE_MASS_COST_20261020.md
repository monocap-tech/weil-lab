## Verified original MG34 marginal numbers

[Actions #39467773045](https://github.com/monocap-tech/weil-lab/actions/runs/39467773045) **PASSED** the exact-Fraction marginal conservation across all four true original rational B/cutoff cases, including independent no-spectral-promotion CI. Artifact `mg34-original-marginal-frequency-cost-audit`, ID `12286225566`.

| True original B / cutoff | Sector just measured | Added joint residual UPPER trace | Δ omitted-frequency UPPER trace | Δ complete Rupper trace | Δ strict Gershgorin lower margin |
|---|---|---:|---:|---:|---:|
| scalar / 2^12 | [4,8] 32 cells | +5.02576717 | +0.70225310 | **+5.72802027** | **-0.58214127** |
| scalar / 2^12 | 2 MG19 sites | +0.04259633 | -0.05395745 | **-0.01136112** | **-0.00012983** |
| nonscalar / 2^12 | [4,8] 32 cells | +5.24287830 | +0.74812461 | **+5.99100291** | **-0.31488002** |
| nonscalar / 2^12 | 2 MG19 sites | +0.04158798 | -0.05818375 | **-0.01659577** | **-0.00019734** |
| scalar / 2^16 | [4,8] 32 cells | +5.02576762 | +0.70225310 | **+5.72802072** | **-0.58214138** |
| scalar / 2^16 | 2 MG19 sites | +0.04259632 | -0.05395745 | **-0.01136113** | **-0.00012983** |
| nonscalar / 2^16 | [4,8] 32 cells | +5.21735835 | +0.75160897 | **+5.96896732** | **-0.31587328** |
| nonscalar / 2^16 | 2 MG19 sites | +0.04165453 | -0.05848638 | **-0.01683184** | **-0.00020678** |

All lines are derived by exact rational subtraction from the **previously verified original MG33 all-frequency bounds**, not by projecting floating values from incomplete Fourier integrals. The new [4,8] full original source joint residual bound has a >5 trace cost, *and* the conservative upper for the now-smaller omitted set increases by ~0.70–0.75. The source-mass Young lower is not guaranteed PSD, so this complement phenomenon is compatible with mathematically positive physical source mass.

The two MG19 nonflat sites contribute enough source-mass credit to improve complete trace *slightly*, but the resulting 24D strict Gershgorin margin becomes *worse*. There is **no scalar or nonscalar positive contraction**. The obvious next method must separately address the indefinite source-mass lower budget and the added-measured-band residual error; do not claim broad source-frequency coverage is an improvement simply because it measures more frequencies.

No actual operator eigenvalues, negative modes or original 470D RH gate have been established.

---

# MG34 — Exact marginal frequency costs and the PSD mass-credit gate

October 20, 2026. Stacked on [MG33 PR #282](https://github.com/monocap-tech/weil-lab/pull/282), whose calculation-bearing original source Actions #39462301107 PASSED but whose nonoverlap frequency expansion worsened original whole-frequency 24D residual upper/margin.

## Formal source identity and acceptance scope

For the actual original SI10 25-generator, MG11 23 boundary-adapted + genuine sinh pole 24D source map F, the directly enclosed joint residual is `R=F-Astar F B`. The original signed seven-prime/digamma multiplier, full real-frequency integral, original pole covariance, and SM41 high tails are inherited from accepted MG33; no surrogate system appears here.

For a fixed original rational trial B and two *disjoint* measured-frequency sets C0 included in C1, MG33 had the same original true residual upper `U_C0+U_remaining(C0)` and new upper `U_C1+U_remaining(C1)`. Even though the actual unmeasured set becomes smaller, independently enclosing its original source covariance by `Hupper-Hmeasured_lower` need not improve, because the sourcewise-Young **Loewner lower** may have large negative directions. It remains a valid lower, but subtracting it can enlarge the upper bound. This is a numerical estimation artifact, NOT a negative actual source mass.

## Exact marginal decomposition

On each of the four original cutoff/scalar-nonscalar trials from the successful pinned MG33 artifact, compare the same source response B on three complete real-frequency certificates:
(1) accepted MG32 [0,4],
(2) MG33 contiguous [0,8],
(3) MG33 [0,8] + the two certified original MG19 nonflat cells with left>=8.

Exactly, in rational arithmetic, for both successive steps:

```
Δ total complete Rupper TRACE
 = added measured sector joint Rupper TRACE
 + Δ remaining original frequency Rupper TRACE.
```

The measured sector and complement contributions are separately enclosed Loewner upper traces. Independently report the signed difference in the original complete (Hlo-Rupper) source Gershgorin lower margin. These are different orderings: a lower trace does NOT imply that the 24D matrix is larger in Loewner order or that its Gershgorin margin improves.

The audit must reproduce MG33's *entire* original 4-case 3-variant rational trace and signed-Gershgorin conservation with no rounding approximation.

## Numerical diagnosis already visible in MG33

At k=12 and scalar tI, the added real [4,8] measured source-residual upper trace increases by exactly the audited measured-band upper-trace contribution 5.025767165864... (scalar, k=12), and the omitted-frequency UPPER trace **increases** from ~37.9574 to ~38.6597 despite a smaller omitted set. The resulting full residual upper trace rises from ~63.5047 to ~69.2328 and its Gershgorin margin becomes more negative. The two additional MG19 cells lower the total hybrid upper trace by ~0.01136 compared with contiguous [0,8], but worsen the Gershgorin margin by ~0.00013. Neither strictly certifies positive residual.

Do not present these differences as actual source mass, actual residual energy, true signed spectral eigenvalues, or distances to RH.

## Next method-selection acceptance

**MG35:** replace naive negative Loewner source-mass credit by a rigorously **PSD-safe** covariance credit or a structure-preserving direct joint bound for the unmeasured frequencies. Independently audit the true nonflat source/cell Fourier intervals and avoid spending substantial time extending more bands before measuring marginal benefit and source-trace loss. To obtain a genuine 24D contraction, certify strict positivity of the whole-original-frequency source residual difference; to advance W-ODD-NEG, separately prove the full true 470-source strong inverse and signed 51/56 cap. No source-space invariant extension is yet proved.

Canonical W-ODD-NEG, complete even/Weil/CC27/RH and independent original Fourier/form/domain verification remain OPEN.

**Actions acceptance: PASSED, exact marginal method diagnosis only.**
