# IV106 W02 — Grouped-prime and full-pole receiver
Conditional analytic advancement; no E19V release or native promotion. Independent of pending E18X run 45951142451. Parent 6e3d7c56d0544fcf5f94c519385058113348791f. Owner-ratified continuation amendment canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c. Actual source premises authenticated by immutable file readback, not newly native audited.

## Source pins
All paths below are in monocap-tech/weil-lab.
- c5c190aa7955f9da9b430b2facfe7a84c96a09b6: verification/iv106/iv106_e2/ActualZetaIV106E2GammaEnvelope.lean blob 6bf91d7024ab6893500ed12ccc0de2fc769f5e41: E2Quarter, E2Global.
- d5a525ed8c3d47078f99ee3f94dce456562be74d: verification/iv106/iv106_e4/ActualZetaIV106E4PrimeCoefficients.lean blob 819c4bf61052e9d3957d051423cb859c5cd51b39: E4Log_upper.
- 71c0c25b29c0691f20dcd2ee3f4b023f330f2da9: verification/iv106/iv106_e7/ActualZetaIV106E7PrimeCutoff.lean blob dd1fefe2a531cea862fb00c50cda0948c14a0f44: literal inventory 2,3,4,5,7,8,9.
- bcc35ba8eeea7d5be48c666ef91b7c99fa9478d7: verification/iv106/iv106_e1/ActualZetaIV106E1ScalarBudget.lean blob 1b2186914d7b8ca8ff44041d058a435ac9293ba0: E1Budget, pi upper bound.
- 3db252bef308aee24a687735305ba63f81b52a34: verification/iv106/iv106_e10/ActualZetaIV106E10IntegratedCoercivity.lean blob 1b86105df1c7ce949ce7c2ab3f33eabd8fcdb3cb: Gamma_bound, Prime_bound, Pole, Mass, integrability.
- c613964eb4c2f1dd44196b3deb609ea07e3ca9ae: verification/iv106/iv106_c3c/ActualZetaIV106C3ActualConstraints.lean blob 25d13ea5fb5fce899121fd61ab5ae54a5b954002: actual_kernel_closure, Constraints_zero_iff.
- 6d1c092ad7a969663895fbea2391188cbf0d23e8: verification/iv106/iv106_e17b/ActualZetaIV106E17BExplicitReserve.lean blob 941e20215fbdeb15036b3c2442fb733c2ac94033: original factor 21.
- Base research 018f7e59f4129ce521cd3ae86d1afd59d3b64b5f: WeilDefect/Arithmetic/ActualZetaCanonicalNativeEnergy.lean blob bda93aa61bc6580197649833f30394aae943d910, ActualZetaNativeFormOperator.lean blob 93beff3a82207f44fd5a431987c39f1aeb7e0092, and ActualZetaNativeLogBounds.lean blob f8728d020bff9d0427ae6e4969da355f37182224; literal quadratic and bounded ratio.
- Parent symbol-pole receiver report blob 1d32da53f1ec8143dbe5a3bcb76359a602d45bda, including E12/E15/E16 and E19L/M references. Source attachment remains conditional.

## 1. Explicit archimedean shift
Let Gamma(xi)=compactWindowArchimedeanSymbol(2*pi*xi), w=log(e+|xi|), D=20/3. Claim Gamma+D>=w everywhere.
For |xi|<=1/3, E2Quarter and the quarter identity give Gamma>=-gamma_E-pi/2-3log2-log pi. Use gamma_E<2/3, 3<pi<22/7, log pi<=log3+(pi-3)/3<=log3+1/21, w<=1+|xi|/e<=7/6. The elementary e bounds 2<e<3 follow by the exponential series. E4 supplies rational upper logs. Hence w-Gamma<=17404891309/2625000000<20/3.
For |xi|>=1/3, E2Global yields Gamma>=log|xi|-25/(8*pi^2*xi^2). Therefore w-Gamma<=log(1+e/|xi|)+25/8<=log10+25/8<=2713792547/500000000<20/3, using log10=log2+log5. These cover the whole real line; no floating quadrature or numerical symbol sampling. The associated arithmetic checks are executable, not a Lean audit of these analytic implications.

