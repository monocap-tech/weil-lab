## MG48 independent exact-rational result — VERIFIED (research-level)

[MG48 Actions #39685179933](https://github.com/monocap-tech/weil-lab/actions/runs/39685179933) **PASSED**: main construction and independent ungrouped-polynomial replay of all **864 exact original 24×24 rational residual upper candidate matrices**, including all four final selected exact rational inertia classifications. Accepted artifact `mg48-original-joint-multiplier-864-source-matrices` (ID **12386391118**).

| True original case | MG43 accepted whole-source Gersh lower | MG48 new joint-multiplier Gersh lower | selected complete-source method |
|---|---:|---:|---|
| 16 cells, k12 | **−1.3146427911** | −23.9349003598 | MG43 |
| 16 cells, k16 | **−1.4906207885** | −24.5654207178 | MG43 |
| 32 cells, k12 | **−1.1941733535** | −23.3104401617 | MG43 |
| 32 cells, k16 | **−1.3130469460** | −24.0860150298 | MG43 |

**0 strict source contraction certificates**. MG48 improves on MG47's separate conditioned subtraction by a large amount, and improves MG46's particular measured-plus-omitted construction modestly for the 32-cell cases, but fails to beat MG43's independently proven whole-frequency Loewner upper in every case. The selected conservative lower matrix is unchanged MG43, whose exact negative rational witness disproves positivity of *that lower certificate only*. The original residual and Weil operator have no established negative mode from this result.

**MG49 next frontier:** diagnose matrix-level loss in MG48's positive charges on the actual MG43 witness rays, comparing measured direct, omitted mass, first-moment interval/Young, high-tail, and true pole uncertainty against the MG43 whole-frequency upper. Then target newly certified local multiplier/source covariance on the OMITTED band instead of reblending the old whole G/S moment brackets. Original 470D inverse, signed 51/56, independent Fourier/form/domain, complete even/Weil/CC27/RH remain OPEN.

---

# MG48 — Joint physical multiplier covariance, original complete-frequency 24D source

**Status: accepted exact rational calculation and independent Actions replay, with NO MG43 improvement.**
Stacked on independently verified MG47 PR #296 (final-head Actions #39663431182).
The MG47 accepted complete-source method is MG43 in every scenario. Its
conservative lower matrices have exact negative rational Rayleigh witnesses;
this says nothing about a negative true original Weil operator.

## Algebraic upgrade over MG47

The *same* original positive unpoled multiplier `a(xi)` generates three
physical source matrices on the actual omitted set D = R minus [-4,4]:

```
H_D = integral_D t t^T
G_D = integral_D a t t^T
S_D = integral_D a^2 t t^T.
```

For k=12 or k=16 set `M_k=17+(347/500)*k`. By the accepted SM41
seven-prime/digamma pointwise majorant `a(xi)<=17+log|xi|` on |xi|>=1,
`a(xi)<=M_k` for 4<=|xi|<=2^k. The physical positive multiplier is
globally bounded below by `kappa=KAPPA>0` on D. Thus on this finite
frequency region

```
(a-kappa)(a-M_k) <= 0.
```

The HIGH tail |xi|>2^k is NOT assumed to obey a<=M_k. Instead, since
a>=kappa>0 and M_k>0,

```
(a-kappa)(a-M_k)
  = a^2-(kappa+M_k)*a+kappa*M_k
  <= a^2
```

pointwise. MG24's independently accepted original 24D SM41 high-tail
second moment satisfies `S_{|xi|>2^k} <= tau2_k*I`. Integrating both
pieces yields the genuine complete-original-frequency **joint** Loewner
constraint

```
S_D <= (kappa+M_k)*G_D - kappa*M_k*H_D + tau2_k*I.
```

This uses one SAME multiplier and source, not three separately optimized
unrelated moments. No unmeasured original frequency is dropped.

## Coupled original complete-source residual upper

Let original physical nonscalar response B and the genuine sinh-pole
coefficient b be as in MG43/MG47. For the accepted physical coefficient
center b0, define

```
C0=I+2 e_p b0^T B,
P0=C0-(kappa+M_k)*B/2.
```

The original omitted residual covariance, with the pole at b0, is
`C0^T H_D C0-C0^T G_D B-B^T G_D C0+B^T S_D B`.
The joint inequality converts this to an upper in H_D and G_D:

```
C0^T H_D C0-kappa*M_k B^T H_D B
 -P0^T G_D B-B^T G_D P0+tau2_k B^T B.
```

Retain genuine original physical `Hlo-HCup <= H_D <= Hup-HClo`.
For each one of MG47's independently valid *same-operator*
`L <= G_D <= U`, put `Gc=(L+U)/2` and `E=(U-L)/2 >= 0`.
The MG40 block-PSD covariance/Young lemma bounds the mixed uncertainty:

```
-P0^T (G_D-Gc) B-B^T (G_D-Gc) P0
 <= eta P0^T E P0 + eta^-1 B^T E B
```

for every positive rational eta. Hence the matrix

```
U0=C0^T Hdup C0 - kappa*M_k B^T Hdlo B
     +tau2_k B^T B
     -P0^T Gc B-B^T Gc P0
     +eta P0^T E P0+eta^-1 B^T E B
```

is a true original omitted-frequency Loewner residual upper *before
pole coefficient uncertainty*. Keep MG46's verified isotropic or sourcewise
diagonal PSD `W` and any `gamma>0`:

```
U_D=(1+gamma) U0+(1+gamma^-1) W.
```

Add the original MG32 actual [0,4] complete 24D direct upper ONCE:
`U_complete=U_C+U_D`. This is a valid simultaneous original complete
24D residual upper, independent of the MG43 whole-source upper.

## Exact acceptance gate

The producer enumerates 3 valid MG47 first-moment lower profiles x
3 upper profiles x 4 rational mixed eta x 3 gamma x 2 valid pole
uncertainties = **216 complete original rational 24x24 matrices**
per case, **864** over meshes 16/32 and k=12/16.
No independently bounded S profile is substituted for the joint constraint.

The separate independent verifier rederives the core using the
**ungrouped original G polynomial**, checks every one of the 864
candidate signed Gersh margins and traces and exact selected full
24x24 matrix, then independently verifies exact rational LDL positivity
or a negative rational Rayleigh vector. Selection compares whole-source
MG43 versus whole-source MG48 on the exact sufficient Gersh margin; a
negative conservative lower certificate is never physical negativity.
No alleged matrix minimum is taken; no source-ray upper is promoted to
a simultaneous Loewner result.

**Verified computational conclusion:** all 864 exact rational matrices and their independent audit passed. MG43 remains selected in all four cases. No 24D contraction. Even a positive original 24D source
certificate would NOT establish the original 470D inverse, signed
odd 51/56 cap, independent Fourier/form/domain, even/Weil/CC27 or RH.
All these obligations remain OPEN.
