# Weil-Defect Theory: Screening, Persistence, and Zeta-Weil Morphology

> Public technical manuscript — Horizon 1.
>
> Mathematical statements are indexed by stable `WD-Txx` identifiers.
> Mathematical standing, formal verification status, and imported-source
> custody are separate axes.  The public verification matrix records the
> formal axis; the theorem ledger and proof-status surfaces remain the
> canonical detailed sources.

## Abstract

We develop an operator-theoretic defect calculus for indefinite coefficient
spaces and use it to organize the sign geometry underlying finite Weil
defects.  The basic object is the physical defect
[
D=S_{+}S_{+}^{*}-S_{-}S_{-}^{*},
]
whose negative index agrees with the negative index of the associated
coefficient-space Krein form.  Nonnegativity of (D) is equivalent, through
Douglas factorization, to contractive screening of the negative synthesis
through the positive synthesis.  This produces a complete abstract screening
taxonomy, including strictly screened, over-budget, attained-critical, and
non-attained critical regimes.

The calculus is stable under selected/background decompositions and legitimate
background elimination.  For a fixed finite selected negative sector, the
finite-dimensional compactness of that sector forces any normalized critical
or negative right-approaching sequence to retain a nonzero nonpositive
right-limit ray.  At criticality there are only two fixed-sector outcomes:
an attained neutral limit or a strictly negative fall-through caused by loss
of positive-coordinate norm.  Moving selected sectors and unselected
backgrounds are therefore separate noncompactness mechanisms rather than
additional fixed-packet branches.

We then specialize this structure to the zeta-Weil setting.  Conjugate-pair
geometry, finite Weil inertia, distinct-frequency rigidity, and selected
residue structure imply a zero-moment law
[
mathbf 1^{T}v=0
]
for selected negative raw residues.  Consequently the associated rational
response has universal inverse-square far decay,
[
R_v(z)=O(|z|^{-2}),
]
which is sharp under zero moment alone.  Combining this with unit-height zeta
zero counting gives an explicit-formula far complementary tail
[
O!left(rac{log R}{R}ight).
]
The surviving near field is a weighted completed-(Xi) next-jet field.
At fixed compact support, only finitely many prime-power translations are
active and the compact-window operator has logarithmic principal order,
[
Psi_c(t)=log|t|+O_c(1),
]
with no automatic positive-Sobolev coercive upgrade.

These ingredients assemble into three morphology classes: persistent selected
negative defect, attained unit-gain neutral defect, and noncompact
moving/background morphology.  The first two terminate at explicit
actual-zeta interfaces,
[
	exttt{AZ-NEXTJET-LOC},
qquad
	exttt{AZ-FIN-WEIL-NULL-EXTENSION},
]
with (	exttt{C-ACTUAL-KPH-FLOOR}) retained as a stronger special-packet
refinement on the negative side.  Horizon 1 proves the independent
Weil-defect theory that reaches these interfaces; it does not prove the
interfaces themselves and does not claim RH closure.

---

# Part I. Abstract Weil-defect calculus

## 1. Coefficient space, synthesis, and physical defect

Let
[
mathcal H,qquad K_{+},qquad K_{-}
]
be complex Hilbert spaces and let
[
S_{+}:K_{+}	omathcal H,
qquad
S_{-}:K_{-}	omathcal H
]
be bounded synthesis operators.  On
[
K_{+}oplus K_{-}
]
use the fundamental symmetry
[
J=
egin{pmatrix}
I&0\
0&-I
end{pmatrix},
qquad
[(x,u),(y,v)]_J
=
langle x,yangle-langle u,vangle.
]

Define
[
E(x,u)=S_{+}x+S_{-}u,
qquad
mathcal A=(ker E)^perp
=overline{operatorname{Ran}E^{*}},
]
and define the physical defect
[
oxed{
D=EJE^{*}
=S_{+}S_{+}^{*}-S_{-}S_{-}^{*}.
}
]

### WD-T01 — Defect identity and index transfer

For every (hinmathcal H),
[
E^{*}h=(S_{+}^{*}h,S_{-}^{*}h)
]
and
[
oxed{
[E^{*}h,E^{*}h]_J
=
langle Dh,hangle.
}
]

Hence
[
oxed{
mathcal A	ext{ is }J	ext{-nonnegative}
iff
Dsucceq0
}
]
and, more generally,
[
oxed{
operatorname{ind}_{-}(mathcal A,J)
=
operatorname{ind}_{-}(D).
}
]

The equality of indices is the first custody principle of the theory:
coefficient-space negativity and physical-space negativity are two
representations of the same finite-dimensional obstruction.

### WD-T02 — Contractive screening

