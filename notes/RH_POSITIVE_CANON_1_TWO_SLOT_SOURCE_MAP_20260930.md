# RH-POSITIVE-CANON-1 — TWO-SLOT SOURCE MAP

Date: 2026-09-30
Branch: `investigation/rh-positive-canon`
Parent: `RH-POSITIVE-CANON-0`

Status: COMPLETE / TRACK B EXACT ENDPOINT SLOT / TRACK A NEAR SLOT / NO OVERSHOOT YET / RH NOT PROVED

## Scope

This pass only maps canonical source objects for the two Horizon-1 RH-facing slots. It does not yet traverse beyond a representative.

## Track A — AZ-NEXTJET-LOC

Project object:
[
\mathcal N_{v,R}[\psi]
=
\sum_{\mu}^{\rm near}
m_\mu\psi(\mu)
\frac{H_v^{(m_\mu)}(\mu)}{\Xi^{(m_\mu)}(\mu)},
\qquad H_v=\Xi R_v.
]

### A1. Suzuki 2023 — global resolvent/screw neighborhood

Source: Masatoshi Suzuki, *Aspects of the screw function corresponding to the Riemann zeta-function*, JLMS 108 (2023), DOI 10.1112/jlms.12785.

Pinned:
- Theorem 1.1(1), eq. (1.2): Fourier transform of the arithmetic screw datum is proportional to (-z^{-2}\xi'/\xi(1/2-iz)).
- Theorem 1.2: RH iff the associated function is a screw function.
- Theorems 1.3–1.4: RH iff the finite-interval screw forms are nonnegative/nondegenerate.

Ring: **E** for the RH-equivalence statements.

Assessment: canonical divisor-resolvent neighborhood, but not the packet-selected weighted next-jet functional. The project object still carries selected source (v), complementary-zero evaluation, multiplicity-sensitive quotient, multiplier weights, and worst-packet quantifiers.

Result: **CLOSE GLOBAL REPRESENTATIVE / NOT EXACT SLOT**.

### A2. Bondarenko–Radchenko–Seip 2023 — mixed zero-jet/integer sampling

Source: Bondarenko–Radchenko–Seip, *Fourier Interpolation with Zeros of Zeta and L-Functions*, Constructive Approximation 57 (2023), DOI 10.1007/s00365-022-09599-w.

Pinned:
- Theorem 1.1, eqs. (1.2)–(1.3): reconstruction from multiplicity-aware zeta-zero jets together with Fourier samples at (log n/(4\pi)).
- Corollary 1.1: simultaneous vanishing of both data sets forces the function to vanish.
- The interpolation loses its stated structure if a single zero or logarithmic-integer point is removed.

Ring: **A**. The theorem itself is unconditional.

Assessment: strongest current canonical jet-data architecture. It has the correct multiplicity-aware jet side and a canonical mixed arithmetic side, but no pinned theorem turns the project quantity
[
H_v^{(m_\mu)}(\mu)/\Xi^{(m_\mu)}(\mu)=R_v(\mu)
]
with its packet weights into a BRS coefficient functional while preserving project quantifiers and prime-power custody.

Result: **NEAR SLOT FOUND**.

### A3. Burnol 2004 — Sonine/de Branges evaluator systems

Source: Jean-François Burnol, *Two complete and minimal systems associated with the zeros of the Riemann zeta function*, JTNB 16 (2004), DOI 10.5802/jtnb.434.

Pinned source statement: zeta-zero systems are complete/minimal in specified extended Sonine spaces, linking zero evaluation, Fourier/co-Poisson structure, and de Branges spaces.

Ring: **A**.

Assessment: relevant evaluator ancestry, but farther than BRS because native metric, support, and packet-weight transport remain unmatched.

Result: **RELATED / NOT CURRENT LEAD**.

### Track-A determination

No exact published representative of the weighted packet next-jet field was found in this pass.

Nearest canonical neighborhood:
[
\boxed{
\text{divisor resolvent}
+
\text{multiplicity-aware zero jets}
+
\text{mixed logarithmic-integer sampling}
}
]

Current lead: **BRS Theorem 1.1**.

---

## Track B — AZ-FIN-WEIL-NULL-EXTENSION

Project endpoint:
[
k\ne0,\qquad W_ck=0,
]
under the explicit Horizon-1 carrier-identification hypothesis that this is the compact-window Weil form/operator.

### B1. Suzuki 2026 — localized Weil operator

Source: Masatoshi Suzuki, *Weil's quadratic form via the screw function*, arXiv:2606.09096v3.

Pinned:
- eq. (1.1): (Q_W^a(v)=\langle A_av,v\rangle).
- eqs. (1.4)–(1.6): (G_a=P_aGP_a), (B_a=D^*G_aD), domain (H_0^1(-a,a)).
- Theorem 1.1: (A_a) is the Friedrichs extension of (B_a).
- eq. (1.7): the bottom spectral value (\lambda_a) is attained.
- Theorem 1.3: (\lambda_a) is continuous in (a).

Ring: **A** for the operator construction and continuity theorem; the surrounding RH/nondegeneracy criterion is **E**.

Assessment: this is the exact canonical endpoint slot at the level of the localized Weil form/operator. After support/convention identification (a=c), the project neutral object corresponds to a localized Weil zero mode:
[
\boxed{A_ck=0}.
]

The notation-level identity (W_c=A_c) is not promoted until the convention/domain audit is performed, but the form/operator role is the same by the project's own carrier-identification hypothesis.

Result: **EXACT ENDPOINT SLOT FOUND**.

### B2. Suzuki 2023 — continuous screw-kernel representation

Pinned:
- Theorem 1.3: under RH the finite-interval screw form is positive definite.
- Theorem 1.4: RH iff the finite-interval screw operator has no zero eigenvalue for every (a>0).
- Theorem 1.5: the screw operator is trace class unconditionally.

This supplies the nearby canonical stack
[
G_a
\xrightarrow{D^*(\cdot)D}
B_a
\xrightarrow{\text{Friedrichs}}
A_a.
]

Result: **EXACT NONDEGENERACY NEIGHBORHOOD**.

### Track-B determination

The neutral endpoint is no longer canonically untyped. The remaining interface is specifically about the same localized Weil null mode under strict-right interval enlargement, including threshold corrections.

So:
[
\boxed{
\texttt{AZ-FIN-WEIL-NULL-EXTENSION}
\neq
\text{“identify the neutral object”}
}
]

It is now localized as a support/spectral-variation question beyond an identified canonical endpoint.

---

## Determination

- Track A exact slot found: **NO**
- Track A near slot: **YES — BRS mixed interpolation**
- Track A RH-equivalent surrounding structure: **YES — Suzuki 2023**
- Track B exact endpoint slot: **YES — Suzuki 2026 localized Weil operator**
- Track B null-extension theorem found: **NO**
- Dependency overshoot performed: **NO**
- RH proved: **NO**

## Next cursor

[
\boxed{
\texttt{RH-POSITIVE-CANON-2 / LOCALIZED-WEIL SLOT OVERSHOOT}
}
]

Next pass only:
1. start at (A_ck=0);
2. traverse one construction edge backward;
3. traverse one spectral/nondegeneracy edge forward;
4. compare interval variation with the project's same-vector strict-right extension;
5. stop at the first typed dependency mismatch.

Do not begin Track-A BRS transport in the same pass.
