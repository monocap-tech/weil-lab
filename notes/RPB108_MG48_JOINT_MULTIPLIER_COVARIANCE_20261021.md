# MG48 — Joint physical multiplier covariance, original complete-frequency 24D source

**Status: proposed exact-rational calculation; NOT independently accepted until CI finishes.**
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

**Until computation AND independent CI both pass:** all numerical
margins, any claimed improvements over MG43, and the new 24D
contraction gate are UNVERIFIED. Even a positive original 24D source
certificate would NOT establish the original 470D inverse, signed
odd 51/56 cap, independent Fourier/form/domain, even/Weil/CC27 or RH.
All these obligations remain OPEN.
