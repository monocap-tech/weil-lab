# RC197: complete canonical action on unchanged native v10

Starting head:a301c40dc56360621d20f044abbbd7e579639f23 (RC196). Aperture11/10, supported canonical M=D^-1 L and D-energy norm remain unchanged. This pass expands complete canonical action coverage to native v10; it does not evaluate an expanded inverse family.

| Absolute D-norm error upper | RC197 |
|---|---:|
| Complete centered endpoint action | <0.000420424080 |
| Complete regular D^-1 Rv10 action | <0.000014538424 |
| Complete canonical Mv10 action | <0.000434962504 |
| Complete action error relative to native source D norm | <0.013875852 |

These are outward decimal summaries of exact rational uppers. No local or global action tolerance is selected; the full relative norm upper is below1.387586%. This is coverage progress, not a comparison with the more accurate actions on different sources.

## Exact source attachment

RC133 uses the RC131 order10 source: a rational Cg midpoint polynomial through8190, followed by11 analytic moments at even n>=8192. Here g is the exact native w14 finite prefix through4094. RC183 already materializes the same Cg prefix; RC130 and RC131 compute it by identical directed kernel, D-division and1e-40 midpoint-floor rules.

The validator reconstructs every finite center and radius through8190 from the exact g input. Every center is compared with the materialized RC183 array, and the entire center/radius digest is compared with RC131. Direct controls at0,2,512,8190 are retained separately. The selected11 analytic coefficients and lambda=4094*4095 are inherited from RC131's second budget, as used by RC133. The source energy intervals come from RC133's actual v10 diagonal row. No new source or changed moment order is substituted.

## Complete action representation

Let p be the exact degree-512 prefix and t=v10-p. The represented endpoint action is C p approximated by a polynomial through1536 and25 exact analytic output moments, plus t/2. The full-domain0<=C<=I bound gives ||(C-I/2)t||_D<=||t||_D/2. The complete omitted source energy is bounded by the native energy upper minus a directed lower bound for the prefix energy. This pays the omitted finite input and the entire analytic native input tail together, without assigning their action zero or assuming cutoff commutation.

For the finite p action, all retained endpoint coefficients have directed intervals. Beyond1536, the coefficient rule is eta_n sum_{k=0}^{24} m_k (512*513/n(n+1))^k, where m_k are exact moments of p. The full geometric remainder is paid with the inherited eta-tail norm estimate. The endpoint input-tail payment dominates the complete action error in this first carrier.

The negative-r D^-1 correction is stored as a finite polynomial through512 with coefficient intervals. Beyond512, the exact coefficient function -r v10_n/D_n is retained, including the native finite and analytic source pieces and actual s. It is not approximated or truncated. The next mixed calculation must evaluate its parameter intervals when using it.

For R, the full omitted input receives RC174's orthogonal high-mode smoothing bound, transferred from physical L2 to D^-1 output D norm with D>=s_lower I. The finite regular input uses the degree-192 analytic kernel, exact Beta/log moments, private600-digit directed helpers and output1536. Parameter uncertainty, kernel truncation, coefficient rounding and the infinite regular output tail are paid. Historical helper files remain unchanged.

The represented canonical action is native v10 + finite endpoint action + analytic endpoint output + half omitted native input + finite negative-r correction + exact native negative-r tail + regular polynomial. The complete error adds endpoint, finite negative-r and regular payments. The identity and exact native correction tails incur no approximation error.

## Verification and next obligations

Nine certificates are SHA-256 bound: RC196, RC183 main/materialized carrier, RC131, RC130, RC133, RC129, RC121 and RC170. Source custody, direct predecessor attachments, full-domain contraction and the accepted five-source gate are checked. Replay reverses full source reconstruction, finite endpoint sums and analytic kernel sums and requires equality of the entire certificate.

```
python scripts/validate_rpb108_rc197_native_v10_canonical_action.py --output certificates/rpb108_rc197_native_v10_canonical_action.json
python scripts/validate_rpb108_rc197_native_v10_canonical_action.py --replay --output certificates/rpb108_rc197_native_v10_canonical_action.json
```

RC196's accepted five-source inverse width0.307029 and ratio0.614058 remain current. No six-source inverse response or mixed coupling is newly certified here. Native z_b6 and t10 complete canonical actions remain open. Stage I, its original augmented source-range/positivity requirements, RH,F4 and Lean closure remain open/unclaimed.

Next: attach the complete v10 source and action to correlated mixed rows, extend the inverse response family, and report that expanded family's acceptance separately. The larger source family may need sharper endpoint-input retention or residual enrichment; the five-source acceptance remains intact.
