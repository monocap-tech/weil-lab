# IV259 — Correlated analytic infinite-tail correction and lifted tapered inverse majorant

## Disposition

PARTIAL. The entire even residual from mode 1536 onward has a cancellation-preserving rational-channel enclosure; the gap 1536<=j<3072 from IV258 is included. On four explicit analytic high-space functions, one with infinite support, construct a correlated actual correction in all 256 inherited retained coordinates. The rational trial's certified comparison decrement has trace >0.09; its first three bands yield a lower decrement matrix with at least three eigenvalues >0.01. These are energy gains in the inherited IV257 congruence, not physical L2 margins or the actual Schur sign. The complete post-correction residual has not been evaluated. IV256's mode-512 joint coercivity and the exact original Schur criterion remain intact. No odd execution or final positivity clearance.

Parent IV258 ae83af23d764da3083568faee8f0acf5eeccdf43, report a3390d6313815ec287c40dec4d5ff8ce5b94a3d6, prefix source eb6620e5a80137e9ee1a50a8634fe168d717f9f8 and receipt 176b6b8ed816e9034195331058e2a87d6cf86de8. IV257 original even receiver 6a2600b3aaee1cbca701098b3d01762e7e8a51c7. IV253 interval kernel b748429e9c9dff261014f9cb46f09bca9268c738; IV251 exact domain/residual identity 0c6a48160f8c06dc320c77be59ecaabc027bf2ba. IV256 proof 27e24514566b823ef0f92e7d610ae7051a84673a, checker 43bab72e8f11a5cc8698b9c7452b7cee95b46eda, parity receipts d129e96bd82e57260c1280d8f0ea76d3d1e5600b and cb5147481c6036db0fa6a8375907a3db4322e778. Frozen original source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0. No integrated proof-binary use or unrelated-lineage adoption. W02 delegated continuation and historical binary custody caveat unchanged.

## 1. Exact whole-tail representation, without expanding Galerkin support

Reconstruct the IV258 corrected even trial columns w'_i in unnormalized cosine coefficients, i=0,...,255. The low projection is unchanged. Old trial W_i has support k<768 and may have l1 as large as 2.04325e140. The added correction Z_i/10^12 has support 512<=k<1536 and l1<4.648. This distinction is essential: it permits a single Chebyshev enclosure on the entire residual interval without paying the large original coefficient norm at the near-tail convergence ratio.

Put K=1536, v=K/j in (0,1] for j>=K, q_k=(k/K)^2, A'_k the exact pole-absorbed divided-difference numerator of IV258. Then
 t_ji=Q(cos_j,w'_i) = j^-2[A'_j M_i(v)-N_i(v)],
 M_i(v)=sum_k w'_ik/(1-q_k v^2), N_i(v)=sum_k A'_k w'_ik/(1-q_k v^2).
All actual boundary and pole weights are retained in A'_k. Let D_k=sqrt(1-q_k), r_k=(1-D_k)/(1+D_k). Poisson kernel identity gives
 (1-q_k v^2)^-1 = D_k^-1[1+2 sum_{m>=1} r_k^m T_m(2v^2-1)].
For k<768, D_k>1/2 and |r_k|<1/13. For the entire even support k<=1534, D_k>1/20 and |r_k|<19/21. Exact interval guards check both facts. The latter numerical guards are specific to even support; odd support reaches 1535 and would need adjusted constants and term counts. No unchanged odd transfer is claimed.

Compute 512 signed coefficients of each channel. Directed scale S0=10^400 reconstructs W,V,F and exact scalar entries using IV258; Chebyshev feature and coefficient centers first quantized at B=10^200, and final signed channel coefficients at U=10^30. For a center dot product, radius at B^2 includes dot(|Wbar|,feature_radius)+sum(|feature_center|+feature_radius), accounting for directed rounding of W to B as in IV258. The factor 2 for m>=1 is included before quantizing to U. The signed sums are taken before absolute values. All coefficient radii and rounding errors contribute to a uniform polynomial sup error for each column. Use the separated omitted-series bound
  (13/3) 13^-512 ||W_i||_1 + 420 (19/21)^512 ||Z_i/10^12||_1
for M, and multiply by max_k |A'_k| for N. This follows from summing the geometric series using 2/D_k and 1/(1-|r_k|) separately. All coefficients at m>=299 were dropped only after checking the cumulative absolute omitted centers per column <=1e-12 for M and <=1e-9 for N, and charging them to the sup error. Thus the retained polynomial degree in the Chebyshev index is at most 298, evaluated on all v in [0,1], not just at samples.

