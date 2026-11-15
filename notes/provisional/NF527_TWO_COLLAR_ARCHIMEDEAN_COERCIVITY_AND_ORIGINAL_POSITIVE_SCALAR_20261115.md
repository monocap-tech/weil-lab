# NF527 — Complete archimedean coercivity from original two-collar support

**2026-11-15 PT. NEW ANALYTIC THEOREM; exact Fraction rational gates LOCAL PASS.** The original NF494 400-source is unchanged (SHA256 \`39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181\`). The full original NF523/NF524 source certification and exact-242-moment two-source graph Cauchy approximation are RETAINED premises, not replayed. NF526 generic smooth explicit-formula native-form bridge is analytic, NOT newly Lean compiled. No CI, main merge, RH or W_ODD_NEG claim.

## Strong support-only signed-form lower bound

Let B=11/10, delta=1/500, E=(-B,-B+delta) union (B-delta,B), m=|E|=2delta=1/250. For every compact smooth complex f supported in E, define the ACTUAL completed-zeta Weil diagonal Z(f) with every authentic divisor multiplicity copy, the true zero sampling and literal prime/pole/digamma terms. The imported unconditional Zeta23.WeilEF.EF_lit_zeta applied to the exact smooth autocorrelation C_ff gives
Z(f)=ARCH(f)-PRIME(f)+POLE(f).
Then **Z(f) > (1/10)*||f||_L2²**. This requires NO RH assumption and does not use any approximation to the original arithmetic source. The identical bound applies analytically to the actual original non-smooth ell_U through NF524's full two-source graph limit and NF526's generic smooth-to-native identity, both not yet Lean-compiled.

### Archimedean bound (NEW)

The actual gammaBracket is G(t)=Re digamma(1/4+i*t/2)-log(pi), already identified with compactWindowArchimedeanSymbol in ActualZetaArchimedeanCoordinates.lean. The exact special value is proved in ActualZetaNativeSymbolSign.lean:
G(0)=-C0, C0=EulerGamma+pi/2+3*log2+logpi.
Subtract the digamma partial fraction series at 1/4 and 1/4+i*t/2:
G(t)=-C0+SUM_{k>=0} [(t/2)^2 / (a_k*(a_k²+(t/2)^2))], a_k=k+1/4.
Every summand nonnegative and nondecreasing in |t|. Classical elementary bounds 0<EulerGamma<1, 3<pi<22/7, log2<7/10, logpi<6/5 prove C0<411/70<59/10. The two log upper bounds follow from four positive Taylor terms of exp(7/10)>2 and exp(6/5)>22/7. Gamma<1 follows from decreasing H_n-log n and n=2, using log2>1/2.

The **exact rational** 20-term partial sum at |t|=30 is
D20=SUM_{k=0}^{19} 15²/(a_k*(a_k²+15²)) >67/10.
The attached Fraction script establishes that inequality without floating acceptance. Hence G(t)>-59/10 for ALL t and G(t)>4/5 when |t|>=30.

Set F_f(t)=int f(x) exp(i*t*x) dx. The support m gives |F_f(t)|²<=m||f||². Plancherel gives int |F_f|² dt/(2pi)=||f||². Since pi>3, the portion with |t|<30 is at most (30*m/pi)||f||²<(1/25)||f||²; the outside portion is more than 24/25. The COMPLETE true archimedean integral, not a truncated or uncorrelated surrogate, satisfies
ARCH(f)=int G(t)|F_f(t)|² dt/(2pi) >
[(4/5)*(24/25)-(59/10)*(1/25)]||f||²
= **(133/250)||f||²**.

### Genuine prime and pole controls

NF526 exact log9 geometry proves only n=9 can enter the original E-E autocorrelation difference support. For an arbitrary complex f supported in E, |C_ff(log9)| <= ||f_positive||*||f_negative|| <= (1/2)||f||² and C_ff(-log9)=conj(C_ff(log9)). True von Mangoldt coefficient Lambda(9)/sqrt9=log3/3<2/5. The COMPLETE original prime term has |PRIME(f)|<(2/5)||f||². Do not apply n=9 pruning to finite NF523 moment-corrected smooth approximants whose support may be larger than E.

For M_pm(f)=int f(x)exp(±x/2)dx, e^((B+delta)/2)<2 is already a source-independent exact NF524 gate. Thus |M_pm(f)| <= 2sqrt(m)||f||. Both true Hermitian cross pole terms give |POLE(f)| <=8m||f||²=(4/125)||f||². For the retained real odd ell_U the exact pole sign is -2M_plus²<=0.

Combining complete original correlations:
Z(f) > [133/250 - 2/5 - 4/125]||f||²
= **(1/10)||f||²**.
This is a strictly positive support-localized form certificate, independent of source-shape details. It does not imply global positivity of arbitrary odd vectors.

### ORIGINAL source vector and explicit nonzero lower (inherited NF523 certified bounds)

ell_U(x)=sgn(x)*1_{B-delta<|x|<B}*(U(|x|)/2)*log(B/(B-|x|)).
NF523 source facts U(B)<-1e-11 and |(U(B-d)/2)'|<7e-4 imply c(d)=U(B-d)/2 < -4e-12 when 0<d<=1e-9, and log(B/d)>1 there. Therefore ||ell_U||²>2*1e-9*(4e-12)²=3.2e-32, and the *analytic, as-yet-uncompiled same-source bridge* implies
**Q_B(ell_U)>3.2e-33>0**.

This **rules out this specific original endpoint-log carrier as a negative Weil witness, CONDITIONAL ON the retained NF524/NF526 analytic transfer obligations**. This does not settle W_ODD_NEG for other test functions, the full even/odd sector, or RH.

## Formalization and no-transfer gates

1. Lean: generic smooth correlation/direct EF/native prime-gamma-pole source identity (NF526), retaining every actual multiplicity and exact source normalization, **OPEN**.
2. Lean: Weierstrass digamma monotonicity and exact D20 rational lower, Fourier support/low-frequency mass and two-collar coercivity, **OPEN**.
3. Lean: specialize to NF524 exact-242-moment full actual two-source graph Cauchy sequence and original U carrier, **OPEN**.
4. Original NF494 all-400 exact coefficient audit was done in NF523/NF524 and NOT replayed here. Source-independent rational script is not a certification of original-source graph analysis.
5. Green packet span membership of ell_U OPEN, and not required for this direct method. No original signed negativity, W_ODD_NEG or RH conclusion.

**NF528**: compile the genuine generic smooth explicit-formula source-to-native bridge and exact two-collar lower bound. Do not spend another iteration numerically integrating a continuous gamma term whose complete signed contribution has a rigorous analytic support-only coercivity bound.
