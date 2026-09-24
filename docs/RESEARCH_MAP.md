# Research Map

## Current horizon

The canonical phase plan is [Horizon 1 — Independent Weil-Defect Theory](HORIZON_1.md).

\[
\boxed{
\begin{array}{ll}
\textbf{H1-P0} & \text{Consolidation and custody}\\
\textbf{H1-P1} & \text{Abstract defect calculus}\\
\textbf{H1-P2} & \text{Zeta-Weil specialization}\\
\textbf{H1-P3} & \text{Defect morphology theorem}\\
\textbf{H1-P4} & \text{Proof audit and theorem normalization}\\
\textbf{H1-P5} & \text{Public mathematical package}
\end{array}
}
\]

Current position:

\[
\boxed{
\text{H1-P0 COMPLETE}
\qquad
\text{H1-P1 COMPLETE}
\qquad
\text{H1-P2 COMPLETE}
\qquad
\text{H1-P3 COMPLETE}
\qquad
\text{H1-P4 ACTIVE}.
}
\]

The RH-facing statements at the bottom of this map are **interfaces out of Horizon 1**, not Horizon-1 completion requirements.

---

## H1-P1 abstract core

### 1. Defect operator and screening

For

\[
E(x,u)=S_+x+S_-u
\]

and

\[
\mathcal A=(\ker E)^\perp,
\]

define

\[
\boxed{
D=S_+S_+^*-S_-S_-^*.
}
\]

Then

\[
\boxed{
\mathcal A\text{ is }J\text{-nonnegative}
\iff
D\succeq0
\iff
S_-=-S_+X
\text{ for a contraction }X.
}
\]

When exact range inclusion holds, the Douglas reduced solution gives

\[
\boxed{
\mathcal A=\operatorname{graph}(-X^*).
}
\]

See [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md).

### 2. Selected/background transfer

For a selected finite negative sector \(M\) and negative background \(B\),

\[
D_{\rm full}
=
D_M-S_BS_B^*.
\]

Selected negativity survives aggregation, but aggregate negativity does not preserve selected-sector custody.

If the background is contractively screened with reduced map \(X_B\), define

\[
R_B=I-X_BX_B^*
\]

and

\[
S_{\rm eff}=S_+R_B^{1/2}.
\]

Then the selected problem re-enters the same calculus:

\[
\boxed{
D_{\rm full}
=
S_{\rm eff}S_{\rm eff}^*
-
S_MS_M^*.
}
\]

For fixed finite \(M\), the reduced residual screening map \(Y\) satisfies

\[
\boxed{
\operatorname{ind}_-
=
\#\{j:\sigma_j(Y)>1\},
}
\]

and

\[
\boxed{
\operatorname{nul}_J
=
\#\{j:\sigma_j(Y)=1\}.
}
\]

See [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md).

### 3. Support filtration and persistence

For a monotone family

\[
\mathcal A_s\subseteq\mathcal A_t
\qquad(s<t),
\]

the right-limit space is

\[
\boxed{
\mathcal A_{c+}
=
\bigcap_{t>c}\mathcal A_t.
}
\]

Its endpoint jump is

\[
\boxed{
\mathcal J_c
=
\mathcal A_{c+}\ominus\mathcal A_c.
}
\]

With a fixed finite negative sector, any normalized right-approaching sequence with

\[
[y_n,y_n]_J\to q_*\le0
\]

has a nonzero right-limit vector

\[
y\in\mathcal A_{c+}
\]

satisfying

\[
[y,y]_J\le q_*.
\]

At criticality, either:

- the positive coordinates converge strongly and \(y\) is neutral; or
- positive coefficient mass is lost and \(y\) becomes strictly negative.

Thus non-attained approximate neutrality without persistence requires an infinite or moving negative-sector mechanism.

Under a bounded physical realization, every genuinely new endpoint vector has diverging representation cost.

See [Support Filtration and Persistence Limits](SUPPORT_FILTRATION_PERSISTENCE.md).

---

## Abstract screening taxonomy

