## MG43 independently accepted original 24D matrix-combination result

**GitHub Actions [#39522608989](https://github.com/monocap-tech/weil-lab/actions/runs/39522608989) PASSED**, both full calculation and a distinct independent exact-rational original matrix auditor, against pinned MG24 #39378465438, MG29 #39440914565, MG40 #39513403010, MG41 #39519080670, MG42 #39520549337. Accepted artifact `mg43-original-independent-G-S-full24-source-grid`, ID **12312157347**. A previous initial workflow run #39522274640 completed the calculation but the independent auditor incorrectly required nonscalar response B to be symmetric; the corrected run distinguishes general original response B from necessarily symmetric physical covariance/Gram matrices and passed all **540** complete-source upper-matrix replays.

| genuine-original MG29 mesh | cutoff k | archived MG40 best nonscalar Gershgorin sufficient lower | new MG43 best floating-ranked candidate, exact rational Gersh lower | independently proven full original source Hlo−U matrix status |
|---|---:|---:|---:|---|
| 16 | 12 | −4.0752440824 | **−1.3146427911** | exact NEGATIVE rational Rayleigh direction |
| 16 | 16 | −4.3599128631 | **−1.4906207885** | exact NEGATIVE rational Rayleigh direction |
| 32 | 12 | −1.1938738051 | −1.1941733535 | exact NEGATIVE rational Rayleigh direction |
| 32 | 16 | −1.3130469460 | −1.3130469460 | exact NEGATIVE rational Rayleigh direction |

All four selected source responses are the genuine archived `matrix_ridge_1/10_blend_1/2`. MG43's proposed independently validated parameter triplets (first moment alpha, second moment beta, matrix uncertainty eta) were respectively:
- 16/k12: (0,0,1/64);
- 16/k16: (0,0,1/64);
- 32/k12: (0,1,1/64);
- 32/k16: (1,1,1/64).

These parameters describe **actually VALID** original full-frequency source residual upper matrices, not reduced versions of MG42's counterfactual F scaling. All 540 original full-matrix Gershgorin margins and traces were computed and independently rechecked using exact Fraction; float was used only to rank which of those matrices was subjected to the complete exact rational sign classification. Every selected true-source conservative lower has a true exact negative direction, not merely a negative lower Gershgorin estimate. There is **NO strict original 24D source contraction**; consequently also no full 470-source inverse, signed 51/56 odd cap, independent Fourier/form-domain, even/Weil/CC27/RH.

**Method result:** choosing first- and second-moment original Loewner bounds independently yields a meaningful **valid but incomplete** improvement for the 16-cell original cases (Gersh bound deficits fall by ~2.76 and ~2.87). The 32-cell candidates neither improve the accepted MG40 bound nor establish source positivity. Do not mistake the finite rational-grid negative candidates for a universal nonscalar-method impossibility. This is a recombination of **existing** accepted original source information, not a genuinely new physical original Fourier measurement.

**MG44 next obligation:** derive additional original complete-frequency **source-specific correlated** first-/second-moment bounds, especially on the exact negative rational directions exported by MG43 and the fee-budget directions of MG42. Any new estimate must provide a proof-valid full original 24D Loewner upper for the true same 23-adapted-plus-pole residual and an exact source positivity acceptance gate. Further reuse of the same coarse independent MG24/MG29 scalar family without new correlations is unlikely to settle the remaining spectral obligations.

---

# MG43 — Independent original first- and second-source moment Loewner recombination

October 20–21, 2026. Stacked on [MG42 PR #291](https://github.com/monocap-tech/weil-lab/pull/291). MG42's independent exact-rational original-source audit [Actions #39520549337](https://github.com/monocap-tech/weil-lab/actions/runs/39520549337), replayed at final head [Actions #39520956951](https://github.com/monocap-tech/weil-lab/actions/runs/39520956951), certified four exact proportional mixed first-moment uncertainty fee thresholds for the best nonscalar original B. In the best MG29 32-cell k16 case, only 3/32 of the current fee is proven tolerable, whereas even 1/8 already produces a genuine rational negative direction of the conservative lower matrix. Mere numerical fee scaling cannot be promoted to an actual-original-source bound.

## New legitimate source-bound family (without inventing new physical information)

Both previously independently accepted full-real-frequency source moment calculations MG24 and MG29 bound **the very same original source matrices**, not distinct or substituted operators. They include the genuine SI10 physical source family, its MG11 23 two-boundary-adapted functions plus actual odd sinh pole, the original signed seven-prime/digamma Fourier multiplier and complete high-frequency tails.

For the original first moment G and second moment S, the accepted Loewner certificates are

```
LG24 <= G <= UG24;       S <= US24
LG29 <= G <= UG29;       S <= US29.
```

For real alpha,beta independently in [0,1], convexity provides two independently valid physical source enclosures:

```
LG(alpha)=(1-alpha)LG24+alpha LG29 <= G
G <= UG(alpha)=(1-alpha)UG24+alpha UG29
S <= US(beta)=(1-beta)US24+beta US29.
```

Importantly, **the alpha controlling first-moment uncertainty need not equal the beta controlling the positive second-moment upper**. MG39 investigated a single shared scalar blend only. Mixing first and second original moment bounds independently is valid even when their error matrices do not commute. No entrywise extrema or invented Loewner matrix maximum is used.

For any already accepted **genuine nonscalar original source response** `B=tI+D`, with `t>=0`, set `Gc=(LG+UG)/2`, `E=(UG-LG)/2>=0`. The actual original all-frequency coupled source residual satisfies the full original 24D Loewner matrix bound

```
R(B)^T R(B) <= Hup -2t LG(alpha)
  -Gc(alpha) D -D^T Gc(alpha)
  +B^T US(beta) B
  +eta E(alpha) +eta^-1 D^T E(alpha)D,   eta>0.
```

The final two terms are justified by MG40's independently proven block-PSD Cauchy–Schwarz uncertainty lemma. This is a **VALID new mathematical combination of existing independent original measured source moment information**. It is not a new Fourier integration, a physical input discovery, or an artificial scaling of the original error fee. It is not assumed to be Loewner better than either parent.

## Original MG43 exact-rational experiment and independent acceptance

For each of the four accepted MG42 best nonscalar B responses (original 16/32-cell MG29 meshes × k12/16), evaluate the finite rational grid

```
alpha in {0,1/4,1/2,3/4,1},
beta in {0,1/2,1},
eta in {1/64,1/16,1/4,1/2,1,2,4,16,64}.
```

There are 5×3×9=135 rigorous candidate complete-source residual matrix UPPER certificates per scenario, **540** total. Keep the original MG40 bound as historical comparison, not as a substitute for proving an MG43 bound. Numerical smallest-eigenvalue estimates may rank candidates for exact checking, but are NOT used to prove signs or source contraction.

Export the actual full 24×24 original rational UPPER `U` and lower-source `Hlo−U` of the proposed best parameter triplet per scenario. Independently reconstruct **all 540** 24D exact rational original source candidate matrices and their exact Gershgorin margins/traces from archived MG24, MG29, MG40, MG41, MG42 source artifacts. The selected candidate's actual mathematical classification must be either:

- **STRICT SOURCE PD:** 24 positive exact rational LDL Schur pivots of `Hlo−U`.
- **STRICT NEGATIVE SOURCE CERTIFICATE RAY:** explicit nonzero exact rational v with `v^T(Hlo−U)v<0`. This is a failure of this conservative lower certificate, NOT a negative mode of the actual operator.
- **INCONCLUSIVE:** no exact sign witness; never promote floating estimates.

Because MG41 showed that the existing MG40 fee-bearing 24D source lower matrices have true exact negative rays while all optimistic zero-fee matrices are positive, this experiment tests whether a better allocation of **already valid independent full-source moment uncertainty** across the G and S terms can narrow that gap WITHOUT violating any source-covariance Loewner inequality.

## Limitations

MG43's alpha/beta/eta grid is not continuous or a proof of optimality. Even if all selected trial matrices remain unhelpful, genuinely new original correlated G/S source information may make a different route viable. Even a strictly positive one of these finite original 24D source residual certificates would not establish source-subspace invariance, a full original 470D strong inverse, signed odd 51/56 cap, independent Fourier/form-domain identification, complete even/Weil/CC27/RH or the Riemann hypothesis.

**Original-source exact calculation and independent 540-case matrix audit PASSED. No source contraction.**
