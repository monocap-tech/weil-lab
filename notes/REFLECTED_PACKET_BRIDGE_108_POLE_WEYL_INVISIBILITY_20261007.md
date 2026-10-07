# RPB108: the entire pole Weyl family misses actual excited null directions

Date: 2026-10-07 UTC. Recovered newer live head 6e9070c744b5845c1af209bc838e458eb9b61ca6 and current cursor. Concurrent aperture frontier 199/200 is preserved; no aperture work here.
Definitions: [pole Weyl invisibility](../docs/TERMINOLOGY_RPB108_POLE_WEYL_INVISIBILITY.md).
Category: exact actual observation obstruction and outside functional-model audit. Analytic, not Lean-certified.

## Result

Knowing the ENTIRE analytic compressed resolvent M(z) of the two actual pole profiles does not automatically determine full actual native nullity. At a hypothetical nonnegative contact with a negative pole-free eigenvalue, the already proved Z=ker H is orthogonal to its ENTIRE pole-generated resolvent-cyclic subspace. Both H and A vanish on this invisible part.

For an active r>=3 chain, Z carries the proved pole-stripped terminal trace, so this is specifically a conditional actual terminal-defect invisibility theorem. It is stronger than noninjectivity of one averaged inverse-boundary moment. No actual null vector is constructed, and this is not a claim that complete actual zeta source analysis misses Z.

An exact two-point/four-point pair has identical M(z), all its derivatives and visible spectral measures, but full contact nullities 2 and 4. Both retain the exact sampled hyperbolic pole and a strictly positivity-preserving base heat semigroup. Thus even the full pole-resolvent function, rather than just two scalar values, cannot supply a generic terminal-defect exclusion.

## 1. Actual invisibility and the observer distinction

Fix hypothetical unshifted nonnegative actual contact in the negative-H branch. Prior singular compatibility proves ker H=Z and c,s perpendicular to Z. For z0 in Z, resolvent self-adjointness gives for every nonreal w

    <z0,(H-w)^(-1)c>=0, <z0,(H-w)^(-1)s>=0,

since (H-conjugate(w))^(-1)z0=-z0/conjugate(w). Hence Z subset V_pole-perpendicular. It is a reducing subspace: H vanishes there, and P=2|c><c|-2|s><s| annihilates it. Therefore

    H=0_Z plus H_reduced, A=0_Z plus A_reduced.

The same compressed resolvent M would result after removing this subspace. Its spectral measure B^*1_D(H)B has ZERO weight at zero even when Z!=0. Because the nonzero spectrum is separated from zero by compact resolvent, M extends holomorphically through zero on this branch. Its values there are exactly the lawful reduced responses from NF41, not a presumed full H inverse.

For active r>=3, w=(D^2-1/4)h_* is in Z, and its terminal derivative has nonzero kappa_R. Thus the actual chain can hide terminal data from all these pole observations, conditionally on contact. For inactive K, the whole K=Z is hidden. The compressed response measures therefore cannot be assumed cyclic on the entire physical carrier in precisely the cases the global proof must exclude.

This observer is NOT Gamma_a. Actual supported positive observability makes Gamma_a injective, so Gamma_a z0!=0 for nonzero z0. The actual source-support theorem makes that complete packet infinite. Pole-resolvent invisibility neither makes its native p/n coordinates zero nor bounds its signed sharp head. Replacing Gamma by B or by V_pole would lose actual source-range custody.

## 2. What the rank-two determinant counts at zero

In the negative-H branch M is diagonal and holomorphic near zero. Its real derivatives satisfy

    E'(0)=||H_e^#c||_2^2>0, O'(0)=||H_o^#s||_2^2>0.

Thus each critical scalar factor has a simple zero. Let epsilon_e and epsilon_o be the indicators of E(0)=-1/2 and O(0)=1/2. Singular compatibility already gives

    dim ker A=dim Z+epsilon_e+epsilon_o,
    order_0 d_pole=epsilon_e+epsilon_o<=2.

In particular:

- active r>=3: the determinant has order TWO, while full actual nullity is r and its r-2 invisible directions can retain the terminal defect;
- inactive r>=1: d_pole(0) is NONZERO although the full actual kernel has dimension r;
- active r=1 or 2 with H invertible: no invisible base zero modes remain, so the scalar determinant does capture that short-chain nullity, but its permitted resonance remains unexcluded.

This is a precise failure of determinant multiplicity -> absolute native nullity. The determinant measures a finite-rank spectral change; a zero eigenspace already annihilated by the perturbation cancels from that change.

The nonnegative-H singular exception has another cancellation. If H has its simple even zero groundstate and A has an odd one-vector contact, then E(z)=-alpha/z+O(1), alpha=||projection_(ker H)c||^2>0, while 1-2O(z)=-2O'(0)z+O(z^2). Hence d_pole has a NONZERO removable value 4alpha O'(0) at zero. One even base zero is removed and one odd native zero is created; relative multiplicity is zero. This branch is conditional, not claimed to occur for actual zeta. It shows why a meromorphic perturbation determinant must retain its base poles as well as its zeros.

## 3. Exact isoweyl positive-jump controls

In a finite space with inner product sum_i omega_i conjugate(u_i)v_i, take symmetric nodes x_i with c_i=cosh(x_i/2), s_i=sinh(x_i/2). Define

    (P u)_i=sum_j 2cosh((x_i-x_j)/2)omega_j u_j
            =2c_i<c,u>-2s_i<s,u>, H=-P, A=0.

