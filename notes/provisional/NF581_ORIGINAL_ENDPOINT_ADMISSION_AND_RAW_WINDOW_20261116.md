# NF581 — original log-energy admission accepted; connect actual seed and window coordinates

Stacked on NF580 PR #611. All new proof scripts below are compiler-pending.

## Compiler receipt

NF575 run 44029579253 job 133857986425 (NF578 head a5e0e17df168572ebcbedaea876e95c1077d956d) completed. The independent actual physical strip log-energy criterion step passed, along with exact source global-combination differentiation and actual left-kernel closure. Thus the strip-controlled physical L2 admission into the original weighted logarithmic Hilbert carrier is Lean accepted. This includes the genuine supported Fourier-coordinate a.e. dictionary and integrable continuum majorant. The separate continuum norm-limit step failed on ambiguous tendsto_const_nhds, the literal endpoint L2 admission module failed on indicator/if elaboration, and full source graph step failed on the earlier dyadic graph limit diagnostics. NF578 independent scalar and convolution geometry and dyadic envelope steps also passed.

NF579 run 44030545789 job 133861153155 was still in progress at last inspection; mollifier, its dependent transform, and continuum limit steps reported failure. Detailed NF579 logs unavailable at this inspection; do not treat those failures as mathematical counterexamples. NF580 focused run 44031883844 queued at last inspection. No new terminal Gram or graph compilation claimed.

## NF581 changes

- Repair continuum dominated convergence by explicitly typing the constant Fourier limit. NF579's pointwise-sample theorem and NF575 wrapper remain.
- Repair literal endpoint membership proof: exact if-branch rewrites, use integrable_indicator_iff for the original log-square majorant and explicit reflection/indicator identity.
- Expose the very same one-collar complex L2 admission witness, alongside the odd endpoint, retaining the old interface. The real half integrability needed for the seed must still be connected.
- New independent RawWindowDictionary: for a pointwise window-supported complex representative f with MemLp f 2 volume, neutralRawTransform f z = neutralWindowEvaluation a z (hf.toLp f) at every complex z. This is the full strip dictionary, not merely a.e. on the real Fourier axis. The actual L2 class also retains window support a.e.
- New EndpointSeedSchwartz: package the same real affine-mollified seed as a smooth compact complex Schwartz function, with exact original two-collar support, real values and odd parity; no abstract seed existence premise (integrability of the actual half and prior mollifier lemmas still explicit). This supplies the intended test-function interface for the original canonical moment correction once compiled. No new Gram premise claimed discharged.

Focused CI configured. No local Lean build, no fresh numeric replay in NF581, no main merge. Prior NF577-580 arithmetic/source receipts retained. Original U identity, source-specific Fourier integration by parts, actual sequence scalar limit and full strip transport, terminal Gram and source graph all require completion. Full Weil coercivity, W_ODD_NEG and RH open.
