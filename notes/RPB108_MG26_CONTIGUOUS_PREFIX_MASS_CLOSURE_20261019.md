# MG26 — Contiguous original-frequency source moment mass closure (pilot)

October 19, 2026 (LA). Stacked on [MG25 #274](https://github.com/monocap-tech/weil-lab/pull/274), the verified nonscalar 24D source-aware trial **no-go for the currently loose MG24 enclosures**. This MG26 pilot does NOT claim to have finished the full low-frequency integral or the original 470D signed 51/56 gate.

## Why MG24/MG25 were not enough

MG24 successfully bounded the *entire* true original source first and second moments using MG19's 24 tiny nonflat panels for a lower matrix and the entire original physical Gram H with global multiplier M for upper. MG25 applied rationalized nonscalar responses to those exact verified matrices: no tested source-aware trial obtained a certified strict matrix contraction. The recorded defect is the unmeasured-frequency source mass and its unknown correlation, not a negative operator mode.

The conceptual MG26 change: pay the **measured band mass** in H *before* applying a coarse global multiplier bound to the complement. This preserves the physical spectral correlation rather than replacing all unmeasured frequencies by a scalar/entire-H budget.

## Real contiguous original source calculation

Original source map `F: R^24 -> L²` comprises 23 true MG11 double-boundary-vanishing supported sine/xcos generators and original sinh pole s. The full physical Gram `H=F*F` is independently reconstructed from the original 25 SI10 interval Gram.

On the exact full, **contiguous** positive-frequency prefix `C=[0,4]`, with the negative real Fourier frequencies included by factor 2, make two independent rational equal-length partitions: 8 cells and 16 cells. No skipped frequency in this prefix. Each source transform on each whole real cell is enclosed as

```
T(xi)=v+d(xi-mid)+e(xi),   |e_i|<=r_i,
```

with original Fourier value/derivative/second-derivative Taylor bounds, including both boundary-cancellation corrections and the original pole. Independently enclose the **actual signed seven-prime+digamma** original positive multiplier with SM43 on the entire cell `l<=a_o(xi)<=u`, including possible max-kappa crossing.

A true-source Young matrix bound with exact rational tau and every mixed source covariance now encloses three distinct 24x24 matrices on C:

```
H_C = int_C T*T        (unweighted source Fourier mass)
G_C = int_C a_o T*T    (first positive moment)
S_C = int_C a_o² T*T   (second positive moment)
```

with both frequency signs. For *each* cell, choose the best of seven independently valid sourcewise-Young tau values by the lower **trace** (not by a spurious Loewner total order). An exact symmetric rational aggregation rounds only after proving the source and multiplier whole-cell inequalities.

Unlike MG19's selected panels, these are a true **partition of [0,4]**. It remains a prefix pilot: frequencies `(4,4096]` or `(4,65536]` are not individually integrated yet.

## Full-original-frequency mass closure

The actual original full source Gram satisfies `H=H_C+H_R`, where `H_R>=0` is the exact Fourier mass on all omitted real frequencies.

Write certified 24D Loewner intervals `L_C^H<=H_C<=U_C^H`, similarly `L_C^G,U_C^G` and `L_C^S,U_C^S`, and a separate full physical Gram bracket `Hlo<=H<=Hup`. Thus

```
Hlo-U_C^H <= H_R <= Hup-L_C^H.
```

Globally `a_o>=kappa=1/1000`. For cutoff `Lambda=2^k`, `a_o<=M_k=17+k(347/500)` on the entire original low band, including all seven prime terms. SM41 separately provides exact whole-real source Fourier **positive high tails** `tau_G(k),tau_S(k)` on `|xi|>Lambda`. Consequently

```
L_G = L_C^G + kappa (Hlo-U_C^H)
U_G = U_C^G + M_k(Hup-L_C^H) + tau_G(k) I

L_S = L_C^S + kappa²(Hlo-U_C^H)
U_S = U_C^S + M_k²(Hup-L_C^H) + tau_S(k) I.
```

These are *actual whole-original-real-frequency* source Loewner brackets, not truncated-frequency conclusions. `M_k H_R` intentionally overpays positive high-frequency mass; the tau terms charge any excess high-frequency multiplier above M. The true remaining covariance is retained in `H-H_C`, which was absent from the earlier coarse source bounds.

Obtain `c=G_o e_p` by the same MG24 exact Loewner column uncertainty, and enclose

```
Gstar=G_o-2bb*
Sstar=S_o-2(cb*+bc*)+4sigma bb*
```

with original `b=F*s`, `sigma=||s||²`. All mixed pole crosses have their own rigorous rational row-sum fees. The original MG24 true whole-frequency 24x24 Gstar/Sstar brackets provide a comparison point, **not** a license to assert matrix Loewner superiority by trace alone.

## Acceptance

MG26 first produces complete 24x24 source mass / first / second moments on both genuinely contiguous partitions, then true whole-frequency Gstar/Sstar Loewner brackets for `k=12,16`. Compare exact rational **trace widths** with verified MG24 as a methodological diagnostic. A smaller width is useful but does NOT by itself prove positive residual. Test the unchanged MG24 scalar trial against the new verified complete coupled matrix as a separate strict Gershgorin acceptance gate.

Strict no-promotion holds: full low band is **not yet integrated**; only the contiguous [0,4] prefix is. Full original 470D strong inverse, signed original 51/56 cap, independent signed Fourier/form/domain audit, complete odd/even/Weil/CC27/RH remain **OPEN**.

**Actions verification: PENDING.**
