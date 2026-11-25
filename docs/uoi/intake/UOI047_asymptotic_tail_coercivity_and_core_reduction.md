# Weil-Lab — UOI047: asymptotic prime/Gamma tail coercivity and core–tail variational reduction

**Research status:** New analytic reduction on the *same nested, three-moment-neutral collar family* used in UOI040–UOI046, derived from UOI045's spatial Gamma estimate and UOI046's frequency-sliced arithmetic method. **Not Lean compiled, no kernel or strict axiom receipt, no CI/GitHub submission, no NF numerical promotion, and not a claim of global original Weil positivity or RH.** The broad-support literal-to-native attachment F01/F08 is still open. Numerical stage-ten checks below verify only the inherited finite rational envelope.

## Source and domain fidelity

Pinned original repository revision `614ba879f7389fdb620c474adaee273b00eac71c`, with the original `ActualZetaOriginalCollarPrimeBound.lean` full two-sided von Mangoldt correlation, `ActualZetaPhaseIVOriginalNarrowSignedGamma.lean` genuine signed Gamma bracket bound, `NeutralWeilSourceMixedForm.lean` crossed exponential poles, and the pre-existing UOI045 spatial log-energy analytic note. Retain only the **literal** analytic form until F01/F08 are discharged.

Set `t=log8`, `delta=1/1000`, `c_j=(j+1/2)t`, `delta_j=delta*8^{-j}`, `I_j=(c_j-delta_j,c_j+delta_j)`. Every `f` in the algebraic union `S_infty=union_m S_m` is `f=sum_j f_j` with finitely many nonzero `f_j in C_c^infty(I_j;C)`, satisfying separately on each collar:

`int f_j = int f_j e^{x/2} = int f_j e^{-x/2}=0`.

The two pole moments and hence the original pole mixed form vanish on `S_infty`. Write `Gamma(f)` for the original digamma Fourier quadratic, `P(f)=sum_{n>=2} Lambda(n)/sqrt(n) [C_f(log n)+C_f(-log n)]` for the **complete** literal two-sided prime quadratic, and `W_lit(f)=Gamma(f)-P(f)`. On `S_infty`, the prime sum for each single test is finite because physical support is bounded at that finite stage.

Prior analytic Gamma inputs (UOI045): with `g_j=859/1000+3j/5`, `G>1.099`, `L(f)=int (1/2)log(1+16pi^2 xi^2)|hat f(xi)|²dxi`,

(1) `Gamma(f)>=sum_j g_j ||f_j||²`;

(2) `sum_j L(f_j) <= L(f)+(1/1000)||f||² <= Gamma(f)+(28/5+1/1000)||f||²`.

The coefficients `g_j` increase linearly, and `g_j>=(3/5)(j+1)`. These are *analytic* source-derived estimates, not a fresh Lean check.

## Main result: the *entire* remote-tail prime quadratic is Gamma-negligible

Let `T_M={f in S_infty: f_j=0 for all j<M}`; this comprises arbitrarily many remote collars, not a fixed finite stage. Put `g_M=859/1000+3M/5`, `delta_M=8^{-M}/1000`.

**Tail coercivity theorem (analytic, using the cited classical Brun–Titchmarsh bound):** There exist absolute finite constants `C_0,C_1,C_2>0`, independent of `M`, and a decreasing explicit-symbolic function

`eps_M = [2 C_0 delta^(3/2) 8^(-3M/2)] / [(8^(1/4)-1) g_M]`

`       + 2 sqrt( [2/log8] * [1+(28/5+1/1000)/g_M] * [(5/3) C_1 delta_M + C_2/g_M] )`

such that for **every finite** `f in T_M`,

`|P(f)| <= eps_M Gamma(f)`, and `eps_M -> 0` as `M->infty`.

The constants may be chosen from the Chebyshev bound `psi(X)<=Cpsi X` (`C_0=8pi sqrt(2/3) Cpsi`) and the arithmetic column estimate established below (`C_1,C_2`); no optimized numerical values or explicit cutoff `M_0` are asserted. Qualitatively `eps_M=O(M^(-1/2))`, with a faster exponentially decreasing low-frequency term.

