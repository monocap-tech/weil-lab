# IRT-0C — canonical-system / de Branges rigidity screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0B1  
**Status:** **COMPLETE PRIMARY SCREEN / CLASSICAL POSITIVE CANONICAL-SYSTEM RIGIDITY IS TOO STRONG FOR DIRECT FALSE-RH USE / ZETA-SPECIFIC SUZUKI FAMILY CONFIRMS THE BARRIER / NARROW PARAMETER-FLOW RESIDUAL SURVIVES / NEXT CURSOR IRT-0C1 SUZUKI-SHIFT PARAMETER FLOW**

## 0. Question

IRT-0B1 showed that plain local generalized-Nevanlinna realization is too weak:
the arbitrary holomorphic summand simply repackages the canonical outside field
\(A_{F,\Omega}\).

IRT-0C asks whether classical canonical systems and de Branges / Hermite--Biehler
structure provide a useful intermediate rigidity:

\[
\text{stronger than local }N(\Omega),
\qquad
\text{but weaker than an RH-strength real-spectrum assertion}.
\]

The primary screen says:

\[
\boxed{
\text{classical positive canonical-system rigidity does constrain the slack,}
}
\]

but

\[
\boxed{
\text{its natural zeta realization crosses directly into RH-strength positivity.}
}
\]

A narrower parameter-flow question remains.

## 1. Classical canonical-system structure

For a two-dimensional canonical system

\[
JY'(t,z)=zH(t)Y(t,z),
\qquad H(t)\ge 0,
\]

with the usual normalization, the Weyl coefficient is a Herglotz--Nevanlinna
function.

De Branges' inverse theorem gives, after normalization, a correspondence

\[
\boxed{
H
\longleftrightarrow
m_H\in N_0.
}
\]

Thus the canonical-system realization does not create a new class between the
classical Herglotz route and the positive Hamiltonian route: they are two sides
of the same rigidity.

Relevant sources:

- Romanov, *Canonical systems and de Branges spaces*, arXiv:1408.6022;
- Langer--Pruckner--Woracek, *Canonical systems whose Weyl coefficients have
  dominating real part*, arXiv:2108.10162;
- standard de Branges inverse spectral theory.

## 2. Hermite--Biehler endpoint rigidity

For a positive canonical system, the endpoint function

\[
E_t(z)=A_t(z)-iB_t(z)
\]

belongs to the Hermite--Biehler class.

The HB condition is

\[
|E_t(z)|>|E_t^\#(z)|,
\qquad z\in\mathbb C_+,
\]

with the usual nondegenerate version, and the associated real entire components
\(A_t,B_t\) carry the real/interlacing spectral zero structure.

Therefore if the critical-line entire function

\[
\xi_{\rm crit}(z)
=
\Xi\!\left(\frac12+iz\right)
\]

were identified directly with one of the real spectral components \(A_t\),
\(B_t\), or an equivalent self-adjoint boundary spectral determinant in a
positive canonical system, its zeros would belong to the real spectral axis.

But

\[
\xi_{\rm crit}(z)=0,\quad z\in\mathbb R
\]

is exactly the critical-line zero condition.

Hence a direct positive de Branges realization of the relevant \(\Xi\) divisor
is not a weaker mixed-divisor theorem. It is already RH-strength spectral
rigidity.

## 3. Holomorphic slack is controlled only by positivity

This answers the IRT-0B1 question precisely.

The canonical system *does* eliminate arbitrary holomorphic slack because the
transfer matrix, endpoint HB function, positive reproducing kernel, and
Nevanlinna Weyl coefficient are all tied to one positive Hamiltonian.

So the desired mechanism exists:

\[
\boxed{
\text{one dynamical realization}
\Longrightarrow
\text{rigid phase / zero-pole geometry}.
}
\]

However, the load-bearing property is positive semidefiniteness of \(H\), or
equivalently the Herglotz/HB positivity it generates.

That is the same resource already identified in IRT-0A.

## 4. Zeta-specific confirmation: Suzuki's shifted xi family

Masatoshi Suzuki studies

\[
\boxed{
\Theta_\omega(z)
=
\frac{\xi(1/2-\omega-iz)}
     {\xi(1/2+\omega-iz)},
\qquad \omega>0.
}
\]

His 2012 work gives two directly relevant facts.

First, whether \(\Theta_\omega\) is a meromorphic inner function in the upper
half-plane is directly related to RH.

Second, a canonical system associated with \(\Theta_\omega\) is constructed
explicitly and unconditionally for the large-shift regime

\[
\omega>1.
\]

Suzuki states that if the construction can be extended unconditionally to all

\[
\omega>0,
\]

then one obtains an RH criterion in which validity of RH is expressed through
positive semidefiniteness of the corresponding family of Hamiltonians.

Source:

- Masatoshi Suzuki, *A canonical system of differential equations arising from
  the Riemann zeta-function*, arXiv:1204.1827.

