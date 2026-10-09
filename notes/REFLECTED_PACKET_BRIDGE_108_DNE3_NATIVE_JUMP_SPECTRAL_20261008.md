# RPB108 DNE3 — Exact global native Lévy form and the arithmetic threshold obstruction

Date: 2026-10-08 America/Los_Angeles. Independent DNE branch; starting head DNE2 `80dde77302d72808daa0fa3e0373a39cc79e341c`. Definitions [native jump form](../docs/TERMINOLOGY_RPB108_DNE3_NATIVE_JUMP_FORM.md); [rational zero-extension validator](../scripts/validate_dne3_native_levy_jump.py). CC46 and the independent NF15 certificate are read-only. **Classification: new full-CANONICAL-domain native positive-jump decomposition, supported boundary-killing condition, original scalar spectral reformulation and tested insufficiency of a crude odd floor. NO first-contact exclusion, RH or new whole-aperture sign.**

## 1. Exact digamma-to-jump identity: all constants fixed

Use CC27's original native Fourier convention `Fh(xi)=int exp(-2pi i xi x)h(x)dx` and

    a_arch(xi) = Re psi(1/4+i*pi*xi) - log pi,
    a0=psi(1/4)-log pi
       = -gamma_E-pi/2-3log2-log pi.

The primary DLMF formula 5.9.16 is

    psi(z)+gamma_E
       = int_0^infinity [exp(-t)-exp(-zt)]/(1-exp(-t))dt,

for Re z>0. Subtract at z=1/4+i*pi*xi and 1/4, take real parts, and put t=2d. This gives without an asymptotic or cutoff

    a_arch(xi)-a0
       = int_R j(d)[1-cos(2pi*xi*d)]dd,        (1)
    j(d) = exp(-|d|/2)/(1-exp(-2|d|))>0.

Near d=0, j(d)=1/(2|d|)+O(1); at infinity it decays exponentially. Thus (1) converges absolutely for each xi. The right side behaves as log|xi|+O(1) as |xi| grows, by the same original digamma asymptotics, and vanishes at xi=0. Plancherel, Tonelli and polarization yield for every *smooth supported* h

    int_R a_arch(xi)|Fh(xi)|² dxi
      = a0 ||h||²
        +(1/2)int_R j(d)||h-tau_d h||² dd.      (2)

The positive multiplier in (1) plus 1 has a two-sided finite constant comparison with log(e+|xi|): continuity and positivity on bounded frequency ranges, and logarithmic asymptotics at large frequency. Therefore (2) extends by closed-form completion to the ENTIRE zero-extended supported canonical logarithmic domain D_a; conversely the positive jump energy plus physical L2 norm is finite exactly on D_a. This is a full-domain identity, not a product-core or smooth-eigenvector assertion.

## 2. Exact prime pair and pole-free operator: no lost factor or boundary term

For each original active prime-power n with ell_n=log n<=2a, c_n=Lambda(n)/sqrt(n)>0, zero extension and a unitary shift on whole physical R give

    c_n||h-tau_ell_n h||²
      = 2c_n||h||²
         -c_n <h,tau_ell_n h+tau_(-ell_n) h>.  (3)

This retains BOTH original physical translation orientations and includes powers 4 and 8 with weight log2. Summing over every active n gives the exact pole-free form H_a (NOT the full original Q):

    H_a(h)=J_a(h)-kappa_a||h||²,                   (4)
    J_a(h)=(1/2)int_R j(d)||h-tau_d h||² dd
         +sum_(ell_n<=2a)c_n||h-tau_ell_n h||²,
    kappa_a=log pi-psi(1/4)+2sum c_n
           =gamma_E+pi/2+3log2+log pi+2S_a.      (5)

These equalities hold on ALL D_a and extend by polarization to mixed tests. They do not silently remove prime/pole terms: the original Q is recovered by adding its exact **positive even / negative odd** Hermitian pole corrections. Every part of J_a is nonnegative. The semibounded selfadjoint pole-free operator is simply the Dirichlet jump generator J_a minus a scalar potential kappa_a. Compactness of D_a->physical L2 from CC31/CC41 gives compact resolvent for both.

