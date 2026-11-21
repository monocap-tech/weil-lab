# Weil-Lab — CP024
## Original-source Stirling–Cauchy phase envelopes without sampled digamma values

**Independent CP### cross-projection research, stacked on CP023 PR #845 → CP022 #844 → CP021 #843 → CP020 #842 → CP019 #840 → CP018 #839, etc.** This is an **analytic-only** step while original IV### signed Weil and NF### numerical Lean acceptance remain the runner priority. Independent PI### pole–prime–Gamma comparisons are not mutated.

**Result level:** The analytic argument below gives *mathematically rigorous uniform bounds from original published complex-analytic theorems*, with all new scalar inequalities independently checked by exact rational arithmetic. The original phase/second derivative theorem attachment, the Cauchy-for-Stirling-composite proof, and original ζ-remainder Cauchy/complex derivative enclosures have **NOT** gained NEW local Lean 4.35 kernel receipts. No new Lean module is introduced. It is incorrect to label this a new LEAN PASS, a complete original Hardy-`Z` curvature certificate, a spectral dictionary, Weil positivity or RH.

## 1. Actual source finding: the original Euler–Maclaurin–Stirling theorem already controls the phase

The frozen original Zeta commit is `smmercuri/zeta@c06b4e13d9c847e50a32c3d738271cbad62ae9f3`. In `Zeta/Gamma/DigammaStirling.lean` the **published**, genuine original `Complex.Stirling.norm_digamma_sub_log_le'` establishes, for (a>0) and (a\le\Re z),

[
\boxed{
\left|\psi(z)-\Log z+\frac1{2z}\right|
\le \left(\frac1{12}+\frac3{2\pi^2 a}\right)|z|^{-2}.
}
]

In `Zeta/Gram/Averaging.lean` the original genuine `hasDerivAt_riemannSiegelTheta` states

[
\boxed{
\theta'(t)=\frac12\big(\Re\psi(w(t))-\log\pi\big),
\qquad w(t)=\frac14+\frac{it}{2},\quad t>0.
}
]

In `Zeta/Gamma/TrigammaDecay.lean` the original `Complex.im_deriv_digamma_nonpos` proves (Im\psi'(w)\le0) for (\Re w>0,\Im w\ge0). This gives (\theta''(t)=-\frac14\Im\psi'(w(t))\ge0) by differentiating the true original phase identity. The corresponding explicit second phase derivative is a **new CP019 Lean source candidate**, so kernel attachment of this combination is still outstanding.

**Important source correction:** Neither the original Hardy-`Z` function-value error bound nor any sample of (\psi) is differentiated. The phase derivative bounds are controlled from the genuine original *holomorphic* digamma–Stirling remainder and a separately published Mathlib complex Cauchy derivative theorem.

## 2. Uniform geometry on the entire frozen interval

Fix

[
I=[149.5,150.05353],\qquad w(t)=1/4+it/2.
]

Since (149.5\le t\le150.05353), the triangle inequality and imaginary part norm give the **exact, uniform** inequalities

[
\frac{299}{4}=74.75\le |w(t)|
\le\frac14+\frac{150.05353}{2}=75.276765<76.
]

In particular, (74\le|w(t)|\le76), (\Re w=1/4), and (\Im w\ge0).

Define

[
H(z)=\psi(z)-\Log z+(2z)^{-1}.
]

On **every closed complex disk**

[
D_t=\{z:|z-w(t)|\le\tfrac18\},
]

we have (\Re z\ge1/4-1/8=1/8>0) and

[
|z|\ge |w(t)|-1/8\ge597/8=74.625>74.
]

The original source `Complex.differentiableAt_digamma`, ordinary complex logarithm holomorphy on the positive real half-plane and the inverse chain rule imply (H) is holomorphic on a neighborhood of this disk. The original Mathlib v4.35 `Complex.norm_deriv_le_of_forall_mem_sphere_norm_le` applies with center (w(t)) and radius (1/8). **This holomorphy/Cauchy assembly is an explicit new Lean proof obligation, not a newly accepted local kernel theorem.**

## 3. First phase derivative: prove (\boxed{2/5\le\theta'\le9/5})

At (z=w(t)), take (a=1/4) in the genuine source Stirling error bound and use (\pi>3), (|w|\ge74):

[
\begin{aligned}
|H(w)|
&\le\left(\frac1{12}+\frac3{2\pi^2(1/4)}\right)|w|^{-2}\\
&<\frac{3/4}{74^2}
=\frac3{21904}<\frac1{5000}.
\end{aligned}
]

Since (|(2w)^{-1}|\le1/148), (\Re\Log w=\log|w|), and the real part is dominated by complex norm,

[
\boxed{
|\Re\psi(w)-\log|w||\le\frac1{148}+\frac1{5000}
=\frac{1287}{185000}<\frac1{100}.
}
]

The original (3<\pi<4) bounds give

[
\frac{37}{2}=\frac{74}{4}
\le\frac{|w|}{\pi}
\le\frac{76}{3}<32.
]

