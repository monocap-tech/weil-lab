# IRT-0A — Weyl/Herglotz two-spectra screen

**Date:** 2026-10-02 (America/Los_Angeles)  
**Repository:** \`monocap-tech/weil-lab\`  
**Branch:** \`research/inverse-realization-transfer\`  
**Parent:** IRT-0 launch  
**Status:** **COMPLETE ARCHITECTURE SCREEN / STRONG FORMAL MATCH / DIRECT CLASSICAL HERGLOTZ TRANSFER BLOCKED BY REAL-SPECTRUM POSITIVITY / RANK-ONE TWO-SPECTRA MECHANISM IDENTIFIED / NEXT CURSOR IRT-0B GENERALIZED NEVANLINNA-PONTRYAGIN**

## 0. Question

Can the missing NEXTJET mixed-divisor transfer be modeled on a mature
non-number-theoretic theorem in which zeros and poles of one meromorphic
function are two coupled spectra of one realized operator?

For the classical Weyl/Herglotz setting, the answer is:

\[
\boxed{\text{YES as theorem architecture; NO as a direct false-RH input.}}
\]

The obstruction is not absence of a transfer theorem. It is the positivity /
self-adjointness structure that makes the theorem true.

## 1. Foreign theorem architecture located

A scalar meromorphic Herglotz-Nevanlinna function is characterized, up to the
appropriate growth/normalization conditions, by a real simple interlacing
zero/pole pattern.

This is exactly the qualitative coupling IRT sought:

\[
\boxed{
\text{one meromorphic carrier}
+
\text{Herglotz positivity}
\Longrightarrow
\text{coupled zero/pole spectra}.
}
\]

Relevant source:

- Jakob Reiffenstein, *Higher-order interlacing for matrix-valued meromorphic
  Herglotz functions*, J. Math. Anal. Appl. 514 (2022), 126260,
  arXiv:2108.10746.

The same architecture is standard in Weyl \(m\)-function theory: a
self-adjoint realization produces a Herglotz \(m\)-function whose poles encode
one spectral problem, while zeros or a Möbius transform encode another boundary
condition / rank-one perturbation.

## 2. Rank-one perturbation gives the cleanest exact model

Let \(A\) be self-adjoint with cyclic vector \(\varphi\) and Weyl/resolvent
scalar

\[
m(z)=\langle \varphi,(A-z)^{-1}\varphi\rangle.
\]

For a real rank-one perturbation, the perturbed scalar denominator has the
schematic form

\[
1-\alpha m(z).
\]

The original and perturbed spectra are therefore coupled by one common
Herglotz object. In the discrete self-adjoint case the two spectra interlace.

Dobosevych--Hryniv (2021) completely characterize possible eigenvalues of
rank-one perturbations of a self-adjoint operator with discrete spectrum and
study reconstruction of the perturbation from its spectrum. In the
self-adjoint rank-one case, the non-common eigenvalues of the original and
perturbed operators strictly interlace.

This supplies an exact theorem schema:

\[
\boxed{
\text{common resolvent scalar}
\to
\text{two spectra}
\to
\text{inverse reconstruction}.
}
\]

Relevant source:

- O. Dobosevych and R. Hryniv, *Direct and Inverse Spectral Problems for
  Rank-One Perturbations of Self-adjoint Operators*, Integral Equations and
  Operator Theory 93 (2021), article 18.

## 3. Two-spectra reconstruction is genuinely stronger than two formulas

Classical and modern Sturm--Liouville inverse results reconstruct the
underlying operator/potential from two spectra because both spectra arise from
different boundary realizations of the same differential expression.

Examples located in this screen include:

- Hryniv--Mykytyuk, *Inverse spectral problems for Sturm-Liouville operators
  with singular potentials, II. Reconstruction by two spectra*,
  arXiv:math/0301193;
- Guliyev, *On two-spectra inverse problems*, arXiv:1803.02567;
- Pronska, *Reconstruction of energy-dependent Sturm-Liouville equations from
  two spectra*, arXiv:1205.4499.

The load-bearing fact is therefore not

\[
\text{EF}_1+\text{EF}_2.
\]

It is

\[
\boxed{
\text{both spectra are boundary/rank-one views of one realized operator}.
}
\]

This validates the NJDG-7 warning: separate explicit formulas for the
\(\Xi\)- and \(\Xi'\)-divisors do not create a mixed transfer.

## 4. Common-carrier test

### Foreign Weyl setting

**PASS.**

Both spectra come from one self-adjoint operator/differential expression,
usually through changed boundary conditions or rank-one perturbation.

### Current zeta setting

**OPEN / NOT ATTACHED.**

For

\[
U(z)=\frac{\Xi'(z)}{\Xi(z)},
\]

the original divisor is the pole divisor and the derivative divisor is the
zero divisor, so they already inhabit one meromorphic function.

However, merely inhabiting one meromorphic function is weaker than being two
spectra of one self-adjoint/Weyl realization.

No such zeta realization is supplied by NJDG or IRT-0A.

## 5. Exact-kernel test

Two-spectra reconstruction can, in principle, reconstruct the full Weyl
function rather than merely finitely many rational jets. Once the Weyl object
is recovered, arbitrary lawful spectral functionals encoded by that object can
be formed.

Therefore the foreign architecture is not trapped by the NJDG-6 finite-row
nonspan in the same way.

This is the first important positive result of IRT:

\[
\boxed{
\text{the finite-rational obstruction is not universal;}
\quad
\text{complete realization data can recover the full meromorphic object}.
}
\]

But the data volume is typically global/infinite and the realization class
carries strong rigidity.

No theorem located in IRT-0A reconstructs the frozen RENJET exponential
functional from a *finite local* derivative-critical packet.

## 6. Quantifier test

Classical inverse spectral uniqueness is global and exact once the admissible
full spectral data are supplied.

Thus its quantifier structure is stronger than an average theorem.

However, this strength is purchased by complete/global spectral data and
self-adjoint realization assumptions. It does not by itself produce the
canonical every-dangerous-packet transfer from the limited NJDG data.

**Disposition:** GLOBAL EXACT / DATA-VOLUME MISMATCH FOR DIRECT INSERTION.

## 7. Conditioning test

The abstract uniqueness theorems do not automatically supply the projective
packet-scale conditioning required by NEXTJET.

Finite/local reconstruction can still be badly conditioned near spectral
collisions. Interlacing supplies order and separation topology but not the
specific projective lower bound required by the canonical packet.

**Disposition:** UNIQUENESS YES / REQUIRED LOCAL CONDITION NUMBER NOT YET
SUPPLIED.

## 8. False-RH compatibility test — decisive classical obstruction

The scalar Herglotz mechanism requires the realized spectral points to lie on
the real axis. Meromorphic Herglotz functions have real simple interlacing
zeros and poles under the standard scalar hypotheses.

Introduce the standard critical-line coordinate

\[
\xi(t)=\Xi\!\left(\frac12+it\right).
\]

A nontrivial zero of \(\Xi\) lies on the critical line exactly when the
corresponding \(t\)-coordinate is real.

Therefore a global classical Herglotz realization whose poles are exactly the
full \(\Xi\)-zero divisor would force the pole divisor into the real spectral
axis. In the false-RH reductio, that is not an admissible premise.

Equivalently, the positivity/self-adjointness that couples the spectra in the
foreign theory is already strong enough to prohibit the nonreal pole geometry
the negative branch is supposed to analyze.

Thus:

\[
\boxed{
\text{CLASSICAL HERGLOTZ / SELF-ADJOINT TWO-SPECTRA}
\text{ is structurally right but directly circular for the false-RH branch.}
}
\]

This does not show that every transform or generalized realization is
circular. It rules out the naive classical \(N_0\) realization with the actual
full divisor as its spectral pole set.

## 9. What IRT-0A learned

The missing ingredient can now be stated much more sharply.

NJDG did not fail because mathematics lacks ways to transfer between two
divisors. Such transfers are routine once one has realization rigidity.

The actual question is:

\[
\boxed{
\text{What weaker-than-self-adjoint rigidity can couple the two zeta divisors
without already forcing RH?}
}
\]

That points directly to generalized Nevanlinna / Pontryagin-space theory.

There the state space may have finite negative index and the function may have
generalized poles/zeros of nonpositive type, while retaining an operator
realization and substantial spectral structure.

## 10. IRT-0A matrix

| Test | Classical Weyl/Herglotz result | IRT disposition |
|---|---|---|
| common carrier | one Weyl/resolvent object | PASS in foreign theory |
| zero/pole coupling | real simple interlacing spectra | STRONG |
| full-object reconstruction | yes from suitable two-spectra/global data | STRONG |
| exact exponential functional | available after full object recovery in principle, not direct finite-packet theorem | PARTIAL |
| every-packet quantifier | global exact theorem, but not packet-local | DATA MISMATCH |
| conditioning | no canonical NEXTJET projective bound extracted | OPEN |
| false-RH compatibility | classical real-spectrum positivity excludes nonreal pole divisor | FAIL |
| direct canonical re-entry | none | NO |

## 11. Determination

IRT-0A is complete.

It identifies a mature theorem architecture formally matching the missing
mixed-divisor transfer, and identifies the exact structural resource that makes
the architecture work:

\[
\boxed{
\text{Herglotz positivity / self-adjoint realization}
+
\text{normalization}
+
\text{complete coupled spectra}.
}
\]

That resource is too strong for direct use on the negative false-RH branch.

The useful residue is therefore not another Herglotz calculation. It is the
question whether **finite-negative-index realization** retains enough of this
coupling while allowing the nonreal divisor geometry that classical
self-adjoint theory forbids.

## 12. Cursor

\[
\boxed{
\texttt{IRT-0B / GENERALIZED-NEVANLINNA-PONTRYAGIN SCREEN}
}
\]

Primary test:

> Does \(N_\kappa\) realization permit nonreal/generalized pole-zero data in a
> quantitatively finite way, and can the required \(\kappa\) be related to the
> dangerous off-critical zeta packet without assuming a global finite number of
> off-line zeros?

No canonical theorem status changes.
