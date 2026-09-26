# SZ-POST3-RATIFICATION-20260926 — Ratification of the mature post-SZ-3 bridge

**Date:** 2026-09-26  
**Branch:** sz-cross-collar  
**Operation:** audit ratification only; no new traversal  
**Canonical theorem head before/after:** SZ-CROSS-COLLAR-3  
**Public promotion:** forbidden

## 0. Scope

This record ratifies the audited post-SZ-3 residue whose dependency gates have
now been discharged.

The ratification is organized by mathematical role rather than chronology.

It does **not** ratify the entire exploratory edge/quasi-analyticity chain.

The canonical cross-collar theorem remains

\[
\boxed{\text{SZ-CROSS-COLLAR-3}}.
\]

The effect of this pass is to add a canonical auxiliary/bridge package beneath
that head.

---

# I. Batch A — auxiliary algebra, background ownership, and no-go results

## A1. SZ-CROSS-COLLAR-4R — RATIFIED AUXILIARY

Ratified statement:

if

\[
S_c=E^*S_b,
\]

then

\[
\boxed{
S_b^*E=S_c^*.
}
\]

Thus zero extension preserves the selected raw coordinate for a fixed packet.

WD-T20 pair diagonalization and the raw selected-residue map are independent
of support, so the associated raw selected source is preserved as well.

**Scope:** coordinate/source naturality only.

The rejected implication

\[
\text{same selected coordinate}
+
\text{negative full form}
\Rightarrow
\text{selected ownership}
\]

remains rejected.

---

## A2. SZ-BACKGROUND-ELIMINATION-COLLAR-0 — RATIFIED ABSTRACT AUXILIARY

Ratified statement:

if a common-carrier background covariance satisfies

\[
K_B(c)\succeq\eta I,
\qquad
\eta>0,
\]

and

\[
K_B(b)\to K_B(c)
\]

in operator norm, then background screening remains admissible on a
sufficiently small right collar.

Mere semidefinite endpoint admissibility is not open.

This is an abstract stability theorem, not the native infinite-carrier route.

---

## A3. SZ-BG-COV-CONT-0 — RATIFIED ON THE NATIVE AUXILIARY CARRIER

Ratified statement:

on the fixed native Problem-1 H^{-1}-type common carrier, support-truncated
zero columns vary in Hilbert-Schmidt norm, hence the associated channel
covariances vary in trace norm and therefore in operator norm.

This result is explicitly **not** continuity of Suzuki's unbounded
\(A_a\).

---

## A4. SZ-BG-GAP-0 — RATIFIED AUXILIARY

Ratified:

1. a global bound
   \[
   K_B\succeq\eta I,\qquad \eta>0,
   \]
   is impossible for the compact/trace-class covariance defect on an
   infinite-dimensional native carrier;

2. under the joint budget
   \[
   X_MX_M^*+X_BX_B^*\preceq I,
   \]
   the background saturation space
   \[
   Z_B=\ker(I-X_BX_B^*)
   \]
   satisfies
   \[
   \boxed{
   Z_B\subseteq\ker X_M^*;
   }
   \]

3. therefore the residual background budget
   \[
   R_B=I-X_BX_B^*
   \]
   is strictly positive on the finite-dimensional selected-active range
   \[
   \operatorname{Ran}X_M.
   \]

This gives a finite selected-active relative gap, not a global physical gap.

---

## A5. SZ-BG-RELATIVE-GAP-0 — RATIFIED NO-GO WITH SCOPE RESTRICTION

Ratified no-go:

norm convergence of the physical selected/background synthesis maps and their
covariances does not imply norm continuity of the corresponding Douglas
reduced solutions or transport of the selected-active relative gap.

The compact diagonal example establishes this even for one-dimensional
selected/background domains.

**Scope restriction:** the nearby example is not a counterexample under a
separately maintained joint nonnegative budget at every parameter. Its role
is only to rule out deriving coefficient-side continuity from physical
continuity plus individual screenability.

The correct robust collar test is therefore pointwise in support.

---

## A6. SZ-COLLAR-BRANCH-CLASSIFICATION-0 — RATIFIED POINTWISE TAXONOMY

At a strict support \(b>c\) with cross-collar negativity:

### Background admissible

