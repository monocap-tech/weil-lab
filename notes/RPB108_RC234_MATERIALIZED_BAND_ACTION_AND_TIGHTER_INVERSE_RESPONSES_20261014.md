# RPB108 — RC234: materialized band correction and tighter actual responses

Date: 2026-10-14 UTC. Aperture B=11/10. Parent RC233: `a4da25ca2ed083616007e77d34c14d8d894c6cae`. Branch: research/rpb108-route-consolidation.

RC234 materializes the actual ideal-band action columns through degree 64, pays their difference from the fixed RC115 rational kernel, and improves the complete augmented action and inverse-response enclosures in both parities. The operator, inputs, output cutoff and D metric are unchanged, so the following error reductions are direct comparisons.

| Input | RC232 complete squared D-action error | RC234 upper, outward | RC234 relative error norm upper |
|---|---:|---:|---:|
| P0, even | 0.1275118543 | 0.0488638810 | 7.644% |
| P1, odd | 0.1093104884 | 0.0484114865 | 11.726% |

| Actual canonical source | RC233 inverse-response enclosure | RC234 enclosure, outward |
|---|---|---|
| r0=i*P0 | [0.1635278206, 1.3274008190] | [0.1689023074, 0.8185523935] |
| r1=i*P1 | [0.0505098736, 1.0927793471] | [0.0532751751, 0.6738403414] |

**The two moment-source upper numbers below one are not the full auxiliary norm below one.** Their source normalization is not the frequency metric, and these two sources do not exhaust the chosen rank-639 augmentation. No Stage I, original whole-space positivity, F4, Lean or RH closure is claimed. The exact rational augmentation is unchanged; an ideal band inverse is never substituted for its inverse.

## Exact band coefficients without a Bessel library

For zero-extended physical Legendre input P_n(x/B), with z=2pi B xi, direct integration gives

\[
 \widehat P_n(\xi)=2B(-i)^n j_n(z),
 \quad j_n(z)=A_n(1/z)\sin z+B_n(1/z)\cos z.
\]

Here j_n is just notation for the finite polynomial/trigonometric expression derived from Legendre integration. No special-function library evaluation is used. Start with A0(t)=t, B0(t)=0, A1(t)=t^2 and B1(t)=-t, and use

\[
 A_{n+1}(t)=(2n+1)tA_n(t)-A_{n-1}(t)
\]

and the same recurrence for B. The Fourier identity follows from the Legendre recurrence and integration by parts. The validator independently checks every polynomial coefficient through n=64 using the finite boundary-derivative expansion of the Fourier integral. Specifically

\[
 P_n^{(k)}(1)=\frac{(n+k)!}{2^k k!(n-k)!},
 \quad P_n^{(k)}(-1)=(-1)^{n+k}P_n^{(k)}(1).
\]

Repeated finite integration by parts gives the sine coefficient of z^(-k-1) as d_(n,k)(-1)^((n-k)/2) when n+k is even, and the cosine coefficient as -d_(n,k)(-1)^((n-k-1)/2) when n+k is odd. These exact coefficients agree with the recurrence for all 65 degrees.

For equal parity n,j the physical outside-band Gram is

\[
 T_{nj}=\frac{4B}{\pi}(-1)^{(n-j)/2}
       \int_{z_U}^{\infty}j_n(z)j_j(z)dz,
 \quad z_U=2\pi B U.
\]

Opposite parity is exactly zero. Physical Plancherel then gives the band Gram

\[
 G_{nj}=m_j\delta_{nj}-T_{nj},
 \quad m_j=2B/(2j+1).
\]

The materialized action coefficient of J_U*J_U P_j on P_n is G_nj/m_n. The code encloses every same-parity coefficient through n=64 for j=0,1. It does not substitute a diagonal identity action for those columns.

## Oscillatory tail integrals and independent replay

Multiplying the finite sine/cosine expressions reduces the tail to constant, cosine and sine integrals against z^-m, with m>=2. Define

\[
 I_m(z_0)=\int_{z_0}^{\infty}e^{2iz}z^{-m}dz.
\]

Integration by parts gives, after L steps,

\[
 I_m(z_0)=e^{2iz_0}\sum_{k=0}^{L-1}
 \frac{i(-i)^k(m)_k}{2^{k+1}z_0^{m+k}}+R_{m,L},
\]

\[
 |R_{m,L}|\le\frac{(m)_L}{2^L}
                 \frac{z_0^{1-m-L}}{m+L-1}.
\]

This is a finite identity with an explicit absolute tail bound, not acceptance of an unbounded asymptotic series. Generation uses L=48; replay uses L=56. Both independently rounded results produce exactly the same stored Gram intervals on a 10^-24 grid.

For numerical stability the code encloses z0^m I_m, which has order-one scale, and separately scales each polynomial coefficient by z0^-m before interval multiplication. This avoids rounding extremely small moments to a fixed absolute grid and then multiplying that error by huge unscaled coefficients. Internal operations use directed rational 10^-60 rounding. No floating-point eigenvalue or sampled oscillatory integral enters acceptance.

