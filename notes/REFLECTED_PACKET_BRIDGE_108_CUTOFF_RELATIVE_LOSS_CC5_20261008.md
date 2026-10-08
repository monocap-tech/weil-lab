# RPB108 CC5: an actual lower-cutoff obstruction, not another conditional sign criterion

2026-10-08 UTC / 2026-10-07 Pacific. Definitions: [CC5 registry](../docs/TERMINOLOGY_RPB108_CUTOFF_RELATIVE_LOSS.md).
Recovered Coupled head `bbf36526c693fddbb0931e6706493566c3262b9e`; NF63 `76a2ef43f9495d2a076fd1e0e472c7645e681f49` was already reconciled in CC4. Publication recheck found shared NF64 `22ced3cbb32c08167f74b4ed776c26ba552af6d6`; its complete new artifacts and additive main-document entry are preserved in this merge.
Aperture and Shadow stay paused. This tests NF63's proposed bounded-background/compact-gain route against the EXISTING target witness; it does not resume a full source/Gram construction.

## Outcome

At a=21/20 the original saved witness has positive native Rayleigh value below 1.874e-32. Its N=32 archimedean lower comparison has Rayleigh value below -3.63e-5. NF63's positive background is valid, but its ACTUAL compact gain satisfies

    g_32 > 1+10^(-6).

The same unchanged vector makes Q_N negative for EVERY integer

    0<=N<=1,400,000,000,000,000.

This is a certified obstruction to those lower comparisons, conditional on the imported native interval certificate and proved archimedean identity. It is not an original negative Weil vector and does not refute NF63's monotone convergence theorem. It quantifies the cost hidden by that theorem: a finite cutoff can be theoretically available yet astronomically large near the actual tiny gap.

## 1. A universal omitted-energy lower bound

NF63's exact Euler identity, with q_j=j+1/4, gives on the original canonical domain

    T_N(h)=Q_original(h)-Q_N(h)
      =integral sum_(j>=N) pi^2 xi^2/[q_j(q_j^2+pi^2 xi^2)]
                            |hhat(xi)|^2 dxi.        (1)

All summands are nonnegative; Tonelli is lawful. The original active primes, orientations, Mangoldt weights and signed pole are identical in the two forms and cancel in this DIFFERENCE. No altered actual divisor is assigned to Q_N.

For any h supported in [-a,a], physical Cauchy--Schwarz gives

    |hhat(xi)|^2<=2a||h||_2^2,
    integral_(|xi|<=R)|hhat(xi)|^2<=4aR||h||_2^2.

Take R=1/(6a). At least one third of the physical Fourier mass lies outside this band. This bound uses L2 support only; no H1 membership, endpoint trace or differentiated source is asserted.

Put u=9R^2=1/(4a^2). Since pi>3, each omitted multiplier on that exterior band is at least

    u/[q_j(q_j^2+u)]
      >=[u q_N^2/(q_N^2+u)] q_j^(-3).

The decreasing-series comparison gives

    sum_(j>=N)q_j^(-3)>=integral_N^infinity (x+1/4)^(-3)dx
                       =1/(2q_N^2).

Combining these facts proves the whole-vector bound

    T_N(h)>=c_N(a)||h||_2^2,
    c_N(a)=1/[24 a^2(N+1/4)^2+6]>0.                 (2)

This is a LOWER bound on the omitted positive tail. It cannot be used as an error upper budget. It explains why dropping even a small absolute positive archimedean contribution can destroy a tiny original positive margin. It is radius-free and has no Bernoulli-origin expansion or divisor-height limit.

## 2. Independent native witness replay

The canonical compact matrix gzip is decoded, and its raw SHA256 must match the saved corrected certificate's native binding. The 112 rational witness coefficients are restored exactly on their 10^-40 coefficient grid. The physical basis is orthonormal, so sum v_j^2 equals the saved mass exactly.

Every one of the 6,328 lower-triangle interval pairs is ordered and included. The two signed endpoints of v^T Q v are accumulated using exact integers on the common 10^-160 product grid. Both replayed endpoints equal the saved native witness interval EXACTLY, and its lower endpoint is positive. This replay is of the complete native matrix, not the binary source or residual-Gram archives.

Illustrative displays (all decisions use rational endpoints):

| Quantity | Value |
|---|---:|
| Physical witness mass squared | 2.873239098190553 |
| Original native Q upper | 5.381890563321915e-32 |
| Original Rayleigh upper zeta | 1.873109191195124e-32 |
| c_32(21/20) | 3.632921773249098e-5 |
| Q_32 witness upper | -1.0438252879567064e-4 |
| Q_32 Rayleigh upper | -3.632921773249098e-5 |

The comparison upper values follow from Q_N(h)<=Q_original(h)-c_N mass, not from numerical quadrature. The source and Gram transport blocker is irrelevant to this test: the exact native interval and tail identity suffice.

Since c_N decreases with N, one exact endpoint inequality proves the entire cutoff range:

    c_(1.4e15)(21/20)=approximately 1.928208925293473e-32
                     >zeta.

Thus no Q_N in the stated inclusive range is positive on the whole physical space. We do not claim that a cutoff immediately above that range succeeds, nor that the original physical lowest level equals the witness Rayleigh value. The witness provides an UPPER test for the original lowest level.