If the background is contractively screenable, WD-T10 removes it and the
remaining failure is a selected residual defect:

\[
\boxed{
\text{SR-R}
\quad\text{or}\quad
\text{SR-B}.
}
\]

### Background inadmissible

The obstruction is a background screening defect:

\[
\boxed{
\text{BG-R}
\quad\text{or}\quad
\text{BG-B}.
}
\]

These four cells exhaust the pointwise owner taxonomy.

They do **not** by themselves imply WD-T37 or WD-T39, which are sequential
morphology statements.

---

# II. Batch B — Suzuki channel bridge

## B0. SZ-ZERO-SIDE-NORMALIZATION-0 — RATIFIED NORMALIZATION LEDGER

The following conventions are canonical for the bridge:

\[
\widehat f(z)
=
\int_{\mathbb R}f(x)e^{izx}\,dx;
\]

for a distinct ordinate of multiplicity \(m_\gamma\),

\[
\boxed{
w_\gamma
=
\sqrt{m_\gamma}\,\widehat f(\gamma);
}
\]

and for one nonreal pair,

\[
\boxed{
p=
\frac{w_\gamma+w_{\bar\gamma}}{\sqrt2},
\qquad
n=
\frac{w_\gamma-w_{\bar\gamma}}{\sqrt2}.
}
\]

Thus

\[
|w_\gamma|^2+|w_{\bar\gamma}|^2
=
|p|^2+|n|^2.
\]

The current Lean pair-eigen equivalence remains an algebraic eigenspace
diagonalization and is **not** the unitary Hilbert normalization used in
analytic norm-square formulas.

Multiplicity changes the weight of the surviving distinct-ordinate channel
but does not create extra independent channels.

---

## B1. SZ-PRECOND-FORM-BRIDGE-1 — RATIFIED

On Suzuki's regular carrier,

\[
D=i\,\frac d{dx}:
H_0^1(-a,a)\to L_0^2(-a,a)
\]

is the exact derivative bridge and

\[
\boxed{
Q_W(v_1,v_2)
=
\langle G_aDv_1,Dv_2\rangle.
}
\]

The operator

\[
B_a=D^*G_aD
\]

has Friedrichs extension \(A_a\).

Suzuki's

\[
K_a=(-\Delta_N)^{-1}
\]

belongs to the denominator of the generalized Rayleigh quotient and is not the
repo auxiliary Dirichlet resolvent.

This supersedes the speculative metric-congruence framing of
SZ-CARRIER-METRIC-COMPAT-0.

---

## B2. SZ-PRECOND-FORM-BRIDGE-2 — RATIFIED WITH B0 NORMALIZATION

For

\[
u=Dv,
\]

the normalized zero-coordinate analysis satisfies

\[
|\widehat v(\gamma)|
\lesssim_a
\frac1{1+|\gamma|}\|u\|_2.
\]

Unit-height zero counting therefore gives a bounded regular analysis map into
the normalized zero coefficient space.

After the unitary pair transform and fixed selected/background split,

\[
\boxed{
G_a
=
S_{+,a}S_{+,a}^*
-
S_{M,a}S_{M,a}^*
-
S_{B,a}S_{B,a}^*.
}
\]

Thus Suzuki's bounded screw operator is itself a physical defect operator in
the Horizon-1 sense on the regular screw carrier.

---

## B3. SZ-CHANNEL-CUSTODY-FORMDOMAIN-0 — RATIFIED

The logarithmic Paley-Wiener Bessel estimate is ratified in the normalized
multiplicity-weighted form:

\[
\boxed{
\sum_{\gamma\ {\rm distinct}}
m_\gamma
|\widehat f(\gamma)|^2
\lesssim_a
\int_{\mathbb R}
\log(e+|t|)
|\widehat f(t)|^2\,dt.
}
\]

Together with the Horizon-1 shifted two-sided logarithmic form estimate, this
extends the zero-coordinate map continuously to the closed logarithmic form
domain.

Hence the polarized zero-side decomposition extends to the full closed form
domain:

\[
\boxed{
Q_W
=
Q_+
-
Q_M
-
Q_B.
}
\]

This is a **closed-form decomposition**. It does not assert that every channel
is represented by a bounded operator on ambient \(L^2\).

No positive-Sobolev bootstrap is used.

