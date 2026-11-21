# Weil-Lab — IV017
## Actual signed two-pole/Gamma coercivity for the new narrow physical Schwartz direction

**Independent canonical Phase IV:** IV017, stacked on IV016 PR #784, IV015 #783, IV014 #781, IV013 #779, IV012 #778, IV011 #774, IV010 #773, IV009 #771, IV008 #769, IV007 #767, IV006 #766. NOT the independent Phase III NF### numerical source/payment certification.

**Kernel custody boundary:** Seventeen new ORIGINAL signed zeta/Schwartz Lean theorem **CANDIDATES** in two modules; eight real upstream source axiom anchors; direct pinned Lean builds and strict standard-only axiom receipts are PENDING. The exact rational constants checked by the separate Python auditor are an arithmetic preflight, NOT proof. No IV017 19/20 bound is represented as accepted until the actual build and all theorem axiom receipts PASS.

### 1. Mathematical pivot: use SIGNED Gamma spectral mass rather than a giant absolute envelope

IV012's general mixed zeta EF absolute Gamma envelope was incapable of revealing the sign of the true new diagonal. IV016 produced an exact original nonzero bump test concentrated near x=1/5 with physical support inside

    I_new = [199/1000, 201/1000],

and its source candidate proved the original von Mangoldt diagonal contribution vanishes by translated nonoverlap: `P_original(t,t)=0`. Thus for this actual original physical test, the remaining diagonal is

    D = Re W_original(t,t)
      = Re pole_original(t,t) + Re arch_original(t,t).

The original Gamma/digamma term is NOT arbitrary: NF599 already certified true two-regime lower estimates on the actual symbol

    gammaBracket(r) > -28/5                 (all real r),
    gammaBracket(r) >  11/10               (|r|>=30).

NF600 already proved that outside Fourier frequencies ξ∈(-5,5), `|-2*pi*ξ| >=30`, directly from the rigorous bound pi≥3. The true original diagonal arch term is the SIGNED integral

    Arch(t) =
      ∫_ℝ gammaBracket(-2*pi*ξ) |Fourier(t)(ξ)|² dξ.

This is a signed spectral quadratic form, NOT the absolute Gamma Fourier integral in IV012's triangle estimate.

### 2. A narrower physical window yields a stronger *uniform* Fourier uncertainty bound

The new physical support width is EXACTLY

    |I_new| = 201/1000 - 199/1000 = 1/500.

For any (possibly nonreal) complex Schwartz input t supported inside I_new, the true real Lebesgue measure, Cauchy–Schwarz and exact Plancherel give

    ‖t‖_(L¹)² <= (1/500) ‖t‖_(L²)².

Mathlib's actual Fourier pointwise estimate supplies

    |Fourier(t)(ξ)|² <= ‖t‖_(L¹)².

Integrating over the existing NF600 low band (-5,5) of width10 gives the exact inequality

    LowMass(t) :=
      ∫_{-5}^{5} |Fourier(t)(ξ)|² dξ
      <= (10/500) ‖t‖_(L²)²
      = (1/50) ‖t‖_(L²)².

This improves the accepted NF600 original double-collar Fourier low-mass fraction from 1/25 to 1/50 for the new physical single interval, **without illegally asserting that the new test itself is supported in the old original two collars**.

### 3. Exact SIGNED Gamma coercivity

Split the full original Gamma integral into the low band and its complement. The actual NF599 symbol bounds yield, for EVERY complex Schwartz t,

    Arch(t) >=
      (-28/5)*LowMass(t)
      + (11/10)*(Mass(t) - LowMass(t)).

Equivalently,

    Arch(t) >= (11/10)*Mass(t)
                 - (67/10)*LowMass(t).

For I_new-supported t with `LowMass<=Mass/50`:

    Arch(t) >= [11/10 - (67/10)/50] Mass(t)
            = (483/500) Mass(t).

**This is a signed lower bound, not an absolute-value majorant.**

Nine first-module Lean proof candidates attach this to the physical narrow L¹ estimate and actual gammaBracket. Four upstream axiom anchors audit the original symbol bounds, Plancherel mass identity and original Schwartz integrability.

### 4. The retained TWO original poles cost at most 2/125 of the diagonal mass

The original physical pole source is

    pole_original(t,t)
      = conj(M_-(t))*M_+(t)
          + conj(M_+(t))*M_-(t),

with M_± the TRUE original `sourceWindowMoment` at the two original imaginary frequencies ±1/2. Both residues are preserved; no surrogate square is substituted.

The original window b=11/10 and rigorous `exp(11/20)<2` imply

    |M_±(t)| <= 2 ‖t‖_(L¹)

for any complex Schwartz t fitting into the original physical window. Thus

    |pole_original(t,t)|
        <= 8 ‖t‖_(L¹)²
        <= (8/500) Mass(t)
        = (2/125) Mass(t).

In particular,

    Re pole_original(t,t) >= -(2/125) Mass(t).

Seven original second-module source candidates derive actual physical moment norm estimates, preserve BOTH polar terms and generalize NF600's spectral Fourier attachment from OLD-COLLAR-only sources to any genuine test supported in the SAME coarse original physical window. This is essential to avoid invoking NF600's old-support source theorem on the new bump.

### 5. Candidate NEW original diagonal quantitative coercivity: 19/20

Combining the actual original prime-free narrow self-interaction from IV016, signed Gamma and two authentic pole estimates:

    D = Re W_original(t,t)
      = Re pole_original(t,t) + Arch(t)
      >= -(2/125) Mass(t) + (483/500) Mass(t)
      = (19/20) Mass(t).