Support compatibility is automatic in this representation. On h supported in D_a, a newly activated shift ell_n>2a has zero overlap, so its added jump energy is exactly 2c_n||h||² and cancels the corresponding increase of kappa by 2c_n when viewed from a larger cap. No fictitious change to previously supported original native Q occurs.

This is a stronger *unweighted* domain representation than the DNE1 smooth product identity. For DNE2's ground-state unitary U_phi on the entire transformed form domain one now has the exact and globally valid, if not manifestly nonnegative term-by-term, expression

    E_phi(u)=J_a(phi*u) - (kappa_a+lambda_0(a))||phi*u||². (6)

The stronger identity that **replaces** (6) by pure weighted `phi(x)phi(y)(u(x)-u(y))²` integrals for EVERY rough quotient u is still NOT claimed; the product-core extension/Beurling-Deny ground-transform identification remains to be justified separately. DNE2's Markov semigroup theorem is unaffected.

## 3. Supported exterior killing and a logarithmic boundary condition

Decompose the continuous jump integral using zero extension:

    J_arch,a(h)
      =(1/2)int_(-a)^a int_(-a)^a
             j(x-y)|h(x)-h(y)|² dxdy
       +int_(-a)^a k_a(x)|h(x)|²dx,              (7)

    k_a(x)=int_(a-x)^infinity j(t)dt
                 +int_(a+x)^infinity j(t)dt, |x|<a.

Both prime jumps in (4) also contain exterior-support losses, and must remain untruncated. The strictly positive `k_a` is minimized at x=0 because j decreases with |d|:

    k_a(x)>=k_a(0)=2int_a^infinity j(t)dt>0.     (8)

Moreover j(t)=1/(2t)+O(1) as t approaches0+, so

    k_a(x)=(1/2)log[1/(a-|x|)]+O_a(1)           (9)

as |x| approaches a from within, with a dimensionless fixed reference scale understood inside the logarithm. Every h in D_a therefore obeys the integrable logarithmic boundary penalty

    int_(-a)^a k_a(x)|h(x)|²dx < infinity.       (10)

This is a REAL domain property of supported canonical functions. It does NOT give pointwise h(+-a), H1 regularity, a Hopf trace, or a contradiction to CC28's essential-support endpoint saturation. In particular an h can approach either endpoint in essential support while (10) holds.

## 4. Actual homogeneous equation becomes a scalar jump spectral problem

The CC40 contact equation, weak on D_a, is

    (J_a-kappa_a)h +2c(h) cosh(x/2)=0,  even;
    (J_a-kappa_a)h -2s(h) sinh(x/2)=0,  odd.      (11)

Here the moment terms are interpreted as bounded physical functionals on (-a,a), using the supported operator of CC41. This restores BOTH original signed poles. The distinct cases are:

- **moment-carrying even or odd:** rank-one perturbation at the scalar level kappa_a, with its own CC40 threshold/susceptibility.
- **moment-zero even or odd:** an eigenvector of the positive Dirichlet jump operator exactly at level kappa_a, obeying the additional cosh- or sinh-moment orthogonality.

Therefore a higher pole-free zero eigenmode is NOT a zero eigenmode of J_a; it is an eigenmode at the explicitly known positive *arithmetic level* kappa_a. CC43's ground-state eigenvalue relation is lambda_0(H)=lambda_0(J)-kappa_a, so its spectral gap is unchanged. Rephrasing this target does not itself rule out equality.

## 5. An unconditional but insufficient odd form floor

For odd real h, reflect x<0 onto (0,a). Its full interior continuous jump part (7) has the exact parity folding

    int_0^a int_0^a [
       j(|x-y|)|u(x)-u(y)|²
       +j(x+y)|u(x)+u(y)|² ]dxdy,
       u(x)=h(x) for x>0.                     (12)

