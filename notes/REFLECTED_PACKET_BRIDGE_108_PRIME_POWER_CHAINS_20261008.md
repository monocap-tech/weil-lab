# RPB108 NF62: exact prime-power chains, original relative bound, and failed gain test

Date: 2026-10-08 UTC (2026-10-07 Pacific). Recovered head 60c50736eeff742784dae81ecd29cb25d4b317a9.

This step proves an all-vector bound for the ORIGINAL arithmetic, without smearing. It is a stronger standalone Garding budget than the old absolute sum and crude absolute pole charge. The test at a=21/20 rejects it as a replacement for the already proved joint prime bound: separating different primes loses too much. No source-gain or aperture certificate is promoted.

Definitions are recorded in [the chain dictionary](../docs/TERMINOLOGY_RPB108_PRIME_POWER_CHAINS.md). The exact derivative-kernel and primitive mass conventions are those of [NF61](REFLECTED_PACKET_BRIDGE_108_CONTINUOUS_KERNEL_20261008.md).

## 1. Group powers of each prime exactly

Use physical zero extension on [-a,a], L=2a. Let T_s h(x)=h(x+s) wherever x and x+s are supported, and zero otherwise. The positive arithmetic loss operator is

    A_prime=sum_{log(n)<=L} Lambda(n)/sqrt(n) (T_(log n)+T_(log n)*).

Thus the original form is Q=E0-<A_prime h,h>+<P_pole h,h>. These are the original orientations and Mangoldt weights, including Lambda(p^r)=log(p). The endpoint equality term is zero as a physical L2 operator.

Fix a prime p, s=log(p), q=p^-1/2. In translated coordinates [0,L], disintegrate x=r+js, 0<=r<s. For almost every r the chain is finite. Its number of points is at most

    m_p=ceil(L/s),

and chains with this maximum have positive base measure. If L/s is an integer m, almost every chain has m points, not m+1; the extra endpoint has measure zero. If s>=L then m_p=1 and the arithmetic operator is zero.

On a chain with k points, ALL powers of p act as the symmetric matrix

    B_(p,k)[i,j] = log(p) q^|i-j| for i!=j, and 0 for i=j.

This is a direct-integral identity: each shift by r s links coordinates r places apart, with amplitude log(p) q^r. No power is assigned weight r log(p). Shorter-chain matrices are principal submatrices of the longest one. The matrices have nonnegative entries. For any complex vector z,

    |z* B z| <= |z|^T B |z| <= rho(B)||z||^2,

where rho is the largest eigenvalue of B; in particular every negative eigenvalue has magnitude at most rho. The longest matrix therefore gives the exact norm of the single-prime physical block. Equality can be realized by putting its nonnegative top eigenvector on each longest chain over a base subinterval. Choosing a smooth base bump away from chain endpoints produces supported smooth functions, so this sharpness is also available on the canonical carrier. The p-block may be zero, in which case sharpness means norm zero.

Define the **chain prime budget**

    B_chain(a)=sum_{p<exp(L)} rho(B_(p,m_p)).

The triangle inequality between different primes now gives the genuine whole-domain bound

    |<A_prime h,h>| <= B_chain(a)||h||_2^2.           (1)

It holds for every physical L2 vector and hence for every canonical vector. The p-block bounds are sharp individually. The sum across different primes is not claimed sharp: their chain eigenvectors generally cannot be synchronized on the same physical h.

For comparison, a single shift has sharp numerical radius cos(pi/(ceil(L/s)+1)); its path matrix has eigenvalues 2cos(j pi/(m+1)). Combining powers in B_(p,m) retains their cross-chain compatibility rather than charging separate shifts independently. A basic finite row-sum bound is

    rho(B_(p,m)) <= 2 log(p)/(sqrt(p)-1).

For fixed p and growing a, the constant chain vector gives the lower quotient

    2 log(p) sum_{r=1}^{m-1} q^r(1-r/m),

which tends to the same row-sum value. Thus a bounded single-prime cost does not mean that the complete sum over active primes is bounded as a grows. No prime-number theorem or zero-free input is used.

## 2. Retain the exact signed pole

The ORIGINAL pole kernel is 2cosh((x-y)/2). With c(x)=cosh(x/2), s(x)=sinh(x/2),

    P_pole=2|c><c|-2|s><s|,
    ||c||_2^2=a+sinh(a), ||s||_2^2=sinh(a)-a.