## 3. Quantitative actual compact-gain failure at N=32

Keep NF63's original definitions

    F_32=L_32 I-A_prime+2|cosh(x/2)><cosh(x/2)|,
    D_32=sum_(j<32)K_j+2|sinh(x/2)><sinh(x/2)|,
    Q_32=F_32-D_32.

The existing JOINT prime norm bound is B=1063939/500000. With the imported m0(0)>=-27/5 and an independently evaluated rational sum H_32=sum_(j<32)4/(4j+1),

    F_32>=(-27/5+H_32-B)mass>157/1000 mass.

This positive BACKGROUND is preserved; it is not asserted to be Q_32. For an upper bound use the existing |m0-w|<10 envelope at zero, giving m0(0)<11. Exact scalar checks give H_32<8, B<3, and 2(a+sinh(a))<5. The last bound includes a rational sinh-series remainder. Consequently

    F_32<27 mass.

The exact compact gain is the supremum of D_32(h)/F_32(h) over nonzero physical h. On the actual saved witness,

    g_32>=1-Q_32(h)/F_32(h)
         >=1+[c_32-zeta]/27
         >1+10^(-6).                               (3)

The conservative displayed lower bound is approximately 1.000001345526583. This is a genuine one-vector LOWER bound on the WHOLE cutoff compact gain and rejects the desired upper bound below one. It is not a finite-prefix upper certificate and does not identify the original actual divisor source gain with g_32.

The inverse Neumann/cross-prime machinery of NF63 cannot make an actually negative Q_32 positive. Improving only the precision of that gain computation is therefore not the next useful task at this cutoff.

## 4. Relative-loss and finite-contact interpretation

Let lambda(a) be the original lowest physical level and ell_N(a) the whole-space cutoff lowest level. Applying (2) to canonical unit trials gives the useful ONE-SIDED relation

    ell_N(a)<=lambda(a)-c_N(a).                     (4)

This is consistent with ell_N increasing to lambda as N tends to infinity. If ell_N>0, necessarily c_N<lambda. For a small positive level lambda<1/6 this forces

    N+1/4>sqrt[(1/lambda-6)/(24a^2)].                (5)

Since the actual witness bounds lambda(21/20) above by zeta, the explicit range exclusion follows without knowing the true gap. If that gap is even smaller, the necessary cutoff is larger. If the original form is nonpositive, eventual cutoff success is not asserted at all.

At a hypothetical ORIGINAL zero contact, a nonzero actual null vector gives

    Q_N(h)=-T_N(h)<=-c_N(a)||h||_2^2<0

for every finite N. Thus finite cutoff search necessarily fails at contact and a shrinking positive gap forces an unbounded required N. The ordered cutoff framework supplies no automatic non-stalling or finite accumulated-loss bound for CC4. This is a concrete actual arithmetic/archimedean obstruction to treating a radius-free approximation theorem as the missing relative-margin theorem.

Conversely, if a positive lowest physical level mu is merely shifted to zero, its ORIGINAL vector has Q(h)=mu mass. The shifted cutoff is

    Q_N(h)-mu mass=-T_N(h)<0,

while the original energy remains positive. The mass term is retained. This test never relabels a shifted positive-eigenmode contact as an original zero.

In complete original source coordinates, (1) reads

    Q_N(h)=||P h||^2-||N h||^2-T_N(h).

Every original divisor row and multiplicity remains present in P,N. The removed positive Euler energy is a physical archimedean comparison tail, not a deletion of selected positive or negative divisor rows. All active prime powers 2,3,4,5,7,8 at the target and both signed pole slots are unchanged. Threshold equality is zero overlap in BOTH forms; it introduces no jump into their difference and cannot repair this cutoff obstruction.

## 5. Decision and validation boundary

Stop N=32 and, more generally, the excluded finite cutoff range as candidates for an actual positive certificate at 21/20. Do not retire NF63's exact representation, convergence, or all possible accelerated/relative-tail treatments. A method retaining or bounding the missing positive energy sharply is a different calculation. No such successful replacement is supplied here.

Concurrent NF64 independently rejects N=32 using two rational step-function witnesses, including the certified-positive original aperture-one anchor. Its stronger N=32 gain lower bounds and original-positive anchor control agree with this cutoff/original distinction. CC5 supplies a different native-positive vector and the much larger excluded cutoff range. NF64's certificates are preserved, not claimed replayed by the CC5 script.

The next arithmetic task remains an ORIGINAL relative margin or complete source-gain bound, not higher precision on a comparison known negative. CC4's exact loss identity remains valid and its zeta-specific nondivergence estimate remains open. CC3's restored one-direction exact-Schur lower bound is unchanged; this cutoff test is on the saved ORIGINAL polynomial vector and does not undo that trial result.

The script audits 6,328 native intervals and the exact 112-coordinate witness, plus 1,935 finite rational support-budget, tail-floor, monotonicity and positive-shift controls. The support uncertainty and infinite-series proof are analytic; no Lean proof is claimed. The complete native interval certificate, joint prime norm and symbol envelope are imported certified hypotheses; their original constructors are not all replayed here. No source/Gram archive replay, original negative Weil vector, new positive aperture, actual contact, RH, F4 or full transport is claimed. Paused refs stay untouched and historical wording is preserved additively.
