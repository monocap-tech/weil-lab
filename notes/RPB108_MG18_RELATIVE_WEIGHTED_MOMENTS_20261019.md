# MG18 — Relative original multiplier payment on the same nonflat source panels

October 19–20, 2026. MG17 #266 passed its complete 24-cell original nonflat-frequency source calculation (Actions 39354119529), but direct SM46 weighted source moments performed *worse* than an identical-cell constant-weight reference. For A_o first moment the weighted-minus-constant lower reference trace was -0.008043; both retained inertia 3 positive, 21 negative. For A_o² the weighted-minus-constant lower trace was -0.0299816 and lower inertia was 2 positive /22 negative against 3 positive /21 negative in the constant reference.

The suspected reason is the **absolute multiplier-reference error fee**, which charges the positive Fourier-source covariance via a large source-dependent diagonal matrix independent of the actual reference weight. This is a certification loss and NOT actual operator negativity.

## New exact weighted relative Loewner method

Let the true original positive multiplier be w(xi)=a_o(xi), and the certified piecewise affine reference be w_ref(xi)>0 on each real original MG17 panel. SM43A rigorously proves |w-w_ref|<=epsilon for EVERY real xi in the cell. The reference itself has a CERTIFIED positive rational minimum wmin (for affine signed-positive max, the minimum of its endpoint affine values clipped at kappa). Put theta=epsilon/wmin. For p=1,2:

  lambda_-^(p)=max(0,1-theta)^p;
  lambda_+^(p)=(1+theta)^p;

and pointwise

  0<=lambda_-^(p) * w_ref(xi)^p
       <= w(xi)^p
       <= lambda_+^(p) * w_ref(xi)^p.

This is an exact relative comparison EVEN if theta>=1, in which case the lower factor is correctly zero and a method failure may result. No positivity is invented.

The original SM46 first/second weighted source moments J0,J1,J2 and the MG11 true Fourier source affine vector V=v+d*(xi-mid) are independently preserved. Let C_p=J0 vv^T+J1(vd^T+dv^T)+J2 dd^T be the complete source weighted reference covariance. For actual original Taylor errors |e_i(xi)|<=r_i, the complete source error satisfies ee^T<=D_r=(sum r_i)diag(r_i). With rational 0<tau<1, whole-matrix Young proves

 (1-tau)C_p-(tau^-1-1)J0 D_r
    <= int_cell w_ref^p T T^T
    <= (1+tau)C_p+(1+tau^-1)J0 D_r.

The NEW exact original TRUE weighted bound is therefore

 2lambda_-[(1-tau)C_p-(tau^-1-1)J0 D_r]
    <= true original M_p(cell)
    <= 2lambda_+[(1+tau)C_p+(1+tau^-1)J0 D_r].

Because the positive multiplier factor is applied **to the actual positive source integral first**, this is a valid full 24x24 Loewner bound even though the already conservatively approximated lower reference need not be PSD. It preserves all 576 mixed entries, the original sinh pole and signed digamma/seven-prime multiplier.

Compare on exactly the SAME 24 MG17 certified nonconstant original frequency cells against BOTH previous independently accepted complete 24x24 methods:

- constant true whole-cell multiplier extrema and MG15 sourcewise Taylor error, optimized over same seven rational Young parameters;
- MG17 absolute signed-affine weighted reference and its whole-cell 2*width*eta*D_q multiplier mismatch, optimized over same seven parameters;
- new MG18 RELATIVE signed-affine original multiplier and sourcewise error as above, optimized over seven parameters.

The validator regenerates the MG17 original scout and full exact source matrices, compares certified earlier accepted constant/absolute trace differences and inertias EXACTLY, then certifies rational 24D lower-reference inertia for all three new full lower/upper matrices. Positive lower reference trace is not accepted as true source or full operator positivity.

## Method acceptance

If the relative method beats constant (or at least absolute weighted) in lower-reference inertia or has improved directional margins, continue to refine the remaining weak source directions. If theta is too large and lambda_-=0, reject this particular cellwise relative bound and seek source-correlated multiplier remainder instead. Do NOT shift to whole 470 source or original RH claims.

Only selected original 24 real-frequency cells are covered; original complete Astar² pole action, full [0,Lambda] low band, genuine source23 Galerkin residual, complete full 470 inverse/infinite odd complement and even/Weil/CC27/RH remain OPEN. Independent original Fourier/form-domain audit remains OPEN.


## Final accepted exact-rational MG18 result

Focused GitHub Actions [39355874992](https://github.com/monocap-tech/weil-lab/actions/runs/39355874992) **PASSED** the full true-original source first and second moment rational computation, exact MG17 same-panel constant/absolute method replay and independent 24D exact lower-reference inertia checks.

On the SAME 24 rigorously nonconstant original frequency cells, complete source/pole matrices have:

| Comparison with same-panel constant bound | First \(A_o\) moment | Second \(A_o^2\) moment |
|---|---:|---:|
| Relative LOWER-reference trace gain | +3115445033/250000000000 (~+0.012462) | +2573853639/31250000000 (~+0.082363) |
| Relative UPPER-reference trace reduction | +4125459873/250000000000 (~+0.016502) | +5668611171/50000000000 (~+0.113372) |
| Relative lower-reference inertia | 3 positive, 21 negative | 3 positive, 21 negative |
| Negative lower-reference directions recovered | 0 | 0 |

MG18 therefore **successfully reverses MG17's adverse absolute-weight error budget** without changing the original Fourier multiplier, selected source space, or frequency panels. Its exact relative upper/lower Loewner matrix traces are greatly improved, but neither complete rational lower reference is PSD.

**MG18 method decision:** ACCEPT relative whole-source multiplier-error charging as an effective enclosure improvement; REJECT it as standalone sufficient to close the spectral gate. Next compare with MG19's independent tighter whole-cell reference intersection, then distinguish ideal affine source rank from certified uncertainty loss. No original entire-band Astar², 470D residual/inverse or full odd/even/Weil/RH result follows.
