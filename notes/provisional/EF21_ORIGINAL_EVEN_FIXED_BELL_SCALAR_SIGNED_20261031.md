# EF21 — Fixed physical cosine-bell test, stable exact Fourier transform, and the two original signed scalar integrals

**2026-10-31. Canonical W-EVEN-FORM remains OPEN.** Parent EF20 [draft PR #399](https://github.com/monocap-tech/weil-lab/pull/399), corrected exact-original 469-source FIR and all 15,023 edge-exclusion checks passed [Actions #41217982951](https://github.com/monocap-tech/weil-lab/actions/runs/41217982951). Initial EF20 run #41216069286 FAILED because its verifier did not initialize a minimum interval margin; the correction passed. EF20's true fixed-h signed mixed nonvanishing still relies on original arch pseudolocality/form-domain proof separate from the numerical source CI.

## 1. The first fully explicit fixed physical test

Use unchanged original SI10 b9 exceptional even 469-source span V, authentic 107 rational center/degree pairs (c_j,p_j) with sum p_j=469. Let B=11/10, h=1/2048, N=469, and use the genuine EF18/EF20 source-specific original arithmetic n=2 jump x0=B-ln 2. Its fixed-h isolated extreme FIR-shifted location is a=x0+N*h≈0.6358567256900548.

Fix the rational bump radius **r=1/65536**, and define

b_r(x)=cos^6(pi*x/(2r)) for |x|<r, and 0 outside.

This is C^5 (not C-infinity), compactly supported, in all original signed logarithmic multiplier strong/form domains because its Fourier transform decays |xi|^-7. Define the actual real EVEN smooth-enough physical test

psi(x)=[b_r(x-a)+b_r(x+a)]/2,

f=F_h psi, F_h=product_(j=1)^107 (T_h+T_-h-2cos(2pi*h*c_j))^p_j.

Its Fourier/physical orthogonality is EXACT: the FIR symbol has zeros of multiplicity p_j at each original signed ±c_j and all physical shifts remain strictly inside I=[-B,B]. Thus f lies in the actual even original exceptional complement F=V^perp, without any Gram inverse.

The original rigorous ln2 bounds imply 2604+1/4<2a/h<2604+3/4. Same-lobe translates have center separation ≥h; opposite-lobe translates have separation ≥h/4. Since 2r=1/32768<h/4, **all 1,878 possible translated bell supports are pairwise disjoint**. With outermost original FIR Laurent coefficients A_{-469}=A_{469}=1, f is certainly not zero, and the physical norm is EXACT

||f||² = (231r/1024) * sum_(k=-469)^469 A_k² >= 231r/512 >0.

This is a new quantitative original physical source-orthogonal L2 norm identity and floor. It is NOT an inverse-Schur lower; the latter needs the signed mixed numerator and an UPPER on its true positive energy denominator.

## 2. Cancellation-free closed Fourier transform (major numerical optimization)

Define sinc(t)=sin(pi*t)/(pi*t), sinc(0)=1, q=2r*xi. The original real normalized bell has the exact Fourier transform

H_r(xi)=r * [ (20/32)sinc(q) + (15/32)(sinc(q-1)+sinc(q+1)) + (6/32)(sinc(q-2)+sinc(q+2)) + (1/32)(sinc(q-3)+sinc(q+3)) ].

A complete exact rational polynomial identity cancels six leading asymptotic coefficients and produces a **cancellation-free closed expression**

H_r(xi)= -45*r*sin(pi*q) / [ 2*pi*q*(q²-1)*(q²-4)*(q²-9) ],

with removable singularities at q=0,±1,±2,±3. Unlike the seven-sinc formula, this rational-sine expression has no catastrophic high-frequency subtraction. In particular H_r(xi)=O(|xi|^-7). For |q|>=4, exact pi>3 and rational product inequalities give |H_r(xi)| <=25*r/|q|^7. The full original signed m(xi)=arch(xi)-2Σ_(n∈{2,3,4,5,7,8,9}) w_n cos(2pi*xi*ln n) is only logarithmic at infinity, so the physical cross and energy integrals below absolutely converge.

The exact source-pinned Fraction validator verifies this rational Fourier identity by multiplying denominators into a polynomial in t=q² and checking ALL its coefficients vanish except the constant -45/2. It also checks the physical norm identity by the known exact integral ∫_-r^r cos^12(pi*x/(2r))dx=231r/512.

## 3. Reduce the real operator problem to two scalar full-original-frequency integrals

The authentic original source e(x)=1_I cos(2pi*(37/64)x) has Fourier transform

ehat(xi)=B*[sinc(2B(xi-c0))+sinc(2B(xi+c0))], c0=37/64.

Our explicitly fixed bell satisfies psihat(xi)=H_r(xi)*cos(2pi*a*xi).

Define the exact FIR Fourier scalar symbol

S_h(xi)=product_j [2cos(2pi*h*xi)-2cos(2pi*h*c_j)]^p_j,

and the genuine pole-free signed original seven-prime+arch multiplier m(xi) from original SI06/SI10.

Then **no numerical 469D linear system remains in this test**. The original signed exceptional/complement numerator is exactly the single real scalar integral

M=Q0(e,f)=∫_R m(xi) ehat(xi) H_r(xi) cos(2pi*a*xi) S_h(xi) dxi.

The original complete pole-free signed even complement energy denominator is exactly

E=Q0(f,f)=∫_R m(xi) [H_r(xi) cos(2pi*a*xi) S_h(xi)]² dxi.

Both are absolutely convergent, retain all real original frequencies and the true seven-prime signed interference. The EVEN positive pole is deliberately excluded here because we are measuring the original pole-free Schur B0/C0; EF16's favorable rank-one pole correction must later be reattached.

The original SI10/EF15 signed cofinite floor implies, under its inherited analytic domain/reality proof,

E >= mu ||f||² >= (17/25000)*(231r/512)>0.

For any new rigorous full-original interval enclosures M∈[Mlo,Mhi], E∈[Elo,Ehi] with 0<Elo<=Ehi, a valid quantitative inverse-Schur lower from this explicit f is max(0,min_abs(M interval))²/Ehi. **None of these signed numerical interval enclosures has been computed yet.** An exact integrand and a valid formula do NOT constitute a certified positive lower.

## 4. Remaining numerical feasibility gate and controls

The 469-factor S_h can be extremely ill-conditioned even though f is bounded and physical. In particular the crude global |S_h|<=4^469, combined with the 1/|xi|^7 bell Fourier tail, introduces factors as large as 4^938 in naive energy-tail bounds: **do not promote such a bound as a feasible precision certificate**. A production calculation must stabilize S_h pointwise (log-amplitude and sign parity), use source-conditioned interval/adaptive frequency integration, rigorously pay original oscillatory seven-prime/arch and high-frequency tails, and preserve one common physical normalization for numerator and denominator. The derived H_r expression eliminates internal Fourier cancellation in the bump, not product-filter conditioning.

The genuine EF20 fixed-h signed jump is isolated by minimum edge margin ~4.603e-5; our r=1/65536≈1.526e-5 is strictly smaller than half that margin. This makes the source detector geometrically interpretable, but a point jump alone never provides a normalized Schur bound. Do not infer a nonzero numerical M from geometry without full original integration.

**Next EF22 acceptance:** rigorously interval-evaluate at least one physically fixed original M, E pair on this exact test or prove a certified fixed-test conditioning/method STOP with explicit error budget. If the 469-factor symbol cannot be evaluated with reasonable enclosure, abandon the universal FIR family in favor of a lower-constraint source-conditioned physical moment-nullspace test. Under no condition substitute cap positivity or EF14 single-ray sign for complete corrected Schur PSD.

**OPEN:** certified M/E, original full C0 inverse/Riesz response, complete 469D finite corrected Schur PSD, even-sector form-domain independent audit, paused odd-sector, whole Weil/RH. All research on an additive draft GitHub branch, no main merge.
