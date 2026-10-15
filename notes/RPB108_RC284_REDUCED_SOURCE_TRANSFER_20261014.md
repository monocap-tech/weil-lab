# RC284 — paid P0/P1 response bounds for reduced references

Parent RC283: `3651ac3a8f82d8f9357416a61d206dcb8b286232`.
Aperture B=11/10. Original Weil action unchanged.

## New certified calculation

RC278's actual P0 and P1 rational trial vectors have degree at most
64. Each RC283 reduced projection (ranks 301, 317, 334) contains these
vectors. Thus, although the augmented reference and its inverse change,

```
(G_old-G_new) Z = 0,
e_new=D^-1 u-N_new Z=e_old,
<2u,Z>-<Z,G_new Z> = old variational center.
```

The inverse-residual correction changes and MUST be paid again.

Let M_old be RC278's fully paid model residual energy upper bound,
including the infinite output tail. For its first 65 retained
Legendre coefficients c_n, with m_n=2B/(2n+1), establish outward
rational lower and upper bounds on

```
sum(n<=64) m_n (H_n+s) c_n^2
```

using s_lower and s_upper from RC129. Write these Eminus and Eplus.
The remaining old-weighted model energy is at most M_old-Eminus.
For a reduced reference with global floor mu, its model energy is bounded

```
M_new <= Eplus + (M_old-Eminus)/mu.
```

This pays every degree >64 and the infinite tail. It is conservative:
many degrees between 65 and the new projection cutoff actually have
inverse weight 1, but here receive the worst global mu.

Low-mode rounding R is unchanged. RC278's global D-fault norm
delta is charged as delta^2/mu. With eta=1/100, the complete added
inverse residual is bounded by

```
Correction <= (1+eta) M_new + 2(1+1/eta)(R+delta^2/mu).
```

All values, including outward rounding, are exact fractions.
The source response upper bound equals RC278's unchanged variational
center upper plus Correction; the native gate lower is
mass_source - lambda * response_upper.

## Tested candidates

| Total rank | Even P0 gate lower | Odd P1 gate lower |
|---|---:|---:|
| 301 | approximately -1.683 | approximately -7.186 |
| **317** | approximately **-0.09655** | approximately **-0.07969** |
| 334 | approximately -0.04779 | approximately -0.03567 |

These are **negative lower enclosures**, not negative original
operator witnesses, eigenvalues, or proof of a failed positivity
condition. No reduced-reference positive source pivot is yet certified.

The certificate also supplies exact *conditional* Chebyshev
inverse-polynomial degrees for absolute D-operator errors 1e-6 and 1e-12.
These are mathematically certified action budgets, **not executed
full original Weil operator solves**.

## What the obstruction tells us

The coarse transfer deliberately overpays the whole >64 residual
as though it belonged to the difficult omitted high-degree tail.
It is consequently unable to preserve the RC278 positive margins.
This does not mean the new rank-317 reference is a bad choice.

**RC285:** use the already available RC274 degree-resolved actual
residual intervals (65–2048) to charge degrees 65 through the new
projection cutoff with the *exact* retained inverse weights; charge
only true omitted degrees at the weaker weights. Keep RC274's global
faults and complete infinite tail. Then retest the fresh P0/P1 source
gates before expanding the coupled source family.

Rank-317 full gate, Stage I, RH, F4 and Lean remain OPEN.

## Replay

```bash
python scripts/validate_rpb108_rc284_reduced_source_transfer.py --output certificates/rpb108_rc284_reduced_source_transfer.json
python scripts/validate_rpb108_rc284_reduced_source_transfer.py --output certificates/rpb108_rc284_reduced_source_transfer.json --replay
```

Replay checks RC129, RC278, RC283 and note immutable Git blob pins.
Successful replay verifies the stored bound, not an independent
reproof of inherited analytic estimates.