The following are equivalent:
[
Dsucceq0,
qquad
S_{-}S_{-}^{*}preceq S_{+}S_{+}^{*},
]
and the existence of a contraction
[
X:K_{-}	o K_{+}
]
such that
[
oxed{
S_{-}=-S_{+}X.
}
]

This is the unit-majorization case of the Douglas factorization theorem.
The reduced solution is the canonical representative used throughout the
screening calculus.  The external Douglas theorem is a load-bearing imported
input; its exact pin is recorded as EXT-1 in
[Imported Source Pins](IMPORTED_SOURCE_PINS.md).

The interpretation is direct: a nonnegative defect means every negative
synthesis channel can be reproduced through the positive synthesis without
exceeding unit coefficient norm.

### WD-T03 — Reduced graph normal form

Assume exact range inclusion
[
operatorname{Ran}S_{-}
subseteq
operatorname{Ran}S_{+}
]
and let (X) be the Douglas reduced solution of
[
S_{+}X=-S_{-}.
]
No contractivity assumption is needed.

Then
[
oxed{
mathcal A
=
{(a,-X^{*}a):
ain(ker S_{+})^perp}.
}
]
On this graph,
[
oxed{
[(a,-X^{*}a),(a,-X^{*}a)]_J
=
|a|^{2}-|X^{*}a|^{2}.
}
]
The physical defect factors as
[
oxed{
D=S_{+}(I-XX^{*})S_{+}^{*}.
}
]

Thus, after the unscreened range-defect case is separated, the sign problem
is reduced to the norm geometry of the reduced screening map.

### WD-T04 — Complete screening taxonomy

The reduced solution gives five basic regimes.

1. **Range defect.** If
   [
   operatorname{Ran}S_{-}
otsubseteqoperatorname{Ran}S_{+},
   ]
   exact screening does not exist and (D
otsucceq0).

2. **Over-budget defect.** If range inclusion holds but
   [
   |X|>1,
   ]
   then (mathcal A) contains a strictly negative vector.

3. **Strictly screened regime.** If
   [
   |X|=r<1,
   ]
   then
   [
   oxed{
   [y,y]_J
   ge
   rac{1-r^{2}}{1+r^{2}}|y|^{2}
   qquad(yinmathcal A).
   }
   ]

4. **Attained critical regime.** If
   [
   |X|=1
   ]
   and (X^{*}) attains its norm, then (mathcal A) contains a nonzero
   neutral vector.

5. **Non-attained critical regime.** If
   [
   |X|=1
   ]
   but no nonzero norm-attaining vector exists, then every nonzero vector of
   (mathcal A) is strictly positive while a normalized sequence can have
   (J)-margin tending to zero.

The final case is essential in infinite dimension.  It prevents the critical
boundary from being collapsed into a simple positive/neutral dichotomy.

### WD-T05 — Rank-one specialization

If (K_{-}=mathbb C) and
[
S_{-}alpha=alpha g,
]
then
[
S_{-}S_{-}^{*}=gotimes g
]
and
[
oxed{
D=S_{+}S_{+}^{*}-gotimes g.
}
]

Therefore (Dsucceq0) is equivalent to the existence of
(cin K_{+}) with
[
g=-S_{+}c,
qquad
|c|le1.
]
The one-negative-channel defect used in the Weil traversal is therefore not a
special ad hoc mechanism; it is the rank-one case of the abstract calculus.

---

## 2. Positive restoration and selected/background custody

### WD-T06 — Monotone positive screening

Let (P_N) be increasing orthogonal projections on (K_{+}) with
[
P_N	o I
]
strongly, and define
[
D_N
=
S_{+}P_NS_{+}^{*}-S_{-}S_{-}^{*}.
]
Then
[
oxed{
D_Npreceq D_{N+1}preceq D,
qquad
D_N	o D	ext{ strongly}.
}
]
Consequently
[
oxed{
operatorname{ind}_{-}(D_N)
ge
operatorname{ind}_{-}(D_{N+1}).
}
]

Negative directions can disappear as more positive screening channels are
restored.  WD-X01 shows that this can happen completely: every finite
truncation may be strictly negative even though the full defect is zero.

Now split the negative coefficient space as
[
K_{-}=Moplus B,
]
where (M) is a selected negative sector and (B) is the unselected negative
background.  Write
[
S_M=S_{-}P_M,
qquad
S_B=S_{-}P_B.
]

### WD-T07 — Selected/background monotonicity and custody

With
[
D_M
=
S_{+}S_{+}^{*}-S_MS_M^{*}
]
and
[
D_{m full}
=
S_{+}S_{+}^{*}
-S_MS_M^{*}
-S_BS_B^{*},
]
one has
[
oxed{
D_{m full}preceq D_M.
}
]
Thus
[
oxed{
	ext{selected negativity}
Longrightarrow
	ext{full negativity}.
}
]

