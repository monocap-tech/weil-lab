# NF524 — Original endpoint logarithm: full actual two-source divisor graph

**2026-11-15 PT. Analytic source-graph membership and graph-Cauchy theorem, checked against original NF494 400-jet source and existing unconditional multiplicity count. Exact-Fraction primary and independent original-source reverse-Horner LOCAL PASS. No new Lean build, no CI acceptance or main merge.** Stacked on NF523 draft PR #552.

## Exact original source, not synthetic data

Keep the same source-built NF498/NF523 physical vector on B=11/10, delta=1/500:

\[
\ell_U(x)=\operatorname{sgn}(x)\mathbf1_{B-\delta<|x|<B}
\,\frac{U(|x|)}2\log\frac{B}{B-|x|}.
\]

Original NF494 H400/U400 source SHA256:
39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181.
Original NF407 and NF406 source SHA256, unchanged:
0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce
and c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675.

NF523 certified actual original U(B)<-1e-11, and for c(d)=U(B-d)/2 on 0<d<delta:
|c(d)|<=M0=2e-7; |c'(d)|<=M1=7e-4.
NF524 independently recomputes U and U' envelopes from ALL 400 original source coefficient intervals and the actual Cauchy tail plus differentiated tail. NF523 already established ell_U is in H^(1/4) and natural Fourier multiplier operator domain, though not H^(1/2).

## NEW uniform Fourier-window source envelope on the entire actual zeta strip

Let F_f(z)=integral_(-B)^B f(x) exp(i z x) dx and t=|Re z|. For ANY |Im z|<=1/2 (no RH):
\[
\boxed{|F_{\ell_U}(z)|\le10^{-4}\,\frac{1+\log(2+t)}{1+t}.}
\]

Proof: on the positive collar put x=B-d and L(d)=log(B/d). The negative collar has the same absolute bound by odd reflection. For |Im z|<=1/2, all exponentials cost at most exp((B+delta)/2)<2, proven by exact rational exp(x)<=1+x/(1-x/2) at x=551/1000.

For t<=500, direct integration gives total bound
4 M0 delta [log(B/delta)+1]<4M0 delta*8=1.28e-8<1e-4/501.
For t>=500, split at d*=1/t; directly integrate 0<d<d* and integrate by parts on d*<=d<=delta. Paying both endpoint terms and the actual derivative c'(d)log(B/d)-c(d)/d gives
\[
|F_{\ell_U}(z)|\le\frac4t
\{M0[3\log(Bt)+\log550+1]+M1\,\delta[\log550+1]\}.
\]
Use log550<7, log(Bt)<=log(t+2)+1 and (1+t)/t<=501/500. Exact Fraction verifies separately:
4*(501/500)*3*M0=2.4048e-6<1e-4 (log coefficient),
4*(501/500)*(11*M0+8*M1*delta)=5.37072e-5<1e-4 (constant).
This proves the uniform bound for ALL original possible nontrivial zeros, including off-critical zeros.

## Existing actual zeta divisor count settles BOTH infinite source coordinate norms

The unchanged Lean theorem neutralActualZetaDivisorDyadicBand_card_bound from WeilDefect/Arithmetic/ActualZetaDyadicSummability.lean gives a finite constant A>0 with each genuine multiplicity-preserving divisor band
D_n={q: 2^n <= 1+|Im rho_q|<2^(n+1)}
having cardinality <=A(n+2)2^n. Actual zeta ordinate z_q=-i(rho_q-1/2) has Re z_q=Im rho_q and |Im z_q|=|1/2-Re rho_q|<1/2 unconditionally by ActualZetaZeroCoordinates.lean.

In the exact original two-source graph, for every multiplicity copy q:
\[
a_\pm(f;q)=\frac{F_f(z_q)\pm F_f(\bar z_q)}{\sqrt2}.
\]
Within D_n, the Fourier estimate implies |F(z_q)|<=2C(n+2)/2^n, C=1e-4. Paying the actual pair normalization and actual multiplicity-count bound:
\[
\boxed{\sum_{q\in D_n}(|a_+(\ell_U;q)|^2+|a_-(\ell_U;q)|^2)
 \le16 A C^2\frac{(n+2)^3}{2^n}.}
\]
The exact rational tail is:
\[
\sum_{n=N}^\infty\frac{(n+2)^3}{2^n}
=\frac{2(N+2)^3+6(N+2)^2+18(N+2)+26}{2^N}.
\]
Thus BOTH original actual-divisor source coefficient sequences are ℓ², with every genuine integer multiplicity retained. Since NF523 already proved ell_U lies in the physical logarithmic Hilbert carrier, **ell_U genuinely belongs to the complete two-source graph** neutralActualZetaSourceGraph B and its equivalent Hilbert graph. The constant A is existential from Lean; no numerical value or zero list is invented.

