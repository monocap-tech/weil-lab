# RPB108 — RC212: complete native t10 canonical action

Parent RC211, commit a89ca21805cb0c618c111514129ad19cb111763b. Aperture 11/10 and M=D^-1 L remain fixed. RC210's accepted six-source inverse width 0.436100 and margin +0.063900, and RC211's complete z_b6 action, are preserved.

## Result

The unchanged native t10, also named t10_common_response in RC136, now has a full canonical action trial with

    ||M t10 - represented_action||_D
      <= 0.0005558493682549691728804711990794203111.

Safe rounded bounds are **0.000555850** in D norm and **0.038687706** relatively (3.8688%) against the certified native source-norm lower. The complete endpoint component is at most 0.000378821 and the complete regular component at most 0.000177029.

This closes the missing t10 full-action construction. It does not certify sufficient precision for the expanded inverse gate. The existing six-source accepted width remains unchanged.

## Exact source custody

RC135 defines native t10 by its finite midpoint/floor output polynomial through even degree 16382 and the selected order-10 analytic carrier. Its generator uses the finite common input (v10+z_b6)/2 through even degree 8190. Native t10 is not silently replaced by the full exact C((v10+z_b6)/2), which would be a different source.

The verifier:

1. Reconstructs the full balanced input intervals g-alpha psi0 through 4094 and checks RC132's immutable hash.
2. Reconstructs every finite native z_b6 output center and generator radius through 8190 and checks RC132's full output center/radius hash.
3. Forms the exact finite common input with the pinned native v10 centers and checks RC135's common-input coefficient hash.
4. Reproduces the historical t10 midpoint/floor coefficients at every even degree 0..512.

All source constants and actual s-dependent directed intervals are retained. RC136's full native t10 D-energy lower/upper and seven-vector independence remain authoritative. The remaining finite source coefficients and its full analytic source tail are paid using the full energy upper minus directed finite-prefix energy lower; they are not assigned zero.

## Full canonical action

The represented action is

    native t10
      + represented endpoint action of the native prefix through 512
      + (1/2) omitted native input above 512
      - r D^-1 native t10
      + represented regular action of the native prefix through 128,

with r=789/125. The endpoint output polynomial extends through even degree 4094, followed by 25 exact signed moments of the finite input and a paid geometric remainder. Coefficient-rounding energy is included. The whole-domain positive endpoint contraction bounds the centered omitted-source action error by half its D norm without any cutoff-commutation assumption.

The negative-r multiplier is exact over every finite and infinite native source coefficient. The regular part uses the analytic Poisson/Beta/log-moment projection through output degree 768. Parameter, kernel-series, coefficient-rounding and the entire output tail are retained. RC174's high-input smoothing at cutoff 128 pays the complete omitted native regular input, using its D-energy upper and the actual D-floor on its support.

The complete action error is the outward-rounded sum of the full endpoint and regular errors. Neither component is accepted by a stand-alone matrix tolerance, and no such tolerance is inferred from the six-source gate.

## Verification

Normal and reversed-order replay pass and require an identical complete certificate. Replay reverses the full z generator input sums, common-input t10 sums, endpoint output and moment sums, and analytic regular-kernel accumulation. The full historical z and common-input hashes match in both orders. Eight inherited certificate blobs and eleven helper blobs match the live repository tree. A mismatched input Git pin is rejected.

```bash
python scripts/validate_rpb108_rc212_native_t10_canonical_action.py --output certificates/rpb108_rc212_native_t10_canonical_action.json
python scripts/validate_rpb108_rc212_native_t10_canonical_action.py --replay --output certificates/rpb108_rc212_native_t10_canonical_action.json
```

These are analytic and rational arithmetic certificates with inherited physical/metric premises. No new Lean validation is claimed.

## RC213 cursor and boundary

The named z_b6 and t10 full-action gaps now have explicit carriers and paid errors. Attach them to enlarged mixed source/action and represented-residual matrices, retaining both signs of every omitted mixed tail. Rebuild the source Gram and trial map and independently test the expanded canonical inverse gate. Adding both sources to the six-response family also containing auxiliary P2 produces an eight-response test; it must not be confused with the historical seven-member native frame.

If the initial errors do not suffice, refine their endpoint and regular input/output carriers based on that expanded test. The accepted six-source gate cannot be transferred to a larger source family without a new enclosure. Original augmentation/source-range and odd-parity obligations remain distinct.

Expanded inverse acceptance, Stage I, original Weil positivity, RH, F4 and Lean closure remain open/unclaimed. All historical files and other branch heads are preserved.
