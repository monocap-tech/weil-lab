# RPB108 DNE11 — Complete native polynomial-log source calculus and effective Gram-error reduction

Date: 2026-10-08 America/Los_Angeles. Independent DNE parent `67d14b6e5b74fbed4b2506ecacf846083c0cb237` (DNE10). [DNE11 definitions](../docs/TERMINOLOGY_RPB108_DNE11_SOURCE_KERNEL_SPLIT.md). Read-only contemporaneous: CC56 finite polynomial source injectivity and NF20 physical-source Gram obstruction. Neither branch is modified.

**Classification:** exact whole-physical polynomial source decomposition; explicit dimension-free L² source-operator truncation bound; finite one-dimensional Gram integral reduction; numerical ONLY original constant-mode source sanity probe. **No rigorous whole56 source Gram interval was evaluated, no DNE9 reflected LMI is certified, no whole-a=53/50 positivity, first-contact exclusion, RH/F4 or Lean theorem.**

## 1. Exact native physical source, with both prime directions and both poles

Fix a=53/50, I=(-a,a), and finite supported polynomial p (a finite physically normalized Legendre combination). The ACTUAL original Weil form Q has the CC27/CC56 physical source

    s_Q[p](x)=s_arch[p](x)
       - sum_(ell_n<=2a)c_n [p_tilde(x+ell_n)+p_tilde(x-ell_n)]
       + exp(x/2)m_-(p)+exp(-x/2)m_+(p),      x in I,   (1)

where n runs through {2,3,4,5,7,8}, ell_n=log n, c_n=Lambda(n)/sqrt(n)>0, m_±(p)=int_I p(y)exp(±y/2)dy, and p_tilde is the zero extension. Both shift orientations and BOTH Hermitian pole terms remain present. For the complete pole-free H source, remove ONLY the final two exponential terms; the archimedean and prime parts do not change. The original full unbounded logarithmic operator is not claimed bounded on physical L²: (1) is lawful for finite polynomial input p, as shown by NF20/CC56.

By CC56's exact kernel representation,

    s_arch[p](x)=a0 p(x)
        +int_I j(|x-y|)[p(x)-p(y)]dy
        +p(x)[J(a-x)+J(a+x)],                          (2)

    a0=psi(1/4)-log pi=-gamma_E-pi/2-3log2-log pi,
    j(t)=exp(-t/2)/(1-exp(-2t))=exp(t/2)/(2sinh t),
    J(t)=int_t^infinity j(u)du
        =atanh(exp(-t/2))+atan(exp(-t/2)).

Every integral in (2) is well defined for a polynomial p: the near-diagonal difference cancels j(t)~1/(2t), and the endpoint J terms lie in L²(I).

## 2. Exact singular/regular split with an unexpectedly simple constant

Define

    r(t)=j(t)-1/(2t) for t>0,   r(0)=1/4,
    D[p](x)=1/2 int_I [p(x)-p(y)]/|x-y| dy.

The function r is real analytic at0, and extends holomorphically to |z|<pi. Put

    CJ=log2+pi/4.

Since J'(t)=-j(t) and J(t)+(1/2)log t ->CJ as t down to0,

    J(t)= -(1/2)log t+CJ-int_0^t r(s)ds.        (3)

Insert j=1/(2t)+r into (2). The positive r contributions from p(x) inside the integral CANCEL the two primitive integrals p(x)[-int_0^(a-x)r-int_0^(a+x)r] coming from J. Therefore the remaining regular part is only -int_I r(|x-y|)p(y)dy, not a two-sided principal-value remainder.

The constants cancel as well:

    a0+2CJ
       =(-gamma_E-pi/2-3log2-log pi)
                       +(2log2+pi/2)
       =-gamma_E-log(2pi).

Thus the exact supported archimedean action is

    +------------------------------------------------------------+
    | s_arch[p](x)=-(gamma_E+log(2pi))p(x)                         |
    |    -1/2 p(x)log(a²-x²)+D[p](x)                              |
    |    -int_I r(|x-y|)p(y)dy,  x in I.                           |
    +------------------------------------------------------------+   (4)

The boundary logarithm is retained EXACTLY. There is no small-distance cutoff, no unproved Fourier boundary trace and no deletion of the physical exterior killing. For p polynomial, the divided-difference term D[p] is a polynomial, explicitly

    D[p](x)=sum_(k=1)^deg(p)
          p^(k)(x)/[2 k k!]
             [(-1)^(k+1)(x+a)^k-(a-x)^k].                 (5)

