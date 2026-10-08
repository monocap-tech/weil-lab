# RPB108 NF65: a global logarithmic tail repair with physical-mass error

2026-10-08 UTC (2026-10-07 Pacific). Recovered head: `22ced3cbb32c08167f74b4ed776c26ba552af6d6`.

NF64 proved that dropping the positive archimedean tail makes the 32-term form negative even at the genuinely ORIGINAL-positive aperture one. Here that tail is retained by a logarithmic main term and finitely many rational corrections. The repaired comparison differs from the complete original form by less than **10^-40 times physical mass**, uniformly over every frequency and every finite aperture. It is positive on the WHOLE canonical domain at the already certified anchor. No new original aperture sign, arithmetic relative-loss principle, or global source-gain bound is claimed.

Definitions are in [the tail-repair registry](../docs/TERMINOLOGY_RPB108_ARCHIMEDEAN_TAIL_REPAIR.md). This is an analytic theorem with exact rational coefficient checks, not a Lean certificate or a numerical whole-space eigensolver.

## 1. Original tail and a nonnegative Laplace representation

Keep NF63's original Fourier convention, original complete prime operator, and exact two-slot pole. Write z=pi^2 xi^2, q=N+1/4, and

    f_z(u)=z/[u(u^2+z)]=1/u-u/(u^2+z),
    R_N(z)=sum_{j>=0} f_z(q+j).

Thus m_original=m_N+R_N. For u>0 and z>=0,

    f_z(u)=integral_0^infinity exp(-ut)[1-cos(sqrt(z)t)] dt,
    R_N(z)=integral_0^infinity
           exp(-qt)[1-cos(sqrt(z)t)]/[1-exp(-t)] dt.

Tonelli applies because the weight is nonnegative. The integral main term is

    I(q,z)=integral_q^infinity f_z(u) du
          =(1/2)log(1+z/q^2).

In particular this term preserves the logarithmic high-frequency growth which the bare finite cutoff lost. No regularity assumption on h is used in the multiplier estimate.

## 2. A finite remainder valid for ALL positive t

The checked primary identity is NIST DLMF 4.36.3, https://dlmf.nist.gov/4.36.E3. Substituting t/2 in the coth partial fraction gives

    1/[1-exp(-t)] = 1/t+1/2
                    +2t sum_{n>=1} 1/[t^2+(2pi n)^2],  t>0.

For beta>0 and any integer m>=0 the exact FINITE identity is

    1/(beta+t^2)
      =sum_{r=0}^{m-1} (-1)^r t^(2r)/beta^(r+1)
        +(-1)^m t^(2m)/[beta^m(beta+t^2)].

It has no condition t<sqrt(beta). Its signed remainder is nonnegative after multiplication by (-1)^m and is bounded by t^(2m)/beta^(m+1). Summing the positive denominator bounds is legitimate for every fixed t; each coefficient series converges. The resulting polynomial kernel is

    A_m(t)=1/t+1/2+sum_{k=1}^m B_(2k)t^(2k-1)/(2k)!,

with Bernoulli convention B_1=-1/2. Identification of these finitely many coefficients can use the generating function in a neighborhood of zero. Global validity comes from the finite rational remainder, NOT from convergence of an infinite Bernoulli Taylor series. Consequently

    0 <= (-1)^m {1/[1-exp(-t)]-A_m(t)}
      <= |B_(2m+2)| t^(2m+1)/(2m+2)!,  for ALL t>0.

This does not repair or reuse the invalid all-distance origin-series extrapolation diagnosed by the aperture-scalability audit. In particular no bound on 4a or a<pi/2 enters this theorem.

## 3. Explicit rational corrections and the global sandwich

For r>=0 set

    d_r(q,z)=(-1)^r partial_q^r f_z(q)
      =integral_0^infinity t^r exp(-qt)[1-cos(sqrt(z)t)] dt.

Therefore 0<=d_r<=2r!/q^(r+1), uniformly in z>=0. A directly evaluable rational expression is

    d_r = r! [q^(-r-1)
          - sum_{j=0}^{floor((r+1)/2)} binom(r+1,2j)
            q^(r+1-2j)(-z)^j/(q^2+z)^(r+1)].

Define the finite tail repair

    S_m(q,z)=I(q,z)+(1/2)f_z(q)
                 +sum_{k=1}^m B_(2k)d_(2k-1)(q,z)/(2k)!.

Integrate Section 2 against the nonnegative Laplace weight. All finitely many terms are integrable, and the global remainder has an integrable majorant. For even m,

    S_m <= R_N <= S_(m+1),
    0 <= R_N-S_m <= |B_(2m+2)| d_(2m+1)/(2m+2)!
                       <= epsilon_(N,m),
    epsilon_(N,m)=|B_(2m+2)|/[(m+1)q^(2m+2)].

The first upper bound is exactly the next, odd, correction. For odd m the inequality orientation reverses. Nothing is asserted about taking m to infinity at fixed q; this construction uses a chosen finite even m.

At N=32, q=129/4, m=16, B_34=2577687858367/6. Exact rational arithmetic proves

    epsilon_(32,16)
      =22376446223625658020818298339328 /
       1726519170378188127122886560394063941690249941230343148642833916481565443
      < 10^-40.