## NEW original full source graph Cauchy convergence with EXACT 242 selected moments

Use the exact NF523 smooth approximation: for 1/2<=s<1 approaching1, dilate f_s(x)=ell_U(x/s), then convolve with an even nonnegative unit-mass compact mollifier η_eps supported within eps<min(delta,B(1-s)). This produces odd strict-interior smooth g_s, converging to ell_U in H^(1/4) and multiplier graph norm.

For every entire complex z, the *actual* window-transform product holds:
F_g(z)=s F_ell_U(sz) F_η(z). Since s(1+t)/(1+st)<=1, log(2+st)<=log(2+t), and |F_η(z)|<=exp(eps/2)<2 throughout the actual zero strip, all g_s obey the same original Fourier bound with constant 2C. Hence differences g_s-ell_U have **uniform** bound with 3C, and for any N their TWO-source ℓ² dyadic tail is bounded by
\[
16A(3C)^2\,
\frac{2(N+2)^3+6(N+2)^2+18(N+2)+26}{2^N},
\]
uniformly in s and mollifier. Finite height bands contain finitely many actual divisor copies. Since g_s->ell_U in compactly supported L², each fixed complex sample converges. The finite-band convergence plus this uniform decaying tail prove convergence of BOTH actual positive and negative divisor ℓ² vectors.

For exact preservation of all original 242 physical selected moments, use NF523's fixed even positive smooth compact bump χ and authentic 242 odd analytic selected generators j_i. Their weighted Gram M_ij=integral χ j_i j_j is strictly positive definite by analytic independence. Let h_j=χ j_j and correct with c_s=M^-1(<j_i,ell_U-g_s>)_i:
\[
\phi_s=g_s+\sum_{j=0}^{241}(c_s)_j h_j.
\]
Then exactly <j_i,phi_s>=<j_i,ell_U> for ALL 242 original directions; coefficients c_s->0. Each fixed compact smooth h_j has complex-strip window decay O((1+t)^-2), by two integrations by parts, and its two actual source vectors lie in ℓ² by the existing Lean theorem neutralActualZetaDivisorQuarticWeight_summable. Therefore corrections tend to zero in BOTH source coordinates. Physical H^(1/4) convergence was already proved in NF523. Hence
\[
\boxed{\|\phi_s-\ell_U\|_{\rm actual\ full\ two-source\ graph}\to0,
\quad \forall i<242:\ <j_i,\phi_s>=<j_i,\ell_U>.}
\]
This is a full actual divisor graph Cauchy theorem for precisely the original endpoint vector, not for every arbitrary physical L² vector.

## STRICT NO TRANSFER

The FULL actual two-source graph is not known to equal the closed Green-packet lift subspace. Existing Lean ActualZetaGreenPacketDensity.lean proves finite Green packet density only IN THAT CLOSED SUBSPACE and its orthogonal packet criterion, NOT density in the full source graph. NF524 does NOT prove the new ell_U graph lift lies in Green-closed-span. The actual Hilbert source signed quadratic/form equality with the physical Weil multiplier is established on specified source images/Green closed subspaces only; graph membership and finite moment preservation alone do not identify that full same-source signed form.

So original finite-selected physical NF522 three named NF404 NO-GOs remain finite-only. Original Green-span membership, complete prime/pole/arch same-source signed diagonal, Weil multiplier image and graph-domain attachment, W_ODD_NEG, full even/odd Weil positivity and RH all OPEN. No numerical zero enumeration or new Lean compilation. Source constant and dyadic exact Fraction tests PASS locally; mathematical graph statements are analytic proofs using those verified premises and existing proved divisor-count theorems.

**NF525:** Test Green-closed-span membership for this explicit source graph vector by the existing packet-orthogonality/observability criterion; in parallel identify the complete authentic Weil multiplier/source signed diagonal on its moment-preserving graph-convergent smooth approximants. Neither is implied by NF524.
