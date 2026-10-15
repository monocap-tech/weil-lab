# RPB108 — RC280: combined jump covariance certifies a five-coordinate block

Parent RC279: `c895261129ffbaae169508c06f8b243421340906`.
Branch: `research/rpb108-route-consolidation`. Aperture B=11/10.

RC280 certifies the complete odd auxiliary block on **P1,P3,P5**, together
with the even block on **P0,P4**. The certified positive block grows from
dimension 3 to **5**, leaving a **366-dimensional** exact Schur problem in
the unchanged rank-371 reference. The finite response trials, their actual
form centers, and the finite residual Gram matrices are unchanged.

The improvement comes from preserving the infinite prime-tail covariance.
Every jump depends on the combined trial's endpoint value, and the continuous
remainder admits a derivative Gram bound. These structures survive the norm
estimate instead of being replaced by separate basis-vector tail costs.

| Certified joint native block | Even | Odd |
|---|---:|---:|
| Positive degrees | 0,4 | 1,3,5 |
| Block dimension | 2 | 3 |
| Native coefficient Euclidean floor lower, approximately | 0.000591926611583 | 0.000000986007771 |
| Remaining coordinates | 140 | 226 |
| Jump/remainder Young parameter | 3 | 3 |
| Tail/global-fault Young parameter | 1/100 | 1/100 |
| Finite/noise Young parameter | 9/100 | 14/25 |

The even three-mode block P0,P2,P4 is not certified positive. The full
six-mode question and all block-to-remaining cross payments remain open.
Stage I, RH, F4 and Lean are not closed. The original index bounds 301 at
zero and 371 at 0.01, including equality, and the lower bound 10 below 0.01
are preserved. Five positive auxiliary directions are not subtracted from
these independent index bounds.

## The common rational prime model is bounded separately

Write t=x/B and q(t)=sum a_n P_n(t). Use exactly the common rational prime
parameters already certified at RC274 and RC279. RC280 checks their equality
across the reused action profiles. The operator is

\[
 K_m q(t)=-\sum_n c_n[\widetilde q(t+\ell_n/B)
                            +\widetilde q(t-\ell_n/B)].
\]

The rational model is not identified with the actual prime operator. Every
actual/model fault inherited from RC279 remains paid. Because the chosen
rational parameters may lie outside the tiny original arithmetic intervals,
RC280 separately reruns RC277's complete weighted Schur proof for their
zero-width parameter intervals. It proves ||K_m||<=3013/1000 on the full
physical space, including both parities and every support boundary.

## One universal jump function for each parity

For each prime power set b_n=|1-ell_n/B| in (0,1). There are seven distinct
positive boundaries. Define the paired step functions

\[
 F_{b,e}=-1_{(-b,b)},\qquad
 F_{b,o}=1_{(b,1)}-1_{(-1,-b)}.
\]

Both have jump +1 at b, with the correct reflected jump for their parity.
For a same-parity polynomial let S=q(1)=sum a_n; then q(-1)=(-1)^base S.
The positive-boundary jump of K_m q is S sigma_n c_n, where

\[
 \sigma_n=1\quad(\ell_n<B),\qquad
 \sigma_n=(-1)^{base+1}\quad(\ell_n>B).
\]

Thus the entire jump part is S J_b, with the universal same-parity function

\[
 J_b(t)=\sum_n\sigma_n c_n F_{b_n,b}(t).
\]

All seven primes remain combined before squaring. The physical norm of J_b is
computed exactly from its constant values on the rational support cells.

For n>0 of matching parity, each paired step has Legendre coefficient

\[
 f_{b,n}=\frac{2n+1}{n+1}[P_{n-1}(b)-bP_n(b)].
\]

Its constant coefficient is -b in even parity and zero in odd parity. Other
parity coefficients vanish. High-precision interval Legendre recurrences give
all universal jump coefficients through degree 2048. Their joint captured
energy is subtracted from the exact norm, giving complete physical tail bounds
approximately 0.000515675713113 even and 0.000564455434307 odd. These bounds
retain every cross-prime term; there is no assumption that boundary tails are
orthogonal. Exact controls independently check the step coefficient formula
and parity by direct integration at low degrees.

## The continuous remainder has a full derivative Gram bound

Set g=K_m q-S J_b. All jumps cancel, so g is continuous and piecewise polynomial.
Away from the support boundaries its t-derivative is K_m q'. Its weak derivative
has no boundary delta terms. Consequently

\[
 B\int_{-1}^1(1-t^2)|g'(t)|^2dt
 \le\|K_m q'\|_2^2
 \le(3013/1000)^2\,B\int_{-1}^1|q'(t)|^2dt.
\]

Integration by parts against P_n has no interior jump terms because g is
continuous, and no outer boundary term because (1-t^2)P_n' vanishes at +/-1.
The derivative Legendre polynomials are orthogonal in the weighted derivative
inner product. Bessel's inequality therefore gives