Consequently **there exists some finite stage index `M_0`** such that for every `M>=M_0` and every `f in T_M`,

`W_lit(f)=Gamma(f)-P(f) >= (1-eps_M) Gamma(f)>0` for `f!=0`.

This proves a positive *infinite-stage far-tail* subspace of the literal signed Weil expression, not universal positivity, and leaves early–remote mixed interactions unconstrained.

## Proof, step 1 — strengthen UOI046's arithmetic column estimate

For `M<=j<k`, let `d=k-j`, `N=8^d`, `A_jk={n>=2: Lambda(n)>0, |log n-d log8|<delta_j+delta_k}`, and `b_jk²=sum_{n in A_jk}Lambda(n)^2/n`. Exact disjointness of the shifted `I_k`-supported packets implies the full-line identity `||V_jk f_k||²=b_jk²||f_k||²`, where `V_jk=sum_{n in A_jk} Lambda(n)/sqrt(n) shift_(+log n)` (orientation merely follows the original correlation convention). All prime powers remain included.

**Strengthened column lemma:** There are absolute finite constants `C_1,C_2>0` so that for all `k>M>=0`,

`sum_{M<=j<k} b_jk² <= C_1 delta_M (k+1) + C_2`.

Details: split at `j<=k/3`. There the admissible interval about `N` has length `h=O(delta_j N)` and, for sufficiently large `k`, `h>=N^(1/6)`. The classical short-interval Brun–Titchmarsh estimate `pi(x+h)-pi(x) <= 2h/log h`, together with `log h>=(1/6)log N`, bounds the ordinary-prime part by `O(delta_j d)`. The total higher-prime-power part is bounded by `O((d+1)^3 8^(-d/2))`, using the elementary count `O(sqrt(N)log N)` for powers `p^r`, `r>=2`, in `(N/2,2N)`. Summing `delta_j d` over `j>=M` costs at most `(delta_M/(1-1/8))k`, and summing higher-power errors over the separated `d` costs an absolute constant.

For `j>k/3`, the trivial **all-integer** count gives `b_jk²=O(delta_j d²+d²8^(-d))`. Summing the first term over `j>k/3` is `O(k²8^(-k/3))=O(1)`; summing the second is `O(sum_{d>=1}d²8^(-d))=O(1)`. The finitely many small `k` excluded by the early-region threshold are absorbed in `C_2`. Therefore the displayed column bound holds **uniformly in M**. In particular the fixed neighboring prime power `n=8` contributes to `C_2`, not to a false exponentially small bound for every edge.

## Proof, step 2 — a tail-sensitive Fourier slice

For each edge `j<k` set `R_d=8^(d/2)` and split its exact Fourier pairing at `|xi|=R_d`. The local zero ordinary moment and Chebyshev's upper bound imply UOI046's low-frequency estimate

`||Pi_<=R_d V_jk f_k|| <= C_0 delta^(3/2) 8^(-3j/2)8^(-d/4)||f_k||`.

Summing the geometric kernel **only over j>=M** gives

`|sum_{M<=j<k} low_jk| <= [C_0 delta^(3/2)8^(-3M/2)/(8^(1/4)-1)] ||f||²`.

Using `Gamma(f)>=g_M||f||²` on `T_M` yields the first term of `eps_M` after multiplying by the original factor two in `P`.

For the high-frequency portion, Cauchy–Schwarz over all ordered edges gives

`|sum high_jk| <= [sum_{j>=M}sum_{d>=1}||Pi_>8^(d/2) f_j||²]^(1/2) * [sum_{k>M}||f_k||² sum_{M<=j<k}b_jk²]^(1/2)`.

The count of thresholds at frequency xi is bounded by `(2/log8)log_+|xi|`. Therefore the first factor squared is at most

`(2/log8) sum_j L(f_j) <= (2/log8)[1+(28/5+1/1000)/g_M] Gamma(f)`.

