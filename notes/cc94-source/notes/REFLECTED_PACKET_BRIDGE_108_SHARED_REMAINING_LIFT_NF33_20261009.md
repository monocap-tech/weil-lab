# RPB108 — NF33: a shared remaining high lift, with certified floor rejection

2026-10-09 UTC. Phase Geometry parent NF32 is
`a2e155a631a3a719c2f53ab629c501d0fe105747`. Coupled CC74 was read only
at `9ed50ac8b568cb9c5a986abd6d6a3a28aac3c9ed`. No other branch is
modified. Definitions precede use in the additive
[NF33 terminology entry](../docs/TERMINOLOGY_RPB108_SHARED_REMAINING_LIFT_NF33.md).

## Result

NF33 constructs one fixed rational two-high-mode lift for all 54 remaining
retained columns in each parity. Both lifted finite native energy matrices
are rigorously positive. All 216 original selected-shell pairings are
enclosed, and the physical selected-shell operator norms are extremely
small. The unchanged NF32 constraint coordinates are then carried through
this same shared map; the complete original physical sources of the two
resulting witnesses are certified.

Both witnesses still have strictly negative floor scores. This rejects
the collective scalar-floor estimator for this particular shared lifted
family regardless of its uncomputed source Gram entries. It does not
assert an actual negative original-form vector or failure of larger high
lifts or sharper inverse response estimates.

| Strict certified quantity | Even | Odd |
| --- | ---: | ---: |
| Physical finite lifted-frame gap | >5.4721e-22 | >3.6139e-19 |
| Selected-shell physical operator norm | <2.5592e-68 | <3.6639e-68 |
| Lifted witness native energy | (5.4988297,5.4988298)e-22 | (3.6145518,3.6145519)e-19 |
| Complete projected source square | (1.4081129681,1.4081129685)e-22 | (7.5638614217,7.5638614219)e-20 |
| Source square / native energy | (0.2560750254,0.2560750256) | (0.2092613921,0.2092613922) |
| Inherited floor budget | 0.207 | 0.207 |
| Lifted witness floor score | (-1.3036483590,-1.3036483573)e-22 | (-3.948753172,-3.948753168)e-21 |

The source-square/energy ratios improve from NF32's approximately
0.2921609901 and 0.2117176274. Selected-shell suppression alone does not
control the complete high source. No additional precision in the present
two-mode lift can change the certified negative scores.

## One shared rational map and physical finite energy

Reconstruct the exact NF31 basis T of E intersect span(x,w)-perp from
the authenticated retained seed and response. Use H2=(e112,e114) even
and (e113,e115) odd. Original signed finite native entries give
C2=Q(H2,H2) and K=Q(H2,T). A verified inverse enclosure of C2 selects
a rational map Z from the midpoint of C2-inverse K, with every entry
rounded downward to denominator 10^100. Selection is not a sign proof.

The fixed trial frame is U=T-H2 Z. It preserves all 54 independent
retained columns. Its exact physical mass matrix is
G=T-star T+Z-transpose Z; its native energy matrix is

\[
L=Q(T,T)-K^{\mathsf T}Z-Z^{\mathsf T}K+Z^{\mathsf T}C_2Z.
\]

Decimal arithmetic chooses rational congruence and inverse
preconditioners only. Outward rational congruence/Gershgorin positivity
and the inverse residual row norm below one prove L>0. The reciprocal
of the certified upper bound on trace(L-inverse G) gives the displayed
physical finite energy gaps. Thus mass conversion includes the shared
high lift and the nonorthonormal constraint basis.

Every entry of K-C2 Z is certified. The 54 free retained coordinates
are an identity submatrix of T, so G>=I. A maximum entry bound b on
this 2-by-54 matrix gives physical operator norm at most sqrt(108)b<11b.
These are bounds on the selected shell, not on all of F.

## Complete original sources of inherited lifted witnesses

