# RPB108: simple generator zeros, orthogonal division tests, and the jump/Pick audit

2026-10-07. Recovered live branch head 1de1dd269bb1fdca75cbb51f84541499d86180e2. The published global cursor is NF44; the external continuation's real-zero/Pick calculation was not committed. This note reconstructs the steps below directly and derives a scalar Pick identity using differences whose interior jumps cancel.

Definitions: [real-zero division](../docs/TERMINOLOGY_RPB108_REAL_ZERO_DIVISION.md). Inputs: actual full-form derivative skew identity, finite derivative-chain regularity ceiling and physical de Branges attachment in NF44. All assertions about a contact kernel are conditional on existence of that hypothetical actual nonnegative contact. Proofs are analytic, not Lean-certified.

## 1. Every zero of the top generator is simple

NF44 gives only real zeros for Phi. Suppose a real t is a repeated zero. Put X_t=D+it. The compact Volterra inverse gives u_1 and u_2 with

    X_t u_1=h_*,   X_t u_2=u_1,
    F_u1(z)=i Phi(z)/(z-t),
    F_u2(z)=-Phi(z)/(z-t)^2.

Both inverses stay in [-a,a]: Phi(t)=Phi'(t)=0 supplies the two right-endpoint matching conditions. There are no endpoint deltas. On a bounded interval the Volterra map is L2-bounded; away from a bounded frequency neighborhood its Fourier multiplier gains one derivative. Removable entire quotients control the bounded neighborhood. Thus u_1 is globally H^r with logarithmic weight and u_2 globally H^(r+1) with logarithmic weight. In particular all derivatives used in the next pairing are canonical.

For real t, X_t is Q-skew: Q(X_t u,v)=-Q(u,X_t v). This follows from NF44's derivative identity and sesquilinearity; the two it contributions cancel. Exact full-nullity, tested against u_2, gives

    0=Q(h_*,u_2)=Q(X_t u_1,u_2)=-Q(u_1,u_1).

Nonnegativity implies u_1 in K. But u_1 is a nonzero global H^r vector, whereas K intersect H^r={0}. Contradiction. Hence every zero of Phi is simple. This conclusion concerns the generator, not the actual zeta divisor or arbitrary polynomial multiples in the kernel.

One real division alone does NOT imply nullity: 0=Q(X_t u_t,u_t) is purely imaginary and gives no real-energy conclusion. The second division above is essential.

## 2. Distinct real-zero tests are strictly positive and Q-orthogonal

For a zero t, compact u_t is globally weighted H^r. If Q(u_t,u_t)=0, nonnegativity puts it in K intersect H^r, impossible. Set d_t=Q(u_t,u_t)>0.

For distinct real zeros t,s, test nullity of h_* against u_s and u_t. Hermitian symmetry gives Q(u_t,h_*)=0. Using X_t-skew and X_t u_s=h_*+i(t-s)u_s,

    0=Q(X_t u_t,u_s)
     =-Q(u_t,X_t u_s)
     =i(t-s)Q(u_t,u_s).

Consequently Q(u_t,u_s)=0 for t!=s. This is orthogonality in actual native energy on the division TESTS, not in physical mass on the null kernel.

The complete actual signed source pairing therefore satisfies

    <Gamma u_t, J Gamma u_s> = delta_(t,s) d_t.

Here J is the already registered positive-minus-negative channel involution; actual multiplicity and normalization weights are unchanged. For evaluating each source row use the entire profile i Phi(z)/(z-t), including i Phi'(t) at collision. No vanishing numerator or undefined 0/0 row may be discarded. Absolute pairing convergence follows from canonical-domain membership and bounded complete analysis, not from formal manipulation of an unregularized Cauchy series.

This creates an actual positive orthogonal family inside the complete source range. It does not prove its completeness, identify a zeta interpolation measure, or compare its weighted sharp heads with those of K.

## 3. Spectral level survives the construction

For the actual lowest positive eigenspace apply the same proof to Q_mu=Q-mu mass, which is nonnegative and derivative-skew. Its top generator again has simple real zeros. The division tests obey

    Q_mu(u_t,u_s)=delta_(t,s) d_t^(mu),
    Q(u_t,u_s)=mu <u_t,u_s>_L2+delta_(t,s) d_t^(mu).

