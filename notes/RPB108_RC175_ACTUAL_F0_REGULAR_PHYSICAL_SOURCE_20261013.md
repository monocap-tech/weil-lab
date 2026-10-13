# RPB108 — RC175: actual f0 regular physical source and mixed canonical rows

Aperture 11/10. Parent RC174: `d771d3d3e19cf3604d6fdf27984299c8e0f2f637`.
Only `research/rpb108-route-consolidation` is written. Historical checkpoints, source frames and Lean remain unchanged.

RC175 evaluates the compressed regular action on the actual native f0 source. It represents the entire physical output function, pays its full source error, and certifies the canonical mixed pairings with P0 and P2. The output is signed; its sign is not replaced by independent positive magnitudes. The complete output Legendre carrier has not yet been realized.

| Paid component | Outward norm upper |
|---|---:|
| Complete physical L2 error in represented R f0 | 0.000213556 |
| Induced D-energy error after D^-1 | 0.000109529 |
| Whole-interval uniform physical source error | 0.002694980 |

The input is RC126/129's exact f0 with eta coefficients at every even degree 2..988. RC174's accepted 10^-4 regular input-tail component budget selects degree 172. RC175 constructs the 86 positive rational coefficient centers at even degrees 2..172 and pays their actual-constant radii. The omitted finite input is retained in the error bound.

## Near-node output function

Use u=x/B, h=t/(2 pi_kernel B), z=u+i h and

\[
Q_n(z)=\frac12\int_{-1}^1\frac{P_n(v)}{z-v}\,dv.
\]

The physical Poisson action on a polynomial sum alpha_n P_n is exactly

\[
(P_tq)(u)=-\frac2{\pi_{kernel}}
\operatorname{Im}\sum_n\alpha_n Q_n(u+i h).
\]

Partial fractions of h/[pi_kernel((u-v)^2+h^2)] prove this identity. The same elementary Q recurrence as RC171–172 evaluates every retained input degree. For real u in [-1,1],

\[
\operatorname{Re}Q_0=\frac14\log\frac{(u+1)^2+h^2}{(u-1)^2+h^2},
\]

\[
\operatorname{Im}Q_0=-\frac12\left[
\arctan\frac{1-u}{h}+\arctan\frac{1+u}{h}\right],
\quad Q_1=zQ_0-1.
\]

The finite weighted sum over the 2,198 near nodes is an exact physical function representation, with the prescribed rational source centers, nodes, weights and kernel pi. Directed 360-digit interval evaluation encloses this function at 0, B/2 and B. Each scalar logarithm and arctangent remainder is paid. Future coefficient integrations must pay their own arithmetic; the three sample evaluations do not replace that task.

## Far-node output polynomial

The 1,898 far nodes use the same 32-term symmetric polynomial in u-v as the historical P0/P2 regular columns. Its degree-62 output depends only on input monomial moments through degree 62, even though the input polynomial reaches degree 172. Higher Legendre input degrees annihilate those moments exactly.

For even j, the required input moment is

\[
\int_{-1}^1v^j q(v)\,dv
=\sum_{n\le j,\ n\ even}\alpha_n
\frac{2j!}{(j-n)!!(j+n+1)!!}.
\]

Signed far-node moments are accumulated before forming the output polynomial. Its rational coefficient centers and radii are stored. The kernel remainder is at most (2c)^65/pi_kernel times the input supremum bound at each node, with c=2 pi_kernel B/t. Legendre's |P_n|<=1 gives the input bound sum |alpha_n|. Output polynomial coefficient rounding is paid uniformly by the sum of radii.

## Complete source error

Let q be the retained rational center input and f_tail the actual discarded degrees after 172. The physical L2 error is bounded by the sum of:

- RC174's high-input-mode regular factor times ||f_tail||_2;
- r times the physical coefficient-center error, with r=789/125;
- RC170's physical operator error times ||q||_2;
- kernel-pi replacement error times ||q||_2;
- sqrt(2B) times the complete far-kernel and polynomial-rounding uniform error.

Every term is rational and outward. D>=s_lower I gives the induced D-inverse error after division by a rational lower bound for sqrt(s_lower). The certificate stores the full input center/radius data and their digest, so the true source is not silently replaced by its center.

For uniform output error, the actual regular kernel has ||k||_2^2=2I2. Cauchy–Schwarz pays the discarded input and center error by sqrt(2I2) times their physical norms. RC170's Linfinity operator error, the pi error and the far polynomial remainder pay the other terms. This produces true-action intervals at each sample, as well as a bound valid throughout the physical interval. The underlying convolution is continuous for these L2 inputs, so the pointwise representative is fixed.

The represented output at the center is negative, near -0.134699, and at the endpoint positive, near 0.178380. Positive selfadjointness of R is an operator statement; this sign-changing output from the sign-changing f0 input is consistent with it.

## Retained output coefficients and actual canonical rows

The same symmetric approximation is evaluated in RC171/172's P0 and P2 columns. Its f0 output coefficient at degree i=0 or 2 is

\[
\widehat g_i=\sum_{n\le172,\ n\ even}
\alpha_n\frac{2i+1}{2n+1}(\widehat R P_i)_n.
\]

RC175 keeps the signed inherited coefficient intervals and pays the full physical output error divided by sqrt(m_i) to obtain actual R f0 coefficient intervals. This identity applies to the common near kernel and the identical symmetric far polynomial; it does not assume self-adjointness of an arbitrary input-truncated action map.

The actual canonical mixed entries then retain the full finite endpoint sums, the exact D overlap and the -r physical mass overlap. The accepted outward intervals are:

| Actual canonical pairing | Lower | Upper |
|---|---:|---:|
| <P0,L f0> | 0.0210692497 | 0.0217027587 |
| <P2,L f0> | 0.0995478422 | 0.0998311561 |

These are two mixed rows, not a full three-source Gram certificate. In particular the diagonal f0 canonical energy and joint action data needed for a three-source inverse have not been evaluated here.

## Source-form canonical trial and remaining work

The inherited full action Cf0 approximately equals w14 with its paid error below 6.997e-26. Thus

\[
f_0+w_{14}-rD^{-1}f_0+D^{-1}\widehat g
\]

is a source-form trial for D^-1 L f0. Its D-error upper is the new regular source's induced error plus the old Cf0 error, still below 0.000109529. The diagonal inverse of the explicit physical L2 function is well-defined in the complete D carrier. This construction does not assert that all of its numerical Legendre coefficients or a usable endpoint-output tail have been materialized.

Next: project this represented regular source into an actionable finite/analytic output carrier with full tail payment, or pay the remaining diagonal and correlated data needed to add f0 to canonical inversion. RC173's two-source inverse and RC174's seven-source input contracts remain intact. Full-family canonical inversion, final Stage I tolerance/closure, original Weil or augmented actions, whole-aperture positivity, Global/F4, RH and Lean remain open.

## Reproduction

Run `scripts/validate_rpb108_rc175_f0_regular_physical_source.py --output certificates/rpb108_rc175_f0_regular_physical_source.json` with RC174, RC172, RC171, RC170, RC169, RC121 and RC129 certificates in that order. Repeat with `--replay`. Replay reverses every Poisson node, signed source moment, inherited mixed-row sum and full endpoint sum and compares the complete rational certificate. Only additive RC175 files are committed.
