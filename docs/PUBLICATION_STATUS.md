# Publication Status Authority

Snapshot base: `936e723ac9c22592f9fb0901f2f25bbf238227c2`  
Publication branch: `publication/preprint-audit`

## Authority rule

**For publication and archive work, this file is the sole current status
authority.**

Historical files such as `PROOF_STATUS.md`, `THEOREM_LEDGER.md`,
`PUBLIC_THEOREM_INDEX.md`, and `LEAN_STATUS.md` remain provenance and
evidence surfaces. They are not to be independently interpreted as the current
publication verdict when they disagree.

The reconciliation precedence used here is:

1. exact formal declaration map in `LEAN_STATUS.md` for Lean certification;
2. `THEOREM_LEDGER.md` for mathematical standing and H1-P4 audit/source status;
3. `PUBLIC_THEOREM_INDEX.md` for public names, dependencies, and manuscript-facing role;
4. live RPB-108 certification notes for post-Horizon actual-zeta results.

This file never upgrades a theorem merely because summary prose says a phase is
"complete."

## Top-level publication verdict

- RH is **not proved** by the current snapshot.
- `FULL TRANSPORT CLOSED` is **not certified**.
- WD-T01–WD-T39 have stable formal statuses recorded below.
- WD-T40 is **mathematically proved conditionally and P4-audit-passed, but
  formally LEAN-BLOCKED** at this snapshot.
- The blocking WD-T40 formal seam is the source-faithful
  polarization/complexification of EXT-4 into the compact-test operator
  identity and cutoff extension required by the Hermitian Gaussian dual test.
- Live RPB-108 work has certified substantial actual-zeta carrier machinery,
  but the actual branch still has independent open attachment/sign/cancellation
  obligations.

## Stable WD-T01–WD-T40 ledger

