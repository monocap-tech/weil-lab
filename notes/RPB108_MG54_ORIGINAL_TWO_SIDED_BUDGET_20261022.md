# MG54 — Two-sided original source budget / joint-method necessity

**Status: new fixed-response structural diagnostic implemented; independent exact-rational CI PENDING.** Parent MG53 [Actions #39886275002](https://github.com/monocap-tech/weil-lab/actions/runs/39886275002) independently established four-case original source direct-only no-go within the **fixed MG52 nonscalar B and complete remaining-frequency upper**.

## New question, not answered by MG53

MG53 proves that even hypothetically zeroing both original measured-frequency direct residual uppers, the **fixed remaining-frequency** upper alone leaves a negative original source-lower witness. However, that does NOT mean replacing only the remaining-frequency upper can close the gate. MG54 tests the converse.

The original complete-frequency accepted MG52 upper, on the same genuine 25 SI10 physical sources, MG11 23 two-boundary-adapted + true odd sinh pole 24D, is

```
U52 = D + R,
D = U_original_real_band_[0,4] + U_original_real_band_[4,8],
R = U_original_real_frequencies_|xi|>8.
```

`D` and `R` are each mathematically valid original full 24×24 upper bounds for original physical positive semidefinite covariance `int R*R` on their **respective** real frequency sets, so BOTH `D>=0` and `R>=0` in exact Loewner order. MG54 checks this by an independent 24×24 exact rational LDL elimination, not by floating eigenvalues. Every physical true sinh pole and high-frequency multiplier tail is still paid in the original accepted U52.

For the previously independently fixed MG43 negative exact rational conservative-source test vector v (not a true physical eigenmode), define

```
h = v^T Hlo v,
d = v^T D v,
r = v^T R v.
```

If `h<d`, even replacing R hypothetically by the ZERO PSD matrix (which is **NOT a valid upper for the real remaining-frequency covariance**) cannot make the remaining original source lower `Hlo-D` positive definite. Since **any legitimate alternative full remaining-frequency covariance upper must be PSD**, refining only R with this accepted original B/D cannot repair the original 24D source contraction.

MG53 independently already established `h<r`, which symmetrically rules out refining only D with this fixed R/B. Together, if **both** inequalities `h<d` and `h<r` hold on exact rational rays for all four source scenarios, this proves a new **TWO-SIDED fixed-architecture obstruction**.

## Quantitative necessary 2D budget frontier

For diagnostic scaling parameters `alpha,beta in [0,1]`, consider the **COUNTERFACTUAL ONLY** matrix

```
U_counterfactual(alpha,beta) = alpha*D + beta*R.
```

This is not independently proved to bound the physical original operator unless both complete physical PSD contributions remain rigorously covered. Scaling physical upper matrices arbitrarily downward is NOT allowed as a certificate.

Necessary nonnegativity on the archived exact original source ray is merely

```
alpha*d + beta*r <= h.
```

This defines a line in a two-dimensional parameter plane. MG54 exports the exact rational intercepts `h/d`, `h/r` and symmetric scaling threshold `h/(d+r)` and proves no version that improves only one component can cross the necessary source positivity gate for the accepted fixed B.

**A ray constraint is necessary, NOT sufficient for an original full 24×24 strict positive-definite lower.** The exact full24 hypothetical zero-remaining and zero-direct matrix signs are checked with genuine rational negative Rayleigh witnesses.

## Research decision

Should the independent verifier pass and certify both `h<d` and `h<r` in all cases, neither improving only measured direct source integration nor only the archived omitted frequency envelope can ever fix the current fixed-B, additive architecture.

**MG55 next frontier:** change the original nonscalar response B or replace the additive independent source-bound architecture with a *simultaneously coupled whole-frequency covariance/response representation*. An actual improvement must still construct a new rigorous complete-original (24\times24) Loewner upper, compare against MG43, and pass independent exact sign verification. This result cannot prohibit another source basis/response architecture or prove any true signed Weil operator negative direction.

No original 24D contraction, original 470D inverse, signed 51/56 odd cap, independent Fourier/form/domain, even/Weil/CC27/RH. All OPEN.
