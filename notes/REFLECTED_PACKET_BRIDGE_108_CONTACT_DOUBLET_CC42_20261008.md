# RPB108 CC42 — Original Weil contact doublets force same-parity outward negativity

Date: 2026-10-08. Branch `research/rpb108-coupled-continuation`. Parent observed before work `4eb3278fc07caaf118166bb86b7093be3f28c095` (CC41 integration). [Definitions](../docs/TERMINOLOGY_RPB108_CONTACT_DOUBLET_CC42.md). This is an *analytic new consequence* of CC28's actual native stationary nonanalyticity, CC41's supported compact-resolvent realization, and CC40's scalar thresholds. It does NOT exclude contact, prove a new original whole-positive aperture, or establish RH/F4/Lean closure.

## 1. Complete original formula and stationarity

For finite a, the canonical supported Weil form is exactly the CC27 native Q, with archimedean digamma Fourier multiplier, all active prime powers with von Mangoldt coefficients and BOTH physical shift orientations, plus the Hermitian signed pole cross terms. On vectors supported in D_a, the same mixed values are obtained on every D_b, b>=a; newly activated prime translations beyond the maximum old support displacement have zero overlap. Simultaneous real translation of two supported vectors preserves the mixed form whenever both translated supports fit a common cap. This is CC28's exact stationarity, NOT an assumed positivity of any enlarged cap.

The frozen stationary correlation q_h^b(r) constructed in CC28 agrees with Q_b(h,tau_r h) for |r|<b-a whenever h in D_a. CC28 proves q_h^b is NOT real analytic at r=0 for any nonzero compact-supported canonical h: the native archimedean log tail cannot be canceled by finite prime cosine multipliers and the entire pole terms. Its proof uses a positive high-frequency measure and Paley-Wiener uniqueness; no positivity or RH is assumed for q_h^b.

## 2. Theorem A: every isotropic packet opens a negative doublet

**Theorem.** Fix finite 0<a<b and nonzero h in D_a with Q_a(h,h)=0. There exists a physically supported vector v in D_b with Q_b(v,v)<0. In fact there are arbitrarily small nonzero r with both h and tau_r h in D_b such that their form Gram is

    [[0,c(r)],[conj(c(r)),0]],       c(r)=Q_b(h,tau_r h)!=0. (1)

Hence the form Gram has exactly one positive and one negative eigenvalue +/-|c(r)|. Taking z=conj(c(r))/|c(r)| and v=h-z tau_r h gives

    Q_b(v,v)=-2|c(r)|<0,
    ||v||_2<=2||h||_2,
    Q_b(v,v)/||v||_2²<=-|c(r)|/(2||h||_2²).        (2)

The last is a bound for the particular physical Rayleigh quotient, not a calculated spectral eigenvalue.

**Proof.** Support inclusion and exact original native stationarity give Q_b(h,h)=Q_b(tau_r h,tau_r h)=Q_a(h,h)=0. If c(r) vanished for every r in some neighborhood of 0, q_h^b would agree with the identically-zero (therefore analytic) function there, contradicting CC28's nonanalyticity theorem. Take arbitrarily small r with c(r)!=0 and the two-by-two Hermitian form has negative determinant -|c|²; the explicit v gives (2). QED.

No old source inverse gap, critical eigenvector differentiability, sign of the pole-free part, numerical aperture margin, nonnegative target assumption, or bounded physical representation of the full original logarithmic operator has been used.

## 3. Theorem B: same-parity negative witnesses and strict scalar-threshold crossing

Assume additionally h is real with definite physical reflection parity (either even or odd). In the nonnegative-contact scenario a real definite-parity h can always be selected from any nonzero complex null by applying real/imaginary and even/odd projections, since all those symmetries preserve Q and the null space of a nonnegative form.

The native real symmetric translation correlation c(r) is real and even: c(-r)=c(r). Let

    sigma_r h = (tau_r h+tau_(-r) h)/2,            (3)

which lies in D_b and has the SAME parity as h. Its mixed original form is

    Q_b(h,sigma_r h)=c(r)!=0.

Put d=Q_b(sigma_r h,sigma_r h) in R. For every sufficiently small real t opposite to c(r),

    Q_b(h+t sigma_r h)=2t c(r)+t² d<0.           (4)

For an explicit choice t=-c(r)/(1+|d|), (4) is at most -c(r)²/(1+|d|)<0. Thus negative original energy occurs in the very same parity sector as the original null, not just on an unrestricted complex span.

CC40's extended-real constrained thresholds obey the equivalence

    Q_b^even>=0 iff beta_e(b)>=-2,
    Q_b^odd >=0 iff beta_o(b)>=+2,

including their moment-zero channels. Therefore any real even contact null at a forces

    beta_e(b)<-2  for every finite b>a,            (5e)