The phase is reduced with a rational pi0, and sine/cosine are evaluated by degree-80 Taylor polynomials with remainder |theta|^81/81!. The actual pi enclosure from RC115 pays the periodic phase-reduction error. Actual pi also changes the lower integration limit and the prefactor 4B/pi; those errors are paid separately.

For completeness |j_n(z)|<=1 follows from the normalized Legendre Fourier integral and |P_n(t)|<=1. Plancherel gives integral_0^infinity j_n(z)^2 dz=pi/[2(2n+1)], so the absolute product integral is at most pi/2<2. These bounds control the lower-limit shift and prefactor uncertainty uniformly for every retained n. The validator explicitly checks the pi lower and upper constants used in that payment. The resulting actual band Gram intervals retain both the zero-extension boundary contribution and its oscillatory phase.

## Full omitted output and the rational operator difference

Let C=J_U*J_U on physical supported L2. It is a positive contraction, hence C^2<=C. For q=P_j,

\[
 \|Cq\|_2^2\le\langle q,Cq\rangle_2=G_{jj}.
\]

Subtracting certified lower bounds for the retained orthogonal coefficient energies gives a full physical output-tail upper

\[
 T_{\rm out}\le G_{jj,\rm upper}
 -\sum_{n\le64}m_n\min_{a\in[G_{nj}/m_n]}|a|^2.
\]

The code verifies nonnegativity. This upper includes all omitted physical output; the finite coefficients alone are not a coverage proof. Its values are below 0.000840276 even and 0.000541271 odd. Diagonal D inversion then costs only the first omitted D weight:

\[
 \|\lambda D^{-1}(I-\Pi_{64})Cq\|_D^2
 \le\frac{\lambda^2 T_{\rm out}}
 {H_{n_{\rm first}}+s_{\rm lower}}.
\]

The actual rational Fhat still differs from J_U. RC232's paid full physical adjoint-product error epsilon bounds ||Fhat*Fhat-C||. Its D-energy action payment remains

\[
 E_{\rm rational}\le\lambda^2\epsilon^2m_j/s_{\rm lower}.
\]

The new rational finite augmentation trial is obtained by dividing the actual band coefficient intervals by the actual H_n+s interval and multiplying by lambda. It pays all finite coefficient rounding in D energy, the full output tail, and the rational-versus-band difference. Those three norm errors are added before squaring. Combining with the unchanged RC231 original-action error gives the new complete N action enclosure. No errors from different components are presumed orthogonal.

This materializes the comparison operator's finite columns, not the dense degree-2400 rational kernel. The difference to that fixed rational kernel remains rigorously enclosed; it is not set to zero.

## Sharper test forms and updated inverse responses

Omitted output has zero pairing with P_j because physical Legendre projection and D are diagonal in the same basis. Thus a form entry does not need to pay the action's entire omitted-output norm. The original test form uses RC231's retained diagonal coefficient interval and pays only actual regular-kernel, prime-parameter/support and pole-Taylor model errors in its pairing. All finite constant/rounding uncertainty remains included.

This gives strictly positive original polynomial test values near 0.0885591960 even and 0.0970828158 odd, with exact rational enclosures in the certificate. Positivity of these two polynomial directions is only a consistency/control result, not an original full-space floor or a new exhaustive spectral count.

Adding lambda G_jj and paying lambda epsilon m_j gives sharper augmented test-form intervals. RC233's existing lower and upper trials, plus one variational scalar proposal, are then rechecked with the new full action bounds and the same actual global N endpoints. The signed identity still adds its inverse-residual correction. New response bounds are intersected with the old certified bounds; both final uppers improve strictly.

The final response widths are approximately 0.649651 even and 0.620566 odd, reduced from 1.163873 and 1.042270. These are the same actual rational operator, canonical sources and response metric. They remain enclosure widths, not lower bounds on actual numerical error. The improvement comes from representing the missing band correction and paying a sharper full output tail, not from adding more source channels or proving a new inverse gate.

All actions and responses preserve reflection, so cross-parity errors and response pairings vanish exactly. The two-source diagonal enclosures cover all complex combinations of r0 and r1. They do not cover arbitrary combinations of the full 639-channel augmentation range or identify its auxiliary frequency normalization.

## Verification and boundary

Generation and replay verify all input blob pins, 65 independent spherical-polynomial boundary controls, actual phase/constant enclosures, explicit finite tail remainders, full output and rational-model payments, and actual signed inverse-response bounds. Replay uses 56 integration-by-parts terms instead of 48 and reverses tail accumulation order; the complete stored certificate must match exactly.

```bash
python scripts/validate_rpb108_rc234_materialized_band_action.py --output certificates/rpb108_rc234_materialized_band_action.json
python scripts/validate_rpb108_rc234_materialized_band_action.py --output certificates/rpb108_rc234_materialized_band_action.json --replay
```

Publication adds this note, its validator and its certificate with an expected-head non-force update. Remote comparison and recursive tree readback verify preservation of existing blobs. Conflict checks cover the additions, not all historical content.

The next obligation is richer actual source/response trials and a complete full-range residual/auxiliary metric certificate. No exact count of further solves or passes is asserted. RC228's canonical inverse gate remains preserved, while the full original augmentation norm below one and Stage I assembly remain open.