Thus distinct zeros give zero actual signed source pairing at unshifted contact, but retain the mu mass pairing for the control. The distinction is exact; no step converts it into a sign on the sharp height-weighted sum. This is a stronger usable interface than diagonal reproducing-kernel positivity, although the required arithmetic implication remains open.

## 4. Single-jump tests are lawful; differentiating them requires a new identity

Choose the jump at interior x=0. For any complex w define, inside [-a,a],

    J_w(x)=exp(-iwx)[integral_(-a)^x exp(iwy)h_*(y)dy
                            -Phi(w) 1_(x>0)],

and extend by zero. Both outer endpoints match. The only jump is -Phi(w) at zero, and globally

    (D+iw)J_w=h_*-Phi(w)delta_0,
    F_Jw(z)=i[Phi(z)-Phi(w)]/(z-w).

The quotient is entire in z and w, with its removable diagonal. Piecewise H1 regularity gives global H^s for every s<1/2, hence the canonical logarithmic domain. Uniform local bounds in w give entire dependence in that domain. Therefore Q(h_*,J_w)=0 is a lawful actual null test, and G(w,v)=Q(J_w,J_v) is a positive semidefinite Hermitian kernel at contact. Its normalized version divided by Phi(w)overline(Phi(v)) is also positive where defined. NF44 already puts all possible denominator zeros on the real axis.

DJ_w contains a delta when Phi(w)!=0. A delta is not a canonical logarithmic-domain vector, so direct use of derivative skew on J_w is unlawful. There is, however, an exact cancellation that avoids every delta pairing.

For nonreal w, NF44 gives Phi(w)!=0. Normalize k_w=J_w/Phi(w). All k_w have the SAME jump -1. Therefore k_w-k_v is globally supported H1 and its derivative is canonical, since

    D(k_w-k_v)=-iw k_w+iv k_v
                       +h_*[1/Phi(w)-1/Phi(v)].

Local uniform logarithmic-domain bounds justify this identity and its use in the full form. The h_* terms vanish in every pairing by exact full nullity. Apply derivative skew to k_w-k_v and k_x-k_y. For H(w,x)=Q(k_w,k_x), obtain the four-point identity

    (w-bar x)H(w,x)-(w-bar y)H(w,y)
       -(v-bar x)H(v,x)+(v-bar y)H(v,y)=0.       (1)

No Q(delta_0,.) term is used or defined. Put F(w,x)=(w-bar x)H(w,x), fix one nonreal base w0 (for example i), and define

    M(w)=F(w,w0)-F(w0,w0)/2.

Hermitian symmetry gives F(w,x)=-overline(F(x,w)) and F(w0,w0) is purely imaginary. Equation (1) now yields

    M(w)-overline(M(x))=F(w,x),
    H(w,x)=[M(w)-overline(M(x))]/(w-bar x).     (2)

The removable diagonal is interpreted by the identity. Entire form-valued dependence of J_w, and absence of nonreal zeros of Phi, make M holomorphic on the upper half-plane. Moreover

    Im M(w)=(Im w)Q(k_w,k_w)>=0.

Thus the normalized jump Gram is an ACTUAL scalar Pick kernel, with all domain hypotheses supplied by the jump-cancelled differences. Choosing another base changes M by a real constant only. This closes the unfinished analytic attachment without importing a point-source evaluation theorem.

