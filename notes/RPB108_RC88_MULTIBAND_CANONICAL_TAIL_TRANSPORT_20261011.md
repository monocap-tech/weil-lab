# RPB108 RC88 — multiband canonical tail coercivity and source transport

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: `81782de29e80ca01a5d47d137cf5bdaa25bb29dc` (RC87).

## Result

RC88 combines nested Fourier energy bounds across 440 rational frequency
layers instead of retaining only one cutoff. It proves a stronger norm
bound for the same actual rank-38 canonical complement map and propagates
it through the complete original-source certificate. No source or Riesz
trial coefficients change.

| Quantity | Prior | RC88 |
|---|---:|---:|
| Actual head rank; original source inputs; polynomial trial dimension | 38; 22; 64 | 38; 22; 64 |
| Canonical complement embedding norm upper, approximately | 0.723521873569 | 0.715574633375 |
| Canonical energy / physical energy lower, approximately | single-cutoff bound | 1.952945512372 |
| Even actual projected-source relative upper | `2061/4096` | `63/128 = 0.4921875` |
| Odd actual projected-source relative upper | `471/1024` | `1843/4096 = 0.449951171875` |
| Retained maximum relative upper | 0.503173828125 | 0.4921875 |

The certified reduction in the retained scalar upper factor is
`5/229`, approximately **2.183406%**. This compares upper bounds, not
measured leakage. The final source matrix improves the RC82 retained
source matrix in whole Loewner order, verified with exact fractions.
Generation and independent replay: **PASS**.

## Actual complement and nested low-frequency bounds

Use physical aperture half-width `B=11/10`, Fourier convention
`exp(-2*pi*i*xi*x)`, canonical weight `w(xi)=log(e+|xi|)`, and head
rank `m=38`. If `z` lies in the actual canonical Riesz-head complement,
then `f=i z` is physically orthogonal to every polynomial of degree less
than 38, by the Riesz pairing identity. This is a statement about the
actual projection `Pi38`, not a nominal inverse.

Let `D_n=(2n+1)!!`. The RC78 Rodrigues and Parseval argument gives, for
`Z_L=2*pi*B*L` and `Z_L^2/(2m+3)^2<1`,

`integral_{|xi|<=L} |Fourier(f)(xi)|^2 dxi <= theta(L) ||f||_phys^2`,

where

`theta(L) = 4*B*L*Z_L^(2m) / [D_m^2*(1-Z_L^2/(2m+3)^2)]`.

To recall its normalization: the physical squared norm of the orthogonal
Legendre plane-wave remainder is at most
`2B sum_{n>=m}(2n+1)|2*pi*B*xi|^(2n)/D_n^2`. Integrating over `[-L,L]`
cancels the factor `2n+1`. Successive integrated terms have ratio
`Z_L^2/(2n+3)^2`, bounded by its first ratio; the displayed geometric
formula bounds the entire infinite sum. No finite-tail truncation or
numerical sampling is used as proof.

Plancherel separately gives the bound 1 for the low-band energy fraction.
The validator therefore uses `Theta_j=min(1,theta(L_j))`, with `theta`
rounded upward on the `10^-50` rational grid, at `L_j=j/100`.
It stops at the first capped value 1, `L_440=22/5`.

## Layered canonical energy bound

Set `L_0=0`. Choose exact positive lower bounds

`a_j <= log((e+L_j)/(e+L_{j-1}))`.

For every real frequency, the lower staircase satisfies

`w(xi) >= 1 + sum_j a_j 1_{|xi|>L_j}`.

Indeed the completed increments telescope to at most the logarithmic
weight at the last completed cutoff. Multiply by `|Fourier(f)|^2` and
integrate. Every summand is nonnegative, so no cancellation or output
orthogonality is assumed. The nested Fourier bounds imply

`||z||_can^2 >= [1+sum_j a_j(1-Theta_j)] ||i z||_phys^2`.

The exact bracket is the recorded rational number `c_layer`, approximately
`1.9529455123719188`. The canonical norm here is the weighted Fourier
norm of the same physical representative. Consequently

`||i(I-Pi38)||^2 <= 1/c_layer`,

and adjoint duality gives the identical bound for
`B38=(I-Pi38)i*`. An upward rational root ceiling on the `10^-30` grid is

`tau_new = 0.7155746333745389...`.

All 440 cutoffs, cumulative bounds, weight increments and contributions
are stored in the certificate. The last capped term contributes zero;
it does not weaken the positive contributions already accumulated.
This fixed staircase is a certified improvement, not a claim of an
optimal frequency partition or exact complement norm.

