# CC58: native NF21 sector recovery and compensated arithmetic correlation

Read [definitions](../docs/TERMINOLOGY_RPB108_COMPENSATED_CORRELATION_CC58.md) first. This additive continuation preserves NF21 and CC57 and does not restart paused global or endpoint-regularity work.

## Recovered original arithmetic

NF21 source revision 7fbb9fa82eef68d55018d858446f174b7ba8aca0 defines the exact source-square matrix D, the compensated lift T=[I;-C2^{-1}B*], and P2=T*DT-S2*S2 with S2=A-BC2^{-1}B*. Subsequent source revision de3f69bd4121aa586b480222405a480f1edf0f17 links that work from NF20. Neither recovered revision supplies a complete evaluated P2.

The deterministic native producer `certify_native_source_square_prime_pole_nf21_106.py` was replayed. All original six active prime powers 2,3,4,5,7,8, twelve oriented shifts, 82 ordered nonempty overlap pairs, signed poles, and both prime-pole crosses are retained. The [archived exact rational intervals](data/RPB108_NATIVE_PRIME_POLE_SOURCE_SECTOR_CC58_20261009.json) give

| Original source-square channel on e0/e1 | Even approximate value | Odd approximate value |
|---|---:|---:|
| Prime-prime | 4.249294 | 2.322359 |
| Pole-pole | 21.678748 | 0.176303 |
| Sum of both prime-pole crosses | -18.683476 | -1.217839 |
| Complete prime-plus-pole sector | 7.244566 | 1.280823 |

Exact checks establish 7.244<K_sector,00<7.245 and 1.280<K_sector,11<1.281, each enclosure width below 10^-38; parity cross is zero. These are source-square values, not native Q energies. The original pole quadratic form is positive even and negative odd. The archimedean source and its mixed crosses are omitted in this sector certificate, and e0/e1 is not the two-mode compensated 56-column carrier. No full-source norm, residual norm, sign or frame follows from these numbers.

The upstream symbolic validator requires unavailable SymPy. CC58 replays its SAME rational Q and R arrays using exact Fraction matrix arithmetic, verifying all its identities and positive residual determinant without that dependency. This is an exact algebraic replay, not a claim that the unmodified upstream executable ran successfully. The native interval producer itself ran unmodified. Its raw JSON SHA256 exactly matches NF21: 9ea91c5d0bf9bac4cf32d8a2bb3644c6fb7d9dd004ad3ebc5f5aac0ee1b01648. The separate upstream low2 consumer also ran unmodified against the authenticated original E112 archive: all eighteen rational checks, including both signed native pole moments, pass; [replay output](data/RPB108_NF21_CONSUMER_REPLAY_CC58_20261009.json).

## Direct complete-arithmetic correlation formula

Fix one parity at a=53/50. Let e_n be the physical orthonormal supported Legendre basis; E is the original 56-dimensional retained parity space and H2 consists of e112,e114 even or e113,e115 odd. For EVERY unmeasured high n, define

    r_n = q_nE - q_nH C2^{-1}B*,
    q_nE,i=Q(e_n,e_i),  q_nH,j=Q(e_n,phi_j).

Every pairing is the complete original signed arithmetic, including archimedean, prime and pole terms. For p_x=Tx, Q(e_n,p_x)=r_n x. Physical L2 source representability for this finite polynomial carrier and Parseval therefore give the exact convergent matrix series

    P2 = sum_{n in high, n not in H2} r_n* r_n.

The two measured high coefficients vanish by C-form compensation; the retained coefficients are S2x. Consequently this formula agrees with T*DT-S2*S2, but never subtracts the retained squared action. It is distinct from summing separate sector squares: each r_n must be formed with all signed contributions BEFORE its square is taken. Cross terms survive inside r_n* r_n.

This identifies a concrete sufficient arithmetic correlation estimate:

    sum_n r_n* r_n < kappa S2,  kappa=207/1000.

