# NJDG-7 — direct weighted critical identity screen and derivative-divisor TSTOP

**Date:** 2026-09-30  
**Repository:** monocap-tech/weil-lab  
**Branch:** \`research/nextjet-derivative-geometry\`  
**Status:** **COMPLETE SCREEN / NO GENUINELY NEW DIRECT WEIGHTED CRITICAL IDENTITY LOCATED / THE CANONICAL WEIGHTED CONTOUR FOR RENJET USES XI'/XI AND THEREFORE SEES ORIGINAL XI-ZEROS AS POLES WHILE XI'-ZEROS ARE ZEROS, NOT RESIDUES / SWITCHING TO XI''/XI' MAKES DERIVATIVE ZEROS VISIBLE ONLY BY SWITCHING TO THE DERIVATIVE DIVISOR / SEPARATE XI AND XI-PRIME EXPLICIT FORMULAS DO NOT SUPPLY A MIXED-DIVISOR TRANSFER / FINITE LOCAL CRITICAL IDENTITIES REMAIN RATIONAL-RESOLVENT BY NJDG-6 / NJDG PLACED AT TSTOP PENDING GENUINELY NEW MIXED-DIVISOR WEIGHTED INPUT / NEXTJET NOT PROVED**  
**Parent:** NJDG-6  
**Canonical Key-C status:** unchanged

## 0. Objective

NJDG-6 proved that finitely many derivative-critical value/curvature rows cannot exactly synthesize the frozen exponential RENJET kernel.

NJDG-7 therefore asks the last currently licensed derivative-geometry question:

> Is there a direct identity at derivative critical points whose zero-side kernel is already the frozen SOURCE-II exponential/mode-weighted kernel, so no finite rational interpolation is required?

The answer under the located and derived identities is **no**.

The obstruction is a change of divisor.

## 1. Original-divisor logarithmic derivative

Let

\[
U(z)
=
\frac{\Xi'}{\Xi}(z).
\]

Its meromorphic poles occur at the zeros \(\rho\) of \(\Xi\), with residues \(m_\rho\).

Hence a weighted contour integral such as

\[
I_t(\Gamma)
=
\frac{1}{2\pi i}
\oint_\Gamma
\frac{e^{t(z-c)}}{(z-c)^2}
U(z)\,dz
\tag{1}
\]

has zero-side residue contribution

\[
\boxed{
\sum_{\rho\in Z(\Xi)\cap\operatorname{int}\Gamma}
m_\rho
\frac{e^{t(\rho-c)}}{(\rho-c)^2}.
}
\tag{2}
\]

After selected-pole removal, cutoff bookkeeping, and the collision-safe finite-part correction, this is exactly the kernel species appearing in the first RENJET.

Thus the exponential weighting itself is not mysterious: it is naturally produced by a weighted contour on the **original divisor**.

## 2. A derivative critical point is invisible to the residue sum

Let \(\tau\) be a simple zero of \(\Xi'\) with \(\Xi(\tau)\ne0\).

Then

\[
U(\tau)=0.
\]

Therefore \(U\) is analytic at \(\tau\), and in fact vanishes there.

Consequently \(\tau\) contributes **no residue** to (1).

So the direct weighted contour that exactly reconstructs the RENJET zero kernel does not automatically acquire any new term from a derivative critical point.

This yields:

\[
\boxed{
\Xi'(\tau)=0
\quad\text{is a zero of the RENJET carrier }U,
\text{ not a pole of it.}
}
\tag{3}
\]

That is why ordinary critical-point insertion does not directly produce a weighted zero-side identity.

## 3. Switching to the derivative divisor

To make derivative critical points appear as poles, one naturally passes to

\[
V(z)
=
\frac{\Xi''}{\Xi'}(z).
\]

Now zeros of \(\Xi'\) are poles of \(V\).

A weighted contour

\[
J_t(\Gamma)
=
\frac{1}{2\pi i}
\oint_\Gamma
e^{t(z-c)}V(z)\,dz
\]

therefore generates weighted sums over the zeros of \(\Xi'\).

But the divisor has changed.

The elementary identity is

\[
\boxed{
\frac{U'}{U}
=
\frac{\Xi''}{\Xi'}-\frac{\Xi'}{\Xi}
=
V-U.
}
\tag{4}
\]

Equation (4) relates the two logarithmic derivatives as functions, but its poles split between two different divisors:

- \(U\): original \(\Xi\)-zeros;
- \(V\): derivative \(\Xi'\)-zeros;
- \(U'/U\): zeros and poles of the meromorphic function \(U\).

Nothing in (4) assigns the original-divisor exponential weights in (2) to derivative-critical residues packet by packet.

## 4. Separate explicit formulas do not provide a mixed-divisor theorem

The GitHub screen located explicit-formula and pair-correlation machinery for zeros of \(\Xi'\), including the Farmer–Gonek–Lee lineage and later implementations.

Those formulas are legitimate analytic objects for the derivative divisor.

But a pair of separate formulas

\[
\text{EF}_{\Xi}
\qquad\text{and}\qquad
\text{EF}_{\Xi'}
\]

does not imply a mixed relation

\[
\text{weighted original-divisor response}
=
\text{controlled derivative-divisor response}.
\]

The missing step is exactly a **mixed-divisor weighted identity**.

A hostile audit in \`x67ai/riemann-rh-program\` independently flags the same category error: \(\Xi\)-zero data and \(\Xi'\)-zero data are distinct analytic objects, and a kernel built from the functions \(\Xi,\Xi'\) is not automatically a correlation theorem for their two zero sets.

NJDG-7 adopts this as a source-screen control, not as canonical project custody.

## 5. Local differential identities remain finite rational resolvents

One might avoid the divisor switch by applying weighted differential operators directly to

\[
U=\Xi'/\Xi
\]

at a derivative critical point.

Let

\[
P_t(\partial)
=
\sum_{k=0}^{r}
a_k(t)\partial^k
\]

be any finite-order differential operator whose coefficients may depend on the already frozen SOURCE-II mode \(t\).

Applied to a zero pole

\[
\frac1{z-\rho},
\]

one obtains a finite combination of

\[
\frac1{(\tau-\rho)^{k+1}}.
\]

Multiplying by the local scalar factor \(e^{t(\tau-c)}\), or differentiating \(e^{t(z-c)}U(z)\) finitely many times before evaluating at \(\tau\), changes only the coefficients.

The zero-side kernel remains a finite rational-resolvent combination.

Therefore NJDG-6 applies unchanged:

\[
\boxed{
\text{finite local weighted differentiation at critical points}
\not\Rightarrow
e^{t(\rho-c)}\text{-weighted RENJET kernel}.
}
\tag{5}
\]

## 6. Infinite-order/contour reconstruction returns to the original explicit formula

There is a formal way to generate exponential zero weights: use an infinite/generating transform or contour integral.

For example, (1) already does so exactly.

But that construction reads the whole original divisor through \(U\). It does not become easier because \(U(\tau)=0\) at a derivative critical point.

Likewise, a Cauchy/Laplace transform over a continuum of critical rows could in principle synthesize an exponential kernel, but it would require:

- a controlled continuum or growing family of derivative-critical data;
- a measure/conditioning theorem on that family;
- an exact mixed-divisor transfer back to the original zeros.

No such input is in custody.

Thus the infinite-transform escape is logically open but is no longer an internal derivative-geometry calculation.

## 7. Relation to the existing complement wedge

For the selected-only frozen mode pair \(t,u\), the canonical tower values are

\[
T(t),\qquad T(u),
\]

and the multiplier-free complement wedge is

\[
\boxed{
W_{\rm cmp}^{(K)}(t,u)
=
C(u)T(t)-C(t)T(u).
}
\tag{6}
\]

Any weighted contour using \(U=\Xi'/\Xi\) that reconstructs the mode-weighted original-divisor tower and is then combined by the same frozen coefficients \(C(u),-C(t)\) yields exactly the same object class as (6).

So a “direct weighted identity” on the original divisor that does not use derivative-critical structure is merely a contour representation of the existing complement wedge.

Conversely, switching to \(V=\Xi''/\Xi'\) creates a derivative-divisor wedge and leaves a new mixed-divisor transfer theorem to be proved.

Hence the two options are:

\[
\boxed{
\begin{array}{ll}
\text{stay on original divisor} &\Rightarrow \text{existing complement wedge},\\[1mm]
\text{switch to derivative divisor} &\Rightarrow \text{new mixed-divisor theorem required}.
\end{array}
}
\tag{7}
\]

There is no third direct identity produced by ordinary criticality.

## 8. Source screen

The NJDG-7 GitHub search targeted:

- exponential weighting of logarithmic derivatives at derivative zeros;
- explicit formulas for zeros of \(\zeta'\) and \(\Xi'\);
- Mellin-weighted derivative-critical identities;
- mixed \(\Xi\)/\(\Xi'\) zero correlations.

Located relevant families:

1. Farmer–Gonek–Lee style explicit formulas / pair correlation for \(\Xi'\)-zeros;
2. higher-\(\Xi\) derivative resolvent work in \`teal-sea/zeta-lab\`;
3. mixed-\(\Xi,\Xi'\) exploratory programs in \`x67ai/riemann-rh-program\`;
4. generic Mellin/logarithmic-derivative identities.

No located source supplied an exact packet-local identity mapping the derivative divisor to the frozen original-divisor RENJET kernel.

The closest mixed-\(\Xi,\Xi'\) program explicitly records that this bridge is absent and that conflating function-level kernels with zero-set correlations is invalid.

**Source determination:** NO HIT.

This is a bounded GitHub/source audit, not a literature-exhaustion theorem.

## 9. NJDG-7 determination

- Exponential weighting of the original zero divisor has a direct contour representation: **YES**.
- That representation uses \(\Xi'/\Xi\): **YES**.
- Simple \(\Xi'\)-zeros contribute residues to that contour: **NO**.
- Replacing \(\Xi'/\Xi\) by \(\Xi''/\Xi'\) makes derivative zeros visible: **YES**.
- It preserves the original zero divisor: **NO**.
- Separate explicit formulas for both divisors provide a packet-local mixed transfer: **NO**.
- Finite local weighted differentiation evades NJDG-6 rational-kernel nonspan: **NO**.
- Infinite/continuum transforms are internally available with controlled derivative-critical data: **NO**.
- An original-divisor weighted contour creates a new theorem class beyond RH-T0117: **NO**.
- A derivative-divisor weighted contour closes RENJET without new mixed input: **NO**.
- Genuinely new direct weighted critical identity located: **NO HIT**.
- NEXTJET proved: **NO**.
- KPH floor proved: **NO**.
- RH proved: **NO**.

## 10. Branch determination

The derivative-geometry investigation has now exhausted the licensed internal and source-screen routes:

1. raw selected/exterior collision \(\to\) derivative capture;
2. quartet/Speiser localization;
3. cofactor blow-up;
4. critical-point frames;
5. curvature enrichment;
6. finite mode-weighted curvature synthesis;
7. direct weighted critical identities.

Every surviving route now requires a theorem not currently present in the branch:

- a genuinely new mixed-divisor weighted identity;
- a continuum/growing-family critical transform with projective conditioning;
- an actual-zero interpolation theorem on the frozen mode-weighted kernel;
- or direct control of RH-T0117 / the canonical KPH floor.

Therefore set

\[
\boxed{
\texttt{TSTOP-NJDG-PENDING-NEW-MIXED-DIVISOR-WEIGHTED-INPUT}.
}
\tag{8}
\]

This TSTOP is an investigation stop, not a proof that all future derivative-zero methods are impossible.

## 11. Re-entry contract

NJDG may reopen only if a new source or construction supplies at least one of:

### R1 — mixed-divisor weighted law

A theorem directly relating the frozen mode-weighted original-\(\Xi\) zero response to derivative-zero data with every-dangerous-packet control.

### R2 — conditioned growing critical transform

A growing/continuum family of derivative-critical rows whose transform reconstructs the exponential kernel with projective conditioning and the correct selection order.

### R3 — actual-zero weighted interpolation

A theorem specific to the actual finite near zero set that synthesizes the frozen exponential kernel from derivative-critical data at projective cost.

### R4 — direct canonical closure

A theorem directly controlling
\[
W_{\rm cmp}^{(K)}
\]
or proving
\[
C\text{-ACTUAL-KPH-FLOOR}.
\]

Anything weaker remains outside the re-entry contract.

## 12. Cursor

There is no automatic NJDG-8.

Current branch cursor:

\[
\boxed{
\texttt{TSTOP-NJDG-PENDING-NEW-MIXED-DIVISOR-WEIGHTED-INPUT}
}
\]

Do not continue with another coordinate or finite-jet rewrite.