The converse is false.  Aggregate negativity does not identify which negative
sector owns the defect.  This asymmetry is a permanent custody rule.

### WD-T08 — Finite selected-sector index cap

If
[
m=dim M<infty,
]
then
[
oxed{
operatorname{ind}_{-}(D_M)le m.
}
]
If (B) is also finite dimensional, with (dim B=b), then
[
operatorname{ind}_{-}(D_{m full})
le
operatorname{ind}_{-}(D_M)+b.
]

A fixed finite selected sector can therefore generate only finitely many
independent negative directions.

### WD-T09 — Shared screening budget

Assume the full negative synthesis is exactly contained in the positive range
and let
[
X=[X_M;X_B]
]
be the reduced screening map.  Then
[
oxed{
D_{m full}
=
S_{+}
igl(I-X_MX_M^{*}-X_BX_B^{*}igr)
S_{+}^{*}.
}
]
Therefore
[
oxed{
D_{m full}succeq0
iff
X_MX_M^{*}+X_BX_B^{*}preceq I.
}
]

Separate bounds
[
|X_M|le1,
qquad
|X_B|le1
]
are not enough.  Screening is a joint resource-allocation problem.  WD-X03
gives the one-dimensional counterexample in which each channel is separately
screenable but the pair exceeds the shared unit budget.

---

## 3. Background elimination, inertia, and shorting

### WD-T10 — Residual positive synthesis

Assume the background is contractively screened,
[
S_B=-S_{+}X_B,
qquad
|X_B|le1.
]
Define
[
R_B=I-X_BX_B^{*}succeq0
]
and
[
S_{m eff}=S_{+}R_B^{1/2}.
]
Then
[
oxed{
D_{m full}
=
S_{m eff}S_{m eff}^{*}
-S_MS_M^{*}.
}
]

Legitimate elimination of a screened background returns the problem to the
same two-channel defect calculus.  The selected sector must fit inside the
residual positive budget left after the background has been paid for.

### WD-T11 — Finite-sector singular-value inertia

For fixed finite-dimensional (M), let (Y) denote the reduced residual
screening map for
[
S_M=-S_{m eff}Y.
]
Then the selected negative index and neutral dimension are counted by the
singular values of (Y):
[
oxed{
operatorname{ind}_{-}
=
#{j:sigma_j(Y)>1},
}
]
[
oxed{
operatorname{nul}_{J}
=
#{j:sigma_j(Y)=1}.
}
]

The critical boundary is therefore a unit-singular-value boundary for the
finite selected sector.

### WD-T12 — Sequential background consumption

Background elimination can be iterated.  Each legitimately screened
background channel consumes part of the positive covariance and leaves a new
residual budget operator.  The resulting selected problem remains inside the
same defect calculus.  This closure property is what allows multi-stage
screening to be analyzed without changing category.

### WD-T13 — Shorted covariance

When the positive covariance is decomposed with respect to a selected positive
subspace and a uniformly positive complementary block, eliminating the
complement replaces the direct selected compression by the Schur/shorted
covariance
[
oxed{
H_W=A-BC^{-1}B^{*}.
}
]
The correction is positive, so
[
H_Wpreceq A.
]

A lower bound on the direct compression alone does not yield a uniform
family-level lower bound after shorting.  WD-X04 gives the exact (2	imes2)
family
[
K_r=
egin{pmatrix}
1&r\
r&1
end{pmatrix}
]
for which the direct compression remains (1) while the shorted covariance
is (1-r^{2}downarrow0).

### WD-T14 — Finite positive shadows

Finite positive projections preserve an already-established algebraic
negative margin, but they need not preserve membership in the relevant
analysis space.  Therefore a finite positive shadow can expose the sign of a
selected ray without supplying the graph/admissibility relation that made the
ray physically meaningful.

This separates **visibility of negativity** from **custody of the analysis
relation**.

---

## 4. Support filtration and fixed-sector persistence

Let
[
mathcal A_ssubseteqmathcal A_t
qquad(s<t)
]
be a monotone family of closed analysis spaces.  At an endpoint (c), define
the right-limit space
[
oxed{
mathcal A_{c+}
=
igcap_{t>c}mathcal A_t
}
]
and the endpoint gap
[
oxed{
mathcal J_c
=
mathcal A_{c+}ominusmathcal A_c.
}
]

### WD-T15 — Right-limit projection and gap duality

Along any sequence (t_ndownarrow c), the monotone family of orthogonal
projections converges to the projection onto (mathcal A_{c+}).  The
right-limit gap is therefore the geometric carrier for vectors that appear
arbitrarily close to the endpoint but are absent at the endpoint itself.

This turns endpoint persistence into a closed-subspace limit problem rather
than a pointwise heuristic.

### WD-T16 — Fixed finite negative-sector persistence

