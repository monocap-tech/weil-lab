# RPB108 CC6: retain the logarithmic tail, truncate only its bounded correction

2026-10-08 UTC / 2026-10-07 Pacific. Recovered Coupled `5871503fcab6c2a05876c2aec4b8e8251ea61afe`; shared NF64 `22ced3cbb32c08167f74b4ed776c26ba552af6d6` is already preserved. Definitions: [CC6 registry](../docs/TERMINOLOGY_RPB108_LOG_TAIL_RETENTION.md). Aperture and Pre-Contact Shadow remain paused.

## Outcome

The cutoff obstruction has a concrete mathematical repair: retain an explicit UNBOUNDED logarithmic tail and truncate only its bounded Euler--Maclaurin correction. At N=K=32 the resulting whole-real-frequency symbol error is at most

    epsilon=8*63!/[6*(129/4)]^64 <8e-59.

The lower comparison differs from the ORIGINAL form by a positive physical-mass-bounded defect of at most 2epsilon. It retains certified positivity at the existing aperture-one anchor and remains positive on CC5's actual saved native-positive vector at 21/20. This is an actual reversal of the finite-cutoff failure on that vector, not a new whole-domain positivity claim at 21/20.

The original exact Schur block and the lower comparison's exact Schur block admit a graph-sensitive error bound. Thus the archimedean approximation can be made much smaller than a known tiny margin with modest representation size, without summing 10^15 Euler terms. This removes the specific discarded-tail obstruction. It does NOT establish the missing original arithmetic relative-loss nondivergence theorem or compute the whole target Schur block.

## 1. Exact omitted tail and a uniform real-frequency remainder

From the pinned original Euler identity, put q=N+1/4, x=pi|xi| and

    f_x(t)=1/t-Re(1/(t+ix))=x^2/[t(t^2+x^2)],
    T_N(x)=sum_(j>=0) f_x(q+j).

For each fixed REAL x, f is smooth on t>=q, all derivatives vanish at infinity, f is integrable, and every derivative of positive order is absolutely integrable. There are no real-frequency poles. Euler--Maclaurin with K endpoint corrections gives

    T_N(x)=M_(N,K)(x)+R_(N,K)(x),
    M=1/2 log(1+x^2/q^2)+f_x(q)/2
      +sum_(k=1)^K B_(2k)/(2k)
              [q^(-2k)-Re(q+ix)^(-2k)].            (1)

The sign follows from f^(2k-1)(q)=-(2k-1)![q^(-2k)-Re(q+ix)^(-2k)]. The exact remainder is, up to its irrelevant overall sign, the integral of the periodized B_(2K) times f^(2K)/(2K)!. One can recover this standard form from DLMF 2.10.1 by integrating its constant B_(2K) term once and including the kth endpoint correction. No divergent asymptotic series is declared convergent.

For EVERY real x and t>0,

    |f_x^(m)(t)|<=2m! t^(-m-1),

since |t+ix|>=t. The Bernoulli Fourier series gives

    ||periodic B_(2K)||_infinity/(2K)!
       <=2 zeta(2K)/(2pi)^(2K).

Use zeta(2K)<2 (already true at K=1, by integral comparison) and pi>3. Integrating the derivative bound proves

    sup_(x real)|R_(N,K)(x)|
       <=8(2K-1)!/[6q]^(2K)=epsilon_(N,K).          (2)

The elementary integral in (1) is EXACT. Only the bounded correction has been approximated. This is not the old Bernoulli-origin expansion: no condition |xi|<q/pi, support-distance radius, or ordinate limit appears. In particular M(x)=log|x|+O(1) at infinity. The principal logarithmic coefficient survives.

For K=N>=1 the simple factorial bound (2N-1)!<=(2N)^(2N) gives

    epsilon_(N,N)<=8*9^(-N).                        (3)

Consequently uniform absolute accuracy costs at most O(log(1/accuracy)) terms in this representation. The sharper exact N=32 factorial budget is approximately 7.124343841839318e-59. Equation (3) is a cost bound for representing the multiplier, NOT a complexity guarantee for solving its whole-space inverse or certifying a Schur block.

External theorem pins: https://dlmf.nist.gov/2.10.E1 (Euler--Maclaurin integral remainder) and https://dlmf.nist.gov/24.8.E1 (Bernoulli Fourier bound). The derivative estimate and their application to this original Euler tail are derived here. The analytic theorem is not Lean-formalized; finite tests do not certify the continuum theorem by sampling.

## 2. Whole-domain form sandwich, with original arithmetic untouched

Define on the ORIGINAL canonical supported logarithmic domain

    Qminus=Q_N+integral M(pi|xi|)|hhat(xi)|^2 dxi-epsilon mass,
    Qplus =Q_N+integral M(pi|xi|)|hhat(xi)|^2 dxi+epsilon mass.

Plancherel and (2) give the whole-domain inequality

    Qminus<=Q_original<=Qplus,
    0<=Q_original-Qminus<=delta mass, delta=2epsilon. (4)

Mixed-form differences are represented by a bounded self-adjoint physical multiplier. Qminus itself remains an UNBOUNDED logarithmic form; its finite corrections are bounded rational multipliers. Its form domain is the original canonical domain, not all supported L2. Adding a sufficiently large mass constant gives equivalent canonical coercivity. Physical compact inclusion and compact-resolvent structure therefore remain available.

This cannot be inserted into NF63's BOUNDED F_32 inverse while keeping the same compact gain. The principal operator has changed from a constant background to a logarithmic one. A future inverse/complement calculation must explicitly retain this unbounded principal part. No such whole inverse calculation is supplied in CC6.

