# NF454 — Original n=9 contact-source moment in J8

Date: 2026-11-02 PT. **Standing: quantitative original source-native result PENDING focused CI.** Canonical W-ODD-NEG and whole signed J7/J8 OPEN.

## Previous / current / next

**Previous NF453 ACCEPTED:** exact complete principal L2 energies for original J7 and J8, a one-sided D7+D8 signed floor, and a negative signed J7 island. NF452 had certified a positive J8 microscopic endpoint collar. Neither whole J7 nor J8 signed value has been determined.

**Current NF454 mathematical reduction:** Isolate the genuine **n=9 activation at the original J7/J8 contact** rather than extrapolating either local signed island. Preserve full source, pole, center, and all original six earlier weights. Let B=11/10, x9=log(9)-B, a=B-x9=2B-log(9), v=U(B), and w9=Lambda(9)/sqrt(9)=log(3)/3. For 0<y<a and x=x9+y, odd source parity yields U(x-log9)=-U(B-y). The authentic *increment* from the seventh prime-power term is

    p9(x)=w9*v;
    z9(x)=-w9*(U(x-log9)+v)=-w9*(v-U(B-y));
    (p+z)9(x)=-w9*U(x-log9).

Hence z9 has a true C0 seam start (since U(-B)=-v), not an invented discontinuity. The precise missing **regularized contact source moment** is

    A9 = ∫_0^a [v-U(B-y)] dy
       = v*a - ∫_(log9-B)^B U(t) dt.

Then

    ∫_J8 z9(x) dx = -w9*A9,
    4∫_J8 p9(x)*z9(x) dx = -4*v*w9²*A9.

These are authentic source-specific summands of the full signed expansion, **not D8 by themselves**. The other terms' correlations with all six earlier prime powers and the full original archimedean response remain open, so no whole-cell sign follows.

## Native exact primitive, no x-grid quadrature

Keep every one of the original 242 selected and four critical coefficient blocks, all 32 critical sines, true sinh pole and all 273 grouped original polynomial-frequency terms. Group each frequency f with omega=2*pi*f. For any nonzero physical original omega, the complex antiderivative of y^k exp(i omega y) is exp(i omega y) P_k(y), where

    P_0=1/(i omega);
    P_k=(y^k-k P_(k-1))/(i omega).

For k even take imaginary part (original polynomial-sine), for k odd real part (original polynomial-cosine). The authentic sinh term integrates as 2*pole*(cosh(B/2)-cosh((log9-B)/2)). The exact primitive uses source coefficients **summed before the endpoint contraction**, in 4096-bit outward Arb/Acb; original NF406 log9 interval encloses the irrational endpoint. Original dyadic source coefficient uncertainty S0 is paid separately by |delta A9|<=2a*S0. NF411 original native v and genuine n9 weight intervals are checked independently.

The checker prints outward intervals for A9, true physical z9 zeroth moment and exact n9 **self** p9*z9 cross moment, with signs certified only if those intervals strictly exclude zero after all sources of uncertainty. This tests the actual J8 n9 contact channel; it does NOT produce a numerical value for the rest of the true original J8 signed integral.

## Stop line

Source, seam and NF411/NF453 custody are mandatory preconditions. Focused workflow: .github/workflows/nf454-original-n9-contact-native.yml; script: scripts/local_replay/nf454_original_n9_contact_native_moment.py.

Original J7/J8 entire signed moments, NF404 global scalar, J242 exterior, canonical W-ODD-NEG, even/whole Weil/domain, RH remain OPEN. **Next NF455:** combine this real source-native contact moment with full original six-prime+arch response cross moment on J8 (and J7 whole), not infer whole signed D8 from a single source increment. No main merge.
