## Accepted original MG42 result — October 20, 2026

[Actions #39520549337](https://github.com/monocap-tech/weil-lab/actions/runs/39520549337) **PASSED** calculation and independent exact rational reconstruction from pinned accepted original MG24, MG29, MG40 and MG41 source artifacts. Accepted artifact `mg42-original-four-nonscalar-relative-PSD-fee-thresholds`, ID `12310044133`. The independent auditor reconstructed ALL four full original 24×24 ideal matrices and PSD mixed-G fees, original signed pole-corrected complete-frequency source data, and **28** exact positive-LDL/negative-Rayleigh endpoint and bisection proof checks.

Best original nonscalar B on all four source cases was `matrix_ridge_1/10_blend_1/2`. For `M(s)=Mideal-sF`, `Mideal≻0` and `F≽0`, the EXACT rational witnesses give:

| MG29 original mesh | cutoff k | accepted 24D exact positive-definite scale s_low | accepted rational negative-Rayleigh scale s_high | counterfactual fee reduction SUFFICIENT | fee reduction still NECESSARILY INSUFFICIENT at s_high |
|---|---:|---:|---:|---:|---:|
| 16 | 12 | **7/16 = 0.4375** | **15/32 = 0.46875** | >=**56.25%** | **53.125%** reduction insufficient |
| 16 | 16 | **13/32 = 0.40625** | **7/16 = 0.4375** | >=**59.375%** | **56.25%** reduction insufficient |
| 32 | 12 | **1/8 = 0.125** | **5/32 = 0.15625** | >=**87.5%** | **84.375%** reduction insufficient |
| 32 | 16 | **3/32 = 0.09375** | **1/8 = 0.125** | >=**90.625%** | **87.5%** reduction insufficient |

All four completed all five exact dyadic bisections (certified interval width 1/32); none relied on unverified floating signs. Strict positivity at s_low and strict negative quadratic at s_high mean the true generalized positivity threshold for each fixed `Mideal,F` lies **between** the endpoints. The endpoint bounds extend to every smaller/larger positive fee scale respectively by PSD monotonicity. The source-fee requirement is dramatically more demanding for the MG29 32-cell enclosures, even though MG40's signed Gersh margins were better in those cases; these are different matrix metrics and must not be conflated.

**Accepted mathematical disposition:** MG42 quantifies exactly the relative **COUNTERFACTUAL** directional uncertainty budget for four *fixed existing* nonscalar response matrices and *frozen* original H/G/S center enclosures. It is NOT a new acceptable smaller bound on the original physical residual; actual original Gstar uncertainty remains certified only with the full F at s=1 and has verified rational negative directions. A valid reduced source fee requires **new rigorous original coupled moment information** (MG43 candidate obligation), not merely numerical scaling or optimizing eta. The result proves no actual original 24D source contraction, no invariant source extension, no complete 470D strong inverse or signed original 51/56 cap, and no complete even/Weil/CC27/RH.

---

# MG42 — Exact relative mixed-G uncertainty budget for the genuine original nonscalar sources

October 20, 2026, stacked on [MG41 PR #290](https://github.com/monocap-tech/weil-lab/pull/290). MG41's accepted original 24D full-matrix independent audit [Actions #39519080670](https://github.com/monocap-tech/weil-lab/actions/runs/39519080670) proved, for ALL 24 original MG40 nonscalar B trials, that the hypothetical zero-cross-fee matrix `Mideal=Hlo-Ucore` is **STRICTLY POSITIVE DEFINITE** (all 24 rational LDL pivots positive), while the actually certified MG40 matrix `Mactual=Mideal-F` has a **STRICTLY NEGATIVE RATIONAL RAYLEIGH** direction. The result concerns conservative source certificates only, not actual signed Weil operator negative spectrum.

## Measure the exact allowable original-source fee instead of tuning a trace

Keep the actual original SI10 25 physical generator/MG11 23 boundary-adapted + genuine sinh pole 24-dimensional source basis; the signed original seven-prime/digamma action, all real frequencies, physical source H, original Gstar first moment and Sstar second moment are inherited from accepted MG24 #39378465438, MG29 #39440914565, and source-response MG40 #39513403010 and MG41 #39519080670.

For each original accepted **best nonscalar B** at k12/k16 and mesh 16/32, independently reconstruct exact rational symmetric original full 24D matrices

```
Mideal = Hlo - [Hup-2t LG -GcD-D^T Gc+B^T US B],
F = eta E + eta^-1 D^T E D >= 0
      (or original MG30 isotropic fallback, also >=0)
E=(UG-LG)/2>=0, Gc=(LG+UG)/2, D=B-tI.
```

MG41 proved `Mideal>0` and a strictly negative rational quadratic of `Mideal-F` at fee scale `s=1`. MG42 studies the **COUNTERFACTUAL PARAMETER FAMILY**

```
 M(s)=Mideal - s F,    s>=0.
```

Since F is PSD, `M(s)` is Loewner-decreasing as s increases. There is a critical threshold `s*` at which the matrix ceases to be positive definite. MG42 does **not** infer this threshold from floating eigenvalues. It constructs **two exact rational dyadic witnesses**:

- `s_low`: a full 24-positive-pivot **EXACT rational LDL** certificate `M(s_low)>0`.
- `s_high`: an **EXACT rational nonzero vector v** with `v^T M(s_high) v<0`.

Therefore `s_low<s*<s_high` when both endpoints are strict (the strict first failure may be singular at the boundary). In particular, reducing the original certified fee by at least `1-s_low` *would be sufficient* for this fixed B/moment-center **IF** independent new original moment work could rigorously prove a truly valid upper at such a reduced fee. Conversely, even the idealized proportional fee reduced by `1-s_high` remains insufficient to give this particular certificate strict positivity when the upper endpoint has a negative rational witness.

Each refinement uses midpoint `s=(s_low+s_high)/2`, accepts only a strict exact 24-pivot rational LDL or a strict exact negative Rayleigh witness, and otherwise leaves the interval safely inconclusive. At most five exact bisections (nominal width 1/32), separately for all four original k/mesh best nonscalar responses. A candidate numeric eigenvector is only a proposal and must be rationalized and checked exactly. The final artifact exports the complete genuine-original rational `Mideal`, `F`, and all exact endpoint/bisection witnesses for an **independent** rerun. This is a directional/generalized-fee-budget classification, not trace tuning.

## No false spectral promotion

This is **NOT** a certificate that `Mideal - sF` for `s<1` bounds the actual original source residual. The verified original first-moment uncertainty currently requires the FULL fee `F`. Until a new original coupled source estimate proves `sF` rigorously valid, smaller-fee cases remain counterfactual. The accepted actual fee has scale `s=1` and fails strict source positivity for these four B. No original full-470 source-space inverse, signed 51/56 odd negative cap, independent Fourier/form-domain criterion, complete even/Weil/CC27/RH is established.

**MG43 possible next step:** Design/source-certify *new coupled first-moment uncertainty* specifically along rational worst-directions from MG42, and compare its actual matrix fee against the exact relative PSD budget. Merely adjusting eta or reducing scalar traces without a **valid** new original Loewner upper is not sufficient.

**MG42 source calculation and independent exact rational audit PASSED; only counterfactual scale budgets certified.**