Suppose the negative coordinate is restricted to a fixed finite-dimensional
selected sector (M), and let
[
y_n=(a_n,u_n)
]
be normalized vectors approaching the endpoint from the right with
[
[y_n,y_n]_J	o q_{*}le0.
]
After passage to a subsequence, finite-dimensional compactness gives
[
u_n	o u
]
strongly, while boundedness gives
[
a_nightharpoonup a
]
weakly.  The limiting vector
[
y=(a,u)
]
belongs to (mathcal A_{c+}).

The key estimate is
[
|a|^{2}-|u|^{2}
le
liminf_{n	oinfty}
igl(|a_n|^{2}-|u_n|^{2}igr)
=
q_{*}.
]
Normalization and (q_{*}le0) force (u
eq0), hence (y
eq0).  Therefore
[
oxed{
	ext{fixed finite selected sector}
+
q_{*}le0
Longrightarrow
exists,0
eq yinmathcal A_{c+}
	ext{ with }[y,y]_Jle q_{*}.
}
]

If the approaching sequence has a uniform negative margin, the limiting ray
remains strictly negative.

### WD-T17 — Critical dichotomy

At criticality,
[
[y_n,y_n]_J	o0.
]
There are exactly two fixed-sector mechanisms.

If
[
|a_n|	o|a|,
]
then weak convergence of (a_n) upgrades to strong convergence and the limit
is neutral:
[
[y,y]_J=0.
]

If positive-coordinate norm is lost,
[
lim|a_n|^{2}>|a|^{2},
]
then the retained selected negative coordinate forces
[
oxed{
[y,y]_J<0.
}
]

Thus weak convergence at criticality does not preserve neutrality.  WD-X06
realizes this fall-through explicitly with
[
y_n=
left(
rac1{sqrt2}e_n,rac1{sqrt2}
ight)
ightharpoonup
left(
0,rac1{sqrt2}
ight).
]

### WD-T18 — Endpoint-jump index control

New right-limit negative directions are carried by the endpoint quotient.
The negative index contributed at the endpoint is bounded by the dimension of
the right-limit gap quotient.  In the one-dimensional jump case this gives a
one-direction rank cap.

### WD-T19 — Boundary amplification

If a new right-limit vector is genuinely absent from the endpoint space, then
normalized endpoint representatives cannot remain uniformly controlled.
Equivalently, vanishing endpoint amplitude requires representative blow-up.

This is the geometric boundary-amplification mechanism used later in the
negative and neutral morphology packages.

### Part I summary

Part I establishes the central structural theorem:
[
oxed{
egin{array}{c}
	ext{fixed finite selected sector}\
+ 	ext{critical or negative right approach}
end{array}
Longrightarrow
	ext{nonzero nonpositive right-limit ray}.
}
]

The non-attained critical branch of WD-T04 remains possible in infinite
dimension globally, but WD-X05 shows why it cannot be realized by a single
fixed finite selected sector whose negative mass stays anchored: the sector
itself must move or become infinite-dimensional.

---

# Part II. Zeta-Weil specialization

## 5. Pair geometry, inertia, and multiplicity

The zeta-Weil specialization identifies the abstract positive and negative
channels using conjugate-pair geometry of the divisor.

### WD-T20 — Pair diagonalization

Each nonreal conjugate-pair block admits a canonical positive/negative
diagonalization.  This provides the coefficient-space (J)-splitting used by
the abstract defect calculus.

### WD-T21 — Simple quartet geometry

A simple off-critical functional-equation quartet contributes two distinct
nonreal conjugate-pair coordinates to the negative side.  This is a geometric
count before multiplicity-null directions are removed.

### WD-T22 — Finite Weil inertia

Bombieri's finite Weil theorem identifies the number of negative eigenvalues
with the number of distinct nonreal conjugate pairs.  Horizon 1 consumes this
as an imported theorem plus exact specialization; the source is pinned as
EXT-2A.

Thus the abstract finite selected-sector negative-index cap is saturated by
the actual finite Weil pair geometry.

### WD-T23 — Multiplicity-null directions

Repeated ordinates create zero directions rather than additional independent
negative channels.  These multiplicity-null directions must be quotiented
before independent finite negative-index counting.  The load-bearing external
input is Bombieri's multiplicity result, pinned as EXT-2B.

The distinction between **pair multiplicity** and **independent negative
channel count** is fixed from this point forward.

---

## 6. Frequency rigidity and zero-moment residues

### WD-T24 — Finite distinct-frequency independence

A finite linear combination of distinct exponential modes cannot vanish on a
nonempty interval unless all coefficients vanish.  This is an internal
finite-frequency rigidity theorem and supplies the local injectivity needed
for the finite selected packet.

### WD-T25 — No exact finite positive compensation

