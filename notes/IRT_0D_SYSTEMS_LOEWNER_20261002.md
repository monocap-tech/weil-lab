# IRT-0D — systems realization / Loewner exactness screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0C1  
**Status:** **COMPLETE PRIMARY SCREEN / EXACT SEMIGROUP REALIZATION FOUND / FINITE LOEWNER EXACTNESS CONDITIONAL ON REALIZATION RANK AND SAMPLE FRAME / STRUCTURED DELAY REALIZATION REQUIRES PRESCRIBED EXPONENTIAL STRUCTURE / NO CANONICAL FINITE-DATA BYPASS / NEXT CURSOR IRT-0D1 RESOLVENT-TO-SEMIGROUP CONTINUUM CONTROL**

## 0. Objective

IRT-0D asks whether systems realization theory can evade the NJDG-6 statement

\[
\text{finite rational critical rows}
\not\Rightarrow
\text{exact nonconstant entire RENJET kernel}.
\]

The answer is more nuanced than a simple no.

The RENJET kernel has an exact semigroup/distributed-delay realization, and
each fixed finite near divisor has an exact finite-dimensional state-space
realization. Therefore the target is not intrinsically outside systems theory.

What fails is the data interface: the canonical branch does not supply enough
well-conditioned resolvent observations to identify the required realization
uniformly packet by packet.

## 1. Exact semigroup form of the RENJET kernel

For one exponential mode,

\[
K_t(w)=\frac{e^{tw}-1-tw}{w^2},
\]

with the removable value \(K_t(0)=t^2/2\).

Direct integration gives

\[
\boxed{
K_t(w)=\int_0^t (t-r)e^{rw}\,dr.
}
\]

Equivalently,

\[
K_t(-s)
=
\mathcal L\!\left[(t-r)\mathbf 1_{[0,t]}(r)\right](s).
\]

Thus the RENJET kernel is exactly the transfer of a finite-impulse
distributed-delay/transport-type system.

It is transcendental as a scalar function of \(w\), but it is not
"unrealizable." Its natural realization is infinite-dimensional if the
transfer variable itself is the state-space frequency variable.

## 2. Finite near block gives an exact finite-dimensional realization

Let the authorized near block be

\[
\Omega=\{w_1,\ldots,w_n\},
\qquad
w_\mu=\mu-c,
\]

with multiplicity/weight vector

\[
b=(m_1,\ldots,m_n)^T.
\]

Set

\[
A_\Omega=\operatorname{diag}(w_1,\ldots,w_n),
\qquad
c^\ast=(1,\ldots,1).
\]

Then the exponential population is

\[
\boxed{
E_\Omega(r)
=
\sum_{\mu\in\Omega}m_\mu e^{rw_\mu}
=
c^\ast e^{rA_\Omega}b.
}
\]

The first mode-weighted near response is therefore

\[
\boxed{
Q_t(\Omega)
=
c^\ast K_t(A_\Omega)b
=
\int_0^t(t-r)c^\ast e^{rA_\Omega}b\,dr.
}
\]

So for each fixed finite packet, RENJET is a matrix-function observable of an
\(n\)-state diagonal realization.

This is an exact identity, not a model approximation.

## 3. Critical rows are resolvent observations

For a sampling point \(\delta\),

\[
H_\Omega(\delta)
=
c^\ast(\delta I-A_\Omega)^{-1}b
=
\sum_{\mu\in\Omega}
\frac{m_\mu}{\delta-w_\mu}.
\]

A first derivative gives

\[
-H_\Omega'(\delta)
=
c^\ast(\delta I-A_\Omega)^{-2}b.
\]

Thus the NJDG critical-value and curvature rows are exactly the systems-theory
data species:

\[
\boxed{
\text{resolvent samples and derivatives}.
}
\]

The NJDG value-to-jet and finite-rational-span calculations are therefore
standard realization/observability phenomena in another language.

## 4. Classical Loewner exactness

The classical Loewner framework reconstructs minimal rational interpolants from
frequency-response samples.

If the underlying transfer function is rational of McMillan degree \(n\), a
sufficiently rich data set has Loewner rank \(n\), and under the standard
nondegeneracy hypotheses one obtains a degree-\(n\) realization interpolating
the data exactly.

Relevant source family:

- Antoulas--Anderson rational interpolation / Loewner theory;
- Mayo--Antoulas and later Loewner realization literature;
- the standard rank identity relating Loewner rank and McMillan degree.

