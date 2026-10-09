# RPB108 — NF27: constrained native retained coupling certificate

2026-10-09 UTC. Aperture a=53/50. Phase Geometry continues NF26 at
`14ba1d21bd15656be6a1c1ce60f217cb703d93cc`. Coupled was recovered
read-only through CC68 at `07f837876b47fcfb5fdad2ea041876af1f497cea`.
No integration or paused branch is modified.

Read the additive [NF27 definitions](../docs/TERMINOLOGY_RPB108_RETAINED_COUPLING_NF27.md).

## Result

NF27 certifies the complete **55-dimensional native retained complement**
of each NF26 seed, its physical inverse bound, and its finite coupling
reaction to the NF26 corrected trial. The reaction uses all 55 retained
directions together, not selected coordinates or a numerical sample.

| Strict certified quantity | Even | Odd |
| --- | ---: | ---: |
| Finite retained reaction / corrected energy | (0.0053911, 0.0053913) | (0.0085503, 0.0085504) |
| Finite retained reaction | $(4.70486,4.70487)\times10^{-37}$ | $(2.70872,2.70873)\times10^{-33}$ |
| Energy after finite retained elimination | $(8.6797,8.6801)\times10^{-35}$ | $(3.14088,3.14089)\times10^{-31}$ |
| Physical native gap on retained complement | $>5.80\times10^{-28}$ | $>6.16\times10^{-25}$ |

Both original finite lifted restrictions span(v)+W are positive. Exact
reflection parity therefore gives a positive 112-dimensional finite
restriction with the NF26 source-aware critical columns. This finite
restriction lies in the polynomial modes through 180; it does not include
the entire infinite high space.

The finite retained reaction is smaller than the NF26 directional margin:
it consumes between 13.9% and 14.2% of that margin even and between 3.58%
and 3.59% odd. This comparison is a useful scale check, **not** a collective
Schur certificate. High elimination also changes the retained background
and mixed coupling, as shown explicitly below.

## 1. Exact retained complement and physical inverse

Work in one parity. Let E be the original 56-dimensional E112 retained
space, x the exact NF24 retained seed, W=E intersect x-perp in physical
L2, and A the authenticated original native matrix on E. The NF26 trial
v=p-y has retained component x.

Choose the exact rational basis

\[
W_j=e_j-(x_j/x_0)e_0,\qquad j=1,\ldots,55,
\]

where indices here enumerate the parity basis. Its columns are exactly
orthogonal to x; x_0 is nonzero for both frozen seeds. No assumption of
orthonormality is made. Let

\[
A_W=W^*AW,\qquad K=W A_W^{-1}W^*.
\]

K is the physical inverse of the constrained native form on x-perp,
extended by zero on x. Positive definiteness of A_W is rigorously verified
for the complete original signed source matrix.

Decimal-200 arithmetic selects fixed rational LDL preconditioners and an
approximate inverse B. The proof arithmetic is outward rational at
10^-280. It verifies positivity by the exact rational congruence
J A_W J*, with strictly positive Gershgorin row margins. Decimal values
are not a positivity test.

For R=I-B A_W, the row-sum enclosure rho satisfies rho<1. The rigorous
Neumann bound is

\[
\|A_W^{-1}-B\|_\infty
\le \|B\|_\infty\rho/(1-\rho).
\]

Every inverse entry is enlarged by that bound. Forming W A_W^-1 W*
preserves the original physical mass. Since K is positive semidefinite,
its physical operator norm is at most trace(K). A rational upper enclosure
of the latter gives Q(w)>=||w||_2^2/trace_upper for every w in W. The
strict decimal physical gap bounds in the result table follow.

These native complement gaps are tiny. NF27 does not call the complement
uniformly stable, or transfer these finite gaps to W plus the infinite
high space.

## 2. Complete finite retained reaction and physical error ball

Let b=P_E L_a v. The complete finite retained reaction is

\[
R_W=b^*K b,\qquad
\inf_{w\in W}Q(v-w)=Q(v)-R_W.
\]

b is computed from all 56 native NF24 source coordinates of p minus
NF26's complete approximate Ly coordinates. The original p coordinates
are inherited from native pairings, so no unit-norm arch source error is
multiplied by the enormous constrained inverse.

The only new source replacement error here is that of the tiny high
correction y. Set

\[
\eta_{unit}=2a\epsilon+8R40,
\quad \epsilon=4(106/125)^{320}/(1-106/125),
\quad R40=2(a/2)^{41}/41!.
\]

