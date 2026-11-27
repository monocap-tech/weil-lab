# IV240 — Physical logarithmic regularity and AM finite-rank receiver

## Scope and immutable inputs
Delegated W02 continuation, canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c. Parent IV239 56a9a1c99ef67606d9ae1159249c198743bac9e7; analytical proof research/IV239-AM-translation-coercivity.md blob 6530c344ee6e932ac02921b6905c4bdacb4b1ca2 and exact mode inventory research/iv239_am_circle_modes.json blob d2ce58d28af3a8ffdcc684cf89cebbef70e3cb25. Frozen cell data custody/iv146-am/am_cells.json blob ba15f7c820fe5fd0a1a3ffb61f80554ef0659cb0, SHA256 2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a. Original source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0, in particular ActualZetaIV152AMPhysicalEnvelope.lean blob d27bf0b67f80fb8797a948ce2928f5a3f39edcf5 with signed log floors; inherited IV238/239 source contracts unchanged. New claim tier analytic proof and exact rational constants; no native compilation or adoption of other lineages. No consumption of integrated terminal proof binaries.

## Setup
Translate the original window by +2 to J=[0,4), f zero outside J almost everywhere. w=H/10^8, g=f/w on J. E=E_-(f) is the invariant original weighted prime difference energy of IV238. Let a=log 2; p(t)=g(t) for 0<=t<a, periodically extended as p_per. Fourier circle coefficients c_k=(1/a) integral_0^a p(t) exp(-2*pi*i*k*t/a) dt. Use unitary angular-frequency Fourier transform on R, fhat(xi)=(2*pi)^(-1/2) integral f(x) exp(-i*xi*x) dx; define L(f)=integral log(1+xi^2)|fhat(xi)|^2 dxi. Assume finite L (in particular supported Schwartz). This is a proposed receiver seminorm, not a claimed estimate for original Gamma or pole forms.

## Exact base multiplier inventory
v=1/w on [0,a). Signed floors 2839=floor(4096a) and -2840=floor(-4096a) imply the endpoint is strictly inside cell 2839. Cells 0..2839 occur. Exact ceil-rounded rational audit gives sup(v)=20000000/11760829<1.71; sum of internal jump magnitudes <=3803434369/10^9; seam budget v(0+)+v(a-)<=2494956868/10^9; combined budget <=6298391237/10^9<6.3. Rounding is upward separately for each jump and seam value, using integer division; no floating decisions. This audit does not claim that the reciprocal multiplier is Sobolev smooth.

## Physical cutoff and periodic tail
For R>0, split f into f_lo and f_hi by Fourier indicators |xi|<=R and |xi|>R. Then ||f_hi||_2<=sqrt(L(f)/log(1+R^2)). Plancherel yields ||f_lo'||_2<=R||f||_2 and Cauchy on the band gives ||f_lo||_infty<=sqrt(R/pi)||f||_2. These low and high components need not be supported in J; they are restricted to the base interval only. Write p_lo=v f_lo and p_hi=v f_hi there, both periodically interpreted in L2. Let T_K be the orthogonal projection onto |k|>K, K positive integer. Then ||T_K p_hi||_{L2(0,a)}<=1.71 sqrt(L/log(1+R^2)).

The periodic distributional derivative of p_lo is d(t)dt + sum_l J_l delta_{t_l}, where d=v f_lo' inside cells, internal jumps J_l=(v_+-v_-)f_lo(t_l), and seam J_0=v(0+) f_lo(0)-v(a-) f_lo(a). The derivative density has L2 norm <=1.71 R||f||_2; total absolute jump mass <=6.3 sqrt(R/pi)||f||_2. Integrating by parts separately in each cell gives for nonzero k:
  c_k(p_lo) = a/(2*pi*i*k) c_k(d) + (1/(2*pi*i*k)) sum_l J_l exp(-2*pi*i*k*t_l/a).
