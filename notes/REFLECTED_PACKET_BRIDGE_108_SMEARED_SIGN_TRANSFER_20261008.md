# RPB108 NF58: sign transfer needs only bounded-level original eigenvectors

Date: 2026-10-08 UTC. Recovered head 1b5db1dc92717e7e0dcd85341ac1494de97c0b70.
Definitions: [smeared sign transfer](../docs/TERMINOLOGY_RPB108_SMEARED_SIGN_TRANSFER.md).

## Result and remaining arithmetic obligation

At every fixed aperture, original eigenvectors with |mu|<=M satisfy

    |Q_a(h)-Q_(a,delta)(h)|<=epsilon_(a,M,k)(delta)||h||_2²

for every integer k>=1 and 0<delta<=exp(-4). For each fixed k the constants are uniform over these eigenvectors and independent of delta. Consequently their error is O_(a,M,N)(log(1/delta)^(-N)) for every fixed N.

This improves NF57's sharp FULL-domain rate on precisely the vectors needed to detect a nonpositive original level. It does not improve that rate on arbitrary canonical vectors. A separate physical lower bound for the smeared form can now transfer sign with this smaller eigenvector error, even if it is insufficient to dominate the worst full-domain error.

No lower bound for the smeared form is proved here. That is the next decisive arithmetic obligation. Further extension of the moment recurrence alone will not discharge it.

## Uniform logarithmic moments with the original mu term

Let C0 be the established global envelope |m0-w|<=C0, S_a the complete active-prime budget, and P_a^bd=4a exp(a) the standing physical pole norm bound. The full original form gives

    Q_a(h)>=E_log(h)-(C0+S_a+P_a^bd)||h||_2².

Put B_a=C0+S_a+P_a^bd. The original physical operator is bounded below by -B_a and has compact resolvent. Its lowest level is attained. These are existing form/operator facts, not properties assumed for a selected matrix.

For an original eigenvector with |mu|<=M, the interior distribution equation is

    m_a(D)h=mu h-p_h on (-a,a).

The L2 domain-promotion proof extends with this extra interior term: its exterior Carleman estimate is unchanged, and the possible endpoint-supported remainder still lies in H^(-1/4) and vanishes. Thus the global multiplier representative is L2. With m0=m_a+t_a, one may use the conservative bound

    ||m0(D)h||_2 <= (M+4+S_a+P_a^bd)||h||_2.

For clarity, apply the removal argument directly to m0(D)h. Its interior equation has right side mu h+T_a h-p_h, with physical norm at most (M+S_a+P_a^bd)||h||_2. Its archimedean exterior norm is at most 4||h||_2. Combining these interior and exterior representatives gives the displayed conservative bound. There is no enlarged homogeneous equation.

Set L_(a,M,0)=1 and L_(a,M,1)=C0+M+4+S_a+P_a^bd. For k>=1 reuse the PROVED constants A_k,D_k,F_(a,k) from LOGARITHMIC_BOOTSTRAP, with the recurrence

    L_(a,M,k+1)
      =(C0+A_k S_a+D_k+M)L_(a,M,k)+F_(a,k).           (1)

Indeed the actual supported equation and commutator give

    m0(D)h=P T_a h-Pp_h+mu h+[m0(D),P]h,

where P is the support indicator. The four terms are controlled in X_k by the existing cutoff, prime, pole and commutator estimates. The mu term contributes M||h||_(X_k); it is never dropped. The multiplier envelope then supplies X_(k+1). Induction proves ||h||_(X_k)<=L_(a,M,k)||h||_2 for every fixed k. Constants can grow rapidly with k; no power Sobolev or exponential Fourier estimate is inferred.

## Smearing error on those eigenvectors

NF57's exact sinc formula gives an error bounded by

    S_a integral [1-sinc(2pi xi delta)]|hhat(xi)|²dxi.

Write L=log(1/delta). On |xi|<=delta^(-1/2) the bracket is at most (32/3)delta. On its complement the bracket is at most 2, while w(xi)>L/2. The moment estimate therefore gives

    error <=S_a[(32/3)delta+2(2/L)^(2k)L_(a,M,k)²]||h||_2².

This is the registered eigenvector budget. All split integrals are nonnegative. No signed tail cancellation, source realization of a sharp cutoff, or derivative hypothesis is involved.

The smooth modulations proving NF57's FULL-domain lower rate do not contradict this estimate: their ORIGINAL physical Rayleigh values grow like log(1/delta). They are not a family of original eigenvectors in a fixed bounded eigenvalue range.

## A quantitative original sign certificate

Suppose an independent actual calculation proves the FULL smeared-form bound

    Q_(a,delta)(v)>=gamma||v||_2² for every v in D_a,
    gamma>0.                                               (2)

Take M=max(B_a,gamma) and any k>=1. Then the original physical lowest eigenvalue satisfies

    lambda_min(Q_a)>=gamma-epsilon_(a,M,k)(delta).           (3)

Proof: if lambda_min>=gamma, the assertion is immediate. Otherwise its attained unit-mass eigenvector has eigenvalue in [-B_a,gamma), hence absolute value at most M. Apply the proved error bound to that ORIGINAL eigenvector and then (2). This proves (3) without assuming original nonnegativity or contact.

If gamma>epsilon, the original physical lower bound b=gamma-epsilon is positive. The unconditional envelope E_log<=Q_a+B_a mass then yields the canonical bound

    Q_a(h)>=b/(b+B_a) E_log(h).

With the established upper norm of the COMPLETE original positive analysis, this implies strict original source gain below one. No smeared source dictionary or artificial zeta divisor is substituted.

The certificate premise (2) requires all supported vectors, or a complete finite restriction plus a proved complement bound. Trial eigenvalues alone do not suffice. Neither the standing original aperture-one certificate nor the error estimate independently establishes (2) at a new aperture. No such new calculation is claimed.

For an original positive eigenvalue mu, Q_a(h)=mu mass is retained in the comparison. The same moment bounds apply because they use |mu|<=M. They do not identify that vector as an original null mode. A mass shift changes both compared forms explicitly.

## Validation and scope

Finite rational controls check the low/high-frequency budgets and the lowest-level transfer, including a case where a smeared positive form coexists with an original negative form when its error exceeds the margin. The distributional promotion, commutator induction, compact-resolvent argument and Fourier tail bound remain analytic, not Lean certified.

This closes a quantitative sign-transfer interface; the independent smeared-form lower bound remains open. Whole-domain aperture-one, all actual source/pole/threshold custody and concurrent fronts remain preserved. No new aperture, original gain bound, global exclusion, RH, F4 or full transport is claimed.