If b_hat denotes the fixed rational midpoint vector, its physical radius
is bounded by

\[
\delta=8\max_i\operatorname{radius}(b_i)
 +\|y\|_{upper}\eta_{unit},
\]

using sqrt(56)<8 and orthogonal projection contraction. Interval-rounding
and all native and moment-coordinate radii are included. Let T_upper
bound trace(K). In the K seminorm,

\[
\left|\sqrt{b^*Kb}-\sqrt{\widehat b^*K\widehat b}\right|
\le \delta\sqrt{T_{upper}}.
\]

The producer pays this ball after evaluating the quadratic form. Treating
uncertain coordinates independently inside a huge inverse would lose the
cancellation and give an unnecessarily poor bound. All square roots use
rational integer-square-root enclosures.

NF26's original corrected energy is carried unchanged. Its enclosure
minus the paid R_W enclosure is strictly positive in both parities.
Together with positive A_W, this proves the finite lifted restriction.

## 3. A frozen exact retained response for the next source calculation

The producer freezes a rational response near K b_hat at denominator
10^100, then applies an exact rational rank-one correction to impose
x*w=0. The final coefficients need not retain denominator 10^100 after
that orthogonality correction. The complete coefficients are published
in the certificate in NF24's retained-index order.

It independently computes the original native energy gain

\[
2Q(v,w)-Q(w,w),
\]

paying 2||y||_upper eta_unit ||w|| in the mixed pairing. Its positive
interval lies inside the certified optimal-reaction interval. The exact
response norms are approximately 3.84e-6 even and 1.77e-5 odd.
These are polynomial response trials, not claimed exact minimizers or
full-form nulls. Their complete physical sources have not been certified
in NF27.

## 4. The collective assembly interface that remains

In the original decomposition span(v)+W+F, with F=E-perp, write

\[
Q=\begin{pmatrix}
q&c^*&r^*\\
c&A_W&B^*\\
r&B&C
\end{pmatrix},\qquad
r=P_F L_a v,\quad B=P_F L_a W.
\]

The original high C satisfies C>=207/1000. NF26 bounds the scalar
s=q-r*C^-1 r from below. Eliminating the SAME high space also gives

\[
M_W=A_W-B^*C^{-1}B,\qquad
d=c-B^*C^{-1}r.
\]

The true collective sign requires

\[
M_W>0,\qquad s-d^*M_W^{-1}d>0.
\]

NF27 instead computes c*A_W^-1 c before high elimination. Neither its
small size nor positivity of q-c*A_W^-1 c controls M_W or d. In
particular, the positive arithmetic difference
NF26_score-R_W is deliberately labeled **NOT a collective Schur bound**
in the machine certificate. There is no assumption that retained and high
eliminations decouple or commute in the relevant estimates.

NF28 should obtain original source information controlling M_W and d,
using source-aware retained lifts or a paid collective residual Gram.
The exact response w supplies a concrete mixed retained trial on which to
test the next complete source calculation, but success on this one trial
would still not certify all collective mixtures.

## 5. Artifacts and reproducibility

- [Rational constrained inverse and native reaction producer](../scripts/certify_native_retained_coupling_nf27_106.py).
- [Complete inverse bounds, paid reactions and exact response coefficients](data/RPB108_NF27_RETAINED_COUPLING_CERTIFICATE_20261009.json).
- [Validation and file custody](data/RPB108_NF27_RETAINED_COUPLING_VALIDATION_20261009.json).

The producer SHA-256 authenticates the unchanged NF24 targets, published
NF26 source certificate and decompressed E112 native archive before use.
The strengthened replay verifies all common reaction intervals exactly,
positive congruence margins, inverse residual norms below one, both
finite eliminated energies, exact response orthogonality and both
independent exact-response energy gains. Strict outward decimal brackets
are checked against the full rational intervals.

```bash
python scripts/certify_native_retained_coupling_nf27_106.py \
  notes/data/RPB108_NF24_COMPENSATED_SOURCE_TARGETS_20261009.json \
  notes/data/RPB108_NF26_HIGH_CORRECTION_CERTIFICATE_20261009.json \
  INPUT_DIR/native112_N720_K620.json.gz --output certificate.json
```

The full collective residual Gram and whole-domain original sign at 1.06
remain open. The highest internally certified whole-domain aperture is
still 1.05. RH, F4, cap-uniform leakage, actual global null exclusion and
Lean closure are not claimed. Historical wording and paused fronts remain
unchanged; Coupled remains read-only.