This is almost exactly the IRT-0C experiment already carried out in the zeta
setting.

## 5. Meaning for IRT

The Suzuki family shows that the failure is not merely a poor choice of
candidate carrier.

There is already a natural zeta-derived inner/canonical-system family for which:

\[
\boxed{
\text{far enough from the critical strip}
\Longrightarrow
\text{unconditional positive canonical system},
}
\]

while propagation of that structure toward the critical regime becomes an RH
criterion.

So the desired "rigid but false-RH-compatible classical realization" is not
visible in the most natural shifted-xi family.

## 6. Relation to the Weil/de Branges side

Suzuki's later work also studies the Hilbert space obtained from the Weil
distribution and identifies it with a de Branges space under RH.

This again places the Hilbert/de Branges positivity on the RH side of the
logical boundary rather than supplying a neutral assumption usable inside a
false-RH reductio.

Relevant source:

- Masatoshi Suzuki, *On the Hilbert space derived from the Weil distribution*,
  arXiv:2301.00421.

This matches the project distinction between:

\[
\text{Weil-form positivity}
\]

and

\[
\text{the negative-branch packet localization problem}.
\]

## 7. Exact admission tests

### Common-carrier test

**PASS in classical canonical systems.**

One transfer matrix / Hamiltonian controls Weyl, phase, and endpoint spectra.

### Holomorphic-slack test

**PASS structurally.**

The arbitrary analytic remainder of IRT-0B1 is no longer free.

### Exact-kernel test

**NOT YET A RENJET TRANSFER.**

Canonical-system realization controls the full analytic object, but no theorem
has been extracted mapping derivative-divisor data to the frozen
mode-weighted RENJET complement functional.

### Quantifier test

**GLOBAL/STRUCTURAL, NOT PACKET-LOCAL.**

The positivity law is stronger than the required local packet statement.

### False-RH compatibility

**FAIL for direct positive realization of the critical divisor.**

Positive/HB spectral structure enforces the real-axis geometry we are trying to
derive.

## 8. Classical route determination

The classical canonical-system/de Branges route therefore folds back onto
IRT-0A:

\[
\boxed{
\text{control of holomorphic slack}
\Longleftrightarrow
\text{positive Hamiltonian / Herglotz / HB rigidity}.
}
\]

For the direct critical divisor this is too strong.

IRT-0C does not locate a classical Hilbert-space realization that is
simultaneously:

1. false-RH compatible;
2. nontrivially restrictive on \(A_{F,\Omega}\);
3. and sufficient for the mixed-divisor RENJET transfer.

## 9. Surviving narrow route: parameter flow

Suzuki's large-shift construction leaves one narrower question that has not yet
been tested by IRT.

Instead of demanding full canonical-system positivity down to \(\omega=0\),
ask whether one can propagate only a **packet-local invariant** from a regime

\[
\omega>1
\]

where the canonical system is already constructed, toward a smaller shift,
with an error/monotonicity law strong enough to imply the frozen NEXTJET/KPH
bound.

The target must be strictly weaker than:

\[
H_\omega(t)\ge0
\quad\text{for all }t,\omega>0,
\]

because proving the full family positivity is RH-criterion strength.

Potential propagated objects include only those with an explicit map to the
canonical packet target, for example:

- one transfer-matrix determinant or phase derivative;
- one localized spectral measure inequality;
- one finite-window Clark mass;
- one packet-scale monotonicity identity;
- one de Branges kernel minor;
- one signed Hamiltonian integral localized to the selected window.

No such invariant has yet been identified.

## 10. New no-credit rule

The following does not count as IRT progress:

\[
\text{prove enough canonical-system positivity to imply RH}
\]

and then use RH to obtain NEXTJET.

The parameter-flow route is admissible only if it closes the local
NEXTJET/KPH interface **before** or **strictly below** the full RH-equivalent
positivity threshold.

## 11. Determination

IRT-0C is complete.

It establishes:

\[
\boxed{
\text{canonical/de Branges rigidity does solve the slack problem}
}
\]

but also:

\[
\boxed{
\text{the classical positive version is already on the RH side of the boundary.}
}
\]

The strongest surviving residue is therefore not a new de Branges
representation. It is a **partial-positivity / parameter-flow extraction**
problem inside an already natural zeta canonical-system family.

## 12. Cursor

\[
\boxed{
\texttt{IRT-0C1 / SUZUKI-SHIFT PARAMETER-FLOW AUDIT}
}
\]

Questions:

1. what exact monotone/analytic dependence on \(\omega\) is available for
   \(\Theta_\omega\), its phase, kernel, spectral measure, or Hamiltonian;
2. whether any quantity remains controlled for \(\omega\) below the fully
   positive regime without implying full innerness;
3. whether a local failure of positivity can be assigned to an off-critical
   packet with a quantitative bound;
4. whether such a packet-local defect couples to the frozen RENJET/KPH
   functional rather than merely restating RH.

No canonical theorem status changes.
