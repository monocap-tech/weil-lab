# RC309 — weighted-Schur closure of the singular Legendre endpoint matrix

**Parent:** RC308 merged at `9e0588cff619151856523f30cca1e6db419cdc54`.  
**Status:** a conditional bounded **abstract** original-action model is now possible; canonical source identification, positivity, Stage I, F4, RH and Lean remain OPEN.

## The question

RC308 established a common physical (L^2) and (D)-energy carrier for the nominal prime, regular archimedean and pole components. The omitted Legendre endpoint/diagonal operator has a kernel that behaves like (1/|n-d|) near the diagonal. That kernel has logarithmically increasing ordinary absolute row sums, which makes naive constant-(L^2) Schur estimates fail.

Crucially, the actual intended operator is **(D^{-1}E)**, with (D_n=H_n+s), (s>3), not the raw endpoint matrix (E). This normalization compensates for the logarithmic growth. RC309 makes that observation exact.

## 1. The inherited native endpoint matrix

Let (B=11/10), (m_n=2B/(2n+1)), and (H_n=sum_{k=1}^n1/k).

The same-parity endpoint coefficients appearing in the inherited original-action source evaluator are

[
E_{nd}=
egin{cases}
dfrac{2n+1}{|n-d|(n+d+1)}, & n
e d,; nequiv dpmod2,\[5pt]
2(H_{2n}-H_n)+dfrac1{2n+1}, & n=d,\[5pt]
0,&n
otequiv dpmod2.
end{cases}
]

For each off-diagonal same-parity pair,

[
m_nE_{nd}=m_dE_{dn}
=rac{2B}{|n-d|(n+d+1)}.
]

Thus the conjugate of (D^{-1}E) on the Hilbert norm

[
|a|_D^2=sum_{nge0}m_n(H_n+s)|a_n|^2
]

has a symmetric nonnegative-entry matrix

[
K_{nd}=sqrt{rac{m_n}{m_d}},
rac{E_{nd}}{sqrt{(H_n+s)(H_d+s)}}.
]

Using the strictly positive Schur test weight

[
p_n=sqrt{rac{m_n}{H_n+s}}
]

reduces the weighted row test **exactly** to

[
sum_d K_{nd}rac{p_d}{p_n}
=sum_{dequiv n;(2)}rac{E_{nd}}{H_d+s}.
]

Since (K) is symmetric, the same constant controls both weighted rows and columns.

## 2. Uniform all-degree bound — not extrapolated from sampling

For every integer (nge2), partition same-parity source indices into:

- **Low:** (d<n/2). Here (E_{nd}<4/n) and there are at most (n/4+1) eligible indices. With (s>0), the entire contribution is at most (3/s).
- **Middle:** (n/2le dle2n), (d
e n). Here (E_{nd}le2/|n-d|); the same-parity reciprocal-distance sum is at most (H_{lfloor n/2floor}), and (H_d+sge H_{lfloor n/2floor}+s). Its contribution is at most **2**.
- **High:** (d>2n). Here (E_{nd}< (4n+2)/d^2) and the full integer tail (sum_{d>2n}d^{-2}le1/(2n)). Thus it costs at most (3/s).
- **Diagonal:** (E_{nn}<3), so its contribution is at most (3/s).

The special rows (n=0,1) satisfy even smaller direct bounds. Hence **for all even and odd n, with no finite cutoff**:

[
oxed{sup_nsum_{dequiv n;(2)}
rac{E_{nd}}{H_d+s}
le 2+rac9s
le 2+rac9{s_{mathrm{lower}}}.}
]

By the weighted Schur test,

[
oxed{
|D^{-1}E|_{D	o D}
le 2+rac9{s_{mathrm{lower}}}.
}
]

The proof uses exact parity and harmonic identities and is valid for arbitrarily large indices. The validator's finite row computations are only *regression checks*, never the source of the infinite-dimensional bound.

This is a boundedness statement, **not** a claim that the endpoint matrix itself is positive-semidefinite.

## 3. Conditional bounded original-action model

RC237's original-source formula for finite Legendre inputs contains the identity contribution together with the endpoint action, a scalar diagonal subtraction of (log2+789/125), the nominal prime source, the regular archimedean convolution and the pole term.

If this inherited decomposition is the correct representation of the complete canonical original Weil action on its dense polynomial core, define the corresponding abstract model

[
N_{mathrm{model}}
=I+D^{-1}igl(E-(log2+789/125)I+S_3igr),
]

with (S_3) the bounded three-component source of RC308, using the native source signs.

Writing (C_3) for RC308's certified (D^{-1}S_3) bound gives

[
|N_{mathrm{model}}|_{D	o D}
le 1+Bigl(2+rac9{s_{mathrm{lower}}}Bigr)
+C_3+rac{log2_{mathrm{upper}}+789/125}{s_{mathrm{lower}}}.
]

The rational certificate establishes this finite number. Therefore, under the imported core identification, the **abstract model** is a bounded operator on the completed (D)-energy Hilbert carrier, and all its polynomial powers exist. This does not imply they satisfy RC292's demanding inverse-approximation or positivity thresholds.

**Identification gap:** RC309 has *not independently derived and verified* the full source identity on every polynomial degree and both parity sectors from the original global Weil formula. The decomposition is imported from the established RC237 native action and must be audited at RC310 before the bounded abstract model is equated to the canonical original operator.

## 4. Exact computational checks

The validator pins RC129, RC303, RC304, RC308, RC237 and RC252. It checks:

- exact weighted symmetry (m_nE_{nd}=m_dE_{dn});
- the native endpoint formula on low/high off-diagonal degree pairs of both parities;
- diagonal harmonic identities;
- finite positive weighted-Schur row subtotals strictly below the analytic universal bound;
- the exact rational inequalities in each interval partition for (2le n<130);
- exact rational (log2) enclosure and inherited scalar shift;
- the combined conditional bounded-model norm estimate;
- forward and reverse certificate replay under pinned input hashes.

No finite test is substituted for the universal proof.

## 5. Remaining research and next cursor

The **endpoint matrix boundedness obligation is discharged for the inherited native coefficient formula**. This is more structural progress than accumulating input columns.

What remains is the mathematical identification of the complete canonical Weil source with the abstract model, including exact action on both parities, any additional diagonal or distributional terms, and the rank-317 augmentation. Even if the identity holds, boundedness alone does **not** imply the needed positive spectral lower bound, nor any of the remaining 314-dimensional Schur positivity conditions.

**RC310:** Audit the complete dense-core action identity and extension theorem. After that, address positivity and actual signed Chebyshev residual tolerances. Stage I, original Weil positivity, global F4 and RH are OPEN.

## Reproduce

```bash
python scripts/validate_rpb108_rc309_endpoint_schur.py --output certificates/rpb108_rc309_endpoint_schur.json
python scripts/validate_rpb108_rc309_endpoint_schur.py --output certificates/rpb108_rc309_endpoint_schur.json --replay
```

The exact GitHub Actions replay verifies rational arithmetic and consistency with imported analytic formulas, not independent review or formal verification of RH.
