# RPB108 — RC208: coupled use of the same variational/residual action error

Parent RC207, commit b6258587b64a3fcd8d80cb3622054412d2112749. Aperture B=11/10; canonical supported M=D^-1 L, six-source family and RC203's eight-trial least-residual coefficient map Y remain unchanged. RC206's exact directional error Gram is rebuilt from the same eight norm bounds and positive weights. Nominal residual, input/source and complete signed analytic tails are unchanged.

## Result

A different inverse payment formula reduces the certified relative six-source width from **0.672096 to 0.597416** (74677/125000). The relative improvement is 9335/84012, approximately **11.11%**.

| Same-family certified quantity | RC206 | RC208 |
| --- | ---: | ---: |
| Inverse width relative to G_lower | 0.672096 | 0.597416 |
| Width / half-Gram threshold | 1.344192 | 1.194832 |
| Threshold minus width | -0.172096 | -0.097416 |
| Half-Gram gate | Failed | Failed |

Both selected endpoints use the new coupled formula. The six-source gate remains open. The smaller width is below RC207's 0.655936 method barrier because that barrier covered the old separately paid formulas. It did not cover this coupled formula. RC207 is neither discarded nor contradicted; its conclusion required a method change, and RC208 supplies one.

## Coupled error identity

For a response vector x, write s=Sx, u=Yx as a physical trial, v as its represented canonical action, r0=s-v and e=Mu-v. All norms and pairings use D energy. The actual residual is r=r0-e.

Define C0=2 Re<s,u>-Re<u,v>. Exact square completion gives

    <s,M^-1 s> = C0-Re<u,e> + <r,M^-1 r>.

RC121 supplies aI<=M<=2I with a=32125/230953. Combining the dependence on the same e before applying Young's inequality gives

    lower: C0 + ||r0||^2/2 + ||e||^2/2 - Re<u+r0,e>,
    upper: C0 + ||r0||^2/a + ||e||^2/a - Re<u+2r0/a,e>.

For 0<theta_lower<=1/2, Young therefore supplies the lawful lower

    C0 + N_lower/2
      - theta_lower W_lower_upper
      - (1/(4 theta_lower)-1/2) E,

where W_lower_upper bounds the Gram of u+r0. For theta_upper>0, the lawful upper is

    C0 + N_upper/a
      + theta_upper W_upper_upper
      + (1/a+1/(4 theta_upper)) E,

where W_upper_upper bounds the Gram of u+2r0/a. The inequality theta_lower<=1/2 is needed to replace the negative error coefficient using its upper Gram E. No independence between the two appearances of e is assumed.

## Full tail and cross-Gram accounting

RC203's original payment is reconstructed exactly and removed to expose the unpaid finite variational endpoints B_lower/B_upper. The finite source/residual cross Loewner endpoints X_lower/X_upper are recovered by subtracting RC203's exact polarized source/trial endpoints. Their difference is checked PSD.

With tC,tW>0, define separate paid full-tail bounds

    P_C=tC U_tail+R_tail/(4tC),
    P_W=tW U_tail+R_tail/(4tW).

C0 is bounded by B_lower-P_C and B_upper+P_C. For c>0, the Gram of u+c r0 has upper

    W(c)=G_U_upper+c^2 N_upper+2c X_upper+2c P_W.

The full source Gram and full nominal residual Gram are retained. The missing cross-tail pairing is bounded using the complete source and residual tail Grams; both signs are paid. W(1) and W(2/a) are checked PSD. Thus the coupled vectors are not truncated to the finite physical prefix.

The selected exact rational proposal is theta_lower=3435420423/(5*10^11), theta_upper=1244900891/(250*10^9), tC=840546275283/10^12 and tW=105068358193/(125*10^9). The original RC206 error Gram is reused exactly. Only the four scalar coupled-payment parameters were proposed numerically; acceptance is exact rational arithmetic.

## Verification and custody

Four input certificates and seven helper modules are pinned by immutable Git blob hashes. The verifier checks the exact RC203 payment reconstruction, the recovered cross interval, reconstruction of RC206's directional error majorant, positivity of the coupled-vector Grams, the final lower endpoint and inverse gap, and exact relative-width domination. The preceding millionth-grid width fails the sufficient matrix test.

Reversed-order replay reverses the coupled-Gram term sums and endpoint option order and requires an identical certificate. Negative controls reject a lower Young parameter above 1/2, zero cross-tail parameter and mismatched input Git pin. The physical reconstruction and analytic source/action premises are inherited; this turn does not rerun their high-degree reconstruction or claim new Lean validation.

```bash
python scripts/validate_rpb108_rc208_coupled_action_error_inverse.py --output certificates/rpb108_rc208_coupled_action_error_inverse.json
python scripts/validate_rpb108_rc208_coupled_action_error_inverse.py --replay --output certificates/rpb108_rc208_coupled_action_error_inverse.json
```

The verifier includes the fixed rational proposal, so regeneration requires no optimizer or proposal file. Its input data and exact formulas determine the complete certificate.

## RC209 cursor and boundary

Next, jointly optimize a newly verified directional error envelope with the coupled formula, or tighten complete nominal residual/cross-tail data. RC207's old method barrier does not settle the optimum of this coupled family. A further error-envelope choice still requires an exact all-mixture bound. A changed trial requires its complete physical action and renewed error proof.

The certified gate deficit is 0.097416 G_lower, not a completion percentage or a lower bound on true inverse uncertainty. Native z_b6/t10 coverage, odd-parity/source-range and original augmentation remain open. Stage I, original Weil positivity, RH, F4 and Lean closure are unclaimed. Other branches and historical files are preserved.
