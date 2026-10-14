# RPB108 — RC245: original-source refinement and orthogonal output splitting

Date: 2026-10-14 UTC. Parent RC244: `6e56c17f165645933ea481d90bf755f4561ae5b9`. Branch: research/rpb108-route-consolidation. Aperture B=11/10.

RC245 extends the complete original-action sources N0 P0 and N0 P1 through output degree 128. Their first 65 center coefficients are preserved exactly. It then compares two consistent response representations: the extended centers, and the old degree-64 centers with newly sharpened complete error bounds obtained by orthogonal output splitting. The second representation improves the response bounds.

The response source count stays two and the trial spaces stay span{P0,P2,P4,R0} and span{P1,P3,P5,R1}. No new source or trial directions are claimed. Both signed-gap intervals still cross zero. Full signed positivity, original whole-space positivity, the full auxiliary norm gate, Stage I, RH, F4 and Lean remain open.

## Longer complete original-source actions

Apply the generic RC242 physical polynomial convolution, complete seven-pair prime action, signed pole Taylor action and combined endpoint-tail machinery to P0 and P1. Retain output through degree 128 and pay every output after that degree. The endpoint tail combines exact degrees 129–256 and a proved complete remainder; the regular and prime tails retain their full physical norm estimates before applying the omitted D weight.

The old degree-64 source centers use the original fine prime-parameter model. The new degree-65-through-128 block uses RC242's practical 10^-16 prime model. Both parameter errors are paid. If E_fine and E_extension are the complete D-energy squared prime-model faults, a conservative fault for the hybrid model is

\[
E_{\rm hybrid}\le(\sqrt{E_{\rm fine}}+\sqrt{E_{\rm extension}})^2.
\]

Projection to any output-degree block is contractive in D energy because D is diagonal in the Legendre basis. This hybrid bound therefore covers the fine model on the old block and the rounded model on the rest. Finite coefficient intervals pay actual s and rounding. All component faults are combined in norm before squaring.

| Original-source squared D-error upper (approx.) | Even P0 | Odd P1 |
|---|---:|---:|
| RC239 error around degree-64 center | 0.002071601 | 0.002996369 |
| RC245 error around extended degree-128 center | 0.001019422 | 0.001275369 |

These are complete action bounds for the same original inputs, with different finite approximation centers. The extended-center uncertainty is smaller by about 51–57%.

## Consistent shared-source trial update

The response source O=N0 P_base also appears as the original part of the first augmented trial action N P_base. When its center changes, change both together. Define the new first N center as

\[
N_{\rm center,new}=O_{\rm center,new}
+(N_{\rm center,old}-O_{\rm center,old}).
\]

The augmentation-center difference is checked unchanged exactly in every output degree. Its complete augmentation fault is unchanged. Thus the source/first-action original uncertainty still has coefficient |1-y0| in the residual; it is not charged as two unrelated faults.

The original and rational frequency form interval matrices remain the RC244 certificates for the same actual inputs and operators. Their validity is independent of the new center choice. The first 65 original center coefficients and all tested input polynomials of degree at most 64 are preserved; the actual form certificates are not recomputed from the coarser extension model.

The extended-center response is certified and intersected with RC244. It does not improve the final enclosure: the newly exposed high-degree source output worsens the fit of the existing trials enough to offset the smaller action uncertainty. This demonstrates why a smaller error bound by itself is not a guaranteed improvement in the inverse certificate.

## Sharper error around the old center

Keep the old degree-64 center and use the new information to split its complete model error into three output-degree blocks:

- Below or at degree 64: the unchanged finite model-rounding error.
- Degrees 65–128: the squared norm of the combined new original output, with every retained coefficient and actual D-weight interval paid.
- Beyond degree 128: the complete endpoint, regular and prime model tails, combined in norm.

These output blocks are exactly orthogonal in actual D energy. Add their squared bounds, then add the complete actual-to-hybrid-model fault norm before squaring. This uses orthogonality of different Legendre output degrees, not independence of errors from different input columns. In particular, degrees 65–128 are squared only after their original endpoint, regular, prime and pole contributions are summed, retaining their cross terms.

If E_low, E_resolved and E_tail bound those three model blocks and delta_model bounds the complete model fault norm, then

\[
E_{\rm old\ center,new}\le
[\sqrt{E_{\rm low}+E_{\rm resolved}+E_{\rm tail}}
+\delta_{\rm model}]^2.
\]

This gives sharper complete errors without changing the old source/action centers:

| Sharpened old-center source squared D error upper, rounded upward | Even P0 | Odd P1 |
|---|---:|---:|
| RC245 | 0.001721921 | 0.002536606 |

The first augmented trial error is updated from this original fault and the unchanged augmentation fault, and the corresponding source uses the same refined original fault. All other action columns are unchanged. Their errors remain fully paid; no same-parity column orthogonality is assumed.

## Response results

Use the RC244 four-trial variational and correlated signed-gap formulas with both representations. Exact nominal least-residual and Galerkin proposals, rational coefficient variations, and the preceding four-component upper trial provide candidates. These choices do not prove optimality. Preserve all previously certified intervals by intersection.

| Certified quantity | Even | Odd |
|---|---:|---:|
| RC244 inverse response upper, rounded upward | 8.055899798 | 10.432433658 |
| RC245 inverse response lower, rounded downward | 0.011438135 | 0.013401437 |
| RC245 inverse response upper, rounded upward | 7.395622002 | 9.616684253 |
| RC245 signed gap lower, rounded downward | -7.307062806 | -9.519601437 |
| RC245 signed gap upper, rounded upward | 0.077121061 | 0.083681379 |

The lower inverse endpoints are preserved, and both upper inverse endpoints and both signed lower endpoints improve. Neither parity certifies a positive signed gap or an actual negative original direction. The nominal fit of the final old-center representation remains the same as RC244; this improvement comes from its sharper complete source errors.

## Verification and next step

The validator checks 170 pinned input/helper blobs. Exact replay reverses prime moment accumulation, endpoint tail summation and response residual summation, requiring certificate equality. It checks the exact augmentation-center difference, strict improvement of both extended-source and sharpened-old-center action error bounds, full hybrid-model fault payment, and consistency of the shared source/action update. The pinned four-dimensional nonidentity metric control verifies the inverse and signed residual identities with noncommuting operators.

Publication adds the validator, certificate and this note to RC244 while preserving existing repository blobs. The residual trial span retains its actual original D-form floor 61/250. The separate canonical eight-source metric-inverse width remains 485647/1000000.

Next: materialize or otherwise refine the R0/R1 augmentation output, which remains a substantial residual fault. A stronger valid inverse correction is another option. The complete signed criterion still requires all 248 even and 391 odd parameter channels, or an equivalent uniform proof.
