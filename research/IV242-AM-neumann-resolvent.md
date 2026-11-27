# IV242 — Original AM Neumann-resolvent comparison and boundary correction

## Scope and pins
Delegated W02 amendment canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c. Parent IV241 5d3e53bf1c3b30a35de74201f735b2cafd7e0114, report blob 75e843ad71d4005dd9f44282e1fa9e41d02f1188; inherited IV238 original prime energy, IV241 signed arithmetic form and domain. Original source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0, ActualZetaOriginalCollarGammaLower.lean blob fbdcffbaa30f0abcf134ed7c515ffc0fbe4e2c07, neutralNF599Gain, neutralNF599GammaGainSeries and neutralNF599GammaZero_lower; ActualZetaIV071GammaFinitePrelude.lean blob d472080290f2da95575f28df1e17050eb6bfbc19, rational resolvent and full finite limit. No new native proof or consumption of integrated terminal binaries. This is an AM-local analytical comparison for its own original prime bound, not an adoption or reassignment of AP/IV106 or a claim of novelty across all project lineages.

## 1. Neumann bracketing of every original gain
Let I=[-2,2], b=2, D the supported logarithmic domain from IV241. On L2(I) let L_N be the nonnegative Neumann Laplacian (form domain H^1(I), energy integral |u'|^2). Let R_N(k)=(L_N+k^2)^(-1) for k>0, and R_0(k) the full-line resolvent compressed to I by zero extension and restriction. For f in L2(I), the variational identity
  <f,R_0(k)f>=sup_{u in H^1(R)} [2 Re<f,u|I>-integral_R(|u'|^2+k^2|u|^2)]
  <=sup_{v in H^1(I)} [2 Re<f,v>-integral_I(|v'|^2+k^2|v|^2)]
  =<f,R_N(k)f>
holds because restriction discards a nonnegative exterior energy. Inner products on each Hilbert space use the same convention; the real variational expression does not depend on convention.

The literal gain for a=n+1/4 is G_r(a)=1/a-4a/(4a^2+r^2). With k=2a its compressed full-line diagonal form is (1/a)||f||^2-2k<f,R_0(k)f>. This dominates the Neumann form (1/a)||f||^2-2k<f,R_N(k)f>. Both are nonnegative (resolvent norm <=1/k^2).

The Neumann eigenbasis is e_0=1/2, e_j=(1/sqrt(2))cos(j*pi*(x+2)/4) for j>=1, eigenfrequencies r_j=j*pi/4. Write f_j=<e_j,f>. Summing every gain by monotone convergence on both Fourier and Neumann spectral sides, adding gamma0||f||^2, gives
  A(f)>=A_N(f)=sum_{j>=0} gamma(r_j)|f_j|^2.
This simultaneously proves that A_N is finite on D; no unsupported exchange of a conditionally convergent series. The monotonicity of gamma in |r| follows directly from every nonnegative gain. No Neumann boundary condition is imposed on f itself.

Thus Q(f)>=A_N(f)-P(f)+Pi(f), or by IV238 exactly retained on its original signed prime term,
  Q(f)>=A_N(f)+E(f)+Pi(f)-integral_I V_H|f|^2
       >=A_N(f)+E(f)+Pi(f)-integral_I r_cell|f|^2.
These are lower models, not equivalence of their positivity with Q positivity.

## 2. Exact boundary-defect identity
For each k>0, u_0=R_0(k)f has kernel exp(-k|x-y|)/(2k) on I; it solves (-d^2+k^2)u_0=f and the exterior-decay Robin conditions u_0'(b)=-k u_0(b), u_0'(-b)=k u_0(-b). This follows from the full-line Fourier multiplier (or direct differentiation of the kernel); no regularity of f beyond L2 is needed, as the solutions are H^2 on I. Put u_N=R_N(k)f, whose derivatives vanish at both endpoints. The difference solves the homogeneous equation, so it is A cosh(kx)+B sinh(kx). Matching the two derivatives gives A=(u_0(b)+u_0(-b))/(2 sinh(kb)), B=(u_0(b)-u_0(-b))/(2 cosh(kb)). Substituting the full-line kernel values gives
  <f,(R_N(k)-R_0(k))f>
   = e^(-kb)/(2k sinh(kb)) |int_I f(x)cosh(kx) dx|^2
     + e^(-kb)/(2k cosh(kb)) |int_I f(x)sinh(kx) dx|^2.
Thus the exact boundary error at each gain is positive and rank at most two. Set k_n=2n+1/2. Multiplying by 2k_n and summing the nonnegative terms, IV241's original arch form is exactly
  A(f)=A_N(f)+sum_{n>=0} [ e^(-2k_n)/sinh(2k_n) |int_I f cosh(k_n x)|^2
                                   + e^(-2k_n)/cosh(2k_n) |int_I f sinh(k_n x)|^2 ].
Both sides finite on D by the gain comparison and monotone limits, so the boundary sum is convergent there. The equality is analytical, not new Lean-certified. The original signed pole is 2|int f cosh(x/2)|^2-2|int f sinh(x/2)|^2. Combining with n=0 boundary correction changes the even coefficient to 2+e^(-1)/sinh(1) and odd coefficient to -2+e^(-1)/cosh(1). The odd coefficient remains negative; neither pole positivity nor cancellation is claimed. Higher boundary terms are favorable. This exact source-preserving correction can be retained as needed instead of discarding all boundary information.

## 3. Explicit coercive-complement dimension
Let F=span(e_j: 0<=j<32768)+span(sinh(x/2) restricted to I), all zero-extended functions. Each belongs to D by the bounded piecewise smooth / finite derivative measure argument in IV241. Dimension <=32769, compared to prior <=33554433. If f in D intersect F-perp, Pi(f)>=0 and f_j=0 for j<32768. Since pi>3, r_j>=24576 for all retained j. Use actual gamma0> -28/5 and monotonicity.

For r=24576, retain first 64 gains (n=0..63) and lower-bound the remaining decreasing sum by its integral from 64+1/4. This gives
  gamma(24576)> -28/5 + sum_{n=0}^{63} (12288)^2/[(n+1/4)((n+1/4)^2+12288^2)]
                        + (1/2) log(1+(12288/(64+1/4))^2).
The attached exact BigInt script floors each positive rational gain at 10^-9. It normalizes the positive log argument by a power 2^15 into [1,2), and uses the first 12 nonnegative terms of log x=2 sum_{k>=0} ((x-1)/(x+1))^(2k+1)/(2k+1), with every term floored to 10^-9, both for log 2 and normalized log. The results are prefix >=8.382419477, half log tail >=5.253610373, gamma(24576)>8.036029850. These are exact rational lower bounds, not floating estimates. With original C=7.979648 from IV238, margin >0.056381850>1/20. Hence
  Q(f)>=(1/20)||f||^2 on D intersect F-perp.
IV241's combination with the global log lower bound promotes this to D-norm coercivity, so its exact finite Schur criterion applies with this smaller F. This witness is about 1024-fold smaller, but still too large to blindly certify densely. Parity decomposition halves each respective sector's number of low modes (16384 even and 16384 odd, plus the one odd pole direction); the full form is parity invariant since Gamma is even, prime translations occur in signed pairs, and pole eigenvectors have definite parity. No full matrix or finite certification bank was generated. This does not show the Schur form is positive.

## 4. Next structural obligation
The Neumann lower model is diagonal for Gamma and preserves exact arithmetic translations plus explicit favorable boundary corrections. Investigate an AM-specific sparse or low-rank finite receiver for that lower model (or a sharper weighted prime comparison) before any large bank. A positive lower model suffices for Q; a negative lower model does not imply Q negative. Need not reproduce other lineages' full complementary-coercivity or parity transport. The true Q finite Schur inverse remains uncomputed. A mere finite compression is insufficient. The remaining actual domination / positivity obligation is open.

Four axes: analytical comparison and exact boundary identity derived; rational margin audit executed in JS with exact BigInt (standalone Node wrapper not separately executed); new native Lean not attempted; report, script and output committed in existing custody branch, no global adoption. Existing terminal raw remote-byte readback caveat unchanged; not a dependency of this operation. Record-only skip ci; no workflow dispatch.
