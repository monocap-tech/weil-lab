# RPB108 DNE7 — Reflected Hankel decomposition and infinite arithmetic sign-indefiniteness

Date: 2026-10-08 America/Los_Angeles. Independent DNE parent `6f9ecef8714f1b7517a8a0d55108d164718a16f0` (DNE6). Definitions: [DNE7 reflected arithmetic Hankel](../docs/TERMINOLOGY_RPB108_DNE7_REFLECTED_HANKEL.md). Contemporary Coupled CC53 and Aperture NF18 are read-only. **Classification:** exact original reflected parity comparison, an INFINITE-dimensional native prime-two negative/positive form result, and exact moment-constrained no-go for unconditional reflection positivity. This does NOT exhibit a negative original Weil vector, exclude an actual null, or prove RH/F4/Lean.

## 1. A full original-arithmetic parity comparison

Fix finite a>0 and a real f smooth with compact support in (0,a). Let Ef(x)=f(|x|) and Of(x)=sgn(x)f(|x|) on I=(-a,a), zero outside. Both lie in the supported canonical logarithmic domain. They have identical physical mass, same-half energies, and the same exterior-killing energies. Their contributions from local diagonal/renormalization terms cancel in H_a(Of)-H_a(Ef).

Here H_a is the COMPLETE original pole-free native form, with the exact digamma/archimedean multiplier, all active prime powers and both physical shift orientations; it differs from the full original Q_a ONLY by the signed Hermitian pole cross terms. The genuine off-diagonal archimedean kernel is `-j(x-y)` with

    j(t)=exp(-|t|/2)/(1-exp(-2|t|)), t!=0,

and every original prime atom has coefficient `-c_n`, `c_n=Lambda(n)/sqrt(n)>0`, at both +/-ell_n, `ell_n=log n`.

Folding the cross-origin pairs gives the exact identity

    H_a(Of)-H_a(Ef)=4 C_a(f),                         (1)

    C_a(f)=A_a(f)+P_a(f),                              (2)
    A_a(f)=int_0^a int_0^a j(x+y)f(x)f(y) dxdy,
    P_a(f)=sum_(ell_n<=2a)c_n
                int_(max(0,ell_n-a))^(min(a,ell_n))
                   f(x)f(ell_n-x) dx.                 (3)

No extra prime factor two appears in P: the difference of both original shift orientations produces the overall factor four in (1). The integral in (3) uses the zero extension. For supported f away from zero, all integrals converge absolutely. DNE4's complete-domain weighted jump formula is not replaced; (1) is an independent and exact comparison of the two physical parity extensions.

## 2. The archimedean reflected Hankel form is positive

For t>0, the native kernel has a convergent geometric expansion

    j(t)=sum_(k>=0) exp[-(2k+1/2)t].

Therefore, for every real f in C_c^infty(0,a),

    A_a(f)=sum_(k>=0)
       |int_0^a exp[-(2k+1/2)x] f(x) dx|² >=0.      (4)

The sum and integrals can be exchanged absolutely because f vanishes near x=0 and the series is uniformly exponentially convergent on its pairwise support. For complex tests use the Hermitian pairing and absolute squares. This is TRUE reflection positivity for the continuous native archimedean part; it is not inherited by the full prime-added Hankel form.

Each prime term is a partial reflection pairing, not a positive square:

    R_ell f(x)=f(ell-x);
    P_n(f)=c_n <f,R_ell_n f>_(L²(0,a)).              (5)

An antisymmetric packet under R_ell_n can have negative P_n, while a symmetric packet has positive P_n. Whether the complete prime-plus-arch comparison is positive requires an additional estimate; the next section disproves universal positivity on arbitrary supported tests.

## 3. Theorem DNE7-A: infinite-dimensional negative and positive reflected sectors

**Theorem.** For EVERY finite aperture a>log2/2, the actual arithmetic C_a has an infinite-dimensional subspace E_- of smooth positive-half profiles with

    C_a(f)<= -(c_2/2)||f||_2²    (f in E_-),          (6)

and an infinite-dimensional subspace E_+ with

    C_a(f)>= c_2||f||_2²         (f in E_+),          (7)

where c_2=log2/sqrt2. Moreover, for ANY fixed finite list of continuous linear moment functionals, both E_+ and E_- can be intersected with their common kernel while remaining infinite-dimensional.

**Proof.** Put ell=log2. Choose 0<delta<min{ell/8,(a-ell/2)/3,(log3-ell)/8}, and put x0=ell/2-delta, y0=ell/2+delta. Both lie in (0,a). Choose a sufficiently small interval J about x0, with reflected J'=ell-J about y0, so J,J' are disjoint in (0,a); all pairwise sums on S=J union J' lie below log3; and the sums from J+J and J'+J' are separated from ell. There are NO active prime-power reflection displacements below ell and no others in [ell,log3). Consequently the only nonzero prime reflection on functions supported in S is the n=2 term. In particular, `R_ell` maps J exactly onto J'.

For any real g in C_c^infty(J), define f_+=(g+R_ell g)/sqrt2 and f_-=(g-R_ell g)/sqrt2, both extended by zero on the rest of (0,a). Their two components have disjoint supports, so ||f_±||_2=||g||_2; reflection gives

    int f_±(x) f_±(ell-x) dx= +/-||f_±||_2².     (8)

