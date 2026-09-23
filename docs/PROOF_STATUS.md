# Proof Status

This file records the standing of the current Weil-defect results. It is deliberately stricter than the project README.

## H1-P1 abstract theorem package

The first abstraction pass has produced the following zeta-independent results.

| Label | Statement | Standing |
| --- | --- | --- |
| WD-A1 | (J)-sign on the analysis space is represented by (D=S_+S_+^*-S_-S_-^*), with matching negative index | PROVED |
| WD-A2 | (D\succeq0) iff the negative synthesis factors contractively through the positive synthesis | PROVED using imported Douglas factorization |
| WD-A3 | Under exact range inclusion, the analysis space is (operatorname{graph}(-X^*)) for the reduced screening solution | PROVED |
| WD-A4 | Complete screening taxonomy: range defect, over-budget negative, strict positive, attained neutral, non-attained approximate-neutral | PROVED |
| WD-A5 | The rank-one defect is the one-negative-channel specialization | PROVED |
| WD-A6 | Increasing positive channels give monotone Loewner screening and nonincreasing negative index | PROVED |
| WD-E1 | Finite strict negativity can screen completely to zero in the infinite limit | PROVED EXAMPLE |
| WD-E2 | Critical screening norm need not produce an actual neutral vector | PROVED EXAMPLE |

The canonical statements and proofs are in [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md).

A major correction follows:

[
oxed{
	ext{zero screening margin}

otRightarrow
	ext{existence of a neutral vector}.
}
]

The norm-one screening operator may fail to attain its norm, producing only an approximate-neutral sequence.

---

## H1-P1.1 restricted-channel theorem package

| Label | Statement | Standing |
| --- | --- | --- |
| WD-B1 | Selected negativity survives addition of negative background; converse custody fails | PROVED |
| WD-B2 | An (m)-dimensional selected negative sector creates at most (m) negative directions | PROVED |
| WD-B3 | Selected and background channels consume one shared screening budget | PROVED |
| WD-B4 | Contractively screenable background reduces to a residual positive synthesis | PROVED |
| WD-B5 | Finite selected-sector inertia is counted by singular values of the reduced residual screening map | PROVED |
| WD-B6 | Legitimate residual-budget elimination can be iterated | PROVED |
| WD-B7 | Complement elimination replaces direct compression by a Schur/shorted covariance | PROVED in the strictly positive setting |
| WD-B8 | Finite positive shadows preserve negative signature but not analysis-space admissibility | PROVED |
| WD-E3 | Individually screenable channels need not be jointly screenable | PROVED EXAMPLE |
| WD-E4 | Direct finite-target covariance can stay strong while shorted covariance collapses | PROVED EXAMPLE |

A fixed finite selected sector has no non-attained critical branch: if its reduced residual screening map (Y) has (|Y|=1), finite rank forces norm attainment and therefore an actual neutral mode.

See [Restricted-Channel and Finite-Index Transfer](RESTRICTED_CHANNEL_TRANSFER.md).

---

## 1. Finite negative-index theorem

For finite symmetric zero sets, the finite Weil matrix has one negative direction per nonreal conjugate pair. In the two-quartet specialization used in the present program,

\[
\operatorname{ind}_{-}=4,
\qquad
\operatorname{ind}_{-}^{+}
=
\operatorname{ind}_{-}^{-}
=
2.
\]

**Standing:** imported theorem + exact specialization.

**Not implied:** survival of a strictly negative eigenvalue in the infinite-zero limit.

---

## 2. Spectral screening

Let

\[
\lambda^-_{N,k}<0
\]

be a negative eigenvalue in a finite truncation containing the selected off-axis cells and finitely many critical-line ordinates.

The infinite-dimensional obstruction is that

\[
\lambda^-_{N,k}\uparrow0
\]

may occur as the critical-line complement is restored.

This is the project’s **spectral screening** distinction:

\[
\boxed{
\text{finite negative index}
\neq
\text{infinite negative-mode survival}.
}
\]

**Standing:** structural theorem/reduction.

---

## 3. Rank-one defect formulation

The selected-cell screening problem admits the operator form

\[
\mathcal K_C(t)
=
\widetilde S_t\widetilde S_t^*
-
\widetilde g_C\otimes\widetilde g_C.
\]

The corresponding threshold satisfies

\[
C_*(t)\le1
\iff
\mathcal K_C(t)\succeq0.
\]

**Standing:** derived.

---

## 4. Critical-line tail monotonicity

For the truncated denominator \(D_N\) and completed denominator \(D_\infty\),

\[
D_\infty(h)\ge D_N(h),
\]

so

\[
Q_\infty(h)
=
\frac{|\langle g,h\rangle|^2}{D_\infty(h)}
\le
\frac{|\langle g,h\rangle|^2}{D_N(h)}
=
Q_N(h).
\]

Thus adding omitted critical-line zeros cannot increase the quotient.

**Standing:** proved with stated input definitions.

---

## 5. Persistent normalized negativity

Assume a PAP/MTP-1 negative-persistence branch and write

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

**Standing:** conditional theorem.

**Condition:** existence of the persistent negative ray.

---

## 6. Quartet zero-moment law

The selected negative coordinate maps to a raw residue vector \(v\neq0\) satisfying

\[
\mathbf1^T v=0.
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

**Standing:** proved in the selected quartet model.

**Important scope:** no stronger universal moment cancellation has been established.

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

Thus the current negative branch compresses to

\[
\boxed{
\text{persistent negative defect}
\Longrightarrow
\mathbf1^Tv=0
\Longrightarrow
O(z^{-2})\text{ far decay}
\Longrightarrow
\text{weighted near next-jet localization}.
}
\]

Persistence also yields

\[
u=-X^*a.
\]

Eliminating \(a\) strongly enough to obtain a stronger \(u\)-only law would require the missing marker/PAP theorem and would be circular.

**Standing:** exact reduction.

**Open gate:** \(\texttt{AZ-NEXTJET-LOC}\) / \(\texttt{C-ACTUAL-KPH-FLOOR}\).

---

## 8. Neutral compact-window mode

For a physical neutral mode \(k\),

\[
C_cu=P_c^*k,
\qquad
C_c^*C_cu=u,
\qquad
N_c^*k=-u.
\]

With

\[
W_c=P_cP_c^*-N_cN_c^*,
\]

one obtains

\[
\boxed{W_ck=0}.
\]

**Standing:** conditional theorem.

**Condition:** existence of the neutral mode.

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

Only finitely many prime-power translations occur.

The principal symbol satisfies

\[
\Psi_c(t)=\log|t|+O_c(1).
\]

Consequently the natural form norm is logarithmic rather than positive-Sobolev:

\[
Q_c(f)+C_c\|f\|_2^2
\asymp
\int_{\mathbb R}
\log(e+|t|)
|\widehat f(t)|^2\,dt.
\]

**Standing:** derived from the compact-window explicit formula and standard asymptotics.

**Negative result:** finite arithmetic translation structure does not by itself provide a quasianalytic regularity bootstrap.

---

## 10. Open obligations

The following are **not proved** in this repository:

\[
\texttt{AZ-NEXTJET-LOC},
\]

\[
\texttt{C-ACTUAL-KPH-FLOOR},
\]

\[
\texttt{AZ-FIN-WEIL-NULL-EXTENSION},
\]

PAP/MTP closure, and RH.

The repository should be read as a theorem-bearing **defect calculus and reduction program**, not as an RH proof announcement.