For an anchored selected negative cell, no finite positive combination of the
retained distinct-frequency Problem-1 modes can exactly reproduce the selected
negative synthesis relation.  This prevents a finite positive helper set from
trivially annihilating the selected defect.

### WD-T26 — Zero-moment law

For the raw residues associated with a selected negative pair combination,
the residue coefficients satisfy
[
oxed{
mathbf 1^{T}v=0.
}
]

This identity is not an imposed cancellation.  It is inherited from the
selected pair structure.  It becomes the arithmetic entry point for the
far-field analysis.

---

## 7. Rational response and native compactness

Define the selected rational response
[
R_v(z)=sum_jrac{v_j}{z-ho_j}.
]

### WD-T27 — Universal inverse-square far decay

Expanding at infinity,
[
rac1{z-ho_j}
=
rac1z+rac{ho_j}{z^{2}}+O(|z|^{-3}),
]
so the zero-moment identity kills the (z^{-1}) term:
[
oxed{
mathbf 1^{T}v=0
Longrightarrow
R_v(z)=O(|z|^{-2}).
}
]

WD-X07 shows sharpness.  For (v=(1,-1)) at two distinct points,
[
R_v(z)
=
rac{ho_1-ho_2}
{(z-ho_1)(z-ho_2)}
sim
rac{ho_1-ho_2}{z^{2}}.
]
No universal (O(|z|^{-3})) improvement follows from zero moment alone.

### WD-T28 — Native Problem-1 compactness

The native Problem-1 zero synthesis is Hilbert-Schmidt, and the corresponding
off-axis helper covariance is trace class.  The proof uses the native
Dirichlet-resolvent energy together with unit-height zeta zero counting.
The zero-count input is the imported theorem pinned as EXT-3.

The consequence is metric-specific: native compactness does not license an
unweighted sampling/frame conclusion.  This distinction is retained as a
scope rule in the public package.

### WD-T29 — Finite-head approximation

A bounded-budget infinite-helper target can be approximated quantitatively by
a finite head.  This is the correct finite reduction supplied by compactness:
one gets approximation with controlled tail error, not an exact finite
replacement unless additional structure is available.

---

## 8. Explicit-formula arithmetic

### WD-T30 — Two-mode selected-preserving multiplier

For two selected modes there exists a scalar multiplier that preserves the
selected conditions while allowing one complementary mode to be cancelled.
The construction is finite and exact.  It is used as a local algebraic tool,
not as a global uniform annihilator.

### WD-T31 — Far complementary tail

Combine
[
R_v(mu)=O(|mu|^{-2})
]
with the unit-height zero count
[
N(T+1)-N(T)=O(log T).
]
Shell summation yields
[
sum_{nge R}rac{log n}{n^{2}}
=
O!left(rac{log R}{R}ight),
]
and hence
[
oxed{
mathcal F_{v,R}[psi]
=
O!left(rac{log R}{R}ight)
}
]
for the far complementary field under the stated bounded multiplier
hypotheses.

The estimate is downstream from the imported zero-counting premise; Lean
certifies the shell deduction from an explicit formal premise, not the
external zero-count theorem itself.

### WD-T32 — Weighted completed next-jet field

After the far tail is separated, the near complementary response is represented
by a weighted next-jet of the completed (Xi)-function:
[
oxed{
mathcal N_{v,R}[psi]
=
sum_{mu}^{m near}
m_mupsi(mu)
rac{H_v^{(m_mu)}(mu)}
{Xi^{(m_mu)}(mu)}.
}
]

This is the finite/intermediate field that survives the zero-moment far-field
gain.  It is the arithmetic object encountered by the persistent negative
morphology.

### WD-T33 — Adaptive cocancellation does not remove the obstruction

At a fixed cutoff, one may choose an adaptive scalar to cancel a selected
near-minus-archimedean contribution.  The corresponding prime term then
collapses onto the far term.  The maneuver therefore reallocates the explicit
formula rather than producing a source-free uniform lower bound.

This is why an adaptive scalar is not a bypass of the next-jet obstruction.

### WD-T34 — Finite prime-power translations

For compact support radius (c), the compact-window explicit formula activates
only prime powers satisfying
[
oxed{
log n<2c.
}
]
The set is finite.  At a threshold
[
2c=log n_0,
]
the source convention is strict at (c), while the threshold term appears in
every sufficiently small strict right enlargement.  The right-limit
bookkeeping therefore differs from the endpoint by at most the finite
threshold contribution.

The compact-window formula is imported and source-pinned as EXT-4.

### WD-T35 — Logarithmic form order

The archimedean multiplier satisfies
[
Repsi!left(rac14+rac{it}{2}ight)
=
log|t|+O(1),
]
using the digamma asymptotic pinned as EXT-5.  The active prime contribution is
a finite bounded trigonometric polynomial.  Therefore
[
oxed{
Psi_c(t)=log|t|+O_c(1).
}
]