## 2. Supported-window structure retains more than E11
Put c=5003/5000, P0=471031/125000. For d in the actual K=ker(C3Constraints 665 k hk), k=34, define M=physical L2 mass, G=E10Gamma, P=E10Prime, pole H=2|m(d)|^2 by the single signed pole-difference row. On constrained smooth core, E10Gamma_bound and E1Budget imply G>=(c+P0)M, before subtracting the prime energy or adding the pole. E10Prime_bound gives P<=P0 M. Both inequalities extend to K by C3 actual_kernel_closure and continuity of G,P,M in the log norm. In detail Gamma/w and prime/w are bounded real multipliers (base signed symbol ratio is bounded; prime sum is bounded and w>=1); U is contractive, so these quadratic forms are continuous. Closed inequalities therefore extend on the original K; no extra smooth-core hypothesis or numerical rank claim.
Define
 lambda=c/(c+P0+D)=375225/4288318.
 E=G-P+H has the exact decomposition
 E = lambda(G+D M)+(1-lambda)(G-(c+P0)M)+(P0 M-P)+H,
 since (1-lambda)(c+P0)-lambda D-P0=0.
 Every summand is nonnegative on K. Thus, for x=J_K d in ambient weighted Fourier coordinates,
 E(d)>= integral q_Gamma |x|^2 +2|<p,x>|^2,
 q_Gamma=lambda*(Gamma+D)/w>=lambda.
 Here p is any valid ambient Riesz representative of the common pole moment on K, as in parent report. The full pole coefficient 2 is retained, not 2lambda. The positive grouped-prime defect P0 M-P and the positive constrained Gamma surplus may be retained in further lower bounds, but are discarded here. The underlying actual operator is unchanged. This does not assert pointwise replacement of the prime symbol by P0 on ambient L2; the grouped prime estimate uses support, and the Gamma surplus uses the actual constrained kernel.

## 3. Dual certificate
Let B=M_{q_Gamma}+2 p<p,.> on ambient L2 and T=M_{1/q_Gamma}. By the same variational proof as the parent, for raw g with r=J_K^*g and d=C^{-1}r,
 E(d)<=<g,B^{-1}g>
 =<g,Tg>-|<p,Tg>|^2/(<p,Tp>+1/2)
 <= (4288318/375225)||g||^2.
 Inverse scalar factor is 11.428657472183357 (approx), versus 21, a 45.577821561031634% reduction of that scalar upper bound. This is not a measured reduction of the actual residual or Schur margin. It also gives a conditional actual compressed coercivity lambda and inverse norm bound, without evaluating the actual inverse. No claim of pointwise dominance of the previous literal-symbol receiver: retain both as candidate upper bounds and compare whole quadratic forms.
For the full actual 734-coordinate bank, select arbitrary fixed z_i and use the PSD upper residual Gram
 R_ij=<g_i-z_i p,T(g_j-z_j p)>+conj(z_i) z_j/2.
 Then L0-R>=0 on all complex coefficient vectors suffices via E15 completion and E16 synthesis. No row independence assumption, proxy bank, or entrywise minimization. The exact pole/response/outside identities of E19L/M remain required for literal g_i. A certified positive lower q envelope is sufficient in the positive Gram integration. No actual 734-column residual/trial Gram is available from the E19U single pole-row enclosure.
 
## 4. Verification
check_budget.py run locally with exact Python Fraction arithmetic, output preserved in check_budget.out. Remote script blob expected c2137cd91a0124f8dce5776fb236a27199cc60c1. The preceding rank-one rational sample algebra was also actually executed locally in this operation and passed (the previous report did not establish execution at its delivery). Neither sample constitutes native proof. No new CI; analytic attachment and current E18X result remain gated. No numerical bank expansion. Next step is authenticated full action assembly, or if unavailable a sharply scoped native attachment of the analytic receiver on accepted inputs; no independent research front.
