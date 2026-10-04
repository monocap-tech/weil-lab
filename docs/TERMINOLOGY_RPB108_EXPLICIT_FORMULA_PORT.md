# RPB108 explicit-formula port terminology

These definitions precede the imported theorem's local use. Earlier historical wording is unchanged.

| Term | Definition and role |
| --- | --- |
| Pinned original closure | The 84 accepted solution bodies and 30 definition files at formalpedia commit ae3af9184af2e274c721b1cf3b0dffa09af02c6c, recorded in EF_LIT_ZETA_DEPENDENCY_MANIFEST.json. |
| Ported closure | Those sources under WeilDefect.External.Zeta23, with local imports, named main exports, copied-helper name repairs and Lean 4.34 API repairs. Hashes are in EF_LIT_ZETA_PORT_MANIFEST.json. |
| Zeta23.ZetaSeam | The actual-zeta zero facts needed by the external zero configuration. Defined in Def_Zeta23_Statement.lean and discharged in the seam/reflection definition files. |
| Zeta23.zetaZeros hs | The external ZeroConfig with carrier equal to IsNontrivialZero and natural multiplicity zeroMult. Its definition precedes EF_lit_zeta. |
| Zeta23.zetaSeam | The compiled closed seam assembled from the proved reflection, multiplicity and finite-window facts in Def_Zeta23_Statement_SeamClosed.lean. |
| Zeta23.EF.EF_lit | Defined in Def_Zeta23_ExplicitFormula.lean: for every compact C² test k, the multiplicity-weighted paperFT samples are summable and their tsum equals literatureRHS k. |
| Zeta23.EF.literatureRHS | Two paperFT pole samples at ±I/2, minus the von Mangoldt prime sum, plus the paperFT/digamma bracket integral with factor 1/(2π). |
| Zeta23.WeilEF.EF_lit_zeta | The proof-bearing compiled theorem deriving EF_lit (zetaZeros hs); it is not a field assumed to hold. |
| Divisor correspondence | The still-required proof relating our full-copy actual-zero indexing to this external distinct-zero weighted sum, including analytic multiplicity and gamma normalization. |
| Same-carrier arithmetic attachment | Application of the certified formula to the already proved compact C² inverse representative J_a(v,w), with its exact sample/zero/pole identities, followed by prime/digamma form transport. Not yet a retained WD-T38 identity. |

The external theorem and its definitions live under WeilDefect/External/Zeta23. The retained WD-T38 source/null identity and spectral-domain claims remain separate unproved obligations.