The compact-window Weil form has logarithmic Fourier/form order.

### WD-T36 — No free positive-Sobolev bootstrap

Logarithmic form control does not imply a uniform estimate by any fixed
positive-Sobolev weight.  Adding finitely many prime translations does not
change that principal order and supplies no smoothing.

Thus the neutral compact-window equation cannot be promoted automatically to
a positive-Sobolev or quasianalytic rigidity statement.

### Part II summary

The zeta-Weil specialization supplies the chain
[
oxed{
mathbf 1^{T}v=0
Longrightarrow
R_v(z)=O(|z|^{-2})
Longrightarrow
mathcal F_{v,R}
=
O!left(rac{log R}{R}ight),
}
]
leaving the weighted completed next-jet field as the near arithmetic
obstruction.  On the compact-window side, the operator has logarithmic
principal order plus finitely many arithmetic translations, with no hidden
regularity upgrade.

---

# Part III. Defect morphology

## 9. WD-T37 — Persistent selected negative morphology

Assume a fixed finite selected packet survives the right-limit process with a
strict negative margin.  By WD-T16 the selected negative coordinate has a
nonzero limit.  The normalized representative therefore retains selected
custody, while WD-T19 records the corresponding endpoint representative
blow-up when the ray is new at the boundary.

The zeta-Weil specialization then supplies:

1. a nonzero selected raw residue source;
2. the zero-moment law
   [
   mathbf1^{T}v=0;
   ]
3. inverse-square rational-response decay;
4. the shell estimate
   [
   O((log R)/R)
   ]
   for the far complementary field;
5. localization of the remaining arithmetic burden into the weighted near
   completed-(Xi) next-jet field.

Thus the public negative morphology is
[
oxed{
egin{aligned}
	ext{fixed-packet persistent negative defect}
&Longrightarrow
	ext{nonzero zero-moment selected source}\
&Longrightarrow
O(|z|^{-2})	ext{ far response}\
&Longrightarrow
O((log R)/R)	ext{ far field}\
&Longrightarrow
	ext{weighted near next-jet morphology}.
end{aligned}
}
]

The branch stops at
[
oxed{	exttt{AZ-NEXTJET-LOC}.}
]
Horizon 1 does not prove the actual-zeta localization/exclusion statement
needed beyond that stop.

The stronger
[
oxed{	exttt{C-ACTUAL-KPH-FLOOR}}
]
is retained as a special-packet sufficient refinement.  It is not silently
substituted for the primary interface and is not a theorem of Horizon 1.

---

## 10. WD-T38 — Attained unit-gain neutral morphology

Suppose the fixed selected critical branch is attained.  Then the residual
screening map has an actual unit-gain vector.  After the carrier identification
required by the theorem hypotheses, this produces a nonzero compact-window
null mode
[
oxed{
W_c k=0.
}
]

The compact-window arithmetic established in Part II gives:

- finitely many active prime-power translations;
- threshold-aware distinction between the endpoint and strict right limit;
- logarithmic principal Fourier/form order;
- no automatic positive-Sobolev coercive gain;
- global quadratic cancellation rather than termwise vanishing.

The neutral morphology therefore has the schematic form
[
oxed{
	ext{attained fixed-packet criticality}
+
	ext{carrier identification}
Longrightarrow
	ext{compact-window null mode of logarithmic order}.
}
]

The remaining question is whether the compact-window null mode can be extended
by zero while preserving the required operator equation through an exterior
collar, including the finite right-limit correction at thresholds.  This is
the open support interface
[
oxed{
	exttt{AZ-FIN-WEIL-NULL-EXTENSION}.
}
]

No unique-continuation, support-rigidity, or exterior-null theorem is imported
upstream of this stop line.

---

## 11. WD-T39 — Noncompact moving/background morphology

The fixed-packet negative and neutral branches do not exhaust all global
noncompact behavior.  WD-T39 separates three distinct custody questions.

### 11.1 Full-coordinate moving escape

For a uniformly bounded coefficient sequence, suppose every fixed block of a
self-adjoint finite-coordinate exhaustion tends to zero.  Then the entire
sequence converges weakly to zero:
[
oxed{
Q_R w_n	o0 	ext{for every fixed }R
Longrightarrow
w_nightharpoonup0.
}
]

This is a full-carrier statement.  Escape of selected negative coordinates
alone is insufficient if a positive block remains anchored.

### 11.2 Fixed selected-packet custody

If a fixed finite selected packet retains positive selected negative mass,
finite-dimensional compactness produces a strongly convergent subsequence of
that selected coordinate with nonzero limit.  Therefore full-coordinate
moving escape is impossible once the selected ray is genuinely anchored.

