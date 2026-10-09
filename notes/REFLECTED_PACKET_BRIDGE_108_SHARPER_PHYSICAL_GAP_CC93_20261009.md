# CC93: sharpen the conditional physical restriction gap

CC parent: 9183934b66e7cd647ac9def9f6ea6290c17e9b23 (CC92). Read-only Native Source remains NF46 6658ff2837838ab00b9b9c605fdd200d473c3293. Other branches are unchanged. No new native polynomial or integration is introduced.

## Result

On the same original six-retained-direction-plus-all-F restriction at aperture 53/50, the conditional physical gap improves from CC92's value above 1.1503e-52 to

    Q_original(h) >= g ||h||_L2^2,
    g > 2.7863e-38.

The exact rational lower bound is saved in JSON. This is over 2.4e14 times the previous conservative bound. The change recovers information lost in the earlier matrix-to-coordinate estimate and replaces its uniform lifted-mass bound by actual paid norms. The original packet, physical restriction and hypotheses remain unchanged.

The theorem still assumes A >= (207/1000)I on the remaining high space and the original block/form-domain attachments specified in CC92. It applies on the attached original form domain, not all physical L2 vectors. It does not prove the remaining-high floor or complete transport.

## Inverse-trace coordinate estimate

For positive definite K=[[E,r],[r*,c]], put beta=E^-1r and s=c-r*E^-1r>0. Exact block inversion gives

    trace(K^-1)=trace(E^-1)+(1+||beta||^2)/s.

The largest eigenvalue of K^-1 is no larger than its trace, so K >= [trace(K^-1)]^-1 I. Use the paid leading inverse's diagonal upper endpoints, squared absolute upper bounds for beta, and a positive lower endpoint for s to enclose the trace above. No eigenvalue sampling or numerical diagonalization decides this bound.

CC92 used min(lambda_lower(E),s)/(3+||beta||^2), which applies the large triangular-map penalty to the entire leading block. The inverse-trace estimate retains how the positive leading block and condensed term enter the inverse separately. The new coordinate lower bounds exceed 2.2290e-37 even and 4.6966e-35 odd.

## Actual lifted physical mass

CC92 already authenticated the complete mass/lift chain. CC93 uses it quantitatively. For each parity, bound the old seed norm by sqrt(retained seed mass) plus its paid high-correction norm. Bound the NF29 response norm by the square root of its exact squared mass; for even add the sum of absolute NF30 additional coefficients. Bound the NF34 witness by its paid retained and high norm upper bounds. Finally add each exact NF37 functional coefficient times the NF36 correction norm.

All square-root upper bounds are rational: a scaled integer square root is rounded upward and its square checked against the exact input. Sum the three squared resulting upper norms to bound ||V||^2 by the physical Gram trace. This avoids assuming lifted-vector orthogonality. The mass bounds are below 2.000000000022 even and 2.000000000406 odd, far below CC92's conservative 12; exact endpoints remain in JSON.

With D >= ||A^-1R||^2 from CC92's authenticated complete physical source Gram and kappa=207/1000, the same completion-square proof gives

    g_parity=min(epsilon/[4(M+D)],kappa/2).

Take the smaller parity gap. Exact parity still joins the two restrictions, and all NF37 lift changes retain the original restriction identity. No new physical domain extension is used.

## Validation and next assembly

The validator reruns CC92's custody, original inverse-packet identity, positivity and physical completion checks, then recomputes the inverse-trace and actual-mass bounds. Exact controls at ordinary and small coordinate scales verify the inverse-trace identity and positivity after its matrix shift. Rational square-root controls cover zero, irrational roots and very small masses. Each parity gap is strictly larger than its CC92 predecessor.

For full retained assembly, the appropriate next packet is the complete signed cross block between these six retained directions and the remaining retained frame, together with that frame's native/source data. The positive current packet must enter that joint matrix through its full inverse; a separate positive diagonal restriction does not pay mixed coupling. This sharper scalar physical gap is available for a justified norm estimate, but it does not substitute for those covariances or prove an old-gap-independent all-cap bound.

The other 106 retained directions, collective coupling, unconditional background floor and complete remaining-background transport remain open. Whole-domain certified aperture stays 21/20. Whole 53/50, all-cap continuation, RH, F4, full transport and Lean closure are not claimed.

## Reproduction

Run `python scripts/certify_cc93_sharpen_physical_gap.py notes/cc92-source notes/cc91-source notes/cc87-source notes/cc85-source --output notes/data/RPB108_CC93_SHARPER_PHYSICAL_GAP_20261009.json`. The immutable source packets already imported by CC92 suffice.
