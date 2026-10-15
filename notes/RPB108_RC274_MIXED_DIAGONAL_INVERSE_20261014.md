# RPB108 — RC274: an odd projection-source gate passes

Parent RC273: `a95e332f9ab0a36950bb398591b08570581a868f`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC274 certifies a **positive odd auxiliary-source gate** for P1 under RC271's
rank-608 diagonal projection reference. Its native gate lower bound exceeds
0.00106755727855. The even P0 gate improves but remains unresolved. This is one
entry of the new auxiliary gate, not positivity of its full matrix or a new
original-operator spectral census. Stage I, RH, F4 and Lean remain open.

| Paid quantity, approximately | Even P0 | Odd P1 |
|---|---:|---:|
| RC273 added inverse correction | 0.000391192576444 | 0.000226846570231 |
| RC274 added inverse correction | 0.000267340430606 | 0.000138910903095 |
| Actual inverse response upper | 0.106243289395 | 0.0337851447885 |
| Native auxiliary gate lower | -0.00161595456977 | **0.00106755727855** |
| Native auxiliary gate upper, preserved | 0.00392398083404 | 0.00407833914453 |

Every accepted value is stored as an exact fraction. The even interval still
contains zero; no negative even gate is proved. The reference operator, source
pair, exact four-trial coefficients and inverse variational centers remain fixed.
The legacy rank-639 rational reference and both of its positive signed pivots are
preserved as separate results.

## Resolve the two remaining native-trial tails

RC273 treated A=y0 P_b+y3 R_b explicitly through output degree 2048 and left
B=y1 P_(b+2)+y2 P_(b+4) inside the complete global column faults. B has degree at
most five. RC274 applies the same exact segment and Green-boundary construction
to B. It verifies that its rational prime parameters are identical to the primary
model's parameters, so their finite model coefficient intervals can be added by
linearity. All seven prime pairs and their input cross terms remain present.

For degrees 65 through 128, the old residual had no modeled output for these
native-trial columns. The new residual physical numerator is enclosed as

\[
 (H_n+s)c_n-[hB+K_{prime,model}B]_n,
\]

where c_n is RC272's preserved D-coordinate center. Both endpoints for s and the
fresh prime coefficient interval are used before taking the squared absolute
bound. This retains cancellation with the old low center. Below degree 65 the
old center and source-diagonal rounding allowance are unchanged.

Above degree 128 the complete physical numerator is the sum of RC273's primary
endpoint/prime interval and the new secondary interval. For the infinite prime
tail, a safe norm triangle combines the two separate certified remaining physical
energies after degree 2048. The endpoint tail is recomputed on the full exact
trial Z=A+B, preserving its signed input moments.

The two old complete native-trial fault terms are replaced by their finite and
global arithmetic components, their regular polynomial tail after degree 64,
and the fresh high prime parameter error. The removed terms are exactly the
known additive contributions in RC273's constructed fault budget; this is not
generic subtraction of one error upper bound from another. The original regular
and pole arithmetic faults are conservatively paid twice across low/high models.
The new model omits no endpoint, prime, regular or signed-pole term without a
corresponding bound.

The remaining complete global D-fault norm is approximately 5.65e-9 even and
5.47e-9 odd, compared with RC273's approximately 6.33e-5 and 9.19e-5. The former
large allowances mainly paid unresolved output, rather than uncertainty in the
original arithmetic coefficients. Resolving that output does not make it zero:
its inverse-weighted energy now belongs explicitly to the model bound.

## A fresh global lower form from the original operator

RC231's whole-domain original identity is

\[
 G_0=D+h-rI-K_{reg}+K_{prime}+K_{pole},
 \qquad r=789/125,
 \quad h(x)=-\tfrac12\log(1-(x/B)^2)\succeq0.
\]

The endpoint nonnegativity is RC121's global form theorem, not an entrywise
positivity inference. Let k be RC112's physical negative prime/pole allowance on
the given parity. If ||K_reg||<=c_reg, then

\[
 G_0\succeq D-CI_2,\qquad C=r+c_{reg}+k.
\]

RC274 obtains a sharper c_reg from the pinned degree-192 regular kernel polynomial.
On [0,2B], its exact Bernstein coefficients are all positive and strictly
decreasing. The Bernstein basis is nonnegative and partitions unity; its derivative
coefficients are the adjacent differences. Thus the model kernel is nonnegative
and decreasing on the entire interval, rather than merely at sample points.

For this symmetric convolution kernel on [-B,B], the Schur row integral is
largest at the center: differentiating its row integral at x>=0 gives
r_model(B+x)-r_model(B-x)<=0. Therefore

\[
 \|K_{reg}\|\le
 2\int_0^B r_{192}(t)\,dt+2B\epsilon_{reg}
 <0.499426812435.
\]

The integral is evaluated exactly and the actual uniform polynomial approximation
fault is added. All 193 exact Bernstein coefficients are recorded, so this is a
global polynomial enclosure, not a sampled monotonicity claim. The resulting
physical allowances C are approximately 10.91457512877 even and 11.38587006902 odd.

