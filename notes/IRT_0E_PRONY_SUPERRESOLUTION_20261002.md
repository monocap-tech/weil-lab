# IRT-0E — moment / Prony / super-resolution screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0D1  
**Status:** **COMPLETE PRIMARY SCREEN / EXACT NOISELESS PRONY RECOVERY FORMALLY MATCHES THE HIGHER-RESOLVENT TOWER / SOURCE-II DOES NOT EXPOSE THE REQUIRED MOMENTS INDEPENDENTLY / FIXED-ORDER JETS DO NOT PAY THE PRONY RANK DEBT / COLLISION-SAFE UNIQUENESS DOES NOT PAY THE STABILITY DEBT / NO NEW NEXTJET CLOSURE / NEXT CURSOR IRT-0F CROSS-ARCHITECTURE SYNTHESIS**

## 0. Objective

IRT-0E asks whether the moment/Prony/super-resolution family supplies the
missing theorem type:

\[
\text{finite/growing local observations}
\Longrightarrow
\text{exact or stable recovery of the exponential near population}
\]

without requiring the packet separation/transversality floor that NEXTJET is
supposed to prove.

This family is formally closer than ordinary finite interpolation because
classical Prony reconstruction is nonlinear and can recover exponential nodes
from moments exactly.

The screen finds a real match, but it does not close the canonical interface.

## 1. Classical Prony exactness

For a finite exponential sum

\[
m_k
=
\sum_{j=1}^{n}a_jx_j^k,
\qquad
k=0,\ldots,2n-1,
\]

the classical Prony map reconstructs the nodes \(x_j\) and amplitudes \(a_j\)
under the standard nondegenerate exact-data hypotheses.

Equivalently, the moments satisfy an order-\(n\) annihilating recurrence whose
characteristic polynomial has roots \(x_j\).

This is the finite-rate-of-innovation principle in signal-processing language:
a finite stream of Diracs can be reconstructed from a number of suitable exact
measurements commensurate with its number of degrees of freedom.

The essential point for IRT is:

\[
\boxed{
\text{finite exact nonlinear reconstruction can produce exponential
structure without a universal finite linear span identity.}
}
\]

Therefore NJDG-6's finite-linear-span obstruction does not rule out Prony-type
nonlinear reconstruction in principle.

## 2. SOURCE-II contains a formal Prony sequence

SOURCE-II-4 has the equivalent higher-resolvent form

\[
\mathfrak J_r
=
S_r(x,v)\psi^{(r+1)}(c)
+
\frac{M_r}{r!}(\psi B_F)^{(r)}(c)
+
M_r
\sum_{\mu\in\Omega}
m_\mu
\frac{\psi(\mu)}{(\mu-c)^{r+1}}.
\]

For fixed selector \(\psi\), define

\[
y_\mu=(\mu-c)^{-1}
\]

and

\[
a_\mu
=
m_\mu\psi(\mu)(\mu-c)^{-1}.
\]

Then the explicit near higher-resolvent sequence is

\[
\boxed{
S_r^\Omega(\psi)
=
\sum_{\mu\in\Omega}
a_\mu y_\mu^r.
}
\]

So the near-divisor part of the SOURCE-II tower is literally a Prony
exponential-moment sequence in the reciprocal coordinate.

This is a genuine formal match, not an analogy.

## 3. First obstruction: the Prony moments are not independent observations

The canonical data supplied by SOURCE-II are the **joint finite-part jets**
\(\mathfrak J_r\), not the isolated sequence \(S_r^\Omega\).

The same formula contains

\[
\frac{M_r}{r!}(\psi B_F)^{(r)}(c).
\]

Here