For a desired retained margin theta A, replace the right side by kappa(S2-theta A), assuming it is positive. This is sufficient because T_rest<=P2/kappa. The minimal exact inverse-response condition is T_rest<S2, or T_rest<=S2-theta A for the margin; the physical correlation estimate is a stronger sufficient surrogate. It does not give a lower frame bound on critical eigenvectors.

A finite row sum K_J satisfies K_J<=P2. Thus K_J>=kappa S2 in any tested direction can refute this sufficient estimator, whereas K_J<kappa S2 cannot certify it without an upper bound on ALL omitted rows. Physical L2 existence proves convergence but supplies no computable tail bound. CC57 also rules out deriving physical residual convergence solely from form convergence of increasingly large compensated lifts. This new fixed-lift Parseval sequence converges monotonically to its Gram, but remains a sequence of lower bounds.

## Paying error before squaring

Let R denote the exact compensated high-source map and Rhat a directly constructed approximation. If ||R-Rhat||<=eta in physical operator norm, for any t>0 the exact Young majorant is

    P2 <= (1+t)Rhat*Rhat + (1+1/t)eta² I.

This follows from ||Rhat x+(R-Rhat)x||² and pays ALL truncation, panel, source and compensation errors in eta. It is not enough to bound the source errors while treating C2^{-1}B* as exact: interval errors in that coefficient matrix must also enter the residual radius. A certified lower enclosure S2_lower can be used on the right side of the gate.

Alternatively define delta=||(R-Rhat)S2^{-1/2}|| and p_hat=||Rhat S2^{-1/2}||². Then

    ||P2||_(relative S2) <= (sqrt(p_hat)+delta)².

An upper bound below kappa suffices. This weights the collective source geometry by the actual corrected retained energy and avoids inserting an old continuation gap. Its usefulness still requires quantitative arithmetic enclosures; simply naming S2^{-1/2} does not supply them. For a cap-uniform theorem, the required constants and margins must hold uniformly over that cap, with an appropriate critical defect metric for a defect-relative claim. None is certified here.

The exact enclosure control in the validator uses S2=10^-39, direct source radius 10^-25 and independent square error 10^-38. The direct squared radius is below kappa S2 while the independent square error is above it. This demonstrates why constructing a canceled source before squaring can pay much smaller errors; it supplies no native bound for Rhat or eta.

## Controls and limits

Five exact Young majorants and a Parseval split of the recovered NF21 rational arrays pass. A fixed included source of magnitude two can be completed by an omitted sector of minus two, minus one, zero or two, yielding full square zero, one, four or sixteen. Therefore an included sector alone cannot determine the complete square without a bound or exact identity for the omitted sector. This abstract completion does not alter the actual fixed Weil arithmetic.

Three genuine Schur crossing controls have high C=1, mixed source b=1, low A=1+epsilon and complete corrected sign epsilon. Three genuine positive ground eigenlevels mu=10^-40,1/100,1/20 use C=2, b=1, A=mu+1/(2-mu). The vector (1,-1/(2-mu)) has original energy mu times its mass; the WHOLE physical mu I shift creates an exact null and a retained-only shift misses it. The correlation construction therefore remains valid without mistaking a positive eigenmode for an original null. These are exact abstract controls, not native crossings.

The [validator](../scripts/validate_compensated_correlation_cc58.py), [validation](data/RPB108_COMPENSATED_CORRELATION_CC58_VALIDATION_20261009.json) and [custody](data/RPB108_COMPENSATED_CORRELATION_CC58_CUSTODY_20261009.json) record the result. NF21 explicitly stages NF22 to construct the full archimedean source first on e0/e1 and then on the explicit near-critical witnesses. Coupled preserves that staging; it does not duplicate the independent producer. Its integration target is a direct enclosure of the complete compensated source, including all archimedean crosses, with a rigorously bounded high tail, or a sharper C_full-dual response estimate. Adding partial sector squares or finite rows cannot supply an upper certificate.

The full original identities have not been shown logically insufficient. The recovered estimates do not yet establish the quantitative cap-uniform, old-gap-independent leakage or defect-relative lower frame. Complete target53/50 positivity, actual contact exclusion, RH/F4, full transport and Lean remain open. The established whole-domain positivity anchor remains21/20.