Therefore the principal IV017 Lean theorem TARGET is

    neutralIV017NarrowOriginalDiagonal_coercive:
      for every complex Schwartz t with support(t) ⊆ I_new,
      (19/20)‖t‖_(L²)² ≤ Re W_original(t,t).

This is a CONCRETE quantification of the new diagonal, not merely its source decomposition. If and only if the direct source Lean proof succeeds, IV017 will close **the new-direction D>=0 obligation for this narrow subclass**. It does not prove global support positivity.

The next proof candidate uses Mathlib's genuinely nonzero complex Schwartz bump around c=1/5 to construct a new physical test that is OUTSIDE the original two strict NF543 collars, equals one at its center, and has `Re W_original(t,t)>=0` from the genuine source inequality. Its positivity remains an unverified Lean candidate as of this stage.

### 6. The old and NEW signs no longer need to be hypotheses in the one-site Schur gate

The old NF600/NF738 original two-collar source supplies, for any finite physical complex old combination S,

    A = Re W_original(S,S)
      >= (2/5) ‖S‖_(L²)² >=0.

The new IV017 estimate would supply

    D >= (19/20) ‖t‖_(L²)² >=0.

The proposed genuine original one-new-test positivity theorem

    neutralIV017OneNewSource_nonnegative_of_singleResidualBound

therefore eliminates BOTH earlier independent sign hypotheses.

What remains is the *actual original mixed pole/Gamma Schur estimate*

    |W_original(S,t)|²
      = |pole_original(S,t) + arch_original(S,t)|²
      <= A * (19/20) ‖t‖_(L²)².

This is a sufficient stronger numerical bound than the sharp `|W(S,t)|²≤AD`, because D≥(19/20)‖t‖². Unlike the two sign hypotheses, **this mixed cross estimate is NOT proved** by IV017 and appears explicitly in the theorem statement.

The quantitative support-extension problem thus narrows from "old sign + new sign + cross determinant" to **a single original mixed residual inequality** for the chosen support class, if IV017's genuine Lean kernel proofs pass.

### 7. Source and strict audit ledger

First source module:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowSignedGamma.lean`.

Nine new theorem candidates:

1. `neutralIV017NarrowPhysicalInterval_volume`
2. `neutralIV017Narrow_support_from_bump`
3. `neutralIV017NarrowL1_bound`
4. `neutralIV017NarrowL1_sq_le`
5. `neutralIV017Density_le_L1_sq`
6. `neutralIV017LowMass_le_tenL1_sq`
7. `neutralIV017NarrowLowMass_le`
8. `neutralIV017SignedGamma_lower`
9. `neutralIV017NarrowGamma_coercive`

Second source module:
`WeilDefect/Arithmetic/ActualZetaPhaseIVOriginalNarrowDiagonalCoercivity.lean`.

Eight new theorem candidates:

1. `neutralIV017OriginalWindowMoment_bound`
2. `neutralIV017OriginalPole_norm_le_eightL1_sq`
3. `neutralIV017NarrowPole_real_lower`
4. `neutralIV017OriginalWindowCorrelation_spectral`
5. `neutralIV017OriginalWindowArch_real_eq_spectral`
6. `neutralIV017NarrowOriginalDiagonal_coercive`
7. `neutralIV017ExistsNonzeroNewSource_diagonalNonnegative`
8. `neutralIV017OneNewSource_nonnegative_of_singleResidualBound`

Four upstream source strict-axiom anchors per module audit the real original symbol, original transformed correlator and actual prior source proofs. Only standard `propext`, `Classical.choice`, `Quot.sound` allowed, with no `sorryAx` and no artificial `axiom`.

Independent auditor:
`scripts/iv017_original_narrow_diagonal_coercivity_audit.py`.
It verifies exact Fraction identities

    width=1/500;
    LowMass coefficient=1/50;
    gamma loss=(11/10)-(-28/5)=67/10;
    Gamma lower=483/500;
    two-pole loss=2/125;
    diagonal lower=19/20.

The actual audit requires TWO genuine Lean compiled `.olean` objects, all 17 new plus eight real original anchor strict `#print axioms` receipts, no compiler errors, SHA-256-binding to original dependency sources, original exact toolchain/manifest and actual compiled objects. Python alone cannot certify the theorem.

Dedicated workflow:
`.github/workflows/iv017-original-narrow-diagonal-coercivity.yml`.

### 8. Known compiler/status boundary

As checked on the IV017 creation date, IV006–IV008 source and axiom audits had already PASSED. IV009 was still **in progress**, while the IV013–IV016 long source dependency chain had not yet published terminal real compiler/strict axiom results. IV017 itself is therefore a **candidate**, and downstream successful source preflight is not acceptance.

Do not mark the proposed 19/20 diagonal constant, source existence proof or one-site conditional support transfer as LEAN PASS until the direct workflow is completed successfully, including every upstream source compilation and all strict anchors.

### 9. Next — IV018

The pending analytically meaningful obstruction is the genuine original **MIXED** signed pole/Gamma bound for an arbitrary old finite complex TWO-COLLAR source S and the narrow nonzero test t, not the new diagonal anymore (if IV017 passes).

Important questions:
- Can the mixed pole moments be bounded by the old 2/5 coercive mass and the narrow new 19/20 coercive mass?
- Is the unchanged real-frequency Gamma mixed cross term small enough, using actual physical support orthogonality or the positive/negative symbol decomposition?
- Can a strict smallness inequality be established uniformly for every old coefficient vector u, rather than for a single selected old vector or a source-independent abstract matrix?
- Does the signed high-frequency Gamma cross term have cancellations that the IV012 absolute envelope discarded?

Any genuine IV018 bound must use the true original signed zeta EF and retain finite family/source custody. Global Weil positivity and RH remain OPEN. Phase III NF### numerical ledger remains separate.