Since j(|x-y|)>=j(x+y), the folded integrand is >=2j(x+y)(|u(x)|²+|u(y)|²). The exterior term has floor (8). Therefore

    J_arch,a(h)/||h||²
       >= 2int_a^infinity j(t)dt
          +2int_a^(2a)j(t)dt.                  (13)

For an active shift ell_n, put N_n=floor(2a/ell_n)+1, so N_n*ell_n>2a. The telescoping identity from h(x) to its zero value after N_n shifts and Cauchy-Schwarz give

    ||h||² <= N_n² ||h-tau_ell_n h||².          (14)

Summing independently gives a fully unconditional original odd jump floor

    J_a(h)>=F_odd(a)||h||²,
    F_odd(a)=2int_a^infinity j+2int_a^(2a)j
             +sum c_n/N_n².                    (15)

Hence F_odd(a)>kappa_a would be sufficient to show H_a^odd>0. It is not necessary, since (13) and (14) discard most geometry and cross-correlation.

**Sharp stopping audit at a=53/50:** The active prime set is exactly 2,3,4,5,7,8, with S_a<12093/3740<4 (CC37 rational coefficient bounds, unchanged set). Since a>1,

    T=int_a^infinity j(t)dt
      <= 2 exp(-a/2)/(1-exp(-2a)) <35/24

using exp(1/2)>8/5 and exp(2)>7. The middle integral is <=T, and N_n>=2 for every active prime. Therefore

    F_odd(53/50) <4T+S_a/4<35/6+1=41/6.      (16)

But `kappa_a>7`: gamma_E>1/2, pi/2>3/2, 3log2>2, log pi>1, and S_a>1 (already c2+c3>1 by log2>2/3, sqrt2<3/2, log3>1, sqrt3<7/4). The Euler bound can be checked as gamma_E>=H_6-log7>49/20-39/20=1/2. All inequalities are strict classical elementary bounds. Consequently

    F_odd(53/50)<41/6<7<kappa_(53/50).        (17)

This **proves that the particular absolute/telescoping odd-floor certificate CANNOT establish odd positivity at 1.06**. It does NOT produce an original negative odd vector or disprove a sharper signed/eigenfunction-adapted arithmetic estimate. The finite NF15 E80 original Q positivity and NF10 F112 complement remain read-only and cannot fill the mixed Schur gap.

## 6. Rational controls and outstanding exact domain transfer

The source-published Fraction validator tests 3^5 supported lattice vectors against: (i) complete ambient/interior/exterior jump splitting, (ii) the prime `2c mass minus two translated correlations` identity, and (iii) the scalar shift identity, followed by 25 odd-parity vectors against both exact folding and its positive floor: **779 exact rational assertions**. The model's strictly positive symmetric weights `j(m log4)=2^{-m}/(1-16^{-m})` are RATIONAL, with j(log4)=8/15 and j(2log4)=64/255. The finite ambient lattice has an explicit exterior; it is not a numerical integral of the real continuum kernel.

The independent local Fraction replay passed all779 cases; this does not prove DLMF 5.9.16, full-domain Fourier-Plancherel extension, any actual native sign, or a true zeta null classification. Those infinite-dimensional statements are analytically argued above. No Lean compilation or full historical test replay is claimed.

**Next DNE4:** Either (A) prove the full weighted `phi(x)phi(y)` jump representation on arbitrary ground-state-quotient eigenfunctions by verifying the precise native Dirichlet-form core/ground-transform hypotheses, then test an ACTUAL arithmetic constrained gap; or (B) directly certify a nontrivial odd/even spectral floor for the explicit J_a at level kappa_a, retaining simultaneous continuous and prime-shift correlations instead of the insufficient telescoping floor (17). Stop if a proposed strict surplus is merely (11) restated.

Status: original whole-positive cap stays a=21/20. DNE3 supplies no RH proof, all-aperture first-contact exclusion, full a=53/50 positivity, F4/transport, or Lean theorem. No other branch modified.