Executed even results: 512 terms, 299 active; max pre-drop M error <1.087e-19, N error <1.974e-15; max absolute coefficient sums <67 and <9.179e6 respectively. Per-column post-drop errors and coefficient absolute sums are stored. The prefix residual trace bounds of IV258 reproduced exactly.

## 2. High numerator asymptotic with explicit uniform error

For j>=1536, write r=alpha*j, z=r^2, alpha=pi/4, f(x)=1/(4x^2+z), a=1/4. The unweighted S(z)=sum_{n>=0} f(a+n). Trapezoidal integration on each unit interval, then summation, gives
 |S(z)-integral_a^infinity f(x)dx-f(a)/2| <= (1/8) integral_a^infinity |f''(x)|dx <= 1/r^3.
Indeed the trapezoid kernel is bounded by 1/8, f' has a single negative minimum, tends to zero, and |f'|<=4/r^3. Thus its total variation <=8/r^3. The difference between integral_0^a f and a/z is bounded by 4a^3/(3z^2)=1/(48z^2); f(a)/2 differs from 1/(2z) by <=1/(8z^2). Since integral_0^infinity f=pi/(4r),
 |S(z)-pi/(4r)-1/(4z)| <= 1/r^3+7/(48r^4)<2/r^3.
For the exact S_sigma the n>=1 exponential correction contributes to z S_sigma at most sum exp(-4 kappa_n)<2401/(2400*7^5), using exp(2)>7. The pole-absorbed term is bounded by |p|/(alpha^2(1/4+z))<16/j^2, since |p|<5 and alpha>3/4. The exact literal prime sine sum b_j=sum a_n sin(j alpha log n) has |b_j|<13. Therefore
 A'_j = j(2+lambda b_j)+a0+epsilon_j,
 lambda=2/alpha<8/3, a0=1/(2alpha^2)<1,
 |epsilon_j| <= 16/j+1/1000, j>=1536.
The weaker last bound includes the unweighted asymptotic error 4/(alpha^3 j)<10/j, the exponential contribution <.001 and the pole allowance. This does not change any actual finite Q entries; it bounds the error in evaluating the exact far-channel correlation.

## 3. Actual four-band analytic trial space and correlations