Therefore for the *isolated finite near transfer* \(H_\Omega\), systems theory
offers the conditional chain

\[
\boxed{
\text{enough samples of }H_\Omega
\to
\text{recover a realization of }A_\Omega
\to
\text{evaluate }K_t(A_\Omega)
\to
Q_t(\Omega).
}
\]

This is an exact mixed resolvent-to-exponential route for each fixed finite
near block.

## 5. Why this does not contradict NJDG-6

NJDG-6 rules out one fixed finite linear combination of critical
value/curvature rows reproducing the nonconstant entire kernel uniformly as a
function of a free node \(w\).

Loewner reconstruction does something stronger and more adaptive:

- it uses a number of samples commensurate with the realization rank;
- it solves an inverse realization problem;
- the resulting coefficients depend on the sampled transfer data;
- the realized model depends on the actual underlying spectrum.

Thus there is no contradiction.

The systems theorem says:

\[
\boxed{
\text{finite-dimensional target}
+
\text{enough target-dependent data}
\Rightarrow
\text{exact reconstruction}.
}
\]

NJDG says:

\[
\boxed{
\text{fixed finite packet-independent row combination}
\not\Rightarrow
\text{uniform exponential kernel}.
}
\]

Both are true.

## 6. Realization-rank debt

The price of Loewner exactness is the realization rank.

If

\[
n=|\Omega|
\]

then exact reconstruction requires enough independent data to resolve a
degree-\(n\) rational transfer function.

The canonical branch does not supply:

1. a fixed uniform bound on the required number of derivative-critical rows
   independent of the packet;
2. a theorem forcing enough such rows in the required packet-scale region;
3. a projective lower bound on the associated Loewner/interpolation
   conditioning.

These are exactly the failures already isolated in NJDG-3 and NJDG-4 under the
names critical-point frame, row separation, and every-packet quantifier.

Hence Loewner theory does not remove those requirements. It identifies them as
a **realization-rank debt**.

## 7. Endogenous samples versus chosen samples

Standard data-driven realization assumes one may sample the transfer function
at chosen interpolation points, or that a sufficiently rich data set has
already been measured.

The zeta derivative-critical rows are endogenous:

\[
\tau_j
\quad\text{must themselves be zeros of }\Xi'\text{ or }\zeta'.
\]

The canonical branch cannot choose arbitrary well-separated sample nodes.

Therefore ordinary Loewner design freedom is absent.

Replacing the critical nodes by arbitrary evaluation points would require
independent access to the near/complement transfer function at those points.
That is not supplied by the derivative-zero route.

## 8. Complement-adaptive exact interpolation is not canonically admissible

For a fixed finite actual spectrum
\(\{w_1,\ldots,w_n\}\), there always exists a polynomial or rational function of
degree \(<n\) matching \(K_t\) on those \(n\) nodes, modulo multiplicity/Hermite
conditions.

Equivalently, Cayley--Hamilton makes

\[
K_t(A_\Omega)
\]

a polynomial in \(A_\Omega\) of degree below the minimal-polynomial degree.

But the interpolation coefficients depend on the actual complement spectrum.

The canonical SOURCE-II selection order freezes the source multiplier from
selected data before complement adaptation.

Therefore

\[
\boxed{
\text{actual-spectrum interpolation}
}
\]

is not a lawful bypass unless one proves that its coefficients or condition
number can be selected independently of the complement, or that the allowed
canonical data already determine them.

That is precisely the actual-zero interpolation re-entry condition previously
recorded by NJDG, not an automatically available systems theorem.

## 9. Structured realization with exponential/delay basis

Structured realization extends Loewner-type methods to transfer functions of
the form

\[
H(s)=
C\left(\sum_{k=1}^K h_k(s)A_k\right)^{-1}B,
\]

where the analytic functions \(h_k\) are specified in advance.

Schulze--Unger--Beattie--Gugercin explicitly include internal delay systems,
where prescribed structure functions contain factors such as

\[
e^{-\tau s}.
\]

Thus systems theory can indeed construct finite structured realizations having
transcendental/exponential transfer dependence.

However this does not derive exponential structure from finite rational
critical data.

The functions \(h_k\) are **input structure** to the realization algorithm.

For IRT, prescribing the known exponential RENJET kernel or delay basis in
advance and then identifying coefficient matrices merely encodes the target
structure that SOURCE-II already knows.

Therefore:

\[
\boxed{
\text{structured delay realization}
=
\text{exact representation if the exponential class is prescribed,}
}
\]

