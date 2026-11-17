# NF577 — recovered original U400, quantitative strip envelope and collar seed limit

Stacked on NF575 PR #607; NF576 was an uncommitted analytic derivation. This is a source-exact local arithmetic replay plus an analytic proof candidate, not a Lean acceptance. No full signed Weil/coercivity or RH claim.

## Original source custody and regularity

Retrieved genuine NF494 native Actions artifact 13781650172 (run 42850200418, PR #522). The raw JSON SHA256 is 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181, matching NF523 and NF575. All 400 outward U coefficients were consumed as exact rational intervals. Original NF407 source and NF406 seam hashes match the frozen receipts. No midpoint Taylor polynomial is substituted.

The actual source is the finite real oscillator sum plus the genuine sinh pole (NF493 PR #521 native script; NF415 native_source and U.at):
U(x)=p sinh(x/2)+sum_(f,k) q_(f,k) x^k S_k(2 pi f x), with S_k=sin for even k, cos for odd k.
The grouped modes come from the original 242 selected and four critical generators, with all 273 oscillator groups and original coefficient uncertainty retained. Every real choice of the original coefficient vector defines an entire function, so C1 regularity is elementary; the numeric intervals are enclosures for the true source coefficients, not a definition of a new U. The exact choice and provenance linking Lean's U to the original frozen source remains to be represented in Lean.

For the true Taylor coefficients u_k of U(B-d), |u_k| <= a_k=max(abs(lo_k),abs(hi_k)) for k<400. With B=11/10, delta=1/500, R=1/25, q=delta/R=1/20, use the inherited NF492/493/494 Cauchy majorant CM=10^400 on |d|=R. The two tail fees are CM*q^400/(1-q) and CM/R*q^399*(400/(1-q)+q/(1-q)^2). Exact Fraction recomputation from recovered raw bytes gives
- M0=sum a_k delta^k + tail0 = approximately 1.9659655557684862e-7 < 2e-7;
- M1=sum k a_k delta^(k-1) + tail1 = approximately 6.957098822919963e-4 < 7e-4;
- U(B) has strict upper bound -1e-11 (outward upper approximately -1.16798644909683e-11);
- tail0 approximately 4.076412541946651e-121; tail1 approximately 8.153897824035919e-116.
These are arithmetic conclusions under the inherited source and holomorphic majorant certificate, not a new Arb computation. Companion replay script accepts the actual zip or raw JSON. Its arithmetic gates were independently reproduced locally.

## Quantitative one-collar strip bound

For positive exponent convention H(z)=int h_U(x) exp(i z x) dx with h_U(x)=1_(B-delta,B) U(x)/2 log(B/(B-x)), put z=t+iy, |y|<=1/2, T=|t|, A_y(d)=U(B-d) exp(-y(B-d))/2. The phase exp(itB) is unimodular. Since e^(B/2)<2, |A|<=c0=2e-7, |A'|<=c1=7e-4+c0/2. For T>=500 split at a=1/T. The initial integral has absolute value <=c0*(log(BT)+1)/T. Integrate by parts on [a,delta]; the two boundaries and derivative of log contribute <=c0*(log(BT)+log(B/delta)+log(delta*T))/T =2*c0*log(BT)/T. The amplitude derivative contributes <=c1*delta*(1+log(B/delta))/T. Thus
|H(z)| <= [c0*(3 log(BT)+1)+c1*delta*(1+log(B/delta))]/T.
For T<=500 use |H(z)|<=c0*delta*(1+log(B/delta)).
Since log(550)<7 (e>2.7 and 2.7^7>550), log(BT)<=1+log(2+T), and 1/T<=(1+delta)/(1+T) in the high band, both bands imply
|H(z)| <= (1/40000)*E(t), E(t)=(1+log(2+|t|))/(1+|t|).
The exact sufficient comparisons are (7*c0+8*delta*c1)*(1+delta)<1/40000 and 8*delta*c0*(1+1/delta)<1/40000; replayed rationally. The bound also holds for negative exponent convention since the strip is symmetric. For ell_U=h_U-h_U(-x), |F_ell(z)|<=E(t)/20000.

## Constructive full graph sequence

As in authentic NF528, c=B-delta/2, s_n=1-1/(2(n+1)), epsilon_n=(1-s_n)*delta/4. Compress h_U inward by h_s(x)=h_U(c+(x-c)/s); convolve with an even nonnegative smooth unit-mass mollifier supported in [-epsilon,epsilon]; reflect oddly to obtain g_n. Exact support margin is (1-s)*delta/4 at each endpoint of each collar. These are real odd strict-collar smooth functions. Strong continuity of translations/dilations in L2 and the approximate identity give convergence: ||rho_eps*h_s-h||2<=||h_s-h||2+||rho_eps*h-h||2 ->0, then reflection doubles the bound. This argument requires neither H1 nor fractional Sobolev approximation.

H_s(z)=s exp(i z(1-s)c)H(sz). Mollifier transform <=exp(epsilon/2). With s>=1/2 the combined exponential factor <=exp((c+delta/4)/4)<2; s E(st)<=E(t). The reflected seed therefore satisfies the same common bound
|F_ell(z)|, |F_gn(z)| <= E(t)/10000.
All formulas concern the actual original collars and full zero strip, not a real-axis-only estimate. Thus the two quantitative analytic hypotheses of NF575 have a source-specific proof (subject to inherited source certificate). NF574/NF575 still need Lean acceptance; formal seed construction and the U identity are not implemented in this commit. Once those are available, NF573 can transport the exact original 242 selected moments assuming its finite Gram/correction premises. No claim of global source density or whole Weil sign.

## Standing

Local exact arithmetic PASS. Mathematical Fourier and approximation proofs supplied; no new Lean code, no new CI invocation intentionally, no main merge. NF575 focused compiler run was in progress at last inspection. Next prioritize formalizing the endpoint Fourier split and affine convolution transport, and exact identity from original NF407 finite oscillator family to Lean U, retaining coefficient uncertainty. Full physical/cofinite Weil coercivity and RH remain open.