Use Parseval for the first term and sum_{|k|>K} k^(-2)<=2/K for the second, followed by triangle in l2 with circle normalization. Therefore
  ||T_K p_lo||_2 <= [a*1.71*R/(2*pi*K) + 6.3*sqrt(a*R/(2*pi^3*K))]||f||_2
  <= A(R,K)||f||_2,
where A(R,K)=(399/2000)R/K + sqrt((1029/2000)R/K), using a<0.7 and pi>3. The full tail bound is
  ||T_K p||_2 <= A(R,K)||f||_2 + 1.71 sqrt(L/log(1+R^2)).
The seam term is necessary; there is no assumption of periodic matching of the physical function or smoothness of p. No new regularity assertion for g or p.

## Finite-rank physical receiver
Let F_K be the span in L2(J) of w(x)exp(2*pi*i*k*x/a), |k|<=K, extended by zero outside. Dimension 2K+1: w>0 on base interval, and circle exponentials independent there. For any periodic base function q, ||q_per||_{L2(J)}<=sqrt(6)||q||_{L2(0,a)} from at most six residue points. IV239 gives ||g-p_per||<=sqrt(15/(m^2 a_2))*sqrt(E)<15 sqrt(E), where m=617177/1562500, a_2>9/20. Since w<=1, approximating f by w times the low circle Fourier sum yields
  dist(f,F_K) <= 15 sqrt(E) + sqrt(6) A(R,K)||f|| + sqrt(6)*1.71 sqrt(L/log(1+R^2)).
This is a tunable finite-dimensional reduction: choose R to control the physical high-frequency tail, then K to control the finite jump and derivative terms. The bound does not require the finite-band arithmetic coefficient and hence is valid at every positive K.

## Explicit quotient estimate
IV239 at K=128 has beta=15950242753998675277085766/12070601072560968206298828125, so E>=beta*a*sum_{0<|k|<=128}|c_k|^2. Approximating by c_0 w instead, applying the triangle inequality and the six-chain multiplicity, gives
  dist(f,span(w)) <= [15+sqrt(6/beta)]sqrt(E) + sqrt(6) A(R,128)||f|| + sqrt(6)*1.71 sqrt(L/log(1+R^2)).
No addition of two full-strength energy lower bounds occurs; this is a sum of upper bounds on separate norm errors using the same energy.
For R=4, exact rational checks show sqrt(6/beta)<68, sqrt(6)A(4,128)<1/3 (sqrt(6)<49/20 and sqrt(1029/64000)<127/1000), and sqrt(6)*1.71/sqrt(log(17))<3 (log17>2, e<3). Thus
  dist(f,span(w)) <= 83 sqrt(E) + 3 sqrt(L) + (1/3)||f||.
For f orthogonal to w, dist=||f|| and
  (2/3)||f|| <= 83 sqrt(E)+3 sqrt(L).
In particular E+L >= [4/(9*(83^2+3^2))]||f||^2 = (2/31041)||f||^2 on w-perp by Cauchy. This very conservative combined bound is not asserted to dominate any actual deficit in the original non-prime form. L itself can supply coercivity on a supported window; this estimate's structural value is the explicit physical-to-base tail transfer, not the small scalar constant. IV239's no-gap obstruction for E alone is unchanged.

## Disposition and next
The proposed regularity receiver operates directly on physical f and controls the discontinuous weight without assuming H^1 or H^(1/2) regularity of g. The finite-rank approximation is in supported L2; the basis w times periodic modes is generally not Schwartz, and one must not directly evaluate an unextended original non-prime form on it. Next choose a mathematically legitimate Schwartz-compatible finite-rank comparison or form-domain extension and identify exact non-prime control contract (including its sign and angular-frequency convention); do not claim Gamma/pole domination or cross-lineage adoption. Quantitative constants are conservative; no actual structural Weil positivity claim. Exact arithmetic audit function executed on remote frozen inputs in connector JS runtime; standalone committed Node wrapper adds input digest checks and was not separately executed. Four axes: analytical proof, exact replay PASS, no new Lean, durable text/source/result custody; no global adoption. Previous terminal raw-byte readback limitation unchanged. Record-only commit uses skip ci on existing custody branch; no workflow activation.