Let I_b be disjoint even-index bands [K,2K), [2K,4K), [4K,8K), [8K,infinity) for b=0,1,2,3. Define h_b by unnormalized cosine coefficients h_b(j)=v^2/32 on I_b, zero elsewhere. In particular the last h_b has infinite support and belongs to D and the operator domain, by square summability with logarithmic weights. The trial supports lie entirely in H_512. Let Y_ib=Q(w'_i,h_b)=sum_{j in I_b} t_ji h_b(j) (absolute convergence). With the channel polynomial centers Mhat,Nhat and asymptotic of section 2, the correlation is enclosed by
 (1/(32K)) sum_{I_b} v^3 [2 Mhat_i(v)+lambda b_j Mhat_i(v)]
 + (1/(32K^2)) sum_{I_b} v^4 [a0 Mhat_i(v)-Nhat_i(v)]
 plus signed-coefficient and asymptotic interval error.
If delta_M,delta_N are the uniform polynomial errors and U_M the absolute coefficient sum, the extra error is bounded by
 37 delta_M/(32K) sum v^3
 + [delta_M+delta_N+(16/L_b+.001)(U_M+delta_M)]/(32K^2) sum v^4,
because |2+lambda b_j|<37, a0<1 and j>=L_b.

For finite bands compute the actual scalar sums S_qm=sum v^q T_m(2v^2-1), q=3,4, and O_3m=sum b_j v^3 T_m(2v^2-1), with directed integer centers at U. This is a complete census of 768,1536,3072 even indices respectively. The prime coefficient and base rotation intervals come from the pinned 400-digit literal bank. Stable integer rotation recurrence at U gives uniform sine-sum radius <1.770e-24, with the same norm-one rotation induction as IV254 and IV257. For the Chebyshev recurrence, use t center floor at U, T_0=1,T_1=t_center, then floor(2*t_center*T_m/U)-T_{m-1}. For true |t|<=1, inhomogeneous error propagates by second-kind Chebyshev polynomials |U_l(t)|<=l+1. Inductively centers have magnitude <=2, initial error <=1/U and one-step perturbation <=5/U, hence error <=(4m^2+1)/U (the guard 4m^2+1<U holds). Multiplication by v^q floor and final rounding gives error <=(4m^2+4)/U. Multiplication by prime center adds error bounded by [14*(4m^2+4)+2*prime_radius_scaled+1]/U. Sum these bounds over the exact finite census.

For the last infinite band v in (0,1/8], compute the nonoscillatory scalar integrals
 (K/2) integral_0^(1/8) v^(q-2) T_m(2v^2-1) dv
by exact integer polynomial recurrence T_0=1,T_1=2v^2-1 and T_{m+1}=(4v^2-2)T_m-T_{m-1}, integrating each power with directed endpoints. The discrete sum differs from the integral by at most twice the total variation <=2(1+2m)/8^q. This follows by comparing step-two left sums with the integral; parity offset is allowed by the doubled allowance. The total variation bound uses variation(T_m) <=2m on [-1,1] and monotonicity of v^q. For each prime the step-two partial sine sum is bounded by 1/|sin(alpha log n)|. Exact literal intervals give B_osc=sum a_n/|sin(alpha log n)|<52. Abel summation bounds the oscillatory scalar sum by B_osc(2+2m)/8^3; its center is zero. The final infinite band is therefore included with explicit, rather than assumed zero, oscillatory remainder. Correlation radii in that band are considerably looser than the direct finite sums.

Contract the signed coefficients with these exact scalar sum centers and their radii. Resulting 256x4 matrix Y has interval centers Y0 and radii E at U, stored in the raw receipt. Upper sums for positive v^q used in the model error are decreasing integral plus initial term, with the correct finite band end or infinity. This covers every j>=1536 in the correlation computation, not the entire post-correction residual norm.

## 4. Certified operator-valued actual correction

By IV251 the original high-block operator C_H <= diag(gamma(r_j)+32) in normalized coordinates. IV254's upper symbol bound implies gamma(r_j)+32<=40 j/K for j>=K: log(K/8)=log192<6, small rational symbol corrections are <1, and log(j/K)<=j/K-1. In unnormalized coefficients the diagonal upper is 80/v. Thus for a linear combination of the disjoint h_b,
 Q(sum_b c_b h_b) <= sum_b D_b |c_b|^2,
 D_b=(80/1024) * upper(sum_{I_b} v^3),
with exact positive rational upward bounds in the receipt. This is an upper form on the actual correction subspace, even though the actual original operator has cross-band interactions.

Define exact analytic correction z_i=sum_b Y_ib/D_b h_b and w''_i=w'_i-z_i. Then in matrix order
 F'' <= F' - G,  G=Y D^-1 Y^T >=0.
Equivalently if r'_i=H C w'_i, r''_i=r'_i-C_H z_i (C the original form operator), then
 E'' = E' - (2 sym(Y D^-1 Y^T)-Q(z)) <= E'-G,
 E'=r'^* C_H^-1 r', E''=r''^* C_H^-1 r''.
This is an actual infinite-tail trial and a lower bound on the actual inverse energy removed. It is not replacing the inverse by a diagonal penalty on the original low form. The exact analytic map is linear and keeps all inter-column correlations. Also E'>=G. The corrected low projection is unchanged. No residual action r'' is evaluated in this operation.

For an executable rational candidate use centers Y0 instead of exact Y; correction coefficients Y0_ib/D_b are exact rationals, all four functions specified explicitly. Its guaranteed comparison decrement is
 G0 + (Y-Y0)D^-1 Y0^T + Y0 D^-1(Y-Y0)^T, G0=Y0 D^-1 Y0^T.
By Young with .1, a uniform matrix lower bound is
 (9/10)G0 - 10 sum_b ||E_b||_2^2/D_b I.
The last bound may be negative outside active directions; do not claim rational trial improves every direction individually. Exact map G is PSD on all directions. Direct per-diagonal lower comparisons (Y0^2-2|Y0|E)/D give a much sharper trace lower, and corresponding plus bounds refer ONLY to the comparison decrement, not an upper bound on actual energy removed.

Results:
- Four-band rational comparison decrement trace >.0909959, exact analytic map gain trace >.0934390 (lower bounds, not physical L2 margins).
- Largest direct rational diagonal gain lower >.0091181, inherited coordinate row 206 (pivot mode 168, not a single cosine).
- Four-band uniform Young loss ~.03893193, dominated by uncertainty in final infinite band. Exact 4x4 generalized inertia test of .9 G0-loss I certifies at least one positive direction with lower gain >.001.
- First three bands alone: comparison trace lower >.0895518 and uniform loss <5.264e-11. Exact inertia certifies three independent directions of the matrix lower bound above .01. This is an operator-valued active-subspace result, not 3 selected coordinate witnesses. The exact gain matrix need not be full rank. Retaining first 3 accurate bands as rational trial is optional; the exact four-band map includes the infinite band.
- The inertia checks use the nonzero spectrum equivalence of G0 and D^-1/2 Y0^T Y0 D^-1/2. On the 3x3 or 4x4 integer Gram H=Y0_scaled^T Y0_scaled, count positive pivots of 9H-10(loss+threshold) D_scaled by exact symmetric congruence. At nonzero diagonal pivot p, update remaining block by p^2 times its Schur complement, preserving inertia. Every tested pivot nonzero. All raw operands retained.
- No negative original Schur direction obtained; the coordinate-wise conservative trial upper after subtracting lower gain is never negative in this receipt. No positive joint corrected trial margin inferred either (IV258's previous positivity issue remains). These gains do not suffice for full sign clearance.

## 5. Lift IV256 to a sharper operator-valued inverse upper bound

Use normalized coordinates on H_512 and a DIFFERENT split I=512<=j<28672, T=j>=28672, as in IV256 (independent of the four correction bands). Write C_H for the exact original high form, eta=1/1000, W the IV256 taper, B=P_TI W_I, d_j=1/5+log(j/28672), D_T=diag(d_j). IV256 proves
 Q_H(v+h) >= eta(||v||^2+||h||^2)+v^* A v - 2 Re <h,Bv> + <h,D_T h>,
 and A-B^*D_T^-1 B >= s I, s>7/1000 in both parities.
Complete the square and drop only the positive eta||h||^2:
 Q_H(v+h) >= (eta+s)||v||^2 + ||D_T^1/2 h-D_T^-1/2 Bv||^2.
The exact finite residual factor in IV256 actually proves the stronger lower receiver A-B^*D_T^-1B >= K_fac K_fac^T/2^46+s_sigma I (K_fac integer factor, s_sigma the exact recorded surplus). This follows from the certified target equality up to symmetric row residual and directed entry error, retaining the positive factor rather than dropping it. The factor is regenerated by IV256's pinned checker, not reconstructed or rerun here. Use either L_I=(eta+s)I, or the stronger L_I=K_fac K_fac^T/2^46+(eta+s_sigma)I. In both cases L_I>=.008 I. For an arbitrary normalized residual r=(r_I,r_T), square completion/variational duality of positive forms gives
 <r,C_H^-1 r> <= ||D_T^-1/2 r_T||^2
    + <r_I+B^*D_T^-1 r_T, L_I^-1 (r_I+B^*D_T^-1 r_T)>.
To see this, substitute y=D_T^1/2 h-D_T^-1/2 Bv into the supremum of 2Re<r,v+h>-Q_H(v+h), optimize separately in y and v. The change of variables is valid on the form domain since d_j grows logarithmically and B bounded. This is a signed mixed-operator majorant, valid on all H_512, not the old disproved diagonal-only inverse receiver. Even using the scalar L_I floor the inverse factor on the mixed low argument is 125 rather than 1000; on residuals with r_T=0 it is an eightfold improvement. The stronger factorized L_I retains the IV256 finite-block geometry. Independent exact check of both s_sigma>7/1000 executed using pinned receipts. The bound applies in Loewner order to a full residual matrix by linearity. It has not been evaluated on r'' here, nor claimed sharp enough yet.

## 6. Exclusive remaining gate and custody

IV259 closes the gap in analytic residual channel coverage and constructs a genuine correlated tail trial without enlarging Galerkin support. The tail correction is relatively modest, and the remaining residual action of the original high operator on these functions and the correlated energy upper bound still need evaluation; four smooth channels alone are not established sufficient. The next gate should compute the action of the original high block on the analytic residual/correction channels and use the lifted factorized inverse majorant, not repeat finite cutoff enlargement or return to scalar trace penalties. The full 512-dimensional actual Schur positivity remains open. No odd run; its ratio guards require adjustment. No native Lean, no new principal gate clearance, no Phase IV adoption or RH conclusion.

Executed even computation in connector V8 ~235.33s, exact BigInt directed arithmetic apart from inherited IV258 floating candidate selection with exact residual checks. The source and raw output include the interval model, all 256x4 correlations and the rational correction recipe; large regenerable coefficient tables are not separately stored. Independent receipt audit checked exact reproduction of IV258 prefix, both comparison traces, uniform loss, exact-map lower trace and small-matrix inertia. Standalone Node wrappers not separately executed. No execution interruption or repository write failure asserted. Record-only skip ci, no workflow dispatch, no main merge or local custody transition.
