# RPB108 RC94 — A certified odd weak Schur block

Date: 2026-10-11. Branch: `research/rpb108-route-consolidation`.
Predecessor: RC93, commit `3b113d8fb33a43f047d796706952be2a120b20b7`.
Aperture: B=1.10, full physical interval length 2.20.

RC94 certifies the full two-dimensional **known odd weak corrected Schur block**, including its cross entry. This is a restriction of the complete rank-1250-head Schur condition to the fixed odd RC63 span. It is not complete-head positivity or a weak/strong elimination theorem.

The four-input source calculation adds only the 128 missing same-parity physical Legendre pairings for degrees 64 through 127. No dense 128-feature Weil head is evaluated. The stronger capture, its canonical tail theorem and the matching RC93 Riesz-error transport reduce the source coupling upper enough to close the odd block. The even block remains unresolved, with even weak_0 the sole remaining negative directional lower among the four fixed modes.

## Exact odd-block acceptance

Let Q_o,lower be the updated signed original Weil lower on the odd weak_0/weak_1 basis, and G_o the RC94 coupling upper. Exact Fraction arithmetic proves

    G_o <= lambda_o Q_o,lower,
    lambda_o < alpha = 247/2500 = 0.0988.

The accepted rational lambda is

`108435948083/1099511627776` (approximately 0.098621920263213).

Therefore

    Q_o,actual − alpha^(-1) Gamma_1250,o
      >= Q_o,lower − alpha^(-1) G_o
      >= (1−lambda_o/alpha) Q_o,lower > 0.

The retained fraction is approximately 0.001802426486. A separate exact lower bisection against the actual canonical Gram upper proves the corrected odd weak block has canonical floor at least

`588757210431/68719476736000000000000000000` (approximately 8.56754501628e-18).

The direct 2×2 corrected lower has approximately

    diagonal entries: 3.4319761e−16 and 3.5599923e−13;
    cross entry:      1.0917169e−14.

Both the positive leading entry and determinant are checked exactly. These displayed approximations are explanatory; they do not determine acceptance.

The result concerns the complete original Weil source, not a reference source. For a head vector R, q=LR and S=i*(q+K iR)=R+i*K iR. Since R belongs to H1250, its complement projection is precisely the head/complement coupling. Thus the source covariance is the required Schur coupling covariance on these weak inputs.

## The source calculation

RC93 used physical Legendre subtraction below degree 64. RC94 retains that exact subtraction and adds only degrees 64 through 127. The four weak inputs are ordered even weak_0, odd weak_0, even weak_1, odd weak_1; opposite-parity source pairings vanish identically. There are 32 new same-parity pairings per input, 128 total.

The target trial coefficients are the unchanged RC67 64-mode coefficients multiplied by the fixed RC63 weak vectors. The target q-polynomials are the full native Chebyshev-to-Legendre map multiplied by those vectors; their degree bound remains 22, even though there are only four target columns. Source forms are built directly on these combinations before integration.

Every new pairing includes the archimedean logarithmic and regular source, all 14 signed prime-power translations with their exact support segments, and the signed pole. No cross-source term is discarded or bounded separately at this pairing stage. The same nominal source approximation as RC68 is used, so its existing operator error allowance remains attached.

For each new Legendre degree n, let h_n be the weak pairing center, r_n its interval radius and m_n=2.20/(2n+1). Subtraction coefficients h_n/m_n are fixed rational numbers. The nominal residual center is reduced by the exact PSD capture increment sum_n h_n^T h_n/m_n. Its entry radius increases by

    sum_n (|h_ni| r_nj + |h_nj| r_ni)/m_n.

This is the fixed-coefficient residual identity, with every pairing error paid. The RC93 weak residual centers and radii are the starting point. Weighted symmetric row bounds then give the new physical residual upper.

Pairings are rounded outward to a 10^34 rational grid during generation. Replay uses a finer 10^36 grid and verifies containment in every saved generation interval before reusing those intervals. No rounded center is accepted without its radius.

## Rank-128 tail and projection scope

H128=i*P_<128 is nested inside H1250. Canonical orthogonality to H128 implies physical annihilation of all Legendre polynomials below degree 128. The plane-wave remainder and an infinite geometric Legendre-tail estimate give the cumulative Fourier bound

    theta128(L) <= 4 B L (2 pi B L)^256 /
                   ((257!!)² [1−(2 pi B L)²/259²]).

A lower staircase for log(e+|xi|), with frequency spacing 1/50, closes after 702 layers at L=14.04. It proves the complement embedding norm upper approximately 0.5960636733, improving RC93's 0.6613593207. All frequency layers, the energy lower, rational e/pi enclosures and exact norm upper are recorded.

