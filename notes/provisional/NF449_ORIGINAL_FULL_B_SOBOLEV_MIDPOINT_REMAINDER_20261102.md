# Weil-Lab NF449 — source-preserving finite-regularity integration of the complete original J8 endpoint remainder

**2026-11-02 PT. Method and reproducible source-native candidate committed; numerical interval is NOT accepted until the dedicated NF449 workflow succeeds, authentic artifact digests are inspected, and any failed checks are resolved.** The accepted NF448 prefix is not modified. W-ODD-NEG, J7/J8 signed cell integrals, original global NF410/NF404 scalar, and RH remain **OPEN**.

## Previous cursor → current circle → next bold

- **NF448 (accepted)**: source-certified complete original \(\frac12\int_0^{1/10}K(t)[U(B)-U(B-t/2)]dt\) via 4096-bit 273-group correlated Taylor/Cauchy, with signed negative midpoint \(-1.3843279409092028599738798764958344962762923052677214817388\times10^{-7}\).
- **NF449 (new method, pending native execution)**: avoid huge local-center analytic series when a *different previously certified feature of the original source* suffices. Use the accepted NF413 genuine all-source \(\|U''\|_{L^2(-B,B)}<256\), accepted NF445 original \(|U'(B)|<1\), full original physical support, and an exact midpoint Peano remainder to integrate the uncomputed \(t\in[1/10,22/5]\).
- **Next**: verify original-source native midpoint and previous-artifact SHA receipts in focused CI. If it succeeds, report *the entire* \(I_B\) and endpoint \(z(B)\) with honest interval width; decide the endpoint sign only if the interval excludes zero. This is **not** J7/J8 signed integral certification.

## Mathematical object unchanged

With \(B=11/10\), \(v=U(B)\), \(K(t)=e^{-t/4}/(1-e^{-t})\), define

\[
F(t)=\frac12 K(t)\big[v-U(B-t/2)\big],\qquad
I_B=I_B[0,1/10]+\int_{1/10}^{22/5}F(t)\,dt.
\]

Original NF407: **242 selected + 4 critical 4096-bit dyadic generators**, all 32 critical sine frequencies, all 273 consolidated order/frequency groups, and original odd sinh pole. Original NF406 seam, original NF404 center and NF447 all seven true von-Mangoldt prime-power translations remain unchanged. Every physical real source argument for the new integral satisfies
\[
B-t/2\in[-B,21/20]\subset[-B,B].
\]
Any entire continuation outside physical support is **not used** in this real midpoint scheme. The old \(t=0\) numerical singularity is excluded by the certified NF448 prefix, hence ordinary \(K\) is harmless for \(t\ge1/10\).

## New exact global \(L^1\) curvature bound

From NF413 and NF445, for any \(y\in[-B,B]\),

\[
|U'(y)|\le |U'(B)|+\sqrt{2B}\,\|U''\|_2
 <1+256\sqrt{11/5}<385<400.
\]

Thus \(|v-U(B-t/2)|<200t\). The kernel has the positive Laplace series

\[
K(t)=\sum_{m=0}^{\infty}e^{-(m+1/4)t},\quad K>0,\quad K'<0,\quad K''>0.
\]

At \(a=1/10\), using \(e^t-1>t\) and \(2\sinh(t/2)\ge t\),

\[
K(a)<1+1/a=11,\quad
|K'(a)|\le \tfrac14 K(a)+\frac1{a^2}<\frac{411}{4}.
\]

On \([a,b]\) with \(b=22/5\),

\[
F''(t)=\tfrac12 K''(t)[v-U(B-t/2)]
+\tfrac12 K'(t)U'(B-t/2)
-\tfrac18 K(t)U''(B-t/2).
\]

Because \(K'<0\), \(K''>0\),

\[
\int_a^b tK''(t)\,dt
 =bK'(b)-aK'(a)-K(b)+K(a)
 <a|K'(a)|+K(a)<\frac{851}{40}.
\]

Cauchy–Schwarz and the exact change of variables give

\[
\int_a^b|U''(B-t/2)|\,dt
 \le \sqrt{2(b-a)}\,\|U''\|_{L^2(-B,B)}
 <256\sqrt{43/5}<768.
\]

Consequently

\[
\begin{aligned}
\int_a^b|F''(t)|\,dt
&<100(851/40)+200(11)+(11/8)(768)\\
&=\frac{10767}{2}=5383.5<5384.
\end{aligned}
\]

This absolute bound is intentionally coarse but is *independent of enormous complex-plane source coefficient envelopes*, and already pays the genuine original NF413 curvature and all physical sources. It does **not** assume pointwise \(U''\) bounds.

## Exact rational composite midpoint enclosure

Let \(N\ge1\), \(h=(b-a)/N=43/(10N)\) and \(t_j=a+(j+1/2)h\). The midpoint Peano kernel on each panel has nonnegative absolute maximum \(h^2/8\), so

\[
\boxed{\left|\int_a^bF(t)\,dt
-h\sum_{j=0}^{N-1}F(t_j)\right|
<\frac{5384}{8}h^2=673h^2.}
\]

This bound does **not** rely on empirical mesh refinement, Gaussian exactness, or high derivatives inferred from low-order data. Numeric gates:

| Complete genuine remainder [1/10,22/5] | Certified absolute midpoint integration error (before outward Arb rounding and dyadic input radius) |
|---|---:|
| \(N=1024\) | \(<0.011868\) |
| \(N=2048\) | \(<0.002967\) |
| \(N=4096\) | \(<0.000742\) |
| \(N=8192\) | \(<0.000186\) |

The new source-native replay evaluates all 273 source groups *at every real rational midpoint* in 4096-bit outward Arb, then sums correlated terms and multiplies by the actual original kernel. The source dyadic coefficient uncertainty is separately paid by \(10^6S_0\). To see why that overcharge covers the new interval, the original source basis has the real physical derivative coefficient error \(|\delta U'(y)|\le10000S_0\) for \(|y|\le B\). Hence, for the *midpoint sum*, \(|\delta F(t)|\le2500tK(t)S_0\), while \(tK(t)<1+t\le27/5\) for this range. Therefore the total original mid-sum source discrepancy is \(<2500(43/10)(27/5)S_0=58050S_0<10^6S_0\). This is independent of Arb rounding. NF448 separately pays its own \(S_0\) prefix charge.

The native run loads and SHA-checks original NF445 derivative, NF447 known contribution and NF448 prefix JSON, and checks original NF413 curvature. It computes \(N=4096\) and an independent \(N=1024\) midpoint resolution and requires the two **separately paid analytical enclosures** to overlap. It then forms outward exact rational sums
\[
I_B=I_B[0,1/10]+I_B[1/10,22/5],\qquad
z(B)=Z_{\mathrm{known}}(B)+I_B,
\]
with unchanged NF447 \(Z_{\mathrm{known}}(B)\approx0.8977981482264882147\).

## Scope, candidate standing, and risks

**New accepted mathematical inference (conditional only on the already accepted NF413/NF445 facts):** a source-preserving all-remainder midpoint error of \(<673 h^2\). This is a proved *analytical error certificate*, independent of running a numerical integrator.

**Not yet accepted:** the numerical value of the entire \(I_B\) or \(z(B)\) until actual native source replay and CI are successful. Even an exact endpoint value or endpoint sign says nothing by itself about the full weighted \(J_7,J_8\) signed integrals \(\int pz\), \(\int z^2\), the original full NF410/NF404 scalar, W-ODD-NEG or RH.

This is a reasoned **method pivot** from NF448's proposed costly local-center Taylor/Cauchy windows. It exploits certified *real-axis Sobolev regularity* already available on the true source, not another lower-dimensional shadow. If the \(N=4096\) error of about \(7.42\times10^{-4}\) is too wide for the desired endpoint decision, the same rigorous architecture can be increased to \(N=8192\) or supplemented by true local-center Taylor only where required. No interpretation of convergence-by-mesh alone as rigorous is allowed.

**Custody:** new additive research branch stacked on NF448 PR #469; no change to canonical older data; no main merge. NF448 raw source numerical JSON remains due for permanent archival before GitHub Actions expiry 2027-01-31.