By the strengthened column lemma, `sum_k(k+1)||f_k||² <= (5/3)Gamma(f)`, and `||f||²<=Gamma(f)/g_M`, the second factor squared is at most

`[(5/3)C_1 delta_M + C_2/g_M] Gamma(f)`.

The full two-sided arithmetic `P` contributes `2 Re sum_{j<k} <f_j,V_jk f_k>`, hence the second term of `eps_M`. Both pieces tend to zero as `M->infty`. QED under the quoted analytic inputs.

## Core–tail Schur-complement reduction (not a finite-dimensional algorithm)

UOI046's earlier all-stage relative bound `|P(f)|<=C_*Gamma(f)` gives a bounded Hermitian prime form on the Gamma completion `H_infty` of `S_infty`. Fix `M>=M_0` and let `H_tail` be the **Gamma-closure** of `T_M` inside `H_infty`. Tail coercivity extends continuously to `H_tail`, so `W=Gamma-P` is a strictly positive, bounded, invertible Hermitian form there.

For each finite-head test `h in S_M`, there is a unique `t_h in H_tail` such that `W(h+t_h,t)=0` for every `t in H_tail`. This is the Riesz/Lax–Milgram solution of the linear tail problem. Define the **effective head form**

`W_eff,M(h):=W(h+t_h,h+t_h)=W(h,h)-W(t_h,t_h)`.

For any `t in T_M` (indeed any in `H_tail`), the exact completion of squares holds:

`W(h+t,h+t)=W_eff,M(h)+W(t-t_h,t-t_h)`.

Every element of the **algebraic** union `S_infty` splits uniquely by physical collar support as `h+t` with `h in S_M`, `t in T_M`. The density of finite tail tests in `H_tail` therefore implies the sharp equivalence

**`W_lit >=0 on every S_infty test` if and only if `W_eff,M >=0 on every S_M head test`.**

If `W_eff,M(h)<0` for some smooth head `h`, approximate the minimizing `t_h` by finite tail tests: this gives an actual smooth finite-stage counterexample, not merely a vector in the completion.

This is an **infinite-dimensional Schur complement**: `S_M` is itself infinite dimensional, and the minimizing tail is generally not a finite collar combination. The result does *not* assert a finite matrix reduction, spectral compactness of `A_infty`, or positivity of the effective form. It isolates the remaining obstruction as head–tail coupling.

## Cross-projection diagnostic

The tail statement refers to the chosen *nested-collar filtration*. It is preserved under a dictionary that is isometric for the actual Gamma form, preserves the complete prime mixed form and maps each tail subspace to the corresponding target tail. Only then do the tail compression norm and the effective head Schur complement transfer. A map preserving only the signed total `W` preserves the Schur complement if it also preserves the relevant decomposition and tail Hilbert topology, but need not preserve Gamma-relative constants. No unspecified spectral equivalence is assumed.

## Exact finite arithmetic illustration, not proof of the theorem

Using the **unchanged** UOI044 ten-stage integer upper-envelope matrix, a transparent rational row-sum estimate for the subspace supported in collars `j=1,...,9` proves `P(f)<(43/100)Gamma(f)` and thus `W_lit(f)>(57/100)Gamma(f)` on that **finite-index tail in stage 10**. This finite arithmetic check is independent of the unquantified large-M theorem and does not establish any particular `M_0` for all larger stages. See `check_uoi047.py`.

## Formalization boundaries

Master ledger #898: F04 original `±log n` prime shift orthogonality; F10 signed Gamma and log physical energy; F25 tail filtration and frequency thresholds; F26 uniform strengthened arithmetic column inequality, relative tail form bound, Gamma completion and Schur complement; F34 preservation laws. F01/F08 broad-support literal/original-native identity remains distinct and open. No CI fan-out or new certificate claimed.

**Classical external arithmetic source:** The Montgomery–Vaughan short-interval Brun–Titchmarsh estimate is quoted, not reproduced as a Lean theorem. Accessible references include https://dms.umontreal.ca/~andrew/PDF/Pretentious010611.pdf and https://math.mit.edu/~drew/PrimeGapsOberwolfach3.pdf.
