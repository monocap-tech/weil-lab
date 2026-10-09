# CC59: a sharper correlation estimate from the original high floor

Read [definitions](../docs/TERMINOLOGY_RPB108_CORRELATED_HIGH_FLOOR_CC59.md) first. CC59 is a conditional original-carrier operator theorem with exact abstract controls. It evaluates no new native source Gram. NF22 had not appeared at independent source head de3f69bd4121aa586b480222405a480f1edf0f17 when this turn recovered the repository.

## Result

The coarse sufficient estimate P2/kappa can be sharpened using the tail sources of the SAME two measured high polynomials, without computing a complete high inverse or adding more measured modes. With the matrices defined below,

    T_rest <= U_corr = [P2-Z*V^{-1}Z]/kappa <= P2/kappa,
    V=C2(C2-kappa I)+H.

Therefore U_corr<S2 is another sufficient certificate for original whole-domain positivity at a=53/50. It can succeed when P2<kappa S2 fails. Its extra data H,Z are already contained in NF21's planned complete 58-source Gram D; no new source functions beyond those 58 are required.

This retains a concrete collective phase correlation, but is an UPPER response bound. It does not establish the requested uniform defect-relative LOWER frame on actual critical eigenvectors.

## Actual high-form derivation

Work separately in one original physical parity. Within F112 split H2, the two measured physical high modes, from U=F112 intersect H2-perp. Polynomial source-domain membership makes the mixed map K:H2->U a bounded finite-rank physical source map. The complete high form has blocks

    C_full = [[C2,K*],[K,D_U]] >= kappa I,  kappa=207/1000.

D_U is the restriction of the canonical high form; it need not be a bounded physical operator. The native C2 is strictly above kappa: NF20 lower bounds its smallest eigenvalue by 14/5 even and 289/100 odd. Thus C2-kappa I has a positive inverse.

Complete the square in the shifted form C_full-kappa I, minimizing over H2. This gives the valid form inequality on U

    D_U >= kappa I+K(C2-kappa I)^{-1}K*.

The unshifted effective high form after eliminating H2 consequently satisfies

    D_eff = D_U-K C2^{-1}K*
           >= kappa[I+K M K*],
    M=C2^{-1}(C2-kappa I)^{-1}>0.

C2 and its shifted inverse commute; no commutativity of the original infinite operator and physical trial projections is assumed. Both sides are coercive closed forms. Inverse order reverses their ordering. The two-mode compensated retained source sigma has zero H2 physical coordinates, so its true remaining reaction is

    T_rest=sigma*D_eff^{-1}sigma.

Let P=P2=sigma*sigma, H=K*K and Z=K*sigma. The finite-rank inverse identity gives

    [I+K M K*]^{-1}=I-K[M^{-1}+H]^{-1}K*,
    M^{-1}=C2(C2-kappa I).

Taking the sigma pairing proves the displayed U_corr bound. Positivity of the inverse ensures P-Z*V^{-1}Z>=0. An actual margin theta A follows if U_corr<=S2-theta A. A source-norm bound is thereby replaced by a joint Gram estimate involving its correlation with the known high sources.

## Precisely sharp under these partial data

For fixed C2,K,sigma and floor kappa, the least compatible high completion is

    D_min=kappa I+K(C2-kappa I)^{-1}K*.

Its shifted complete high form is positive semidefinite by exact square completion, and its effective high inverse ATTAINS U_corr. Increasing the unknown high form only decreases the reaction. Thus no smaller universal response upper bound follows from just C2,K,sigma and this floor. Additional original arithmetic information can improve it; this is not sharpness under all Weil identities. A compact-resolvent abstract realization can append a diagonal growing operator on a complement orthogonal to these finite source spans without changing any tested response.

## Recovering H and Z from the planned native source Gram

