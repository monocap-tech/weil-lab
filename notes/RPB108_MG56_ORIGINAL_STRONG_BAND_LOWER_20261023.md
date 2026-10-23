# MG56 — Genuine original pole-corrected strong-action 24D Fourier-band lower

**Status: mathematically derived implementation, exact numerical and independent verification PENDING CI.** Parent [MG55 #304](https://github.com/monocap-tech/weil-lab/pull/304) independently verified the 18 original changed-response Jensen certificates and showed its inherited MG24 whole-frequency original action-second-moment lower was negative semidefinite. MG56 tackles that exact obligation by constructing **NEW** original action-second-moment information, rather than searching response blends again.

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