The actual source-transfer upper from RC93 scales by tau128²/tau64². This follows because the inherited archimedean, prime and pole transports each use one complement embedding factor, and their degree-below-38 subtractions still lie in H128. It does not add a second tail factor. The physical Riesz trials and their error covariance remain unchanged.

Hence the nominal projected residual upper N128=tau128² W128,upper and transferred error E128 are legitimate components for the actual rank-128 source complement. The accepted upper is

    G(t)=(1+t)N128+(1+1/t)E128.

Projection nesting gives Gamma1250 <= Gamma128 <= G(t) on the specified weak inputs. The Weil complement floor 247/2500 is used only for rank 1250. No rank-128 Weil complement floor or rank-128 head positivity is claimed.

## Matching head transport and results

The RC93 targeted physical Riesz-error covariance is also valid for transporting the RC92 signed trial Weil entries. RC94 applies the exact original-source identity

    Q(R_i,R_j)=Q(V_i,V_j)
      + <q_i+KV_i,E_j> + <E_i,q_j+KV_j>
      + <KE_i,E_j> − <LE_i,E_j>.

The source norms come from the complete RC68 nominal source Gram plus its approximation error. The physical Riesz-error Gram is RC93's targeted upper; the matching canonical error upper is its physical upper divided by rho=252/257. The negative canonical term retains its diagonal sign. This introduces no new trial solve and no trial/source basis mismatch.

The six updated signed head entries yield full 2×2 Loewner lowers using the same fixed scales (100,1) and (80,1). The odd acceptance would narrowly fail with the older RC92 lower: its source/head upper was about 0.10028. With the matching sharper error transport, it is about 0.098622 and passes the 0.0988 threshold.

The selected rational Young parameters are 39/64 even and 31/64 odd. Both source uppers improve RC93 in the whole Loewner order.

| Direction | New coupling squared upper | Reduction from RC93 | Directional Schur lower | Certified positive |
| --- | ---: | ---: | ---: | --- |
| even weak_0 | 2.34365149e-18 | 44.058% | -1.1640779e-17 | unresolved |
| even weak_1 | 9.63758018e-15 | 61.335% | 6.43238623e-14 | yes |
| odd weak_0 | 3.24689773e-17 | 63.436% | 4.21178058e-16 | yes |
| odd weak_1 | 3.73971401e-13 | 69.043% | 8.55074132e-13 | yes |

Positive directional tests alone do not establish the odd span result: RC94 also proves the full corrected odd matrix positive. The even corrected lower is not positive. This proves no actual negative even direction or actual coupling lower; it leaves that certificate unresolved.

The odd margin is small but strictly rational and positive. It is an internally replayed interval certificate, not a Lean formalization.

## Remaining obligations

The next local target is the even weak_0 coupling, including its cross interaction with even weak_1. Its nominal physical residual center remains positive, approximately 2.18e−18, with a radius approximately 4.06e−19. Further capture or a structural source-tail/correlation estimate may help; current information does not prove actual danger. The existing odd result should be retained while that targeted obligation is investigated.

For the complete matrix Schur theorem, we must additionally certify that all potentially dangerous modes are covered, control the corrected strong head block and pay the weak/strong inverse allowance. Positivity of the known odd principal block does not control those missing off-diagonal interactions. No complete 1,250-feature certificate or global first-contact exclusion follows here.

This pass demonstrates an actual source-side enlargement without dense Weil-head evaluation. It does not show that all remaining calculations can be avoided.

## Verification and deliverables

Inputs, in order: RC93, RC92, RC63, RC67, RC59, RC56, RC43, RC46, RC68 and RC66. SHA-256 digests and relevant source/trial/native/precision crosslinks are checked.

Independent replay reintegrates every new pairing using reflected archimedean logarithmic moments, affine prime overlap moments followed by binomial reconstruction, and a positive Rodrigues pole-moment recurrence. It verifies the factorial tail identity and rational logarithm staircase separately. All 128 finer replay intervals lie within their saved generation intervals. Exact capture PSD checks, whole-source improvement tests, head transport, odd Schur acceptance and canonical corrected-floor tests pass. Replay matches the final certificate exactly.

- `scripts/validate_rpb108_rc94_weak_source_capture_128.py`
- `certificates/rpb108_rc94_weak_source_capture_128.json`
- `notes/RPB108_RC94_ODD_WEAK_SCHUR_BLOCK_AND_SOURCE_CAPTURE_128_20261011.md`

No Lean files or other research fronts are changed. No complete-head positivity, RH or Global/F4 claim is made.