Thus P_a(f_±)= +/-c_2||f_±||². The archimedean reflected kernel is bounded on SxS by j(2 inf S)<infinity and

    0<=A_a(f)<=j(2inf S)||f||_1²
                   <=|S|j(2inf S)||f||_2².   (9)

Shrinking J makes |S|j(2inf S)<c_2/2. Equations (4),(8),(9) give (6)-(7). The map g->f_± is injective, so each subspace is infinite-dimensional. Intersecting an infinite-dimensional linear space with the kernels of finitely many linear forms leaves an infinite-dimensional subspace; this includes original even cosh and odd sinh pole moments. QED.

The result describes **indefinite parity COMPARISON**, not an actual negative direction of H or Q. Each highly localized test may carry a large positive diagonal logarithmic energy, so (6) does not contradict the certified whole-positive aperture 21/20.

## 4. Explicit rationally guarded original-a=53/50 construction

Take a=53/50 and ell=log2; choose eps=1/100 and centers x0=3ell/8, y0=5ell/8, with J=(x0-eps,x0+eps), J'=(y0-eps,y0+eps)=ell-J.

Use the standard strict rational guards

    2/3<ell<7/10,     log3>1,     sqrt2<3/2.        (10)

Then J,J' are disjoint and both inside (0,a), with minimum combined support >0. Every pairwise sum on S=J union J' lies in

    (3ell/4-2eps,5ell/4+2eps) subset (ell/2,1). (11)

The J+J and J'+J' intervals avoid ell because ell/4>2eps. Hence only cross-paired n=2 reflections survive; every prime power n>=3 has log n>=log3>1.

Because j decreases, for x,y in S one has j(x+y)<j(ell/2)=2*2^(-1/4)<2. Since |S|=4eps,

    0<=A_a(f)<8eps||f||²=(2/25)||f||²,
    c_2=ell/sqrt2>4/9,
    2/25<2/9<c_2/2.                               (12)

Thus the infinite-dimensional anti-reflected packet subspace at the ACTUAL TARGET a=53/50 satisfies the completely explicit strict native bound

    C_(53/50)(f)< -(c_2/2)||f||².                 (13)

This uses the full original coefficients, not a toy replacement dictionary or a finite location perturbation of zeta. Source strict inequalities (10) are standard elementary analytic bounds; the validator checks the rational implications of them, not logarithms by floating sample.

## 5. Stronger finite-moment no-go and the null-adapted condition

The negative subspace in Theorem A is infinite-dimensional. Removing the finite-dimensional span of ANY finite collection of prescribed positive-half moments cannot eliminate all its negative vectors. In particular, one can impose simultaneously

    int_0^a f(x)cosh(x/2)dx=0,
    int_0^a f(x)sinh(x/2)dx=0                           (14)

and retain infinitely many negative C directions. Therefore a proof strategy based on universal reflected positivity plus finitely many pole-moment corrections is mathematically impossible at prime2-active apertures.

For comparison, suppose the actual original Q_a is nonnegative and a REAL ODD original null has h=Of with the original sinh moment zero. Then H_a(Of)=Q_a(Of)=0 and the corresponding even test is legal. Using the full original positive even pole, whose moment is `2int f cosh`, gives

    0<=Q_a(Ef)=H_a(Ef)+8(int f cosh)²
              =-4C_a(f)+8(int f cosh)².            (15)

So any such actual null must obey

    C_a(f)<=2(int f cosh)².                         (16)

This is a necessary inequality; it does NOT exclude negative C, so Theorem A is perfectly compatible with it. A true null must also satisfy `H_a(Of,g)=0` for ALL admissible odd g and `int f sinh=0`. The proof target must exploit THAT eigenfunction equation, not only the moment constraints or unconditional sign properties on the entire canonical domain.

## 6. Classification and next office

**Proved DNE7:** exact parity comparison (1)-(3), continuous archimedean reflection positivity (4), full original prime-two reflected sign-indefiniteness with infinite-dimensional bounded-negative and positive subspaces (6)-(7), robustness under arbitrary finite moment constraints, explicit a=53/50 rationally guarded witness (10)-(13), and the contact-specific necessary comparison (15)-(16).

**Not proved:** existence of a negative original H or Q test, an actual Riemann-zeta null eigenvector, any lower bound for C on the low J-eigenspace, strict odd surplus gamma_odd> -lambda0, even/moment-carrying null exclusion, whole a=53/50 positivity, RH/F4/transport/Lean.

**DNE8 target:** restrict the exact reflected Hankel comparison to the genuine FINITE-RANK low-energy spectral space of the ACTUAL supported positive J_a (where a potential H-null must live at arithmetic level kappa_a), and test whether CC41's localization bounds and DNE4's weighted response supply an original-arithmetic estimate unavailable on arbitrary high-frequency packets. Do not relabel the bounded-negative C subspace as a crossing. The missing information is spectral ADAPTATION, not another generic reflection or fixed finite-moment estimate.

Concurrent Coupled CC53 and Aperture NF18 are read-only; DNE only adds files on its own branch.
