# Proof Status

This file records the standing of the current Weil-defect results. It is deliberately stricter than the project README.

## Standing labels

- **PROVED** — established within the stated framework/hypotheses.
- **CONDITIONAL** — proved assuming an explicitly named branch condition.
- **DERIVED** — exact reformulation or reduction from retained inputs.
- **IMPORTED** — external theorem used with explicit scope.
- **PROVED EXAMPLE** — explicit construction establishing possibility or sharpness.
- **OPEN** — required later but not established.

---

# H1-P1 — Abstract defect calculus

H1-P1 is complete.

## H1-P1.0 — Abstract screening

| Label | Statement | Standing |
| --- | --- | --- |
| WD-A1 | The \(J\)-form on the analysis space is represented by \(D=S_+S_+^*-S_-S_-^*\), with matching negative index | PROVED |
| WD-A2 | \(D\succeq0\) iff the negative synthesis factors contractively through the positive synthesis | PROVED using IMPORTED Douglas factorization |
| WD-A3 | Under exact range inclusion, the analysis space is \(\operatorname{graph}(-X^*)\) for the reduced screening solution | PROVED |
| WD-A4 | Screening taxonomy: range defect, over-budget negative, strict positive, attained neutral, non-attained approximate-neutral | PROVED |
| WD-A5 | The rank-one defect is the one-negative-channel specialization | PROVED |
| WD-A6 | Increasing positive channels give monotone Loewner screening and nonincreasing negative index | PROVED |
| WD-E1 | Finite strict negativity can screen completely to zero in the infinite limit | PROVED EXAMPLE |
| WD-E2 | Critical screening norm need not produce an actual neutral vector | PROVED EXAMPLE |

Canonical source: [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md).

The key correction is

\[
\boxed{
\text{zero screening margin}
\not\Rightarrow
\text{actual neutral vector}.
}
\]

In infinite dimension, the norm-one screening operator may fail to attain its norm.

---

## H1-P1.1 — Restricted channels and finite index

| Label | Statement | Standing |
| --- | --- | --- |
| WD-B1 | Selected negativity survives addition of negative background; converse custody fails | PROVED |
| WD-B2 | An \(m\)-dimensional selected negative sector creates at most \(m\) negative directions | PROVED |
| WD-B3 | Selected and background channels consume one shared screening budget | PROVED |
| WD-B4 | Contractively screenable background reduces to a residual positive synthesis | PROVED |
| WD-B5 | Finite selected-sector inertia is counted by singular values of the reduced residual screening map | PROVED |
| WD-B6 | Legitimate residual-budget elimination can be iterated | PROVED |
| WD-B7 | Complement elimination replaces direct compression by a Schur/shorted covariance | PROVED in strictly positive setting |
| WD-B8 | Finite positive shadows preserve negative signature but not analysis-space admissibility | PROVED |
| WD-E3 | Individually screenable channels need not be jointly screenable | PROVED EXAMPLE |
| WD-E4 | Direct finite-target covariance can stay strong while shorted covariance collapses | PROVED EXAMPLE |

Canonical source: [Restricted-Channel and Finite-Index Transfer](RESTRICTED_CHANNEL_TRANSFER.md).

For a fixed finite selected sector with reduced residual screening map \(Y\),

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

Therefore

\[
\boxed{
\|Y\|=1
\Longrightarrow
\text{an actual neutral vector exists}.
}
\]

A fixed finite selected sector cannot realize the non-attained critical morphology by itself.

---

## H1-P1.2 — Support filtration and persistence

