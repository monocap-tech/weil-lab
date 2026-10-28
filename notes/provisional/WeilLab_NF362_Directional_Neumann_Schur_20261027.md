# Weil-Lab — NF362: directional Neumann–Feshbach reduction for original `W-ODD-NEG`

**Date:** 2026-10-27. **Custody:** Read-only analytic continuation of NF361, no GitHub writes, no changed source selection, no imported positivity theorem. `W-ODD-NEG` and RH **OPEN**. Original operator/form identification and stronger exterior floor's native CI acceptance remain independently open.

## 0. Decision

NF361 rules out the convenient uniform `N242 <= 0.99832 G242` sufficient criterion under the locally replayed stronger exterior floor. Do not reattempt it. Instead retain the *actual* off-diagonal covariance and replace the infinite **signed** exterior resolvent by a short, monotone expansion in the **positive** exterior inverse, with a rigorously quantified complete-infinite remainder. This is a new **conditional analytic reduction**, not numerical acceptance of the moments.

## 1. Exact setup and inherited input

Let `A=A_star >= kappa_star I>0`, `K=K_minus >= 0` bounded, and `W=A-K` be the true odd original closed quadratic form on the supported physical odd Hilbert space. Let `J=J242` be the unchanged 242-dimensional selected original physical space, `F=J^perp`, `Q=P_F`, `E=A^-1 J`, and `H` and `L` the self-adjoint operators associated with the *compressed forms* `a|_F` and `k|_F` respectively (not `QA^-1 Q` or a commutative pointwise restriction). Let `C=H-L` be the signed exterior form operator.

The inherited accepted original J242 leakage is `0 <= L <= epsilon I` with exact epsilon from PR350, approximately `1.6767873157142093e-5`. The older accepted exterior floor is `C >= mu_old I`, `mu_old=0.001-epsilon`. A newer `mu_new=0.009981124873103...` floor has been locally replayed in NF356 but is *not* repository-native-Arb accepted. In the mathematical implications below use any valid `mu>0` satisfying `C>=mu I`.

For every `v in F` from the common form domain,

```
a_F(v,v) = w_F(v,v)+k_F(v,v) >= mu ||v||^2 + k_F(v,v)
             >= (1+mu/epsilon) k_F(v,v).
```

Hence, with `r=epsilon/(mu+epsilon)`:

```
0 <= L <= r H,    0 <= T=H^-1/2 L H^-1/2 <= r I,     r<1.
```

This is a **form-order** assertion; it does not assert that the full original A operator preserves F.

## 2. Exact original energy-dual Schur and small-contraction expansion

For `h in J`, put `e=A^-1 h in E` and `g=Q K e in F`. The full signed Feshbach correction is

```
D[h]=<g,C^-1 g>=<x,(I-T)^-1 x>,   x=H^-1/2 g.
```

This follows from the original `A`-form orthogonality `a(e,v)=0` for `v in F`; therefore the entire original signed mixed coupling equals `-k(e,v)`. It is not the physical-Schrödinger `QWJ` coupling, and no positive-frequency cross was discarded.

For each `j>=0`, set `M_j[h]=<x,T^j x> >=0`. In the positive Loewner order on the **entire J242 coefficient space**,

```
D = sum_{j>=0} M_j,    0 <= D-sum_{j=0}^N M_j
       <= [r^(N+1)/(1-r)] M_0.
```

Positive-kernel Cauchy–Schwarz and the exact form restriction give

```
M_0 = sup_{v in F} |k(v,e)|^2/a_F(v,v) <= r k(e,e).
```

Thus the complete, *all-infinite* tail satisfies the stronger **directional** bound

```
boxed( 0 <= D-D_N <= [r^(N+2)/(1-r)] N242 ),
N242[h]=k(A^-1 h,A^-1 h),
D_N[h]=sum_{j=0}^N M_j[h].
```

The resulting sufficient (not necessary) **actual full-odd signed Schur gate** is

```
boxed( G242 - N242 - D_N - [r^(N+2)/(1-r)] N242 >= 0 ),
G242[h]=a(A^-1 h,A^-1 h)=<h,A^-1h>.
```

This is a matrix inequality over **all** actual selected directions. Neither G242/N242 nor any actual M_j has yet been computed. Critical four-dimensional tests are method-feasibility screens, not full acceptance.

## 3. Paired-moment optimization: two positive solves, not four

