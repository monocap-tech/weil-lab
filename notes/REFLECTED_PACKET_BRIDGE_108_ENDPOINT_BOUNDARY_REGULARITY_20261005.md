# RPB108: actual weak-null boundary regularity and a genuine Gaussian upper bound

Base: 787af35c12cbb98b713e6fe29cd9ae360ddfbcdd.
Definitions: docs/TERMINOLOGY_RPB108_ENDPOINT_BOUNDARY_REGULARITY.md.

## Result

For any fixed a>0, every actual full native weak-null vector h in D_a has a locally L2 full residual representative across both support boundaries, with no boundary-supported distribution defect. Its frozen multiplier action is globally L2, so its squared logarithmic Fourier energy is finite. These properties are derived, without H1 or a physical operator-domain premise.

No nonzero weak-null vector is asserted to exist. The theorem applies also to kernels of indefinite windows, since only the mixed null equation is used. A zero diagonal in an indefinite form, selected-only nullity, or an abstract retained record is insufficient.

## Exact source dictionary

Extend h by zero outside [-a,a]. Write M_pm(h)=integral exp(plus/minus y/2)h(y)dy and p_h(x)=M_-(h)exp(x/2)+M_+(h)exp(-x/2). Outside its support, the already derived actual full native distribution is represented by

    q_h(x)=p_h(x)-integral k(abs(x-y))h(y)dy
            -sum_(log(n)<=2a) Lambda(n)/sqrt(n)
               [h(x-log(n))+h(x+log(n))],
    k(s)=exp(-s/2)/(1-exp(-2s)).

The prime set is the frozen right-limit set, including threshold equalities. Terms are defined almost everywhere; no boundary traces or continuity of the translated L2 vectors are needed. The exterior dictionary is pinned in ACTUAL_EXTERIOR_MOMENT_RIGIDITY_20261005 at the base commit.

## Uniform L2 estimate right up to the edge

For every s>0, exp(2s)-1>=2s, hence

    k(s)=exp(-s/2)[1+1/(exp(2s)-1)]
         <=exp(-s/2)+1/(2s).

At the right edge put x=a+u, y=a-v. The exterior integral is the half-line Hankel operator with kernel k(u+v), applied to h(a-v), extended by zero beyond v=2a. At the left edge the same construction uses h(-a+v).

For the Carleman kernel 1/(u+v), use the positive Schur weight v^(-1/2). Substitution v=u t^2 gives

    integral_0^infinity dv/[(u+v)sqrt(v)]=pi/sqrt(u).

The symmetric weighted integral is the same. Weighted Cauchy-Schwarz followed by Tonelli proves operator norm at most pi. Thus 1/[2(u+v)] has norm at most pi/2. The other kernel exp(-(u+v)/2) is rank one with norm one, since integral_0^infinity exp(-u)du=1.

Domination by the sum gives norm at most pi/2+1<18/7 on either boundary. The two output half-lines are disjoint, so the joint norm squared is at most 2(18/7)^2=648/49<16. Consequently

    ||archimedean exterior(h)||_L2(R minus [-a,a]) <=4||h||_2.

This estimate has no positive distance from the support as a hypothesis. The singular kernel is retained. The finite prime translation operator has norm at most S_a=2 sum Lambda(n)/sqrt(n). Therefore the non-pole exterior core has L2 norm at most (4+S_a)||h||_2 globally outside the support.

## The boundary defect is excluded by the actual dual norm

Let L_h be the tempered frozen multiplier distribution with Fourier transform m_a Fourier(h). The existing envelope |m_a-w|<=C_a gives

    integral |m_a Fourier(h)|^2/w <=(1+C_a)^2 Elog(h)<infinity.

Thus L_h belongs to the whole-line logarithmic dual space. This conclusion needs only the original one-logarithm form membership, not multiplier-domain membership.

Choose a compact smooth chi equal to one on a neighborhood of [-a,a]. The modified distribution T=L_h+chi p_h also belongs to that dual space, because chi p_h is compact smooth. Full weak-nullity makes T zero on the open interior. On the open exterior it equals the known L2 exterior core plus chi p_h. Define r0 to be that exterior L2 function and zero on the interior. The preceding bounds make r0 globally L2.

T-r0 is consequently a distribution supported on the two points {-a,a}, and still belongs to the logarithmic dual space. It must vanish. Here is the exclusion argument, rather than a presumed boundary-removal field: every distribution supported on finitely many points is a finite sum of delta derivatives. Its Fourier transform is a finite exponential polynomial with polynomial coefficients. For a nonzero such polynomial of maximal degree d, integration of its squared modulus over [0,T] is c T^(2d+1)+O(T^(2d)), c>0. Distinct point phases have lower-order cross integrals, by integration by parts. Since w<=log(exp(1)+T) on that interval, its weighted squared integral is at least order T^(2d+1)/log(exp(1)+T), which diverges. No nonzero such distribution belongs to the dual space.

