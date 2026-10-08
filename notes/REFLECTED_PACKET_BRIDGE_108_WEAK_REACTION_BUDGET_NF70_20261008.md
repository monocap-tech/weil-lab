# RPB108 NF70: actual weak-channel reaction budget at aperture 21/20

2026-10-08 UTC / 2026-10-07 Pacific. Global base `1f775b9102814625192e3cbe4bae329738c8f4c7` (NF69); inspected Coupled `faa030e98bd0bcf4826a3044b241d25e64d739b2` (CC9) read-only. Definitions: [weak reaction budget](../docs/TERMINOLOGY_RPB108_WEAK_REACTION_BUDGET.md).

**Result.** This step evaluates an actual arithmetic budget, rather than another abstract coordinate construction. CC9's positive completed two-plane yields a deterministic lower matrix, an exact finite inverse UPPER bound, and a concrete dangerous mixed row. Its weak remaining lower gap is about 1.368075812642414e-32, with inverse coefficient about 7.30953643620464e31. The complete available absolute estimates for that row pay a weak inverse-reaction upper budget about 389.23. Including the strong row gives about 414.52.

These large numbers are UPPER estimator budgets, not actual reaction values, negative witnesses or proof of a closing gap. They quantify why absolute source boundedness does not provide the missing relative arithmetic control. Actual completed correlations with the other 110 directions are still unevaluated. This calculation identifies a concrete mixed-row target and its required scale inside the already certified plane.

## 1. Actual pinned inputs and byte custody

Read CC9's certificate at the pinned Coupled head, retaining its entire original two-column residual credit, mixed entries, normalization and source errors. Its certificate is copied BYTE IDENTICALLY into Global for reproducibility; Git blob 49ca3c54438f439d65f8c1c12da27de1204fefcf. The Coupled ref is untouched.

The native compact112 archive at a=21/20 is decoded and its uncompressed SHA256 checked:

    0499d604127a76afcea90f314e09824e2f327c43a01b8aa2471e2d797c51b7f8.

The original saved Schur certificate carries this SAME native hash, c=699/1000 and complete source-map bound M=surrogate norm+actual source allowance<8. The full binary residual-Gram archive is not replayed: the >1MB contents read returned no payload and the blob reader could not decode binary as UTF-8. The native compact archive and CC9's newly reconstructed actual two-plane source Gram suffice for the calculation below. The saved whole-source norm bound is imported with pins, not reconstructed from the compact native matrix.

No whole inverse matrix is extracted from CC9's four-source reconstruction. No zero/divisor source prefix is substituted.

## 2. Deterministic lower plane and exact inverse metric

Let S_V be the EXACT original completed Schur matrix on CC9's retained plane V=span(h,u), where h is the saved rational coefficient witness and u the defined rational physical constant. These vectors are independent but not physically orthogonal.

CC9 encloses a certified matrix Lower with S_V>=Lower. From the complete outward intervals, take the symmetric rational midpoint m and radius e=max_i sum_j radius_ij. Then

    G0=m-e I <=Lower<=S_V,
    G0=[[a,b],[b,d]]>0.

The row-radius subtraction is a WHOLE Loewner allowance, including the mixed entry. G0 is a deterministic rational matrix, not an entrywise-lower matrix with an unproved Loewner order. Define

    rho=b/d,
    ell=a-b^2/d>0,
    hweak=h-rho u.

Exact inversion gives for any mixed coefficient pair (z_h,z_u),

    z*G0^(-1)z
      =|z_h-rho z_u|^2/ell+|z_u|^2/d.              (1)

As S_V>=G0>0, inverse order yields S_V^(-1)<=G0^(-1). The inverse coefficient in (1) is therefore a lawful UPPER reaction allowance. It is not the actual inverse of S_V and supplies no lower bound on its reaction.

Stored exact rationals give conservative displays:

| Quantity | Display |
| --- | ---: |
| ell, weak plane margin | 1.368075812642414e-32 |
| rho=b/d | -3.908378862784848e-17 |
| 1/ell, weak inverse coefficient | 7.309536436204640e31 |
| 1/d, strong inverse coefficient | 27.18538709488628 |

The original native h/u coupling is POSITIVE, about 2.738743893982963e-18. The certified completed LOWER-plane coupling b is NEGATIVE, about -1.437676369714094e-18. The full inverse reaction changes the mixed entry's sign; using native correlations alone would change the required cancellation in (1). All signed terms are retained.

The weak direction is a direction WITHIN this certified plane. No claim is made that it is the sole critical direction of the whole112 form; the other 110 coordinates remain unresolved.

## 3. The exact remaining mixed row

After eliminating the ORIGINAL F112 complement C>=c I, let S be the exact completed112 form. For any retained remainder vector r, its cross pair with V is

    z_h=S(h,r), z_u=S(u,r),
    z_h-rho z_u=S(hweak,r)
      =Q(hweak,r)-<B_hweak,C^(-1)B_r>.             (2)

Here B is the ACTUAL projected physical source map, not a divisor-coordinate prefix. Both terms in (2) have the same original vector and all native/source normalization. A possible whole test must preserve their correlation and the sign in (2).

For a retained remainder coordinate map R, put J=S restricted to R and Z=(S(h,R),S(u,R)). Exact second square completion has remaining gate

    J-Z*S_V^(-1)Z.
    
Using (1) gives the sufficient LOWER form

    J-ell^(-1) Zweak*Zweak-d^(-1) Zu*Zu,           (3)
    Zweak=Z_h-rho Z_u.

