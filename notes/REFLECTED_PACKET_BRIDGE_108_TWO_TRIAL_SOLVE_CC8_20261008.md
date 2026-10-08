# RPB108 CC8: actual two-direction complement solve, with whole residual enclosure

2026-10-08 UTC / 2026-10-07 Pacific. Coupled base `2386b78360d55d44b74c2998f1e321323e3ff1da`; shared NF66 `48fef33ca0cede19d81a91f8f357153372498436` recovered and reconciled additively. Definitions: [CC8 registry](../docs/TERMINOLOGY_RPB108_TWO_TRIAL_SOLVE.md). Aperture and Pre-Contact Shadow remain paused.

## Objective and scope

CC7 supplied whole inverse-tail budgets but did not evaluate an inverse head. CC8 reconstructs THREE complete original sources at a=21/20: the saved witness's even part and two physical complement polynomials of degree 112 and 114. It computes all trial native/action mixed products, certifies a two-direction ORIGINAL inverse-estimator credit, and encloses the first WHOLE shifted-resolvent quadratic action on the saved source direction by an actual trial plus its whole residual.

The actual shifted trial is not the entire inverse vector, and its interval is not a 112-column action map. A small inverse-series tail does not erase this trial's remaining head-solve error. No whole target positivity is asserted.

## 1. Actual source construction and original arithmetic

Use the same original operator constructor and Fourier/physical normalization as CC3. On t=(x+a)/(2a), 2a=21/10, each source has the exact structure

    Lp(t)=-[log(t)+log(1-t)]p(t)/2+regular_p(panel)+error.

The new trials z_112,z_114 are DEFINED by rational midpoint normalization factors on the 800-digit outward grid. Exact physical Legendre orthogonality puts both in F112, with zero retained mass coefficients 0..111. They are not assigned a new complement bound. The known c112=699/1000 is retained.

All six original prime powers 2,3,4,5,7,8 and both signed pole slots remain in the 13 translation panels. Exponential order 140, 180 Bernoulli pairs, gamma order 56, 1,000 outward logarithm terms and the original explicit remainder budgets are reused. Smooth panel coefficients use the 250-digit grid with their SUM of radii. Exact endpoint-log and squared-log moments supply every singular mixed product; no quadrature-only sign is used.

The witness's actual odd coefficients are not set to zero in its original norm or corrected baseline. Reflection makes their pairings with these EVEN trials zero exactly. The even normalization substitution is bounded by the existing whole finite-source norm estimate, as in CC3.

Every retained physical projection 0..111 is removed from the actual action products. All 56 reconstructed even witness pairings are checked against the independent native matrix; both new witness/trial native pairings and the 112/114 cross native pairing receive Hermitian symmetry overlap audits.

## 2. Two-trial original inverse credit

Write Z=(z_112,z_114), B=B_h, with the ORIGINAL physical complement operator C. The newly enclosed quantities are

    b=Z^*B, QZ=Z^*CZ, GZ=(CZ)^*(CZ), v=(CZ)^*B.

GZ is an actual full source-action Gram with every retained projection removed. It is NOT QZ squared or a fictitious operator assigned the same Gram. Set

    J=GZ/c-QZ, a=v/c-b.

C>=cI implies J>=0. The actual 2x2 outward determinant and diagonal are checked strictly positive. Rational coefficients t are selected by solving the midpoint system Jt=a; that midpoint solve is only a proposal. Their certified improvement is evaluated afresh with ALL interval products:

    credit(t)=2 t^*a-t^*Jt,
    <B,C^(-1)B> <=||B||^2/c-credit(t).              (1)

Equation (1) is the original inverse square-completion identity with u=Zt and r=B-Cu. Adding the credit to the saved corrected sufficient-form baseline is lawful on exactly the SAME coefficient direction, with the complete saved source error still subtracted. Every off-diagonal QZ and GZ product remains present.

## 3. First actual shifted-complement solve

For the ORIGINAL shifted complement choose tau=c, L=C+tau I. This is the original counterpart of CC7's repaired-complement inverse construction. L>=2c mass, so it is protected independently of the unknown retained Schur gap. Its actual two-trial action moments are

    QL=QZ+tau Z^*Z,
    GL=GZ+2tau QZ+tau^2 Z^*Z,
    vL=v+tau b.

The trial masses are exact and the two trials are physically orthogonal. Select rational ts from the midpoint GL ts=vL, then enclose the ENTIRE projected original residual

    rL=B-LZts,
    ||rL||^2=||B||^2-2ts^*vL+ts^*GLts.              (2)

