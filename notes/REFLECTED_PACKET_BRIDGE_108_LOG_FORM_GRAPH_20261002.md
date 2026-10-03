# RPB-108 — concrete logarithmic energy graph

Continues from `c4a8107a7f4975ee089d115b4825928ab3d2cb24`.

`NeutralLogFormGraph` constructs the actual L2 class of
sqrt(log(e+|xi|)) times the normalized Fourier transform of every vector in the
canonical supported logarithmic domain. Its existence is proved from that
domain's finite one-logarithm energy. The physical vector and this energy
coordinate form an injective complex linear map into L2 × L2. The pulled-back
product norm is the maximum of the physical L2 and energy L2 norms; triangle,
complex homogeneity and positive definiteness are proved.

This is a concrete topology reconstruction step, with no new source-identity
or spectral operator-domain assumption. It does not redefine the canonical
subtype's inherited L2 topology, install a complete Hilbert structure or identify
the graph with the retained source space. Completeness/closedness, actual carrier
membership and the actual source form/observation map remain open. Source
quadratic/polarization/normalized attachment, enlarged cancellation, actual
regularity and whole realization remain open. Threshold bookkeeping is closed;
logarithmic Gaussian coercivity has not started.


Certification: Lean 4.34.0 / pinned mathlib `5ed2965256430c3649e86755f9576b54eca72435`; 8,986 build jobs passed. Seven endpoint audits use only `propext`, `Classical.choice`, and `Quot.sound`; unfinished-declaration gate passed. Validation head `155bd3435303813ae8afc633d13a2abad62b0647`, run `37080997568`, job `111081267718`, source blob `6a25651c2c54d7ff9e4d20d4b410b56b7d5047a3`.

Next: establish graph closedness/completeness and reconstruct the retained source identification, then attach the actual carrier and source identity. The weakest locally integrable defect route remains the regularity target; spectral-product L2 membership is not established from WD-T38 and is not assumed here.

Audited endpoints:

- `neutralLogWeightedFourier_memLp`
- `neutralLogWeightedL2_coe`
- `neutralLogFormGraphEmbedding_injective`
- `neutralLogFormGraphNorm_eq_max`
- `neutralLogFormGraphNorm_add_le`
- `neutralLogFormGraphNorm_smul`
- `neutralLogFormGraphNorm_eq_zero_iff`

Validation-only workflow/cache changes are excluded. The original research workflow remains unchanged. No canonical or WD-T40 standing is promoted.