For the increment bounds, the ratio `(e+L_j)/(e+L_{j-1})` decreases with
`e`, so an upward enclosure `e_hi` gives a valid lower ratio. The directed
logarithm is then rounded downward on the `10^-40` grid. Independent replay
checks these logarithms with 24 positive atanh-series terms and an exact
geometric tail; their arguments are close enough to 1 for that enclosure
to lie strictly within the saved directed boxes.

## Propagation through the complete actual source

RC82 uses the complete nominal physical source `F_nom`, its degree-less-
than-38 subtraction, the RC81 direct physical Riesz-error Gram `E_phys`,
and the physical source approximation error `delta` from RC68. All of
those physical data remain unchanged.

RC71's subtraction residual physical Gram upper is `W`. Since `B38`
annihilates the subtracted polynomial exactly,

`Gram_can(B38 F_nom) <= tau_new^2 W`.

The old projected arch, prime and parity pole constants, expressed in
units of `sqrt(rho)` with `rho=252/257`, each arose by applying the old
uniform adjoint norm to a physical output or physical polynomial remainder.
RC79 had already propagated that norm through all these terms. Set

`gamma=tau_new/tau_old`.

Multiplying each of these old constants by `gamma` is valid because its
physical bound before applying the adjoint is unchanged. The prime term
receives this replacement of its one old tail factor; no second projection
factor is applied. For the arch and pole terms, the unchanged physical
polynomial output belongs exactly to the actual head and is annihilated
before the adjoint contraction.

Let `k_p` be the sum of the new projected component constants in parity
`p`, and `T=V'DV` the unchanged physical trial Gram. With `nu=1/65536` and
`s_new=tau_new^2/rho`, the transfer covariance divided by `rho` is bounded
by the upward-rounded matrix

`E = (1+nu) D_k E_phys D_k + (1+1/nu)delta^2 s_new T`.

The second term uses the same strengthened adjoint norm on the physical
operator approximation error. Set `E_can=rho E`. Exact PSD checks prove
whole Loewner improvement over RC82's transfer enclosure.

The final actual original-source upper is

`A(t)=(1+t_p)tau_new^2 W+(1+1/t_p)E_can`,

with outward Loewner rounding on the `10^-24` grid. The old RC82 Young
parameters first give a whole-matrix improvement over RC82's retained
source upper. A finite exact nine-parameter search then selects `t=1/4`
for even inputs and `t=5/16` for odd inputs, unchanged from RC82. The final
matrix also passes the whole Loewner improvement check.

The comparisons

`A_even <= (63/128) M22_even`,
`A_odd <= (1843/4096) M22_odd`

use RC67's actual original 22-input canonical Gram lower matrix. Actual
source parity preservation justifies their combination into the retained
maximum factor `63/128`.

## Independent replay and provenance

Replay independently encloses `e` using its rational Taylor series and
geometric tail, and `pi` using Machin's arctangent identity. It checks the
double-factorial identity `(2m+1)!/(2^m*m!)`, reconstructs the integrated
first Legendre term from its physical and frequency normalizations, and
verifies the geometric closure. Its positive atanh logarithm bounds must
fit the saved directed enclosures.

Replay also reconstructs the layer sum through the telescoping staircase
levels and subtraction of cumulative energy fractions. It directly
contracts the 64-mode physical trial Gram using mass sums, rebuilds the
actual source attachment in units of `rho` instead of the generation
formula, and verifies final PSD comparisons after exact native-to-Legendre
congruence. All comparisons use rational arithmetic, and replay requires
equality with the entire saved JSON certificate.

Ten input hashes bind RC87, RC82, RC78, RC79, RC71, RC68, RC67, RC70, RC59
and RC81. The relevant RC87, RC82 and RC79 dependency links, matching tail
constants, fixed physical Riesz error and nominal residual identities are
checked exactly.

```bash
python scripts/validate_rpb108_rc88_multiband_canonical_tail_transport.py --replay certificates/rpb108_rc88_multiband_canonical_tail_transport.json
```

## Remaining scope

The scalar source budget remains open. This result does not establish a
38-input original source covariance, enlarged Weil or complement floor,
actual rank-38 scalar-budget failure, whole-aperture positivity, RH, F4 or
any Lean formalization. Crossing the upper factor 1/2 does not discharge
the required sufficient gate. Further reductions must still control the
particular source residual and transfer or change the positivity criterion.
