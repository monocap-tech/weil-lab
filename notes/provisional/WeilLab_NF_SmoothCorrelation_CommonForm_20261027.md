# Weil-Lab NF — direct smooth-correlation common-form composition

Date: 2026-10-27. Scope: read-only analytic proof/custody audit. Repository: `monocap-tech/weil-lab`, research head `3a06261ae27c46f73c3687c974d7b23624ab0dd5` (#355), not integrated `main`. No repository mutations, GitHub CI run, or Lean build conducted in this pass.

## Statement and conditions

Fix `a>0`. Let `D_a` denote the supported logarithmic Fourier form domain, with squared norm `E_log(h)=∫ log(e+|ξ|)|ĥ(ξ)|² dξ`. Let `Q_native,a(f,g)` denote the native full signed multiplier-plus-Hermitian-cross-pole form (same physical vectors in both slots). Let `S_+, S_-` be the **normalized** complete actual-zeta divisor source analyses, including multiplicity copies, of the same supported physical vector.

Under the accepted *generic actual-zeta explicit formula* `Zeta23.WeilEF.EF_lit_zeta`, the whole-divisor unit-window local-count/sampling estimate, and the analytically proved density of `C_c^∞(-a,a)` in `D_a`, the following identity holds on the **entire** supported logarithmic carrier:

`⟨S_+ f,S_+ g⟩ - ⟨S_- f,S_- g⟩ = Q_native,a(f,g)`.

This is a statement about the full unselected source pairing, not selected-background WD-T10 domination, actual WD-T38 witness attachment, global positivity or RH. The identity's real form on the odd subcarrier at `a=11/10` is precisely the inherited SI10/SM41 original signed Weil quadratic, including all seven primes and the actual `-2 |⟨f,sinh(x/2)⟩|²` odd pole.

## Direct analytic proof on smooth physical tests

1. Choose arbitrary `f,g ∈ C_c^∞(-a,a)` (complex values allowed). Put `k(t)=∫ g(s) conjugate(f(s-t)) ds`. Standard compactly supported convolution shows `k∈C_c^∞(R)`, `supp k⊂[-2a,2a]`. The *existing Lean-certified* `neutralWindowCorrelation_rawTransform` proves, already for general compact-window `L²` inputs and all complex `z`, the exact transform identity

   `neutralRawTransform(k,z) = conjugate(F_f(conjugate(z))) F_g(z)`.

   The existing `neutralWindowCorrelation_hasCompactSupport` is likewise general in the inputs. Thus the only new generic admissibility lemma at the smooth level is `ContDiff R 2 k`, which follows from smooth compact convolution; Green-specific high Fourier moments are unnecessary.

2. The generic accepted actual-zero theorem `Zeta23.WeilEF.EF_lit_zeta Zeta23.zetaSeam` applies directly to that `k`. The existing `neutralRawTransform_eq_paperFT`, `neutralActualZetaLiteraturePointEquiv`, `neutralActualZetaLiterature_ordinate`, `neutralActualZetaLiterature_multiplicity`, and `neutralActualZetaDivisor_tsum_literature` give the *literal* equality of the multiplicity-weighted zero sum and the sum over raw copies. Inserting the correlation-transform equality gives

   `Z_a(f,g) := Σ_q conjugate(F_f(conjugate(γ_q))) F_g(γ_q) = literatureRHS(k)`.

   Absolute convergence is furnished by the generic EF theorem for `k∈C_c²` and/or the independent full-divisor sampling estimate. No RH, zero simplicity, line-only reduction, or selected source is assumed.

3. The *existing universal* pole theorem `neutralWindowCorrelation_poleCrossTerms` identifies the two pole samples with the symmetric mixed moments. The prime term is finite by `supp k⊂[-2a,2a]`; for each surviving `n`, Fourier inversion of this smooth correlation and the two shifts `±log n` gives the signed cosine pairing. The archimedean integral is absolutely integrable because `f,g` are smooth compactly supported and their Fourier transforms decrease faster than any power; the exact `r=±2πξ` Fourier dictionary and evenness of the digamma bracket give the canonical archimedean multiplier. **The existing Lean prime/arch spectral transport theorems are specialized to Green vectors**; their proofs can be generalized on these smoother inputs but are not a compiled universal theorem in the inspected branch. Composition yields

   `Z_a(f,g) = Q_native,a(f,g)`.

   Explicitly, the right-hand side is `∫ m_a(ξ) conjugate(f̂(ξ)) ĝ(ξ) dξ + conjugate(M_-(f)) M_+(g) + conjugate(M_+(f)) M_-(g)` with the project's fixed Fourier, cutoff, and Hermitian conventions. No finite Galerkin certificate enters.

4. The *existing universal* `neutralLogPairSource_mixed_difference` shows that the **unnormalized** full-divisor positive-minus-negative source form equals twice the zero-side pairing after reindexing the actual conjugate-ordinate involution (the same algebra as the proved Green-specific `neutralActualZetaGreenZeroForm_source_decomposition`). The *existing* source normalization is `|neutralActualZetaSourceNormalization|²=1/2`; hence the **normalized** signed source covariance equals `Z_a(f,g)`, not `2Z_a(f,g)`.

## Extension to the whole logarithmic form domain

The source sampling theorem analytically established in `notes/REFLECTED_PACKET_BRIDGE_108_LOG_SAMPLING_GRAPH_DENSITY_20261004.md` gives `Σ_q |F_h(γ_q)|² ≤ C_a E_log(h)` (including multiplicities and all raw copies). Conjugation/partner reindexing supplies the same bound for the paired evaluation. Consequently both normalized source maps are bounded from `D_a` to `ℓ²`, and their mixed signed covariance is continuous on `D_a × D_a`.

The certified actual native form operator `ActualZetaNativeFormOperator.lean` is bounded on the supported logarithmic Hilbert carrier: the symbol divided by the positive logarithmic weight is bounded, and the pole correction is bounded. Therefore `Q_native,a` is also jointly continuous on the same domain.

The logarithmic sampling/density research note gives an analytic density proof of `C_c^∞(-a,a)` in `D_a` by inward dilation plus compact mollification. Approximate both physical slots in `D_a`; use joint continuity to pass the smooth identity to every `f,g∈D_a`. This avoids relying on the **Green-specific** closure-density argument for this particular transport.

## Original odd restriction / domain boundary

At `a=11/10`, the native multiplier equals SI10/SM41's full seven-prime original `m(ξ)`. Original `A_o` has multiplier `max(1/1000,m)` and `K_-` has multiplier `(1/1000-m)_+`, so their difference is pointwise `m`. The symmetric cross-pole is `2|⟨f,cosh(x/2)⟩|²−2|⟨f,sinh(x/2)⟩|²` on the real physical parity decomposition; for odd f the cosh part vanishes. The original supported odd quadratic and canonical native quadratic therefore agree on the *same logarithmic form domain* by this algebraic definition. The distinct strong `L²` operator domain and its use in unbounded strong residual identities are not automatically identified by this form-level equality.

## Standing and STOP

- **Analytically complete by composition, subject to the existing generic explicit formula and unit-window sampling/density inputs:** full normalized source/native **mixed form** equality on fixed supported logarithmic carriers.
- **Already Lean-certified:** general compact-window `L²` correlation transform and support; generic actual zeta explicit formula; pole correlation; native multiplier/pole bounded form operator; partner algebra on selected/Green inputs; original-source normalizations.
- **Not newly Lean-certified:** generic smooth-convolution admissibility and the *arbitrary-smooth-input* prime/arch spectral dictionary/composition; analytic all-supported-vector sampling/density transfer. No new Lean build or kernel axiom audit was performed.
- **Not discharged:** any WD-T38 retained P/C/k same-vector/null witness; actual unshifted selected-background contraction; AZ-NEXTJET-LOC; infinite original odd Schur upper; even and full Weil signs; F4/CC27 and RH transfer.

**Recommendation:** Do not reopen generic source construction as an active research frontier. If formal verification is prioritized, write one generic smooth-correlate theorem and a supported-log core extension, reusing certified components, then rejoin the original signed Schur/other RH-facing obligations. For mathematical research, this audit supplies no independent sign or arithmetic barrier clearance.
