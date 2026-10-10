# RPB108 RC23 — Riesz error transport and an executable canonical matrix gate

2026-10-10. Independent route consolidation.
Parent: 9fc3f9a89659f0d207ea0392407a18d7f4c7cc1f (RC22).
Only research/rpb108-route-consolidation is written.

## Result and evidence boundary

A whole-space weak-residual certificate for approximate canonical Riesz
vectors now yields explicit errors for the feature, head and source Gram
matrices. An exact rational verifier checks a robust finite acceptance
gate, using a trial-source residual Gram rather than an unchecked inverse
subtraction.

The verifier passes 22 exact synthetic controls, including rejection of
unsafe source leakage, insufficient head floors, singular metrics,
understated coefficient norms, inadequate error margins and float inputs.

No actual RC22 Riesz vectors, weak residuals or matrices are computed.
The verifier validates finite inequalities CONDITIONAL on the supplied
matrix error bounds and native attachment. It cannot authenticate those
hypotheses from a JSON file, and its output explicitly marks them unverified.
No new original positivity or aperture extension is claimed.

## Standing and definitions

RC22 specifies an 8600-feature canonical Chebyshev moment head at B=11/10.
Its entire original-form complement has floor d=247/2500.
Its sufficient actual head/source conditions are m=1/4000 and beta=1/300,
giving Schur reserve 1223/8892000.

Use the supported logarithmic Hilbert carrier D_B with inclusion i,
||i||<=1. The original bounded canonical operator is
A_Q=I+i^*R_B i. RC21 gives ||R_B||<18, hence ||A_Q||<=19.
These represent the full native form, including all prime and pole
contributions; the unbounded physical logarithmic principal part is
represented by the canonical identity.

The exact moment representatives r_j are those of
ell_j(h)=integral T_j(x/B)(i h)(x)dx.
Let R a=sum a_j r_j be the exact feature map.
Its exact matrices, as in RC22, are

    M=R^*R, A=R^*A_Q R,
    sigma_j=i^*R_B i r_j,
    V=R^*sigma=A-M=V^*, U=sigma^*sigma.

M is positive definite for these independent moment functionals.
All adjoints and norms here use the canonical metric unless physical
L2 is stated explicitly.

## Weak Riesz residuals give whole canonical errors

Suppose trial vectors v_j in D_B satisfy certified D_B-dual residual bounds

    ||ell_j-<v_j,.>_D||_(D*)<=epsilon_j.

The canonical Riesz isometry gives exactly

    ||r_j-v_j||_D<=epsilon_j.

This uses the complete dual norm; checking the residual only on finite
test vectors is insufficient.

For each v_j, the approximate-source functional is
h -><R_B i v_j,i h>_2. Suppose trial source vectors w_j in D_B have
certified dual residuals bounded by zeta_j for that functional.
Since ||i^*R_B i||<=18,

    ||sigma_j-w_j||_D<=18epsilon_j+zeta_j.

Thus for the approximate feature/source maps Rhat and Shat,

    ||R-Rhat||<=e,
    ||sigma-Shat||<=d_s,

whenever nonnegative rational e,d_s satisfy

    e^2>=sum epsilon_j^2,
    d_s^2>=sum (18epsilon_j+zeta_j)^2.

These are whole-space bounds, with a conservative column
Hilbert--Schmidt sum. Correlated source error estimates may be sharper.

A physical L2 representation of a weak residual may bound its D_B-dual
norm because ||i||<=1, but that representation and its physical norm must
be proved. Mere form-domain membership does not supply a physical L2
logarithmic source. No such membership-to-source shortcut is used here.

## Explicit Gram error transport

Assume certified approximate-map norm bounds
||Rhat||<=v and ||Shat||<=s.
Define approximate matrices

    Mhat=Rhat^*Rhat,
    Ahat=Rhat^*A_Q Rhat,
    Uhat=Shat^*Shat,
    Vhat=HermitianPart(Rhat^*Shat).

The exact V is Hermitian. Taking the Hermitian part does not enlarge
the operator-norm error relative to it.
Expansion and the triangle inequality give

    ||M-Mhat||<=eM=2v e+e^2,
    ||A-Ahat||<=eA=19(2v e+e^2),
    ||U-Uhat||<=eU=2s d_s+d_s^2,
    ||V-Vhat||<=eV=v d_s+s e+e d_s.                 (1)

Quadrature or other entrywise construction errors must additionally be
converted to matrix operator-norm errors and added to these budgets.
No approximate inner product is silently treated as exact.
The script's gram_errors function implements (1).

