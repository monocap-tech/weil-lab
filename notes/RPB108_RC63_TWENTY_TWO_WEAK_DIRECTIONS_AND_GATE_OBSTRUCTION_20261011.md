# RPB108 RC63 — 22-feature weak directions and gate obstruction

RC63 certifies actual weak combinations of the 22 native Riesz features. They impose the following ceiling on any uniform canonical head floor:

\[
\boxed{h_{22}\le 1.729203922546154\ldots\times10^{-10}<1.8\times10^{-10}.}
\]

The exact outward rational ceiling is stored in the certificate. This is more than **1,900 times smaller** than RC57's actual low-eight floor 1/2,900,000. That low-eight result remains valid on its original space, but the same floor **cannot extend to the 22-feature head or any native superspace containing it**.

In particular, the head-floor requirement of RC57's conditional 1250-feature gate is now ruled out. The conditional theorem itself is not invalidated; its head hypothesis cannot hold on that enlarged native space. RC63 does not prove an actual negative original Weil direction or whole-aperture indefiniteness.

## Fixed rational witnesses

For a real rational coefficient vector v, define the actual canonical vector

\[
u(v)=\sum_{j=0}^{21}v_jR_j.
\]

The validator embeds six fixed rational witnesses with denominator 10^12: two weak combinations and one positive control in each parity sector. Their coefficients are stored explicitly. A floating calculation suggested candidate directions, but the validator uses no floating eigenvalues or eigensolver. Every accepted bound is reconstructed with exact rational arithmetic and certified square-root upper bounds.

The physical norm p=v*P22 v and RC59's actual metric bounds give

\[
\frac3{10}p\le\|u(v)\|_{\rm can}^2\le\frac{252}{257}p.
\]

RC60 supplies correlated physical and canonical Riesz-error Gram uppers. RC62 supplies the correlated nominal original-source covariance. These are evaluated on the complete witness vector, retaining cancellation among its feature coefficients.

## Actual directional Weil bounds

Let e=v*Ep_up v, c=v*Ec_up v, t=v*T v and s=v*Uplus_up v. The actual trial original-source norm is at most

\[
S_v=\sqrt{s}+\delta_S\sqrt{t}.
\]

RC61's actual trial Weil entry intervals give an exact quadratic center b and paid radius r for the same vector. The original-source identity then gives

\[
b-r-2\sqrt e\,S_v-k_{\rm parity}e-c
\le Q(u(v))\le
b+r+2\sqrt e\,S_v+k_{\rm parity}e.
\]

The negative canonical error Gram retains its sign in the upper bound. Square roots are bounded upward by exact integer-square-root arithmetic with denominator 10^30; final quadratic and Rayleigh endpoints are rounded outward rationally. Signed Rayleigh lower bounds use the correct lower metric denominator when the quadratic lower endpoint is negative.

The resulting canonical Rayleigh intervals have these outward decimal summaries:

| Parity and witness | Actual Rayleigh lower | Upper | Certified sign |
|---|---:|---:|---|
| Even weak 0 | -2.949211e-10 | 2.782658e-10 | Unresolved |
| Even weak 1 | -2.485153e-10 | 2.362358e-10 | Unresolved |
| Odd weak 0 | -1.868438e-10 | 1.729204e-10 | Unresolved |
| Odd weak 1 | -1.904840e-10 | 2.137337e-10 | Unresolved |
| Even positive control | 8.572456e-10 | 4.292218e-9 | Positive |
| Odd positive control | 1.330475e-7 | 7.008590e-7 | Positive |

All 22 individual feature signs certified in RC62 remain positive. The weak combinations show why those individual signs do not establish a comparable uniform floor.

For each of the four weak witnesses, the exact certificate proves

\[
Q(u(v))-\frac1{2,900,000}\|u(v)\|_{\rm can}^2<0.
\]

This is a negative value of the shifted form, not a negative original Weil value. The strongest ceiling comes from odd weak 0. The same actual vector remains in every native superspace containing the first 22 features, so the obstruction automatically applies there.

## Consequence for the scalar Schur budget

RC57's conditional 1250 gate used the inherited 1250-complement floor a=247/2500 and squared source budget gamma=1/64,000,000. The scalar norm-based Schur estimate has reserve h-gamma/a.

Since any admissible enlarged-head floor h is at most the certified ceiling above, a positive reserve using this inherited complement floor requires its source budget to satisfy

\[
\gamma<a h\le a\,h_{\rm ceiling}
=1.708453475475600\ldots\times10^{-11}.
\]

The old source budget is more than **900 times larger** than that ceiling. This is a limitation of this scalar sufficient criterion with the inherited complement bound. It is not a lower bound on the actual projected-source covariance, does not rule out a sharper projected-source estimate, and is not a necessary condition for positivity by every method.

The complement floor used here still belongs to the 1250-feature complement. No 22-feature complement floor is inferred.

## Independent replay and next frontier

Generation and replay pass. Replay independently reconstructs the directional Gram quadratics by upper-triangle bilinear sums, checks all square-root allowances by exact squared inequalities, rebuilds the actual signed Rayleigh endpoints, and checks the four strict shifted-form witnesses and the two positive controls. Input hashes connect the computation to RC59 through RC62 and the original RC57 gate.

From the repository root:

```sh
python scripts/validate_rpb108_rc63_twenty_two_weak_floor_obstruction.py > certificates/rpb108_rc63_twenty_two_weak_floor_obstruction.json
python scripts/validate_rpb108_rc63_twenty_two_weak_floor_obstruction.py --replay certificates/rpb108_rc63_twenty_two_weak_floor_obstruction.json
```

The next frontier is the actual projected-source residual and a sharper treatment of these weak combinations. A positive uniform 22-feature floor remains open at a much smaller scale; the low-eight floor cannot serve as the enlarged-head target. No actual head indefiniteness, whole-aperture positivity, aperture extension, RH, or F4 completion is claimed.
