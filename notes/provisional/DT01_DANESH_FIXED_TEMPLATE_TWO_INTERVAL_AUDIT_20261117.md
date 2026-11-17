# DT01 — Danesh two-interval criterion: independent audit and fixed-template reduction

Date: 2026-11-17. Separate Phase IV exploration; no dependency on, or modification of, the current NF original-Weil-carrier (OWC) stack. Analytic research note, not Lean acceptance, RH proof, or a priority claim.

## External input and lineage

Payam Danesh, *A quantitative two-interval criterion for the Riemann hypothesis*, arXiv:2611.10726v1 (2026-11-07), https://arxiv.org/html/2611.10726v1. First confirmed direct reading in this side pass; a bounded archive search found earlier Weil-Lab cross-collar coupling, aperture, full signed Schur/Birman–Schwinger and pole work (including October 9–16 and NF387–391), but no prior discussion explicitly identifying this paper or its shrinking-support/translation Laplace-pole theorem. This is not exhaustive. Compare Suzuki, arXiv:2206.03682 and 2606.09096, before any priority claim.

## 1. Source and normalization audit

Use centered actual zeros z_rho=rho-1/2 with all multiplicities, H_f(z)=integral f(x)exp(zx)dx, B(f,g)=sum H_f(z_rho)overline(H_g(-overline(z_rho))), Q(f)=B(f,f), linear in first argument. For our Fourier convention F_f(v)=integral f(x)exp(ivx)dx, put v_rho=-i z_rho. Then H_f(z_rho)=F_f(v_rho) and H_g(-overline(z_rho))=F_g(overline(v_rho)). This matches the raw mixed sample product after ordering the arguments; the precise existing P/N graph inner-product constants and native explicit-formula bridge must be checked separately before claiming Lean/OWC interoperability. Same translations preserve B on the zero side without RH.

Danesh's short-support lower bound for a single support of diameter d<log 2 is q(d)||f||_2^2, with q(d)=(1/2)log(e+pi/(2d))-C0-2d exp(d/2). No prime terms, gamma lower bound log(e+|y|)-C0, half the Plancherel mass at |y|>=pi/(2d), absolute pole charge. Thus q(d)>0 for sufficiently small d. The proof checks at these steps.

Theorem 4 asserts the eventual bound R=|B(f,g)|/sqrt(Q(f)Q(g))<=1 for all real tests in [0,w(L)] and [L-w(L),L] is equivalent to RH when w is nonincreasing, w->0 and log(1/w)=o(L). In the converse, partitioning a fixed smooth test into O(m) pieces of size O(1/m), m~1/w(t+O(1)), gives O(m log m exp(eta t)) for the translated correlation under a hypothesized bound R<=exp(eta L). The zero count and two integrations by parts supply O(log m/m) for each diagonal. The subexponential partition cost is essential. The final Laplace argument is checked below. No obvious circular use of RH found in this first proof audit. This is not an exhaustive external verification or formalization.

## 2. New candidate reduction: just ONE fixed template at dyadic scales

Fix any real even b in C_c^infty((-1/2,1/2)) of integral 1 (a nonnegative normalized standard bump is fine). Write b_d(x)=d^-1 b(x/d) and C_d(r)=B(tau_r b_d,b_d), where tau_r b_d(x)=b_d(x-r). For all sufficiently small d, Q(b_d)>0 by the short-support lemma. Let w meet the assumptions above, and use only d=2^-n, n>=1, with d<=w(L), L=r+d. The pair can be translated simultaneously into the original intervals: its containing intervals are [0,d] and [L-d,L]. There is no change in B or Q.

**Candidate theorem (analytic argument below):** RH is equivalent to the eventual bound
    |C_d(L-d)| <= Q(b_d)
for ALL sufficiently large real L and ALL dyadic d<=w(L). The two tests are identical translates, not independent functions. In fact, if Theta=sup_rho Re(z_rho)>0, then for each 0<=eta<Theta and every L0, there exist L>L0 and an allowed dyadic d with |C_d(L-d)| > exp(eta L) Q(b_d). The quantifier over sufficiently small d is essential here. This does NOT prove a criterion using just the exact width d=w(L) or finitely many scales.

Proof:
1. RH suffices by ordinary sequence Cauchy–Schwarz on actual zeros. Otherwise symmetry gives Theta>0 (Theta<=1/2; no attainment assumed). Suppose the exponentially relaxed bound holds for every allowed pair beyond L0 at some eta<Theta.
2. Uniformly |Re z|<=1/2, H_{b_d}(z)=H_b(dz), and compact smoothness gives |H_b(dz)| <= C_b(1+d|Im z|)^-2 for 0<d<=1. The all-multiplicity count N(T)=O((1+T)log(2+T)) then implies
    0<Q(b_d)<=sum_rho |H_b(d z_rho)|^2=O_b(d^-1 log(2/d)).