The input norm bounds v,s and dual residuals still require certification.
Equations (1) do not provide their actual numerical values.

## A trial-source certificate without inverse subtraction

For any EXACT finite coefficient matrix C, approximate the exact source
map sigma by R C. Its complete residual Gram is

    E_C=(sigma-R C)^*(sigma-R C)
       =U-V^*C-C^*V+C^*M C.                        (2)

The exact orthogonal source residual Gram is
Gamma=sigma^*H sigma, H the complement of range(R).
Since orthogonal projection minimizes the error,

    Gamma<=E_C.

Thus E_C<=beta^2 M suffices for ||H A_Q P||<=beta.
If C=M^(-1)V, equality holds and this reduces to RC22's exact interface.
A rational trial C can instead come from approximate solves; no true
inverse needs to be subtracted without a validated error bound.

For an exact rational norm bound c>=||C||, form

    Ehat_C=Uhat-Vhat^*C-C^*Vhat+C^*Mhat C.

Using (1),

    ||E_C-Ehat_C||<=eU+2c eV+c^2 eM.

Therefore the robust finite acceptance conditions are

    Mhat-eM I >0,                                  (3)
    Ahat-m Mhat-(eA+m eM)I >=0,                     (4)
    beta^2 Mhat-Ehat_C
       -[eU+2c eV+(c^2+beta^2)eM]I >=0.            (5)

They imply positive actual canonical M, actual head floor >=m and actual
whole source leakage <=beta.
Together with RC22's entire tail floor, they would certify original
whole positivity for the specified actual head.

The coefficient norm itself is checked exactly: for c>=0, the block

    [[c I, C], [C^*, c I]]

is positive semidefinite iff ||C||<=c. This follows by completing the
square for c>0, with the c=0 case forcing C=0.
The source gate (5) is a residual-Gram inequality; it is not a positive
block test with the wrong sign for the paid projection term.

## Executable finite interface

scripts/validate_rpb108_rc23_canonical_matrix_gate.py uses exact Python
fractions and symmetric Schur elimination to test (3)--(5) and the
coefficient norm block. A zero diagonal pivot is permitted for a PSD
matrix only when its remaining row vanishes; strict metric positivity
rejects every zero pivot. This handles singular PSD controls correctly.

The present implementation accepts REAL symmetric Gram matrices.
The exact native operator and Chebyshev features preserve real vectors,
so a real canonical certificate extends to complex vectors by writing
h=u+i v and using the real symmetric form. A genuinely complex input
requires a Hermitian extension of the verifier and is not accepted here.

Run without arguments for the synthetic controls. With a JSON path, input:

- M, A, U, V: approximate real symmetric square matrices;
- C: the exact rational trial coefficient matrix;
- cNorm: its proposed nonnegative rational norm bound;
- eM, eA, eU, eV: nonnegative rational whole operator error bounds.

Entries are rational strings or integers. Floats and asymmetric Gram
matrices are rejected. The supplied approximate matrices need not obey
Ahat=Mhat+Vhat exactly; their errors must attach them to the SAME exact
native feature and source matrices.

The generic routine can assess smaller synthetic matrices, but flags
whether the dimension matches RC22's 8600-feature head.
A conditional pass at another dimension is not the RC22 certificate.
Even at dimension 8600, identity, weak residual, error and native source
attachments are external mathematical obligations.

The script never reports an aperture extension from user-supplied input.
Its output records that the supplied error bounds and native attachment
have not been independently verified. The current default run is solely
a validator test, not actual zeta evidence.

## Computational and research boundary

The implementation is a reference exact verifier, not a scalable
8600-dimensional production solver: dense rational Schur elimination
can incur substantial time and coefficient growth.
No practical preconditioner, Riesz solve, quadrature enclosure or actual
matrix file is created in this step.

This result makes the missing canonical-data requirements explicit:
whole weak residuals and map norms yield matrix error budgets, and a
trial-source Gram test pays source leakage without fragile inverse
subtraction. It does not establish that the actual head or leakage
meets the required floors.

## Validation and standing

22 exact controls pass. They include valid exact and small-error gates,
excess source leakage despite a positive head, excessive uncertainty,
negative head, singular metric, underreported coefficient norm,
nonorthonormal/error transport algebra, malformed numeric types,
singular PSD handling and the retained conditional Schur reserve.

All matrix controls are synthetic. The Riesz and whole operator proofs
above are analytic deductions. No actual original matrix, source
residual or negative vector is evaluated; no new whole aperture
positivity, RH/F4 theorem or Lean closure is claimed.
Existing 1.06 positivity and prior restricted results remain intact.
Other branches and historical files are unchanged.