| ID | Public name | Mathematical standing | Audit/source status | Formal status | Dependencies | Manuscript role | Lean declaration custody |
|---|---|---|---|---|---|---|---|
| WD-T01 | Defect identity and index transfer | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §2 Abstract defect/screening | WeilDefect.WDT01.wd_t01_defect_inner_identity + WeilDefect.WDT01.wd_t01_nonnegative_iff + WeilDefect.WDT01.wd_t01_negative_rank_iff |
| WD-T02 | Contractive screening equivalence | INTERNAL-PROOF + IMPORTED Douglas | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T01; EXT-1 | §2 Abstract defect/screening | WeilDefect.WDT02.wd_t02_contractive_screening_equivalence + WeilDefect.WDT02.wd_t02_unique_reduced_solution |
| WD-T03 | Reduced-screening graph normal form | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T02 | §2 Abstract defect/screening | WeilDefect.WDT03.wd_t03_kernel_decomposition + WeilDefect.WDT03.wd_t03_analysis_graph_iff + WeilDefect.WDT03.wd_t03_graph_signature + WeilDefect.WDT03.wd_t03_defect_factorization |
| WD-T04 | Abstract screening taxonomy | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T02 | §2 Abstract defect/screening | WeilDefect.WDT04.wd_t04_range_defect_no_exact_screening + WeilDefect.WDT04.wd_t04_range_defect_negative + WeilDefect.WDT04.wd_t04_over_budget_negative + WeilDefect.WDT04.wd_t04_strict_screened_lower_bound + WeilDefect.WDT04.wd_t04_attained_critical_neutral + WeilDefect.WDT04.wd_t04_nonattained_critical_positive + WeilDefect.WDT04.wd_t04_critical_approximate_neutral + WeilDefect.WDT04.wd_t04_complete_reduced_taxonomy |
| WD-T05 | Rank-one defect specialization | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T02 | §2 Abstract defect/screening | WeilDefect.wd_t05_rank_one_covariance + WeilDefect.WDT05.wd_t05_defect_rank_one + WeilDefect.WDT05.wd_t05_signed_factor_iff_vector + WeilDefect.WDT05.wd_t05_covariance_iff_unit_vector + WeilDefect.WDT05.wd_t05_physical_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_analysis_nonnegative_iff_unit_vector + WeilDefect.WDT05.wd_t05_rank_one_specialization |
| WD-T06 | Monotone positive screening | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §2 Abstract defect/screening | WeilDefect.WDT06.wd_t06_truncated_inner_identity + WeilDefect.WDT06.wd_t06_quadratic_mono + WeilDefect.WDT06.wd_t06_defect_mono + WeilDefect.WDT06.wd_t06_defect_le_full + WeilDefect.WDT06.wd_t06_defect_strong_tendsto + WeilDefect.WDT06.wd_t06_quadratic_tendsto + WeilDefect.WDT06.wd_t06_negative_rank_antitone + WeilDefect.WDT06.wd_t06_monotone_positive_screening |
| WD-T07 | Selected/background custody | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §2 Abstract defect/screening | WeilDefect.wd_t07_selected_full_identity + WeilDefect.wd_t07_selected_negative_implies_full + WeilDefect.WDT07.wd_t07_full_le_selected + WeilDefect.WDT07.wd_t07_negative_rank_custody + WeilDefect.WDT07.wd_t07_full_negative_without_selected_negative + WeilDefect.WDT07.wd_t07_selected_background_monotonicity_and_custody |
| WD-T08 | Finite selected-sector index cap | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T07 | §2 Abstract defect/screening | WeilDefect.WDT08.selected_adjoint_comp_injective + WeilDefect.WDT08.wd_t08_selected_negative_rank_le_finrank + WeilDefect.WDT08.wd_t08_background_null_finrank_lower + WeilDefect.WDT08.wd_t08_selected_negative_on_background_null + WeilDefect.WDT08.wd_t08_full_negative_rank_background_reduction + WeilDefect.WDT08.wd_t08_finite_selected_sector_index_cap |
| WD-T09 | Shared screening budget | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T07 | §2 Abstract defect/screening | WeilDefect.WDT09.wd_t09_full_quadratic_factorization + WeilDefect.WDT09.wd_t09_shared_defect_factorization + WeilDefect.WDT09.wd_t09_full_nonnegative_iff_joint_budget + WeilDefect.WDT09.wd_t09_separate_contractions_not_joint + WeilDefect.WDT09.wd_t09_shared_screening_budget |
| WD-T10 | Background elimination and residual budget | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T02; WD-T09 | §2 Abstract defect/screening | WeilDefect.WDT10.wd_t10_residual_budget_positive + WeilDefect.WDT10.wd_t10_residual_sqrt_sq + WeilDefect.WDT10.wd_t10_effective_covariance + WeilDefect.WDT10.wd_t10_background_covariance_elimination + WeilDefect.WDT10.wd_t10_full_defect_reduction + WeilDefect.WDT10.wd_t10_full_nonnegative_iff_effective_physical + WeilDefect.WDT10.wd_t10_full_nonnegative_iff_residual_screening + WeilDefect.WDT10.wd_t10_background_e… |
| WD-T11 | Finite-sector singular-value inertia | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T03 | §2 Abstract defect/screening | WeilDefect.WDT11.wd_t11_norm_one_attains_neutral + WeilDefect.WDT11.wd_t11_graphQ_diagonal + WeilDefect.WDT11.wd_t11_negative_rank_le_count + WeilDefect.WDT11.wd_t11_negative_space_strict + WeilDefect.WDT11.wd_t11_negative_space_finrank + WeilDefect.WDT11.wd_t11_negative_index_exact + WeilDefect.WDT11.wd_t11_neutral_space_finrank + WeilDefect.WDT11.wd_t11_neutral_space_graphQ_zero + WeilDefect.WDT11.wd_t11_finite_… |
| WD-T12 | Sequential background consumption | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T10 | §2 Abstract defect/screening | WeilDefect.WDT12.sequentialResidualBudget + WeilDefect.WDT12.wd_t12_sequential_budget_covariance + WeilDefect.WDT12.wd_t12_second_background_elimination + WeilDefect.WDT12.wd_t12_sequential_background_consumption |
| WD-T13 | Shorted-covariance reduction | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §2 Abstract defect/screening | WeilDefect.WDT13.wd_t13_complement_isUnit + WeilDefect.WDT13.wd_t13_complement_inverse_nonnegative + WeilDefect.WDT13.wd_t13_schur_correction_positive + WeilDefect.WDT13.wd_t13_schur_le_compression + WeilDefect.WDT13.wd_t13_schur_lower_bound + WeilDefect.WDT13.wd_t13_schur_isUnit + WeilDefect.WDT13.wd_t13_block_solution_exists + WeilDefect.WDT13.wd_t13_block_solution_first_component + WeilDefect.WDT13.wd_t13_direc… |
| WD-T14 | Finite positive-shadow separation | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §2 Abstract defect/screening | WeilDefect.WDT14.wd_t14_positive_shadow_margin + WeilDefect.WDT14.wd_t14_positive_shadow_preserves_negative_margin + WeilDefect.WDT14.wd_t14_graph_shadow_admissible_iff + WeilDefect.WDT14.wd_t14_graph_admissibility_failure_example + WeilDefect.WDT14.wd_t14_finite_positive_shadows_preserve_signature_not_admissibility |
| WD-T15 | Right-limit projection and gap duality | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §3 Zeta-Weil divisor/pair geometry | WeilDefect.WDT15.wd_t15_gap_antitone + WeilDefect.WDT15.wd_t15_right_limit_gap_duality + WeilDefect.WDT15.wd_t15_sequence_right_limit_eq + WeilDefect.WDT15.wd_t15_sequence_gap_eq_right_limit_orthogonal + WeilDefect.WDT15.wd_t15_monotone_projection_limit + WeilDefect.WDT15.wd_t15_right_limit_projection_and_gap_duality |
| WD-T16 | Fixed-sector persistence | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T15 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.WDT16.exists_weaklyTendsto_subseq_of_norm_le + WeilDefect.WDT16.wd_t16_fixed_negative_sector_compactness + WeilDefect.WDT16.wd_t16_nonpositive_limit_persists + WeilDefect.WDT16.wd_t16_uniform_negative_margin_persists + WeilDefect.WDT16.wd_t16_uniform_negative_margin_forces_endpoint_jump + WeilDefect.WDT16.wd_t16_fixed_finite_negative_sector_persistence |
| WD-T17 | Fixed-sector critical dichotomy | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T15 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.WDT17.weaklyTendsto_strong_of_norm_sq_tendsto + WeilDefect.WDT17.wd_t17_critical_positive_mass_le_half + WeilDefect.WDT17.wd_t17_fixed_sector_critical_dichotomy + WeilDefect.WDT17.wd_t17_neutral_branch + WeilDefect.WDT17.wd_t17_loss_branch |
| WD-T18 | Endpoint-jump index bound | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T15 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.WDT18.endpointInside + WeilDefect.WDT18.endpointQuotientMap + WeilDefect.WDT18.wd_t18_endpoint_quotient_map_injective + WeilDefect.WDT18.wd_t18_endpoint_jump_negative_rank_le_quotient + WeilDefect.WDT18.wd_t18_one_dimensional_jump_rank_cap |
| WD-T19 | Boundary amplification and representative blow-up | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §3 Zeta-Weil divisor/pair geometry | WeilDefect.WDT19.analysisSpace + WeilDefect.WDT19.weak_limit_mem_physical_rightLimit + WeilDefect.WDT19.wd_t19_endpoint_representative_blowup + WeilDefect.WDT19.BoundaryAmplifies + WeilDefect.WDT19.wd_t19_boundary_amplification + WeilDefect.WDT19.wd_t19_vanishing_amplitude_normalized_blowup |
| WD-T20 | Conjugate-pair diagonalization | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §3 Zeta-Weil divisor/pair geometry | WeilDefect.wd_t20_pair_pos_eigen + WeilDefect.wd_t20_pair_neg_eigen + WeilDefect.pairEigenEquiv + WeilDefect.wd_t20_pair_diagonalization |
| WD-T21 | Simple quartet pair geometry | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T20 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.quartetPairPos + WeilDefect.quartetPairNeg + WeilDefect.wd_t21_quartet_pair_pos_conjugate + WeilDefect.wd_t21_quartet_pair_neg_conjugate + WeilDefect.wd_t21_quartet_pairs_nonreal + WeilDefect.wd_t21_quartet_pairs_distinct + WeilDefect.wd_t21_simple_quartet_negative_count + WeilDefect.wd_t21_simple_quartet_pair_geometry |
| WD-T22 | Finite Weil inertia saturation | IMPORTED + SPECIALIZED | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | EXT-2A | §3 Zeta-Weil divisor/pair geometry | WeilDefect.BombieriFiniteInertiaData + WeilDefect.wd_t22_finite_weil_inertia_saturation + WeilDefect.SimpleQuartetPacketNegative + WeilDefect.wd_t22_simple_quartet_packet_pair_count + WeilDefect.wd_t22_simple_quartet_packet_inertia + WeilDefect.wd_t22_two_simple_quartet_negative_index |
| WD-T23 | Multiplicity-null reduction | IMPORTED/DERIVED | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | EXT-2B | §3 Zeta-Weil divisor/pair geometry | WeilDefect.BombieriMultiplicityNullData + WeilDefect.wd_t23_same_frequency_synthesis_factor + WeilDefect.wd_t23_same_frequency_zero_sum_null + WeilDefect.wd_t23_total_multiplicity_nullity + WeilDefect.wd_t23_single_ordinate_nullity + WeilDefect.wd_t23_single_ordinate_has_null_iff_repeated + WeilDefect.wd_t23_distinct_frequency_reduction |
| WD-T24 | Finite exponential independence | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §3 Zeta-Weil divisor/pair geometry | WeilDefect.realExpMode + WeilDefect.realExpMode_ne_zero + WeilDefect.hasDerivAt_realExpMode + WeilDefect.iteratedDeriv_realExpMode + WeilDefect.iteratedDeriv_finite_exp_sum + WeilDefect.wd_t24_finite_distinct_frequency_exponential_independence |
| WD-T25 | No exact finite positive compensation | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T24 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.problemOneDenominator + WeilDefect.problemOneL + WeilDefect.problemOneMode + WeilDefect.problemOneL_problemOneMode + WeilDefect.wd_t25_finite_problem_one_relation_trivial + WeilDefect.wd_t25_no_exact_finite_positive_compensation |
| WD-T26 | Selected zero-moment residue law | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T20 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.rawResiduesOfNegativePairs + WeilDefect.wd_t26_zero_moment + WeilDefect.wd_t26_coefficient_mem_rawResidues + WeilDefect.wd_t26_nonzero_raw_residue_of_nonzero_coefficient + WeilDefect.wd_t26_selected_zero_moment_residue |
| WD-T27 | Universal inverse-square far decay | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T26 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.rationalResponse + WeilDefect.residueFirstMoment + WeilDefect.rationalResponse_laurent_two + WeilDefect.rationalResponse_zero_moment_remainder_bound + WeilDefect.rationalResponse_zero_moment_remainder_isBigO + WeilDefect.rationalResponse_zero_moment_isBigO + WeilDefect.wd_t27_universal_inverse_square_far_decay + WeilDefect.wd_t27_universal_inverse_square_isBigO |
| WD-T28 | Native Problem-1 compactness | INTERNAL-PROOF + imported zero count | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED | EXT-3 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.ZetaZeroShellCountData + WeilDefect.NativeProblemOneResolventData + WeilDefect.NativeHilbertSchmidtCriterion + WeilDefect.NativeTraceClassCovarianceCriterion + WeilDefect.wd_t28_native_problem_one_hilbert_schmidt_actual + WeilDefect.problemOneGreenPairing_eq_dirichletEnergy + WeilDefect.problemOneColumnEnergySq_eq_dirichletEnergy + WeilDefect.wd_t28_actual_dirichlet_energy_summable |
| WD-T29 | Quantitative finite-head approximation | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | WD-T28 | §3 Zeta-Weil divisor/pair geometry | WeilDefect.wd_t29_finite_head_approximation + WeilDefect.wd_t29_quantitative_finite_head_approximation |
| WD-T30 | Two-mode selected-preserving multiplier | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §4 Explicit formula/log form | WeilDefect.wd_t30_two_mode_kernel_combination + WeilDefect.wd_t30_zero_functional_preserves_every_mode |
| WD-T31 | Zero-count far-tail estimate | INTERNAL-PROOF + imported zero count | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T27; EXT-3 | §4 Explicit formula/log form | WeilDefect.ZetaLogShellCountData + WeilDefect.FarShellResponseData + WeilDefect.logarithmicTail_tsum_le + WeilDefect.farShellResponse_norm_le_logarithmic_kernel + WeilDefect.wd_t31_shell_aggregation + WeilDefect.rationalResponse_zero_moment_norm_le_inverse_square + WeilDefect.farShellResponseData_of_zero_moment + WeilDefect.wd_t31_zero_moment_zero_count_far_tail |
| WD-T32 | Weighted completed next-jet representation | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §4 Explicit formula/log form | WeilDefect.completedResponseLift + WeilDefect.iteratedDeriv_centered_power + WeilDefect.iteratedDeriv_centered_power_mul + WeilDefect.wd_t32_complementary_next_jet_identity + WeilDefect.nearComplementaryResponse + WeilDefect.weightedNearNextJetField + WeilDefect.wd_t32_weighted_near_next_jet_representation |
| WD-T33 | Adaptive cocancellation guard | INTERNAL-PROOF | P4-AUDIT-PASSED | LEAN-CERTIFIED | — | §4 Explicit formula/log form | WeilDefect.wd_t33_adaptive_cocancellation |
| WD-T34 | Finite compact-window prime translations | DERIVED from IMPORTED compact-window formula | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED | EXT-4 | §4 Explicit formula/log form | WeilDefect.activePrimePowers + WeilDefect.wd_t34_active_prime_powers_finite + WeilDefect.activePrimePowerFinset + WeilDefect.activePrimeTranslationShifts + WeilDefect.wd_t34_active_prime_translation_shifts_finite + WeilDefect.translateBy + WeilDefect.symmetricPrimeTranslation + WeilDefect.compactPrimeTranslationSum + WeilDefect.wd_t34_finite_prime_power_translations + WeilDefect.primePowerThreshold + WeilDefect.pr… |
| WD-T35 | Logarithmic compact-window form order | DERIVED | SOURCE-PINNED; P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T34; EXT-4; EXT-5 | §4 Explicit formula/log form | WeilDefect.logarithmicFourierWeight + WeilDefect.one_le_logarithmicFourierWeight + WeilDefect.logarithmicFourierEnergy + WeilDefect.spectralMass + WeilDefect.shiftedCompactWeilForm + WeilDefect.wd_t35_shifted_form_logarithmic_order + WeilDefect.wd_t35_compact_weil_logarithmic_form_order |
| WD-T36 | No free positive-Sobolev bootstrap | INTERNAL-PROOF/SHARPNESS | P4-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T35 | §4 Explicit formula/log form | WeilDefect.positiveSobolevFrequencyWeight + WeilDefect.logarithmicFourierWeight_isBigO_log + WeilDefect.logarithmicFourierWeight_isLittleO_positiveSobolev + WeilDefect.positiveSobolevFrequencyWeight_not_isBigO_logarithmic + WeilDefect.wd_t36_no_uniform_positive_sobolev_coercivity_of_witness + WeilDefect.wd_t36_no_positive_sobolev_bootstrap + WeilDefect.finitePrimeTrigCorrection + WeilDefect.finitePrimeTrigBound + … |
| WD-T37 | Persistent negative morphology | CONDITIONAL COMPOSITE | COMPOSITE-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T16; WD-T07; WD-T26; WD-T27; WD-T31; WD-T32; WD-T33 | §7 False-RH morphology | WeilDefect.wd_t37_selected_source_zero_moment_of_wd_t26 + WeilDefect.wd_t37_selected_source_nonzero_of_wd_t26 + WeilDefect.wd_t37_p3_n1_endpoint_ray + WeilDefect.wd_t37_p3_n2_normalized_representative_blowup + WeilDefect.wd_t37_p3_n3_normalized_full_negativity + WeilDefect.wd_t37_p3_n4_zero_moment_source_far_decay + WeilDefect.wd_t37_p3_n5_far_localization + WeilDefect.wd_t37_p3_n6_weighted_next_jet_morphology + W… |
| WD-T38 | Attained neutral morphology | CONDITIONAL COMPOSITE | COMPOSITE-AUDIT-PASSED | LEAN-CERTIFIED-FROM-IMPORTED-PREMISE | WD-T17; WD-T34; WD-T35; WD-T36 | §7 False-RH morphology | WeilDefect.wd_t38_p3_u1_fixed_packet_critical_dichotomy + WeilDefect.wd_t38_attained_neutral_selected_coordinate_nonzero + WeilDefect.rightLimitPrimePowers + WeilDefect.wd_t38_p3_u3_right_limit_prime_decomposition + WeilDefect.wd_t38_p3_u3_right_limit_prime_support_finite + WeilDefect.wd_t38_p3_u4_logarithmic_order_neutral_carrier + WeilDefect.wd_t38_p3_u5_no_free_positive_sobolev_control + WeilDefect.wd_t38_p3_u5… |
| WD-T39 | Noncompact background morphology | INTERNAL/CONDITIONAL COMPOSITE | COMPOSITE-AUDIT-PASSED | LEAN-CERTIFIED | WD-T15–T17; WD-T07; WD-T14 | §7 False-RH morphology | WeilDefect.FullNegativeSpace + WeilDefect.fullNegativeCoeff + WeilDefect.fullCoeff + WeilDefect.fullJValue + WeilDefect.wd_t39_p3_b1_anchored_mass + WeilDefect.wd_t39_p3_b2_full_coordinate_escape_weak_zero + WeilDefect.wd_t39_p3_b3_fixed_packet_custody + WeilDefect.normEscapeSubsequence + WeilDefect.wd_t39_p3_b4_norm_escape_of_unbounded + WeilDefect.BoundedBackgroundRegime + WeilDefect.wd_t39_p3_b4_bounded_backgro… |
| WD-T40 | Gaussian support-gap null-extension exclusion | INTERNAL-PROOF / CONDITIONAL on WD-T38 hypotheses | P4-AUDIT-PASSED | LEAN-BLOCKED | WD-T38; WD-T34; WD-T35; EXT-4; EXT-5 | §7 False-RH morphology | F-1 carrier + normalized F-2 multiplier + F-3 support-gap pairing + repaired cutoff/pairing closure + concrete source-pole growth + conditional Gaussian-admissibility assembly are kernel-checked; RPB-107 additionally certifies the exact two-exponential pole quadratic factor and the conjugated Hermitian Gaussian dual test. The remaining blocker is the source-faithful polarization/complexification of EXT-4 into a co… |

