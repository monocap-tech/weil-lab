# RPB108: complete matched 9/10 residual and estimator obstruction

Matched input custody: `8989e6db22b8d9d1a800000b7bc5b39abef0ff2b`.
Recovery constructor custody: `80c318af093daf61302e062d3994f3ee0ab1c8f4`.
Definitions: [matching 9/10](../docs/TERMINOLOGY_RPB108_PRIME5_84_SCHUR_090.md), [panel recovery](../docs/TERMINOLOGY_RPB108_GRAM_CHECKPOINT.md), [estimator audit](../docs/TERMINOLOGY_RPB108_PRIME5_090_ESTIMATOR.md).

Both complete actual 84-source residual Gram runs reproduce byte for byte. Their nine-panel cumulative checkpoint states also agree exactly; each run used its own independent checkpoint. The complete outputs, not checkpoint agreement alone, establish repetition. All 7,056 actual source/native comparisons pass, every mixed term and all 84 projected coordinates are retained, and the maximum entry width is approximately 3.041949685829048e-114. The actual Gram operator-error correction is approximately 1.6082746171179735e-35.

At the certified complement c=149/250, beta=250/149, the sufficient estimator has a rigorous negative direction after including the actual source correction. Its estimator Rayleigh upper bound is approximately -4.8863202507077115e-24, while its native Rayleigh lower bound is approximately 4.1619269176484736e-22. The actual full form has not been shown negative.

The independent stored-vector audit recomputes the native and residual energies at a fresh 100-digit interval grid, verifies native/source hashes, all 84 projection coordinates, symmetry, the residual trace bound and delta=eta(2M+eta). Both audit reports reproduce byte for byte. The directional complement requirement lies approximately in [0.6029973522530454,0.6029973522531227]. The present integrated complement proof supplies an unrounded lower bound approximately 0.5969032507427541; merely rounding that lower bound more tightly cannot resolve this audited direction. This comparison does not bound the actual complement from above.

Canonical data:

- `notes/data/RPB108_PRIME5_GRAM84_090_CERTIFICATE_20261006.json`: SHA256 `05f214a7a8dce93b75523cdcbe52265cbe365a72c717757fd9de3697ede6e6cc`; Git blob `b0449b3c27585b7c2aa35b08f2d275c259bc4462`.
- `notes/data/RPB108_PRIME5_ESTIMATOR_NEGATIVE_090_VALIDATION_20261006.json`: SHA256 `caff9da3e8f6b92a45313c20d97c0ba5c3552760a813a65c58e09ebd97fa4b2e`.

The full residual is reusable. Next is a stronger certified complement or lift estimate with a fresh corrected sign; increasing retained dimension requires fresh matched native/source inputs. The actual fixed-aperture whole-domain frontier remains 22/25. Global endpoint exclusion, retained historical packet attachment, F4 and FULL TRANSPORT CLOSED remain open. Historical notes, Lean, axioms, workflows and CI configuration are unchanged.
