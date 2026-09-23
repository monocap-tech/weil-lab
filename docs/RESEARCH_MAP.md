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
\text{H1-P1 ACTIVE}.
}
\]

The RH-facing statements at the bottom of this map are **interfaces out of Horizon 1**, not Horizon-1 completion requirements. Terminology is governed by the [Terminology Registry](TERMINOLOGY.md).



## Abstract screening normal form

H1-P1.0 has extracted a zeta-independent synthesis model. For

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

The abstract screening taxonomy is therefore:

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

See [Abstract Defect Calculus](ABSTRACT_DEFECT_CALCULUS.md).

H1-P1.1 now adds the selected/background transfer rule. For a finite selected negative sector (M) and background (B),

[
D_{m full}=D_M-S_BS_B^*,
]

so selected negativity survives aggregation but aggregate negativity does not preserve selected custody.

If the background is contractively screenable with reduced map (X_B), define

[
R_B=I-X_BX_B^*,
qquad
S_{m eff}=S_+R_B^{1/2}.
]

Then the selected problem restarts as

[
D_{m full}
=
S_{m eff}S_{m eff}^*
-
S_MS_M^*.
]

For fixed finite (M), the reduced residual screening map (Y) satisfies

[
operatorname{ind}_-
=
#{sigma_j(Y)>1},
qquad
operatorname{nul}_J
=
#{sigma_j(Y)=1}.
]

Therefore non-attained approximate neutrality can arise only through an infinite or moving limiting mechanism, not from a single fixed finite selected packet.

See [Restricted-Channel Transfer](RESTRICTED_CHANNEL_TRANSFER.md).

## Core dependency graph

\[
\boxed{
\begin{array}{c}
\text{finite Weil negative index}\\
\downarrow\\
\text{finite negative modes}\\
\downarrow\\
\text{infinite spectral screening}
\end{array}
}
\]

The zeta-specific work had isolated two explicit branches, but H1-P1.0 shows that the abstract screening boundary contains an additional non-attained critical case. Its zeta-Weil status remains to be determined in H1-P2/P3:

\[
\begin{array}{ccc}
&\text{screening boundary}&\\
\swarrow && \searrow\\
\textbf{negative persistence}&&\textbf{neutral persistence}\\
\downarrow&&\downarrow\\
\text{normalized negative ray}&&W_ck=0\\
\downarrow&&\downarrow\\
\mathbf1^Tv=0&&
\log|D|+\text{finite shifts}+\text{pole}\\
\downarrow&&\downarrow\\
O(z^{-2})&&
\text{logarithmic regularity only}\\
\downarrow&&\downarrow\\
\text{weighted next-jet localization}&&
\text{null-extension/support rigidity}
\end{array}
\]

Only after the negative and attained-neutral branches are understood—and the approximate-neutral branch is either specialized or excluded—does the actual-zeta RH-facing problem begin.

## Three layers

### A. General defect structure

Objects intended to survive abstraction away from zeta-specific arithmetic:

- finite negative index;
- finite-to-infinite spectral screening;
- rank-one positivity defects;
- negative versus neutral persistence;
- operator-null modes;
- graph/minimum-compensator relations.

### B. Zeta-Weil attachment

Objects using the actual quartet/explicit-formula geometry:

- antisymmetric quartet residue coordinates;
- zero-moment conservation;
- \(O(z^{-2})\) rational far field;
- completed-\(\Xi\) weighted next jets;
- compact-window prime shifts;
- logarithmic archimedean order.

### C. RH-facing exclusion

The unresolved statements that must attach the abstract machinery to the actual zeta divisor:

- worst-packet next-jet control;
- an actual KPH floor or equivalent transversality statement;
- neutral null-extension/support rigidity.

## Current frontier

### Negative branch

\[
\boxed{
\texttt{AZ-NEXTJET-LOC}
}
\]

or an equivalent actual-zeta theorem excluding the required weighted near-field compensation.

### Neutral branch

\[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
}
\]

or an equivalent support theorem for the logarithmic-order compact-window operator.

## Current H1-P1 cursor

[
oxed{
	exttt{H1-P1.2 / SUPPORT FILTRATION AND PERSISTENCE LIMITS}
}
]

The remaining abstraction target is the support/observation filtration: right-limit analysis spaces, persistence across a critical endpoint, representative blow-up, and moving finite-sector limits.

## Next consolidation pass

The next theorem-extraction pass should minimize hypotheses and classify each result as one of:

1. **general Weil/Pontryagin defect theorem**;
2. **zeta-Weil theorem**;
3. **RH-facing corollary or open obligation**.

The goal is to make the first two categories independently intelligible even if the third remains open.
