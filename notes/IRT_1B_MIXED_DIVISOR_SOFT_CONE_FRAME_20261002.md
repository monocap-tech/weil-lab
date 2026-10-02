# IRT-1B — mixed-divisor soft-cone frame design

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-1A  
**Status:** **COMPLETE DESIGN PASS / DERIVATIVE CAUCHY FRAME DEFINED / ZERO-MOMENT SECTOR HAS EXACT CAUCHY--VANDERMONDE INJECTIVITY / FRAME CONDITIONING REDUCED TO DERIVATIVE-POINT GEOMETRY / ORDINARY XI-PRIME CRITICALITY SEES ONLY THE UNWEIGHTED ROW / MIXED FACTOR-THROUGH HAS KPH-FLOOR STRENGTH ON A CONDITIONED FRAME / NEXT CURSOR IRT-1C MIXED-CAUCHY-ALIGNMENT SOURCE SCREEN**

## 0. Objective

IRT-1A reduced the desired upstream theorem to a second-channel soft-cone
activation plus a projective bridge into the KPH residual.

IRT-1B asks whether the derivative divisor can supply the second channel in a
canonical finite-dimensional form and whether any part of the two-theorem
contract is already algebraic.

The result is asymmetric:

\[
\boxed{
\text{activation geometry can be made exact;}
}
\]

\[
\boxed{
\text{the mixed bridge remains genuinely new actual-zeta content.}
}
\]

## 1. Derivative-divisor observation operator

Let

\[
F=\{\rho_1,\ldots,\rho_n\}
\]

be the admitted selected packet.

Let

\[
\Tau(F)=\{\tau_1,\ldots,\tau_m\}
\]

be a derivative-divisor family chosen by a canonical packet-scale region rule,
independently of the KPH soft vector and independently of the SOURCE-II
complement response.

Define

\[
\boxed{
(D_{\Tau,F}v)_\ell
=
R_v(\tau_\ell)
=
\sum_{j=1}^n
\frac{v_j}{\tau_\ell-\rho_j}.
}
\]

This is the simplest genuinely mixed-divisor observation matrix.

The selected divisor supplies the columns. The derivative divisor supplies the
rows.

## 2. Exact numerator degree on the dangerous zero-moment sector

Write

\[
P_F(z)=\prod_{j=1}^n(z-\rho_j).
\]

Then

\[
R_v(z)
=
\frac{N_v(z)}{P_F(z)},
\]

where \(N_v\) is a polynomial of degree at most \(n-1\).

Its leading coefficient is

\[
{\bf1}^Tv.
\]

Therefore on the zero-moment sector

\[
q:={\bf1}^Tv=0,
\]

one has

\[
\boxed{
\deg N_v\le n-2.
}
\]

For the CF-A17 defect this condition is exact.

Hence a nonzero dangerous channel can have at most \(n-2\) distinct zeros of
\(R_v\) away from the selected poles.

## 3. Exact derivative-frame injectivity

Take \(m=n-1\) distinct derivative sampling points
\(\tau_1,\ldots,\tau_{n-1}\), none equal to a selected zero.

If

\[
{\bf1}^Tv=0
\]

and

\[
D_{\Tau,F}v=0,
\]

then \(N_v\) has at least \(n-1\) distinct roots while

\[
\deg N_v\le n-2.
\]

Therefore

\[
N_v\equiv0,
\]

hence

\[
R_v\equiv0,
\]

and all residues \(v_j\) vanish.

Thus:

\[
\boxed{
D_{\Tau,F}
\text{ is injective on }
\{v:{\bf1}^Tv=0\}
}
\]

whenever \(n-1\) legal distinct sampling points are supplied.

This is an exact algebraic result. It requires no zeta estimate beyond the
existence of the sampling points.

## 4. Cauchy--Vandermonde determinant

Define the augmented frame matrix

\[
\mathcal F_{\Tau,F}
=
\begin{pmatrix}
{\bf1}^T\\
D_{\Tau,F}
\end{pmatrix}.
\]

For \(m=n-1\),

\[
\boxed{
\det \mathcal F_{\Tau,F}
=
\pm
\frac{
\displaystyle
\prod_{1\le j<k\le n}(\rho_k-\rho_j)
\prod_{1\le \ell<r\le n-1}(\tau_r-\tau_\ell)
}{
\displaystyle
\prod_{\ell=1}^{n-1}
\prod_{j=1}^{n}
(\tau_\ell-\rho_j)
}.
}
\]

Therefore the exact frame degeneracies are explicit:

1. selected-node collision;
2. derivative-node collision;
3. derivative point approaching a selected pole in the chosen normalization;
4. escape/scale effects through the denominator and matrix norm.