WD-X05 shows the sharp opposite situation: if the selected one-dimensional
sector itself moves through infinitely many coordinates, the nested tail
intersection can be trivial even though every stage contains a normalized
strictly negative vector with signature tending to zero.

### 11.3 Unselected-background compactness trichotomy

After a fixed selected negative ray has been anchored, let (b_n) denote the
normalized unselected negative background.  After passage to a subsequence,
one of three regimes occurs:
[
oxed{
egin{array}{ll}
mathbf{B_infty}:&
|b_n|	oinfty,\[1mm]
mathbf{B_T}:&
b_n	ext{ bounded with positive tail/weak norm loss},\[1mm]
mathbf{B_F}:&
b_n	o b	ext{ strongly}.
end{array}
}
]

In the bounded regimes a weak background limit cannot erase an already
anchored selected negative ray.  If the selected limit has margin
[
[y,y]_Jle-kappa,
qquad
kappa>0,
]
then the full weak limit satisfies
[
oxed{
[Y_{m full},Y_{m full}]_{m full}
le
-kappa-|b|^{2}<0.
}
]

In the (mathbf{B_F}) regime the entire negative sector converges strongly.
The positive coordinate remains, in general, only weakly convergent; full
strong coefficient convergence requires an additional positive-coordinate
compactness hypothesis.

WD-T39 introduces no new RH-facing interface.  It classifies where compactness
can fail before or around the two fixed-packet morphologies.

---

# Part IV. Sharpness and failure modes

## 12. Canonical sharpness witnesses

The examples below are not proof-producing substitutes for the theorems.
Each is attached to the exact theorem boundary it sharpens.

### WD-X01 — Finite negativity can screen completely

There is an explicit rank-one model in which every finite positive truncation
has one negative direction,
[
D_N=-rac1{N+1},
]
while the restored infinite positive channel gives
[
D=0.
]
This shows that WD-T06 cannot be strengthened to persistence of finite
truncation negativity under infinite positive restoration.

### WD-X02 — Critical norm one need not be attained

The canonical audit model is multiplication by (t) on (L^2(0,1)):
[
|M_t|=1
]
but no nonzero vector attains the norm.  The Lean certificate uses an
equivalent diagonal (ell^2) realization.  In either model every nonzero
vector remains strictly positive while approximate-neutral directions exist.

Thus
[
oxed{
|X|=1

otRightarrow
	ext{actual neutral vector}
}
]
in infinite dimension.

### WD-X03 — Individual screening is not compositional

With two scalar negative channels of size (r),
[
rac1{sqrt2}<r<1,
]
each channel is separately contractively screenable, but the combined map has
norm
[
sqrt2,r>1.
]
This is the sharpness witness for the shared-budget statement WD-T09.

### WD-X04 — Direct compression does not uniformly control shorting

For
[
K_r=
egin{pmatrix}
1&r\
r&1
end{pmatrix},
qquad
0<r<1,
]
the direct selected compression is (1), while the Schur-shortened covariance
is
[
1-r^{2}downarrow0.
]
Thus direct compression alone does not provide a uniform family-level shorted
floor.

### WD-X05 — Moving finite sectors can lose every persistent ray

Choose normalized strictly negative vectors supported on the (n)-th
positive and negative coordinates with signature tending to zero.  The
corresponding nested coordinate-tail sectors contain every sufficiently late
vector, but
[
oxed{
igcap_Nmathcal A_N={0}.
}
]
Finite dimension at each stage is therefore not enough; the finite selected
sector must be fixed.

### WD-X06 — Critical weak limits can become negative

Let
[
y_n
=
left(
rac1{sqrt2}e_n,
rac1{sqrt2}
ight).
]
Then
[
|y_n|=1,
qquad
[y_n,y_n]_J=0,
]
but
[
e_nightharpoonup0
]
and hence
[
y_nightharpoonup
left(
0,rac1{sqrt2}
ight)
]
with
[
oxed{
[y,y]_J=-rac12.
}
]
This realizes the negative-fall-through branch of WD-T17.

### WD-X07 — Inverse-square far decay is sharp

For
[
v=(1,-1)
]
at two distinct selected points,
[
mathbf1^{T}v=0
]
but the first moment is nonzero, and
[
R_v(z)
sim
rac{ho_1-ho_2}{z^{2}}.
]
Therefore zero moment alone does not imply (O(|z|^{-3})).

---

# Part V. Standing, verification, and boundary

## 13. Mathematical standing and formal verification

Horizon 1 uses two independent status axes.

The **mathematical standing** of a result records what sort of claim it is:
internal proof, derived statement, imported theorem plus specialization,
conditional composite, scope rule, example, or open interface.

