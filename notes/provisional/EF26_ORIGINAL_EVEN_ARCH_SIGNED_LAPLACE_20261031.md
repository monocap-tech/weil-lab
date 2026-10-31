# EF26 — Original signed arch mixed as a positive-filter Laplace series

Date: 2026-10-31. Canonical W-EVEN-FORM OPEN. Base EF25 [draft PR #410](https://github.com/monocap-tech/weil-lab/pull/410), native original SI10 469-source even fixed FIR test, genuine arch E<30||f||², |M_arch|<47||f||, verified [Actions #41225935038](https://github.com/monocap-tech/weil-lab/actions/runs/41225935038), independent analytic audit open. EF24 true original arithmetic-only mixed Mprime<0, and arithmetic-only |Mprime|²/E<1/400, CI accepted.

## Exact physical original digamma translation identity

Let a_arch(xi)=Re ψ(1/4+iπxi)-lnπ, e=1_I cos(ωx), ω=2π*(37/64), I=[-B,B], B=11/10. The exact original digamma integral is

 a_arch(xi) = ψ(1/4)-lnπ + ∫_0^∞ e^(-t/4)/(1-e^-t) (1-cos(πxi t))dt.

For the actual original even complement f=F_h ψ_bell (EF21), <e,f>=0 EXACTLY; e,f even. Put s=t/2 and w(s)=e^(-s/2)/(1-e^(-2s)). Then Fourier Plancherel and parity produce

 M_arch=q_arch(e,f)=-2∫_0^∞ w(s)<T_s e,f>ds.

The integrand has NO singularity at s=0 because f stays strictly away from ±B and global cosine-source orthogonality gives <T_s e,f>=0 for all sufficiently small s; <T_s e,f>=0 also for s>2B by physical support. This is an integral of the ACTUAL original source, not a surrogate positive cap.

Write e(x+s)=cos(ω(x+s))1_{|x+s|<=B}. Since f is supported in [-B,B] and <f,cos(ω(x+s))>=0 by original c0 orthogonality and parity, we obtain an EXACT cutoff exterior formula

  M_arch=+2 ∫_I f(x) ∫_{B-x}^∞ w(s)cos(ω(x+s)) ds dx.

The outer integral is supported away from the singular s=0; Fubini and the exact geometric source support justify exchanging. Expand the original positive exponential kernel

  w(s)=∑_(m=0)^∞ exp[-(2m+1/2)s],  λ_m=2m+1/2.

This yields the exact original Laplace-series identity

  M_arch=2 Re{ e^(iω B)∑_(m=0)^∞
    e^(-λ_m B) Λ_h(λ_m) cosh(λ_m a) J_r(λ_m)/(λ_m-iω) },

where **all input objects are from the unchanged original SI10 source**:
- h=1/2048, r=1/65536, a=B-ln2+469h,
- Λ_h(λ)=∏_{j=1}^{107}[2cosh(λh)-2cos(2πh c_j)]^{p_j}>0, ∑p_j=469,
- J_r(λ)=∫_{-r}^r cos^6(πt/(2r))e^{λt}dt =
  45sinh(λr)/[2λ∏_{k=1}^3((λr/π)^2+k²)]>0.

The Λ factors are POSITIVE at real Laplace arguments even though the fixed original FIR coefficients have astronomical signed cancellation; the integral/series evaluation bypasses direct 939-term cancellation and full-frequency oscillatory mesh.

## Uniform sign pattern and finite sufficient certificate

Let θ=ωB=407π/320. For every real λ>0 the real factor is

  Re[e^(iθ)/(λ-iω)] = [λcosθ - ωsinθ]/(λ²+ω²).

Original SI14 source rational trig enclosures give cosθ<0 and sinθ<0. The linear numerator is **positive** at λ0=1/2 and λ1=5/2, **negative** at λ2=9/2, and strictly decreasing thereafter because cosθ<0. All Λ, J_r, cosh and exponential factors are strictly positive.

Thus the infinite original signed arch mixed series has **only two positive terms**, followed by a strictly negative tail. It suffices to check ONE finite outward partial sum S_K for K>=2. If S_K<0, all omitted terms also have negative sign, and M_arch<0 rigorously WITHOUT any numerical tail upper. EF26 implements a 340-digit outward integer interval evaluation for m=0,...,12; the actual source CI result must be inspected before claiming the sufficient sign check succeeds. If not, the script records INCONCLUSIVE, not a guessed total sign.

## Exact rigorous numerical method, no synthetic source

The SI06 original π bound is recomputed from the same Machin arctangent identity at higher series order via EF24. Original ln2 uses the same rigorous SI06 atanh source series with 450 terms. Taylor sin/cos uses the EF24 340-digit outward integer, 150-term trig source implementation. Positive exp(x) for x<=40 uses an exact Taylor series on x/64<1, 221 positive terms and outward remainder <2/221!, then six interval squarings. Negative exp is 1/exp(pos), and cosh/sinh are exact interval exponentials. The whole original 469-factor Λ_h(λ) product is evaluated in positive interval space, without cancellation, and J_r positive rational hyperbolic expression. Every interval op is outward directed; any claimed sign is based on strict integer enclosure, not display decimals.

**Scope:** a sign of M_arch, IF the CI proves it, combines with EF24 Mprime<0 for an original whole pole-free signed mixed M<0 on this ONE cofinite test. This is not automatically a numerically useful normalized Schur floor nor finite 469D corrected even Schur positivity, and it is not RH. The analytic translation/Fubini/digamma proof is independently auditable; source CI only checks exact finite constants/partial interval signs. EF27 should then quantify source-normalized full mixed inverse-Schur correction and compare to finite even block/pole, or if partial sign inconclusive prove precise conditioning STOP and switch to lower-moment source-adapted complement.

No main merge. Whole original even/odd/full Weil/RH OPEN.

## Original filter dynamic-range repair and exact common positive scaling

The FIRST focused [EF26 Actions #41227005306](https://github.com/monocap-tech/weil-lab/actions/runs/41227005306) **FAILED** when the source first-term Λ(λ₀) was smaller than the fixed-point lattice 10^-340: the native double-log pilot gave log10 Λ(λ₀)≈-723.3838, and the outward interval [0,positive] could not prove the mathematically known positive source sign. This is a finite-representation resolution failure, not a proof that Λ or any term is zero. Failure retained.

**Repair:** multiply each of the exactly 469 positive real-Laplace original FIR factors by exact rational 100. Every computed source Λ̃(λ)=100^469 Λ(λ), and every computed mixed summand and partial sum is therefore exactly **100^469 times its original value**. A common strictly positive multiplier preserves ALL signs and comparisons of a finite partial with zero. Neither the source f nor the original Weil form is rescaled in mathematics; this is only the stored interval number. This removes the 10^-723 underflow without inventing additional digits or altering the genuine 107-center SI10 frequencies. The rescaled revised native CI run must pass before claiming any finite signed arch result.