---

# III. Batch C — same-source and margin package

## C0. SZ-SAME-SOURCE-SECTOR-SCOPE-0 — RATIFIED

For a symmetry-closed packet of complete quartets, restricting the physical
carrier to a parity/reality sector restricts the selected target to the
matching symmetry sector.

For one quartet:

\[
\begin{array}{c|c}
\text{sector} & \text{negative-coordinate relation}\\
\hline
\text{complex even} & u_-=-u_+\\
\text{complex odd} & u_-=u_+\\
\text{real} & u_-=\overline{u_+}\\
\text{real even} & u_+\in i\mathbb R,\ u_-=-u_+\\
\text{real odd} & u_+\in\mathbb R,\ u_-=u_+
\end{array}
\]

The selected-coordinate map is surjective onto the corresponding typed target.

No restricted-sector statement is asserted for packets not closed under the
relevant zeta symmetries.

---

## C1. SZ-CROSS-COLLAR-SAME-SOURCE-0 — RATIFIED

For a fixed finite selected packet,

\[
\boxed{
\sigma_c(\mathcal F_c)=M_\Pi
}
\]

on the unrestricted complex form carrier, with the typed sector version from
C0 when parity/reality is imposed.

Therefore every collar quotient class has a representative

\[
h^\circ
\]

with

\[
\boxed{
\sigma_b(h^\circ)=0.
}
\]

Since the cross functional annihilates old directions,

\[
q_b(\widetilde k,h^\circ)
=
q_b(\widetilde k,h).
\]

Hence

\[
\boxed{
\Lambda_{c,b;k}\ne0
\Longrightarrow
\exists x_b:
q_b(x_b)<0,
\qquad
\sigma_b(x_b)=\sigma_c(k).
}
\]

The associated raw selected residue source is exactly unchanged across the
collar.

This is source custody, not selected sign ownership.

---

## C2. SZ-SAME-SOURCE-MARGIN-0 — RATIFIED

Define the same-source affine margin

\[
\boxed{
\mathfrak m_b(u)
=
-\inf_{\sigma_b(x)=u}q_b(x).
}
\]

On the affine fiber

\[
\widetilde k+\ker\sigma_b,
\]

write

\[
L_b(h)=q_b(\widetilde k,h).
\]

If \(q_b|_{\ker\sigma_b}\) is nonnegative and \(L_b\) vanishes on its
nullspace, then

\[
\boxed{
\mathfrak m_b(u)
=
\sup_{\substack{h\in\ker\sigma_b\\q_b(h)>0}}
\frac{|L_b(h)|^2}{q_b(h)}.
}
\]

If the selected-preserving restriction contains either a negative direction or
a null direction coupled nontrivially to \(\widetilde k\), then

\[
\boxed{
\mathfrak m_b(u)=+\infty.
}
\]

Cross leakage implies only pointwise positivity of the margin, not a
support-uniform lower bound.

The fixed-margin/vanishing-margin subsequence dichotomy is ratified.

---

## C3. SZ-COMPACT-COLLAR-UNIFORMITY-0 — RATIFIED

For a fixed finite packet and compact collar \(c<b\le A\),

\[
\boxed{
\sup_{c<b\le A}\|\sigma_b\|
\le
C_{\Pi,A}<\infty,
}
\]

with

\[
C_{\Pi,A}^2
=
\sum_{\gamma\in\Gamma_\Pi}
\frac{2A\,m_\gamma}{|\gamma|^2}
e^{2A|\Im\gamma|}.
\]

Also, continuity of Suzuki's screw kernel on \([-2A,2A]\) gives

\[
\boxed{
\sup_{c<b\le A}\|G_b\|
\le
2A\sup_{|t|\le2A}|g(t)|
<\infty.
}
\]

These bounds also hold after the C0 symmetry restrictions.

---

## C4. SZ-MARGIN-MV-FIRST-ORDER-0 — PARTIALLY RATIFIED / CORE LAW RATIFIED

On the regular Suzuki carrier, let

\[
r_b=G_bJu
\]

and correct it by the fixed old-support right inverse:

\[
d_b
=
r_b
-
JR_c(\sigma_br_b).
\]

Then

\[
\boxed{
\sigma_b(d_b)=0,
}
\]

and

