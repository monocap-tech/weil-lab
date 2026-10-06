# RPB-108: uniform 84-moment complement through 19/20 and panel reordering

Date: 2026-10-06 UTC. Parent: `a2db64ae7ac70b3070c6397b0d0c6e3eaf0e8b24`.
Branch: `research/rpb108-larger-aperture-complement`.
Definitions: [larger complement and panel registry](../docs/TERMINOLOGY_RPB108_COMPLEMENT_095_PANELS.md).

## Actual result and scope

For every 1/2<=a<=19/20, the actual supported form-domain complement to
physical Legendre degrees 0 through 83 satisfies

```
Q(h) >= (17/50) ||h||_2^2,
Q(h) >= (9/100) Elog(h).
```

These are complement bounds. The finite 84-dimensional component and its
coupling are not covered by this pass. The whole-domain positivity frontier
remains 81/100, with its previously certified physical bound 10^(-20)
and logarithmic bound 4*10^(-23).

The new physical cutoff is 103/10; the logarithmic cutoff remains 19/2.
The exact physical lower expression exceeds 0.352214495495532 and is
rounded down to 17/50. The exact logarithmic expression exceeds
0.099999996939316 and is rounded down to 9/100. Decimal displays do not
enter certification. The physical complement inverse factor is 50/17.

## Certified operator geometry

At the upper aperture A=19/20, rational intervals verify

```
log(5) < 2A < log(7),
A < log(3), 2A < 2log(3), 2A < 3log(2),
0 < 2A-log(5) < min(log(5)-log(3), 2log(3)-log(5)).
```

The active prime powers at that endpoint are exactly 2,3,4,5.
Prime 4 retains amplitude log(2)/2; prime 5 has log(5)/sqrt(5).
The existing joint prime-2/4 three-vertex estimate and prime-3/5
four-vertex estimate therefore remain valid. The latter has chain
edge amplitudes A3,A5,A3 and norm upper bound
(A5+sqrt(A5^2+4A3^2))/2, rounded outward.
Independent exact 4x4 positive pivot checks pass for both signed
adjacency bounds. A verified trial rejects a bound smaller by 10^(-6).

The [original prime-5 complement proof](REFLECTED_PACKET_BRIDGE_108_PRIME5_84_081_20261005.md)
uses these same geometric hypotheses. They are rechecked at 19/20.
Compression to a smaller support cannot increase either translation
operator norm; before prime-5 activation its overlap is empty.
Thus the endpoint translation loss bounds hold throughout the stated
interval.

## Uniform analytic estimates

The quarter-line archimedean estimates are unchanged:

```
m0(t) >= log|t|-7/(216 t^2), |t|>=1,
m0(t) > -27/5 globally.
```

Let J be the sum of the joint prime bounds and
cT=log(T)-7/(216 T^2). The actual 84-moment low-band estimate rho84(T)
and pole estimate p84 give the physical complement lower expression

```
cT-(27/5+cT)*rho84(T)-p84-J.
```

At A=19/20 and T=103/10 it exceeds 17/50. The geometric majorant's
ratio is strictly below one. The moment and pole estimates increase
with support aperture, so the same lower bound holds for every smaller
window in the interval, on that window's matching moment complement.

The independent logarithmic cutoff 19/2 gives a strictly positive
high-symbol gap after the prime loss, and

```
1/10-(27/5+J+3/10)*rho84(19/2)-p84 > 9/100.
```

The script retains the original archimedean-floor and pole checks,
and re-evaluates every load-bearing rational quantity at the new
upper aperture. It does not alter the archived 81/100 calculation.

## Source panel change

Put ell_n=log(n)/(2a). The complete activation boundaries are
0,1 and ell_n,1-ell_n for n=2,3,4,5. At a=log(6)/2,
ell_2=1-ell_3 and ell_3=1-ell_2. No prime 6 term is activated:
Lambda(6)=0. The ordering changes because two existing source
translation boundaries cross.

Rational checks at 81/100, 41/50 and 89/100 recover the old order.
Checks at 9/10 and 19/20 recover the new order.
The crossing is strictly between 89/100 and 9/10.

At 19/20, the actual panels are:

| t interval | Active translations |
| --- | --- |
| (0,1-ell_5) | +2,+3,+4,+5 |
| (1-ell_5,1-ell_4) | +2,+3,+4 |
| (1-ell_4,ell_2) | +2,+3 |
| (ell_2,1-ell_3) | +2,+3,-2 |
| (1-ell_3,ell_3) | +2,-2 |
| (ell_3,1-ell_2) | +2,-2,-3 |
| (1-ell_2,ell_4) | -2,-3 |
| (ell_4,ell_5) | -2,-3,-4 |
| (ell_5,1) | -2,-3,-4,-5 |

For each panel the checker encloses a rational interior point and
certifies every translated point as inside or outside (0,1).
Those checks determine the entire open panel: every possible indicator
transition is among the sorted boundaries, so no translation indicator
can change within the panel. Boundary points have measure zero for
these source operators.

The old fourth and sixth panel patterns are rejected at 19/20.
This is a complete activation-geometry check, not a construction of
the new source polynomial enclosures.

## Reproduction and next obligation

The complement and panel certificates each reproduce byte for byte:

```sh
python scripts/certify_native_prime5_complement84_095.py > /tmp/complement-095.json
cmp /tmp/complement-095.json notes/data/RPB108_PRIME5_COMPLEMENT84_095_20261006.json
python scripts/certify_native_prime5_geometry_095.py --output /tmp/geometry-095.json
cmp /tmp/geometry-095.json notes/data/RPB108_PRIME5_GEOMETRY_095_20261006.json
```

The 84-coordinate native and source constructors still whitelist their
archived apertures; their degree-83 case is currently tied to 81/100.
No whitelist is bypassed and no larger-aperture matrix or source run
is reported here. Extending them requires checked truncation bounds,
normalization and the correct panel layout, then a matching complete
Gram and corrected Schur sign.

A next target 41/50 remains below the panel crossing and can retain the
old nine-panel order. The larger uniform complement is available, but
a sharper target-specific complement factor may be needed for the
sufficient Schur estimator.

Historical notes are unchanged. Global endpoint exclusion, historical
fixed packet attachment, F4 and FULL TRANSPORT CLOSED remain open.
No Lean or workflow edits; no CI run requested.
