# Weil-Lab — NF358: the remaining strong residual is outside the four probes

Research status: **read-only local exact-rational replay; no new GitHub PR, no native Arb / GitHub CI acceptance; W-ODD-NEG OPEN**. Original canonical form/domain realization remains open. Fixed selected original 242-dimensional space; four critical directions unchanged.

## Pinning

- PR #355: https://github.com/monocap-tech/weil-lab/pull/355
- Artifact 12776684037; ZIP SHA256 `f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0`.
- Source JSON `original_exterior_scalar_floor_stop.json`: SHA256 `d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9`.
- Local source checker `/mnt/data/nf358_residual_probe_replay.py`, exact results `/mnt/data/nf358_residual_probe_projection.json`.

## What is new

Put `S = E* E` (physical four-probe Gram), `C_E = E* W E`, `Z = E* W Phi`, and use the exact retained dyadic four-probe coefficient matrix `Y_C` from #355. Assuming the inherited strong realization of the original form, define `R=QW(Phi-E Y_C)`, with `P_E=E S^-1 E*` the *physical* orthogonal projector onto the existing exterior probe space.

Then the EXACT identity is

```
E* R = Z-C_E Y_C,
(P_E R)* (P_E R) = (Z-C_E Y_C)* S^-1 (Z-C_E Y_C).
```

The independent rational replay reconstructs `Z` and `C_E` from *all* their dyadic midpoint and radius entries (intervals, not just midpoints) and multiplies them by the retained **exact** `Y_C`. It obtains

```
||Z-C_E Y_C||_F^2 < 2.32572037746132825e-609,
lambda_min(S) > 5.676971221037680405e-213,
||P_E R||_F^2 < 4.096762669577556e-397.
```

These are bounds under the original inherited projection/domain hypotheses. The parent residual upper and its directly recomposed 4x4 native-box upper overlap and differ only in their last printed digits.

The accepted parent four-probe energy-operator bound is

```
g = 0.00191130015923938334... < 1/500.
```

On assuming the locally replayed, still-unmerged stronger exterior floor `mu > 499/50000`, and signed-energy Gram `H_phi >= .99 I`, a slightly sharper sufficient full four-critical-direction certificate would be

```
||R||_F^2 < mu_min * .99 * (1-g)
          = 0.00986131597216668304...
```

This is **not proved**: only `||P_E R||_F^2` was bounded. Therefore the actual remaining criterion is explicitly

```
||(I-P_E)R||_F^2 < 0.00986131597216668... - 4.096762670e-397.
```

The number on the right is a conditional sufficient allowance, NOT an observed full strong residual.

## Conditioning consequence

Because `Phi` lies in selected `J_242` and every column of `E` belongs to `J_242^perp`, for `h=Phi-EY_C` one has `||h_j||^2=||Phi_j||^2+||E(Y_C)_j||^2`. The archived dyadic source coordinates and verified original physical Gram imply `||Phi_3|| > 10^17`. For the stronger-floor scalar completion to pass, it would therefore require the **relative projected strong residual** in this column to be < approximately `10^-18` measured against `||h_3||`. This is a conditioning/precision diagnostic, not a proof that such a residual does or does not exist.

## Decision

The existing four probes are **no longer a useful frontier for controlling `R`**. They almost completely eliminate their *own* component. Only the complete unprobed part `||(I-P_E) QW(Phi-EY_C)||_F` matters for the residual-based sufficient method. That requires new analytic strong-action information: e.g. certified original squared-multiplier action with correlated physical projection cancellation, or an energy-resolved inverse strategy. Simply recomputing `Z`, `C_E`, the existing finite Schur block, or the same four modes at higher precision cannot supply that information.

No finite-probe data has been promoted to a global infinite Schur upper bound. The 238 other selected source directions remain unclosed independently; a four-direction success would not establish W-ODD-NEG or RH.