Therefore T=r0. Subtracting chi p_h proves L_h is globally L2. On the support interior L_h=-p_h; outside it is the previously bounded exterior core. With H=||h||_2 and P_a=4a exp(a), Cauchy-Schwarz for the pole moments gives

    ||p_h||_L2([-a,a]) <= P_a H,
    ||L_h||_2 <= B_a H,    B_a=4+S_a+P_a.

Plancherel now derives m_a Fourier(h) in L2. Since w<=abs(m_a)+C_a, it also derives

    integral w^2 |Fourier(h)|^2 <=(B_a+C_a)^2 H^2.

This is the frozen multiplier domain, not the full unrestricted pole operator domain. The pole still grows exponentially on the whole line.

Restoring the full pole yields a genuine residual representative r_h: zero on the interior, the exact native exterior formula outside, and no delta terms at the boundary. It is locally L2. Since r_h=L_h+p_h, Cauchy-Schwarz and the pole growth give finite exponential weighted L1 mass for every sigma>1/2. This proves saturated-window residual realization, without creating a larger interval of vanishing.

## Actual Gaussian upper estimate and its limit

For the unchanged moving Gaussian, let beta_R=exp(-(2pi xi-R)^2/R), M_R=integral beta_R|Fourier(h)|^2, and g_R=K_R*h. Then ||g_R||_2<=sqrt(M_R).

The L2 multiplier action and the exact whole-line Gaussian pole identity give a well-defined actual action with

    |A_a(h;conjugate(g_R))|
      <=B_a H sqrt(M_R)+P_a exp(-R+1/(4R))H^2.

All integrals genuinely converge: the core uses L2 pairing, and the pole uses the already proved Gaussian weighted integrability. This is a derived upper estimate for the same physical h.

There is also a sharper separate whole-line prime bound. With f_R=Fourier_inverse(sqrt(beta_R)Fourier(h)), the weighted prime correlations are the translations of this same f_R. Cauchy-Schwarz bounds the full prime Gaussian action by S_a||f_R||_2^2=S_a M_R. This bound concerns the whole-line pairing; a spatial collar split cannot discard individual interior prime or pole terms, because endpoint nullity cancels their sum with the archimedean term.

Combine the new upper bound with the existing lower estimate. For lambda_R=log(R)-C'_a>0 and

    e_R=D_a(1+log(R))exp(-R/4)+P_a exp(-R+1/(4R)),

put x=sqrt(M_R)/H when H>0. The quadratic inequality lambda_R x^2<=B_a x+e_R gives

    x<=B_a/lambda_R+sqrt(e_R/lambda_R),
    M_R <=[2 B_a^2/lambda_R^2+2e_R/lambda_R]H^2.

Thus Gaussian mass is O((log R)^(-2)), with exponentially small additive errors. This does not yield exponential mass decay or the signed exponential collar upper estimate. The one-sided Gaussian obstruction forbids the latter, not this logarithmic suppression.

The prior collar partition remains valid, now with an actual locally L2 residual up to the boundary. The remaining independent issue is a stronger signed estimate on its boundary interaction. The old strict-gap residual interface still requires carrier support strictly inside the vanishing interval; this theorem only gives vanishing on the vector's own open support window.

## Validation and standing

The rational constant/control certificate reproduces byte for byte. It verifies the pi ceiling, each-boundary Schur budget, joint squared budget 648/49<16, interval kernel checks at seven displacements, and rejection of a control that drops the singular term. These checks validate constants; the universal Schur and boundary-distribution arguments above are analytic proofs and are not claimed to be mechanically or Lean checked.

Pinned inputs: ACTUAL_EXTERIOR_MOMENT_RIGIDITY_20261005, ACTUAL_NATIVE_LOG_BOUNDS_20261004, ACTUAL_MOVING_GAUSSIAN_COERCIVITY_20261004, GAUSSIAN_FAR_FIELD_BOUNDARY_COLLAR_20261004 and ENDPOINT_BRIDGE_AUDIT_20261005, at the base commit. Historical notes remain immutable.

The numerical aperture frontier remains 81/100. No actual endpoint, negative witness, enlarged same-vector weak-null persistence, exponential upper theorem or RH conclusion is asserted. Retained selected-witness attachment, global endpoint exclusion, F4 entry and FULL TRANSPORT CLOSED remain open. Lean, axioms and CI unchanged.
