# RPB108: exact Green inverse eliminates the inactive contact branch

Date: 2026-10-07 UTC. Recovered live head 4a2952ae9a25e6c1bf2d972b03f15bec322678fd.
Definitions: [pole Green null attachment](../docs/TERMINOLOGY_RPB108_POLE_GREEN_NULL_ATTACHMENT.md).
Category: actual full-native analytic branch closure. Not Lean-certified.

## The theorem

At a nonnegative unshifted actual contact, let K be the finite full-native kernel, with its proved derivative flags F_j and r=dim K. Then

    L_p:F_2 -> Z=K intersect ker C intersect ker S

is a bijection, whose inverse is the full-line exponential Green operator J_p. Consequently, if K!=0, its pole moments are active and have rank min(2,r). The wholly pole-invisible contact branch is impossible.

The result uses the EXACT mixed-null equation against a newly constructed lawful canonical test. It does not identify a historical retained packet or deduce a bounded signed sharp head. It improves NF40's forward injection to an actual inverse attachment, and discharges the inactive branch left conditional in NF40-NF42. Historical statements and controls are preserved.

## 1. A support condition that is exactly two pole moments

For any canonical h supported in [-a,a], set

    u(x)=-integral exp(-|x-y|/2)h(y)dy.

The derivative jump of -exp(-|x|/2) is +1, so (D^2-1/4)u=h in global distributions. In angular Fourier frequency,

    u_hat(eta)=-h_hat(eta)/(eta^2+1/4).

This is the unique full-line L2 inverse: the denominator has no real root. Outside the window the exact formulas are

    u(x)=-exp(-x/2)(C(h)+S(h)), x>a;
    u(x)=-exp(x/2)(C(h)-S(h)), x<-a.

Thus u has the same compact window precisely when C(h)=S(h)=0. Neither a cutoff nor a dilation is used. Its Fourier multiplier gives u, Du, D^2u canonical and u globally H2; indeed the logarithmic form weight times (1+eta^4)|u_hat|^2 is bounded by a constant times the form weight times |h_hat|^2. The canonical domain is the fixed-support logarithmic domain already proved for the full native form. In particular all three vectors are legitimate tests and have no boundary delta. These statements require no endpoint regularity assumption on h.

## 2. Complete native integration by parts

For this u, every part of Q satisfies

    Q(D^2u,u)=-Q(Du,Du).                         (1)

The archimedean Fourier term has identical integrand on both sides, with absolute convergence supplied by the weighted H2 bound. Every frozen actual prime translation commutes with global D; integration by parts on the zero extensions gives (1) for its correlation and scalar terms individually. All actual prime terms at the fixed window are retained.

For the pole contribution Q_P=2 C(.) overline(C(.))-2 S(.) overline(S(.)), global integration by parts gives

    C(Du)=-S(u)/2, S(Du)=-C(u)/2,
    C(D^2u)=C(u)/4, S(D^2u)=S(u)/4.

Therefore Q_P(D^2u,u)=Q_P(u,u)/4=-Q_P(Du,Du), proving (1) also for the indefinite pole rows. This is why treating H alone, or a selected background, would not suffice.

Take h in Z. The EXACT full mixed-null equation tested against this u now gives

    0=Q(h,u)=Q(D^2u,u)-(1/4)Q(u,u)
      =-Q(Du,Du)-(1/4)Q(u,u).                   (2)

Nonnegativity forces BOTH energies to vanish. Cauchy-Schwarz for the nonnegative Hermitian form promotes each zero energy to full mixed nullity against every canonical test. Thus u is in F_2 and Du is in K. No null attachment is assumed in constructing u.

The earlier lawful derivative promotion gives D^2v in K for v in F_2. The moment identities then give L_pv in Z. Uniqueness of the full-line inverse proves the asserted bijection.

## 3. Why the inactive branch is now impossible

The exact derivative-chain theorem gives dim F_2=max(r-2,0). If the two pole moments vanished identically on a nonzero K, then Z=K and (2) would inject all r dimensions into the strictly smaller F_2. This is impossible, including r=1 and r=2.

The existing moment recurrence on the parity chain therefore starts with a nonzero generator moment. It gives rank min(2,r), hence dim Z=max(r-2,0). This closes a branch, not the terminal defect itself. For r>=3 the pole-invisible subspace still has dimension r-2. It remains the excited H-null chain above the simple even negative level described in NF40-NF41, and its nonzero rough endpoint trace survives pole stripping.

NF42's compressed Weyl invisibility remains relevant on this Z for long active chains. Its algebraic inactive determinant scenarios are now excluded at an ACTUAL nonnegative continuum contact. The finite weighted isoweyl examples never had the continuum derivative flags or identity (1); they remain lawful controls for compression alone.