Define the *actual* positive exterior responses recursively for each forcing `h`:

```
u_0=H^-1 g,        u_{j+1}=H^-1 L u_j.
```

All these vectors belong to the positive compressed form domain, and the identities are

```
M_(2j)   = a_F(u_j,u_j),
M_(2j+1) = k_F(u_j,u_j).
```

Consequently the four-term complete-source functional is exactly

```
D_3 = a_F(u_0,u_0)+k_F(u_0,u_0)
    + a_F(u_1,u_1)+k_F(u_1,u_1).
```

**Only two positive exterior inverse responses** `u0,u1` are required. This is not a claim that either response is already available or that computing them is easy. The alternative six-term gate adds one response `u2` and its two form quadratics. No full signed exterior inverse is computed.

For a proposed trial `y` of `H^-1 b`, the matched positive form/residual identity (for admissible strong-domain trial y, or its form-dual version) is

```
<b,H^-1b> = 2Re<b,y> - a_F(y,y)
           + <b-Hy,H^-1(b-Hy)>.
```

The final term must be *upper* certified (via a genuinely matched positive reference or an independent residual estimate); ignoring it only yields a Galerkin **lower**, just as in #355. Work on a **fixed few critical forcings first**. Avoid false raw-coordinate overprecision or a 242-column inverse campaign.

## 4. Exact rational tail budgets, archived input custody

`nf362_directional_neumann_gate.py` hashes the downloaded GitHub PR348 native archive and PR350 pruned leakage archive and their expected JSONs, reads exact fractions, and validates the scalar consequences. PR348 has a four-dimensional plane with `|w(f,f)|<=eta a(f,f)`, `eta=2.9552733316649...e-12` under the inherited realization; this **only calibrates** error tolerance, not the actual positive margin.

| Full terms included | Tail versus N242, mu_new (local) | Tail versus N242, mu_old (accepted) |
| --- | --- | --- |
| 1 | 2.81753e-6 | 2.85956e-4 |
| 2 | 4.72539e-9 | 4.79488e-6 |
| 3 | 7.92514e-12 | 8.04000e-8 |
| 4 (**2 positive solves**) | **1.32916e-14** | 1.34814e-9 |
| 5 | 2.22918e-17 | 2.26054e-11 |
| 6 (**3 positive solves**) | 3.73866e-20 | **3.79044e-13** |

All numbers above are rigorous rational **upper coefficients**, not measured Schur corrections. For the four near-critical original vectors, the corresponding energy-dual projections e obey `k(e,e)/a(f,f)<11/10` using Young's inequality with parameter 1/20 and the locally replayed r. Thus the four-term tail is `<1.47e-14 a(f,f)`, i.e. `<0.005 eta a(f,f)`. With only the older accepted mu, Young with parameter 1/5 gives `k(e,e)/a(f,f)<131/100`, so the six-term tail is `<4.97e-13 a(f,f)`, i.e. `<0.2 eta a(f,f)`. These comparisons make no claim of certified positive signed energy. The actual positive margin could be much smaller than eta, so term depth must ultimately be driven by proved signed margins.

An exact-rational 2×2 PSD rank-one negative-operator example with `K=[[1,1/100],[1/100,1/10000]]`, `H_F=1` shows the generic geometric tail constant is attained. The four terms from its paired positive responses were independently recomposed. This no-go on generic constant improvement does **not** preclude actual-specific cancellations.

## 5. Next bounded task and stop

**Next:** On the already accepted four near-critical original functions, construct their A-form-orthogonal projections into `E=A^-1 J242` by a *positive exterior* solve, then test the first directional forcing `g=QK e` and one matched response `u0=H^-1 g`. Audit the physical/source form-domain status and residual certification against the actual original multiplier. Only if the first moment yields tractable certified upper/lower data should a second response `u1`, or eventually a complete J242 finite matrix, be considered.

This proposal is a more specific replacement for NF359's unstructured full form-dual remainder and NF360's impossible uniform scalar inequality. It preserves all 242 selected sources, seven-prime multiplier, true pole, and complete infinite signed complement. It **does not** close original source/domain acceptance, W-ODD-NEG, the even form, the actual global Weil bridge, or RH.

**Repositories:** no GitHub write, PR, manifest update, or promotion. Local report `nf362_directional_neumann_gate.json` and exact Fraction checker `nf362_directional_neumann_gate.py`.
