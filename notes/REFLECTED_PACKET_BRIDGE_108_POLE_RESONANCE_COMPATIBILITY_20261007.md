# RPB108: singular pole compatibility and the exact short-chain resonances

Date: 2026-10-07 UTC. Recovered 2e379972f2130b9be9c400bf107f0ee3b4da82eb and current cursor.
Definitions: [actual pole resonance compatibility](../docs/TERMINOLOGY_RPB108_POLE_RESONANCE_COMPATIBILITY.md).
Category: actual structural compatibility, with an explicit failed structural exclusion. Analytic, not Lean-certified.

## Result and scope

At any hypothetical nonnegative unshifted actual contact, the complete decomposition A=H+2|c><c|-2|s><s| gives MORE than a negative-index bound:

- s is orthogonal to ker H_o in every case.
- If H has its allowed one negative eigenvalue, c is orthogonal to ker H_e, and the ENTIRE pole-free kernel equals Z. No extra unidentified pole-free zero eigenspace remains.
- In that branch, actual nonnegativity forces E<=-1/2 and O<=1/2. Equalities add exactly one even or odd active pole response to Z, respectively.
- If H>=0, the actual contact kernel is necessarily one-dimensional, odd and pole-active. A possible even zero groundstate of H is removed by the positive pole; it must not be silently inverted.
- An active two-vector actual chain forces H to be invertible, E=-1/2 and O=1/2 simultaneously. An active one-vector chain forces its one parity resonance; a one-vector even chain also forces invertibility of H.

These close singular-range and inverse custody for the short-chain compatibility problem. They do not furnish an arithmetic inequality excluding either resonance. A two-point positive-jump model below permits both equalities and nonnegative contact, so rank, parity and pole-free order alone cannot do that.

## 1. Nonnegativity excludes pole coupling to a zero base mode

The existing actual theorem gives n_-(H)<=1, confined to the even sector. For odd z in ker H, nonnegativity immediately gives

    0<=Q_A(z)=-2|S(z)|^2,

so S(z)=0. This proves s perpendicular to the odd base kernel.

Suppose H has a negative physical eigenfunction e, normalized in mass, with H e=-d e, d>0. It is even. For an even base zero vector z, e and z are physically orthogonal. The determinant of the restriction of Q_A to their span is

    det [[-d+2|C(e)|^2, 2 conjugate(C(e)) C(z)],
         [2 conjugate(C(z)) C(e), 2|C(z)|^2]]
       =-2d|C(z)|^2.

A nonnegative form cannot have that negative determinant. Thus C(z)=0. Reflection splits every base zero vector into its two parity pieces, and both now annihilate P. They belong to K. Conversely z in Z already satisfies H z=A z-P z=0. Therefore

    ker H=Z                                           (1)

in the negative-H branch. This is an actual mixed-form argument on the physical operator domain; it requires no inverse, regularity gain or source deletion.

## 2. Lawful responses and their signs, including singular H

Since H has compact resolvent, zero is isolated from its nonzero spectrum. Its inverse on the kernel orthogonal complement is bounded physical L2 and maps into dom H. The orthogonality just proved places c and s in the appropriate ranges, so H_e x=c and H_o y=s are exact equations for x=H_e^#c and y=H_o^#s.

On the odd complement, H_o is strictly positive. Cauchy-Schwarz after H_o^(1/2) gives

    |S(u)|^2<=O E_H(u), O=<s,H_o^#s>>0.

Testing u=y shows that H_o-2|s><s| is nonnegative exactly when O<=1/2. At equality its additional kernel is span y; at strict inequality it has no additional kernel. The previously identified ker H_o is unchanged because s annihilates it.

For the even complement write H_e=diag(-d,B) on span e plus its positive spectral space, with B bounded below strictly positively. Write c=gamma e+b. Nonnegativity requires gamma!=0 (otherwise e remains negative). Put p=<b,B^(-1)b>. The positive block after the pole is B+2|b><b|. Square completion, or its rank-one inverse, gives the remaining scalar Schur complement

    sigma=-d+2|gamma|^2/(1+2p).

Consequently sigma>=0 exactly when

    E=-|gamma|^2/d+p<=-1/2.                          (2)

The inverse of B+2|b><b| exists on the positive complement; this assertion does not invert the base zero eigenspace. At equality the extra even kernel is span x. At strict inequality no extra even kernel remains. Base zero vectors are unchanged by Section 1. Thus in the negative-H branch the exact orthogonal decomposition is

    K=Z plus [span x if E=-1/2] plus [span y if O=1/2]. (3)

The response vectors are orthogonal to Z by construction, and to each other by parity. Their moment values are C(x)=E, S(y)=O, with the other parity moment zero. Neither response is an arbitrary coefficient vector, a historical selected packet, or a presumed Green lift.

## 3. The nonnegative-H branch, and exact short-chain consequences

If H>=0 and has zero spectrum, zero is its lowest physical eigenvalue. The same strict modulus decrease used in POLE_STRIPPED_CHAIN shows that a real groundstate has one sign and that the ground eigenspace is simple: two nonnegative independent groundstates would have a sign-changing real combination, whose modulus strictly lowers energy. Reflection then makes that groundstate even. Its C moment is nonzero because c>0. The positive even pole removes this zero mode. If H has no zero spectrum, its even part is already strictly positive. In BOTH cases the full even part has no kernel.

The odd H is strictly positive in this branch (an odd zero would contradict the simple even groundstate). The negative odd pole can therefore create at most one zero mode, exactly at O=1/2. Its S moment is nonzero. Thus a nonzero actual K in this branch has r=1, is odd and active. If H has an even zero groundstate, the FULL H remains singular although its odd inverse is lawful. This is the exceptional inverse case that a naive global H^(-1) formula would miss.