| Label | Statement | Standing |
| --- | --- | --- |
| WD-C1 | Monotone analysis-space projections converge strongly to the right-limit projection | PROVED |
| WD-C2 | Right-limit analysis space is the orthogonal complement of the limiting gap union | PROVED |
| WD-C3 | Fixed finite negative sectors force a nonzero nonpositive right-limit ray from any unit critical/negative sequence | PROVED |
| WD-C4 | Critical sequences give either an actual neutral right-limit vector or a stricter negative limit via positive-mass loss | PROVED |
| WD-C5 | Uniform negative margin forces a persistent negative endpoint-jump vector | PROVED |
| WD-C6 | New right-limit negative index is bounded by endpoint-jump quotient dimension | PROVED |
| WD-C7 | New endpoint vectors require representative-norm blow-up under bounded physical realization | PROVED |
| WD-C8 | Boundary amplification cost diverges as support approaches the endpoint and target error tends to zero | PROVED |
| WD-C9 | Vanishing coefficient amplitude becomes physical blow-up after normalization | PROVED |
| WD-E5 | Moving finite sectors can lose every nonzero persistent ray | PROVED EXAMPLE |
| WD-E6 | Positive-coordinate mass loss can turn neutral approximants into a strict negative persistent limit | PROVED EXAMPLE |

Canonical source: [Support Filtration and Persistence Limits](SUPPORT_FILTRATION_PERSISTENCE.md).

The decisive finite-sector result is

\[
\boxed{
\text{fixed finite negative sector}
+
[y_n,y_n]_J\to q_*\le0
\Longrightarrow
0\ne y\in\mathcal A_{c+},
\quad
[y,y]_J\le q_*.
}
\]

Hence nonpersistent approximate neutrality requires a moving/infinite-sector mechanism.

---

# H1-P2.0 — Zeta-Weil specialization map

The canonical mapping is [Zeta-Weil Specialization Map](ZETA_WEIL_SPECIALIZATION_MAP.md).

The pass establishes the following standing distinctions:

| Specialization statement | Standing |
| --- | --- |
| (K_+=K_{\rm crit}\oplus K_{{\rm off},+}), (K_-=K_{{\rm off},-}) | DERIVED specialization map |
| finite selected packet (Pi\mapsto M_\Pi\subset K_-) | DERIVED specialization map |
| unselected negative divisor (mapsto B_\Pi) | DERIVED specialization map |
| selected/full sign identity (Q_W=Q_{\Pi,t}-\|S_{B_\Pi,t}^*h\|^2) | DERIVED from WD-B1 |
| rank-one selected-cell defect = WD-B4 + WD-B7 + WD-A5 terminal form | DERIVED specialization map |
| fixed finite packet criticality produces a nonpositive persistent ray | DERIVED from WD-C3/C4 |
| representative blow-up is WD-C7/C9 rather than arithmetic | DERIVED classification |
| (mathbf1^Tv=0) for selected negative pair residues | PROVED zeta/Weil-specific structure |
| (R_v(z)=O(|z|^{-2})) | PROVED consequence of zero moment |
| prime/pole/archimedean terms are an alternate Weil-form representation, not extra (K_+) channels | SCOPE CLASSIFICATION |

The specialization therefore separates:

[
oxed{
	ext{ZW-0 pair geometry}
	o
	ext{ZW-1 zeta-divisor structure}
	o
	ext{ZW-2 explicit-formula arithmetic}.
}
]

A key derived correction is:

[
oxed{
	ext{fixed finite packet}
+
	ext{critical right-approach}
Longrightarrow
	ext{actual nonpositive persistent ray}.
}
]

Thus a nonpersistent approximate-neutral morphology can remain only through moving/infinite-sector background mechanisms, not as an independent fixed-packet case.

---

# Zeta-Weil results carried into H1-P2

The following statements originated in the prior zeta traversal and are now awaiting explicit specialization mapping onto H1-P1.

## 1. Finite Weil negative index

For finite symmetric zero sets, the finite Weil matrix has one negative direction per nonreal conjugate pair.

In the two-quartet specialization used in the prior traversal,

\[
\operatorname{ind}_{-}=4,
\qquad
\operatorname{ind}_{-}^{+}
=
\operatorname{ind}_{-}^{-}
=
2.
\]

**Standing:** IMPORTED theorem + exact specialization.

**Not implied:** survival of a strictly negative eigenvalue in the infinite-zero limit.

---

## 2. Spectral screening

Finite negative eigenvalues may satisfy

\[
\lambda^-_{N,k}<0
\]

for every finite truncation while

\[
\lambda^-_{N,k}\uparrow0
\]

as the positive critical-line complement is restored.

**Standing:** structural reduction, now abstractly covered by WD-A6 and WD-C1.

