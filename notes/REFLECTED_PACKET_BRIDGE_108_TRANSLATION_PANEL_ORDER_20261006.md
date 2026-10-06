# RPB108: actual translation panels across log(6)/2

Base: `40e16ff6d6fd78944cd01efa65f48291657dda64`.
Definitions: [translation-panel registry](../docs/TERMINOLOGY_RPB108_TRANSLATION_PANEL_ORDER.md).

## The collision changes actual source terms

The certified positivity frontier is a=22/25. The next larger target a=9/10 has d=2a=9/5, beyond log(6), with exactly the same active prime powers 2,3,4,5. Composite 6 has Lambda(6)=0; the first new prime term is 7 at d=log(7). The present change concerns the support of existing translations, not an added prime-6 term.

Let ell_n=log(n)/d and extend a polynomial p by zero outside [0,1]. Its forward translate p(t+ell_n) is supported for t<1-ell_n, and its backward translate p(t-ell_n) for t>ell_n, apart from endpoint values. The actual source contributes -Lambda(n)/sqrt(n) times each supported translate. These statements give identities almost everywhere on the physical L2 carrier; no boundary distribution derivative is used.

The two reflected cutoff pairs collide at

\[
d=\log 6=\log 2+\log 3,
\qquad \ell_2=1-\ell_3,\quad \ell_3=1-\ell_2.
\]

At 22/25 the old nine-panel order is valid. At 9/10 the order becomes

\[
0<1-\ell_5<1-\ell_4<\ell_2<1-\ell_3
<\ell_3<1-\ell_2<\ell_4<\ell_5<1.
\]

Exact rational logarithm enclosures prove every strict inequality at the new target. There are still nine open panels, but two active sets change. In the table, signs denote argument shifts; every source coefficient still has its original negative sign.

| Panel index | Old active shifts | Correct active shifts at 9/10 |
| --- | --- | --- |
| 3 | +2 | +2, -2, +3 |
| 5 | -2 | +2, -2, -3 |

For the degree-zero polynomial p=1, the unnormalized actual-minus-stale source difference on each of these panels is

\[
-\frac{\log 2}{\sqrt2}-\frac{\log 3}{\sqrt3}<0.
\]

The unchanged smooth core cancels in this difference. Physical normalization multiplies it by the same positive factor. Thus using the old active table beyond the collision changes an actual source even in degree zero; this is not merely a relabeling problem.

## Geometry interface and proof of support

The new `translation_panels(a)` interface encloses all eight forward/backward support cutoffs and the endpoints 0,1. It sorts candidate intervals, then requires each upper endpoint to be strictly below the next lower endpoint. Sorting midpoints alone is insufficient and never supplies the certificate.

For a panel between consecutive true cutoffs, a forward translate is active precisely when its cutoff lies to the right of the panel; a backward translate is active precisely when its cutoff lies to the left. Since each support indicator is monotone and every support cutoff is in the partition, its value is constant on that entire open panel. This proves the active-set formula for every interior point, independently of the later rational witness checks.

The implementation also checks exact reflected cut enclosures and maps every panel's active set to the reflected panel by reversing argument signs. An unresolved or coincident cutoff enclosure rejects. The geometry interface does not silently select a side of the collision when strict order is unavailable.

## Independent audit

Both audit runs agree byte for byte. At apertures 81/100, 41/50, 17/20 and 22/25, the generated active sets agree with every entry of the historical hardcoded nine-panel table. At 9/10, exactly panels 3 and 5 differ, with the mixed prime-2/3 translations listed above.

An independent rational witness inside each panel checks all eight translation arguments against [0,1], giving 72 support checks at each of five apertures, or 360 checks in total. These are implementation controls in addition to the whole-panel support proof. Both degree-zero stale-table source differences have strictly negative exact upper endpoints. Three invalid aperture-domain controls reject. A rational aperture whose cutoff enclosures are unresolved at the collision also rejects. Reflection passes at every audited aperture.

Reproduce with:

```sh
python scripts/validate_native_translation_panel_order.py > /tmp/panel-order-repeat.json
cmp /tmp/panel-order-repeat.json notes/data/RPB108_TRANSLATION_PANEL_ORDER_VALIDATION_20261006.json
```

## Next matching calculation and scope

This closes the support-order obligation for the target 9/10 and provides the lawful new active sets. The shared native/source constructors remain unchanged in this pass and still require an audited aperture extension. The next complete source constructor must consume these cuts and active sets consistently; its residual Gram must use the same order. Fresh native/source enclosures, all 7,056 pairings, the full Gram correction and a corrected sign remain necessary before claiming positivity at 9/10.

The certified whole-domain positivity frontier remains 22/25. No positivity at 9/10, global endpoint exclusion, historical selected-packet attachment or F4 closure is inferred. Historical notes and certificates are preserved; Lean, axioms and workflows are unchanged.