All original primes, prime-power weights, orientations and both signed pole slots are identical. Complete original source coordinates give

    Qminus(h)=||P h||^2-||N h||^2-R(h), 0<=R<=delta mass. (5)

P,N are the complete ORIGINAL analysis, not newly assigned divisor rows. The comparison defect can be realized as a bounded auxiliary channel, but it is not an actual divisor source or evidence for original negativity. Prime threshold equality remains zero overlap in both forms. Fixed-vector support inclusion leaves Qminus unchanged, exactly as it leaves the original form unchanged.

## 3. Certified-positive controls recovered, not new apertures

At the imported aperture-one anchor, (4) yields

    Qminus_1 >=(4e-32-delta) mass >3.99e-32 mass,
    Qminus_1 >=(2e-34-delta) E_log >1.99e-34 E_log,

using mass<=E_log. This is a proved positive WHOLE-domain lower comparison at the existing anchor, conditional on its existing internal certificate. The original constructor is not replayed, and its historical constants are unchanged.

For CC5's unchanged native-positive vector at a=21/20, its exact saved interval [qlo,qhi] and mass give

    Qminus(h)>=qlo-delta mass>0,
    Qminus(h)/mass>1.87e-32.

The certificate imports the exact CC5 native replay endpoints and checks this inequality by rational arithmetic. It does not integrate the new logarithmic multiplier on that vector or claim a whole target lower bound. The inference from (4) is nonetheless rigorous, unlike a positive floating restriction. The former N=32 lower cutoff is negative on this SAME vector; adding the retained tail changes the comparison, not the original energy. NF64's independent cutoff witnesses and certificates are left untouched.

## 4. Exact completed-Schur comparison bound

Use one CC4 protected fixed physical chart E+F. Let the ORIGINAL complement C>=c mass, original completed graph W, and original exact Schur S. Suppose c>delta. The comparison complement obeys Cminus>=c-delta>0, so its EXACT completion Sminus is lawful.

Every vector with retained coefficient x is W x+z, z in F. Original square completion and (4) give

    Qminus(Wx+z)>=S(x)+c||z||^2-delta||Wx+z||^2.

Minimizing the right hand side over unrestricted physical z only lowers it, and completing the physical square gives

    S-delta*c/(c-delta) W^*W <= Sminus <= S.          (6)

The upper bound follows by testing the original minimizer Wx. The lower bound uses the ENTIRE graph mass, not just the retained finite coefficients; W need not be physically orthogonal to F. It does not replace either actual inverse by the same residual Gram or drop perturbed cross blocks. The finite control script verifies (6) on 324 exact genuinely coupled 2x2 completions with simultaneous perturbations in all blocks.

If S>=mI and ||W||_(coeff->mass)<=Mgraph, put

    theta=delta*c*Mgraph^2/[(c-delta)m].

When theta<1, (6) implies

    (1-theta)S<=Sminus<=S,
    0<=log det S-log det Sminus<=-dim(E) log(1-theta). (7)

At two endpoints the difference between original and comparison accumulated log-determinant losses is bounded by the sum of their endpoint budgets in (7). This is a faithful error budget for an eventual loss computation. It is not an independently evaluated bound on either aperture loss.

Known graph/complement bounds and a KNOWN positive Schur margin can therefore determine representation accuracy before a new inverse calculation. CC6 has not computed these inputs for the whole 21/20 chart. At a shrinking unknown original margin, theta may grow without bound even for tiny fixed epsilon. Refining N as the margin shrinks is possible at the multiplier level but is not a proof that the original margin stays positive.

## 5. Genuine crossing, positive-eigenmode and contact boundaries

CC4's genuine differential and canonical logarithmic crossing operators remain countercontrols. A mass-small multiplier error does not remove an original crossing. At any original null vector, Qminus(h)<=0 by (4); it cannot produce a positive certificate across actual contact. A fixed lower comparison may reach zero slightly earlier while the original form is still positive. No finite absolute tolerance rules out that event.

For an original positive eigenlevel mu, shifting both forms subtracts EXACTLY mu mass. Their difference is still R. Thus original Q(h)=mu mass does not become original nullity: (Qminus-mu mass)(h)=-R(h)<=0. The finite script also tests a positive mu smaller than delta, demonstrating why comparison nullity must not be mistaken for original contact.

The corrected representation removes CC5's unavoidable 1/N^2 discarded-positive-energy floor; it does not remove CC4's relative division by the true shrinking gap. The original exact shell reaction H^*D^(-1)H still needs an arithmetic estimate. Neither (2), (6), nor retained-tail positivity at the anchor supplies such an estimate.

## 6. Decision and validation boundary

Retire the discard-tail truncation as the practical comparison at the tiny-gap witness. Keep the retained logarithmic principal part for the next original/comparison inverse and completed-Schur calculation. This is a concrete usable representation theorem with a whole-domain error budget, rather than another claim that an unspecified finite cutoff must eventually succeed.

Eight exact tail-decomposition interval controls, 64 geometric-budget controls and 324 coupled Schur controls pass. The tail checks compare a 32-term model with an exact 64-term tail segment plus a separately bounded model starting at N=96, including x=10^6 beyond any local expansion radius. They are finite algebra/interval controls; the uniform remainder proof is analytic. No quadrature-only sign, new whole-domain aperture, computed target Schur, original contact exclusion, RH, F4, full source/Gram archive replay or Lean result is claimed. Both paused branches remain untouched.
