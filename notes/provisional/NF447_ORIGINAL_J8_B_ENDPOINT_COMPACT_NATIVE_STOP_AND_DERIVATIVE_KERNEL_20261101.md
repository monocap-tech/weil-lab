# Weil-Lab NF447 — Original J8 endpoint: exact derivative kernel, native integration stop

**2026-11-01 PT. MIXED STANDING:** Exact original-source derivative kernel **ACCEPTED**; rigorous \(|I_B|<902\) and \(|z(B)|<7300\) **ACCEPTED**; all seven original prime-power source shifts and nonintegral endpoint contribution **SOURCE-NATIVE CERTIFIED**. Direct Acb quadrature on the first compact panel returned **nan + nanj — METHOD STOP**. Original complete numerical \(z(B)\), original signed \(D_7,D_8\), NF410/NF404, W-ODD-NEG and RH remain **OPEN**.

Repository custody: [draft PR #468](https://github.com/monocap-tech/weil-lab/pull/468), stacked on NF446 [PR #467](https://github.com/monocap-tech/weil-lab/pull/467). No merge to main.

## Previous cursor → current circle → next bold

**NF446:** Exact original NF407 246-source central digamma+two-image correlation reduced to physical compact \(U=u_4|_{[-B,B]}\). The complete true J7/J8 response satisfies \(|z|<25000\), but its native integral was unevaluated.

**NF447:** At \(x=B=11/10\), obtain a single physical compact integral and analytic scalar. Attempt genuine validated source-native Acb integration. A native numerical integral **did not resolve**; replace its singular quotient by an exact derivative-kernel representation, derive an improved true bound, and independently evaluate all other physical endpoint terms at 2048-bit precision.

## True original J8 endpoint identity

Set

\[
K(t)=\frac{e^{-t/4}}{1-e^{-t}},\qquad v=U(B),\qquad
H(d)=\log\coth(d/4)+2\arctan(e^{-d/2}).
\]

The original NF446 combined response at \(B\), after principal-log cancellation, becomes

\[
\mathcal J(B)=v\left[\psi(1/4)-\log\pi+
\frac12\left(\log\frac4B+\frac\pi2+H(2B)\right)\right]+I_B,
\]

\[
\boxed{I_B=\frac12\int_0^{4B}K(t)[U(B)-U(B-t/2)]\,dt.}
\]

The **complete physical** endpoint includes the genuine original source shifts and NF404 centering:

\[
z(B)=\mathcal J(B)-
\sum_{n\in\{2,3,4,5,7,8,9\}}\frac{\Lambda(n)}{\sqrt n}
[U(B-\log n)+v]-a_{\rm NF404}\sinh(B/2).
\]

All seven regular minus shifts are active at the one-sided original J8 endpoint; no plus shifts. The true von Mangoldt factors are \(\Lambda(4)=\Lambda(8)=\log2\), \(\Lambda(9)=\log3\), **not** the logarithms of the prime powers. Every source argument remains within true physical support \([-B,B]\); no exterior entire generator is used.

## Genuine source-native analytic integration attempt — METHOD STOP

Original true NF407 source: 242 selected +4 critical 4096-bit dyadics, 32 sine frequencies, 273 grouped polynomial/frequency combinations. Original source JSON SHA256 0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce; original NF406 seam SHA256 c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675.

The original ACb evaluator attempted the joint compact-source kernel (not separately huge images) at 1024-bit precision with intervals

\[
[10^{-12},10^{-3}],\ [10^{-3},1/20],\
[1/20,1],\ [1,4B].
\]

The omitted collar \(0<t<10^{-12}\) was bounded from original NF413 true \(\|U''\|_2<256\) and original NF445 true \(|U'(B)|<10^{-6}\) by

\[
|I_{[0,h]}|\le \frac h4(10^{-6}+256\sqrt{h/2})(1+h)
<1.3\times10^{-16}\quad(h=10^{-12}).
\]

Original 4096-bit source-radius uncertainty was separately charged (<\(10^{-690}\)). The first genuine computed interval \([10^{-12},10^{-3}]\) returned **nan + nanj**. Subsequent panels were not computed. **This is a numerically unresolved analytic integration, not a source-certified point value.** [Original native method-stop CI #41393081856 SUCCESS as custody](https://github.com/monocap-tech/weil-lab/actions/runs/41393081856), native JSON SHA256 468678b2c3d8f83deaebb129987d38843abf231faa250f53a4f48fb54941c4ca, artifact #13117944253.

## Exact tK derivative-kernel remedy

By the fundamental theorem of calculus, for all \(0\le t\le4B\),

\[
U(B)-U(B-t/2)=\frac t2\int_0^1U'(B-\theta t/2)\,d\theta.
\]

Thus

\[
\boxed{
I_B=\frac14\int_0^{4B}tK(t)
\left[\int_0^1U'(B-\theta t/2)d\theta\right]dt.
}
\]

This is **an analytic, removable integrand at \(t=0\)**, since \(\lim_{t\downarrow0}tK(t)=1\). It removes numerical \(0/0\) before integration. Every source argument is in \([-B,B]\). **It is an exact reformulation, not a completed numerical integration.**

By original NF413 \(\|U''\|_2<256\) and true original NF445 source-native \(|U'(B)|<10^{-6}\),

\[
|U'(B-\theta t/2)|\le10^{-6}+256\sqrt{\theta t/2}.
\]

Average in \(\theta\), using \(\int_0^1\sqrt\theta\,d\theta=2/3\) and \(t/2\le2B<9/4\). Then \(\left|\int_0^1U'(B-\theta t/2)d\theta\right|<10^{-6}+256\). Since \(0<tK(t)<1+t\) and \(4B=22/5\),

\[
\boxed{
|I_B|<
\frac{10^{-6}+256}{4}\left(4B+\frac{(4B)^2}{2}\right)
=\frac{2816000011}{3125000}<902.
}
\]

Elementary \(\log(4/B)<2\), \(\pi/2<2\), \(H(2B)<3\), together with original \(|v|<1\), \(|\psi(1/4)-\log\pi|<10\), show the separate scalar has magnitude \(<14\). Hence \(|\mathcal J(B)|<916\), and with seven actual original prime terms each \(<901\), plus centering \(<2\),

\[
\boxed{|z(B)|<7300.}
\]

These original-source bounds are rigorous but **not decision quality**. [NF447 derivative/source exact rational CI #41393532381 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41393532381), JSON SHA256 ee5238adc9313428244c8f019b965bd994328f7e890e999ca45a9fd7b63c7bca, artifact #13118282476.

## Independent original source-native nonintegral terms

At 2048-bit Arb precision, independently evaluate

\[
Z_{\rm known}(B)=v\left[\psi(1/4)-\log\pi+
\frac12\left(\log\frac4B+\frac\pi2+H(2B)\right)\right]
-\sum_{n\in\{2,3,4,5,7,8,9\}}
\frac{\Lambda(n)}{\sqrt n}[U(B-\log n)+v]
-a_{\rm NF404}\sinh(B/2).
\]

The genuine original full-source native outward ball has midpoint

\[
\boxed{Z_{\rm known}(B)\approx 0.897798148226488214696549278262.}
\]

This is **not the complete physical \(z(B)\)**: \(z(B)=Z_{\rm known}(B)+I_B\), with the latter still uncomputed. The source coefficient/radius paid broad enclosure is

\[
\boxed{-901.102201851774<z(B)<902.897798148227.}
\]

The full exact outward rational intervals are in the native JSON, not the rounded display. [Seven prime-power original source-native CI #41393812202 SUCCESS](https://github.com/monocap-tech/weil-lab/actions/runs/41393812202). Final source known-part JSON SHA256 016b26dd713d796a99bb775a2ce6d0ba6173aff506bda609e96b0a6ab36c5164, artifact #13118566824. This is an independently source-certified **nonintegral** component, not evidence for \(z(B)\)'s sign.

## Obligation ledger and next NF448

**Accepted:** True original compact endpoint analytic reduction; exact removable tK derivative integral; \(|I_B|<902\) from original NF413/445, \(|z(B)|<7300\), and original 2048-bit native seven-prime-power known terms with correct von Mangoldt weights.

**METHOD STOP:** Direct Acb numerical integration on first near-zero panel returned nan; no resolved \(\int K(t)[v-U(B-t/2)]dt\) and no narrow \(z(B)\) enclosure.

**OPEN:** Actual full signed J7 and J8 continuous \(pz,z^2\) integrals, original complete principal \(E_p\), NF410/NF404 whole scalar, fourth J242 exterior upper, W-ODD-NEG, even/whole Weil, operator domain and RH. Existing certified original signed physical cells stay 6/8: J1/J2/J3 positive, J4/J5/J6 negative.

Permanent compact [NF447 source and method-stop custody](../data/provisional/NF447_original_J8_B_endpoint_weighted_derivative_and_ACB_stop_custody_index.json) pins source, CI, original exact/native JSON SHA. Full raw numerical JSON still in GitHub Actions; permanent raw repo archival due. Research stays draft; no main merge.

**Next bold — NF448:** Implement a genuine **analytic divided-difference** source evaluator for \(U(B)-U(B-t/2)\) with a validated \(tK(t)\) Taylor/special-function kernel, or a native source-derivative two-variable validated integration. First obtain a decision-quality enclosure of \(I_B\), and only then original J7/J8 signed moments. Re-running the unchanged singular quotient or increasing endpoint-image count would repeat the NF447 METHOD STOP.
