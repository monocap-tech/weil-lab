# NF579 — literal normalized collar mollifier and direct spectral-sample graph convergence

Stacked on NF578 PR #609. At inspection its focused run 44029579404 was still queued. No new Lean PASS claim in NF579.

## Main analytical simplification

Once the true target and smooth seed have a common full strip envelope, NF575's independent physical L2 convergence premise can be weakened to pointwise convergence of the *literal real-axis window samples*. The weighted dominated-convergence argument in NF575 only used physical convergence to deduce these scalar limits. Its actual log-norm squared identity, Fourier a.e. dictionary, and integrable majorant remain unchanged. The NF579 variant takes the scalar limits directly; the old NF575 theorem is retained as a wrapper. The full two-source divisor graph theorem then follows through NF574 as before (all pending dependency acceptance).

For the authentic one-collar half h and s tending to 1 through (1/2,1), with c=1099/1000 and epsilon=(1-s)/2000, choose the actual normalized ContDiffBump of inner radius epsilon/2, outer radius epsilon. Put h_s(x)=h(c+(x-c)/s), v_s=rho_s*h_s, g_s=v_s-v_s(-x). The new Lean candidates construct rho_s (real nonnegative, even, smooth, compactly supported and mass 1); prove integrability of the compressed half from integrability of h via two reflections and one dilation; establish smoothness and pointwise confinement of the odd seed; and bound the literal complex transform of rho_s by exp(epsilon/2) on the full strip.

The transform identities implemented as Lean candidates are
H_s(z)=s exp(i z (1-s)c)H(sz),
V_s(z)=R_s(z)H_s(z).
The latter uses integrability of the actual twisted factors and applies Mathlib's integral_convolution to the exponentially twisted complex functions. The affine identity uses the exact change of variables, not an assumed Fourier scaling formula. Twisted-factor integrability from compact support and physical integrability remains to be connected. The positive-exponent raw transform is used consistently (native Fourier coordinate -2 pi ξ).

For fixed real t, R_s(t) tends to 1: since rho_s>=0, mass=1 and |y|<=epsilon,
|R_s(t)-1| <= sup_{|y|<=epsilon}|exp(i t y)-1| <= |t| epsilon.
Also H(st) tends to H(t) by dominated convergence for integrable h, as the real-axis exponential has modulus 1. The affine phase tends to 1 and s tends to 1. Thus V_s(t) tends to H(t), and odd reflection gives pointwise convergence of G_s(t) to F_ell(t). No independent proof of physical dilation strong continuity or L2 approximate identity is required for this route. A common strip envelope still must be proved using the actual endpoint Fourier estimate and these identities. NF577 gave that analytical estimate. The raw-transform to literal window evaluation dictionary and toLp realizations for these seeds, and formal scalar limits, are not yet implemented.

## New local exact source replay

Executed Python Fraction directly on the recovered NF494-native.zip in this pass. The raw member was nf494-original-J8-source-H400-joint-compact-native.json (996666 bytes); SHA256 39cba367d70243c2d15e5a9323fc8097d58187923dcf0eca2b031136871f0181; original source and seam hashes matched. Consumed all 400 outward intervals with the original 10^400 holomorphic majorant and radius 1/25; exact gates PASS. Printed M0=1.9659655557684862e-7, M1=0.0006957098822919963, endpoint upper=-1.16798644909683e-11, Cauchy tails 4.076412541946651e-121 and 8.153897824035919e-116; high/low scalar sufficient comparisons 1.26268032e-5 and 1.6032e-6 both <1/40000. This explicitly verifies the arithmetic on the raw bytes, not the inherited majorant theorem or Lean source binding.

## Standing

New Lean implementations committed and focused CI configured, not compiled locally (no Lean installation). Existing compiler-certified original 242-column left-kernel theorem and generic square transport stand. Terminal Gram verification still pending. The direct scalar sample route is a chosen simplification of the historical construction, not a change of carrier. No axiom/sorry/admit intentionally introduced. No main merge. Next formalize fixed-frequency limits, compact support/twisted integrability and the actual endpoint Fourier split; complete actual U source attachment. Full signed Weil coercivity, W_ODD_NEG and RH OPEN.