Now combine (1)-(3) with the proved actual moment ranks:

| Actual chain | Forced compatibility |
|---|---|
| Active r=1, even | H has one negative eigenvalue; Z=0 implies ker H=0. Full H inverse is lawful; E=-1/2 and O<1/2. |
| Active r=1, odd | O=1/2. If H is negative, E<-1/2 and H is invertible. If H>=0, its even groundstate may be zero, so only the required odd inverse is necessarily lawful. |
| Active r=2 | Both parities occur with active moments. H has one negative eigenvalue; Z=0 and (1) force H invertible. E=-1/2 and O=1/2 simultaneously. |
| Active r>=3 | H has one negative eigenvalue; ker H=Z has dimension r-2, and both scalar resonances hold. The inherited pole-free terminal chain is retained. |
| Inactive r>=1 | The previous strict-modulus argument forces one negative eigenvalue; ker H=K, both response inequalities are strict, and all terminal data lie in the pole-free excited kernel. |

For active r=2 there is also exact derivative attachment of the two actual responses. One response is the regular chain generator and the other is terminal rough. If x is globally H1, then differentiating its interior equation lawfully, using global support and the same operator domain promotion, gives

    D x=(1/2)y.

If y is globally H1 instead, D y=(1/2)x. One can avoid a new promotion argument here: the already proved derivative of the regular vector is in K; moments and the one-dimensional opposite parity space identify its coefficient as 1/2. Both responses cannot be H1, by the existing derivative-endomorphism obstruction. No derivative of the rough response is taken. This records exact physical attachment and its trace custody, not another trace-vanishing criterion.

## 4. Exact positive-jump control permits the double resonance

Take a two-point physical Hilbert space, with reflection exchanging the points, and

    c=(5/4,5/4), s=(-3/4,3/4),
    P=2cc^T-2ss^T=[[2,17/4],[17/4,2]], H=-P, A=0.

These pole entries are the actual hyperbolic formula evaluated at points +/-2log(2): cosh(log2)=5/4 and sinh(log2)=3/4. They are not continuum L2 observations. The base is an exact symmetric positive-jump generator plus scalar mass:

    H=(17/4)[[1,-1],[-1,1]]-(25/4)I.

Its heat semigroup is positivity preserving. It has one simple even eigenvalue -25/4 and one positive odd eigenvalue 9/4. Direct inversion gives

    <c,H^(-1)c>=-1/2, <s,H^(-1)s>=1/2.

Thus both resonances and nonnegative two-dimensional full contact coexist with the rank-two pole and pole-free order structure. Adding positive decoupled sectors preserves this example. Adding a scalar mu>0 to both H and A produces the corresponding positive-eigenvalue comparison at level mu; subtracting mu restores precisely these response equalities.

This control does NOT have a continuum derivative chain, a singular endpoint trace, the logarithmic archimedean multiplier or actual zeta source range. It refutes only the implication one negative even base eigenvalue + positive base semigroup + prescribed rank-two hyperbolic pole + nonnegative full contact -> impossibility of simultaneous pole resonances. The established actual rough positive-eigenmode control separately tests the derivative/endpoint structure.

## 5. Controls, remaining theorem and dependency standing

The actual positive-eigenmode test applies every calculation to A-mu and H-mu, keeping P unchanged. Its response vectors solve (H-mu)x=c and (H-mu)y=s. No zero-level response is identified with these shifted vectors. For the known lowest actual eigenspace, A-mu>=0, so the singular-range and index arguments really do apply to the control at that shifted level.

Artificial compact-good-row logarithmic controls do not have this prescribed correction and cannot be substituted into (1)-(3). Fixed finite source restoration still changes the normalized actual sharp head by o(1); the present decomposition uses the complete native form. Two-row comparison contact has extra rows in its null equation, so none are removed by this pole calculation. All four existing controls remain active.

No actual bounded-return or oscillation mechanism found. The global dependency graph does not shorten. The smallest global exclusion theorem remains actual unshifted full mixed-null source range -> liminf S_K(T)/log(T)<=0, and bounded/sublogarithmic sharp subsequence remains unproved. This pass closes the singular inverse/range attachment inside the new internal compatibility graph; it does not advertise the scalar equalities as a new equivalent endpoint criterion. An exclusion based on these responses must use the prescribed actual prime/archimedean spectrum to rule out the relevant zero-level equality, and must also cover inactive chains. No numerical response values are computed.

## Source custody and validation

Inputs at recovered head:

- POLE_STRIPPED_CHAIN_20261007: 87a296ab96c1888b77c864136279d31b420d6e74.
- NATIVE_ORDER_OBSTRUCTION_20261007: 738289b9df5d11436c79ea72dfbe8e85841904f1.
- KERNEL_DERIVATIVE_CHAIN_20261007: e124b8a31a00df61908ce71cedd4ab7f83a14c76.
- CRITICAL_EIGENMODE_TARGET_20261007: 3354b89638b643d5b21c4c428f069f738ccf59f5.

The companion rational script passes 517 assertions checking the singular-coupling determinant, even and odd Schur signs, resonance nullities and the hyperbolic two-point positive-jump control. Results and input pins are in notes/data/RPB108_POLE_RESONANCE_COMPATIBILITY_20261007.json. It certifies finite algebra only. Physical associated-operator domains, isolated-zero inverses, the strict-modulus groundstate argument and exact chain attachment are analytic arguments above. No external theorem, new regularity result, Lean build, axiom audit, aperture estimate or packet identification is introduced. Historical wording and certificates retained. F4 and FULL TRANSPORT CLOSED remain open.