The decimal value is approximately 1.2961e-41, only for orientation; the certificate uses the displayed fraction. There are 32 Euler head terms, the logarithmic main term, the half-endpoint term, and 16 Bernoulli corrections. The odd seventeenth correction supplies an explicit upper comparison.

## 4. Physical and canonical forms: the missing topology is supplied

Let Q_minus use the archimedean symbol m_N+S_16, and let Q_plus use m_N+S_17. Both retain the ORIGINAL complete primes and EXACT signed pole. For every h in the canonical logarithmic domain D_a,

    Q_minus(h) <= Q_original(h) <= Q_plus(h),
    0 <= Q_original(h)-Q_minus(h)
      <= Q_plus(h)-Q_minus(h)
      <= epsilon_(32,16) ||h||_2^2 < 10^-40 ||h||_2^2.

All form domains agree: their archimedean symbols differ by bounded multipliers and have the same logarithmic growth. The prime and pole terms are bounded at each fixed finite aperture. The DIFFERENCE operators are bounded in physical L2 with norm <=epsilon; the original and repaired logarithmic operators themselves remain unbounded. This is not a bare bounded cutoff or an absolute integrated-kernel error disguised as coercivity.

Since w(xi)=log(e+|xi|)>=1, the same estimate is <=epsilon E_log(h). However the stronger physical-mass statement is retained. Unlike an H0^1 tail bound it applies directly to the rational step witnesses, whose weak derivatives are not L2. Unlike fixed-N truncation error divided by w, it is uniformly small at high frequency.

Let lambda_minus, lambda_original and lambda_plus be the corresponding WHOLE physical Rayleigh infima. They are finite by the original Garding bound and satisfy

    lambda_minus <= lambda_original <= lambda_plus
                  <= lambda_minus+epsilon_(32,16).

An independent proof lambda_minus>0 would prove an original sign. No positive finite matrix restriction is promoted to such a whole-space bound.

## 5. Actual anchor control: the false negative disappears

The complete aperture-one certificate at source commit
`811b0826abf45d688d1e2da7900cda852103ddee` establishes on the whole domain

    Q_original >=4e-32 mass,    Q_original >=2e-34 E_log.

Subtract the proved uniform error, using mass<=E_log. It follows that at a=1

    Q_minus >=(4e-32-1e-40)mass >3e-32 mass,
    Q_minus >=(2e-34-1e-40)E_log >1e-34 E_log.

Thus this repaired comparison is itself whole-domain coercive at the genuine ORIGINAL-positive anchor. This transfers an existing certificate; it is not an independent new original positivity argument.

In particular NF64's exact odd step witness, mass
31999998475473/32000000000000, has positive Q_minus even though its bare Q_32 is below -49/1000 times mass. The repaired tail contributes more than
[49/1000+4e-32-1e-40] times its mass. That statement follows from the exact witness inequality and the WHOLE anchor, without a sampled Fourier quadrature. NF64's g_32>1 remains correct for its different bare cutoff. This repair is not assigned that compact gain.

At a=21/20, NF64's negative bare-cutoff witness still has no assigned original sign. The repaired sandwich tracks the unknown original energy within the proved tiny physical allowance; approximation alone does not supply the missing sign.

## 6. Continuous-kernel and eigenlevel custody

In NF61's mean-zero derivative representation let h=J_a u, M_a=J_a^*J_a, and C denote the integrated form on u. The multiplier estimate gives the genuinely relative operator inequality

    0 <= C_original-C_minus <= epsilon_(32,16) M_a.

This is the physical relative-mass topology which an absolute continuous-kernel distance lacked. It holds for every u in the derivative representation; the original form result separately covers all of D_a, including rough vectors. No lower bound proportional to the identity on the compact derivative space is asserted.

At every positive original eigenlevel mu, subtract the SAME mu||h||_2^2 from both forms. Their difference and error bound are unchanged. A positive original level smaller than epsilon can have a nonpositive lower-comparison level. Neither a lower-comparison zero nor a shifted level is original zero-level contact. The actual divisor identity remains Q_original=||P_a h||^2-||N_a h||^2; no actual-divisor dictionary is invented for Q_minus.

## 7. Validation, remaining obstacle, and handoff

The exact validator checks Bernoulli recurrence and signs, the finite rational remainder at arguments far outside the corresponding Taylor radius, rational derivative formulas, integrated coefficients, the exact <10^-40 budget, anchor conversions, and positive-level shift preservation. Its 389 finite checks support the coefficients and controls; the analytic all-frequency theorem is the Laplace/partial-fraction proof above, not a generalization from samples.

The tail-loss obstruction of the bare 32-term model is repaired, with a uniform physical-mass allowance and a genuine whole-domain anchor control. The remaining global obstacle is an ORIGINAL arithmetic/source inequality that determines sign across unbounded apertures. This result approximates the difficult original sign to a tiny known budget; it does not determine that sign. No new prime estimate, coupled-continuation relative-loss principle, global gain below one, or RH proof is claimed. The other thread's continuation priority and paused Aperture/Precontact work remain untouched.

A future original sign calculation may use the repaired lower/upper forms, but must independently control the whole logarithmic domain, its exact prime/pole coupling, and approximation arithmetic. Numerical cancellation in high-order rational corrections would require outward enclosures; the current theorem is exact symbolic arithmetic and does not certify a floating implementation.