\[
\boxed{
q_b(Ju,d_b)=\Delta_{c,b}(u)^2.
}
\]

Using C3,

\[
\|d_b\|
\lesssim
\Delta_{c,b}(u),
\]

so

\[
\boxed{
\mathfrak m_b(u)
\ge
C_*
\Delta_{c,b}(u)^2
}
\]

uniformly on a fixed compact right collar, with an explicit positive constant
depending only on the collar, packet, and chosen old-support right inverse.

A matching upper bound

\[
\mathfrak m_b(u)\lesssim\Delta_{c,b}(u)^2
\]

remains conditional on a selected-preserving coercivity estimate and is
**not** ratified unconditionally.

Accordingly, no universal first collar exponent is asserted.

---

# IV. Batch D — finite-dimensional endpoint reductions only

This batch ratifies only the internally closed pieces of the endpoint
reconnaissance.

## D1. Finite dimensionality of the regular zero kernel — RATIFIED AUXILIARY

For

\[
u\in\ker G_c
\]

and

\[
v=D^{-1}u,
\]

one has

\[
B_cv=0.
\]

Since \(A_c\) extends \(B_c\),

\[
v\in\ker A_c.
\]

Suzuki's \(A_c\) has discrete spectrum with finite-multiplicity eigenspaces.

Therefore

\[
\boxed{
\dim\ker G_c<\infty.
}
\]

---

## D2. Variance-growth identity — RATIFIED AUXILIARY

For

\[
F_u(x)
=
\int_{-c}^c g(x-y)u(y)\,dy
\]

and

\[
m(b)
=
\frac1{2b}
\int_{-b}^bF_u(x)\,dx,
\]

the collar residual satisfies

\[
\Delta_{c,b}(u)^2
=
\int_{-b}^b|F_u(x)-m(b)|^2\,dx.
\]

Differentiation gives

\[
\boxed{
\frac d{db}
\Delta_{c,b}(u)^2
=
|F_u(b)-m(b)|^2
+
|F_u(-b)-m(b)|^2.
}
\]

Hence

\[
\boxed{
b\longmapsto\Delta_{c,b}(u)^2
\text{ is nondecreasing.}
}
\]

---

## D3. Stabilized persistence and flatness filtrations — RATIFIED AUXILIARY

Inside the finite-dimensional space

\[
K_c:=\ker G_c,
\]

define

\[
P_\varepsilon
=
\ker\bigl(G_{c+\varepsilon}J_\varepsilon\bigr).
\]

The nested family \(P_\varepsilon\) stabilizes for all sufficiently small
\(\varepsilon>0\); call the stabilized space

\[
P_c^+.
\]

For \(N\ge0\), define

\[
F_N
=
\left\{
u\in K_c:
\Delta_{c,c+\varepsilon}(u)
=
o(\varepsilon^N)
\right\}.
\]

The descending chain \(F_N\) stabilizes at some finite index \(N_c\).

Thus

\[
F_\infty
=
\bigcap_NF_N
=
F_{N_c},
\]

and the finite-dimensional edge-defect quotient

\[
\boxed{
\mathcal E_c
=
F_\infty/P_c^+
}
\]

is a legitimate downstream research object.

No assertion that \(\mathcal E_c=0\) is ratified.

---

# V. Source normalization for later edge work

## E1. SZ-SUZUKI-ARCHIMEDEAN-ANALYTICITY-PIN — RATIFIED SOURCE-PINNED DERIVATION

Suzuki's equation (1.3) gives

\[
g(t)
=
a_\infty(t)
+
\sum_{n\ge2}
\frac{\Lambda(n)}{\sqrt n}
(t-\log n)_+,
\qquad t>0.
\]

The non-prime component is built from exponentials, a linear term, and

\[
e^{-t/2}\Phi(e^{-2t},2,1/4).
\]

Since the Hurwitz-Lerch series is analytic for \(|e^{-2t}|<1\),

\[
\boxed{
a_\infty\in C^\omega((0,\infty)).
}
\]

Suzuki §2.2 separately gives the logarithmic origin singularity.

Thus the only positive-axis nonanalytic sites of the screw kernel are

\[
\boxed{
0
\quad\text{and}\quad
\{\log p^m\}.
}
\]