For checks: D[1]=0, D[x]=x, D[x²]=(3x²-a²)/2. The finite prime terms remain piecewise polynomial with EXACT original cut positions x=±a±log n, and pole sources are explicit exponentials with true moments.

This removes the archimedean principal-value and endpoint-integral difficulties from the physical source Gram: the only non-polynomial non-pole components are the known universal log(a²-x²) and a SMOOTH analytic convolution.

## 3. Rigorous rational Taylor source truncation, uniformly through the endpoints

Define the holomorphic function

    q(z)=z*j(z)=z exp(z/2)/(2sinh z), q(0)=1/2,

with rational Taylor series q(z)=sum_(n>=0)q_n z^n. Comparing coefficients in 2sinh(z)q(z)=z exp(z/2) gives the EXACT recursion

    q_n=1/[2^(n+1)n!]-
         sum_(k=1)^(floor(n/2)) q_(n-2k)/(2k+1)!.       (6)

In particular q0=1/2, q1=1/4, q2=-1/48, q3=-1/32. Let

    r_N(t)=sum_(n=1)^N q_n t^(n-1).                     (7)

For every a=53/50 and real t in [0,2a=53/25], there is a UNIFORM rational majorant on |z|=R=5/2. Indeed

    |sinh(x+iy)|²=sinh²x+sin²y.

If |x|>=1/2 on |z|=R, |sinh z|>1/2. If |x|<1/2 then sqrt6<|y|<=5/2, on which |sin y|>1/2. Also |exp(z/2)|<=exp(5/4)<4. Consequently |q(z)|<10 and |q(z)-1/2|<11 on the entire circle. Cauchy bounds the nth coefficient of q-1/2 by 11/R^n. With ratio

    (2a)/R=(53/25)/(5/2)=106/125,

the error after retaining q1..qN satisfies

    sup_(0<=t<=2a)|r(t)-r_N(t)|
       <=(550/19)*(106/125)^N
       =:delta_N.                                       (8)

The finite INTEGER inequality

    550*106^600*10^41 < 19*125^600

has been independently checked exactly. Thus

    delta_600<10^(-41).                                 (9)

Let s_arch,N replace ONLY r in (4) by r_N. Schur's kernel norm test, with uniform |r-r_N|<=delta_N over I², proves for every finite supported polynomial p

    ||s_arch[p]-s_arch,N[p]||_L²(I)
        <=(2a)delta_N ||p||_L²(I)
        <3*10^(-41)||p||_L²(I).                         (10)

The bound does NOT deteriorate with the polynomial's degree. It is a bound on the analytic regularization-error OPERATOR, not on the native full source (which remains logarithmically unbounded as the degree grows). In particular (10) holds uniformly on any 56-mode low family and on any specified finite high Galerkin correction.

Because r_N is polynomial with rational coefficients and a=53/50 rational, the regular action `int_I r_N(|x-y|)p(y)dy` is itself an exactly computable polynomial in x; splitting the integration at y=x gives two finite polynomial primitives. The approximated ENTIRE original source therefore consists only of:
(1) polynomial pieces;
(2) p(x)log(a²-x²);
(3) piecewise polynomial original prime translates;
(4) the exact original exponential-pole sources.
No evaluation of digamma or singular improper integration remains in the source CONSTRUCTION.

## 4. Exact full physical source Gram from finite one-dimensional moments

Let W:R^d -> physical L²(I) map coefficient vectors to any explicitly chosen FINITE polynomial family w_i; it may include the NF19 two-high-mode Galerkin correction. Let S=L_Q W and S_N=L_Q,N W be their complete actual/approximated physical source maps, with L_Q,N defined by (1) and r_N in (4). From (10),

    ||S-S_N||_(coeff->physical L²)
          <=epsilon_N:=(2a)delta_N||W||_(coeff->L²).    (11)

For the physical low projection P_E onto E_p, the complete original high-source Gram is

    P_high=S*P_F S
       =S*S-[<w_i,Qe_k><Qe_k,w_j>]_(ij),               (12)

equivalently each entry is

    P_high,ij=int_I s_Q[w_i](x)s_Q[w_j](x)dx
          -sum_(k in E_p)Q(w_i,e_k)Q(w_j,e_k).          (13)

