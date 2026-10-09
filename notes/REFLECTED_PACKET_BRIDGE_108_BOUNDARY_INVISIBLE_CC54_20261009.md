# RPB108 CC54 — Actual source-invisible near-critical retained directions

Date 2026-10-09 UTC / 2026-10-08 Pacific. Starting Coupled head `1351ddeafef708e3f0caa4f6071098bf516456c1` (CC53). Independent source head recovered read-only as `27adced74c6d676ad8153adba279bf971484a1e5`; no NF19 source/action handoff is available. [Definitions](../docs/TERMINOLOGY_RPB108_BOUNDARY_INVISIBLE_CC54.md) precede load-bearing use. Paused fronts and historical wording preserved.

**New ACTUAL original arithmetic result:** there exist original E112 vectors z in each parity whose complete signed pairing with the first exterior mode is exactly zero, with the following paid native bounds:

| Original vector at a=53/50 | Even z, phi=e112 | Odd z, phi=e113 |
| --- | ---: | ---: |
| Exact original Q(z,phi) | 0 | 0 |
| Physical mass ||z||^2 lower | >9/10 | >4/5 |
| Original Q(z,z) lower | >8e-35 | >3e-31 |
| Physical Rayleigh upper | <1e-34 | <4e-31 |
| True correction magnitude | <1e-63 | <1e-63 |

These are source-invisible positive-energy controls for the measured mode, not original Weil nulls. Separately, a native two-plane min-max certificate proves that the retained A spectral subspace below 1e-26 even / 1e-23 odd has dimension at least two. Therefore a nonzero exact first-mode-invisible vector exists even within those ACTUAL retained eigenvector subspaces. No positive first-mode lower frame bound holds on either subspace.

## 1. Actual data and candidate/proof separation

The [exact certifier](../scripts/certify_native_boundary_invisible_cc54.py) uses the authenticated original E112 and NF18 boundary sources, with uncompressed SHA256s `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81` and `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee`. NF18's exact rational witness has SHA256 `b3e23133db4562c1b28816e922f9c085899818399dcfcee74a323b4f6da10d5c`.

All original archimedean terms, both orientations of all six prime powers, and both signed poles remain. No additional native columns are generated. This is the original physical unconstrained E112/F112 split, not CC52's pole-free moment-constrained carrier.

For candidate generation only, use center matrices to propose

\[
s\approx w-\frac{b^*w}{b^*A^{-1}b}A^{-1}b,
\]

where w is the authenticated NF18 rational near-critical witness. Round each seed coordinate to denominator 10^80. Decimal precision120 is not a proof. The resulting [rational seed file](data/RPB108_BOUNDARY_INVISIBLE_CC54_SEEDS_20261009.json) is an explicit reusable artifact; all proof checks can be replayed with `--seeds`, bypassing Decimal inversion entirely.

## 2. Exact true-native source cancellation and paid energy/mass

Actual original arithmetic gives Q(e110,e112)>2/5 and Q(e111,e113)>1/2. With p the corresponding low physical unit mode, define the true original coefficient

\[
\delta=\frac{Q(s,\phi)}{Q(p,\phi)},\qquad z=s-\delta p.
\tag{CC54.1}
\]

Thus Q(z,phi)=0 exactly. The numerator is evaluated with full signed rational source intervals. Its small interval is never substituted by zero. The interval quotient proves |delta|<1e-63 in both parities, despite uncertainty in the exact value of delta.

Let D be the certified absolute upper bound on delta. Exact interval quadratic and mixed evaluations give

\[
\|z\|_2^2\ge\|s\|_2^2-2D|s_p|,
\]
\[
Q(z,z)\le Q(s,s)_{\rm upper}
+2D|Q(s,p)|_{\rm upper}+D^2|Q(p,p)|_{\rm upper}.
\tag{CC54.2}
\]

The matching lower estimate subtracts these absolute corrections. These native bounds prove the table, including strict positive original energy. Approximate seed mass is 0.96218 even / 0.85021 odd and corrected Rayleigh is about 9.4877e-35 / 3.6787e-31 (displays only). The proof uses Fraction endpoints, not these decimals.

## 3. Actual retained spectral geometry

Use the two physical vectors w and s. The exact validator forms their physical Gram M and original native Gram Q2. It proves

\[
\varepsilon M-Q_2>0,\qquad
\varepsilon_e=10^{-26},\quad\varepsilon_o=10^{-23},
\tag{CC54.3}
\]

by positive lower diagonal bounds and a strictly positive lower determinant after paying the full signed mixed interval. This also proves that the two vectors are independent: a dependent combination would have zero energy and mass, contradicting strict matrix positivity. The min-max principle then gives at least two retained eigenvalues of A below epsilon. NF17's original positive floor ensures that all retained energies are positive.

The measured b is a single linear functional, hence its restriction to a spectral subspace of dimension at least two has a nonzero kernel. For a physical unit vector v in that kernel,

\[
b(v)=0,\qquad0<Q(v,v)<\varepsilon.
\tag{CC54.4}
\]

Therefore |b(v)|^2/d>=c Q(v,v) fails for every c>0. This is an actual native retained spectral obstruction to the FIRST-MODE lower frame inference. It is not a claim that any individual eigenvector has zero source; the kernel may require a coherent combination of retained eigenvectors. It is also not a claim about eigenvectors of the whole supported Weil operator.

## 4. Relation to CC53 and the next arithmetic obligation

CC53 certifies an UPPER collective reaction of roughly20.4%/20.6%, relative to A. That upper bound and the first-mode invisibility here are compatible: a rank-one response can have a nonzero largest relative eigenvalue and a large kernel. Upper Schur control cannot be read as a lower source frame bound.

The complete response remains G=G1+T with unknown positive residual Gram T. On the vectors in (CC54.1) or (CC54.4), G1 vanishes, so all complete-source frame information must come from unmeasured response. Original energy is positive, so these controls exclude the inference 'one measured source coordinate vanishes => original null'. They do not establish full-high invisibility, negate whole positivity, or prove that the complete arithmetic cannot enforce a collective lower frame bound.

Independent NF19's source/action Gram remains the next load-bearing data. CC52's compensated-tail pivot>1/5 and constrained55-dimensional gate are preserved. No transfer to that carrier is licensed here. Whole-domain original positivity remains certified through21/20; target53/50 whole sign, all-cap defect-relative leakage/frame bound, contact exclusion, RH/F4 and Lean remain open.

[Machine-readable certificate](data/RPB108_BOUNDARY_INVISIBLE_CC54_CERTIFICATE_20261009.json) records actual signed source, exact correction/energy/mass enclosures, and two strict min-max determinant certificates. No GitHub Actions or Lean replay is claimed. No abstract crossing control is counted as new actual Weil arithmetic.