---

## 3. Rank-one selected-cell defect

The selected-cell screening problem takes the form

\[
\mathcal K_C(t)
=
\widetilde S_t\widetilde S_t^*
-
\widetilde g_C\otimes\widetilde g_C.
\]

The threshold satisfies

\[
C_*(t)\le1
\iff
\mathcal K_C(t)\succeq0.
\]

**Standing:** DERIVED.

**Abstract carrier:** WD-A5.

---

## 4. Critical-line tail monotonicity

For truncated and completed denominators,

\[
D_\infty(h)\ge D_N(h),
\]

so

\[
Q_\infty(h)\le Q_N(h).
\]

Adding omitted critical-line positive channels cannot increase the selected quotient.

**Standing:** PROVED with stated input definitions.

**Abstract carrier:** positive-channel monotonicity / WD-A6.

---

## 5. Persistent normalized negativity

Assume the PAP/MTP-1 negative-persistence branch and write

\[
y=(a,u),
\qquad
\kappa=\|u\|^2-\|a\|^2>0.
\]

For a corresponding right-limit sequence,

\[
\frac{Q_{\Pi,t_n}(g_n)}{\varepsilon_n^2}
\to-\kappa.
\]

For the full Weil form,

\[
\frac{Q_W(g_n)}{\varepsilon_n^2}
=
[z_n,z_n]_{\mathcal J}
-
\|b_n\|^2,
\]

hence

\[
\limsup_{n\to\infty}
\frac{Q_W(g_n)}{\varepsilon_n^2}
\le-\kappa.
\]

**Standing:** CONDITIONAL.

**Abstract carriers:** WD-B1, WD-C5, WD-C9.

---

## 6. Quartet zero-moment law

The selected negative coordinate maps to a raw residue vector \(v\ne0\) satisfying

\[
\boxed{
\mathbf1^Tv=0.
}
\]

Therefore

\[
R_v(z)
=
\sum_{\rho_j\in F}
\frac{v_j}{z-\rho_j}
=
O(|z|^{-2}).
\]

**Standing:** PROVED in the selected quartet model.

**Abstract carrier:** none; this is genuinely zeta/functional-symmetry-specific structure.

---

## 7. Weighted next-jet localization

With

\[
H_v=\Xi R_v,
\]

the surviving finite/intermediate complementary field is

\[
\mathcal N_v[\psi]
=
\sum_{\mu\notin F}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}
{\Xi^{(m_\mu)}(\mu)}.
\]

The negative branch compresses to

\[
\boxed{
\text{persistent negative defect}
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
O(z^{-2})
\Longrightarrow
\text{weighted near next-jet localization}.
}
\]

**Standing:** DERIVED exact reduction.

**Open interface:** \(\texttt{AZ-NEXTJET-LOC}\) / \(\texttt{C-ACTUAL-KPH-FLOOR}\).

---

## 8. Neutral compact-window mode

For a physical neutral mode \(k\),

\[
W_ck=0.
\]

**Standing:** CONDITIONAL on existence of the neutral mode.

**Abstract carrier:** attained critical screening plus physical null-mode realization.

---

## 9. Fixed-window arithmetic operator

At fixed support \(c\),

\[
\mathcal W_c
=
\mathcal A_\infty
-
\sum_{\log n<2c}
\frac{\Lambda(n)}{\sqrt n}
(\tau_{\log n}+\tau_{-\log n})
+
\mathcal R_{\rm pole}.
\]

Only finitely many prime-power translations occur, and

\[
\Psi_c(t)=\log|t|+O_c(1).
\]

**Standing:** DERIVED from the compact-window explicit formula and standard asymptotics.

**Negative result:** finite arithmetic translations do not by themselves provide a quasianalytic regularity bootstrap.

---

# Open Horizon-1 interfaces

The following are **not proved**:

\[
\texttt{AZ-NEXTJET-LOC},
\]

\[
\texttt{C-ACTUAL-KPH-FLOOR},
\]

\[
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}.
\]

PAP/MTP closure and RH are also not proved.

The repository should be read as a theorem-bearing **defect calculus and reduction program**, not as an RH proof announcement.
