# RPB-108 — regularity from actual central cancellation through an inner collar

Date: 2026-10-02 (America/Los_Angeles).
Recovered research head: ec1b0fa24e853d604f7a2feab8283dcf55fea4f4.
Terminology: [inner collar with fixed cutoff](../docs/TERMINOLOGY_RPB108_INNER_COLLAR.md).

## Standing and purpose

**Mathematical standing: written analytic reduction conditional only on actual central cancellation and the existing carrier/symbol hypotheses. Formal certification: NOT YET LEAN-CERTIFIED. Actual WD-T38 witness instantiation: OPEN.**

This pass identifies a route that eliminates an independent spectral operator-domain or defect-representation assumption once actual central cancellation has been attached. It neither supplies central cancellation nor packages another representation premise. No Lean source changes, new axioms, or stronger hypotheses are introduced.

## The actual attachment obstruction

The retained WD-T38 constructor supplies a named density, symbol, Q and pole, separately from its abstract physical vector and endpoint operators. Its density/log-energy integrability witnesses now survive in its arithmetic output. The constructor still contains no equation identifying the named density with the actual normalized Fourier norm-square density; no equation identifying Q with sourceDomainQuadratic of the physical vector; and no same-domain identification of the selected/effective synthesis defect with the full geometric source form.

Consequently an actual physical carrier's canonical logarithmic form membership cannot presently be obtained merely by applying the retained named-density witness. The existing diagonal, mixed-form and normalized comparison bridges do not fill those identification equations. Endpoint restricted nullity also does not give cancellation on the larger interval (-a,a), c<a. The source realization and enlarged cancellation remain the priority obligations.

## Analytic reduction with no spectral L2 premise

Write A_a(u) for the actual frozenWeilCompactAction and p for the actual neutralWeilSourcePole. Retain 0 <= c < a and RightLimitWeilSymbolTemperatePremise a. Suppose the required actual central witness is available:

A_a(u)=0 for every compact Schwartz test with tsupport u contained in U=(-a,a).

Choose c<b<a, put V=R\\[-b,b], and define

g_b(x) = neutralArchimedeanGapFunction carrier (b-c) x
         - neutralFinitePrimePhysical carrier (rightLimitPrimePowerFinset a) x
         + p(x).

The cutoff in the physical prime sum is a, not b.

1. **Local integrability is constructed.** The gap convolution is continuous by neutralArchimedeanGapFunction_continuous. The finite prime function is locally integrable by neutralFinitePrimePhysical_locallyIntegrable. The actual pole is locally integrable by neutralWeilSourcePole_growthData. Thus g_b is locally integrable without global spectral membership.

2. **The auxiliary symbol premise is derived.** In the mathlib frequency coordinate, the exact identity is symbol_b = symbol_a + prime_a - prime_b. Temperate growth follows from the retained premise at a and neutralFinitePrimeSymbol_temperate. This does not posit a fresh source realization, change thresholds, or discard any shell.

3. **The certified exterior attachment supplies A_a on V.** Apply neutralArchimedeanMultiplierCore_exterior_pairing at b using the derived symbol premise. Combine it with neutralWeilMultiplierCore_eq_archimedean_sub_prime at a and the actual pole pairing. For every compact Schwartz test vanishing on (-b,b),

A_a(u) = integral u(x) g_b(x) dx.

Both prime and pole pairings converge by their existing integrability theorems. The multiplier's archimedean part is independent of the auxiliary radius; its prime part remains frozen at a. This consumes the existing exterior/digamma work.

4. **Compatibility on the overlap is proved.** Every compact test supported in U intersect V is central and also an exterior test for b. Its g_b pairing is zero. Apply locallyIntegrable_ae_zero_of_compactSchwartz_on_open to obtain g_b=0 almost everywhere on U intersect V.

5. **Identify the existing concrete residual on V.** Let r_a=neutralExteriorResidualCandidate carrier a. It is already locally integrable and is zero on U. On the complement of U, every displacement from the carrier has magnitude at least a-c, so both gap truncations a-c and b-c give the same untruncated kernel. The prime cutoff and actual pole are identical. Therefore r_a=g_b outside U, pointwise, and r_a=g_b almost everywhere on V by step 4. There is no boundary distribution inferred from a pointwise formula.

6. **Attach all compact tests by a smooth cutoff.** Choose a real smooth compact cutoff chi equal to one on a neighborhood of [-b,b], with support contained in U. For a compact Schwartz test u, split

u = chi*u + (1-chi)*u.

Both terms are smooth compact functions, hence compact Schwartz tests. The first has support in U, so its A_a pairing and r_a pairing are zero. The second vanishes on (-b,b); step 3 computes its A_a pairing, and step 5 replaces g_b by r_a almost everywhere on its support. Additivity of A_a is frozenWeilCompactAction_add, and integral additivity is lawful by local integrability and compact support. Hence

A_a(u) = integral u(x) r_a(x) dx

for every compact Schwartz test.

7. **Consume boundary removal immediately.** The actual compact source defect is now identically zero on all tests. The function q_defect=0 is a locally integrable representative of that actual defect; it is not an assumed representation field. Feed this witness and the same central witness into neutralExteriorIntegralGrowthResidual_realizes_of_regular_cancellation from 592eaf7. This certifies whole compact weak realization once the reduction has been formalized and the central witness has actually been supplied.

The argument removes the independent regularity obligation after central cancellation: the strict margin c<a provides an open cover of the two boundary points by the inner collar. No new boundary analysis is required.

## Exact outstanding formal work

Formalize the derived temperate premise at b, fixed-cutoff inner-collar pairing, almost-everywhere overlap compatibility, and smooth compact cutoff split; assemble step 7 using the existing theorem. These are consequences of the existing analytic objects plus central cancellation, not new source premises. This written reduction is not a claim that those new assembly statements have already passed Lean.

Before claiming an actual realization, attach the original source form-domain/quadratic witness and derive actual enlarged central cancellation. The current repository still has no recovered concrete WD-T38 instance doing this.

## Spectral membership and scope

MemLp (neutralWeilSpectralProduct carrier a) 2 is **not derived and not assumed**. Named-density one-logarithm integrability is not yet carrier energy; even actual one-logarithm form energy does not by itself imply the squared-symbol L2 condition. This pass stops that stronger route and supplies the locally integrable collar strategy above.

The regularity reduction is conditional on actual central cancellation; central cancellation itself is OPEN. Whole compact realization and source quadratic/polarization/normalized attachment remain OPEN for the actual WD-T38 carrier. Threshold bookkeeping stays CLOSED. F-4 logarithmic Gaussian coercivity is NOT STARTED. WD-T40 and RH standing are unchanged.

## Verification

Checked the argument against the exact definitions and certified identities in NeutralArchimedeanExterior, NeutralExteriorResidual, NeutralWeilCoreSplit, NeutralExteriorAttachment, NeutralExteriorSourceAttachment, NeutralWeilFrozenExtension, and NeutralSourceBoundaryRemoval. No Lean modules, root imports, dependencies, toolchain, workflow or certified source blobs are changed. The prior whole-root certificate at ec1b0fa remains the source certificate; this documentation pass has no new Lean certificate.
