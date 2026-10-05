# RPB108: sharper actual complement and smaller exact obstruction

## Definitions and actual complement theorem

H is the actual supported logarithmic form domain at aperture a=1/2, with Fourier convention exp(-2pi i x xi), and Q is its actual native multiplier-plus-pole form. Let v_n(x)=sqrt(2n+1)P_n(2x) on [-1/2,1/2]. For k=20 or 64 put E_k=span(v_0,...,v_(k-1)) and F_k={f in H: <v_n,f>_2=0 for n<k}. These are physical projections; no graph-density assumption is used.

**New actual complement theorem.** For every nonzero f in F_20,

Q(f)>(1/5)||f||_2^2 and Q(f)>(9/100)||f||_H^2.

The former 64-moment bound remains true, but 20 moments suffice. This statement uses the established actual multiplier bounds and independently improves the low-frequency observation estimate.

## Plane-wave tail proof

The physical Fourier coefficient of v_n is sqrt(2n+1)(-i)^n j_n(pi xi), where j_n is the spherical Bessel function. Its real Poisson integral gives

j_n(y)=y^n/[2^(n+1)n!] integral_(-1)^1 exp(iyu)(1-u^2)^n du,
|j_n(y)| <= |y|^n/(2n+1)!!.

The last bound follows by integrating the absolute value and evaluating the beta integral. Physical Legendre polynomials form a complete L2 basis on the compact interval: continuous functions are L2 dense and Weierstrass polynomial approximation gives polynomial density there. This is an elementary physical L2 fact, not an assertion of density in the logarithmic form norm or full graph norm.

For f in F_k, Cauchy--Schwarz applied after the finite physical projection yields

|Fourier(f)(xi)|^2 <= ||f||_2^2 sum_(n>=k)(2n+1)|j_n(pi xi)|^2.

On |xi|<=4, |pi xi|<13. Write a_n=(2n+1)13^(2n)/[(2n+1)!!]^2. Then a_(n+1)/a_n=169/[(2n+1)(2n+3)]<=q_k=169/[(2k+1)(2k+3)]<1. Thus the low-frequency mass is at most rho_k^2||f||_2^2, where

rho_k^2=8a_k/(1-q_k).

At k=20 this exact rational bound is approximately 0.000762014335757. The bound is integrated over the full frequency band of length eight; no multiplicity-copy observations are counted.

The same moment vanishing annihilates degree-19 Taylor polynomials of exp(plus or minus x/2). Hence the actual pole cross-form has absolute value at most p_k||f||_2^2, p_k=8/[4^(2k)(k!)^2]. All moments belong to the same supported f.

The established actual multiplier bounds are m>=5/24 on |xi|>=4, m>=w/10 there, m>-10 everywhere, and w<2 on the low band, with w=log(e+|xi|). They therefore give

Q(f)>=[5/24-(245/24)rho_k^2-p_k]||f||_2^2,
Q(f)>=[1/10-(51/5)rho_k^2-p_k]||f||_H^2.

At k=20 the bracket displays are 0.20055443698914807 and 0.09222745377527938. Exact rational comparisons place them above 1/5 and 9/100. `scripts/certify_native_legendre_bessel_complement.py` checks these constants, pi<13/4, and the unchanged actual prime bounds. Output: `notes/data/RPB108_BESSEL_COMPLEMENT_CERTIFICATE_20261005.json`.

## Canonical comparison of the two finite carriers

For each k, H=E_k+F_k topologically. The coercive form on F_k defines the unique lift z_e^(k) by Q(z_e^(k),f)=Q(e,f) for all f in F_k. Define S_k(e,e')=Q(e,e')-Q(z_e^(k),z_e'^(k)). Completing the square gives Q(e+f)=S_k(e,e)+Q(f+z_e^(k),f+z_e^(k)).

Set V=span(v_20,...,v_63). Since F_20=V+F_64 and Q is coercive on F_20, the V block of S_64 is positive and at least (1/5) times the physical norm squared. Eliminating this block gives exactly S_20, by successive completion of the square, or equivalently successive minimization of Q(e+f) over the two complements. Thus 44 finite coordinates can be eliminated lawfully. Full Q positivity, negative index and weak kernel transport exactly through these eliminations.

The previously certified positive E_8 restriction of S_64 does not by itself prove positivity of the E_8 restriction of S_20: eliminating V subtracts another nonnegative coupling term. The new carrier needs its own actual corrected-source calculation.

## Fresh corrected block on the larger complement

The existing actual eight-source constructor is now instantiated against F_20. Its exact endpoint-log residual Gram is obtained from the F_64 Gram by adding the exact degree-20..63 log projection products. Smooth and mixed source products are integrated on the same exact prime panels and only degrees 0..19 are projected out. Every cross term and source error remains included.

`scripts/certify_native_coupled_schur.py --projection-dimension 20` independently validates the new complement and constructs this actual residual enclosure. Interval shifted-pivot elimination starts at the prior 1/250000 margin and halves it only when certification fails. No failure is interpreted as actual negativity. The certified margin and pivots are recorded in `notes/data/RPB108_REDUCED_COUPLED_SCHUR_CERTIFICATE_20261005.json`.

The calculation certifies S_20(e,e)>(1/500000)||e||_2^2 on E_8. The maximum surrogate Gram entry width is below 5.66e-53 and the actual Gram operator error from the source remainder is below 1.49e-30. Shifted pivot lower displays are 0.0605380, 0.2033270, 0.0160891, 0.1215006, 0.0335038, 0.0120374, 0.00134285, 0.5265567. These are elimination pivots, not eigenvalues. The negative diagonal control is rejected. The default degree-64 certificate reproduces byte-for-byte after parameterization, and the complement constants reproduce exactly.

## Exact remaining sign problem

Let T=S_20 restricted to E_8 and W=span(v_8,...,v_19). The recorded interval calculation certifies T>(1/500000)I. Let B:W->E_8 represent the mixed form S_20(e,w)=<e,Bw>_2. The remaining form is

S_12(w,w')=S_20(w,w')-<Bw,T^-1 Bw'>_2.

Then full Q>=0 if and only if S_12>=0. Its negative index and weak kernel equal those of Q. Reflection splits S_12 into two six-coordinate sectors. Positivity on E_8+F_20 yields actual negative index and weak nullity at most 12, six per parity. Zero diagonal energy alone still does not mean weak-kernel membership.

The remaining entries include the corrected mixed coupling. Raw positivity on W, or a representation of S_12 without those entries, would not close the sign. Approximate coercive lifts and rigorous source residuals can supply such entries without assuming operator-domain membership. No retained k membership, full graph density, simplicity or background positivity is imported.

The global endpoint input remains independently open. F4 and FULL TRANSPORT CLOSED remain open. The existing 64-complement certificate is preserved; Lean source, axioms and previous CI claims are unchanged.