Reflection gives <c,s>=0. All entries of -H are strictly positive, so the power series for exp(-tH) has strictly positive entries for t>0. This is more than abstract positivity preservation. Equivalently H is a symmetric jump generator plus nonnegative killing and a scalar mass shift: choose a constant diagonal large enough for the off-diagonal rates, and put the remainder into killing. No continuum jump or arithmetic divisor is claimed.

Model 2: nodes +/-2log2, weights one. Then

    ||c||^2=25/8, ||s||^2=9/8.

Model 4: nodes +/-2log(3/2) with weight 25/33 each, and +/-2log3 with weight 8/33 each. Their c values are 13/12 and 5/3, and positive-half s values are 5/12 and 4/3. Exact rational calculation gives the SAME norms 25/8 and 9/8, and <c,s>=0.

For either model, c and s are eigenvectors of H with eigenvalues -25/4 and 9/4. All their pole-compressed data are therefore IDENTICAL for every nonreal z:

    M(z)=diag((25/8)/(-25/4-z),(9/8)/(9/4-z)).

This is a rational-function identity, not an agreement at finitely many sample points. Model 2 has ker H=0 and full A-nullity 2. Model 4 has ker H={c,s}-perpendicular of dimension 2 and full A-nullity 4. Both have one simple even negative base eigenvalue, positive odd base eigenvalue, actual sampled hyperbolic P, and simultaneous pole resonances. Their determinants both have order two at zero. All resolvent derivatives and high-energy compressed moments also agree.

These distinct nodes avoid creating extra dimensions merely by counting identical copies. The larger hidden subspace is genuine in the finite physical carrier. The models have no canonical logarithmic continuum domain, derivative filtration or endpoint trace. They refute a pole-Weyl reconstruction/exclusion based only on the listed observation and order properties; the actual conditional theorem in Section 1 supplies the separate link to a terminal chain.

## 4. Named external reconstruction theorem: the missing hypothesis is cyclicity

[Gesztesy-Naboko-Weikard-Zinchenko, arXiv:1506.06324, Theorem 5.6 and Remark 5.7, pp. 23-24](https://arxiv.org/pdf/1506.06324) reconstruct a self-adjoint operator from its compressed spectral measure when the observing subspace generates the entire Hilbert space under the bounded functional calculus; a resolvent-span condition suffices. Their Remark 5.5 describes the invisible reducing part in the Donoghue setting.

For H and N=span{c,s}, self-adjointness, separability and closed finite-dimensional observation hold. The whole-carrier generation condition is NOT proved. Section 1 proves it fails conditionally whenever the actual Z is nonzero. There is no identification of N with a deficiency subspace, so no boundary-triplet or Donoghue simplicity claim is imported. Reconstruction on V_pole is lawful but leaves its orthogonal reducing component undetermined. Herglotz positivity and analytic continuation do not supply the missing generation hypothesis.

The exact smallest extra statement for whole-carrier pole reconstruction would be prescribed actual c/s cyclicity for H. Even proving only zero-level observation injectivity would remove Z and shorten the chain to active r<=2; it would NOT exclude the remaining scalar resonances. Neither statement is proved or substituted for the existing global gate.

## 5. Positive-eigenmode and arithmetic/source audits

Scalar shifts act exactly by M_(H-mu)(z)=M_H(z+mu). If the actual shifted lowest eigenspace has a pole-invisible part, it lies in ker(H-mu) and is invisible at level mu to the SAME pole cyclic subspace. Resonance orientation, Herglotz sign and compressed analytic structure therefore survive the actual positive-eigenmode control, with its eigenvalue retained. In both finite models, H_mu=H+mu I and A_mu=mu I produce identical shifted compressed functions and positive-eigenvalue analogues for any mu>0.

Actual source-range nullity is a different condition: Jsrc Gamma_a h is orthogonal to the actual complete source graph. No theorem here turns that condition into pole cyclicity, determinant nonvanishing or a bounded signed sharp subsequence. The prescribed prime/archimedean operator could add such information, but its complete source observations cannot be replaced by this two-profile resolvent.

Artificial compact-good-row logarithmic controls retain their nonactual source graph. Finite restoration retains the existing o(1) normalized sharp effect but is not a reason to discard an unobserved reducing subspace. The two-row comparison contact still has its auxiliary rows; this calculation never removes them. All four controls remain active.

No actual bounded-return or oscillation mechanism found; the global dependency graph does not shorten. The remaining global theorem is still signed sharp-head arithmetic, and actual unshifted source-range nullity -> bounded/sublogarithmic sharp subsequence remains unproved. The useful research result is the exact boundary of a functional-model transfer: pole Weyl data are a complete model only for their observable reducing component, which can miss an actual terminal defect under the established contact hypotheses. No new equivalent endpoint criterion, regularity investigation, aperture estimate or historical packet attachment is introduced.

## Custody and validation

Pinned inputs at recovered head:

- POLE_RESONANCE_COMPATIBILITY_20261007: dd12a329fb0ecf518814adfcb2313029af803169.
- POLE_STRIPPED_CHAIN_20261007: 87a296ab96c1888b77c864136279d31b420d6e74.
- SOURCE_HEIGHT_GRAPH_ERROR_20261007: b968aa0a3c5eb5ba680ee0251692e24853dadd74.

The rational companion passes 158 assertions verifying both weighted models, their full matrix adjoint laws, hyperbolic pole entries, eigenvectors, kernel dimensions, resolvent compression and scalar shifts. Finite checks are controls, not actual spectral computation or Lean proofs. The analytic actual invisibility, determinant orders and external hypothesis audit are given above. Source pins and results are retained in notes/data/RPB108_POLE_WEYL_INVISIBILITY_20261007.json. Canonical cursor updated additively; concurrent aperture work and historical certificates retained. F4 and FULL TRANSPORT CLOSED remain open.
