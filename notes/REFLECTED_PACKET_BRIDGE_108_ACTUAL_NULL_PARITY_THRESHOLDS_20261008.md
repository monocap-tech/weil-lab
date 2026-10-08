# RPB108 — Actual contact null: parity pole thresholds, F112 control, and native cutoff identity

Date: 2026-10-08. Branch: `research/rpb108-coupled-continuation`. Definitions: [native contact thresholds](../docs/TERMINOLOGY_RPB108_NATIVE_CONTACT_THRESHOLDS.md). Parent custody: latest observed Coupled `ed1eadcc795094b27a6cb7d1ab0f5f3580e3c776`; NF12 source remains read-only on `research/rpb108-phase-geometry-localization`. **Result class:** analytic reductions and a new inherited-certificate corollary, not RH, full 1.06 positivity, or a proved global contact exclusion.

## 1. The ACTUAL homogeneous contact equation

For each finite a use the original complete native formula of CC27, with h extended as zero off [-a,a]. Write `ell_n=log n`, `c_n=Lambda(n)/sqrt(n)`, `m_±(h)=int h(x)exp(±x/2)dx`, and let A_arch be the Fourier multiplier `Re psi(1/4+i pi xi)-log pi`. The native original form is

    Q_a(h,f)=<h,A_arch f>
       -sum_(ell_n<=2a) c_n <h, tau_{+ell_n}f + tau_{-ell_n}f>
       +conj(m_-(h))m_+(f)+conj(m_+(h))m_-(f).

The sum includes every active prime power and both orientations. If Q_a>=0 on the full canonical supported D_a and h!=0 has Q_a(h,h)=0, form Cauchy--Schwarz forces Q_a(h,f)=0 for ALL f in D_a. Thus, as a distribution on (-a,a),

    A_arch h(x) -sum c_n[h(x+ell_n)+h(x-ell_n)]
       +m_-(h)exp(x/2)+m_+(h)exp(-x/2)=0.        (1)

Do NOT infer a physical L2 full-operator domain or pointwise values from (1). CC28 plus the contact nullity also imply the essential closed support of h reaches both endpoints (prior separate report).

Reflection and real conjugation commute with Q. If some complex null exists, its nonzero even/odd and real/imaginary components are themselves null because the form is nonnegative. Hence one can choose a REAL definite-parity null.

## 2. Exact pole rank-one split

Define H_a = Q_a minus BOTH original pole cross terms (archimedean + all prime translations). On real even/odd supported vectors set

    c(h)=int h(x)cosh(x/2)dx,   s(h)=int h(x)sinh(x/2)dx.

The original signed pole is +2 c(h)^2 on even and -2 s(h)^2 on odd. Therefore

    Q_a^+(h)=H_a^+(h)+2 c(h)^2,
    Q_a^-(h)=H_a^-(h)-2 s(h)^2.                (2)

No approximating pole rank, arbitrary mass shift, or source truncation occurs. Equation (1) is equivalently, on real parity vectors,

    EVEN: A_arch h -sum c_n(shifts h)+2 c(h)cosh(x/2)=0,
    ODD:  A_arch h -sum c_n(shifts h)-2 s(h)sinh(x/2)=0.  (3)

For a null h and all f in the same parity:

    EVEN H_a(h,f)=-2 c(h)c(f),
    ODD  H_a(h,f)=+2 s(h)s(f).                (4)

In particular the pole-free mixed functional H_a(h,f) vanishes for EVERY moment-zero trial f. A moment-zero null satisfies H_a(h,f)=0 on all tests, so it is a separate, non-deletable zero-moment channel.

## 3. Two monotone extended-real scalar contact thresholds

On nonempty real parity moment-one affine spaces define

    beta_e(a)=inf {H_a(h): h even in D_a, c(h)=1},
    beta_o(a)=inf {H_a(h): h odd  in D_a, s(h)=1}.          (5)

Allow -infinity and do not assume minimizer/invertibility. For m(h)!=0 scale h to m(h)=1. Formula (2) proves

    Q_a >=0 on entire D_a
       <=> beta_e(a)>=-2 and beta_o(a)>=+2.    (6)

Why (6) also includes zero-moment directions: if a moment-zero k had Q_a(k)<0, take any u with moment one. The affine family u+t k has fixed moment one and Q_a(u+t k)->-infinity, violating its scalar threshold. Equivalently take small-moment approximants to k and continuity. The reverse implication of (6) on nonzero moments follows by homogeneity. This is an **exact equivalent reformulation** of the original positivity problem, not a new estimate establishing its truth.

The original native form is support-compatible: on any h supported in D_a, every newly activated prime translation with ell_n>2a has zero self or mixed overlap, even when the larger cap includes it. Thus H_b restricted D_a equals H_a for b>=a. The moment functionals are unchanged under inclusion. Therefore

    beta_e(b)<=beta_e(a), beta_o(b)<=beta_o(a), b>=a.   (7)

