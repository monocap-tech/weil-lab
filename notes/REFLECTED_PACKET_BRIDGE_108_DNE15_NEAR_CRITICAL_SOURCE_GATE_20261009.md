# RPB108 DNE15 — Near-critical complete source norms reject the coarse residual gate

Date: 2026-10-09 UTC. Independent DNE continuation from70554a248d88b0ee6f1ed13ce95538c0fefa0500. [Definitions](../docs/TERMINOLOGY_RPB108_DNE15_NEAR_CRITICAL_GATE.md).

## New arithmetic result

DNE14's successful compensated constant-line test does not extend to the actual near-critical targets. At a=53/50, both NF24 rational directions have complete original physical residuals whose squared norms rigorously exceed the scalar-floor budget.

| Paid native quantity | Even | Odd |
|---|---:|---:|
| Frozen compensated energy Q(p,p), approximate display | 9.25563570359728e-35 | 3.30701999543587e-31 |
| Complete F112 source residual squared, approximate display | 3.24016495886e-35 | 9.26898325531e-32 |
| CERTIFIED exact-H2 ratio P2(x)/S2(x) | (0.35007,0.35008) | (0.28028,0.28029) |
| Coarse required ratio upper | 0.207 | 0.207 |
| Scalar-floor gate | **Fails** | **Fails** |

Thus each parity's full56-dimensional coarse matrix gate `P2<kappa S2` has an actual rational retained direction violating it. The complete P2 matrices need not be constructed to prove this failure. This says nothing adverse about the actual infinite Schur sign: the true inverse may be much smaller on these source vectors than1/kappa.

## Authenticated inputs and independent native source evaluation

The NF24 target ledger was recovered at read-only Aperture head b7fa4461ab4cca2ebc9383ae4b9407c03a580826. Its exact bytes match the published SHA256:

    6eee61fb4e58ac5be0e95f492f461b289da37ee13aeaa74bbf4acc06f6650c00.

The ledger specifies all56 retained rational coefficients, both rational high coefficients, their exact-H2 minimizer enclosures, finite energies, norms and all56 certified low source coordinates. It authenticates its NF17/NF18/NF19 input hashes. DNE15 does not claim a fresh replay of those raw matrix archives.

The copied target is published as deterministic gzip/base64, with decoded bytes checked against the same hash. Source construction here is independent of the missing raw matrices: physical normalized Legendre polynomials, exact singular polynomial action, original endpoint logs, all six active prime powers {2,3,4,5,7,8} in both orientations, and the correct signed even/odd poles are evaluated directly. The certified complete low projection square is subtracted AFTER the full source square is enclosed.

All archimedean/prime/pole cross-correlations are retained before squaring. No tiny remaining high pairing is set to zero, no prime reflection is made positive, and no endpoint strip is discarded.

## Paid errors and replay

The primary runs use600-digit directed Decimal intervals, r_360 and degree64 pole exponentials; the replay uses650 digits and r_400. The smooth source operator error is

    epsilon_N=[2a*(550/19)*(106/125)^N+3e-99]||p||_2.

It is about1.025e-24 at N360 and1.401e-27 at N400. The source-error bound is independent of polynomial degree. With T_N the enclosed COMPLETE source square, the actual projected norm square receives the additional radius

    epsilon_N*(2 sqrt(T_N^upper)+epsilon_N).

Projection is a contraction. The row's native energy is taken from the independently certified NF24 finite form intervals; source approximation error is not incorrectly used to estimate an energy on the1e-35 scale.

The primary ratio intervals for the frozen rational p are approximately

    even: (0.3500746889,0.3500749416),
    odd:  (0.2802820425,0.2802820465).

Higher-order replay narrows them to

    even: (0.350074815067,0.350074815413),
    odd:  (0.280282044499,0.280282044506).

All displayed decimal intervals here are widened outward. Primary and replay enclosures overlap and agree with NF24's independently structured, non-certifying Gaussian source diagnostic. The inequality conclusion uses the paid intervals, not this numerical agreement.

Rational r_N coefficients follow DNE11's exact recurrence. Pi uses the400-term Fraction Machin enclosure. Gamma uses H100 and200 Bernoulli pairs with the first-omitted B402 remainder bound, then directed conversion. Decimal ln/sqrt endpoints are widened by a representable neighbor; basic arithmetic uses directed floor/ceiling contexts.

## Faster exact moment construction, lawful in both parities

