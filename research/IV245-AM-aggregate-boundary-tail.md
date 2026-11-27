# IV245 — Infinite Gamma boundary aggregate and uniform error receiver

## Scope and immutable dependencies
Delegated W02 amendment canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c. Parent IV244 8eeeb8964f208d38d75263e32d51b9e6e5fc2b53, report blob 45ca9f91fac9be3560259d9a15ada9de56b2553f; IV244 exact witness results blob 3906416100c3b468066607c92eb5ac99f858e657; IV243 exact constants blob f83acc6c0e2caf3e05815c3dea219c8ad1774ddb; IV242 boundary identity report blob 19724bfc0e211ff1a5e9b8d1ad9096273067b6ee; inherited IV241 supported logarithmic form domain and original signed arithmetic normalization at source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0. No integrated proof-object dependency; no new native Lean claim or cross-lineage adoption.

## 1. Literal boundary tails by parity
Let I=[-2,2], k_n=2n+1/2, t=2-x in [0,4], F(t)=f(2-t), M_n=integral_0^4 F(t)e^(-k_n t)dt. Write B_m^tail for the IV242 boundary terms n>=m (not the finite truncation Q_m of IV244). On even functions the sinh moment vanishes, and on odd functions the cosh moment vanishes; in either case the remaining hyperbolic moment equals e^(2k_n) M_n, since cosh+sinh=exp. Thus the exact boundary tail in each parity is
  B_m^even=2 sum_{n>=m} |M_n|^2/(1-exp(-4k_n)),
  B_m^odd =2 sum_{n>=m} |M_n|^2/(1+exp(-4k_n)).
For general f use its orthogonal even/odd decomposition; original boundary form has no mixed parity terms.

Define G_m=2 sum_{n>=m}|M_n|^2 for any supported L2 function (no parity requirement). Sum the geometric series to get the integral kernel on [0,4]:
  K_m(t,u)=2 exp(-k_m(t+u))/(1-exp(-2(t+u))).
The identity is valid as a bounded quadratic form, not just an entrywise expansion. For z=t+u>0, K_m=e^(-(k_m-1)z)/sinh(z)<=1/z for m>=1. The kernel value at the single corner is immaterial. Weighted Schur with p(t)=t^(-1/2), t>0, gives
  integral_0^4 (t+u)^(-1)u^(-1/2)du <= pi t^(-1/2)
by u=t v^2 and integral_0^infty 2/(1+v^2)dv=pi. By weighted Cauchy-Schwarz (or Schur test) the Carleman kernel has norm <=pi; the same holds for each finite geometric partial sum and K_m. In particular the double integral with |F(t)F(u)| K_m is finite. Dominated convergence identifies the infinite series and its integral quadratic form for complex L2 functions. G_m is positive because each partial sum is a positive Gram form. This establishes 0<=G_m<=pi Id without any unproved form-domain or entrywise-order inference.

## 2. Uniform near-exact aggregate lower form
Set epsilon_m=exp(-4k_m), or any larger positive epsilon<1. Termwise positive Gram comparison gives
  G_m <= B_m^even <= G_m/(1-epsilon),
  G_m/(1+epsilon) <= B_m^odd <= G_m.
Define the aggregate lower model Q_agg,m=A_N-P+Pi+first m exact boundary terms + G_m(f_even)+G_m(f_odd)/(1+epsilon). It has the original log domain; the aggregate and true tails are bounded L2 forms. Since ||f_even||^2+||f_odd||^2=||f||^2,
  0 <= Q(f)-Q_agg,m(f) <= pi epsilon/(1-epsilon) ||f||^2.
This is a genuine operator-order bound, not entrywise comparison. It holds even when low/high components have cancellation. All original prime translations, Gamma diagonal and both pole signs are unchanged.

For m=4, k_m=17/2 and exp(-4k_m)=exp(-34)<7^(-17) by the authenticated exp(2)>7. Choose epsilon=1/232630513987207. With pi<4 the absolute quadratic form loss is strictly below delta=4/232630513987206<10^-13 times squared norm. The four explicit terms plus one shared Hankel kernel (applied separately by parity) preserve the infinite tail up to this uniform bound. This does not assert a positive lower spectral margin for Q.

## 3. Finite truncation does not converge uniformly
For any fixed m>=1, take F_d on [0,4] equal to 1/sqrt(2d) on [0,d], and sigma/sqrt(2d) on [4-d,4], zero elsewhere, where sigma=+1 for even and -1 for odd and 0<d<1. Its norm is one and it belongs to the logarithmic domain by IV241's bounded piecewise smooth finite derivative measure argument. In the contribution from the first endpoint,
  (1/(2d)) integral_0^d integral_0^d K_m(t,u)dt du -> (1/2) integral_0^1 integral_0^1 1/(v+w)dv dw=log 2
as d->0, using d K_m(dv,dw)->1/(v+w) and the above integrable domination. The remote endpoint contribution and both cross contributions are O(d), since their summed coordinate is bounded away from zero and K_m is bounded there. Thus G_m(F_d)->log 2 in either parity. Even B_m^tail>=G_m yields ||B_m^even||>=log 2. For odd, ||B_l^odd||>=log 2/(1+exp(-4k_l)) for each l>=m; monotonicity B_m^odd>=B_l^odd and l->infinity give ||B_m^odd||>=log 2 as well. Tail forms go to zero on each fixed f, by convergence of the positive series, but NOT uniformly on the L2 unit sphere (even on the log-domain unit sphere measured in L2). This is an additional analytic method obstruction, not a claim about convergence in log-form norm or a negative direction of Q. Arbitrary boundary-count escalation does not give a uniform small additive L2 error. The aggregate lower model resolves that specific problem.

## 4. Exact inherited witness check
Use IV244's same rational even witness, exact squared norm 13.64727032, exact Q_64 lower endpoint 509558195524/10^15. By Q>=Q_64 and the aggregate bound, Q_agg,4 >= Q_64-delta||f||^2. Exact directed integer replay gives loss <=235/10^15 and aggregate lower endpoint 509558195289/10^15>0.000509558. This is a verified transfer of an existing witness, not a new eigenvalue computation or independent new sign audit. The audit function was executed twice on pinned remote JSON; the standalone Node wrapper, which adds source blob checks, was not separately run. No full positivity, fast solver, or certification bank claimed.

## 5. Next structural obligation
The remaining nonlocal boundary component is now a single explicitly bounded positive Hankel operator, not a long list of terms. It is not compact by default, and a finite-rank approximation in L2 operator norm must not be presumed. Next construct an efficient positive-semidefinite representation of the aggregate on low/high blocks (e.g. exact kernel integration or a controlled geometric partition separating the corner singularity), and seek a sharper weighted complement comparison rather than paying the IV243 uniform 20 penalty. Prior truncation STOP m<=32 remains intact for the pure finite Q_m models. The new lower model is different and has only been tested on the inherited witness. No new mathematics outside AM, no global adoption, no terminal claim. Four axes: analytical derivation and exact rational audit PASS; native Lean not attempted; durable source/report/results; scope local. Prior terminal raw remote-byte caveat unchanged. Record-only skip ci, no workflow dispatch.