Equation (3) keeps EVERY remaining column and their mixed products. It requires an independent lower enclosure of J and upper Gram enclosures for the entire completed mixed rows. Positive individual diagonal tests or a finite trial subset do not establish it. No such full J or completed row Gram is evaluated here.

One can choose any independent 110-vector quotient complement of V in E112, provided its physical mass Gram is retained. The absolute bounds below hold on the WHOLE E112 mass-unit sphere, so they remain lawful on any physically orthogonal remainder without inventing one from floating eigenvectors.

## 4. Actual whole-native row plus imported full-source estimate

From the compact native112 matrix compute all 112 entries of its action on the SAME hweak, paying outward interval endpoints and the rational constant's normalized coefficient nu sqrt(21/10). Their interval squared magnitudes give

    ||A112 hweak||_2 <=2.645436655338585e-16.

This is an actual WHOLE retained native row bound, not a one-direction Rayleigh quotient. Three independent overlaps agree with CC9's separately reconstructed native witness energy, native witness/constant coupling and native constant energy.

CC9's complete actual projected two-plane source Gram gives

    ||B_hweak||_2 <=1.952574509585399e-16.

This includes the witness's odd-source allowance, all source errors, all mixed retained products, both signed poles, all six active prime powers with their exact weights and orientations, and every retained projection. The imported complete112 source bound supplies ||B_r||<=M||r||_2, M<8. Therefore C>=699/1000 gives the legitimate absolute whole-row bound

    |S(hweak,r)|
       <=[||A112 hweak||+M||B_hweak||/c]||r||_2
       <=2.307583961300505e-15 ||r||_2.             (4)

Dividing its squared coefficient by ell yields

    ell^(-1) Zweak*Zweak <=389.2287027694976 I.     (5)

The same construction on u gives |S(u,r)|<=0.9645563966474946||r||_2. Adding its strong reaction allowance gives

    ell^(-1) Zweak*Zweak+d^(-1)Zu*Zu
       <=414.5211453258914 I.                     (6)

The recorded exact rationals, not rounded displays, control every inequality. This is a finite, genuine entire-row upper budget. The tiny native/source amplitudes in (4) do NOT by themselves imply a small relative reaction because (1) divides by the tiny certified weak margin.

Crucially, (4) uses the triangle inequality between two arithmetic terms. It bounds their possible size and does not evaluate their actual cancellation. Nothing in (5)-(6) says the actual reaction is near those upper values. Failure to certify a useful lower matrix with this budget is an ESTIMATOR limitation, not proof of negativity.

## 5. Concrete conditional scales for an improved mixed-row estimate

For illustration only, suppose the unresolved remainder J were independently known >=kappa I. Reserving half its budget for the weak term in (3) would require

    ||Zweak||^2 <ell kappa/2.

Certified conservative thresholds for that conditional test are:

| Hypothetical remainder margin kappa | Sufficient weak-row norm threshold |
| --- | ---: |
| 1 | 8.270658415877222e-17 |
| 1/100 | 8.270658415877222e-18 |
| 1e-32 | 8.270658415877222e-33 |

These are NOT known remainder margins, evaluated mixed-row norms, necessary conditions or actual contact predictions. The strong row still requires its separate half-budget. They translate a future independent matrix gap into the precise completed arithmetic-correlation scale to be certified.

The native entry widths and CC9 source errors are already paid in this calculation. Repeating source precision improvements without calculating the correlated difference in (2) would not remove the absolute inverse-estimator amplification. This statement does not preclude precision work if a future actual cancellation computation needs a smaller enclosure.

## 6. Structural implications and next substantive task

NF69 identifies the source finite gate and physical Schur gate by inertia. NF70 now puts an actual numerical weak-correlation target into that physical chart, using the concurrently improved CC9 plane.

The next substantive input is an enclosure of the COMPLETE ORIGINAL mixed row in (2), with a compatible remainder lower form, or a direct matrix residual solve giving the entire J/Z inverse reaction. Do not infer original accumulated-loss nondivergence from (4), finite source boundedness, finite output rank, the passed plane or its protected infinite slice.

CC9's protected codimension110 slice is preserved. Its positive margin supplies a dimension bound, not a guarantee that all remaining directions are positive or that the actual singular output is only one-dimensional. The fixed-aperture calculation here is not a moving-aperture derivative or a finite-aperture nondivergence theorem.

Positive physical eigenlevel mu still requires the extended negative channel (N,sqrt(mu)physical). This budget is for the ORIGINAL unshifted Schur matrix; no level is shifted to zero. Prime-power activation equality keeps zero physical overlap, and neither signed pole is suppressed.

## 7. Validation and scope

Script: [certify_native_weak_reaction_budget_nf70.py](../scripts/certify_native_weak_reaction_budget_nf70.py). Uses existing exact outward rational interval helpers. It checks compact native byte custody, independent aperture/source bindings, deterministic plane positivity, exact inverse/shear identities and three independently constructed native overlaps. The lower-margin, full absolute source allowance and conditional thresholds are verified rationally.

Saved certificate: [NF70 budget](data/RPB108_WEAK_REACTION_BUDGET_NF70_CERTIFICATE_20261008.json). Input source constructions are imported with custody; full binary Gram and source archives are not replayed. The native compact112 archive IS decoded/hash-checked, and all 112 native weak-row entries are evaluated.

No actual remaining completed-row norm, remaining110 sign, whole-domain aperture certificate, negative vector/contact, original global gain, arithmetic nondivergence, RH, F4, full transport or Lean closure. Only Global is published; Coupled and paused Aperture/Shadow refs are untouched. Historical NF69 and CC9 remain unchanged.
