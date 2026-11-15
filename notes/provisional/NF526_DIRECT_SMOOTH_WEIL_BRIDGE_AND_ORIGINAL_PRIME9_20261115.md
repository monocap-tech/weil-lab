# NF526 — direct smooth Weil bridge; authentic endpoint n=9 prime-only reduction

**2026-11-15 PT. ANALYTIC ONLY for the generic smooth/source-form identity, with an exact Fraction local PASS for endpoint support selection. No new Lean compile or dedicated GitHub CI.** Stacked draft on NF524 PR #553, commit bffd9f773020e2a3411a2c7837aac6d58b7d637a. Original NF494 H400/U400 source SHA256 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181 unchanged.

## Same original arithmetic vector

The retained source is ell_U(x)=sgn(x) 1_{B-delta<|x|<B} [U(|x|)/2] log(B/(B-|x|)); B=11/10, delta=1/500. NF524's full genuine two-source zeta-divisor graph membership and exact 242-original-moment strict smooth approximants phi_s -> ell_U in the *complete* graph norm are premises. This NF does not recompute the original 400 coefficients or their Cauchy fees.

## 1. Direct generic C_c-infinity Weil identity (analytic derivation, formalization OPEN)

For any f,g in C_c^infinity((-B,B)), define C_fg(t)=integral_R g(u)*conj(f(u-t)) du and F_f(z)=integral_R f(x)*exp(i*z*x) dx. C_fg is compact smooth, supported strictly within (-2B,2B), and exact all-complex F_Cfg(z)=conj(F_f(conj z))*F_g(z). Smooth strip-decay plus the repo's existing unconditional all-multiplicity dyadic zeta divisor count make the actual zero sum absolutely convergent.

Apply actual imported Zeta23.WeilEF.EF_lit_zeta DIRECTLY to this generic C_fg (not only to a Green synthesis). The formula gives the actual full multiplicity zero sum = two true pole cross moments - all finite supported prime powers + the complete literal digamma term. Fourier inversion of C_fg gives C_fg(t)=integral conj(hat f(xi))*hat g(xi)*exp(2*pi*i*xi*t) dxi, using hat f(xi)=int f(x)exp(-2*pi*i*xi*x) dx. The prime term is exactly the existing rightLimitPrimeSymbol with its aperture-threshold convention, the gamma-bracket change of variables is the existing compactWindowArchimedeanSymbol, and pole terms are the existing neutralLogPoleOperator. This gives the native rightLimitCompactWeilSymbolMathlib and W_B=neutralActualZetaLogWeilFormOperator B, on the SAME smooth test vectors.

The true graph's raw source coordinates are p_pm(q)=[F_f(conj z_q) +/- F_f(z_q)]/sqrt(2); the Hilbert source operator uses a further 1/sqrt(2), so its mixed difference equals 1/2 sum_q [conj(A_f)D_g+conj(D_f)A_g]. The authentic conjugate-ordinate involution (every multiplicity copy preserved) identifies the two terms, giving exactly sum_q conj(A_f)D_g. No arbitrary prime/pole/arch factor change.

Therefore analytically S(f,g)=<P f,W_B P g> for strict smooth source vectors. On the original h=graph(ell_U), NF524 gives h_s=graph(phi_s)->h. Both S and W_B are bounded on their ACTUAL graph/logarithmic domains by existing proved operators. Passing to the limit yields **analytic same-original-source diagonal** S(h,h)=<Ph,W_B Ph>. This does NOT require ell_U in Green closed span. **New generic Lean proof is not compiled:** generalize existing ActualZetaPrimeTransport and ActualZetaArchimedeanTransport beyond Green syntheses; use ActualZetaCorrelationTransform's existing generic all-complex lemma.

## 2. Original endpoint *prime-only n=9* (source-structure theorem; exact rational PASS)

Put w(d)=U(B-d)/2 * log(B/d) for 0<d<delta; ell_U is real odd and supported in (-B,-B+delta) and (B-delta,B). Its autocorrelation support lies inside [-delta,delta] union [2B-2delta,2B] union [-2B,-2B+2delta]. With B=11/10, delta=1/500, the positive outer interval is [2.196,2.2]. Exact Fraction bounds for log9 via log9=4 sum_{k>=0} 2^(-(2k+1))/(2k+1) and positive geometric tail prove 2.196<log9<2.198, and s=2B-log9 satisfies 4delta/3<s<2delta. Log2>delta, log8<2.196, log10>2.2 (from log(1+x)>=x/(1+x)); hence **the ONLY prime-power term of the exact original autocorrelation is n=9**. The finite smooth phi_s may have extra prime terms from its moment correctors; do not prematurely prune these.

At log9, C_ell,ell(log9) = - integral_{s-delta}^{delta} w(d) w(s-d) dd, and C(-log9)=C(log9). Thus authentic PRIME(ell_U) = (2 log3/3) integral_{s-delta}^{delta} w(d)w(s-d) dd. No pointwise U sign is certified on this overlap.

For the same real odd vector M_plus=2 integral_0^delta w(d) sinh((B-d)/2) dd and M_minus=-M_plus. The exact Hermitian POLE(ell_U)=-2 M_plus^2 <= 0.

The fully correlated signed scalar is therefore, conditional on the generic smooth bridge,
Q(ell_U)= ARCH(ell_U) + (2log3/3)*I9 - 2M_plus^2,
where ARCH is the COMPLETE original integral of compactWindowArchimedeanSymbol(2*pi*xi)*|hat ell_U(xi)|^2, not a finite selected-moment projection.

If the retained NF523 original-source envelope |U(B-d)/2| <= 2e-7 is used as a premise, rational inequalities show d,s-d>delta/3 on the n=9 overlap, log(B/d),log(B/(s-d))<8, overlap length<2delta/3 and 2log3/3<4/5; therefore **|PRIME|<1/366210937500000 <2.74e-15**. With sinh((B-d)/2)<1 and same source bound, **-1/781250000000000000 < POLE<=0**, i.e. |POLE|<1.28e-18. These are valid conditional source bounds, not new original-source coefficient replay. Neither the full ARCH sign nor the original signed scalar is decided.

## 3. Strict scope / NF527

The generic literal-C^2-to-native Fourier prime/gamma conversion must be formalized/compiled; only then can the original endpoint form attachment be promoted to a Lean-certified theorem. Green span/observability of ell_U remains OPEN and is not needed for this direct bridge. W_ODD_NEG, original signed sign, positivity of full even/odd branches and RH remain OPEN. No main merge/CI claim.

Local exact script: scripts/local_replay/verify_nf526_original_prime_support_exact.py; emitted receipt: notes/data/provisional/NF526_prime_support_exact_receipt.json. This exact calculation checks geometry/log bounds and conditional magnitude fees only, not the zeta explicit formula nor original NF494 coefficients.

NF527: compile generic smooth explicit-formula transport; obtain source-certified correlated rigorous ARCH and n=9 overlap from original H400/U400.