\[
\boxed{
\begin{array}{ccl}
\operatorname{Ran}S_-\not\subseteq\operatorname{Ran}S_+
&\Rightarrow&
\text{range-defect negativity},\\
\operatorname{Ran}S_-\subseteq\operatorname{Ran}S_+,\ \|X\|>1
&\Rightarrow&
\text{over-budget negativity},\\
\|X\|<1
&\Rightarrow&
\text{uniform positive screening},\\
\|X\|=1\text{ attained}
&\Rightarrow&
\text{neutral mode},\\
\|X\|=1\text{ not attained}
&\Rightarrow&
\text{approximate-neutral boundary}.
\end{array}
}
\]

H1-P1.2 refines the last line:

\[
\boxed{
\text{fixed finite selected sector}
+
\text{right-approach}
\Longrightarrow
\text{actual nonpositive right-limit ray}.
}
\]

Hence the genuinely nonpersistent approximate-neutral case belongs to moving/infinite-sector noncompactness.

---

## Zeta-Weil branches already identified

The prior zeta traversal explicitly produced two arithmetic morphologies that H1-P2 must now attach to the abstract carriers.

### Negative-persistence branch

\[
\boxed{
\text{persistent negative ray}
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
R_v(z)=O(|z|^{-2})
\Longrightarrow
\text{weighted near next-jet field}.
}
\]

The surviving arithmetic object is

\[
\mathcal N_v[\psi]
=
\sum_{\mu\notin F}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)}.
\]

### Neutral branch

\[
\boxed{
\text{neutral persistence}
\Longrightarrow
W_ck=0.
}
\]

At fixed support,

\[
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole},
\]

with principal symbol

\[
\Psi_c(t)=\log|t|+O_c(1).
\]

### Approximate-neutral question

H1-P2 must determine whether any remaining zeta-Weil critical sequence without an attained neutral mode is caused by:

- a moving selected packet;
- an infinite negative background;
- positive-coordinate escape;
- or another explicitly identified noncompactness mechanism.

---

## Three layers

### A. General defect structure — COMPLETE

- defect operator and negative-index transfer;
- Douglas screening;
- rank-one specialization;
- shared screening budgets;
- background elimination;
- finite-sector singular-value inertia;
- shorted covariance;
- support filtration;
- endpoint jumps;
- persistent-ray compactness;
- representative blow-up;
- moving-sector escape.

### B. Zeta-Weil attachment — COMPLETE

- quartet channel decomposition;
- selected/unselected divisor decomposition;
- zero-moment conservation;
- \(O(z^{-2})\) rational far field;
- completed-\(\Xi\) weighted next jets;
- compact-window prime shifts;
- logarithmic archimedean order.

### C. RH-facing exclusion — OUTSIDE HORIZON 1

- worst-packet next-jet control;
- actual KPH floor or equivalent transversality;
- neutral null-extension/support rigidity.

---

## H1-P2 specialization layers

The canonical mapping is now recorded in [Zeta-Weil Specialization Map](ZETA_WEIL_SPECIALIZATION_MAP.md).

\[
\boxed{
\text{ZW-0: Weil/Krein pair geometry}
\longrightarrow
\text{ZW-1: zeta-divisor structure}
\longrightarrow
\text{ZW-2: explicit-formula arithmetic}.
}
\]

The first genuinely non-abstract structural identity is the pair-antisymmetry law

\[
\mathbf1^Tv=0,
\]

which yields

\[
R_v(z)=O(|z|^{-2}).
\]

Prime/pole/archimedean terms begin only at ZW-2; they are not extra positive screening coordinates.

## H1-P2.1 disposition

The canonical ZW-1 theorem package is [Quartet Channel and Residue Structure](QUARTET_CHANNEL_RESIDUE_STRUCTURE.md).

\[
\boxed{
\text{pair antisymmetry}
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
R_v(z)=O(|z|^{-2}),
}
\]

with inverse-square order sharp.

Native Problem-1 synthesis is Hilbert-Schmidt/compact, so unweighted sampling/frame inputs remain metric-separated from native coercivity.

## H1-P2.2 disposition

