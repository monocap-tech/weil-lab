## MG56 — Independently VERIFIED original corrected-action lower, strictly negative-definite (a method no-go)

Original full24 true physical strong-action source production and distinct independent replay [Actions #39894269994](https://github.com/monocap-tech/weil-lab/actions/runs/39894269994) **PASSED**. Original 32-cell corrected [0,4] Fourier lower artifact `mg56-original-0to4-true-pole-corrected-strong-action-24D-band-lower` ID **12475648897**.

A separate exact rational two-implementation structural/attribution check [Actions #39895407054](https://github.com/monocap-tech/weil-lab/actions/runs/39895407054) **PASSED** (forward and reverse full24 strict-positive LDL of `-L_[0,4]`, full trace decomposition and physical cell attribution). Audit artifact `mg56-original-strong-action-exact-negative-lower-error-census` ID **12476233679**.

| Accepted result | Value |
|---|---:|
| New true original pole-corrected strong-action band LOWER trace | −360.680532369788 |
| New full24 strong lower Gershgorin estimate | −33.847273281487 |
| Positive original coordinate directions certified | **0/24** |
| New 24D lower inertia | **STRICTLY NEGATIVE DEFINITE**, independently certified |
| Archived MG24 k12 full-strong LOWER trace | −6339.904841877821 |
| Archived MG24 k16 full-strong LOWER trace | −6794.957104231404 |
| New band lower minus each accepted MG24 full-strong lower | **PSD in BOTH cases** |
| Exact raw 32-cell affine strong-action source signal trace | +4.996571884566 |
| Exact raw 32-cell Young error-charge trace | **365.677104215189** |
| Three physical cells [1/8,1/2] share of the full error charge | **78.8933861581%** |

**Interpretation:** The new original physical action lower improves both MG24 old full source lower matrices in Loewner order, but it remains **strictly negative definite**, not merely indefinite. Since the TRUE physical strong-action moment satisfies `S_*=(A_*F)^*(A_*F)>=0`, the trivial zero matrix is already a STRICTLY BETTER full24 lower than this entire new MG56 certificate. Thus this candidate gives **no useful positive curvature for any response difference direction** and cannot repair MG55's response convex-hull bounds. A strictly negative **conservative LOWER** matrix is NOT a negative source physical action/eigenmode, and makes no claim about RH.

**Method-level cause:** This is a massive **error-bound loss**, not evidence of negative physical strong energy. For accepted 32 true original positive-frequency cells, raw physical source affine signal contributes approximately 5.0 to trace, whereas independently charged source/multiplier/pole remainder radii induce approximately 365.7 in diagonal Young penalties. Just the adjacent original positive real-frequency cells [1/8,1/4], [1/4,3/8], [3/8,1/2] are responsible for 78.9% of those charges. Merely shrinking arbitrary other cells or revisiting scalar tau searches cannot resolve the main obstruction efficiently.

**MG57 should localize and recombine the SAME-CELL pole/strong-multiplier error** specifically in those three cells. First establish how much of the large error radius is due to multiplier interval, original adapted-source Taylor drift, and independent global pole-column uncertainty, with an independent certified numerical attribution. Then pursue a new band moment enclosure that retains the **joint physical source/pole cross covariance** before diagonal Young domination. A positive exact rational 24×24 action-moment lower is still a distinct open obligation, and the other 470D/odd 51/56/even/Weil/RH gates remain OPEN.

---

# MG56 — Genuine original pole-corrected strong-action 24D Fourier-band lower

**Status: independently VERIFIED original action source Loewner certificate; strongly NEGATIVE DEFINITE, hence dominated by the intrinsic zero PSD lower.** Parent [MG55 #304](https://github.com/monocap-tech/weil-lab/pull/304) independently verified the 18 original changed-response Jensen certificates and showed its inherited MG24 whole-frequency original action-second-moment lower was negative semidefinite. MG56 tackles that exact obligation by constructing **NEW** original action-second-moment information, rather than searching response blends again.

## Actual original operator and physical Fourier formula

The original physical 25-source SI10 map F, MG11's 23 two-boundary adapted sources plus the actual sinh pole s in 24D, and original signed seven-prime/digamma archimedean strong action `A_*=A_o-2|s><s|` remain unchanged. Write the genuine original source Fourier transform `t(xi)` in the adapted 24D coordinates and the genuine pole column `b=F^*s`, enclosed by MG24's independently accepted exact rational component intervals `bmid±brad`. Then the TRUE original pole-corrected action-source Fourier transform is

```
u_j(xi) = a_o(xi)*t_j(xi) - 2*t_p(xi)*b_j.
```

This is NOT the unpoled second moment `S_o`, and it is NOT an arbitrary source response B or a surrogate constant multiplier.

The original whole physical 24D strong-action moment is
`S_*=(A_*F)^*(A_*F)=int_real u(xi)^*u(xi) dxi`, hence is positive semidefinite. Its true original Fourier-band moment `S_[0,4]` (with the reflected negative frequency interval) is also PSD and satisfies

```
S_* >= S_[0,4] >= L_[0,4],
```

with the last bound derived from genuine same-cell rational interval data.

## New exact Fourier source interval construction

Reuse MG29's independently accepted 32 genuine original physical source cells covering all positive frequencies [0,4], with their actual fourth-derivative supported Taylor radii. On a cell `[left,right]` (width h, midpoint xi0), let `x=xi-xi0` and

```
t(xi)=v+x*d+e(xi), |e_j|<=r_j,
a_o(xi)=ac+delta_a(xi), |delta_a|<=da,
b_j=bmid_j+delta_b_j, |delta_b_j|<=brad_j.
```

The exact physical corrected action affine central part is
`u0_j=ac*v_j-2*v_p*bmid_j`,
`u1_j=ac*d_j-2*d_p*bmid_j`, with rigorous cellwise uniform error

```
rho_j = |ac|*r_j
  +da*(|v_j|+(h/2)*|d_j|+r_j)
  +2*|bmid_j|*r_p
  +2*brad_j*(|v_p|+(h/2)*|d_p|+r_p).
```

Because the true multiplier deviation is a common scalar and the pole correction uses the same `t_p`, this radius encloses the ACTUAL original corrected action; no separate coordinate may independently change multiplier sign. (The new bound remains conservative and does not yet take all cancellations.)

For any 0<tau<1, accepted MG15 affine directional Young inequality gives exact original cellwise source MOMENT lower and upper

```
L_cell=2h*(1-tau)*(u0*u0^T+h^2*u1*u1^T/12)
       -2h*(1/tau-1)*diag(rho_i*sum_j rho_j),

U_cell=2h*(1+tau)*(u0*u0^T+h^2*u1*u1^T/12)
       +2h*(1+1/tau)*diag(rho_i*sum_j rho_j).
```

The factor 2 covers the actual negative-frequency mirror. Exact rational Young tau chosen per physical cell to maximize its lower trace from a **fixed accepted** finite grid. Sum all 32 original cells and use the independently accepted outward-rational compaction to obtain new genuine full24 `L_[0,4]<=S_[0,4]<=U_[0,4]`.

This creates an actual full original all-real-frequency Sstar lower because the omitted physical second moment is PSD, not because any source frequencies were assumed absent.

## Acceptance and scope

Producer and independently written verifier regenerate the same physical source cells, midpoint action and derivatives, componentwise rational error radii, fixed-grid tau, rank-one cell midpoint integration, diagonal Young fees, exact 24×24 lower/upper matrices and PSD bracket widths. The independent verifier accumulates full24 quadratics WITHOUT calling MG56's producer or its cell accumulator. Source Gram and true pole b are independently reloaded from accepted MG24 physical original source.

Export exact full24 inertia classification, a rational negative-ray witness if indefinite, any strictly positive **coordinate** lower bounds and comparisons against inherited MG24 k12/k16 negative semidefinite whole-frequency strong lower. A positive coordinate bound certifies that **one original source direction** has nonzero strong action; it does **not** certify the full 24D Sstar matrix positive definite. Conversely, an indefinite conservative `L_[0,4]` is not a negative physical strong-action eigenvalue.

Only full exact rational LDL `L_[0,4]>0` may be called a genuine full24 strong-action coercivity result, and even that would leave the original source residual contraction, full original 470D inverse, odd signed 51/56 spectral cap, independent Fourier/form/domain audit, even/Weil/CC27/RH all OPEN.

If the present local lower remains indefinite, the next meaningful gate is to sharpen the exact *physical corrected-action* interval contributions (or jointly include genuine [4,8] action source) until a positive lower is certified on a useful whole response-difference subspace. Do not promote a broad loose strong-moment lower or a few positive ray estimates to global positivity.
