# RPB108: seven-eighths transverse input and exact critical null-flux audit

Date: 2026-10-07 UTC.
Requested checkpoint 0f092bd6a21685dfdf95ff2108ebb784822e5e2c; recovered live head 966bbb59f0156c97be3448f7436db833b4f5f991. The newer subcritical distributional promotion is preserved.
Definitions: [external strip and source-flux registry](../docs/TERMINOLOGY_RPB108_EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX.md).

## External input and source custody

At [openai/math adc7f124](https://github.com/openai/math/tree/adc7f1241b42e322a6451854ab7e4b4c146bf78a), the published declaration in lean/OAI/NumberTheory/DirichletL/Nonvanishing.lean states nonvanishing for (7/8)<Re(s). Its proof delegates to ProbeFinalAssemblyUnconditional.zeta_nonzero, whose read body delegates to zeta_of_certified detector_certified_bands.

The comparator JSON points to this solution module. The sorry in ComparatorChallenges/QuasiRiemannHypothesis.lean is the challenge placeholder, not the solution proof. The configuration permits propext, Quot.sound and Classical.choice and sets enable_nanoda=false. Reading those settings is not an actual #print axioms or kernel replay. The official family scope note lists this formalized result. We accept it here as the external input requested by the user; no local rebuild or full dependency audit is claimed.

Pinned external blobs:
- Nonvanishing.lean: 46c67f4000906b1391a471d6e6396ac0da3c16a5.
- Detector/FinalAssemblyUnconditional.lean: e7c20910424837fb954796e1216f5aa453bbd5da.
- ComparatorChallenges/QuasiRiemannHypothesis.json: acf552468fc23c1a27d685d33983c58c50040542.
- ComparatorChallenges/QuasiRiemannHypothesis.lean: e7d1caf6c579dc9afbf0d2b01f79e5cd2511b028.
- Official family note lean/docs/003.md: cf794e93da2e1a494434153f5b91f2990fe9fd60.

For a nontrivial zero rho with real part sigma, nonvanishing gives sigma<=7/8. The functional equation sends it to another nontrivial zero at 1-rho, hence 1-sigma<=7/8. Thus 1/8<=sigma<=7/8 and

    |beta_rho|=|sigma-1/2|<=3/8.

The magnitude is independent of the sign convention relating beta to sigma-1/2. Functional-equation custody: [NIST DLMF 25.4.3](https://dlmf.nist.gov/25.4#E3), xi(s)=xi(1-s), with its displayed completed-zeta definition. Multiplicities and all actual source copies remain unchanged. Equalities at strip endpoints are allowed.

## Exact use of full-native nullity

Fix actual h in K_a. Choose b>a with the same frozen right-limit prime set and t0<min(1,b-a); such b exists because the next finite prime activation threshold has a positive gap. Translated tests for 0<t<t0 lie in D_b. This is source-pairing custody, not a larger-window null equation.

Let p_q,n_q be the unchanged complete physical source evaluations. The exact pair translation law is

    p_q(tau_t h)=exp(i theta_q t)[cosh(beta_q t)p_q+sinh(beta_q t)n_q],
    n_q(tau_t h)=exp(i theta_q t)[sinh(beta_q t)p_q+cosh(beta_q t)n_q].

Full native source/form equality and the exact boundary-flux attachment therefore give

    F_h(t)=sum_q [cosh(beta_q t)cos(theta_q t)d_q
                         +2 sinh(beta_q t)sin(theta_q t)j_q].

Full native nullity is used both to identify this pairing with the genuine exterior residual flux and to subtract sum d_q=Q(h)=0. Consequently

    F_h(t)=-E_h(t)+R_h(t),

    R_h(t)=sum_q [(cosh(beta_q t)-1)cos(theta_q t)d_q
                         +2 sinh(beta_q t)sin(theta_q t)j_q].

All fixed-t sums converge absolutely by source l2 boundedness. The sign of the cross term uses j=Im(p conjugate(n)); reversing the negative source convention must transform the entire formula consistently.

## Joint transverse remainder is already critically integrable

Take any 0<s<1/2. Existing actual null bootstrap and source/Fourier equivalence give M_(+,s)=sum |theta|^(2s)|p|^2 finite. No critical moment is assumed. Write B=3/8 and V=||p||^2+||n||^2. Elementary inequalities imply

    |cosh(beta t)-1| <= B^2 t^2 exp(Bt)/2,
    |sinh(beta t)| <= B t exp(Bt),
    |sin(theta t)| <= |theta t|^s.

Cauchy-Schwarz, retaining the actual positive-negative cross contribution jointly, gives

    |R_h(t)| <= exp(Bt)[ B^2 t^2 V/2
                     +2B t^(1+s) sqrt(M_(+,s)) ||n|| ].

Hence its critical integral is finite, with the explicit budget

    integral_0^t0 |R_h(t)|/t^2 dt
       <= exp(Bt0)[B^2 V t0/2
                  +(2B/s)t0^s sqrt(M_(+,s))||n||].

This is an actual full-null estimate using complete sources. Relative to B=1/2, the algebraic cosh budget improves by 9/16 and the sinh budget by 3/4, with a smaller exponential factor. However, the SAME critical integrability already held with B=1/2. The improvement changes constants, not the integrability exponent.

Combining with the exact previously proved flux criterion yields the new source-side joint criterion

    h in Xcrit
       iff integral_0^t0 |E_h(t)|/t^2 dt < infinity

for actual full-native null h. The transverse part is no longer a candidate for the missing divergence. The remaining term is the signed ordinate-energy defect, whose phase involves theta and has no small beta coefficient.

## Critical derivative-promotion gate remains unclosed

For h in K_a intersect Xcrit, g=h' satisfies the exact differentiated full-native interior equation and belongs to the critical negative space Zcrit. The newer promotion proof works only in H^-sigma with sigma<1/2. Its support-projection and commutator estimates have geometric budgets involving 1/2-sigma, from the Fourier kernel of the physical support indicator.

That 1/2 is NOT the old transverse bound |beta|<=1/2. Replacing it by 3/8 would change an unrelated integral. The actual quarter-line archimedean multiplier m0, its logarithmic growth, the cutoff-pole exponent 1/2 and the support indicator are unchanged by the external zero location theorem.

The exact zero equation permits joint pairing cancellations but the revised source remainder estimate does not place g in L2 or put inverse tests in the missing critical dual domain. In particular it supplies no estimate on the weighted theta phase, which is the unbounded part of the differentiated source observation. We have not proved K_a intersect Xcrit -> L2 derivative.

A projection control remains decisive against a generic operator substitution: projecting a smooth function with a nonzero endpoint value creates a jump, whose Fourier tail gives infinite critical logarithmic H^(1/2) energy. This is independent of beta. It does not disprove a joint theorem restricted to exact actual zero-null solutions.

## Controls and positive-eigenvalue boundary

Unweighted equality sum d_q=0 does not imply critical signed cancellation. An abstract source control has p_j^2=2^-j at theta_j=2^j, j>=1, and a single negative coordinate of norm one at theta=0, with all transverse parameters bounded by 3/8. Then total positive and negative norms agree, every positive moment of order r<1 is finite, and E(t)=sum 2^-j(1-cos(2^j t))>=0 has infinite critical integral. Tonelli and the high-frequency phase lower bound give this directly. These are abstract norm/phase coordinates; they are NOT asserted to be simultaneous evaluations of a compact physical function at actual zeta zeros. Thus this control refutes only an inference from strip width, norm balance and subcritical moments.

For an actual physical eigenmode q_h=mu h, the frozen spectral flux formula instead contains

    F_h^mu(t)=-D_m(t)+(cosh(t/2)-1)Ppole(h)+mu D_mass(t).

The added term follows by subtracting the interior pairing mu<h,P tau_t h> from the translated full action. For mu=0 it disappears. The generic compact cusp has no native equation at all; the actual positive-eigenvalue control has mu>0. Neither is a counterexample to a theorem using exact zero normalization.

The sharper transverse bound applies to the actual divisor observations of positive eigenmodes too. It therefore cannot by itself distinguish those modes; a new decisive estimate must use the zero equation to control E_h or the critical derivative's exterior/dual pairing. The previously constructed rough positive eigenmode's order-one moment has not been shown finite or infinite. We do not silently supply either outcome.

## Smallest remaining theorems and standing

Category: endpoint exclusion.
- For critical source membership: a zero-null-specific bound integral |E_h(t)|/t^2 finite on the whole hypothetical contact kernel.
- For critical derivative promotion: an exact-zero critical dual/exterior estimate promoting its distributional derivative to L2.
- Alternatively, the newly recovered route needs only a positive-source trace moment of any fixed order r>1, with no separate critical-promotion gate.

The external strip and exact joint remainder do not discharge any of these missing arithmetic estimates. This records failure of the proposed constant substitution and isolates the actual signed term; it does not prove no future argument using quasi-RH can work.

Validation: exact rational source rotation/hyperbolic algebra, strip arithmetic and neutral-tail controls repeat. The infinite-source inequalities, actual dictionary, functional symmetry and external theorem are analytic/imported inputs, not certified by these controls. External proof dependency closure was not rebuilt; local Lean unavailable. No aperture marching or historical packet work. Canonical cursor updated additively, 24/25 certificate preserved. Global endpoint exclusion, F4 and FULL TRANSPORT CLOSED remain unproved.
