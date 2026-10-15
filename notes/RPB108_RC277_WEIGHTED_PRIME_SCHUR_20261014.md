# RPB108 — RC277: actual weighted prime bound and smaller original index bounds

Parent RC276: `3aae55dbc98a3ab3aaf8ba6c249a0449aae3fb67`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC277 proves a global physical L2 norm bound of **3013/1000** for the complete
actual prime operator. The bound retains all seven active prime powers and
their actual translations. It implies new bounds for the original canonical
operator: nonpositive index, including nullity, at most **301**, and index at
or below 0.01 at most **371**. The inherited lower bound of 10 below 0.01 is
preserved. The earlier upper bounds were 582 and 608, respectively.

These bounds follow directly from a global diagonal lower form and moment
codimension. They do not require solving the existing 606-dimensional auxiliary
Schur problem, which remains open. The rank-608 projection reference, its two
positive auxiliary pivots, and the legacy rank-639 reference are unchanged.
Stage I, RH, F4 and Lean remain open.

## A weight for all actual prime translations

Let T=-Kprime on physical L2([-B,B]), with zero extension outside the interval:

\[
 (Tf)(x)=\sum_{n\in\{2,3,4,5,7,8,9\}}c_n
     [\widetilde f(x+\ell_n)+\widetilde f(x-\ell_n)],
 \quad \ell_n=\log n,\quad c_n=\log p/\sqrt n.
\]

Completeness of this active prime-power list and the rational enclosures of
ell_n and c_n are inherited from the pinned RC43 certificate. T is bounded,
selfadjoint and positivity preserving. Choose the positive even weight

\[
 \phi(x)=1+\frac3{10}(x/B)^2,\qquad 1\le\phi\le13/10.
\]

The validator proves pointwise on the whole interval that

\[
 \boxed{T\phi\le\frac{3013}{1000}\phi.}
\]

Here T acts on the zero extension of phi too. Weighted Schur then gives
||T||<=3013/1000 and Kprime>=-(3013/1000)I on the entire physical space,
hence on both parity spaces. For completeness, each symmetric translation
edge uses

\[
 2|u||v|\le |u|^2\frac{\phi(y)}{\phi(x)}
                  +|v|^2\frac{\phi(x)}{\phi(y)}.
\]

Integrating the paired edges gives |<f,Tf>|<=integral |f|^2 Tphi/phi.
There is no finite-section restriction or prime-tail omission.

## Exact support cells and quadratic certificates

For x>=0, the plus shift is active when x<=B-ell, and the minus shift when
x>=ell-B. For every RC43 translation enclosure [el,eh], split [0,B] at all
in-range rational points B-el, B-eh, el-B and eh-B. The resulting 16 knots
give 15 open cell interiors. Every one of the 16 knot points is also certified
separately, giving 31 region certificates in total.

On an open interior (l,r), a plus shift can be active only if l+el<B;
a minus shift can be active only if r>el-B. On singleton knots these tests
use <= and >=. This distinction prevents a shift active only at a cell's
endpoint from being charged across the whole neighboring long cell. The
uncertainty strips conservatively include every potentially active shift.
Reflection covers x<0.

Write a=3/10 and [cl,ch] for a coefficient enclosure. For each potentially
active orientation, the numerator polynomial has coefficientwise upper bounds

\[
 b_0=c_h(1+a e_h^2/B^2),\quad b_2=a c_h/B^2,
\]

\[
 b_1=2a c_h e_h/B^2\quad(\text{plus}),\qquad
 b_1=-2a c_l e_l/B^2\quad(\text{minus}).
\]

These are pointwise upper bounds because x>=0. A potentially inactive term is
still safely overestimated: its upper polynomial is positive, since it is
at least the positive actual shifted weight times its coefficient. Actual
translations remain interval parameters throughout; they are never replaced
by rational-model translation operators.

Subtract the summed upper polynomial from k phi, k=3013/1000. The validator
checks the exact rational minimum of this quadratic on each closed cell or
singleton. It checks both endpoints and every interior convex vertex. All
minima are strictly positive; the least is approximately 0.0011789427561.
Closed-cell checks for a chosen interior activation set bound its full
interior; the separate singleton checks cover any additional knot activations.

## Transfer to the original canonical operator

Use the exact original common-form identity from RC231,

\[
 G_0=D+h-(789/125)I-K_{reg}+K_{prime}+K_{pole},\qquad h\ge0,
\]

and RC121's global canonical metric inequality L<=2D. The pinned RC274 regular
bound is 0.49942681243419112635... . The even pole term is positive; the odd
negative pole allowance from RC42 is
2||sinh(x/2)||_2^2<=1885179761/4000000000. Therefore

\[
 G_{0,b}\succeq D-C_b I,
\]

with C_even approximately 9.824426812434191 and C_odd approximately
10.295721752684191. Exact outward rational values are in the JSON.

For t=0 or t=1/100, nonnegative t permits

\[
 G_{0,b}-tL\succeq(1-2t)D-C_bI.
\]

The actual diagonal is D P_j=(H_j+s)P_j, where H_j is harmonic, and s_lower
is derived from the pinned RC129 actual D Gram entry, divided by 2B. It is
not the differential Legendre eigenvalue j(j+1).

On the physical Legendre moment annihilator of all same-parity degrees below
j0, D>=(H_j0+s_lower)I. This subspace has the listed finite codimension in
the canonical form domain as well: physical moments are continuous there,
and the retained polynomials certify independence. If
(1-2t)(H_j0+s_lower)>C_b, then on this full infinite complement

\[
 G_{0,b}-tL\succeq
 \frac12\left(1-2t-\frac{C_b}{H_{j0}+s_{lower}}\right)L>0.
\]

| Threshold t | Parity | First omitted degree | Moment codimension | Canonical gap lower, approximately |
|---|---|---:|---:|---:|
| 0 | Even | 232 | 116 | 0.0001667193712 |
| 0 | Odd | 371 | 185 | 0.0000310870563 |
| 0.01 | Even | 284 | 142 | 0.0002257718855 |
| 0.01 | Odd | 459 | 229 | 0.0001451668259 |

Min-max thus bounds the full original threshold index, including threshold
equality, by 116+185=301 at zero and 142+229=371 at 0.01. The lower form at
the preceding same-parity degree is nonpositive; these are the smallest
cutoffs supplied by this particular diagonal estimate, with no optimality
claim for the operator. The two prior positive auxiliary pivots are not
subtracted from these independent counts.

## Validation and next cursor

The validator checks 266 inherited Git blob pins. Normal execution and reverse
replay reproduce the exact same JSON. Exact controls check the weighted edge
square, an interior quadratic minimum, a concave endpoint minimum, rejection
of an undersized toy Schur bound, and acceptance of a conservative toy bound.

```bash
python scripts/validate_rpb108_rc277_weighted_prime_schur.py --output certificates/rpb108_rc277_weighted_prime_schur.json
python scripts/validate_rpb108_rc277_weighted_prime_schur.py --output certificates/rpb108_rc277_weighted_prime_schur.json --replay
```

RC278 should use the improved global actual-prime bound to construct a smaller
positive projection reference, or strengthen the retained principal response
bound. A positive canonical gap on the finite-codimension complement does not
prove positivity on the remaining moment directions. Full original positivity
is still the acceptance gate.
