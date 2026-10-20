# MG40 — Original nonscalar 24D complete-spectrum source uncertainty

October 20, 2026. Stacked on [MG39 PR #288](https://github.com/monocap-tech/weil-lab/pull/288), which independently certified 64 exact rational interval witnesses excluding *all* t>=0 scalar source responses for *every convex MG24/MG29 source-moment interpolation* at the accepted original 16/32-cell k12/16 cutoffs. This is a method no-go, not an actual Weil spectral no-go.

## Structural advance: directional rather than isotropic nonscalar G uncertainty

Preserve the original SI10 25 physical generators, MG11 23 boundary-adapted sources, the actual odd sinh pole, all original signed seven-prime/digamma Fourier multiplier terms and full original frequency tails. The exact original source map F and original action Astar satisfy

`R=F-Astar F B,` `R*R=H-GB-B^T G+B^T S B.`

Independently accepted MG29 original `LG<=G<=UG`, `S<=US` and original physical `Hlo<=H<=Hup` allow `B=tI+D`. MG30 bounded its nonscalar mixed first-moment uncertainty using a scalar fee:

```
 U_old=Hup-2tLG-GcD-D^T Gc+B^T US B +2||E|| ||D|| I
 Gc=(LG+UG)/2, E=(UG-LG)/2.
```

**MG40 proves a new complete original source matrix bound.** Since `-E<=Delta=G-Gc<=E` and `E>=0`, the block matrix `[[E,Delta],[Delta,E]]` is PSD by an orthogonal congruence to `diag(E+Delta,E-Delta)`. By its Cauchy–Schwarz inequality, for every real source vector x,

```
  |x^T Delta D x| <= sqrt((x^T E x) ((Dx)^T E (Dx))).
```

Therefore, for any rational `eta>0`, the whole symmetric matrix inequality is rigorously valid:

```
 -(Delta D+D^T Delta)
    <= eta E + eta^-1 D^T E D.
```

The new original true coupled pole-including matrix upper is

```
 U_eta=Hup-2tLG-GcD-D^T Gc+B^T US B
       + eta E + eta^-1 D^T E D.
```

Unlike MG30's isotropic scalar uncertainty fee, the MG40 upper retains **the actual direction of the source residual response matrix D and the original first-moment error E**. This is independently proved through the block-PSD identity; no unverified operator commutation or entrywise interval 'join' is involved.

## Concrete original acceptance

Use pinned successful original MG24 Actions #39378465438, MG29 Actions #39440914565 and MG30 Actions #39442984941. Exactly re-evaluate the same original 9 deterministic scalar/nonscalar B trials per mesh/cutoff, with 16/32 cells and k12/16. For each nonzero D test rational `eta = 1/64,1/16,1/4,1/2,1,2,4,16,64`; retain the previously accepted MG30 upper as a guaranteed valid fallback. Choose the stronger **exact Gershgorin lower margin** of `Hlo-U`, not the lowest trace; trace and positive-definiteness need not correlate.

Independent calculation-bearing CI replays **every selected original 24D matrix** and all tested 9 eta alternatives from archived original G/S/H moments in exact Fraction, checks positivity of E and US, reproduces MG30 accepted old margins, and tests any source positivity by an actual strict full 24x24 Gershgorin margin. The four best nonscalar original full matrices Hlo−U are exported and independently reconstituted, with the original physical pole retained inside G and S.

If matrix-valued fees improve margins without making them strictly positive, MG40 still yields a useful method refinement and reveals the remaining source-moment uncertainty. If no improvement, it is a precise tested-eta no-go, not a universal nonscalar impossibility.

**No finite 24D source certificate proves source invariance, the full 470D strong inverse, signed 51/56 cap, independent original Fourier/form/domain, complete even/Weil/CC27/RH or RH. All remain OPEN until separately accepted.**

**CI acceptance pending.**
