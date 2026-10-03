# RPB-108 — canonical diagonal and mixed logarithmic energy

Continues from `5b17412df5ee039020f577872ae529656da0bc2c`.

`NeutralLogFormEnergy` proves that every canonical-domain vector's actual weighted Fourier L2 coordinate has squared pointwise norm equal almost everywhere to the canonical logarithmic density. Its squared L2 norm equals the genuine real logarithmic energy integral. For any two vectors on this same domain, the two energy coordinates' inner product equals the mixed logarithmic Fourier pairing, whose integrability is proved from L2 Hermitian integrability and actual a.e. representative laws.

These are unconditional identities for the constructed canonical objects. No imported source quadratic identity, actual carrier membership, strict null-persistence or spectral-product L2 membership is used or proved. In particular, this is the canonical log-energy form, not an identification of the full multiplier-plus-pole Weil form with WD-T38's selected operator.

The missing WD-T38 source realization remains the attachment frontier. Graph completeness remains an independent topology obligation; proving it alone will not identify the selected operator or attach its null identity. Source quadratic/polarization/normalized estimate attachment, enlarged central cancellation, locally integrable actual defect representation and whole compact realization remain open. Spectral L2 membership is not established from the retained WD-T38 hypotheses; the stronger route remains stopped. Threshold bookkeeping is closed. Logarithmic Gaussian coercivity has not started.

Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,987 build jobs passed. Five endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; unfinished-declaration gate passed. Validation head `7483613d34ce8e0bd8b34d76627a5d7541040d94`, run `37083393114`, job `111088555146`, source blob `8b91dba883fc31e1e77645dd2ffe67546c6e8bb4`.

Audited endpoints:

- `neutralLogWeightedL2_sq_norm_ae`
- `neutralLogWeightedL2_mixed_ae`
- `neutralCanonicalLog_mixed_integrable`
- `neutralLogWeightedL2_inner`
- `neutralLogWeightedL2_norm_sq`

Next substantive obligation: reconstruct the actual selected source form-space map into physical L2 and its same-domain form/observation identification. Further topology construction alone cannot supply this missing identification.

Validation-only workflow/cache changes are excluded. Historical notes and canonical/WD-T40 standing remain unchanged.
