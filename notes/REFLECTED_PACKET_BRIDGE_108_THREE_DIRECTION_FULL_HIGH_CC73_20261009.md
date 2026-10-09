# CC73 — a three-direction restriction including every high mode

Definitions: docs/TERMINOLOGY_RPB108_THREE_DIRECTION_FULL_HIGH_CC73.md. Integration parent CC72: fd8ca0ab3800140bb192a512ec953f625c3bb53c. Read-only producer NF29: 50723e823db4d102a7b419deec433942d8376423.

## Native source extension

NF29 freezes a two-high correction of NF27's retained response w and certifies the complete original source Gram of (v,w_h) in each parity. Unlike a retained mixture, this high correction preserves both retained directions x and w. Every original archimedean, prime, pole and mixed source contribution is included, with endpoint logarithms and all thirteen translation cells; source errors are paid before sign comparisons. The native finite energy comes from authenticated signed entries and separately paid small mixed pairings.

The odd two-direction coarse matrix is positive definite. The even matrix is indefinite. The complete source-square/energy ratios for the lifted response are (0.42957950,0.42957952) even and (0.19819722,0.19819723) odd, against the floor0.207. The odd determinant is strictly positive, not inferred from its two diagonal scores. Thus the ORIGINAL retained Schur restriction on span(x_odd,w_odd), with ALL F included in the minimization, is positive.

The even rejection concerns the fixed coarse test, not the actual original sign or all possible high lifts. Tiny measured high coordinates do not imply a small complete residual source: they are suppressed below2.15e-87 even and2.324e-85 odd while the even complete budget still fails. This is a genuine original-source control against substituting selected-shell suppression for full leakage control.

The unmodified complete producer and independent checker are freshly replayed; exact custody comparisons are recorded separately. The checker independently expands native lifted energies, reconstructs Q(v,h) as Q(p,h)-Q(y,h), checks unsquared source projections against the original N720/K620 archive, and rechecks both sufficient matrix signs.

## New quantitative full-high restriction

The unchanged even seed line remains Schur-positive. Exact parity combines it with the odd two-direction block, giving the three-dimensional retained space

    Z3=span(x_even,x_odd,w_odd).

The exact physical mass is diagonal: M=diag(||x_even||^2,||x_odd||^2,||w_odd||^2). In the even line, mu_even=U_even,00_lower/||x_even||^2. In the positive odd block, the inverse-trace bound gives

    mu_odd >= det(U_odd)_lower /
        (U_odd,11_upper*||x_odd||^2+U_odd,00_upper*||w_odd||^2).

This follows from the generalized physical matrix M^-1/2 U M^-1/2, whose inverse trace is trace(U^-1 M). No coordinate norm replaces physical mass. The odd physical retained Schur gap exceeds6.5082e-32. The combined retained gap is approximately3.325292835e-36, limited by the even seed.

To include ALL high vectors quantitatively, write the chosen trial columns Tz=z+Hz, with the NF26 high lifts on both seeds and the NF29 high lift on w_odd. Their complete sources are Rz=P_F L Tz. The energy identity is

    Q(Tz+f)=S(z)+Q_C(f+C^-1 Rz).

Let eta^2=trace(R*R M^-1)_upper/kappa^2 and xi^2=trace(H*H M^-1). Since the retained columns are physically orthogonal, these trace bounds need only the complete source diagonals and exact rational lift norms; all unknown signed cross terms are covered by the positive Gram trace. The paid bounds are approximately

    eta^2 < 3.185e-23,
    xi^2  < 5.972e-25.

Set u=f+C^-1 Rz. The physical vector Tz+f=z+u+(H-C^-1 R)z satisfies

    ||Tz+f||^2 <= (1+4eta^2+4xi^2)||z||^2+2||u||^2.

Consequently

    Q(h)>=g||h||^2 for every h in Z3+F,
    g=min(mu/(1+4eta^2+4xi^2),kappa/2)>3.32e-36.

This is positivity of an infinite-dimensional original restriction, with every F112 high mode included. It does not depend on the old whole-domain positivity margin. It is still a single-aperture result using these three explicit retained directions, not a uniform theorem on actual critical eigenvectors or every aperture cap.

## Restricted null exclusion and assembly scope

An original null whose retained component lies in Z3 is excluded by the physical gap above, including a null with zero retained component. This extends the original-seed retained restriction by one odd response direction. It leaves109 retained directions outside the restriction.

CC62's E2+F112 gap remains valid separately. Positivity of that restriction and of Z3+F112 does not certify their union: the missing same-parity mixed retained couplings remain load-bearing. CC71 finite116 positivity also remains valid. None of these restrictions alone is whole-domain53/50 positivity.

Next tasks are source-aware treatment of the failed even response, complete high control on the remaining retained background, and the signed collective assembly. A successful odd two-direction block cannot stand in for the other54 odd background directions or the even background.

## Exact controls and reproduction

Three rational block controls have high diagonal1, mixed coefficient-1/3, and retained diagonal s+1/9 for s=-1/100,0,1/100. Their exact high Schur value and determinant are s, so they test a genuine original positive/null/negative crossing with fixed coercive high floor. For the positive control the physical gap conversion is checked directly against the shifted determinant. Three whole-mass shifts of the PSD rank-one null control by1/1000,1/10,2 have exactly those positive ground levels. These specified block controls do not model complete Weil arithmetic.

The unmodified NF29 scripts use the original producer input names. A scratch staging directory can map the existing CC69/CC70 authenticated input copies to those names without changing any bytes. Its three native archives are the original E112, first-high and second-high signed archives; its independent checker also uses the authenticated NF24 residual-projection base64 archive. Full hashes are in the producer, validation and CC73 custody certificate.

```sh
python3 scripts/certify_native_lifted_response_nf29_106.py --output /tmp/nf29_replay.json
python3 scripts/check_native_lifted_response_nf29_106.py /tmp/nf29_replay.json --output /tmp/nf29_validation.json
python3 scripts/certify_three_direction_full_high_cc73.py /tmp/nf29_replay.json notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json notes/data/RPB108_NF26_FIXED_TRIAL_CC69_20261009.json notes/data/RPB108_NF27_SOURCE_INPUT_CC70_20261009.json --output /tmp/cc73_gap.json
```

Highest whole-domain anchor remains21/20 with margin1/(3*10^63). Whole53/50, full retained collective Schur positivity, all-cap old-gap-independent leakage, uniform defect-relative frame, global actual null exclusion, RH/F4, full transport and Lean remain open. No full-Weil nonimplication or actual negative vector is claimed. Historical wording and paused fronts are unchanged.