The model also has exact real spectral atoms. Since Phi has simple real zeros and J_w is entire in the form domain, M extends meromorphically across the real axis with at most simple poles at those zeros. Formula (2), using x=bar w, gives M(bar w)=overline(M(w)). Near a generator zero t,

    k_(t+iy)=u_t/[Phi'(t)iy]+O_D(1),
    y Im M(t+iy) -> d_t/|Phi'(t)|^2 > 0.

Consequently

    Res_(w=t) M(w)=-d_t/|Phi'(t)|^2.

Every generator zero is therefore a genuine real Pick pole with a strictly positive atom weight d_t/|Phi'(t)|^2. These are nodes of the division model, NOT an identification of its pole set with the actual zeta divisor. No infinite partial-fraction expansion or completeness claim is needed for the local residue statement.

For the shifted control replace Q by Q_mu throughout. Its h_* terms vanish only in Q_mu, and its Pick Gram is

    H_mu(w,x)=Q(k_w,k_x)-mu<k_w,k_x>_L2.

The mass correction cannot be dropped when comparing its actual source sum with that of an unshifted null kernel.

## 5. Actual divided-difference observations remove the source poles

The exact actual source profile of k_w is

    F_kw(z)=i[Phi(z)/Phi(w)-1]/(z-w).             (3)

At ANY fixed nonreal actual source point z_rho, Phi(z_rho)!=0. As w approaches z_rho the value in (3) tends to i Phi'(z_rho)/Phi(z_rho); the apparent pole is removable. The same holds at the reflected point bar z_rho. This is an individual-row algebraic cancellation before summing the complete source pairing. Holomorphy of the complete pairing follows independently from bounded source analysis and form-valued dependence; no unproved interchange of an infinite meromorphic series is needed.

The raw term i Phi(z)/[Phi(w)(z-w)] and its correction -i/(z-w) each have a pole at w=z, but their residues cancel. Thus the actual Pick function in (2) is holomorphic at nonreal source nodes precisely because the lawful jump correction is retained. Its positivity cannot be used to declare those nodes real. This is a concrete actual-source obstruction, stronger than merely observing that Gram positivity is off diagonal.

An exact algebraic control also makes the inference failure explicit. Take alpha=1+i/4 and its conjugate, inside the existing transverse strip, and put

    R(w)=1/(alpha-w)+1/(bar alpha-w),
    C(w)=w-R(w),   M_control(w)=R(w)+C(w)=w.

M_control has positive scalar Pick kernel identically 1. Its source term R has two nonreal poles and C cancels their principal parts exactly. The pair has nonzero height 1 and is not a critical-line collision. This is an algebraic inference countercontrol, NOT an actual zeta source-range contact. No assumption that the actual correction equals this artificial C is made. Equation (3) supplies the actual cancellation; the rational control audits the same proposed pole-location inference separately.

## 6. Required controls and next interface

| Control | Exact scope |
|---|---|
| Actual rough positive eigenmode | All division and jump Gram statements hold for Q_mu; actual source pairings retain mu mass. It still has positive sharp/log slope. |
| Compact-good-row logarithmic control | Does not automatically satisfy full derivative skew or Volterra null attachment. Its positive slope still rejects any sign inference based only on positive Gram/compactness or corrected Pick positivity. |
| Fixed finite restoration | A fixed finite head change is O(1) and cannot change the logarithmic coefficient. Full-form identities here cannot be kept after changing the form without rechecking them. |
| Two-row comparison contact | Generic auxiliary rows need not satisfy derivative skew. No actual simple-zero or interpolation attachment is inferred for that comparison. |
| Corrected conjugate-pole control | A genuine positive Pick kernel can coexist with nonreal source poles when its correction cancels them. It audits precisely the proposed analytic inference. |

The internal graph advances: simple real generator zeros and strictly positive, mutually Q-orthogonal compact division tests are attached to the actual source range. Their normalized energies give the exact positive real pole weights of the attached Pick model. The jump tests also have lawful full mixed-null/source custody. The scalar Pick reconstruction is now proved using lawful differences. No individual delta pairing is defined or needed. Completeness of the real-zero division family and an arithmetic sign consequence are not proved here.

The next useful interface is the organization of the real-zero division family inside the complete actual source range: completeness, a lawful biorthogonal relation, or a relation to the height multiplier could constrain the terminal direction. The present Pick attachment supplies the analytic model but its corrected holomorphy does not itself supply that constraint. The shifted positive eigenmode retains the exact mass term as the comparison equation.

No bounded-return mechanism is obtained. Actual unshifted source-range nullity -> bounded/sublogarithmic sharp subsequence remains UNPROVED. The signed sharp/log arithmetic gate, endpoint exclusion and F4 remain open. Aperture 0.9975 custody and direct a=1 work are preserved.

## Validation

The companion checker verifies the skew-shift/repeated-division algebra, four-point reconstruction, removable Cauchy quotients, spectral mass term and exact nonreal-pole cancellation. Finite algebra checks do not certify the analytic Sobolev/domain arguments above. No Lean proof or project axiom is added. Dependencies are pinned by remote blob SHA in the companion manifest before publication.