Write D for NF21's complete physical source-square Gram on E+H2, and T=[I;-C2^{-1}B*]. Physical source projections of the high columns onto E and H2 have matrices B and C2. Physical projections of LTx onto E and H2 are S2 and zero. Therefore

    H = D_HH-B*B-C2²,
    Z = D_H,: T-B*S2,
    P = T*D T-S2².

Every entry uses the COMPLETE original archimedean, prime and pole action, including all source-sector crosses. NF21's e0/e1 prime-plus-pole sector alone supplies none of these complete matrices. To avoid subtracting large source-square terms, compute directly

    K_j=P_U L phi_j,
    sigma_i=L(T e_i)-sum_(k in E) (S2)_{ki} e_k,
    H_jl=<K_j,K_l>,  Z_ji=<K_j,sigma_i>,  P_il=<sigma_i,sigma_l>.

The joint physical Gram [[P,Z*],[Z,H]] must be positive semidefinite. Enclosures must pay errors in both compensated sources and high sources, in C2 and its products, and in the inverse and final subtraction. The positive finite matrix V has the native lower bound V>=C2(C2-kappa I)>0, making its inverse well-defined; it does not remove near-critical conditioning of the retained sign. CC58's direct-source error bounds remain useful, but they do not by themselves pay perturbations of K,C2 or V. No error ledger is silently declared complete here.

## Exact controls

The [Fraction validator](../scripts/validate_correlated_high_floor_cc59.py) checks the high-floor square completion, finite-rank inverse identity, attained response, monotonicity under four unknown-high increments, recovery of H,Z from a full physical source matrix, and positivity of the correlation subtraction. [Output](data/RPB108_CORRELATED_HIGH_FLOOR_CC59_VALIDATION_20261009.json); [custody](data/RPB108_CORRELATED_HIGH_FLOOR_CC59_CUSTODY_20261009.json).

A scalar measured block c=3, measured-to-unmeasured coupling k=3 and floor kappa=207/1000 give

    D_min=kappa+9/(3-kappa),
    effective high floor=kappa[1+9/(3(3-kappa))],
    physical residual squared P=1.

For retained corrected S2=4, the coarse response bound 1/kappa is greater than4, while the correlated bound is strictly below4. The complete original model is positive and the sharper gate certifies it. A unit residual on a separate floor-kappa coordinate orthogonal to K has the SAME physical residual norm but no improvement. Thus the phase alignment Z is load-bearing, not replaceable by P alone.

Three genuine crossing controls set S2=U_corr+epsilon for epsilon=1/100,0,-1/100 with the least high completion. Their full Schur sign is exactly epsilon; the refined bound attains it, while the coarse sufficient gate fails throughout this crossing collar. At epsilon=0 the complete model has an actual null vector, not a truncated null.

Three positive ground-level controls add mu I to the high completion and set the low block to U_corr+mu for mu=10^-40,1/100,1/20. The complete vector has original energy mu times its physical mass. The WHOLE physical shift produces a null and the retained-only shift misses it. The shifted correlated bound attains contact. These are genuine finite model eigenlevels, not original Weil zeros or crossings.

## Next native checkpoint and remaining theorem

Preserve NF22's staged native archimedean construction and directional witness checks. Besides sigma, retain the two projected high-source vectors K_j; their H,Z joint Gram permits this sharper gate at the same source-construction frontier. If the coarse gate fails, test the correlated gate before concluding that a full high inverse is indispensable. If the refined gate fails, that is still inconclusive about actual negativity, because D_U can be strictly larger than its least completion.

The exact minimal positivity condition remains T_rest<S2. Neither P nor H nor Z is completely enclosed natively here. An old-gap-independent cap-uniform theorem requires quantitative bounds on these actual correlations, and a defect-relative lower frame requires a separate critical-space lower estimate. CC59 supplies a conditional mechanism and sharp partial-data controls, not those estimates. No logical nonimplication from complete Weil identities is proved. Whole positivity remains certified at21/20; target53/50, actual contact exclusion, RH/F4, full transport and Lean remain open. Paused fronts and historical wording are untouched.
