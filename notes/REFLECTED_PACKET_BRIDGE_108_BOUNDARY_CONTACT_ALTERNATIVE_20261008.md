# RPB108 — Boundary-saturated contact and a non-covariance continuation alternative

Date: 2026-10-08. Active branch: `research/rpb108-coupled-continuation`. Definitions: [boundary-contact alternative](../docs/TERMINOLOGY_RPB108_BOUNDARY_CONTACT_ALTERNATIVE.md). This is an **analytic deduction / frontier discrimination**, not an all-aperture theorem or a new numerical sign certificate. All CC19–CC39 and external NF handoffs remain intact.

## 1. Decision: distinguish the conclusion from the route

CC19/CC26's complete old-gap-independent shell estimate is sufficient for non-stalling continuation; with its full fixed-cap quantifiers, the uniform exit property is RH-equivalent. It is not a necessary intermediate *proof strategy*. A proof could instead exclude every first zero-energy contact directly from the actual native arithmetic, prove an independent zeta-specific inequality, or certify each finite aperture with a separate complete signed bound. None of these global alternatives is currently established.

The issue is not whether a generic source crossing satisfies stationary identities: CC19, CC28 and CC35 show such structures may cross. A replacement must use arithmetic facts that **do not hold** for those controls. CC25 already shows finite divisor alterations cannot preserve the exact original native identity on an open physical aperture, but this injective local identity determination has no sign estimate and no critical-line reference source.

## 2. A proved endpoint-saturation theorem from CC28

**Theorem (native contact boundary saturation).** Fix a finite a>0 and suppose the complete original Weil form is nonnegative on the canonical supported space D_a. If h in D_a is nonzero and Q_a(h,h)=0, then its essential closed physical support meets both -a and +a. More explicitly, h cannot vanish a.e. throughout **either** endpoint collar (-a,-a+epsilon) or (a-epsilon,a), for any epsilon>0.

**Proof.** A null vector of a nonnegative Hermitian form is orthogonal for that form to every test in D_a: for all f in D_a, Q_a(h,f)=0. Suppose first h vanishes on (-a,-a+epsilon). For every 0<r<epsilon, the left translate tau_{-r}h stays in D_a. Thus Q_a(h,tau_{-r}h)=0. By the exact stationary mixed formula, this is CC28's frozen correlation q_h^a(-r). That correlation is Hermitian: q_h^a(r)=conj(q_h^a(-r)). Hence q_h^a vanishes on a whole neighborhood of zero. It is therefore real analytic at zero. CC28 proved that the frozen native q_h^a is **not** real analytic at zero for any nonzero compact physical vector in the canonical logarithmic domain: the eventually positive log-frequency multiplier forces an exponential Fourier moment if it is analytic, which in turn forces compactly supported h to vanish by holomorphic uniqueness. Contradiction. If h instead vanishes in a collar of +a, translate right by r and repeat. Both endpoints must belong to its essential closed support. QED.

The proof retains the exact archimedean multiplier, every currently active prime translation, both orientations and both signed pole cross terms. It uses no physical operator-domain smoothness, unproved zeta critical covariance, old source gap, or passage to a larger positive aperture. It is a consequence of CC28's analytic nonanalyticity theorem, **not** a new proof of RH.

## 3. Adversarial discrimination