The **formal verification standing** records what Lean verifies.  The durable
labels are:
[
egin{array}{l}
	exttt{LEAN-CERTIFIED},\
	exttt{LEAN-CERTIFIED-FROM-IMPORTED-PREMISE},\
	exttt{LEAN-BLOCKED},\
	exttt{SCOPE-ONLY}.
end{array}
]

The distinction is essential.  For example, when a Lean theorem consumes an
explicit formal premise representing zeta zero counting or the compact-window
formula, Lean certifies the downstream deduction from that premise.  It does
not thereby certify the external analytic theorem itself.

At the close of LEAN-H1, every stable Horizon-1 theorem and example has a
durable final formal status.  Exact declaration maps and CI certificate
evidence are recorded in [Lean Status](LEAN_STATUS.md).

---

## 14. Imported-source custody

The public theory has a small, explicit set of load-bearing external inputs.

- **EXT-1 — Douglas factorization.** Used directly by WD-T02 and downstream
  reduced-screening statements.
- **EXT-2A/2B — Bombieri finite inertia and multiplicity.** Used by WD-T22
  and WD-T23.
- **EXT-3 — Unit-height zeta zero counting.** Used by WD-T28 and WD-T31.
- **EXT-4 — Compact-window geometric explicit formula.** Used by WD-T34,
  WD-T35, and WD-T38.
- **EXT-5 — Digamma asymptotic.** Used by WD-T35.

These are source-pinned to exact theorem or equation locations in
[Imported Source Pins](IMPORTED_SOURCE_PINS.md).  Contextual sources are not
promoted to load-bearing status merely because they motivate the same
geometry.

---

## 15. Outputs delivered to the actual-zeta boundary

The negative branch reaches
[
oxed{
	exttt{AZ-NEXTJET-LOC}
}
]
after the zero-moment law, inverse-square far response, and
(O((log R)/R)) shell reduction have been proved.

A stronger special-packet sufficient refinement is tracked as
[
oxed{
	exttt{C-ACTUAL-KPH-FLOOR}.
}
]

The attained neutral branch reaches
[
oxed{
	exttt{AZ-FIN-WEIL-NULL-EXTENSION}
}
]
after the compact-window null equation has been reduced to a logarithmic-order
operator with finitely many arithmetic translations and the endpoint/right
threshold distinction has been isolated.

These are not theorem IDs.  They are open downstream obligations.

The noncompact morphology adds no new actual-zeta interface; it determines
which coefficient-custody failures prevent entry into a fixed-packet branch
and which background failures remain possible after a selected ray is
anchored.

---

## 16. Scope rules

Several negative statements are structural jurisdiction rules rather than
standalone theorems.

1. Unweighted sampling or frame statements do not automatically transfer to
   native Problem-1 coercivity without an explicit metric comparison.

2. Prime, pole, and archimedean explicit-formula terms are an alternate
   representation of the Weil form, not extra positive screening coordinates.

3. Neutrality is a global quadratic cancellation and does not imply termwise
   vanishing of explicit-formula contributions.

4. Weighted near next-jet localization does not by itself produce a
   source-free uniform lower bound.

5. Unselected-background escape cannot be used to erase an already anchored
   fixed selected negative ray.

These rules prevent category errors when the abstract defect calculus is
translated back into arithmetic language.

---

## 17. Conclusion

Horizon 1 produces an independent Weil-defect theory with a fully audited
operator core, a typed zeta-Weil specialization, a complete fixed-packet and
noncompact morphology classification, sharpness witnesses, and an exhausted
Lean certification track.

Its central structural conclusion is not a proof of RH.  It is a reduction of
the possible defect mechanisms to sharply separated classes:

[
oxed{
egin{array}{c}
	ext{fixed selected negative persistence},\
	ext{fixed attained-neutral persistence},\
	ext{moving selected-sector escape},\
	ext{unselected-background escape},\
	ext{fixed full-divisor negative weak limit}.
end{array}
}
]

For the two fixed-packet branches, the remaining arithmetic responsibility is
exposed at named interfaces rather than hidden inside the operator theory.

The resulting boundary is therefore explicit:

[
oxed{
	ext{independent Weil-defect theory}
quadVertquad
	ext{actual-zeta interface problem}.
}
]

Discharging the open actual-zeta interfaces would be new work beyond this
manuscript.  No such discharge is assumed here.

---

# Appendices

## Appendix A. Stable theorem index

See `PUBLIC_THEOREM_INDEX.md` when assembled.

## Appendix B. Verification matrix

See `PUBLIC_VERIFICATION_MATRIX.md` when assembled.

## Appendix C. Dependency map

See `PUBLIC_DEPENDENCY_MAP.md` when assembled.

## Appendix D. Examples and sharpness

See `PUBLIC_EXAMPLES.md` when assembled.

## Appendix E. RH-facing interfaces

See `RH_INTERFACE_APPENDIX.md` when assembled.
