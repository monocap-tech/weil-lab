# RPB108 RC17 — direct native screen and exact signed pole bounds

2026-10-10. Independent route consolidation.
Parent: 42540e155a11022971fe894fa9bd0db4fa7b3a02 (RC16).
Only research/rpb108-route-consolidation is written.

## Result

At B=11/10 the actual physical native remainder satisfies

    -16 I <= R_B <= 21 I,   ||R_B|| <=21.

The bounds retain the archimedean remainder, all seven active prime powers,
and both signed pole moments. The exact pole eigenvalues improve RC15's
unsigned 4sinh(B) allowance.

For a canonical finite head with entire physical complement norm at most
delta=1/2000, the ORIGINAL canonical form has complementary floor
249999/250000 and cross-block norm squared at most 441/4000000.
If its actual canonical head floor is at least 1/4000, the Schur reserve is

    46583/333332000 >0.

This avoids phase-reference normalization and its small reference floor.
No actual head is computed or certified, and no new aperture positivity
follows from the result alone.

## Native decomposition and attachments

Use the supported logarithmic Hilbert carrier D_B, Fourier convention
exp(-2pi i xi x), and physical inclusion i:D_B -> L2(-B,B), ||i||<=1.
The original bounded canonical form operator is

    A_Q=I+i^*R_B i.

The full Q is not asserted to be a bounded physical L2 form: its unbounded
logarithmic principal part is represented by I in D_B.

The native decomposition is pinned to CC27
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, and CC37
notes/REFLECTED_PACKET_BRIDGE_108_EFFECTIVE_NATIVE_REMAINDER_CC37_20261008.md,
blob a8a4ec58ebc43745d73630b97188cac1597b15ed,
at CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.
RC15 records their attachments and the cap-specific coefficient enclosure.
The inherited archimedean physical remainder has norm <8.

Zero extension makes each physical translation S_d a contraction.
The signed prime contribution is -sum c_n(S_log(n)+S_log(n)^*), where
c_n=Lambda(n)/sqrt(n). At this cap exactly 2,3,4,5,7,8,9 are active,
since 9<exp(2B)<10. RC15's coefficient enclosure is

    sum c_n <12093/3740+11/30.

The last term is log3/3, not log9/3. In either direction the prime norm
is at most twice this sum.

## Exact pole spectrum

In physical L2 let v_+(x)=exp(x/2), v_-(x)=exp(-x/2), and
m_+(h)=integral h(x)exp(x/2)dx, m_-(h)=integral h(x)exp(-x/2)dx.
The pole form is

    conjugate(m_-)m_+ + conjugate(m_+)m_-
      =|m_even|^2-|m_odd|^2,

where m_even=(m_++m_-)/sqrt2 and m_odd=(m_+-m_-)/sqrt2.
Their representers are w_even=(v_++v_-)/sqrt2 and
w_odd=(v_+-v_-)/sqrt2. Symmetry of (-B,B) makes them orthogonal.
Their squared norms are

    ||w_even||^2=2sinh(B)+2B,
    ||w_odd||^2=2sinh(B)-2B.

Consequently the physical pole operator has nonzero eigenvalues
2sinh(B)+2B and -(2sinh(B)-2B), with zero on the remaining complement.
Its full norm is 2sinh(B)+2B; its negative norm is 2sinh(B)-2B.
This uses both moments without a moment-neutral restriction.

Fresh rational Taylor enclosures prove exp(11/10)<31/10.
Thus exp(-11/10)>10/31, giving

    2sinh(B)<861/310,
    negative pole allowance <179/310,
    full pole allowance <1543/310.

Combining these with the archimedean and prime bounds gives

    8+2(12093/3740+11/30)+179/310 <16,
    8+2(12093/3740+11/30)+1543/310 <21.

Hence the displayed signed remainder bounds. This is a global physical
remainder estimate, not an estimate on only selected packet profiles.
The positive pole eigenvalue may be dropped for the lower bound but
remains in the cross-block norm bound.

## Direct whole-complement Schur theorem

Let X:D_B -> L2(-B,B) have finite rank and ||i-X||<=delta.
Let P be the CANONICAL orthogonal projection onto range(X^*) and H=I-P.
Then XH=0, so ||iH||<=delta, while ||iP||<=1.

Define the actual head G=P A_Q P, the cross block C=H A_Q P,
and the tail D=H A_Q H, restricted to their corresponding subspaces.
Orthogonality in D_B gives H I P=0. Therefore

    D>= (1-16delta^2)I_H,
    ||C||<=21delta.

The lower tail uses the one-sided remainder bound. The cross block uses
the full remainder norm, retaining its positive as well as negative parts.
No phase metric or transformed normalized projection is involved.

If G>=m I_P and 16delta^2<1, then

    G-C^*D^(-1)C
      >= [m-441delta^2/(1-16delta^2)]I_P.

Strict positivity of this reserve proves A_Q>0 on the WHOLE carrier:
the block factorization has a positive finite Schur block and a uniformly
positive entire tail, with bounded invertible triangular factors.
This is the exact Schur argument, not an inference from blockwise
positivity. A positive head and tail can coexist with a negative coupled
direction; the validator includes such a control.

Equivalently, the sufficient tail-accuracy condition is

    delta^2 < m/(441+16m).

At m=1/4000 this threshold is 1/1764016.
The explicit conservative choice delta=1/2000 yields

    D>=249999/250000,
    ||C||^2<=441/4000000,
    Schur cost <=147/1333328,
    m-Schur cost >=46583/333332000.

These are conditional exact bounds for the defined projection. None is
a measured head eigenvalue.

## Finite-space existence and computational cost

RC16's Fourier--Taylor approximation applies directly to i, with no
reference normalization: choose T=exp(4/delta^2), and a Taylor term count
n satisfying

    n >= (264/7)BT,
    2^n >=4sqrt(BT)/delta.

Its proved complete residual bound is
1/sqrt(log(e+T))+2sqrt(BT)(2pi BT)^n/n! <=delta.
The canonical finite space is range(X^*), defined using the canonical
Riesz representatives of the coefficient functionals; it is not a
physical polynomial projection.

Here T=exp(16000000), and the construction still requires an
astronomical head dimension. The logarithmic cutoff exponent is 250000
times smaller than RC16's exp(4*10^12) choice.
This compares the two stated sufficient constructions at numerical head
floor 1/4000. Their actual heads live in different metrics and have NOT
been shown to attain the same floor. The comparison is neither a
complexity lower bound nor a practical spectral computation.

The direct route removes avoidable reference-floor losses, but the
generic inclusion approximation still cannot support a feasible head
calculation. A practical certificate needs sharper actual operator or
source-profile tail estimates and then an actual canonical head floor.
The phase-reference route remains mathematically valid; this result does
not decide which actual finite head is easier to certify.

## Validation and standing

scripts/validate_rpb108_rc17_direct_native_screen.py passes 23 exact rational
checks: exponential enclosure, signed and full pole allowances, complete
native remainder bounds, direct tail/cross budgets, Schur reserve, cutoff
comparison, pole spectral algebra, and an unsafe blockwise-positivity
control. Operator and whole-complement arguments are analytic proofs above;
finite controls do not substitute for an actual head evaluation.

No finite space is instantiated, no actual original matrix or negative
vector is evaluated, and no whole positivity at 1.10, RH/F4 theorem or
Lean closure is claimed. The existing 1.06 certificate and prior restricted
theorems remain intact. Historical notes and other branches are unchanged.