The subtracted E-pairings are finite ORIGINAL native source/action rows (NF17/NF19 where available), not approximations from a guessed bounded full Weil operator. The source inner product in the first term must include the COMPLETE archimedean-prime, prime-prime, archimedean-pole and prime-pole cross interactions.

Define the truncated high-source Gram P_high,N=S_N*P_F S_N. The fully rigorous whole-matrix operator error satisfies

    ||P_high-P_high,N||
       <=epsilon_N(2||P_F S_N||+epsilon_N)
       <=epsilon_N(2||S_N||+epsilon_N).                 (14)

The first version is sharper and can be certified from the evaluated truncated matrix. Thus DNE11 supplies an effective arbitrary-precision physical source Gram algorithm with a completely explicit error ledger for the infinite archimedean analytic tail. The remaining first source Gram `S_N*S_N` is a FINITE COLLECTION of known one-dimensional integrals of polynomial/logarithmic/piecewise-polynomial/exponential expressions. The only nontrivial endpoint singularities are log and log², integrable with known primitives or rigorously enclosed by interval quadrature after splitting at every original prime cut.

**Crucial status:** none of those complete d=56 truncated source Gram matrices has yet been evaluated, and no finite-interval quadrature errors for the 56x56 Gram have been paid. A bound for the analytic tail is NOT a certificate for the total physical residual. Nor does the scalar physical source floor 207/1000 become sharp simply from knowing S_N: NF20 proves its indiscriminate use already fails by more than 4x in genuine native E112 directions. The full form-dual geometry may still need source-aligned treatment.

## 5. First real original-source pilot — numerical, NOT interval certified

A separate reproducible mpmath probe evaluates the normalized constant vector e0=1/sqrt(2a) at a=53/50 directly from the UNTRUNCATED original CC56 source (2), all six prime weights, and the positive even pole. Its partition splits the x-integral at all active prime translation-panel boundaries and at zero; the endpoint logarithms are integrated as improper integrable terms.

At 45 and 65 working decimal digits, the displayed values agree:

    H_a(e0,e0)       ≈ -4.61202451798124222114267511708
    Q_a(e0,e0)       ≈  0.04015208427542074468707444145
    ||s_H(e0)||²_L2 ≈ 21.35582325869849124388021619
    ||s_Q(e0)||²_L2 ≈  0.08366183438191535692927289705

The first two agree with the independently PINNED CC40/NF12 exact interval sources (physical normalized Legendre degree0), which is a useful consistency check on the native source's constants, pole and translation orientations. For only the one-dimensional constant projection E0, its physical high squared residual from the probe is

    ||(I-P_E0)s_Q(e0)||² ≈0.0820496445102548671.

**This is NOT ||P_F112 s_Q(e0)||²**: the other 55 even retained Legendre projections have not been subtracted. The displayed integral results are exploratory numerical values, NOT validated source-Gram interval enclosures. Agreement of two mpmath precisions does not pay a rigorous quadrature bound or certify the numerical results as inequalities. The pilot script records this explicit scope.

## 6. Exact controls, rejection tests and decision

The [rational validator](../scripts/validate_dne11_native_source_split.py) checks recurrence (6) against 2sinh*q=z exp(z/2) through order18; it compares two independent rational formulas for the singular polynomial D on monomial degrees0..8 at four rational physical points; verifies the constant polynomial regular convolution primitives; checks the exact 600/1000 Cauchy tail integer inequalities; and verifies the cancellation of pi/2 in (4). The independent exact BigInt replay passes all108 assertions. Analytic derivations (2)--(14) are not numerically proved by those finite controls.

**DNE11 accomplished:** a new exact supported physical source formula (4), a rational polynomial analytic-tail approximant with certified OPERATOR error <3e-41 independent of polynomial degree at N600, a complete finite-1D-integral Gram construction and certified analytic-tail propagation (11)--(14), and a small **real native arithmetic numerical sanity probe** whose signed low pairing matches the inherited exact source. This resolves the previously unspecified infinite archimedean-tail/endpoint source-integration structure.

**Still open:** actual certified interval evaluation of the complete 56x56 (or even the full E112) physical residual source Gram; full original high inverse/form-dual bound; DNE9's true 56-dimensional Feshbach/reflected LMI; full a=53/50 sign; global first contact, RH/F4/transport/Lean.