\[
B_F(z)
=
\frac{\Xi'}{\Xi}(z)
-
\sum_{\rho\in F}\frac1{z-\rho}
\]

still contains the unselected divisor, including the near poles in \(\Omega\).

The explicit reciprocal sum and the \(B_F\) derivative are therefore not two
independent measurements. They form the collision-safe finite-part
combination already constructed by SOURCE-II.

To feed classical Prony inversion one would need to isolate

\[
S_r^\Omega(\psi).
\]

Doing so requires independent knowledge of the \(B_F\)/outside-field
contribution or an equivalent decomposition theorem.

Thus:

\[
\boxed{
\text{Prony moment extraction}
\Longrightarrow
\text{independent complement-field knowledge}.
}
\]

That is exactly the existing NEXTJET debt.

## 4. Second obstruction: exact reconstruction has rank-scale data cost

Suppose, artificially, that the isolated moments
\(S_r^\Omega(\psi)\) were available.

If the reciprocal near measure has \(n\) distinct support nodes, generic exact
Prony recovery requires a number of exact moments commensurate with \(n\);
classically the \(2n\)-moment system is the basic square reconstruction model.

SOURCE-II-4 proves something different:

> for every **fixed** order \(K\), a collision-safe jet tower gives any
> preassigned fixed polylogarithmic truncation accuracy.

It does not provide:

- a uniform fixed upper bound on \(n=|\Omega|\) for every admissible packet;
- a theorem allowing \(K\) to grow with the actual Prony rank with all constants
  and covariance controls uniform in that growth;
- a rank-adaptive data acquisition mechanism independent of the complement.

Indeed the authorized mesoscopic block obeys only the general upper estimate

\[
N_\Omega\ll (R+1)L,
\]

and SOURCE-II's error-balancing choice

\[
R=L^{K/2}
\]

makes the admissible block size potentially grow with the same truncation
parameter.

This does not prove that every actual block realizes the upper bound. It does
show that the current theorem gives no uniform fixed-rank model on which a
fixed-order Prony inversion can be licensed packetwise.

Thus exact Prony recovery incurs a **rank debt** not paid by arbitrary
fixed-order asymptotics.

## 5. Collision does not destroy exact uniqueness

One tempting objection to Prony is minimum separation.

For exact noiseless algebraic recovery, separation is not fundamentally
required in the same way it is for stable numerical recovery.

The confluent Prony formalism treats collided nodes by incorporating
multiplicity/derivative information, and modern separation-free
super-resolution results show that finite sparse source locations can be
uniquely recovered from finitely many exact observations under suitable
waveform/model hypotheses even when the points are arbitrarily close.

Therefore:

\[
\boxed{
\text{“nodes may collide”}
}
\]

is not, by itself, an exact-identifiability no-go.

That is an important correction to any overly strong separation argument.

## 6. Stability is the actual collision obstruction here

SOURCE-II does not supply exact infinite moment data.

Its finite-order normal form has a nonzero remainder:

\[
\mathcal P_v[\psi]+\mathcal A_v[\psi]
=
\sum_{r=1}^{K}L^{-r}\mathfrak J_r
+
O_K(L^{-K/2})
\]

after the canonical mesoscopic balance.

Therefore the relevant reconstruction theorem must be **stable**, not merely
unique.

Near-colliding Prony nodes make the inverse moment map badly conditioned.
The confluent-Prony literature expresses local reconstruction accuracy in terms
of the geometry of the nodes, and modern super-resolution bounds show
polynomial deterioration in the super-resolution factor with exponent
controlled by cluster size.

For a cluster of \(p\) nodes, representative minimax/Prony bounds deteriorate
at powers comparable to \(SRF^{2p-1}\), where \(SRF\) is inverse bandwidth
times inverse minimum separation.

Hence a truncation error that is harmless for a well-separated packet can be
amplified catastrophically by an arbitrarily tight cluster.

No retained theorem supplies the corresponding packetwise lower separation or
condition-number floor.

Thus:

\[
\boxed{
\text{collision-safe exact representation}
\ne
\text{stable inverse reconstruction}.
}
\]

## 7. Positive-measure separation-free theorems do not transfer directly

Some super-resolution results exploit positivity of the unknown measure or
special totally-positive measurement kernels to obtain uniqueness/recovery
without a minimum-separation hypothesis.

That architecture is not directly available here.

In the reciprocal Prony coordinate,

\[
y_\mu=(\mu-c)^{-1}
\]

may be complex in the false-RH setting, and the effective amplitudes

\[
a_\mu
=
m_\mu\psi(\mu)(\mu-c)^{-1}
\]

are generally complex even though the multiplicities \(m_\mu\) are positive
integers.

Therefore the near-divisor reconstruction is not a positive atomic measure on
a real compact interval in the sense required by the strongest
positivity-based super-resolution theorems.

Importing those theorems would require a new positivity transform, which is
not presently in custody.

## 8. Functional recovery without node recovery

IRT does not actually need to recover every \(\mu\) if the target is only

\[
Q_t(\Omega)
=
\sum_{\mu\in\Omega}m_\mu K_t(\mu-c).
\]

Could finitely many moments determine this functional directly?

For a uniformly bounded-rank atomic class, yes in principle: once the
annihilating recurrence is known, any analytic functional of the recovered
nodes can be evaluated.

Without a uniform rank bound, however, finitely many truncated moments have a
nontrivial nullspace.

If measured kernels span only

\[
1,w,\ldots,w^K
\]

(or the corresponding reciprocal powers), and \(f(w)\) is not in that finite
span, then one can choose a finite signed atomic configuration annihilating all
measured moments while having nonzero \(f\)-functional.

Since the RENJET kernel \(K_t(w)\) is nonpolynomial entire, no fixed finite
moment set determines it uniformly over atomic measures of unbounded rank.

This is the moment-theoretic version of NJDG-6.

## 9. Polynomial/entire approximation is already SOURCE-II-type representation

One can approximate the entire kernel \(K_t\) uniformly on a bounded domain by
a finite polynomial and then evaluate that polynomial from finitely many power
moments.

But SOURCE-II already supplies arbitrary fixed-order Taylor/jet normal forms to
any preassigned fixed polylogarithmic accuracy.

Thus the statement

\[
\text{entire target}
\approx
\text{finite moment polynomial}
\]

is not new arithmetic input.

Without an independent sign/bound theorem for the moments, approximation only
repackages the existing finite jet tower.

## 10. Exact comparison with the existing routes

The Prony architecture maps onto the project as follows:

\[
\begin{aligned}
\text{Prony nodes}
&\leftrightarrow
(\mu-c)^{-1},
\\
\text{Prony moments}
&\leftrightarrow
\text{higher-resolvent near statistics},
\\
\text{annihilating polynomial}
&\leftrightarrow
\text{actual near-divisor polynomial},
\\
\text{moment rank}
&\leftrightarrow
\text{near-block cardinality/multiplicity rank},
\\
\text{Vandermonde conditioning}
&\leftrightarrow
\text{near-zero collision geometry},
\\
\text{measurement noise}
&\leftrightarrow
\text{finite SOURCE-II truncation/far-tail remainder}.
\end{aligned}
\]

Every useful exact/stable reconstruction theorem requires one of:

1. independently observable moments;
2. a rank/sparsity bound;
3. sufficient growing data order;
4. a separation/cluster-conditioned error budget;
5. positivity or another structural prior.

None is currently supplied in the required canonical form.

## 11. IRT-0E matrix

| Route | Exact uniqueness | Stable through collisions | Required input | IRT disposition |
|---|---:|---:|---|---|
| classical Prony | yes, finite rank | conditioning can be poor | about \(2n\) exact moments | rank + observability debt |
| confluent Prony | yes with multiplicities | geometry-dependent | confluent exact moments | stability debt |
| separation-free sparse recovery | yes under special kernels/models | theorem-specific | known sparsity and exact/special measurements | model mismatch |
| clustered super-resolution | quantitative | degrades with cluster/SRF | bandwidth + separation/cluster control | missing packet floor |
| positive-measure methods | often stronger | may avoid separation in special cases | positivity/real support | false-RH reciprocal data complex |
| finite moment functional recovery | only with bounded model class | no uniform unbounded-rank theorem | rank/structure | truncated-moment nullspace |
| polynomial approximation | approximate | stable as approximation | moment bounds | already SOURCE-II representation |

## 12. Determination

IRT-0E does locate a true non-number-theoretic analogue of the higher
resolvent tower:

\[
\boxed{
\text{SOURCE-II near higher resolvents}
=
\text{a reciprocal-coordinate Prony moment sequence}.
}
\]

But this does not yield a new canonical estimate because the moment sequence is
not independently observed; it is embedded in the same joint finite-part field
whose complement component remains uncontrolled.

Even granting an oracle for the moments, exact recovery incurs a rank-scale data
cost, and stable recovery through near-collisions incurs precisely the
conditioning/separation debt that the canonical branch lacks.

Thus Prony does not supply the missing theorem. It explains its information
content.

## 13. Cursor

The five major foreign architectures opened by IRT-0 have now been screened:

1. Weyl/Herglotz/two-spectra;
2. generalized Nevanlinna/Pontryagin, including local \(\pi_+\);
3. canonical systems/de Branges and Suzuki shift flow;
4. systems/Loewner/semigroup/contour realization;
5. moment/Prony/super-resolution.

The next pass should no longer open another adjacent representation formalism
without synthesis.

\[
\boxed{
\texttt{IRT-0F / CROSS-ARCHITECTURE SYNTHESIS + NEW-THEOREM-TYPE EXTRACTION}
}
\]

Primary objective:

> identify the minimal structural ingredient common to the foreign theories
> that actually succeed at zero/pole or resolvent/exponential transfer, and
> state the weakest theorem type not already equivalent to a canonical
> complement-field/KPH obligation.

No canonical theorem status changes.