For each exact NF32 constraint vector a, the new witness is u_Z=Ua.
The same shared map is used; no individual source optimization selects
these witnesses. Their retained components remain exactly orthogonal
to x and w. Native energies use the complete signed finite116 form,
including both high components, not approximate unit-mass source
integration. The validator independently expands the full quadratic
form and compares it with both the frame congruence and the source
certificate's native-energy enclosure.

The complete source uses the exact endpoint logarithm and removable
singularity polynomial, rational regular kernel N320, degree40 pole
approximation with its paid tail, and all thirteen original prime
translation cells. Exact polynomial/log/log-square moments include
every arch/prime/pole cross. The outward grid has 500 decimal digits;
no quadrature or sampling is a proof input.

Original native retained source coordinates define P_E L_original u_Z.
Subtracting their midpoint polynomial leaves a reconstructed P_F source.
Its physical error eta pays the degree-independent uniform kernel and
pole source errors and the retained midpoint ball (sqrt(56)<8). For
reconstructed squared norm s, the physical source-square payment is

\[
2\eta\sqrt{s_{\rm upper}}+\eta^2.
\]

The physical residual reconstruction errors are below 6.812e-22 in
both parities. Independently available original N720/K620 native
pairings against e118 even and e117 odd agree after source-error
payment. These unsquared checks include the signed high lift.

The source certificates give Q(u_Z,u_Z)-||P_F L_original u_Z||^2/kappa<0.
Since u_Z belongs to span(U), the complete shared-family floor matrix
on the successful pair plus U cannot be positive definite. Its missing
cross entries cannot remove this witnessed negative value. Actual
inverse-weighted high response can be smaller than this floor bound;
the original native witness energy itself remains positive.

## Reproduction and validation

The original NF24 native archives and inherited NF24/NF26/NF27/NF29/
NF30 inputs are hash authenticated. The exact NF32 trial is separately
hashed. The fresh frame and selection replays reproduce their certificates
identically. Independent checks verify exact retained membership and
physical mass, three-way native-energy overlap, source-square payments,
native projection overlaps and the negative floor scores. Python syntax
compilation passed. Machine certificates retain exact rational endpoints.

From the repository root with those original inputs staged:

```sh
python3 scripts/certify_native_shared_remaining_lift_nf33_106.py choose --output notes/data/RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json
python3 scripts/certify_native_shared_remaining_lift_nf33_106.py frame --trial notes/data/RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json --output notes/data/RPB108_NF33_SHARED_REMAINING_FRAME_CERTIFICATE_20261009.json
python3 scripts/certify_native_shared_remaining_lift_nf33_106.py source --trial notes/data/RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json --parity even --output notes/data/RPB108_NF33_EVEN_LIFTED_PROBE_CERTIFICATE_20261009.json
python3 scripts/certify_native_shared_remaining_lift_nf33_106.py source --trial notes/data/RPB108_NF33_FIXED_SHARED_REMAINING_LIFT_20261009.json --parity odd --output notes/data/RPB108_NF33_ODD_LIFTED_PROBE_CERTIFICATE_20261009.json
python3 scripts/validate_native_shared_remaining_lift_nf33_106.py --output notes/data/RPB108_NF33_SHARED_REMAINING_LIFT_VALIDATION_20261009.json
```

## NF34 obligation and boundary

The next useful step is a larger shared high lift targeted at the remaining
certified response, or a sharper justified inverse-weighted collective
bound. A passing witness would still leave the entire remaining source
Gram, its signed mixed covariance with (v,t), and the full collective
matrix sign to certify. The present two-mode shared family is rigorously
rejected by the scalar-floor estimator; merely completing its same Gram
or improving its numerical precision cannot repair that estimator.

The prior four-direction restriction with the entire original infinite
high complement remains certified. Finite lifted-frame positivity is not
whole-domain positivity. Highest internally certified whole-domain
aperture remains 21/20=1.05; whole aperture 53/50=1.06, RH, F4 and Lean
remain open. Historical wording and paused branches remain unchanged.