For the **upper logarithm**, the genuine Mathlib `Real.log_two_lt_d9` states (log2<0.6931471808<7/10). Thus

[
\log\frac{|w|}{\pi}\le\log32
=5\log2<\frac72.
]

For the **lower logarithm**, the original published Mathlib inequality `Real.one_sub_inv_le_log_of_pos` supplies (log x\ge1-x^{-1}), so (x\ge37/2) gives

[
\log\frac{|w|}{\pi}\ge1-\frac2{37}=\frac{35}{37}.
]

Combining with the original exact (\theta') formula and the source Stirling (1/100) bound,

[
\boxed{
\frac{3463}{7400}
=\frac12\left(\frac{35}{37}-\frac1{100}\right)
\le \theta'(t)
\le\frac12\left(\frac72+\frac1{100}\right)
=\frac{351}{200}
}
]

for **all (t\in I)**.

The exact rational comparisons (3463/7400>2/5) and (351/200<9/5) yield the simple **source-derived analytic phase envelope**

[
\boxed{\frac25\le\theta'(t)\le\frac95}
\qquad\forall t\in I.
]

This is a mathematically derived bound from genuine published source lemmas plus elementary analytic inequalities; the required *new composed Lean theorem and original phase derivative bridge* are still not accepted.

## 4. Second phase derivative: complex Cauchy directly bounds the original trigamma

On any boundary point (z\in\partial D_t), the **same genuine original Stirling bound** with (a=1/8), (\pi>3), and (|z|\ge74) yields

[
\begin{aligned}
|H(z)|&
\le\left(\frac1{12}+\frac3{2\pi^2(1/8)}\right)|z|^{-2}\\
&<\frac{17/12}{74^2}
=\frac{17}{65712}
<\frac1{3000}.
\end{aligned}
]

Genuine complex Cauchy now gives

[
\boxed{
|H'(w)|\le\frac{(1/3000)}{1/8}
=\frac1{375}.
}
]

Differentiate the *analytic definition* of (H=\psi-\Log+(2z)^{-1}), not an inequality:

[
\psi'(w)=\frac1w+\frac1{2w^2}+H'(w).
]

Therefore,

[
\boxed{
|\psi'(w)|
\le\frac1{74}+\frac1{2\cdot74^2}+\frac1{375}
=\frac{66827}{4107000}
<\frac1{50}.
}
]

The original phase curvature identity gives (|\theta''(t)|<1/200), while original source `Complex.im_deriv_digamma_nonpos` gives (\theta''(t)\ge0). Hence

[
\boxed{
0\le\theta''(t)\le\frac1{200}
}
\qquad\forall t\in I.
]

**Significance:** CP023's *assumed* ( |\theta'|\le2, |\theta''|\le1) have now been replaced by explicit analytically derived stronger envelopes using published original source results. The remaining gap is the new **Lean formal assembly**, not missing numerical phase samples or another external special-function theorem.

## 5. A sharper exact finite-approximant interface

CP023's original Hardy-`Z` remainder formulas remain the exact analytic ones, with (R=\zeta-A_{6,256}):

[
Z_R'(t)=\Re[e^{i\theta}i(\theta'R+R')],
]

[
Z_R''(t)=\Re[e^{i\theta}(
-\theta'^2R-2\theta'R'-R''+i\theta''R)].
]

The previously derived **original complex Euler–Maclaurin remainder** uniform Cauchy targets are **still unaccepted local CP019–CP022 Lean source candidates**:

[
|R|\le3/10^{13},\quad
|R'|\le12/10^{13},\quad
|R''|\le96/10^{13},\quad
|R'''|\le1152/10^{13}.
]

Under these existing **UNCOMPILED** zeta-remainder derivative hypotheses, and using the improved *source-derived phase* bounds above, the exact rational error budgets become:

[
\boxed{
|Z_R'|
\le\frac95\frac3{10^{13}}+\frac{12}{10^{13}}
=\frac{87}{5\cdot10^{13}}
=1.74\times10^{-12},
}
]

[
\boxed{
|Z_R''|\le
\left(\frac{81}{25}+\frac1{200}\right)
\frac3{10^{13}}+
2\frac95\frac{12}{10^{13}}+
\frac{96}{10^{13}}
=\frac{29787}{200\cdot10^{13}}
=1.48935\times10^{-11}.
}
]

These improve CP023's respective (1.8\times10^{-12}) and (1.59\times10^{-11}) allowances. CP024's mathematical phase estimates no longer require invented future numerical phase boxes. Formal original v4.35 kernel acceptance remains mandatory before numerical custody is promoted.

Consequently, **the sufficient finite original approximant conditions** become

[
\boxed{
Z_A'(149.5)\ge\frac{12}{5}+\frac{87}{5\cdot10^{13}}
}
]

and

[
\boxed{
\forall t\in I,\quad
|Z_A''(t)|\le
4-\frac{29787}{200\cdot10^{13}}.
}
]

No finite-approximant derivative enclosure proving either inequality has yet been accepted. The remaining numerical task is the original finite Euler–Maclaurin (255)-term sum and corrections, with cancellation-preserving complex ball arithmetic and original zero-bracket sign certificates.

## 6. Exact arithmetic, immutable source custody, compiler status

`scripts/cp024_source_digamma_stirling_cauchy_phase_bounds.py` is an **executable exact rational arithmetic source preflight**, not a proof checker for complex analysis. Its main test covers: exact endpoint and complex-disk geometry; (a=1/4) and (a=1/8) source Stirling coefficient majorants; complex Cauchy (1/375) residual-derivative transfer; exact (\psi') bound; original log2 upper and lower-log inequalities; exact final (\theta',\theta'') rational bounds; improved original Hardy-`Z` remainder error buffers; and multiple deliberately false overly tight bounds as negative controls.

**All scalar `fractions.Fraction` assertions were independently executed locally and passed.** The code guards against accidentally applying the digamma disk radius (1/8) to the original complex zeta Euler–Maclaurin remainder radius (1/4), whose derivative bounds are separately (3,12,96,1152) in units (10^{-13}).

Its six original immutable source SHA + theorem-signature gates were directly checked against actual GitHub contents:

| Primary source | True frozen Git blob | Needed theorem |
|---|---|---|
| Zeta `Zeta/Gamma/DigammaStirling.lean` | `9b5a21dfefe6c778411b03fc7e0cf8e8c5bcfac8` | `Complex.Stirling.norm_digamma_sub_log_le'` |
| Zeta `Zeta/Gamma/TrigammaDecay.lean` | `60b6e9a4645d06988d2ca2d293b141195382d37c` | `Complex.im_deriv_digamma_nonpos` |
| Zeta `Zeta/Gram/Averaging.lean` | `6a30171433903a57736de2ab83b120ef660e08bd` | `hasDerivAt_riemannSiegelTheta` |
| Mathlib4 v4.35 `Mathlib/Analysis/Complex/Liouville.lean` | `70382d63ec267d2704790b1d77692e1f5cd5faed` | `Complex.norm_deriv_le_of_forall_mem_sphere_norm_le` |
| Mathlib4 v4.35 `Mathlib/Analysis/Complex/ExponentialBounds.lean` | `bbc13e49781e7f620ffa0b69d693e753d2190cb8` | `Real.log_two_lt_d9` |
| Mathlib4 v4.35 `Mathlib/Analysis/Complex/Norm.lean` | `0e2b6317a777c4d168a9098fb17ad33323efd4c3` | `Complex.abs_re_le_norm` |

The exact arithmetic and source contracts are required to run before the new source-only receipt `CP024_SOURCE_BASED_STIRLING_CAUCHY_PHASE_BUDGET_PASS_NOT_LEAN` can be issued. Its JSON explicitly marks **not Lean** and false for all pending actual phase and zeta-remainder kernel acceptance, original full Hardy-`Z` curvature, actual root sign and global Weil/spectral claims.

The **existing opt-in only** `.github/workflows/cp021-original-independent-leaf-source-only-opt-in.yml` was extended with a single additional CP024 source/math stage (downloads five additional original files and reuses the existing Complex Norm pin). It remains triggered only by explicit PR label `cp021-leaf-source` or eligible manual dispatch; **no new workflow file, no normal push/PR-created/synchronize fanout, no job launched**. The genuine original v4.35 two-leaf kernel workflow still needs a dispatch and actual accepted `.olean`/standard-axiom receipts; CP024 adds no further uncompiled Lean module.

Live GitHub evidence on CP021 PR #843: inherited CP014 **source-lineage** run `44878586072` completed with **success**, and separate CP013 source-lineage run `44878586071` was still **queued** at inspection. A successful source-lineage run is **not** a new original Lean kernel receipt.

## 7. Compatibility/invariance boundary

The Stirling bounds are intrinsic analytical facts about the genuine original Gamma phase (	heta), but the **numerical envelopes (2/5,9/5,1/200)** and the resulting Hardy-`Z` local derivative margins depend explicitly on the frozen height interval and the chosen complex radius. They are not invariant under arbitrary support relocation in the original signed Weil test space.

The exact identity (Z=Z_A+Z_R) is a genuine analytic representation, not an equality between the original signed Weil `Pole−Prime+Gamma` bilinear form and a normalized complete spectral/zero-side (3\times3) quadratic form. Such a dictionary, its preservation laws and missing normalization/positivity hypotheses remain separate and **OPEN**.

**Next CP025:** (i) obtain actual original 4.35 compiler feedback for the independent germ/Borwein leaves (no compiler pass has occurred); (ii) formalize the newly analytic, source-grounded (	heta') and (\theta'') envelopes from original DigammaStirling/Stirling-Cauchy theorems when capacity permits; (iii) construct genuine validated whole-interval finite (A_{6,256}) derivative balls preserving phase cancellation; (iv) separately certify the original narrow root sign and canonical ordinal attachment. Original signed Weil–full spectral equivalence, global Weil positivity and RH remain open.

**No global RH or Weil positivity claim.**