If Q_a>=0 and a null h of definite parity has NONZERO moment, then h/m(h) attains beta_e=-2 (even) or beta_o=+2 (odd). It is a global constrained minimizer and obeys (4). If its moment is ZERO, it solves the pole-free homogeneous equation, and beta might remain strictly on the positive side of the threshold. This exception is real: e.g. H=diag(0,-1), moment(x)=x_2, Q_even=diag(0,1), has zero-moment null e_1 while beta_even=-1>-2. Likewise H=diag(0,3), Q_odd=diag(0,1), beta_odd=3>2. Do not declare scalar threshold saturation for a zero-moment null without another argument.

A minimal complete contact classification now has THREE cases: (i) even pole-moment threshold -2 reached and attained; (ii) odd threshold +2 reached and attained; (iii) a zero-moment pole-free null. Cases can coexist. For global proof one must prove strict inequalities beta_e>-2 and beta_o>2 (and then zero-moment nullity is automatically excluded if a physical coercivity reserve is also derived); merely weak inequalities prove nonnegative Q, which is the compact-test Weil criterion once all caps are covered.

## 4. New concrete F112 pole-free control from NF10, at a=53/50

Read-only NF10 certified on F112, the physical L2-orthogonal complement of normalized Legendre polynomials of degree0..111 on [-a,a], for a=53/50:

    Q_a(h)>=17/100 ||h||_2²  for h in F112.   (8)

ODD: H_a^-(h)=Q_a^-(h)+2s(h)^2>=17/100||h||².

EVEN: since h in F112 is orthogonal to all degree<=111 polynomials, choose the degree110 Taylor polynomial p_110(x)=sum_(k=0)^55 (x/2)^(2k)/(2k)! of cosh(x/2). Taylor's theorem on [-a,a] gives

    ||cosh(x/2)-p_110(x)||_infty <= exp(a/2)(a/2)^112/112!.

Thus |c(h)|² <= 2a exp(a) (a/2)^224/(112!)² ||h||_2². Combining with (8),

    H_a^+(h)>= [17/100
       -4a exp(a)(a/2)^224/(112!)²] ||h||_2².           (9)

At a=53/50<2, exp(a)<8, a/2<1, 112!>=2^111. So the subtraction is <2^-216<1/100 and

    H_a^+(h)>=4/25 ||h||_2²,    H_a^-(h)>=17/100 ||h||_2²
    on the corresponding parities of F112.                (10)

This is an evaluated **actual pole-free infinite-complement positivity consequence** of NF10, with no fresh 112x112 source Gram and no old-gap denominator. It does NOT give whole-domain positivity or the finite 112-mode Schur coupling for H_a. On the full F112 (both parities), H_a>=4/25 physical mass.

## 5. NF12 test on the ACTUAL complete four-mode matrix

