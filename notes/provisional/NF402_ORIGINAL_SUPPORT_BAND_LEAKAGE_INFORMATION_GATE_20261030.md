# NF402 — Physical-support/Fourier-band noncommutation and the missing leakage witness

**2026-10-30 PT | Canonical original obligation `W-ODD-NEG` OPEN.** Continuation of accepted NF401 original J242 242D selected signed response. This is an **exact scope-level methodological obstruction and a corrected two-quantity acceptance criterion**, not a Fourier-tail native measurement, a complement upper bound or RH proof.

## Previous → Current → Next

**Previous NF401 (accepted):** Actual 4096-bit original selected 242-vector response recovered byte-for-byte from original NF400 Actions artifact #12964112303, independent receipt and exact candidate-ball workflows [#41109578378](https://github.com/monocap-tech/weil-lab/actions/runs/41109578378) and [#41110295260](https://github.com/monocap-tech/weil-lab/actions/runs/41110295260) SUCCESS. Source original native SHA256 `644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515`. Original selected physical center `j_*=P_J P_I m(D)u4` has norm approximately 0.7028719679151. For any `j∈J242` with physical support low-band residual `||t_L-j||_I<=tau`, exact original source bounds give `||j-j_*||_I<=rho=H+tau<3.29e-13`, where `H` is the NF375 certified original full-line multiplier highband action bound at `Lambda=2^24`, `tau=2.8e-13`.

**Current NF402:** Before treating the Fourier tail of the source-determined supported `j_*` as a decisive candidate test, audit the order of **spatial restriction** and **spectral truncation**. They do NOT commute. Fourier-tail magnitude **alone** cannot imply physical low-band mismatch on the interval and cannot STOP all candidates. The correct source-specific stop must additionally pay the low-band full-line response *outside the support interval*. Source-only rational provenance replay and exact finite-dimensional noncommutation regression committed.

**Next:** Either compute actual original `||1_{|xi|>Lambda} jhat_*||` **and** independently certify an upper for `||1_{I^c} U_L||`, or bypass the whole-line Fourier-tail detour and directly certify the true supported low-band complement upper `||(I-P_J) t_L||_I`. Do not overinvest in an unidentifiable shadow.

## Original mathematical objects and exact necessary coupling

Set `I=[-11/10,11/10]`, `S=1_I`, `Lambda=2^24`, `B_L=F^{-1}1_{|xi|<=Lambda}F`, `B_H=I-B_L` on whole-line `L²(R)`. Define

```
U_L=B_L(m(D)u4)                 whole-line bandlimited response
t_L=S U_L                       original physical supported lowband response
w=S m(D)u4                      complete supported multiplier response
j_* = P_J w in J242             accepted original selected physical center
H_src >= ||S B_H(m(D)u4)||      original NF375 highband bound
tau=7/25000000000000
rho=H_src+tau<329/10^15
ell=||(I-S)U_L||_(L²(R))         UNMEASURED original outside leakage
T_* = ||B_H j_*||_(L²(R))        UNMEASURED original selected Fourier tail
```

The NF375 complete original highband bound is on `B_H m(D)u4` before support restriction (therefore also bounds its restriction). It **is not** a bound for `ell`. In the original supported realization, `||j-j_*||_I<=rho` is valid if `||t_L-j||_I<=tau`.

For any such `j`, extending the supported `j` by zero outside `I`, and using Plancherel and `B_H U_L=0`,

```
||B_H j|| <= ||j-U_L||_R
            = sqrt(||j-t_L||_I^2 + ||U_L||_(I^c)^2)
            <= sqrt(tau^2+ell^2).

T_* <= ||B_H(j_*-j)|| + ||B_H j||
    <= rho + sqrt(tau^2+ell^2).
```

Thus a **necessary original candidate existence condition** is

```
max(0, T_*-rho)^2 <= tau^2+ell^2.              (NF402)
```

To STOP all original candidates under the NF401 physical ball via this specific Fourier method, we would need independent source-authenticated data `Tlo<=T_*`, `ell<=Lupper`, and the **strict** certified inequality

```
Tlo>rho  AND  (Tlo-rho)^2 > tau^2+Lupper^2.
```

**No** `Tlo` or `Lupper` currently exists. A large measured Fourier tail alone proves no physical support mismatch. An ordinary unsigned whole-line `U_L` norm upper does not magically supply a small outside-leakage upper.

## Why Fourier tail alone carries insufficient information

On a whole-line Hilbert space, spatial projector `S` and Fourier band projector `B_L` fail to commute: `B_H S U_L` is generally nonzero even when `B_H U_L=0`. A simple exact rational finite-Hilbert witness in `scripts/local_replay/nf402_original_support_band_leakage_exact.py` takes `B_L=diag(1,0)`, `S=(1/2)[[1,1],[1,1]]`, `U_L=(1,0)`, `j=SU_L=(1/2,1/2)`. Then **physical error zero** `||j-SU_L||=0`, while `||B_H j||²=1/4>0`. This toy is **not** a calculation on the original Weil form; it is an exact counterexample to the abstract inference.

More strongly, the restrictions to the original finite interval `I` of odd `L²(R)` functions with Fourier support in `[-Lambda,Lambda]` are dense in the odd `L²(I)` space (any fixed `Lambda>0`). If an odd compactly supported test `g` is orthogonal to all such restrictions, its Fourier transform vanishes on the open interval `(-Lambda,Lambda)`; as `g` has compact support this Fourier transform is entire, and the identity theorem gives `g=0`. Thus **no generic nonzero physical approximation-error lower bound follows from the full-line highband tail of an arbitrary supported `j` alone**. The fixed original source `U_L` can still be ruled out by a source-specific computation; the density theorem does not certify that it approximates `j_*`.

This is the exact information/custody distinction: a numerical **shadow of a supported candidate** is not a measurement of **the known original whole-line source response**.

## Independent original-object acceptance alternative

The accepted NF400 geometric identity remains the simpler scope-preserving criterion:
```
min_(j in J242) ||t_L-j||_I = ||(I-P_J)t_L||_I .
```
This is necessary and sufficient for existence of *some* unrestricted physical selected candidate under the inherited Hilbert realization; **additional dyadic/endpoint/tail entry contracts** for a particular computational certificate remain separate. For the fixed `j_*=P_J w`, NF400 had the sufficient inequality `||t_L-j_*||²<=||(I-P_J)t_L||²+H_src²`; a true original upper `||(I-P_J)t_L||<=2.75e-13` would meet the original `tau=2.8e-13` physical target. This complement **upper remains OPEN**.

## Exact scope and custody

- Accepted original source NF401 native SHA256 `644337986f62a3f25bb6b2005efc82f517975c84629b32b5ae8d1e5b95614515`, NF398 highband source SHA256 `bae006e4fb542c4b0c6d184ae8cfbc2e7c924d45c89092ebda89cf0c6057c877`.
- Replayer `scripts/local_replay/nf402_original_support_band_leakage_exact.py` reads accepted NF401 original evidence and original NF398 `H`/cutoff, reproduces exact rational `rho` bound and finite exact noncommutation example; does not claim to numerically prove the infinite-dimensional density theorem (analytic proof above).
- Signed source unchanged, original 30,371 WJJ/WJF archived cells, 0 new signed kernel evaluations. Exact proof conditional on inherited original Fourier/operator realization, no global operator domain audit.
- `W-ODD-NEG`, original finite-selected complement **upper**, infinite exterior form inverse, even/whole Weil and RH all **OPEN**. No main merge.