The theorem does **not** exclude contact. In the genuine differential control q_a(h)=int_{-a}^a (|h'|^2-|h|^2) on H_0^1(-a,a), the first contact is a*=pi/2. Its nonzero null h(x)=cos x (on [-pi/2,pi/2], zero outside) reaches both endpoints in essential support. Q_{a*} is nonnegative and Q_{a*}(h,h)=0. Thus endpoint saturation is consistent with an actual first crossing.

The CC28 native nonanalyticity also persists under a finite positive physical-level shift; a shifted positive eigenmode cannot be relabeled an original zero mode. Neither support saturation nor the nonanalyticity argument distinguishes zero-level from the full shifted positive-level control. It only rules out an **interior-localized contact mode**.

A further shortcut also fails: exact finite dictionary rigidity (CC25) implies identification of coefficients from complete mixed data, not positivity of their quadratic form. There is no known critical-line comparator dictionary with the same native form. Functional equation alone cannot be a sign discriminator (Davenport–Heilbronn controls); Euler-product-type multiplicativity alone is also insufficient (Helson zeta functions can have prescribed off-line zeros/poles). The actual prime coefficients, gamma factor, and functional equation must be used jointly; this labels the arithmetic interface, not a proved sign mechanism.

References for the two outside comparison classes: Karatsuba, *On the Zeros of the Davenport–Heilbronn Function Lying on the Critical Line*, Math. USSR Izv. 36 (1991); Andersson, *Mittag-Leffler type theorems for Helson zeta-functions*, arXiv:2408.15713. These are controls only, not models of the unchanged original Riemann zeta explicit formula.

## 4. Alternative route to test, with an explicit stopping rule

**Boundary-contact/virial route (open).** Represent a hypothetical first contact by its exact canonical null equation Q_a(h,f)=0 for **all** f in D_a and the now-proved fact that h reaches both endpoints. Work with the complete *native* signed form (rather than the inverse old-defect source-shell covariance). For admissible dilations U_{s/a}h supported at s<a, compute the complete signed difference

    V_a(h;s)=Q_s(U_{s/a}h,U_{s/a}h)-Q_a(h,h),
    (U_{s/a}h)(x)=sqrt(a/s) h(a*x/s).

At first contact, Q_a(h,h)=0 and every earlier D_s is strictly positive; therefore V_a(h;s)>0 for any nonzero dilate and s<a. A proposed **arithmetic-specific** theorem forcing V_a(h;s)<0 on some inward sequence at any contact null would contradict earliest contact without controlling CC19's old-gap-relative incoming covariance. Such a theorem is *not* currently proved, and merely asserting it is equivalent to another exclusion hypothesis. The high-frequency log energy by itself naturally decreases under *outward* dilation, so there is no a priori favorable sign; the exact prime and pole correlations are indispensable. No differentiability of generalized h under scale is assumed; finite differences are the primary object.

**Hard test for the next pass:** derive an explicit native finite-difference or endpoint-commutator formula on an admissible smooth core, preserve all primes/poles and mixed terms, and test it on (i) genuine differential contact and (ii) the full shifted positive-level control. If it has the same sign in the two controls, or if positivity is imported at the unknown target aperture, stop: it is not an independent arithmetic discriminator. If it differentiates the actual coefficients from the controls, isolate the smallest specific number-theoretic inequality still needed, rather than promoting a conditional identity to a theorem.

A second independent option is to abandon continuous-contact control and keep **direct complete signed certificates at selected caps**. NF10 has a rigorous a=53/50 physical high-mode floor 17/100, and NF11 evaluated eight prime-only low modes; neither is a whole-domain 1.06 sign certificate. The full native/source Gram and corrected Schur sign remain the local next tasks. This is how previous successful fixed-aperture reframings worked, but it does not prove a reusable global continuation theorem.

## 5. Result classification and custody

- **Proved (inherited CC28 + new deduction):** any contact null at a nonnegative original finite cap is boundary-saturated on BOTH endpoints.
- **Proved limitation:** boundary saturation alone does not prevent genuine first contact; a differential countercontrol satisfies it.
- **Unproved:** any favorable native dilation/endpoint sign, old-gap-independent arithmetic suppression, contact exclusion for actual zeta, global non-stalling, RH/F4, retained attachment and Lean closure.
- **Validation:** analytic proof above; no new executable rational or Lean tests. Existing CC39 provenance and check counts are not restated as fresh validation.

This is one alternative target **within Coupled Continuation**, not the launch of a new Global, Aperture or Shadow frontier. Historical reports, branches and numerical certificates are unchanged.