For the unchanged projection reference this gives a second global D-energy bound:

\[
 N_P\succeq I_D-C D^{-1}+\lambda D^{-1}P.
\]

It can be negative immediately outside the retained projection and cannot be
inverted there by itself. It becomes stronger at higher degrees as H_n grows.

## Mix global lower forms before inversion

The first lower form remains RC272's projection-aware Young bound,

\[
 N_P\succeq dI_D+\kappa D^{-1}P,\quad
 d=a[\gamma-p(1+\theta^{-1})\delta^2]>0,
 \quad\kappa=\lambda-p(1+\theta)>0.
\]

For a single global 0<=t<=1, take their convex combination. On retained degrees a
safe diagonal lower endpoint is

\[
 b_n=(1-t)d+t+
 \frac{(1-t)\kappa+t(\lambda-C)}{H_n+s_{hi}}.
\]

On omitted degrees it is

\[
 b_n=(1-t)d+t\left(1-\frac{C}{H_n+s_{lo}}\right).
\]

The validator checks lambda>C. If n0 is the first omitted matching degree, put
q0=1-C/(H_n0+s_lo)<0. The safe mixing limit is d/(d-q0). Candidate t values are
fractions j/20, j=0,...,18, of a downward-rounded limit. The global mixed floor
(1-t)d+t*q0 is checked strictly positive. Retained degrees have a larger bound,
and the omitted diagonal increases with degree.

This is one convex combination valid simultaneously on the whole parity carrier.
The script does not take an entrywise maximum of two operator lower bounds; that
step is invalid in general and an exact matrix counterexample is checked. No
commutation of the actual reference with these diagonal majorants is assumed.

Inverse order gives N_P^-1<=diag(b_n^-1) in the D metric. The resolved residual
model is weighted with these diagonal upper bounds. The infinite model tail uses
b_n at the first omitted degree after 2048, which is stronger than the global
mixed floor. The remaining global fault norm still uses the global floor.

The finite theta proposals include 0.3,...,0.9, 0.99, the previous selected theta,
and the exploratory proposals 0.77 even and 0.61 odd. Every candidate is accepted
only by exact arithmetic. The selection is not an optimality assertion over all
parameters or all possible inverse estimates.

| Selected mixed bound, approximately | Even | Odd |
|---|---:|---:|
| Young theta | 0.76 | 0.60 |
| Global convex weight t | 0.0160074383125 | 0.0145555523838 |
| Fraction of safe mixing limit | 0.45 | 0.40 |
| Global mixed D floor | 0.000727221151462 | 0.000810031698286 |
| Complete weighted model energy | 0.000267333577206 | 0.000138906369687 |
| Infinite model tail contribution | 0.0000319814092963 | 0.0000420448465064 |

## Paid response and evidence boundary

Let V be the complete resolved and infinite model energy in this diagonal inverse
majorant, R_s the source-diagonal uncertainty and epsilon the remaining global
D-fault norm. The added inverse correction is bounded by

\[
 C_{inv}=\left[\sqrt V+\sqrt{R_s}
       +\sqrt{\epsilon^2/b_{global}}\right]^2.
\]

It is added to the unchanged variational inverse response center. The actual
response upper is intersected with the prior upper bound. For source P_b the
native auxiliary gate is mass(b)-lambda*T_b. The odd lower endpoint is strictly
positive; the even lower endpoint is not. Both upper endpoints remain positive,
so neither calculation establishes a negative direction.

A positive entry of Mass-lambda*T does not certify the complete odd block, its
cross-source pairings, or the entire rank-608 matrix. Nor can this new entry be
subtracted from the independent 582-dimensional nonpositive-index ceiling.
The legacy signed pivots concern different sources and a different reference.
Those results are retained without transferring their numerical margins.

## Reproduction

```bash
python scripts/validate_rpb108_rc274_mixed_diagonal_inverse.py \
  --output certificates/rpb108_rc274_mixed_diagonal_inverse.json
python scripts/validate_rpb108_rc274_mixed_diagonal_inverse.py \
  --output certificates/rpb108_rc274_mixed_diagonal_inverse.json --replay
```

All 257 inherited blob pins are verified. Replay uses the higher-precision prime
boundary recurrence and static intervals, reverses dependency and accumulation
order, regenerates the Bernstein bounds, and compares the entire certificate
exactly. Direct prime-output integration checks the first new degree; exact matrix
controls check global convex mixing and the failure of entrywise maximization.
These are analytic and exact-arithmetic certificates, not Lean formalization.

Next: strengthen the even projection-source response or extend the auxiliary
cross-response matrix with all inverse covariance payments. The inherited original
below-0.01 count ceiling 608, nonpositive ceiling 582 and separate eight-source
inverse width 485647/1000000 remain unchanged. No Stage I or global closure is
claimed.