\[
 \sum_n n(n+1)mass_n\,|g_n|^2
 \le B\int_{-1}^1(1-t^2)|g'|^2dt.
\]

The physical tail above degree 2048 is at most this energy divided by
first*(first+1), with first=2050 even or 2049 odd. This argument applies to the
full infinite tail. The n(n+1) factor is used only for this derivative estimate;
the original D diagonal remains H_n+s.

For several trials q_i, polarization yields the same Loewner bound with the
exact derivative Gram

\[
 (G')_{ij}=B\sum_{n,d}a_{i,n}a_{j,d}
                   \min(n,d)(\min(n,d)+1),
\]

where the sum is over matching parity. The formula follows from
integral P_n' P_d'=min(n,d)(min(n,d)+1) for equal parity. The validator checks
this normalization by exact integration for degrees through 8 and checks
positivity of the actual derivative Gram. Signed cross terms among the
combined trials remain intact.

## Transfer the tail matrices to the inverse response

Keep RC278's full lower form

\[
 G\succeq W=D_P+(D-C_b)_Q\succeq\mu_bD>0.
\]

On the tail beginning at first, set
d_first=H_first+s_lower and w_first=1-C_b/d_first. Physical tail energy is
converted to W-inverse residual energy by division by d_first*w_first.
Since a trial has degree at most 64, its source and augmentation terms have
no output above 2048. Its modeled residual there is the negative original
endpoint-plus-prime output. The regular polynomial and pole Taylor models
also have finite degree below this cutoff; their actual model faults remain
in the global error payment.

Let S_vec contain the three combined endpoint values. The universal jump
covariance is the rank-one matrix

\[
 J_{tail}=\frac{\|Q_{2048}J_b\|_2^2}{d_{first}w_{first}}
                       S_{vec}S_{vec}^*.
\]

The continuous-prime covariance is bounded by

\[
 C_{tail}=\frac{(3013/1000)^2}
 {first(first+1)d_{first}w_{first}}\,G'.
\]

RC252's signed endpoint moment expansion is extended to arbitrary signs of
S. Its geometric remainder bounds all higher-degree endpoint output. A
three-column Cauchy payment gives an endpoint tail covariance E_tail.
No original endpoint term is dropped or assigned zero tail.

For rho=1/10 and the selected eta, the complete supported model tail satisfies

\[
 T_{tail}\preceq(1+\eta)J_{tail}
 +(1+1/\eta)[(1+\rho)C_{tail}+(1+1/\rho)E_{tail}].
\]

RC279's remaining global model faults, finite e0 interval uncertainty and
source D-inverse uncertainty are recomputed without their separately charged
model tails. Only those supported tails are replaced. If V_fine denotes that
full joint error envelope, then for the selected zeta

\[
 V_{new}=(1+\zeta)T_{tail}+(1+1/\zeta)V_{fine}
\]

bounds all noise. Global faults are not assumed orthogonal to the supported
tail, and within-column or between-column errors may be correlated.

Finally, with RC279's unchanged finite residual Gram upper S_fin, the added
inverse correction satisfies

\[
 E^*D N^{-1}E\preceq(1+\theta)S_{fin}+(1+1/\theta)V_{new}.
\]

The actual auxiliary gate is bounded below by subtracting this full matrix
and the paid variational-center interval radius from Mass-C_b times the
variational center. The correction sign remains added to the inverse response.

## Certified result and validation

The selected exact lower matrices certify P0,P4 jointly in even parity and
P1,P3,P5 jointly in odd parity. Their native Euclidean floors in the table
are reciprocal inverse-trace witnesses, followed by exact PSD checks after
subtracting the certified floor. Opposite-parity couplings vanish. This is a
five-dimensional positive block, rather than five independent diagonal tests.

For orientation, diagonal entries of the new noise envelopes are about
5.64e-6 to 5.78e-6 even and 6.92e-6 to 7.58e-6 odd. The previous entries were
about 4.81e-5 to 1.13e-4 even and 6.01e-5 to 1.25e-4 odd. These diagonal costs
are not a claim that the old envelope dominates the new one in every Loewner
direction. The certified positive block matrices supply the acceptance test.

The validator checks 275 inherited Git blob pins. Normal generation and reverse
replay recompute the step projections with the inherited independent interval
precisions, reverse the certified energy sums, and compare the complete rational
JSON. Exact controls cover step normalization and parity, derivative Grams,
endpoint cancellation and the inherited correlated matrix Young payments.

```bash
python scripts/validate_rpb108_rc280_combined_jump_tail.py --output certificates/rpb108_rc280_combined_jump_tail.json
python scripts/validate_rpb108_rc280_combined_jump_tail.py --output certificates/rpb108_rc280_combined_jump_tail.json --replay
```

No new finite original Weil actions or full-range inverse solves are performed.
The rank-371, rank-608 and rank-639 reference certificates and the eight-source
inverse width 485647/1000000 remain preserved. RC281 must pay the enlarged
block-to-remaining cross columns and certify the remaining principal Schur
response. Positivity on the full aperture remains open.
