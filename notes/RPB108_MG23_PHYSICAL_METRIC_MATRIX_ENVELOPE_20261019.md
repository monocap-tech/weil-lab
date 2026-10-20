# MG23 — Keep the physical source metric in the complete-frequency residual envelope

October 19, 2026. Stacked on [MG22 #271](https://github.com/monocap-tech/weil-lab/pull/271), whose actual-original whole-frequency scalar trial passed focused Actions. The active canonical obstruction is still **W-ODD-NEG: OPEN**. MG23 does not calculate the full 470-source inverse, the true coupled moment matrices, or the signed negative cap.

## Structural change, not a new source-count campaign

MG22 proved a genuine complete-frequency one-step trial for the 23 physical dual-boundary-adapted odd source functions, and a stronger one on the genuine 22-dimensional pole-null subspace. However its scalar path used

```
||A_o Fz||^2 <= M_k^2 tr(H) ||z||^2 + tau_k ||z||^2
K0_old = (M_k^2 tr(H)+tau_k)/ell
```

where the real physical Gram is `H=F*F >= ell I`. This spends the source trace-to-minimal-eigenvalue ratio before examining the pole correction. In fact MG12 already proved the stronger complete-frequency **matrix** inequality

```
S_o = (A_o F)*(A_o F) <= M_k^2 H + tau_k I
```

for the **actual original multiplier**, not selected frequency cells. The low-frequency multiplier bound applies to the true `||Fz||` norm, and MG11 pays the whole-real high-frequency strong tail `tau_k I`. Consequently

```
K0_new = M_k^2 + tau_k/ell
```

is a valid relative upper on the entire physical frame, and therefore on its 22D pole-null hyperplane. This strictly improves MG22's pole-null scalar upper because `tr(H)>ell`. No numerical conditioning guess is involved.

## Retain the exact rank-one pole coupling

Write `b=F*s`, `sigma=||s||^2`, `Astar=Ao-2|s><s|`. For any exact positive rational `eta`, vector Young gives the complete ORIGINAL-frequency matrix Loewner envelope

```
Sstar <= (1+eta)(M_k^2 H+tau_k I)
        + 4(1+1/eta)sigma b b*
```

without discarding the 23D coupled source geometry. This is a **matrix upper bound on the genuine strong action**, but **not an evaluation of the exact original `Sstar`**. By ambient Cauchy–Schwarz, `bb* <= sigma H`, so the following completely rigorous scalar consequence is available for a one-step trial:

```
Kstar(eta) = (1+eta)(M_k^2+tau_k/ell)
             + 4(1+1/eta)sigma^2.
```

MG23 tests rational `eta` and all MG22 dyadic cutoffs `k=12,16,20,24,30`, reconstructing the actual 25D physical interval Gram, double-boundary transform, physical 23D metric, and nonzero original pole overlap. For full 23D, the accepted scalar `Kstar` is the smaller of the new bound and MG22's older valid bound; on the 22D pole-null frame the new `K0` is strictly better.

## Genuine one-step residual — no unwarranted iteration

By the inherited positive form bounds, conditional on original Fourier/form/domain identification,

```
< Astar h,h > >= kappa_star ||h||^2
< Ao h,h > >= kappa ||h||^2
kappa_star = 33621/10^9;  kappa = 1/1000.
```

For `J=F` and true physical `Y=tF`, the complete residual `R_t=F-tAstar F` satisfies

```
R_t*R_t <= (1-2t kappa_star+t^2 Kstar) H.
```

The exact optimal scalar choice `t=kappa_star/Kstar` gives a valid positive squared-residual gap `delta_star=kappa_star^2/Kstar`. For `b*z=0`, `Astar Fz=Ao Fz` as an ambient physical function and the same argument gives `delta0=kappa^2/K0`.

**Critical nonclaim:** Neither `(I-tAstar)Fz` nor its image under another residual application is generally inside the finite 23D frame. These finite-source inequalities are not invariant-subspace or full-Hilbert contraction theorems. Therefore they cannot be iterated into a Neumann inverse. A better finite-frame residual margin by itself does not settle MG07's original 470D signed 51/56 negative cap.

## Test and acceptance doctrine

- Use exact rational arithmetic for all cutoffs, multipliers, strong tails, Young parameters and squared-residual gaps; never export positive small gaps through coarse decimal truncation.
- Independently validate the H-relative formula, the rank-one Cauchy upper, MG22 fallback, and nonpromotion fields in Actions.
- Report the precise MG22-to-MG23 improvement, but do not infer useful resolvent conditioning without checking the quantitative gap against the signed-negative budget.
- Explicitly keep the original `Gstar` and `Sstar` *uncomputed*; this is a **symbolic Loewner envelope with original physical interval inputs**, not an exact coupled low-band source moment matrix.
- Maintain full470 inverse, original signed odd, even, Weil/CC27, RH and independent Fourier/domain checks as **OPEN**.

**Next acceptance after MG23:** Calculate the same-basis complete low-band **coupled** `G_o` and `S_o` with all source off-diagonals and entire high tail, then the actual mixed pole response `c=F*A_o s`. Assemble

```
Gstar = Go - 2bb*
Sstar = So - 2(cb*+bc*) + 4 sigma bb*
R*R = J*J - J*Astar Y - Y*Astar J + Y*Astar^2 Y
```

for the relevant **original 470-source** map. Test the full signed 51/56 cap only after that complete residual is certified. The pole-null 22D decomposition is useful structure, but is not itself the missing signed certificate.

**Verification status at authoring:** MG23 implementation and independent CI gates are submitted for Actions; new numeric gains are not claimed until that run passes.