### WD-T40 reconciliation note

The repository contains optimistic summary language such as `LEAN-H1
EXHAUSTED` / Horizon-1 package completion. That language records package-phase
or historical handoff status. It does **not** override the exact current
declaration map, which records WD-T40 as `LEAN-BLOCKED`.

Publication language must therefore say:

> WD-T40 has an audited mathematical proof under the stated WD-T38 hypotheses;
> its full formal certification remains blocked at the source-faithful EXT-4
> operator-realization seam.

It must not say that WD-T40 is fully Lean-certified.

## Live RPB-108 results: certified infrastructure, no new stable WD IDs yet

The following post-Horizon results are certified on the live RPB branch but are
not assigned new stable public theorem IDs by this publication branch.

| Live family | Certified content | Publication treatment |
|---|---|---|
| Actual zeta zero/divisor custody | actual open-strip zero coordinates, reflection/conjugation, analytic multiplicity, divisor copies, finite windows/countability | stable exposition candidate |
| Actual growth / explicit formula | theta/Mellin/Jensen growth chain, literal explicit-formula transport, zero-side summability modules | stable exposition candidate; imported-source boundaries explicit |
| Logarithmic/source carriers | canonical log-Hilbert/form carrier, source-domain and native form attachments | stable exposition candidate |
| Actual Green graph | Green synthesis, graph closure, closed subspace, bounded lift, packet convergence, exact packet closed span | stable exposition candidate |
| Actual graph analysis | adjoint analysis, kernel/orthogonal-complement characterization, packet observations | stable exposition candidate |
| Copy observability | equal synthesized whole graph packets give identical observation rows; raw multiplicity copies are not independent observations | mandatory carrier-warning theorem |
| Carrier factorization | graph-image observation completion distinguished from positive-energy quotient/completion; kernel/descent/domination criteria exact | mandatory architecture theorem family |
| Background finite tests | unshifted background positivity on Green completion iff all finite actual packets are nonnegative | live reduction; does not settle sign |
| Background Gram tests | unit domination implies mixed Cauchy-Schwarz; strict violation yields finite negative packet; collision rows remain identical | live reduction; no actual violating pair certified |

## Live P0 blockers

### P0-A — actual unshifted background sign

Open. Need either:

- uniform positivity for all finite actual packets on the intended window/selection; or
- one rigorous finite actual negative certificate.

No coordinate-diagonal or pair-only check is a global PSD certificate.

### P0-B — retained same-vector WD-T38 attachment

Open. Need lawful identification/membership of the retained physical vector in
the actual source/Green carrier and the retained source/null identity on that
same object, or a fresh actual constructor carrying equivalent custody.

### P0-C — central cancellation / transport completion

Open. Actual central cancellation, required background completion on the actual
branch, downstream boundary-removal consumption, F-4 completion, and
`FULL TRANSPORT CLOSED` are not certified.

### P0-D — negative-branch RH-facing interfaces

Open:

- `AZ-NEXTJET-LOC`;
- `C-ACTUAL-KPH-FLOOR`.

SOURCE traversal remains off the critical path unless a downstream branch
explicitly calls one of its retained lemmas.

## Publication claim guard

Until all P0 blockers and global false-RH exhaustiveness are certified, no
abstract, title, introduction, README, preprint metadata, or archive release may
state or imply that RH has been proved.

