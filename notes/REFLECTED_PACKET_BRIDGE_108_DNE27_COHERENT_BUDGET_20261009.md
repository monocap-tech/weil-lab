# RPB108 — DNE27: improved coherent source credits and eight-direction gap

Definitions precede use in [DNE27 terminology](../docs/TERMINOLOGY_RPB108_DNE27_COHERENT_BUDGET.md).
Parent DNE26: d82a8197a4dc7cef144ff8a6c4b04d6a06166663.
Read-only Phase NF40: 090e389c030c9b488de00d1e44a6b1b6bd43f96c.
Read-only Coupled CC79: dd93e5cc7d003d44cdc240c5710f4c253dc1346f.
Only research/rpb108-direct-null-exclusion is written.

## Result

The ORIGINAL DNE23 four-column frames are unchanged. A sharper complete
source domination and a rebalanced Young split increase both their
physical gaps and DNE25's conditional complete-remainder source credits.

| Paid quantity | Even | Odd |
| --- | ---: | ---: |
| Complete three-source domination Gamma3<=rho V | rho=0.953 | rho=0.959 |
| New rational Young split theta | 0.217 | 0.154 |
| Prior four-column remainder credit | 0.00145 | 0.00625 |
| New four-column remainder credit c | 0.00316 | 0.00962 |
| Credit improvement | >2.17 times | >1.53 times |
| Full-high physical gap, strict lower | >4.27555e-36 | >2.29448e-32 |

The original eight-direction retained restriction, together with every
original infinite high correction, now has the common certified guard

    Q(h)>=4*10^-36 ||h||^2, h in Z8+F112.

This improves the prior reported guard 10^-36. No retained direction is
added: eight remain jointly certified and 104 remain outside that plane.
The higher source credits are paid budgets for a conditional remaining
test, not a passing complete remaining Gram or whole-domain positivity.

## Sharper complete-source correlation

DNE22 certifies V=Q3-Gamma3/kappa>=g diag(s_i^-2)>0 at kappa=11/25.
DNE23 used Gamma3<=V to pay the unknown low-source crosses together.
DNE27 instead tests the entire matrix rho V-Gamma3 on a rational grid.
Strict outward congruence/Gershgorin margins certify rho=953/1000 even
and rho=959/1000 odd. All signed source entries are retained. These are
not three independent diagonal ratios or assumptions about covariance.

Let r0 be the complete low F112 source, let P0 bound its norm square,
and let g0 be its three source crosses. For every coefficient z,

    |g0 z|^2<=P0 z*Gamma3 z<=rho P0 z*V z.

The inherited paid original native low row p has V-dual square at most
d_native. Thus the entire mixed coarse row satisfies

    |[p-g0/kappa]z|<=M sqrt(z*V z),
    M=sqrt(d_native)+sqrt(rho P0)/kappa.

The square roots are outward rational bounds. No actual low-source cross
is inferred, and no inverse-high covariance is substituted for a raw
source covariance. P0, the native row, Q3 and Gamma3 are authenticated
original inputs from DNE18/DNE22/DNE23.

## Rebalanced four-column lower form

Let A_low be the inherited original low coarse diagonal lower bound.
Young's inequality gives, for theta in (0,1),

    U4>=diag(alpha,theta V),
    alpha=A_low-M^2/(1-theta).

The rational search checks alpha>0 and the native comparison for each
candidate. The selected choices are theta=217/1000 even and 77/500 odd.
This yields L=diag(alpha,theta g/s_i^2)>0 on the original four-column
coarse SOURCE matrix U4=Q4-Gamma4/kappa. The lower form includes all
mixed coefficients at once. It is not a splice of independently
condensed directions.

The original native matrix Q4 is positive since U4>0 and Gamma4 is a
Gram. DNE23's low/lift pairings, the CC62 low diagonal and NF32's complete
native matrix enclose all its entries. Absolute scaled row bounds q_i
pay the Gershgorin comparison

    L>=(c/kappa)Q4.