c and s are orthogonal by parity. The two nonzero physical eigenvalues are exactly 2(a+sinh(a)) and -2(sinh(a)-a). Hence the **negative pole allowance** is

    <P_pole h,h> >= -2(sinh(a)-a)||h||_2^2.          (2)

For even h, the pole is nonnegative, so no pole loss is required. For odd h, only the negative rank-one term remains. Neither parity statement claims positivity of the rest of the original form.

Combining (1), (2) and the established |m0-w|<=C0 gives

    Q_a(h) >= E_log(h)
              -[C0+B_chain(a)+2(sinh(a)-a)]||h||_2^2. (3)

The even-vector version omits 2(sinh(a)-a). This is an unconditional original-form relative bound at every fixed finite a. It improves the standalone budget C0+S_a+4a exp(a), where S_a=2sum Lambda(n)/sqrt(n). It is not an improvement over every prior specialized complement estimate; the existing Legendre complement already annihilates polynomial approximations to the pole.

In NF61's mean-zero derivative carrier, the exact prime part is -J_a* A_prime J_a and M_a=J_a*J_a. Therefore (1) becomes

    |<C_prime u,u>|<=B_chain(a)<M_a u,u>.

The original integrated pole satisfies C_pole>=-2(sinh(a)-a)M_a. These are proved bounds RELATIVE TO MASS, unlike an absolute Hilbert–Schmidt approximation error. But (3) still subtracts a mass loss and does not prove C_a>=gamma M_a with gamma>0. The required full original sign remains.

For a positive original level mu, the lower bound on Q_a-mu mass contains the extra +mu inside the mass-loss bracket. It cannot be erased because a shifted eigenvector has zero shifted form. No L2 derivative is asserted for rough original eigenvectors.

## 3. Actual arithmetic test and rejection as the current gain route

At a=1, the chains for p=2,3,5,7 have maximum lengths 3,2,2,2; the powers are 2,3,4,5,7. At a=21/20 they have lengths 4,2,2,2; the newly active power is 8 with weight log(2)/sqrt(8). There is no prime-9 term because log(9)>21/10. Outward exact logarithm, square-root and positive-matrix weighted-row bounds prove

| Aperture | Complete chain prime budget | Negative pole allowance |
| --- | --- | --- |
| 1 | <3 | <351/1000 |
| 21/20 | <10/3 | <51/125 |

These are whole-vector arithmetic/pole loss bounds, not lower bounds on the complete original form. They substantially improve the crude absolute budgets, without source truncation or averaging.

The decisive comparison is the recovered prime-8 audit: its already certified JOINT prime norm bound is 1063939/500000=2.127878. Our constant-chain Rayleigh lower bounds prove that B_chain(21/20) exceeds that value. Thus even EXACT single-prime spectral evaluation cannot make this separated-prime budget beat the existing joint bound. Increasing the precision of these matrices cannot fix that structural loss.

The failed 112-vector certificate at 21/20 requires a complement constant above about 0.708374555; the published one is 0.699. That failure is already documented in [the prime-8 decision](REFLECTED_PACKET_BRIDGE_108_PRIME8_105_DECISION_20261008.md). This NF does not replace its joint prime constant, insert a new c into old Grams, alter its exact witness, restart the paused aperture experiment, or claim an original negative vector. The 113-vector complement-only probe is also left unchanged.

## 4. Research decision

Keep (1)–(3) as reusable elementary original-arithmetic bounds, especially when no joint prime computation is available. Stop this separated-prime estimate as an active candidate for repairing the current scalar certificate or proving strict global source gain. A useful arithmetic advance must exploit interactions BETWEEN primes and the original archimedean/pole terms, or prove the full relative margin by another mechanism. A sharper bound for one isolated prime cannot supply that interaction.

The existing all-aperture complement-recovery theorem remains valid and stronger in scope than a single new complement calculation. It does not settle the complete corrected Schur sign. This step supplies no new independent positive margin, aperture extension, contact exclusion, RH, F4, full transport or Lean result. It narrows this particular candidate without shortening the global proof graph.

The validator proves 57 exact finite arithmetic, weighted-row, endpoint, pole-series and positive-level controls. The infinite direct-integral decomposition, sharpness and analytic inequalities are separately proved above; the finite sample is not their proof. Source pins and the validation report are stored in the accompanying custody manifest. Concurrent coupled and aperture work is preserved additively.