not

\[
\boxed{
\text{finite derivative rows}
\Rightarrow
\text{new exponential mixed-divisor theorem}.
}
\]

## 10. Infinite-dimensional systems make the target exact, not identifiable

General infinite-dimensional linear systems admit transfer functions defined
from semigroup resolvents,

\[
G(s)=C(sI-A)^{-1}B+D,
\]

and distributed/delay systems naturally produce irrational transfer functions
with infinitely many poles/zeros or exponential dependence.

This validates the formal class match.

But exact realization of a known irrational transfer function and
identification of that function from sparse observations are different
problems.

Finite Loewner data generally produce a finite rational interpolant/model
reduction of an irrational transfer. Exact recovery requires prior structured
knowledge or an infinite/growing data regime.

## 11. Resolvent-to-semigroup theorem class

The systems literature contains a genuinely different bridge:

\[
\boxed{
\text{resolvent control on a continuum}
\Longrightarrow
\text{semigroup control}.
}
\]

Examples include:

- Hille--Yosida generation, which requires resolvent existence and bounds on a
  half-plane/ray, including resolvent powers in the general bounded-growth
  form;
- inverse-Laplace formulas expressing \(e^{tA}\) through contour integrals of
  \((sI-A)^{-1}\);
- Kreiss-type theorems controlling powers or exponentials from uniform
  resolvent bounds on a domain;
- Hilbert-space stability theorems of Gearhart--Prüss type.

This theorem class does bridge rational resolvent data to exponential
dynamics, but the input is not a finite set of scalar samples.

It requires domain/contour-scale resolvent information.

That is the surviving systems-theoretic possibility.

## 12. Relation to the canonical outside field

A contour-scale resolvent theorem applied to the zeta packet would require
uniform control of the pole-removed resolvent/transfer function along a
contour or region around the packet.

But that function is again the canonical analytic outside/complement field
together with the explicitly retained near divisor.

Therefore systems theory recasts the remaining question as:

\[
\boxed{
\text{Can SOURCE-II supply a lawful contour-scale bound on the
pole-removed transfer sufficient to control its semigroup/exponential
functional?}
}
\]

This is stronger than finitely many derivative-critical rows and is not
excluded by NJDG-6.

It is also not currently in custody.

## 13. IRT-0D matrix

| Route | Exactness | Data required | Canonical disposition |
|---|---|---|---|
| finite ordinary Loewner | exact for finite rational transfer with enough samples | rank-scale sample set | critical-frame/rank debt unresolved |
| actual-spectrum polynomial interpolation | exact on one fixed finite spectrum | actual complement nodes | complement-adaptive / not automatically lawful |
| structured delay realization | exact within prescribed structure class | known exponential/delay basis + samples | structure baked in |
| finite Loewner on irrational target | rational interpolant/approximation | finite samples | not exact |
| infinite-dimensional semigroup realization | exact | generator/realization known | representation, not identification |
| Hille--Yosida/Kreiss/inverse Laplace | exact/quantitative semigroup control | continuum resolvent control | new theorem class, input unavailable |

## 14. Determination

IRT-0D does not produce a finite-data bypass.

It does produce an exact structural identification:

\[
\boxed{
\text{RENJET exponential response}
=
\text{semigroup / matrix-function observable},
}
\]

while

\[
\boxed{
\text{derivative-critical rows}
=
\text{resolvent observations}.
}
\]

The missing bridge is therefore a recognizable systems-theory problem:

\[
\boxed{
\text{resolvent observations}
\longrightarrow
\text{semigroup observable}.
}
\]

Finite rows require realization-rank data and conditioning already missing in
NJDG. Standard rank-independent bridges require continuum resolvent control.

This is a materially sharper formulation of the NEXTJET deficit.

## 15. Cursor

\[
\boxed{
\texttt{IRT-0D1 / RESOLVENT-TO-SEMIGROUP CONTINUUM-CONTROL SCREEN}
}
\]

Questions:

1. can the canonical pole-removed zeta transfer be bounded on a contour/strip
   strongly enough for an inverse-Laplace or semigroup theorem;
2. can such a contour bound be obtained from existing actual-zeta estimates
   without assuming RH or the desired KPH floor;
3. does contour control of the transfer give the exact frozen
   \(K_t(A_\Omega)\) / RENJET functional with acceptable projective constants;
4. or does the required contour bound reduce exactly to the existing
   SOURCE-II complement-field obligation?

No canonical theorem status changes.