## 4. Attachment in the complete actual source graph

This inverse also has a complete source-coordinate meaning, without replacing physical nullity by coefficient nullity. In each actual pair, let

    T_rho=i theta_rho I+beta_rho swap,
    Gamma(Dv)=-T Gamma(v)

on lawful derivatives. The exact translation convention is Gamma(tau_t v)=exp(tT)Gamma(v), tau_t v(x)=v(x-t). Thus for the actual u just constructed,

    Gamma(u)=(T^2-1/4)^(-1) Gamma(h).             (3)

The paired generator is normal in the positive complete source carrier. With the previously incorporated external strip input |beta_rho|<=3/8,

    |(i theta_rho +/- beta_rho)^2-1/4|
       >= theta_rho^2+7/64.

Hence the inverse source filter is bounded by 64/7, and T^2 times that filter is bounded as well. This is a global algebraic source filter, not an aperture estimate. The improved transverse bound certifies this attachment uniformly; it is not needed for the physical proof (2). Only sufficiency for h in Z is claimed: no general compact source-range converse is silently assumed.

The scalar block inverse by itself does not imply actual compact realization. It is the two physical pole moments that remove both exponential tails; full mixed nullity and Q>=0 then establish actual nullity of that realization.

## 5. Four controls and the missing exclusion

| Control | Audit of the new implication |
|---|---|
| Actual rough positive eigenmode | At its lowest positive level mu, Q_mu=Q-mu L2 is nonnegative. The scalar mass also obeys (1). For h in ker Q_mu with both moments zero, (2) holds with Q_mu and gives a compact inverse in the SAME shifted kernel. Pole activity is therefore forced there too. Nothing eliminates its positive logarithmic slope or sets mu=0. |
| Artificial compact-good-row logarithmic control | Generic auxiliary rows do not obey the pole integration-by-parts identity (1). The new theorem is not inferred from row compactness, tail estimates or density. This control retains its positive slope and is not falsely attached to the actual operator. |
| Fixed finite source restoration | The proof uses the complete actual form and every actual prime term. The existing o(1) change in the normalized sharp head under finite restoration is unchanged; deleting rows does not authorize retaining the complete equation (2). |
| Two-row comparison contact | Its auxiliary null equation contains the extra rows, whose derivative terms must be retained. Their matrix does not become the prescribed pole correction merely by being rank two. No actual full-native inverse-null or endpoint exclusion is transferred. |

The inverse attachment is shared by the actual shifted control, so it cannot itself prove the zero-exclusive signed-head theorem. It does exclude the inactive branch using actual physical support, the exact full-null equation and positivity together, whereas each of these alone was insufficient.

No actual bounded-return/oscillation mechanism has been found. The INTERNAL graph shortens: pole-inactive contact is removed and L_p's actual inverse is discharged. The GLOBAL remaining theorem is still signed sharp-head arithmetic on the now necessarily active actual contact kernel:

    liminf_(T->infinity) S_K(T)/log T <= 0.

The proved positive sharp/log limit remains intact. Actual source-range nullity -> bounded/sublogarithmic sharp subsequence is still unproved. No claim of r<=2, all-vector pole visibility, vanishing terminal trace, same-vector enlarged transport, RH, F4, or FULL TRANSPORT CLOSED is made.

## Custody and validation

Inputs at recovered head:

- KERNEL_DERIVATIVE_CHAIN_20261007: e124b8a31a00df61908ce71cedd4ab7f83a14c76.
- POLE_STRIPPED_CHAIN_20261007: 87a296ab96c1888b77c864136279d31b420d6e74.
- POLE_RESONANCE_COMPATIBILITY_20261007: dd12a329fb0ecf518814adfcb2313029af803169.
- POLE_WEYL_INVISIBILITY_20261007: 50cb4bd709953cd799d88d11a57e5b87fc0f49f6.
- SOURCE_HEIGHT_GRAPH_ERROR_20261007: b968aa0a3c5eb5ba680ee0251692e24853dadd74.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: c369d3760606d9e5b9ae0f4862156fd712e5be29.
- ACTUAL_LOG_OPERATOR_ATTACHMENT_20261007: 5b9fedd77956f6ba3e2efc0a71be14f673596fd1.

The companion exact rational checker checks pole integration-by-parts algebra, moment propagation/ranks, the inactive dimension contradiction, active stripping dimensions and the transverse margin. Its manifest separates those finite checks from the analytic domain and mixed-null proof above. No new external theorem or axiom is introduced. Lean is unavailable in the partial local mirror; no Lean certification is asserted. Aperture work is preserved independently.
