# RPB108 — RC210: collective regular-input tails close the six-source gate

Parent RC209, commit 2733eb54d1a7858f3d1d1c59be33df19e7207adf. Aperture B=11/10, actual supported M=D^-1 L, six response sources P0,P2,f0,psi0,w14,v10, and the eight raw trials P0,P2,f0,psi0,w14,q185,v10,q202 remain unchanged. The RC203 least-residual coefficient matrix Y, represented actions, full nominal residual/source Grams and their signed tails remain unchanged.

## Result

The collective regular-input-tail error bound, transported through RC208's coupled inverse formula, certifies

    inverse enclosure gap <= (4361/10000) G_lower = 0.436100 G_lower.

Consequently the six-source half-Gram gate is **accepted**, with the strict certified margin

    (1/2)G_lower - enclosure gap >= (639/10000)G_lower = 0.063900 G_lower.

| Same-family certified quantity | RC208/209 upper | RC210 |
| --- | ---: | ---: |
| Six-source inverse width | 0.597416 | 0.436100 |
| Width / half-Gram threshold | 1.194832 | 0.872200 |
| Threshold minus width | -0.097416 | +0.063900 |
| Six-source half-Gram gate | Failed | Accepted |

The inverse-width reduction is approximately 27.00%. Both selected inverse endpoints use the coupled formula. This closes the specified six-source inverse-width contract; **Stage I remains open** because native z_b6/t10, odd/source-range and original augmentation obligations are not supplied by this certificate.

## New physical error information

RC209 established that independent marginal-error envelopes with the old carriers could not pass the gate. The dominant omitted regular-action inputs have a shared linear operator R. Paying their individual norms loses cancellation between the w14 and v10 response coefficients.

For f0,w14,v10, the represented regular actions use inputs through degree 512. For psi0 the represented regular action is zero and the actual input starts at degree 990. Form the four actual omitted inputs h_f,h_psi,h_w,h_v in physical L2. Every input is supported in Legendre degrees at least 514. The true omitted regular action on their mixture is exactly

    D^-1 R (c_f h_f+c_psi h_psi+c_w h_w+c_v h_v).

Construct its physical input Gram before applying the common high-mode operator bound. This is not an assumption that individual errors cancel: the underlying omitted inputs and their common linear action are identified from the pinned source certificates.

RC174's high-input smoothing estimate, evaluated at cutoff 512 with RC170 constants, gives ||R h||_L2^2<=phi_512^2 ||h||_L2^2 for every such high-mode input. The D floor s>=s_lower then gives

    ||D^-1 R h||_D^2 <= (phi_512^2/s_lower)||h||_L2^2.

The verifier recomputes phi_512^2 exactly and checks agreement with RC193, RC190 and RC197. Psi's omitted input is allowed in the common cutoff-512 space; its sharper individual cutoff-988 bound is removed from the old separate payments, not reused as a common operator bound.

## Complete four-input Gram

The physical input Gram is reconstructed with directed interval arithmetic over even degrees 514 through 32766:

- f0: actual eta_n for 514<=n<=988, zero afterward;
- psi0: actual eta_n for n>=990;
- w14: pinned rational finite coefficients through 4094, then its complete 15-moment analytic carrier;
- v10: pinned rational finite coefficients through 8190, then its complete 11-moment analytic carrier.

Here eta_n=(2n+1)/(n(n+1)(H_n+s)); the common actual s is retained in the directed interval. The physical Legendre mass is 2B/(2n+1). Source definitions and moment centers are inherited exactly, without changing finite/analytic carrier conventions.

Beyond 32766, retain the common leading vector (0,1,mu_w0,mu_v0) before taking a square. The two nonleading analytic remainders are bounded by their full positive moment amplitudes at the first omitted degree. If T bounds the physical eta tail energy, a valid full tail Gram upper is

    (3/2)T leading*leading^T
      +6T diag(0,0,delta_w^2,delta_v^2).

The physical eta tail energy is at most T=up(B/(D_cut,lower^2 (cut-1)cut)). This accounts for the entire infinite source tail. Finite interval widths are converted to Loewner endpoints with outward rational rounding. The four-input upper is checked PSD, multiplied by the common smoothing factor, and transported through the corresponding four rows of Y.

## Remaining error components

Remove only each explicitly identified old regular-input-tail norm payment from its additive canonical-action bound. The remaining eight marginal norm bounds keep all finite regular projection, input-center, endpoint, negative-r and rounding errors. Their positivity and equality to the appropriate RC193/RC188/RC190/RC200 complete source bounds are checked. This uses the additive decompositions in those immutable certificates, rather than subtracting arbitrary upper bounds from a total error.

A positive diagonal triangle majorant controls the remaining error map for all complex mixtures. Combine its Gram E_remaining with the correlated regular-tail Gram E_regular using

    E_complete=(1+tau)E_regular+(1+1/tau)E_remaining,
    tau=1/3.

All errors remain paid without independence or orthogonality assumptions. On RC209's specific limiting probe, the new complete squared-error bound is approximately 67.35% smaller than the old exact sum-of-individual-norm triangle bound. That percentage is probe-specific, not a claimed uniform Gram reduction.

## Inverse transport and verification

The second verifier replays the entire collective-tail certificate, reconstructs RC206's old error Gram as a control, and substitutes the newly proved E_complete into RC208's coupled formula. The unpaid variational base, both full coupled-vector Grams, source/residual cross tail bounds, nominal residual bounds and RC121 coercivity are retained. The selected positive rational proposal is embedded in the inverse verifier. It is proposed numerically but accepted only by exact rational PSD checks.

Normal and reversed-order replay pass for both certificates. The reversed source replay recomputes all directed coefficient/moment and physical Gram sums in reverse order and reproduces the same rational matrices. The inverse replay also reverses coupled-Gram term and endpoint-option order. Exact lower-endpoint positivity, inverse-gap positivity, relative-width domination and half-Gram gate positivity all pass. The immediately preceding millionth-grid width fails the sufficient width test.

All 13 inherited source input blobs and seven helper blobs match the repository tree. The inverse verifier additionally pins the new collective-tail certificate/helper and the RC208 certificate. Negative controls reject a mismatched source input pin and an invalid lower Young parameter. These are analytic/rational arithmetic certificates; no new Lean compilation or original Weil positivity is claimed.

```bash
python scripts/validate_rpb108_rc210_collective_regular_input_tail.py --output certificates/rpb108_rc210_collective_regular_input_tail.json
python scripts/validate_rpb108_rc210_collective_regular_input_tail.py --replay --output certificates/rpb108_rc210_collective_regular_input_tail.json
python scripts/validate_rpb108_rc210_collective_regular_inverse.py --output certificates/rpb108_rc210_collective_regular_inverse.json
python scripts/validate_rpb108_rc210_collective_regular_inverse.py --replay --output certificates/rpb108_rc210_collective_regular_inverse.json
```

The component tail certificate records the pre-transport upper 0.597416 because it evaluates no inverse enclosure. The inverse certificate supplies this checkpoint's authoritative upper 0.436100 and gate acceptance.

## RC211 cursor

Preserve the accepted six-source inverse contract. Extend the remaining native z_b6/t10 complete-action coverage and test the expanded source family with its paid errors and inverse response. Odd-parity/source-range and original augmentation acceptance must also be supplied before Stage I closure. Enlarging the source family is new coverage, not a same-family precision improvement, and its gate must be tested independently.

Stage I, original augmented Weil positivity, RH, F4 and Lean closure remain open/unclaimed. This continuation adds new certificates and verifiers without changing historical files or other branch heads.