All action terms in (2) are newly reconstructed. The complete source norm is enclosed from the saved corrected estimator: if q and s are the saved native and corrected witness intervals, dG is the saved actual Gram error, and m is the full witness mass, then

    c(q_lower-s_upper)-2dG m <=||B||^2
                            <=c(q_upper-s_lower).  (3)

The source auditor's definitions make (3) a bound on the ACTUAL projected source, not on the surrogate alone. Outward native/baseline intervals keep the inference one-sided. The two complete-map error copies on the lower side are retained.

Let u=Zts and E=2<B,u>-<u,Lu>. Completing the WHOLE inverse square gives

    E <= <B,L^(-1)B> <=E+||rL||^2/(2c),
    ||L^(-1)B-u||^2 <=||rL||^2/(2c)^2.             (4)

This is an actual enclosure of the first shifted inverse quadratic, including its infinite complement residual. A positive trial E is a LOWER inverse test; it is not an inverse upper bound until the residual term is added. It is not the sum of CC7's 129 head actions or their entire matrix.

## 4. Outcome

The three-source reconstruction passes. The actual 112/114 native off-diagonal is approximately 0.6091838188906054; it is retained together with the complete action off-diagonal. All 56 independent native pairings and three new cross-source symmetry overlaps pass. Four additional overlaps agree with CC3's independently repeated degree-112 native/action quantities.

| Certified quantity | Display |
| --- | ---: |
| Two-trial inverse credit lower | 1.423758453096636e-32 |
| Original completed-Schur directional lower | 1.351579870198155e-32 |
| First shifted-head quadratic lower | 4.692002927056879e-33 |
| First shifted-head quadratic upper | 2.146595595181053e-32 |
| Residual squared / original source norm squared upper | 0.620127591165301 |
| Physical shifted-solve error squared upper | 1.199853578308559e-32 |

All decisions use stored rational endpoints. The new credit is strictly more than twice CC3's entire credit upper endpoint. The resulting ORIGINAL completed direction is strictly above 1.35e-32, compared with CC3's earlier >6.24e-33. This is a certified improvement on the same coefficient direction, not a finite trial Rayleigh value relabeled as a Schur lower bound.

The first shifted-head enclosure is deliberately broad: its residual remains substantial. In particular its head-solve error is much larger than CC7's <2e-37 series-tail budget. Displaying that small tail alongside this broad actual solve does not produce a precision certificate for a 129-term head.

Nevertheless the actual first head plus its ENTIRE remaining original inverse tail already gives a second lawful original Schur lower bound. On lambda>=c,

    0<=1/lambda-1/(lambda+c)<=1/(2c).

Therefore

    <B,C^(-1)B> <=head_upper+||B||^2_upper/(2c),
    S(v)>=q_native_lower-head_upper-||B||^2_upper/(2c)
         >5e-33 (display 5.082603950306632e-33).       (5)

Equation (5) is the first ACTUAL shifted-head-plus-whole-tail sign test on this source direction. It does not use an unevaluated head or set the head residual to zero. It is weaker than the two-trial unshifted credit result but independently demonstrates how the resolvent construction can be consumed correctly.

The physical L2 source errors are bounded by approximately 1.14670e-55, 2.03191e-49 and 6.90009e-48 for the witness, degree 112 and degree 114 respectively. Integration degree is 1228. The midpoint coefficients remain only proposals; each quoted sign includes all source, normalization, panel and moment intervals.

## 5. Controls, relative loss and custody

Twelve exact genuine three-dimensional complement cases verify the original inverse square, all coupled action blocks, the nondecreasing optimized two-trial credit, the shifted quadratic enclosure and physical solve-error bound. The source-norm extraction keeps both complete source-error terms. Four independent CC3 pairing overlaps, the strict doubled-credit inequality and both actual directional sign tests are also checked. These finite controls do not stand in for the actual three-source integrations.

NF66's strictly positive supported error floor is read and preserved. A fixed retained-tail comparison can fail before a hypothetical original contact; representation accuracy remains distinct from original arithmetic relative-loss nondivergence. CC8 evaluates the ORIGINAL shifted operator, so it supplies no new approximation argument against such a contact.

The complete original source identity, active prime-power weights, orientations, exact signed pole and threshold zero-overlap remain intact. The shift tau is used only for L inverse and is explicitly undone whenever the unshifted inverse is bounded. It is not a positive original eigenlevel relabeled as zero, and it does not move the original Schur target.

Only the compact native archive is decoded and hash-checked. The binary 112-source and residual-Gram archives are not replayed. This reconstruction creates three actual sources, not a new full source family. CC3, CC7, NF66 and historical custody remain unchanged. No full target Schur sign, new positive aperture, original contact exclusion, arithmetic accumulated-loss nondivergence, RH/F4, full transport or Lean result is claimed.