On the fixed-cardinality \(n=7\) CF-A17 neighborhood, selected-node geometry is
already compact and distinct. A projective derivative-frame theorem therefore
reduces to projective control of the \(\Xi'\)-sampling geometry.

## 5. Quantitative activation target

The full-frame version is:

### DD-FRAME

For every sufficiently high admitted actual packet in \(U_*\), a canonical
selection rule produces \(n-1\) derivative zeros
\(\tau_1,\ldots,\tau_{n-1}\) such that

\[
\boxed{
\inf_{\substack{
\|v\|=1\\
{\bf1}^Tv=0
}}
\|D_{\Tau,F}v\|
\ge
H_F^{-a}
}
\]

for one fixed \(a\).

A sufficient geometric form is a projective lower bound on the augmented
Cauchy--Vandermonde determinant together with a projective upper bound on the
matrix norm.

Near CF-A17, where the KPH kernel is simple, this can be weakened further.

### DD-ONE-RAY

A canonically selected derivative zero \(\tau(F)\) satisfies, for the normalized
KPH soft ray \(v_F\),

\[
\boxed{
|R_{v_F}(\tau(F))|
\ge
H_F^{-a}.
}
\]

One scalar observation is enough on a one-dimensional soft cone.

The choice of \(\tau(F)\) may not depend on \(v_F\).

## 6. Ordinary derivative criticality gives only the wrong row

Factor

\[
\Xi(z)=P_F(z)G_F(z).
\]

At an ordinary zero \(\tau\) of \(\Xi'\) with \(\Xi(\tau)\ne0\),

\[
0
=
\frac{\Xi'}{\Xi}(\tau)
=
\frac{P_F'}{P_F}(\tau)
+
\frac{G_F'}{G_F}(\tau).
\]

Equivalently,

\[
\boxed{
\sum_{j=1}^n
\frac1{\tau-\rho_j}
=
-\frac{G_F'}{G_F}(\tau).
}
\]

This is the derivative-divisor critical equation.

But it is the Cauchy row applied to the constant vector:

\[
D_{\tau,F}{\bf1}.
\]

The desired mixed observation is

\[
D_{\tau,F}v.
\]

For the CF-A17 dangerous channel,

\[
{\bf1}^Tv=0.
\]

Thus the ordinary critical equation constrains exactly the unweighted moment
that vanishes on the dangerous channel.

This is the weighted-criticality mismatch.

No linear algebra converts the critical equation into a bound on
\(D_{\tau,F}v\) for an arbitrary zero-moment \(v\).

## 7. Higher critical curvature does not repair the typing automatically

Differentiating the logarithmic derivative at a simple derivative zero gives
unweighted higher-resolvent rows such as

\[
\sum_j\frac1{(\tau-\rho_j)^2}
\]

plus the corresponding complement field.

These remain observations with fixed unit weights on the selected divisor.

The KPH channel requires the coefficient vector \(v\).

NJDG-5 showed that critical curvature can determine one logarithmic-derivative
jet at the critical point, but the curvature datum is itself second-resolvent
information and does not supply a uniform weighted frame on the KPH soft vector.

Thus finite derivative order alone does not remove the coefficient mismatch.

## 8. What a factor-through bridge would mean

The most direct candidate bridge is

\[
\boxed{
D_{\Tau,F}
=
M_F A_F^{\rm KPH}+E_F
}
\]

on the relevant zero-moment/soft sector, with

\[
\|M_F\|\le H_F^b
\]

and subordinate \(E_F\).

At an exact KPH null vector \(v\),

\[
A_F^{\rm KPH}v=0.
\]

If \(E_F=0\), the bridge forces

\[
D_{\Tau,F}v=0.
\]

But the conditioned derivative frame from Sections 3--5 forces

\[
v=0.
\]

Therefore:

\[
\boxed{
\text{DD-FRAME}
+
\text{bounded exact DD-BRIDGE}
\Longrightarrow
\text{no KPH null}.
}
\]

This is exactly the intended mechanism.

## 9. Quantitative factorization cost shows the bridge has target strength

When \(A_F^{\rm KPH}\) is invertible,

\[
D_{\Tau,F}
=
D_{\Tau,F}(A_F^{\rm KPH})^{-1}
A_F^{\rm KPH}.
\]

Let \(v_{\min}\) be a unit right singular vector with

\[
\|A_F^{\rm KPH}v_{\min}\|
=
KPH(F).
\]

Then

\[
\boxed{
\left\|
D_{\Tau,F}(A_F^{\rm KPH})^{-1}
\right\|
\ge
\frac{
\|D_{\Tau,F}v_{\min}\|
}{
KPH(F)
}.
}
\]

Consequently, under DD-FRAME,

\[
\left\|
D_{\Tau,F}(A_F^{\rm KPH})^{-1}
\right\|
\ge
\frac{H_F^{-a}}{KPH(F)}.
\]

So a theorem asserting a projective factorization bound

\[
\left\|
D_{\Tau,F}(A_F^{\rm KPH})^{-1}
\right\|
\le H_F^b
\]

immediately yields

\[
\boxed{
KPH(F)\ge H_F^{-(a+b)}.
}
\]

Thus once the derivative frame is conditioned, a projectively bounded
factor-through theorem is quantitatively KPH-floor strength.

This is not a defect in the design. It tells us that the genuine new theorem
cannot be hidden in generic operator algebra.

## 10. Why source-free factorization is impossible as a universal theorem

CF-A17 supplies a source-free bounded carrier with

\[
KPH(F_*)=0
\]

and a nonzero zero-moment null vector.

For an arbitrary legal collection of \(n-1\) sampling points in generic
position, the augmented Cauchy frame is injective on that null sector.

Therefore no source-free universal theorem can simultaneously guarantee:

1. a conditioned derivative-style Cauchy frame;
2. projectively bounded factor-through through \(A_F^{\rm KPH}\).

Any such theorem must use actual-zeta information in the placement or
interaction of the derivative divisor.

This is exactly the IRT requirement.

## 11. Minimal mixed-divisor theorem after IRT-1B

The derivative route no longer needs exact RENJET reconstruction.

The minimal source theorem can be stated as:

### AZ-MIXED-CAUCHY-ALIGN

For every sufficiently high admitted actual zeta packet \(F\in U_*\), a
canonically selected derivative-divisor family \(\Tau(F)\) satisfies:

1. **frame**
   \[
   \inf_{\|v\|=1,\ {\bf1}^Tv=0}
   \|D_{\Tau,F}v\|
   \ge H_F^{-a};
   \]

2. **mixed alignment**
   \[
   \|D_{\Tau,F}v\|
   \le
   H_F^b
   \|A_F^{\rm KPH}v\|
   +
   o(H_F^{-a})
   \]
   on the KPH soft cone.

Then

\[
KPH(F)\ge H_F^{-(a+b+o(1))}.
\]

The local simple-soft version replaces the full frame by one canonical
derivative observation with nonzero projective pairing against the soft ray.

## 12. Comparison with NJDG

NJDG asked derivative zeros to supply:

- critical-point frames for logarithmic-derivative jets;
- curvature reconstruction;
- exact synthesis of the weighted RENJET kernel;
- or a direct mixed-divisor weighted identity.

IRT-1B identifies a smaller target.

It asks only for a **Cauchy observation frame on the selected coefficient
sector** plus a mixed alignment inequality with the KPH residual.

No exponential kernel appears.

No complement reconstruction appears.

No higher RENJET jet appears.

This is the cleanest derivative-divisor theorem signature obtained so far.

## 13. What remains genuinely external

Nothing in the present stack proves either of the following actual-zeta facts:

- every dangerous selected packet has enough nearby derivative zeros to form a
  projectively conditioned Cauchy frame;
- those derivative Cauchy observations align projectively with the KPH residual.

The first is a sharpened critical-frame existence/conditioning question.

The second is a weighted mixed-divisor theorem not implied by ordinary
criticality.

The second is the deeper obstacle.

## 14. Determination

IRT-1B establishes:

- canonical derivative Cauchy observation matrix: **YES**;
- exact injectivity on the zero-moment sector with \(n-1\) distinct sample
  points: **YES**;
- explicit Cauchy--Vandermonde determinant: **YES**;
- quantitative frame reduced to derivative-point geometry: **YES**;
- ordinary \(\Xi'\)-criticality controls the weighted KPH row: **NO**;
- critical curvature automatically supplies the missing weights: **NO**;
- projectively bounded factor-through plus conditioned frame implies KPH floor:
  **YES / EXACT**;
- source-free universal mixed factor-through possible: **NO / CF-A17 CONTROL**;
- direct derivative-to-RENJET reconstruction still required: **NO**;
- new minimal actual-zeta theorem signature isolated: **YES**;
- KPH floor proved: **NO**;
- NEXTJET proved: **NO**;
- RH proved: **NO**.

## 15. Cursor

The next lawful pass is a theorem-specific source screen, not another
representation design:

\[
\boxed{
\texttt{IRT-1C / MIXED-CAUCHY-ALIGNMENT SOURCE SCREEN}
}
\]

Search only for results capable of supplying one of:

1. every-packet projectively conditioned \(\Xi'\)-Cauchy frames near a
   prescribed zeta packet;
2. weighted mixed \(\Xi/\Xi'\) Cauchy estimates on a prescribed coefficient
   vector;
3. a pointwise theorem forcing derivative-divisor observations to align with
   a reciprocal-Cauchy soft mode;
4. a stronger mixed-divisor identity whose implication to
   AZ-MIXED-CAUCHY-ALIGN is explicit.

Average pair correlation, density, or one-sided derivative-zero proximity is
insufficient.

No canonical theorem status changes.
