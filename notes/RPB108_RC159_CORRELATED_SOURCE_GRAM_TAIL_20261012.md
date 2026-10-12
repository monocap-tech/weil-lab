# RC159: correlated source-Gram tail refinement

Resume from RC158 (`8ee21aeb4fdbebfca69ed28f30f836202a5e5061`) on `research/rpb108-route-consolidation`, aperture 11/10. Definitions are entered additively in `docs/TERMINOLOGY_RPB108_RC159_CORRELATED_GRAM_TAIL.md`.

RC158's strongest width witness was the seventh conditioned source direction. Its source-Gram enclosure width exceeded twice its certified lower energy. RC159 replaces the inherited independent diagonal tail majorant by a shared leading eta feature and a paid higher-moment remainder. The source frame, finite Gram prefix, and Gram lower remain unchanged.

The complete prescribed analytic source tails are recovered from RC128's w14 moments, RC131's v10 moments, RC132's z_b6 moments, and RC135's t10 moments. Their native scales are retained. Beyond even degree 16382, all tails share eta_n. Scale each polynomial at n=16384 and apply the full signed native-to-conditioned source transform before taking absolute values. The first three conditioned leading coefficients vanish exactly, preserving the cancellation in w14-alpha*psi0.

Write the conditioned tail as eta_n[a+sum_{k>=1}b_k x_n^k], with 0<x_n<=1 and ||eta_tail||_D^2<=T. For r_j=sum_{k>=1}|b_kj|,

\[G_{tail}\preceq(1+\tau)Taa^T+(1+1/\tau)7T\operatorname{diag}(r_j^2).\]

This bound holds for all real and complex signed source mixtures; no tail orthogonality is assumed. Seven rational tau values are tested. Every full Gram-width candidate is accepted by exact rational PSD bisection, rejecting the preceding 1e-6 grid point. The selected tau is 1/100.

The certified full source Gram width falls from **2.014662 to 0.036203 times the unchanged Gram lower**, improving the certified relative upper bound by **55.64903x**. On RC158's seventh-coordinate witness, the new Gram-width-to-lower-energy ratio is approximately **0.03314950**, compared with approximately 2.01077590 previously; its width improves by **60.65780x**.

The correlated upper is also transported back to native seven-vector coordinates, and its difference from the retained lower is checked PSD. No claim is made that two independently valid upper matrices are ordered in Loewner sense; improvement is assessed against the same positive Gram lower and witness.

The structural reference inverse enclosure (1/2)G_Lo<=Sigma<=G_Hi now has certified relative width at most **0.536203**, obtained by adding one half to the new Gram-width bound. It remains above the half-Gram target. RC159 does not rerun the variational inverse assembly or claim an inverse-width gate.

The source-Gram uncertainty that dominated RC158 is substantially reduced. Next: transport this correlated Gram bound into the conditioned functional and nominal residual intervals, preserve paid endpoint correlations, and rerun the complete seven-source variational inverse enclosure. Stage I tolerance, original Weil/augmented transport, whole-aperture positivity, F4, RH, and Lean closure remain open.

## Reproduction

```bash
python scripts/validate_rpb108_rc159_correlated_source_gram_tail.py \
 --output certificates/rpb108_rc159_correlated_source_gram_tail.json \
 certificates/rpb108_rc158_seven_inverse_assembly.json \
 certificates/rpb108_rc155_seven_source_action_interface.json \
 certificates/rpb108_rc136_seven_vector_joint_matrices.json \
 certificates/rpb108_rc128_collective_second_response.json \
 certificates/rpb108_rc131_finite_part_response_capture.json \
 certificates/rpb108_rc132_balanced_action_shared_covariance.json \
 certificates/rpb108_rc135_common_response_capture.json
```

Add `--replay` to reverse higher-moment sums and parameter order and check exact certificate equality. All inputs are hashed; historical checkpoint files are unchanged.