The regular convolution polynomial is grouped by endpoint moments before multiplying the kernel coefficients. For p(x)=sum p_k x^k of parity s in {0,1}, put

    M_t=sum_(k congruent s mod2) p_k*a^(k+t+1)/(k+t+1).

For each kernel monomial r_m |x-y|^m, the low polynomial coefficients are

    2*(-1)^s*r_m*binom(m,l)*M_(m-l), l congruent s mod2.

When m is odd there is also the high contribution

    2*r_m*p_k*Beta(k+1,m+1)*x^(m+k+1).

This is the same split convolution as DNE14, evaluated in O(N²+N degree(p)) interval operations. Odd parity changes the sign of the low endpoint contribution; it is not silently reused from the even formula.

For log moments use a polynomial-division primitive rather than a large binomial substitution. With b=-sign*a,

    J_k^sign(x)=([x^(k+1)-b^(k+1)]log(a+sign*x)-S_k)/(k+1),
    S_k=b*S_(k-1)+x^(k+1)/(k+1), S_-1=0.

At x=b the logarithmic product has exact limit0. The complete-interval log² moments remain DNE11's beta-derivative moments. Odd monomials on individual prime panels are included.

Independent Fraction controls passed1462 assertions, including both signed convolution parities and the stable primitive derivative cancellation. All116 singular Legendre-action identities through degree115 passed. Each native run checked its complete even log moments against beta derivatives and the odd half-interval x-log moment against its closed form. Both primary/replay producers and the rational gate-transfer validator ran locally. No Lean or GitHub Actions execution is claimed.

## Exact transfer from frozen rational correction to the H2 minimizer

Let delta be the difference between the frozen high coefficients and the true C2 minimizer. The authenticated ledger encloses each component by less than1e-60 (actual upper errors are below1e-80).

For every normalized high phi_n, n112..115, the native source formula gives `||L_Q phi_n||_2<200`. An explicit conservative ledger is:

- constant part<3 and harmonic singular action<6;
- endpoint-log part<11, since ||log(a²-x²)||_2<2 and ||phi_n||_infty<11;
- regular convolution<62, using the DNE11 Cauchy bound sup|r|<=550/19;
- all six two-orientation prime actions<12;
- both pole rank-one actions together<18.

The total is112<200. The log-norm inequality follows from the exact beta moment and0.74<log(2a)<0.76, pi>3; the other displayed numerical guards are independently checked in the rational transfer validator. Standard |P_n(t)|<=1 on[-1,1] controls the Legendre supremum.

Therefore the physical source change is below4e-58. Since both residual squares are below1e-30, their squared-norm change is below1e-72. CC60's original native C2 spectrum is below5, so exact high completion lowers the finite energy by less than1e-118. Adding these payments preserves both displayed ratio brackets and strict coarse-gate failures.

Consequently the failure is not caused by freezing the two-mode inverse. It also holds for the EXACT H2 compensated sources, whose H2 pairings vanish and whose residual is P_U L_Q p_star.

## Concrete next arithmetic target

CC59 bounds the unmeasured reaction by

    T_rest <= [P2-G]/kappa,
    G=Z*V^-1 Z, V=C2(C2-kappa I)+H.

On the now-measured exact targets, this sufficient gate requires

    G/P2 >1-kappa/(P2/S2).

The required fraction lies in(0.40868969,0.40870659) even and(0.26145283,0.26147919) odd: about40.87% and26.15%. These quantify the native correlation improvement needed. No native H,Z,G or successful CC59/CC60 gate is evaluated here.

DNE16 should compute the projected high-source correlations with these compensated residuals, then test CC60's fixed rational variational correction with BOTH low and measured-high projections paid. Alternatively use a stronger source-aligned high-form estimate. Repeating a norm-only floor or extending the constant-line result cannot repair the certified failure.

## Scope

DNE15 closes two COMPLETE cancellation-sensitive near-critical physical residual norms and proves failure of the exact two-high-compensated coarse scalar/matrix sufficient gate in each parity. It does not compute the full residual Gram, determine the true inverse-weighted reaction, prove native negativity, exclude nulls, certify whole1.06, or settle global contact, F4, transport, RH or Lean. DNE14's constant-line theorem is unchanged. Other branches receive no writes.

Reproduce with the published producer, a decoded or.gz.b64 target, a parity argument and an output filename. Environment variables DNE15_PRECISION and DNE15_ORDER select600/360 or650/400. The transfer validator accepts --targets, --even and --odd certificate paths.