**DNE12 objective:** implement rigorous interval integration for the finite polynomial-log/panel/exponential source products in (13), including explicit logarithmic endpoint moment payment; start with the normalized e0 scalar pilot as an INTERVAL certificate, then lift to the complete 56-column source Gram after a specified original-Q high Galerkin correction. Compare the native source-aligned residual estimate with NF20's 4x scalar estimator barrier; do not claim whole sign if the coarse norm gate fails.

No other GitHub branch, historical report or theorem numbering is changed by this DNE publication.


## 7. Further exact closure: finite polynomial-log moment bank without exponential quadrature

The full physical source can be reduced still further. All original pole terms are rank-two combinations of exp(±x/2) and their moment functionals. Approximate EACH exponential by its Maclaurin polynomial of degree64:

    e_(±,64)(x)=sum_(k=0)^64 (±x/2)^k/k!,  |x|<=a.

Because a/2=53/100<2/3 and exp(a/2)<2, Taylor's bound gives uniformly

    |exp(±x/2)-e_(±,64)(x)|
       <=2*(2/3)^65/65! =:epsilon_exp.               (15)

The exact integer inequality

    2*2^65*10^100 < 3^65 *65!

proves epsilon_exp<10^-100. Replace exp(±x/2) in BOTH the output profile and the moment functional by the corresponding degree64 polynomial. Each original rank-one pole operator then differs by at most (2a)epsilon_exp(4+epsilon_exp) in physical L² operator norm; summing the two original pole directions gives

    ||R_pole-R_pole,64|| <=4a epsilon_exp(4+epsilon_exp)
                          <3*10^-99.                  (16)

The SAME signed pole geometry is retained: this is a quantitatively paid approximation, not removal of a pole.

Let `s_Q^[600,64](p)` be (1) with the analytic regular kernel replaced by r_600 and both pole exponentials (profiles AND moments) replaced by degree64 polynomials. Original prime translations and prime coefficients are unchanged. By (10) and (16),

    ||s_Q(p)-s_Q^[600,64](p)||_2
       <3*10^-41 ||p||_2                               (17)

for EVERY finite supported polynomial p, independent of polynomial degree and number of high correction modes. Identical error budget holds for the pole-free H source (which has no rank-two pole error at all).

On EACH cell of the finitely many original prime-panel boundaries x=±a±log n, the approximated physical source has the very simple exact shape

    s_Q^[600,64](p)(x)
       =U_p(x) -(1/2)p(x)L_a(x),
    L_a(x)=log(a²-x²),                                 (18)

where U_p is a PIECEWISE POLYNOMIAL. Its coefficients belong to the computable real field generated by rational values, the original log n and Lambda(n)/sqrt(n), gamma_E+log(2pi), and the finite polynomial pole moments. The nonlocal regular integral of r_600 is polynomial as proved above; the truncated pole moments are elementary polynomial integrals. No digamma call, analytic convolution integration, or exponentials remain in this approximate source.

Thus every entry of the approximated complete source squared Gram can be expanded into the following THREE families:

    int_I U_i(x) U_j(x) dx,                            (19a)
    int_I [U_i(x)p_j(x)+p_i(x)U_j(x)] L_a(x) dx,       (19b)
    int_I p_i(x)p_j(x) L_a(x)^2 dx.                    (19c)

(19a) is integrated EXACTLY, panel by panel, by polynomial primitives. For (19b), after cutting at all prime boundaries, each integrand is a polynomial times log(a-x)+log(a+x): substitution t=a±x and the elementary primitive

    int t^m log t dt =
       t^(m+1)[log t/(m+1)-1/(m+1)^2]

give finite closed forms at the panel endpoints. All endpoint limits exist.

Crucially (19c) has NO panel cuts, because the universal singular coefficient is simply -(1/2)p everywhere. Only complete-interval even monomial log-squared moments survive by symmetry. Set

    M_(m,k)(a)=int_-a^a x^(2m) [log(a²-x²)]^k dx.

For k=0,1,2 they have the EXACT generating formula

    M_(m,k)(a)=a^(2m+1)
       [(2log a+partial_beta)^k
                       B(m+1/2,beta)]_(beta=1),       (20)

where B denotes Euler's beta function. Its first two beta derivatives are elementary combinations of digamma/trigamma at half-integers, hence rational harmonic numbers, log2 and pi², so no unresolved improper integration remains. For example,

    M_(0,1)=4a[log(2a)-1],
    M_(0,2)=2a[4(log(2a)-1)^2+4-pi²/3].              (21)

