# MG24 — Complete-original-frequency coupled 24-source matrix enclosures

October 19–20, 2026. Stacked on [MG23 #272](https://github.com/monocap-tech/weil-lab/pull/272), which passed its exact-rational complete-frequency physical-metric scalar source gate. The canonical active obstruction **W-ODD-NEG stays OPEN**. This is not an RH result.

## What changed

MG19 proved rational **selected-frequency** coupled first/second source moment Loewner bounds for the SAME 24 true odd source channels: 23 double-boundary-adapted supported SI10 generators plus the original odd sinh pole `s`. Those 24 nonflat cells are not the full Fourier spectrum. MG23 proved a coarse **complete-frequency** strong-action upper, retaining the actual physical Gram geometry. MG24 combines these two already verified forms of evidence into explicit full-frequency matrix brackets for the first and second source moments, then pays the original rank-one pole cross terms.

Use the exact common physical basis `F=[h_0,...,h_22,s]`, its full Gram `H=F*F>0`, `b=F*s=H e_23`, `sigma=<s,s>`, and full original source moment matrices

```
Go = F* Ao F,    So = (Ao F)*(Ao F),   c = Go e_23 = F*Ao s.
Gstar = Go - 2bb*
Sstar = So - 2(cb*+bc*) + 4sigma bb*.
```

All these are **true complete ORIGINAL operator expressions**. The actual numeric `Go`, `So`, `c`, `Gstar`, `Sstar` remain unknown exactly; MG24 computes rigorous finite matrix Loewner brackets containing them.

## Complete original frequency accounting

Let `L_1` and `L_2` be the real exact MG19 24×24 selected-frequency first- and second-moment **lower-reference** matrices (the relative weight policy, with all sourcewise Taylor/multiplier errors paid). Fourier source moments from omitted frequencies are positive semidefinite, so

```
L_1 <= Go,   L_2 <= So.
```

Crucially the lower-reference inertias are NOT the inertia of the true source operators and are not accepted as spectral negatives.

On all frequencies `|xi|<=Lambda=2^k`, the original multiplier obeys `0<ao(xi)<=M_k=17+k(347/500)`. Each original physical 25 source transform has the proven SM41 pointwise `|T_i(xi)|<=u_i/|xi|` for sufficiently large `|xi|` with sin `u=1/2`, xcos `u=7/10`, sinh pole `u=2/5`. After the MG11 exact double-boundary transform, the coefficient bound on each genuine `h_i=f_i-a_i s-c_i f_pivot` is paid by `u'_i<=u_i+|a_i|u_s+|c_i|u_pivot`, preserving the original pole channel. Let `E=sum (u'_i)^2`.

The ENTIRE WHOLE-REAL original high-frequency first and second moments are then bounded by rational scalar tails

```
tau_1(k) = 2 E (M_k+1)/2^k
tau_2(k) = 2 E (M_k²+2M_k+2)/2^k
```

and the full positive source matrices obey

```
Go <= M_k H + tau_1 I
So <= M_k² H + tau_2 I.
```

For actual interval original physical Gram `H`, construct exact rational center `H0` and row-radius `e_H` so `H0-e_H I <= H <= H0+e_H I`. Complete upper matrices are

```
U_1 = M_k H0 + (M_k e_H + tau_1) I
U_2 = M_k² H0 + (M_k² e_H + tau_2) I.
```

Therefore full source moments satisfy the genuine coupled Loewner sandwiches `L_1<=Go<=U_1` and `L_2<=So<=U_2`, on the same physical basis with no frequency omitted without payment.

## Certify the nonlocal pole response from the source moment sandwich

This step is essential, because the signed `Sstar` mixed terms cannot be dropped.

Set `D=U_1-L_1>=0`. The actual pole response vector `c=Go e_23` is constrained by BOTH source-matrix inequalities. In particular, the PSD operator interval implies

```
c_i = (L_1+U_1)_{i,23}/2 +/- (sqrt(D_ii D_23,23))/2.
```

Use exact integer-square-root outward rational enclosures for each half-width, not floating eigenvalues. Combine `c` with the original interval pole vector `b=H e_23` and `sigma=H_23,23`. Compute the exact midpoint of

```
T = -2(cb*+bc*) +4sigma bb*
```

and bound every original interval-product error. A symmetric row-sum diagonal charge converts entrywise interval errors into a **true matrix Loewner bound**.

Finally obtain complete true original pole-corrected **24×24** Loewner brackets

```
L_Gstar <= Gstar <= U_Gstar
L_Sstar <= Sstar <= U_Sstar.
```

This is stronger in *scope* than MG19's selected-frequency source moments or MG23's symbolic pole Young envelope. It does NOT automatically provide a good quantitative positive margin; the interval width may destroy spectral usefulness.

For a real scalar `t>0`, the true physical strong one-step source residual `R=F-t Astar F` obeys

```
R*R <= (H0 +e_H I) -2t L_Gstar +t² U_Sstar.
```

A check of the matrix margin is a separate **strict acceptance gate**, not a conclusion inferred merely from having an enclosure. The independent original Fourier/form/domain premises are inherited, not formalized here.

## Acceptance and nonclaims

The MG24 validator reconstructs MG19 real certified source moments on original nonflat panels, the full 25D physical interval Gram, its true 23D double-boundary transform, and the original sinh pole. It produces all 24×24 source/pole/full-residual rational matrices for dyadic cutoff powers 12,16,20 and independent exact Fraction regression plus explicit full470 no-promotion checks. Export all strictly positive gaps as rational fractions, not 1e-12 rounded decimals.

Even if the *finite* coupled source residual becomes contractive, the 24-source frame is NOT invariant under `I-t Astar`; a Neumann inverse on the full Hilbert space does NOT follow. No original 470-source trial map `J,Y`, signed 51/56 negative cap, complete original odd/even/Weil/CC27/RH is certified. The full true source matrices are bracketed rather than calculated to sharp numerical accuracy. The next method test is whether these brackets are viable enough to support a block-adaptive 470D trial instead of adding more selected windows.

**MG24 verification: PENDING calculation-bearing and independent GitHub Actions.**
