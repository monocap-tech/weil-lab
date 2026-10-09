# CC71 — complete finite116 positivity and collective background lifts

Terminology: docs/TERMINOLOGY_RPB108_COLLECTIVE_TWO_HIGH_LIFT_CC71.md. Integration parent: CC70, 602bccebddb4768d141d4a4f1efa925925629ba0. Read-only source head remains NF27, a446275d4ba9a6c71599c310c35e81d2e439de95. This checkpoint consumes already authenticated original native entries; it does not restart a paused front.

## Result

The complete original finite restriction on the normalized Legendre modes e0 through e115 is positive. This includes the entire E112 retained block and two high modes in each parity, with all native mixed couplings. Its physical lower bound exceeds 9.23e-35 even and 3.27e-31 odd; hence the combined original finite116 restriction has a common physical gap greater than 9e-35.

This is an original finite-domain sign certificate. It does not prove the entire original form positive at 53/50: all modes above 115 remain outside this restriction.

For the complete 55-dimensional retained complement W in each parity, eliminating H2 jointly also passes. The largest two-high reaction fractions lie in (0.29754284466,0.29754284468) even and (0.25011331807,0.25011331808) odd. Thus this observed high reaction consumes about 29.75% and 25.01% of the worst retained-background energy, while leaving a positive finite Schur matrix.

Both backgrounds admit 55 frozen rational source-aware lifts. The complete fixed-lift energy matrices are independently certified positive. Their physical gaps exceed 5.43e-28 even and 5.82e-25 odd. Every lift's original measured high source coordinate is below 1e-68, with the inherited native-entry interval errors paid. These are concrete collective background lifts for a subsequent complete-source calculation, not inferred actual high minimizers.

## Proof arithmetic and physical mass

The script authenticates the unchanged NF24 seeds and the decompressed original E112, first-boundary, and second-boundary signed-source archives. Every full matrix entry is an outward interval from that original arithmetic. Decimal-200 LDL arithmetic selects fixed rational preconditioners only. Positivity is established by outward rational congruence with positive Gershgorin margins; inverse bounds use the verified row-norm Neumann residual. No numerical eigenvalue or sampled source is a proof input.

With K=Q(H2,W) and C2=Q(H2,H2), the background Schur matrix is S=A_W-K* C2^-1 K. A paid inverse of S gives the physical gap

    Q_S(Wa) >= ||Wa||^2 / trace(S^-1 W*W)_upper.

All inverse uncertainty is paid. The high form's gap is bounded below by 1/trace(C2^-1)_upper. Writing z=h+C2^-1 K a and using W*W>=I gives

    ||Wa+h||^2 <= (1+2||C2^-1 K||_F^2)||Wa||^2+2||z||^2.

This yields a positive physical gap for W+H2 without treating the rational W coordinates as orthonormal. The certified lower bounds exceed 4.26e-28 even and 4.57e-25 odd.

For the frozen rational Z, its actual native form is

    L=A_W-K*Z-Z*K+Z*C2 Z,
    G= W*W+Z*Z.

The producer separately certifies L>0 and pays trace(L^-1 G) for the physical gap. It also directly encloses K-C2 Z. There are 110 residual entries (two measured high modes times 55 columns); sqrt(110)<11. Since G>=I, their Frobenius bound gives

    ||P_H2 L_original Ua|| <= 11*residual_max*||Ua||.

This is a selected-shell physical source bound on the finite lifted background. It contains no old positivity gap. It is not the near-critical all-source-shell leakage bound or the uniform defect-relative frame under investigation.

Finally, the producer independently certifies the full original 58-by-58 native matrix in each parity on E+H2. These bases are physically orthonormal, so 1/trace(full_inverse)_upper is a physical gap directly. The retained principal block of that joint inverse is the inverse of the complete 56-dimensional two-high Schur matrix, proving its positivity as well. The complete retained finite two-high elimination is therefore closed, including the seeds.

## What the collective loading does and does not imply

The two-high loading is computed from the two eigenvalues of C2^-1 K A_W^-1 K*, using its trace, determinant and paid rational square-root enclosure. A high-form variational principle implies that the complete infinite-high true-response loading is at least this finite value. Thus CC71 strengthens CC70's native lower bounds to above 0.29754 even and 0.25011 odd.

These finite values are below one, allowing the observed collective Schur sign. They are lower bounds for the unknown full response; no remaining-high upper bound follows. In particular, the unchanged robust joint bound using NF26's floor-based seed response and NF27's finite retained reaction still cannot pass. Signed collective response or stronger source-aware residual control remains necessary.

Future use of the frozen lifts must preserve their finite mass and energy matrices and certify the complete source Gram into F, including the measured residual and all omitted high coordinates. That calculation can test the collective floor-based Schur matrix for the corrected trial family. Directional success on a single mixture cannot replace the matrix sign test.

## Controls, reproduction and scope

Three exact two-block crossings use diagonal energies 1 and 1 with mixed coefficient b=0.99,1,1.01. Their true Schur values are 1-b^2 and the frozen lift has energy 2-2b; the difference is exactly (1-b)^2. The same controls at retained diagonal 1e-36 and mixed coefficient 1e-18 b give genuine near-critical positive, zero and negative signs. Three whole-mass shifts (1/1000,1/10,2) of the null control have those exact positive physical ground levels. These test signed high elimination and the distinction between a true Schur sign and a fixed-lift sufficient test. They do not model complete original Weil identities.

```sh
python3 scripts/certify_collective_two_high_lift_cc71.py notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json INPUT_DIR/native112_N720_K620.json.gz INPUT_DIR/native_boundary_columns_112_113.json.gz INPUT_DIR/second_boundary.json.gz --output /tmp/cc71_certificate.json
```

Whole-domain anchor remains 21/20 with margin 1/(3*10^63). Earlier infinite-high restricted null exclusions remain valid. CC71's finite116 positivity adds no whole-domain null exclusion. Whole 53/50 positivity, full infinite-high collective retained Schur sign, all-cap leakage, uniform defect-relative critical frame, global actual null exclusion, RH/F4, full transport and Lean remain open. No full-Weil nonimplication or actual countermodel is claimed. Paused fronts and historical wording remain unchanged.
