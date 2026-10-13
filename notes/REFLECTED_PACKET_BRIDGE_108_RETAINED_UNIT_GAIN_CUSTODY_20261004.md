# RPB108 retained unit-gain and physical-adjoint custody — 2026-10-04

Parent certified research: dbda720299b7c1d474aa25d8826263764fd5c1fa.

## Pinned recovery

All 152 non-external Lean files in the pinned research tree were read and scanned, without read errors. The attained-neutral WD-T38 constructor occurs only at its definition in Morphology/Neutral.lean. NeutralDefectMorphology occurs there and in the audit zeroDensityReindex; no concrete actual-zeta constructor application was recovered.

Canonical monocap-tech/weil main remains b019d40205680f9761a4b0a80cbcad56ee1b606b. Of its 44 Lean files, the root and Neutral.lean differ from the lab, while all 42 other modules have identical Git blobs. Neutral's canonical blob is 5f20024f9d8d6567584f838478dca071848a7618; the pre-repair lab blob is 4dc461eb06a2839d6e181958f623ede3e21818be. The lab already contains the canonical constructor machinery. Scope is these pinned trees, not all historical branches or other repositories. File hashes and search excerpts are preserved in docs/RPB108_RETAINED_WITNESS_SCAN_20261004.json.

## Exact repair

The existing constructor accepts haCarrier, hunit and hreal, proving aLim=C uLim, C†(C uLim)=uLim, and C uLim=P†k. Its output previously preserved only coefficientCarrier and the resulting physicalNull, dropping the latter two original equations.

NeutralDefectMorphology now retains unitGain and physicalAdjoint. The constructor populates them from its unchanged original hunit and hreal inputs. zeroDensityReindex preserves both on the same maps, coefficient and physical vector. No new constructor premise or representation layer is added.

This repairs witness erasure. It does not identify P with the full positive actual-divisor source synthesis or the effective positive background synthesis. The historical hypothesis 8 in docs/NEUTRAL_DEFECT_MORPHOLOGY.md retains that physical/form identification as an assumption; the pinned Lean tree contains no concrete application realizing it.

## Source comparison and domain boundary

The certified Green source identities now provide the full actual-divisor P/N mixed and diagonal arithmetic dictionary, including the factor two and the true Hermitian cross-pole expression. The historical single positive pole-square formula is not valid on the unrestricted complex domain merely by naming it.

The selected/background audit proves selected nullity leaves the unselected negative covariance; full nullity needs either vanishing background analysis or the actual effective-positive reduction. Existing generic effectivePositive theorems and concrete neutralLogBackgroundOperator do not supply that identification or its positivity.

Constructed Green synthesis has derived H¹ regularity. Retained logarithmic form membership does not imply H¹ or membership in this synthesis range. A proposed range link would therefore be a substantive stronger result, not a routine subtype conversion. A lawful closure/extension of the source dictionary to the retained form domain is the appropriate construction target; its continuity and actual effective-positive realization must be proved.

Next cursor: build the actual-zeta finite-selected effective positive/source realization on the lawful logarithmic form domain, using the certified same-Green full-divisor mixed/quadratic identities and the existing selected/background reduction. Prove continuity/closure or a lawful domain extension before identifying abstract P with the actual effective positive synthesis; identify the selected negative map and its normalization, then instantiate the fixed-packet critical construction. The WD-T38 output now retains its original unitGain and physicalAdjoint proofs, but no concrete application was recovered in the pinned 152-file lab scan or canonical main comparison. Do not assume arbitrary retained k is in the H¹ Green synthesis range or upgrade one-logarithm energy to spectral operator-domain membership. Same-vector source/null attachment, central cancellation, background completion and F-4 remain open.

Residue preserved: certified actual Green full-divisor sampling, P/N source identities, zero-to-native Weil transport, exact prime/pole/digamma dictionaries; generic endpoint null identity and threshold-aware stop interface. No retained spectral membership, central cancellation, positivity, or RH conclusion is claimed.

## Exact mapping recovered

| Item | Existing retained value | Certified concrete target | Current link |
| --- | --- | --- | --- |
| Positive coefficient | aLim=C uLim | Actual-divisor P analysis, or effective positive analysis after background reduction | Not instantiated |
| Physical-adjoint coefficient | C uLim=P†k | Same canonical physical source analysis | Original proof now retained; P remains abstract |
| Negative coefficient | N†k=-uLim with N=-PC | Finite selected actual negative source map | Generic theorem only |
| Physical vector | k; extension vector=extend k | Canonical logarithmic physical vector | Concrete instance absent |
| Unit gain | C†C uLim=uLim | Same finite-sector compensator | Original proof now retained |
| Null identity | (PP†-NN†)k=0 | Native endpoint form/action on the same vector | Source/background identification missing |
| Named density/Q | Independent arithmetic parameters | Physical Fourier norm-square / source quadratic | No equality; zero-density audit remains valid |

Certificate: candidate 1d7e6c5c217cf8f0816d930f6074e1558747a5fc; [run 37181637139](https://github.com/monocap-tech/weil-lab/actions/runs/37181637139), job 111375227963. Lean 4.34.0; isolated 8935/full 9185 build jobs. All four projections/constructors audit to exactly [propext, Classical.choice, Quot.sound]; unfinished gate passed. No new theorem assumptions or constructor inputs. Exact two-module source promoted.