The prime-panel endpoints are exact expressions ±a±log n, with standard outward log enclosures available; no intervals for them have yet been generated in this work. In combination, (17)--(21) turn each finite polynomial native source Gram into a FINITE algebraic/logarithmic/beta-moment expression plus a dimension-independent analytic error below3e-41. A machine-checkable outward interval evaluation of these finite expressions is the remaining calculation.

**Updated stopping decision:** We no longer require a general endpoint improper-integral quadrature engine to evaluate the approximated source Gram. The source-norm calculation is reduced to reusable finite exact MOMENT TABLES and outward rational enclosures for transcendental coefficients and panel endpoints. Those tables have not yet been assembled for all56 corrected columns; no numerical source-Gram or Schur sign is certified by (17) alone.


## 8. Concurrency reconciliation: NF21 completes prime/pole source-square; DNE11 resolves arch source polynomialization

NF21 independently published a [rigorously interval-enclosed original prime-plus-pole SOURCE-SQUARE sector](https://github.com/monocap-tech/weil-lab/blob/research/rpb108-phase-geometry-localization/notes/REFLECTED_PACKET_BRIDGE_108_PHYSICAL_SOURCE_SQUARE_NF21_20261009.md) on normalized e0/e1. It includes prime-prime, pole-pole and SIGNED prime/pole correlations in the true physical L² source, but explicitly excludes the archimedean source and every archimedean cross term. NF21 also gives the exact finite original 58-mode compensated physical residual identity

    P_2=T*D T -S_2^2,                                (22)

where D is the complete original 58x58 source-square Gram, `T=(I,-C_2^-1 B*)` and S_2 is the already certified original signed two-high-mode Schur form. The more stable equivalent is to integrate the COMPENSATED full source, not to subtract two large nearly equal Gram matrices after numerical rounding. DNE11's polynomial-log moment bank is a direct source-side means to calculate every missing archimedean and cross entry of that D, with its own <3e-41 truncation error bound. This is a handoff interface, NOT a duplicated NF21 source-square certificate or an assertion that its full D was computed here.

For the independent ORIGINAL normalized e0 numerical pilot, separate physical source energies are

    ||L_arch e0||²             ≈ 7.08214407559017004439
    ||(L_prime+L_pole)e0||²   ≈ 7.24456598107430401165
    2<L_arch e0,(L_prime+L_pole)e0>
                               ≈ -14.24304822228255869911
    -------------------------------------------------------
    ||L_Q e0||²                ≈ 0.08366183438191535693. (23)

The prime-plus-pole value agrees with NF21's independent exact 1e-12 outward source-sector certificate to its displayed precision, and H/Q low native pairings agree with the older exact NF12 source. This is a useful cross-validation of the sign and physical source normalization. Nevertheless (23) is computed by mpmath quadrature, so its arch/cross terms are NOT INTERVAL CERTIFIED by DNE11. The high F112 projection of e0 has likewise not been computed. The large destructive covariance illustrates why dropping original archimedean/prime/pole correlations makes NF20's crude source estimator ineffective.

CC57 separately proves by an [exact infinite block control](https://github.com/monocap-tech/weil-lab/blob/research/rpb108-coupled-continuation/notes/REFLECTED_PACKET_BRIDGE_108_RESIDUAL_GRAPH_GAP_CC57_20261009.md) that qualitative C-form Galerkin convergence does NOT guarantee decay of the physical source residual, even under compact resolvent, physical source existence and positive complete Schur. DNE11's strong uniform bound (17) is a bound on TRUNCATING the SMOOTH ORIGINAL ACTION KERNEL at a fixed polynomial input, **not** a bound on the native high Galerkin residual as the number of high trial directions tends to infinity. It therefore neither conflicts with CC57 nor cures its graph-norm obstruction. A single chosen source-aligned P_2 interval gate may still work; failure of the scalar physical gate is inconclusive for the true C-form-dual Schur.

**Updated next research decision:** DNE12 can use NF21's actual 58-mode compensated residual identity (22), DNE11's finite moment bank and NF17/NF19's authenticated original native signed matrices. The first stringent checkpoint is to enclose the arch-only squared and arch/(prime+pole) cross terms in (23) by outward rational/interval moments, reproducing NF21's prime-pole e0 sector, BEFORE attempting all58 original source columns. The final sign requires an accurate compensated source, not merely a precise estimate of large unsubtracted source squares. CC57's graph-gap falsifier must be preserved.
