## Verified MG38 original full-matrix outcome — October 20, 2026

Original calculation [Actions #39507961568](https://github.com/monocap-tech/weil-lab/actions/runs/39507961568) PASSED. Then the stronger independent [Actions #39508270844](https://github.com/monocap-tech/weil-lab/actions/runs/39508270844) **PASSED**, exporting actual exact rational **full 24×24 signed comparison matrices**, full original Hlo minus *band-only* matrices, every negative rational Rayleigh vector, and complete rational congruence bases; the separate CI auditor reconstructs each decisive sign by exact Fraction matrix multiplication. Accepted artifact `mg38-original-whole-source-matrix-feasibility-gate`, ID `12305011490`. Previous first-pass artifact ID `12304262899` did not include independent full-matrix witness replay; the stronger audit supersedes it.

| original B trial | cutoff k | independently accepted original MG30 complete-source Rupper trace | independent MG36 complete-source Rupper trace | exact rational signed Loewner comparison of U36−U30 | exact necessary Hlo−V[4,8] |
|---|---:|---:|---:|---|---|
| scalar tI | 12 | 29.77298323 | 68.53050791 | **strictly POSITIVE** by rational congruence | negative rational Rayleigh witness |
| nonscalar ridge | 12 | 88.57726616 | 74.86757399 | negative Rayleigh witness for U36−U30; MG30 NOT Loewner-smaller | negative rational Rayleigh witness |
| scalar tI | 16 | 29.77298340 | 68.53051285 | **strictly POSITIVE** by rational congruence | negative rational Rayleigh witness |
| nonscalar ridge | 16 | 86.91331301 | 74.78829773 | negative Rayleigh witness for U36−U30; MG30 NOT Loewner-smaller | negative rational Rayleigh witness |

**Critical verified inference 1 — source-matrix full-spectrum superiority (scalar only):** At both original k=12 and 16, `U36−U30 ≻0` is an exact rational positive-definite matrix theorem for these two separately certified upper bounds on the genuine original-source residual. This is stronger than a mere TRACE comparison. In nonscalar cases, U36−U30 has an exact negative Rayleigh witness: do NOT infer either reverse Loewner ordering or that an actual operator has a negative mode.

**Critical verified inference 2 — necessary source-certificate feasibility no-go:** In **all four** actual B/cutoff scenarios `Hlo−V_[4,8]` has an exact rational negative quadratic witness. Given that any additional measured-prefix/omitted-frequency residual covariance **upper** is necessarily PSD, for the CURRENT Hlo and current selected measured-band upper V, no arbitrarily good new remainder-only bound can produce `Hlo−(V+P) ≻0`. Even a formal P=0 cannot make this particular conservative source-certificate matrix strictly positive. This statement does NOT say the actual physical Gram H-Ractual^*Ractual is negative: Hlo and V are conservative interval bounds and may be very loose.

**MG39 route recommendation:** The original complete-source MG30 scalar bound is already massively stronger than MG36 in full matrix order, but MG30's exact positive source-contraction acceptance margin still fails narrowly. Focus on original **joint H/Gstar/Sstar source-moment uncertainty**, exact signed source residual and robust eigenvalue acceptance on the MG30 matrix, rather than direct extra-band Young/radius refinements. An important acceptance requirement is that every newly proposed bound be no worse than the independently certified original MG30 scalar matrix in an actual Loewner (not only trace) comparison, or separately prove its strict positive residual source gap.

W-ODD-NEG, original full 470D inverse, signed 51/56 odd negative cap, independently audited source Fourier/form/domain, complete even/Weil/CC27/RH still **OPEN**.

---

# MG38 — Original whole-spectrum source-residual benchmark and remainder feasibility

October 20, 2026. Stacked on accepted [MG37 #286](https://github.com/monocap-tech/weil-lab/pull/286). The verified MG37 source covariance structural no-go states that retaining the exact MG32 omitted-frequency upper after measuring [4,8] gives `U_new = U_MG32 + U_band`, with U_band PSD. Therefore further tuning of **only** the added-band certificate cannot improve the complete residual upper in Loewner order. The four original-source exact Young optimal trace barriers also remain above MG32.

## Distinct MG38 question: which original full-frequency enclosure is actually useful?

The original MG30 method already has a genuinely independent rigorous full-real-frequency, all-pole 24-channel source residual upper using coupled first/second original `Gstar/Sstar` moments (from MG29), while MG36's rigorously different full-frequency upper is assembled by directly measuring `[0,4]`, `[4,8]`, and a physical SM41/Young remainder. Comparing their upper TRACE alone proves no matrix ordering.

MG38 independently reconstructs `U30` from accepted MG29 original `LG<=Gstar<=UG`, `Sstar<=US`, the exact original MG30 anchored mixed-source identity `B=tI+D` and original 24D physical Hlo/Hup, but reuses MG36's **exact exported Hlo=U36+(Hlo-U36)** instead of recomputing the SI10 physical Gram. Thus it reconstructs original full-frequency MG30 **on exactly the same true 23-adapted + sinh-pole basis** and audits its EXACT accepted original Gershgorin residual margin from independent original MG30 Actions #39442984941.

## Source-matrix ordering acceptance

Compute the true symmetric rational matrix

```
Delta = U36 - U30.
```

If a rational change of basis W has **strict positive Gershgorin margin** for `W^T Delta W`, this proves `U30 < U36` in full Loewner order and establishes actual matrix superiority of the older complete-source moment method. If an exact rational nonzero v satisfies `v^T Delta v<0`, then U30 does NOT globally dominate U36 by that order. Otherwise the order is INCONCLUSIVE. Floating eigenvectors only propose exact rational trial vectors/bases, and no scalar TRACE comparison can substitute for a Loewner proof.

This is an *independent source enclosure benchmark*, not the false claim that MG38 has already developed a new stronger Fourier estimate.

## Separate necessary feasibility gate for a revised remainder

The complete MG36 upper has the form

```
U36 = U_prefix + V_[4,8] + U_remainder.
```

The directly measured [4,8] upper V is itself PSD (nominal affine covariance plus nonnegative diagonal interval error). Any replacement source-prefix and omitted-frequency upper `P` is PSD because it bounds an actual PSD residual covariance.

A necessary condition for a hypothetical original source contraction from this **fixed** `V` is

```
 Hlo - V  > 0.
```

Indeed, if `Hlo - V` has a strict negative rational Rayleigh witness then `Hlo - (V+P)` is also nonpositive along that direction for any `P>=0`, including a hypothetically perfect zero-cost remainder. A rational negative ray excludes a *source-certificate* contraction using this particular V even if the remainder error is eliminated completely; it says NOTHING about actual original operator negative spectrum. Conversely positivity of `Hlo-V` alone is necessary, not sufficient, because P cannot realistically vanish.

MG38 computes this necessary matrix and classifies an exact rational negative ray, a rational positive congruence, or INCONCLUSIVE. Both the independent MG30/G36 matrix comparison and this gate are original 24D finite-source results, not a 470D inverse or odd signed cap.

## Acceptance and next method

Require accepted pinned Actions original MG24 #39378465438, MG29 #39440914565, MG30 #39442984941 and MG36 #39495457084. All four true original rational B/cutoff cases must exactly reproduce MG30 source margins and MG36 full rational matrices before any source ordering claim. Independent CI checks each negative Rayleigh vector with exact Fraction quadratic calculations inside the actual script, and audits output status and no-promotion.

**If the MG36 fixed band upper already fails even the ideal remainder necessary test, the method must reduce direct source-residual covariance too; working on the remainder alone cannot save it. If the band passes but MG30 global complete-source moment upper is better, prioritize independent precision improvements for original Gstar/Sstar moments and their coupled residual, rather than extra frequency-coverage interval calculations.**

W-ODD-NEG, original all-470 strong inverse, signed negative 51/56 cap, independently audited Fourier/form/domain, full even/Weil/CC27/RH remain **OPEN**.

**MG38 calculation and independent exact rational matrix-witness CI PASSED; no source contraction.**
