# RPB108: the projected fractional null test leaves the entire boundary target

Date: 2026-10-07 UTC. Recovered d00cd66c764cbe9bf25bb27ccce3be6b93772b56.
Definitions: [projected fractional translation registry](../docs/TERMINOLOGY_RPB108_PROJECTED_FRACTIONAL_NULL_TEST.md).
Category: endpoint exclusion. Direct attempted use of the exact zero equation.

## Attempt and lawful fixed-cutoff construction

Fix h in the actual full-native K_a and choose the same t0 and matching enlarged support b used in the signed source cutoff note. For 0<epsilon<t0 define

    L_(epsilon,r)h=integral_epsilon^t0 (h-tau_t h)t^(-1-r)dt,
    v_(epsilon,r)=P_a L_(epsilon,r)h.

The actual logarithmic bootstrap places h in every finite logarithmic order. Translation is continuous there, and the read support projection is bounded there. At positive epsilon, the integrand has a finite Bochner norm budget. Thus v is in D_a and Lh and its exterior part are lawful enlarged-support tests with the same frozen prime set. In particular full-native nullity gives

    Q_a(h,v_(epsilon,r))=0.

No multiplier domain of an uncut fractional derivative is assumed. Nothing below asserts that these test vectors stay bounded as epsilon tends to zero.

## Exact exterior term and sign

Because P_a h=h,

    b_(epsilon,r)=(I-P_a)L_(epsilon,r)h
                =-integral_epsilon^t0 (I-P_a)tau_t h t^(-1-r)dt.

The full core is globally L2 and the pole is bounded on the compact enlarged support. Hence the exterior pairing is the genuine residual pairing. At every positive epsilon,

    Re Q_b(h,L_(epsilon,r)h)
      =Re Q_a(h,v_(epsilon,r))+Re Q_b(h,b_(epsilon,r))
      =-B_(epsilon,r)(h).

The first term is exactly zero. The second term has the minus sign from h-tau_t h. The source identity F=-E+R then yields

    I_(epsilon,r)(h)
       =-B_(epsilon,r)(h)
          +integral_epsilon^t0 R_h(t)t^(-1-r)dt.

Thus applying the null equation to the support-projected fractional test does not establish a bound for I. It isolates the entire remaining boundary quantity. Replacing Q_b(h,Lh) by Q_a(h,v) drops a generally nonzero exterior pairing. Interior full-nullity alone does not annihilate it.

The transverse remainder integral is already bounded for r<2 by the two derived subcritical source moments. The missing target at r=3/2 is therefore precisely a lower bound along a cutoff sequence for the signed boundary integral B^K, or equivalently the earlier finite-liminf signed source trace. No such bound is derived here.

## Existing absolute estimates do not close the cutoff limit

For any fixed 0<s<1/2 the read actual null theorem gives

    integral_a^(a+t) |r_h(x)|^2 dx <= C_(a,s)t^(2s)||h||_2^2.

The zero-extension h is also in H^s globally. Its mass on the translated boundary source strip satisfies the same concentration exponent. Cauchy-Schwarz gives

    |F_h(t)|<=C'_(a,s)t^(2s)||h||_2^2.

Consequently the available absolute estimate yields only

    |B_(epsilon,r)(h)|
      <=C' ||h||_2^2 (epsilon^(2s-r)-t0^(2s-r))/(r-2s)
      when r>2s.

At r=3/2 every available s<1/2 has r-2s>1/2, so this budget diverges as epsilon tends to zero. For example s=3/8 gives exponent 3/4. Improving the transverse bound from 1/2 to 3/8 changes neither of these physical collar powers.

This is a failure of the available upper bound to establish convergence, not a claim that every particular boundary integral diverges. For an individual H1 null vector it can converge. The whole-kernel contradiction still needs the stated additional signed estimate.

Similarly the crude logarithmic norm bound on L_(epsilon,r)h grows like epsilon^(-r). Fixed-cutoff legality is not uniform cutoff control. A finite-dimensional kernel does not bound an epsilon-dependent family of test operators on that kernel without an independent estimate.

## What the exact zero equation does and does not distinguish

For an actual physical eigenmode satisfying q_h=mu h, the projected interior test instead obeys

    Q(h,v_(epsilon,r))=mu <h,v_(epsilon,r)>_2.

For mu=0 this term is zero, exactly as used above. The exterior part still survives. This identifies the genuine use of zero normalization rather than silently treating a positive eigenmode as full-null.

The projection does not manufacture a same-vector enlarged full-null witness. h is unchanged throughout; translations and the integral are tests. The established strict-margin/nonpersistence results remain intact.

A hypothetical nonzero K forces I^K_(epsilon,r)->+infinity for every 1<r<2 by the preceding promotion/trace theorem. Since the transverse trace remainder remains bounded, it would force B^K_(epsilon,r)->-infinity despite every projected test pairing being zero. This is a conditional consistency check identifying the exact false implication; it does not assert that an actual nonzero zero-kernel exists.

## Smallest remaining theorem

Failed implication: lawful fixed-cutoff support projection + exact full-native mixed-nullity -> uniform signed cutoff source bound. The exterior term is the precise missing term.

The smallest sufficient theorem on this direct-test route remains: at every hypothetical nonnegative actual contact,

    limsup_(epsilon down to 0) B^K_(epsilon,3/2)>-infinity.

The previously proved source comparison makes this equivalent to the finite-liminf signed source criterion. This must be a signed full-residual estimate on the actual zero kernel. A generic absolute collar estimate, a single averaged inverse-boundary scalar, or the disappearance of the interior eigenvalue does not supply it.

## Source custody and validation

Pinned at the recovered head:
- SIGNED_CUTOFF_SOURCE_MOMENT_20261007, blob 52f34cc5c348c7ad5b00058c1208599f531bf4c7: cutoff definitions, bounded transverse remainder and trace criterion.
- EXACT_TRANSLATION_BOUNDARY_FLUX_20261005, blob 432ffd64d6460c65cee106f0b46afdb50d1ec28a: full-null projected test, global core and exterior pairing sign.
- LOGARITHMIC_BOOTSTRAP_20261005, blob c2d087875d8dd85dfcdbd64893923ef51fcf1028: bounded support projection and finite logarithmic domains.
- FRACTIONAL_NULL_REGULARITY_20261005, blob f5dd2cfe71a99cd41fcfd21b01a62c2b17ce89ff: actual full-residual collar bound and source-strip concentration.
- EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007: accepted external transverse input remains unchanged.

Analytic validation: positive-cutoff Bochner legality, matching support/prime custody, exact decomposition, exterior minus sign and power integral are explicit. The existing signed-cutoff and external-flux controls pass as regression controls; no new numerical certificate claims the boundary estimate. No new Lean file/build, axiom audit or CI claim. No aperture marching or historical packet work. Cursor updated additively, 24/25 whole-domain certificate preserved. Endpoint exclusion, critical promotion, F4 and FULL TRANSPORT CLOSED remain unproved.
