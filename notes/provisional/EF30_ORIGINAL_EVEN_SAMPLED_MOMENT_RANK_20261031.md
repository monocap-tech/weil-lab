# EF30 — Original SI10 sampled-moment row equivalence and central recurrence rank gate

2026-10-31; active W-EVEN-FORM OPEN. Parent EF29 PR #421, source #41234333164 and final #41234685098 PASS. Original 471 signed vector gtilde=g-a_arch(c0)h0 and source A_prime known, but actual kernel projection delta and complete A open.

## Exact source-preserving moment simplification

Use the unchanged original SI10 107 rational centers c_j with Taylor orders p_j totaling 469, real-even original source modes U_jk(x)=x^k cos(2pi c_j x) for k even and x^k sin(2pi c_j x) for k odd, and the 471 original EF28 real-even C5 bell pairs phi_l, centers x_l=l/512, r=1/8192. Genuine original moment H_(j,k),l=<U_jk,phi_l> equals integral of b_r(t)U_jk(x_l+t) over t in [-r,r]. Binomial and angle addition expansions show this equals a linear combination of sampled original modes U_jq(x_l), q<=k, same c_j, with the leading coefficient

  beta_j=int_-r^r b_r(t) cos(2pi c_j t)dt=bhat_r(c_j).

For all original c_j<896 and r=1/8192, 4c_j r<1; therefore |2pi c_j t|<pi/2 throughout the bell and beta_j>0. Each block is a REAL INVERTIBLE TRIANGULAR transform of sampled source rows. No original source has been approximated or replaced. The genuine positive even pole c(x)=cosh(x/2) contributes row J_r(1/2) cosh(l/1024), J_r>0. The full original 470x471 source-and-pole moment Htilde has exactly the same rowspace and kernel as the simpler sampled 470x471 matrix, with the same coefficient-space Euclidean projector and the same EF29 residual delta.

## Original source recurrence can prove full row rank via ONE coefficient

On integer sample index l, the true original source rows are rational scalar multiples of l^k cos(theta_j l) (even k) or l^k sin(theta_j l) (odd k), theta_j=2pi c_j/512. They solve the true original characteristic shift recurrence

  P(E)=prod_j (E^2-2cos(theta_j) E+1)^p_j
      =sum_(s=0)^938 b_s E^s,

of degree 938, leading and constant coefficients exactly 1. Source rows are EVEN in l. Native rational frequencies imply roots exp(+/-i theta_j) are algebraic roots of unity. Explicit rational alias checks of all 214 conjugate source roots ensure distinctness (including no self-conjugate root).

Suppose a real source combination vanishes at all l=1,...,471. By EVENNESS it vanishes at -471,...,-1. Applying the order-938 recurrence at index -469, all terms but b469 F(0) vanish; if the actual original central coefficient b469 is nonzero, F(0)=0. Then 939 consecutive F values vanish at indices -469,...,469. A bilateral recurrence with nonzero leading and constant terms propagates zero to every integer index. Uniqueness of distinct-root exponential polynomials now forces every coefficient of the 469 native source rows to vanish. **Thus rigorous b469 != 0 is a sufficient original full source-row rank 469 certificate.** It is NOT a condition-number estimate.

The EF30 verifier performs the FULL original 469 quadratic factor polynomial multiplication using EF24/SI06 native 340-digit outward integer cosine intervals and verifies the actual b469 interval, mirror coefficients, degree, all roots and source order. It marks source rank accepted ONLY if the original b469 interval excludes zero. If it includes zero, no rank claim is permitted. An independent exact Fraction toy polynomial validates the recurrence algebra but supplies no original-source evidence.

## The positive even-pole row is independent, exactly

The sampled original source entries are ALGEBRAIC because the c_j and x_l are rational and exp(i2pi c_j x_l) is a root of unity. Hence their nullspace has an algebraic-coordinate basis. Let a be any NONZERO algebraic vector in that nullspace. The actual positive-pole overlap is

 sum_(l=1)^471 a_l cosh(l/1024)
 = (1/2)sum_l a_l (T^l+T^-l), T=exp(1/1024).

By Hermite-Lindemann, T is transcendental because 1/1024 is nonzero algebraic. The right side is a nonzero Laurent polynomial in T with algebraic coefficients: choose its largest l with nonzero a_l. Such a polynomial cannot vanish at T. Therefore the pole row is not in the real span of source rows and **adds exactly one row rank**. If the b469 central gate certifies source rank469, full Htilde rank470 and nullity exactly 1. This argument does NOT assert the pole is nonzero on every REAL source-null vector: the full source-nullspace has dimension at least two and the pole functional has its own kernel.

## Explicit scope and next obligation

EF29 actual original signed gtilde and the original h0 row are preserved in native Actions artifact #13054987778. This EF30 pass is a genuine original MOMENT ROWSPACE/rank advancement, not yet an evaluated residual. Even if exact Htilde rank470 is proved, its unique kernel orientation, a numerical condition budget, delta=dist(gtilde,range Htilde^T), signed original arch diagonal A_arch, corrected even Schur sign and whole Weil/RH remain unproved.

EF31 entry: produce an outward certified oriented one-dimensional kernel vector or exact determinant quotient, then contract with EF29 true original outward signed gtilde and separately enclose A_arch. A floating SVD rank or nullspace from a conditioned pilot alone does not certify delta; if available precision cannot resolve the kernel, record a quantitative finite-grid method STOP. The original source/domain/digamma analytic audit stays separate. All research additive, no main merge.

## Source-verified original exact rank receipt (2026-10-31)

Native original [Actions #41236300352](https://github.com/monocap-tech/weil-lab/actions/runs/41236300352), job `124640690086`, **SUCCESS**, including manifest and governance. The actual 107 rational SI10 source-center trigonometric values were outward-evaluated at 340 decimal places, all 469 quadratic recurrence factors multiplied with directed rounding, all 214 sampled conjugate roots checked distinct, and the genuine order-938 central source coefficient was enclosed strictly NEGATIVE, displayed approximately **b469≈−1.2390712361×10^127**. Adjacent source coefficients were also decisively signed: b467≈−1.2382636363×10^127 and b468≈+1.2388692886×10^127, with reciprocal symmetry. The accepted source proof therefore establishes **exact rank 469 of the unchanged source rows**; by the documented algebraic/transcendental original pole-row argument **rank Htilde=470, nullity1**. This is an original mathematical rank certificate, not an inference from a numerical singular-value threshold.

The source script was strengthened after the first PASS to fail closed unless the full original outward integer interval proves **−1.24×10^127 < b469 < −1.23×10^127**, with a new repeat workflow pending. No exact source-oriented one-dimensional kernel coefficient vector was produced, and its contraction δ with EF29's true original 471-vector remains UNCOMPUTED. The exact rank result does not imply manageable numerical conditioning or a sign of corrected Schur.