The external read-only [NF12 exact signed low4 certificate](https://github.com/monocap-tech/weil-lab/blob/research/rpb108-phase-geometry-localization/notes/data/RPB108_NF12_FULL_NATIVE_LOW4_106_CERTIFICATE_20261008.json) has exact rational original arch, prime and pole intervals (grid 10^25). Subtracting only the pole gives these pole-free low2 parity restrictions at a=53/50 (numbers rounded for display):

    H_even degrees(0,2) = [[-4.612024518, -0.103377064],
                           [-0.103377064, 0.181161845]];
    H_odd  degrees(1,3) = [[ 0.563865294,  0.231489278],
                           [ 0.231489278, 0.362688537]].

The EVEN determinant is about -0.84620969: exactly one positive and one negative mode. The ODD determinant is about +0.15092019 with positive diagonal: both modes positive. Strict determinant signs follow directly from the stored rational enclosure endpoints, not only these decimals. The negative even pole-free mode is not a negative ORIGINAL Q direction: NF12's original +2cosh pole corrects it, and its original low16 Q is positive. This is precisely the rank-one stabilization architecture anticipated by (2).

As simple one-mode upper bounds on the infinite-dimensional scalar infima, NF12's native degree0 gives beta_e<=-1.98273837 (threshold -2), and native degree1 gives beta_o<=+2.68600896 (threshold +2). These are **upper bounds, not positive lower certificates** for beta; they do not imply a positive global scalar margin or a near-contact eigenfunction. NF12's low16 finite positivity and NF10's high complement remain separate until full mixed sign is enclosed.

## 6. Exact native IMS / cutoff null identity

The full off-diagonal CONTINUOUS kernel from CC27 (not the full diagonal singular distribution) is

    K_cont(d)=2cosh(d/2)- exp(-|d|/2)/(1-exp(-2|d|)), d!=0,

plus atoms -c_n at d=+/-ell_n. Let real smooth bounded phi, with bounded derivative. Multiplication preserves D_a. At a nonnegative contact, Q_a(h,phi² h)=0. Subtract and symmetrize the two native forms; any local diagonal terms disappear because (phi(x)-phi(y))²=0 on the diagonal. The remaining logarithmic kernel has near-diagonal 1/|d| singularity, tamed by the quadratic multiplier difference. This yields the exact finite double integral

    Q_a(phi h) =
      (1/2) int int Re(conj(h(x))h(y)) [phi(x)-phi(y)]²
        [exp(-|x-y|/2)/(1-exp(-2|x-y|)) - 2cosh((x-y)/2)] dx dy
      +sum_(ell_n<=2a) c_n int Re(conj(h(x))h(x+ell_n))
                               [phi(x+ell_n)-phi(x)]² dx.  (11)

Functions are zero extended; all spatial integrals extend over R where meaningful. For d~0 the bracket is O(1/|d|), the cutoff difference is O(d²), and the resulting O(|d|) kernel is integrable against L2 pairings. Core approximation extends (11) to null h in the canonical log form domain; no operator-domain source regularity is assumed.

Since Q_a>=0, the RIGHT SIDE of (11) is nonnegative for every admissible real phi. For phi(x)=x (bounded on supported interval, use a bounded smooth extension off it) this gives the exact necessary original weighted correlation inequality

    0 <= (1/2) int int Re(conj(h(x))h(y)) (x-y)²
                 [exp(-|x-y|/2)/(1-exp(-2|x-y|))-2cosh((x-y)/2)] dx dy
          +sum_n c_n ell_n² Re int conj(h(x))h(x+ell_n) dx. (12)

This uses ACTUAL arithmetic kernel and nullity, with no inverse old source defect and no differentiability of h under dilation. It is a necessary condition, **not** a strict contradictory sign; a genuine differential first-contact also obeys its own IMS identity Q(xh)=int|h|²>0.

The continuous K_cont changes sign at the positive root of exp(3d)-exp(d)-1=0, between log(13/10) and log(4/3). It is negative near diagonal and positive beyond the root; the additional negative prime atoms live at log n>=log2, beyond that sign-change. Thus a globally positive-kernel or Perron--Frobenius argument is NOT licensed for the actual whole form merely by borrowing results for the pure logarithmic Laplacian. Compare Chen--Weth, *The Dirichlet Problem for the Logarithmic Laplacian*, https://arxiv.org/abs/1710.03416, and Hernández-Santamaría et al., *Optimal boundary regularity and a Hopf-type lemma*, https://doi.org/10.3934/dcds.2024084. Their favorable-kernel theorems require hypotheses that the signed complete native kernel does not satisfy globally. No transfer of pure-logarithmic boundary regularity to native null h is claimed.

## 7. Next falsifiable arithmetic tests, without restarting global shell leakage

**Target A, local a=53/50:** compute the 112-native corrected *pole-free* constrained Schur problem using inherited F112 positive floor (10), NF12 low16, and fresh native/source mixed rows. Certify lower bounds beta_e>=-2 and beta_o>=2 or exhibit a genuine signed negative vector. Finite Ritz upper bounds cannot prove these lower bounds. Do not discard the 96 omitted native modes or their cross terms.

**Target B, global first contact:** assuming Q_a>=0 and a moment-carrying null, derive a strict arithmetic inequality showing the actual constrained minimum of H_a cannot equal -2 (even) or +2 (odd). Keep the separate zero-moment H_a-null exclusion. A proof of (11) or the monotonicity (7) alone is insufficient; the missing step is a zeta-specific strictly signed estimate on the constrained minimizer.

**Target C, endpoint regime:** test whether a native boundary trace estimate, with explicit prime-shift and pole contributions, makes the moment-zero class impossible. The CC28 saturation theorem proves only support reaches both endpoints; pure logarithmic-Laplacian Hopf lemmas cannot simply be imported.

Adversarial controls: (i) the differential first-contact operator has a nonzero boundary-saturated null and satisfies a valid cutoff/virial identity; (ii) subtracting a full positive physical level creates shifted contacts without original zero modes; (iii) a moment-zero null may occur while the scalar threshold is strict, as shown in section3. Any proposed closure must reject these controls for the right arithmetic reason.

## 8. Custody and proof classification

**New analytic reductions:** parity-resolved contact equations (3)-(4); extended-real scalar threshold equivalence and monotonicity (6)-(7); exact native null cutoff identity (11).

**New quantitative corollary of certified actual data:** the entire pole-free F112 complement is positive at a=53/50 with conservative floor 4/25 by (10). Independent NF12 directed low4 entries support a one-negative even/two-positive odd pole-free inertia test; this is only finite restriction.

**Open:** all-cap scalar inequalities, absence of zero-moment nulls, native first-contact exclusion, full original positivity at 53/50, RH/F4, retained attachment and Lean formalization. The original whole-domain positive anchor remains a=21/20. No new executable validator or Lean proof is claimed; arithmetic interval input is the separately published NF10/NF12 evidence, the remaining claims are analytic deductions and finite matrix arithmetic checks.