The canonical ZW-2 theorem package is [Explicit-Formula Arithmetic Attachment](EXPLICIT_FORMULA_ARITHMETIC_ATTACHMENT.md).

Negative branch:

\[
\boxed{
\mathbf1^Tv=0
\Longrightarrow
R_v(z)=O(z^{-2})
\Longrightarrow
\mathcal F_{v,R}
=
O((\log R)/R)
\Longrightarrow
\text{weighted near next-jet field}.
}
\]

Neutral branch:

\[
\boxed{
\text{fixed support}
\Longrightarrow
\text{finitely many prime translations}
\quad\text{and}\quad
\Psi_c(t)=\log|t|+O_c(1).
}
\]

The explicit formula supplies no automatic positive-Sobolev or quasianalytic gain.

Therefore

\[
\boxed{
\textbf{H1-P2 — ZETA-WEIL SPECIALIZATION: COMPLETE.}
\]

## H1-P3.0 disposition

The fixed-packet negative branch is packaged in [Negative Defect Morphology Theorem](NEGATIVE_DEFECT_MORPHOLOGY.md).

\[
\boxed{
\begin{aligned}
\text{persistent selected negativity}
&\Longrightarrow
\text{negative endpoint jump}\\
&\Longrightarrow
\text{normalized full-Weil negativity}\\
&\Longrightarrow
\mathbf1^Tv=0\\
&\Longrightarrow
R_v(z)=O(z^{-2})\\
&\Longrightarrow
\mathcal F_{v,R}=O((\log R)/R)\\
&\Longrightarrow
\text{weighted finite/intermediate next-jet field}.
\end{aligned}
}
\]

The theorem does not assert a generic lower bound for the near field. Its stop line is \(\texttt{AZ-NEXTJET-LOC}\).

## H1-P3.1 disposition

The attained-neutral branch is packaged in [Neutral Defect Morphology Theorem](NEUTRAL_DEFECT_MORPHOLOGY.md).

\[
\boxed{
\text{fixed-packet criticality}
\Longrightarrow
\begin{cases}
\text{negative fall-through to P3.0},\\
\text{attained neutral mode}.
\end{cases}
}
\]

On the neutral branch,

\[
\boxed{
W_ck=0,
}
\]

and the corresponding compact-window operator has logarithmic principal order with finitely many prime translations.

The unresolved fixed-vector support question is exactly \(\texttt{AZ-FIN-WEIL-NULL-EXTENSION}\).

## H1-P3.2 disposition

The remaining noncompact species are packaged in [Noncompact Background Morphology Theorem](NONCOMPACT_BACKGROUND_MORPHOLOGY.md).

\[
\boxed{
\text{moving selected escape}
\ne
\text{unselected-background escape}.
}
\]

The former can erase every selected weak limit. The latter cannot erase an already anchored fixed selected negative ray; it only prevents strong full-divisor convergence.

Thus

\[
\boxed{
\textbf{H1-P3 — DEFECT MORPHOLOGY THEOREM: COMPLETE.}
\]

## H1-P4.0 disposition

Stable theorem labels and the normalized dependency graph are now canonical:

- [Theorem Ledger](THEOREM_LEDGER.md);
- [Dependency Audit](DEPENDENCY_AUDIT.md).

The dependency graph is acyclic at the Horizon-1 level, and the RH-facing interfaces occur only downstream of the morphology theorems.

## Current cursor

\[
\boxed{
\texttt{H1-P4.1 / IMPORTED SOURCE PINNING}
}
\]

The next pass should pin every load-bearing external theorem/formula to its exact source location and normalize the conventions inherited from it.

---

## RH-facing interfaces

### Negative branch

\[
\boxed{
\texttt{AZ-NEXTJET-LOC}
}
\]

or an equivalent actual-zeta theorem controlling the required weighted near-field compensation.

### Selected screening floor

\[
\boxed{
\texttt{C-ACTUAL-KPH-FLOOR}
}
\]

or an equivalent packetwise transversality theorem.

### Neutral branch

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
}
\]

or an equivalent support theorem for the logarithmic-order compact-window operator.