This source pin is canonical auxiliary input for future edge analysis.

---

# VI. Explicitly NOT ratified

The following remain residue/provenance and are excluded from the canonical
post-SZ-3 bridge.

## N1. SZ-CROSS-COLLAR-4

Not ratified.

Its abstract factorization lemma may be retained, but the selected-ownership
inference is rejected.

---

## N2. SZ-CROSS-COLLAR-5 and SZ-CROSS-COLLAR-6

Not ratified as current theorem units.

They are superseded historical residue.

Their valid content has been recovered by 4R, same-source custody, and the
margin package.

---

## N3. SZ-CARRIER-METRIC-COMPAT-0

Not ratified as the bridge architecture.

Only its structural observation that a boundedly invertible congruence cannot
identify the compact auxiliary covariance realization with Suzuki's unbounded
localized operator is retained as provenance.

The operative bridge is B1.

---

## N4. Superflat Stieltjes construction in SZ-MV-ROUGH-ENDPOINT-0

Not ratified.

It remains an illustrative complex-analysis model because the Cauchy
jump-to-\(L^2\)-density step has not been promoted to project-standard
load-bearing proof status.

None of Batches A–D depends on it.

---

## N5. SZ-KERNEL-EDGE-PROP-0, SZ-KERNEL-EDGE-QA-1, and SZ-KERNEL-EDGE-QA-2

Not ratified in this pass.

The C5 source gate needed by QA-1 is now closed, but these notes form a
separate genuinely novel edge/quasi-analyticity package and should receive
their own adversarial audit before canonicalization.

Their current contents remain research residue unless superseded by that
audit.

---

# VII. Canonical consequences after this ratification

The canonical post-SZ-3 bridge now supports the following chain.

Let

\[
0\ne k\in\ker A_c.
\]

The ratified SZ-3 theorem gives the cross functional

\[
\Lambda_{c,b;k}
\]

and

\[
\Lambda_{c,b;k}\ne0
\Longrightarrow
\lambda_b<0.
\]

The newly ratified bridge adds:

### 1. Full form-domain zero-side custody

The closed Weil form carries a normalized positive / selected-negative /
background-negative decomposition.

### 2. Same selected source

For every fixed finite selected packet, collar leakage can be represented by a
negative test vector with the exact endpoint selected coordinate.

### 3. Pointwise owner classification

At each strict support:

\[
\boxed{
\begin{cases}
\text{SR-R or SR-B}, & \text{background admissible},\\
\text{BG-R or BG-B}, & \text{background inadmissible}.
\end{cases}
}
\]

### 4. Exact same-source margin

The strength of the negative excursion with the source held fixed is measured
by

\[
\mathfrak m_b(u).
\]

### 5. Regular-carrier quantitative transfer

On the regular Suzuki carrier,

\[
\boxed{
\mathfrak m_b(u)
\gtrsim
\Delta_{c,b}(u)^2.
}
\]

### 6. Finite-dimensional vanishing-margin obstruction

If the margin/residual becomes superflat, the remaining regular obstruction is
encoded by the finite-dimensional quotient

\[
\boxed{
\mathcal E_c=F_\infty/P_c^+.
}
\]

---

# VIII. What remains open

This ratification does **not** prove

\[
\mathcal E_c=0;
\]

it does not produce a universal first nonzero collar exponent;

it does not supply selected-preserving coercivity;

it does not establish the residual support-filtration compatibility required
for a literal automatic invocation of WD-T37;

and it does not determine which of SR-R, SR-B, BG-R, BG-B actual zeta occupies.

The next genuinely new analytic question remains the edge package:

\[
\boxed{
\text{can an actual regular kernel mode be superflat but leaking?}
}
\]

That question is deliberately outside this ratification pass.

---

# IX. Canonical status

The canonical **theorem cursor** remains

\[
\boxed{
\text{SZ-CROSS-COLLAR-3}.
}
\]

No new traversal theorem was produced here.

The following are now canonical supporting packages:

\[
\boxed{
\text{POST-SZ-3 AUXILIARY / CHANNEL / SAME-SOURCE / MARGIN PACKAGE}.
}
\]

Thus later work may use the ratified results enumerated in Batches A–D as
dependencies without reopening their original residue status.

No public repository changes are authorized by this record.