and any real odd contact null forces

    beta_o(b)<+2  for every finite b>a.           (5o)

These are **strict qualitative threshold violations**, not differentiability or a common lower bound on their size. A zero-moment original contact is included: the negative witness (4), if also zero-moment, can be perturbed by a moment-one trial in the same parity while remaining negative, so the corresponding constrained infimum strictly violates its threshold. No moment nonzero hypothesis is hidden here.

## 4. Corollary: positivity on a larger cap forces strict coercivity on every smaller cap

If Q_b>=0 on the whole supported D_b, then for every a<b and nonzero h in D_a, Q_a(h,h)>0. Otherwise Theorem A would construct negative energy in D_b.

CC41 realizes Q_a by the selfadjoint supported operator L_a=A_a+R_a, with A_a>=I associated with the closed canonical logarithmic form and R_a bounded selfadjoint. The inclusion D_a into physical L2 is compact by finite-band Hilbert-Schmidt control and logarithmic Fourier tails (the inherited CC31 compactness argument). Therefore L_a has compact resolvent and, because Q_a>=0 and has no nonzero null, its physical lowest eigenvalue m_{a,b} is STRICTLY positive and attained.

If r_a>=0 bounds ||R_a||, then Q_a(h)>=m_{a,b}||h||_2² and ||h||_D²<=Q_a(h)+r_a||h||_2². Hence

    Q_a(h)>=m_{a,b}/(m_{a,b}+r_a) ||h||_D²,    (6)

with the r_a=0 case interpreted naturally (positive). The gap depends on the specific a and positive horizon b; neither a computable numerical constant nor a uniform-in-b strict reserve has been established. In particular, (6) is NOT the CC19 non-stalling quantitative exit property.

If Q_a is nonnegative and has nonzero null, Theorem A gives a negative test at EVERY larger finite b; CC41's compact-resolvent property then gives at least one actual negative eigenvalue of L_b. Thus a hypothetical first contact cannot remain neutral, plateau, or immediately recover nonnegativity on a later cap.

## 5. Adversarial controls and exact scope

**Genuine crossing (CC19/CC28):** The differential q_s(h)=||h'||²-||h||² on H_0^1(-s,s) has a contact at s=pi/2 and a boundary-saturated even null cos x. For larger supports q becomes negative, and the old normalized correlation tends to -(2/pi) sin r as the critical aperture is approached. Symmetrized translates give an even negative witness. This control PASSES Theorem B: the theorem is a structural sign-opening result, not an arithmetic-only RH discriminator.

**Positive-level shift:** Replacing original Q by Q-mu||h||² creates different shifted contacts. The shifted operator remains stationary and has the same high logarithmic nonanalytic obstruction to a locally vanishing translate correlation. It also passes the doublet result, but this does not classify any shifted null as an ORIGINAL null.

**Nonstationary/persistent-kernel control:** A general increasing family of nonnegative forms may have a persistent interior null (e.g. an identically zero quadratic form), so strict interior positivity is not a theorem of nested domains or compactness alone. The CC28 native high-frequency nonanalyticity is load-bearing.

Theorems A-B constrain what happens IF an exact native zero-energy vector exists, and quantitatively exhibit a strictly negative signed form doublet. They do not show that no contact exists, bound |c(r)| below in terms of the old defect, or demonstrate a zeta-specific sign advantage over genuine differential crossing. CC40 even/odd contact thresholds and its zero-moment class remain the global RH-strength obstruction.

## 6. Interaction with NF13 and next falsifiable frontier

NF13 certified the full original native E32 on a=53/50 (finite strict lower 10^-22); NF10 certified the complete F112 physical complement on that cap. These separate finite/infinite certificates do not imply whole-domain positivity at53/50. This CC42 theorem provides a conditional tool: **if** a genuine first null were certified at some a, all b>a would be strictly negative in the same real parity; conversely any eventual whole-domain nonnegative cap would automatically imply strict positivity at ALL smaller apertures.

The next direct-null problem is not to differentiate eigenvalues at contact. It is to prove a genuinely original-arithmetic impossibility of its null equation, or a sign inequality forcing Q_a>0 before the doublet can arise, using the precise prime/gamma/pole correlations and treating moment-zero nulls. Theorem B removes flat-contact and parity-switch ambiguities but does not solve that remaining arithmetic question.

## 7. Custody / validation status

This report is an analytic deduction from the earlier CC28 and CC41 theorems plus CC40's exact threshold equivalence. The two-by-two Gram and parity-preserving quadratic algebra are elementary exact identities, not new numerical zeta source measurements. No executable validation, Lean proof or new native full112 matrix is claimed here. Other research branches remain untouched. Whole-domain positive anchor remains a=21/20; RH, global first-contact exclusion, all-cap non-stalling, F4/transport/Lean are open.