The inequality can also be seen by absolute summation and even/real symmetry; no RH. For dyadic shells above 1/d the weights decay geometrically with exponent 3 up to a logarithmic factor.
3. For an arbitrary fixed real even h smooth compact supported in [-A,A], set F_h(t)=B(tau_t h,h). Choose 0<c<Theta-eta; for each large t choose a dyadic d(t) with (1/2)exp(-ct)<d<=exp(-ct). For r=t+x-y, |x|,|y|<=A, the common d(t) lies below w(r+d(t)) eventually by monotonicity and log(1/w)=o(t), uniformly in x,y. All r+d exceed L0.
4. Set h_d=h*b_d. Exact convolution and simultaneous translation give
    F_{h_d}(t)=integral integral h(x)h(y) C_d(t+x-y) dx dy.
For each fixed t,d the zero-side interchange is justified by absolute strip-decay bounds, compact x,y and the zero count. Hence the hypothesized scalar bound gives
    |F_{h_d}(t)| <= ||h||_1^2 exp(eta(t+2A+1)) Q(b_d)
                 =O_h((1+t)exp((eta+c)t)).
5. Exact even-real identity: F_h(t)=sum_rho H_h(z_rho)^2 exp(t z_rho); F_{h_d}(t) uses the additional factor H_b(d z_rho)^2. Since H_b(0)=1 and H_b'(0)=0, Taylor near zero together with the uniform strip bound away from zero gives
    |H_b(dz)^2-1|<=C_b d^2 |z|^2
for the full centered zero strip and 0<d<=1. The Schwartz decay of H_h ensures sum_rho |z_rho|^2 |H_h(z_rho)|^2<infinity. Thus
    |F_h(t)-F_{h_d}(t)|<=C_h d^2 exp(Theta t)
                       =O_h(exp((Theta-2c)t)).
No restriction to finite zero height, and no assumption of a maximal off-line zero.
6. Choose c=(Theta-eta)/3. Combining estimates yields
    F_h(t)=O_h((1+t)exp((Theta+2eta)t/3)).
Choose alpha strictly between (Theta+2eta)/3 and Theta. Then every fixed such h has F_h(t)=O_h(exp(alpha t)).
7. Choose a zero z0 with Re z0>alpha and a real even normalized bump h with H_h(z0)!=0 (a sufficiently narrow dilation of b works). The one-sided Laplace transform of F_h for Re s>1/2 equals
    sum_rho H_h(z_rho)^2/(s-z_rho).
Termwise integration is permitted by the absolute square sum and the strip bound; the right side is locally normally convergent off the discrete zero set, with a nonremovable pole at z0 of residue mult(z0)*H_h(z0)^2. The asserted growth would instead make the Laplace transform holomorphic on Re s>alpha. Meromorphic identity theorem contradiction. Thus any eta<Theta must fail at arbitrarily large L. In particular eta=0 yields the RH-equivalence.

The proof replaces Danesh's variable partitions by a fixed-shape convolution and an exponentially small approximation whose cost is balanced against the unknown rightmost zero displacement. The approximation is NOT presumed to converge fast enough merely by shrinking: step 5 pays the entire actual zero-side error at the exact exponential rate exp(Theta t). The arbitrary h is used only as an auxiliary in the contradiction, not as a member of the criterion's required test family. No independent theorem proving the hypothesized bound has been supplied.

## 3. Exact parity and arithmetic target

Let q=Q(b_d), c=C_d(r), which is real for real b by zero conjugation. Center the pair at +/-r/2. The symmetric and antisymmetric two-pulse energies are 2(q+c) and 2(q-c). Hence the scalar bound is exactly equivalent to their joint nonnegativity; even and odd both must be covered by this argument. A single historical odd endpoint test cannot settle the absolute-value gate.

Let k_d(u) be the actual mixed correlation of the two translated bumps; its support lies in [r-d,r+d]=[L-2d,L]. The direct explicit formula (Danesh Eq. 36) expresses C_d as the pole integrals plus the off-diagonal gamma kernel minus the prime-power sum,
    C_d(r) = integral k_d(u) [exp(u/2)+exp(-u/2)-exp(-u/2)/(1-exp(-2u))] du
             - sum_{exp(r-d)<=n<=exp(r+d)} Lambda(n)/sqrt(n) k_d(log n).
Because r>d and d<log 2, the cross formula is nonsingular, while the individual diagonals have no prime powers. The pole and prime terms must be kept in the same correlated enclosure: bounding them independently in absolute value pays terms of exponential size. This makes a scalar moving-window prime discrepancy test, not a finite-precision determinant or an eigenvalue search. For L1-normalized b_d, q has scale O(d^-1 log(2/d)), with lower bound q(d)d^-1||b||_2^2.

## 4. Boundaries / next

- DT01 is an independently derived analytical proof candidate relative to Danesh, not a claim of priority or peer review. An exterior search found related Suzuki screw-function work; compare fixed-profile/translate criteria before any novelty claim.
- Directly audit the theorem above (especially uniform dyadic width eligibility, full zero sum error, and absolute convergence under dilation). Then formalize the exact translation, even/odd identity, and scalar moving-window arithmetic dictionary against existing OWC source maps and normalizations.
- Investigate the scalar correlated prime-pole discrepancy, with explicit scales. No assertion that known prime distribution or finite checks suffice for all L,d; the uniform bound is still RH-strength. No implication from NF527's fixed-aperture collar positivity to this growing-aperture criterion.
- OWC phase III remains independent; no modification of NF sources, no added workflow, no RH or global positivity claim.