The best sufficient credit among the paid denominator-1000 theta grid
choices is rounded downward to denominator 100000. The reported
0.00316 and 0.00962 each retain strictly positive rational margins.
No floating optimization enters the certificate, and no claim that
these credits are maximal over all parameters is made.

It follows that the entire four-column source satisfies

    Gamma4<=kappa(Q4-L)<=(kappa-c)Q4.

The complete remaining test from DNE25 can therefore use these larger
credits on THIS unchanged frame: c B_Y-Gamma_Y>0 after exact native
energy orthogonalization would prove whole-aperture positivity. A frozen
rational remainder may instead pay r+kappa epsilon<c. The remaining
native border, orthogonalization and complete source Gram are still
uncomputed; the increased budget does not assert that they pass.

## Physical gap with all high vectors

The original high block C>=kappa I and its square completion are
unchanged. For each of the four finite columns, use its authenticated
physical norm upper bound plus sqrt(source diagonal upper)/kappa to
bound the inverse-completed physical column norm b_i. Weighted Cauchy
gives

    physical_gap >= [b0^2/alpha
        +sum_(i=1..3)(s_i b_i)^2/(theta g)+1/kappa]^-1.

The computed physical bounds improve the corresponding DNE23 rational
bounds in both parities. The common reported guard is 4*10^-36.
Physical masses of the nonorthogonal frame are paid; finite coordinate
energy is not treated as physical mass. Exact reflection parity combines
both sectors and every original high vector remains included.

## Validation and custody

Two fresh arithmetic consumers at 160 and 200 rational root digits each
pass 10 explicitly counted outer certificate assertions. The grid
feasibility decisions and root helper assertions are additional. The
independent validator passes 861 rational checks, including 248 flat
full-source domination quadratic tests, 98 exact coherent Young
identities, 486 nonorthogonal physical/high-completion tests, native
comparison margins, improved gaps and replay comparisons. Both root
precisions select identical rho, theta and source credits. The higher
precision physical gap is no weaker. Python syntax checks pass.

Three genuine border crossings retain positive diagonals and cross
positive/null/negative determinants at borders .99,1,1.01. Whole-mass
shifts of the exact null matrix [[1,1],[1,1]] give positive ground levels,
while a retained-only subtraction misses the shifted null. These are
abstract controls, not original Weil countermodels. They supplement the
inherited DNE23/DNE25 original-form and source controls.

All six load-bearing inputs are SHA256 authenticated. Expensive complete
original source producers are not rerun. No new source or actual inverse
response is evaluated. The result is an outward computational improvement
combined with the inherited original-source and closed-form high
theorems, not a Lean proof.

## Current-head interface and preserved boundary

NF40 certifies an actual native boundary defect compression and a
zero-response abstract extension. Its missing signed boundary/source
correlations remain open. It does not supply the low-mode border for
DNE26's changed NF38 lifts. Those separate packets are not used in the
new numerical credits. DNE27 deliberately keeps the fully paid DNE23
frame; it writes neither Phase nor Coupled.

Whole 1.06 positivity, the remaining 104-dimensional source reaction,
exact unit-response exclusion, all-aperture continuation, RH/F4/full
transport and Lean remain open. DNE24's exact null reduction is unchanged.
Earlier results and historical wording are preserved additively.

## Reproduction

```sh
python3 scripts/certify_dne27_coherent_budget.py notes/data/RPB108_DNE23_EIGHT_DIRECTION_CERTIFICATE_20261009.json notes/data/RPB108_DNE22_PROBE_PLANE_CERTIFICATE_20261009.json notes/data/RPB108_DNE18_CC62_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_EVEN_INPUT_20261009.json notes/data/RPB108_DNE22_NF32_ODD_INPUT_20261009.json notes/data/RPB108_DNE25_SOURCE_BUDGET_CERTIFICATE_20261009.json --output /tmp/dne27.json
```

Replay with --digits 200. The validator takes the same six inputs,
primary output, replay output and a validation output path. Custody
retains source/output hashes and the pinned research heads.
