# RPB108 EF09 — same physical original even refined-cap lower, without changing the operator

**Priority:** W-EVEN-FORM (2); canonical W-ODD-NEG remains separate and unmodified.  
**Parent:** EF08 reconciled branch head `e905cac16d8b930925c92ca3ad440f891fb206f9`.  
**Standing:** candidate original *conservative cap method discriminator*, not actual original even positivity or negativity.

## The exact narrow question

On the original zero-extended physical supported cosine

\[
f(x)=\cos(2\pi(19/25)x)\mathbf 1_{[-11/10,11/10]}(x),
\]

EF08's exact-rational all-frequency **positive** energy upper is below
\(877811/10^6=0.877811\), including the actual signed Fourier multiplier
and positive even pole. EF07 certified the **conservative** cap lower
\(0.8023309563\), with [0,1] lower >0.7346753311 and [1,4] lower
>0.0676556251. Their intervals overlap by at most 0.0754800447 under
the looser rounded EF08 upper.

EF09 does NOT change the multiplier \(m\), original cap \(K_{\rm cap}\),
the physical function \(f\), or the pole. It refines only the *integration
lower bound* of the cap on the same physical vector.

For an original refined cap leaf \([a,b]\) with certified constant
weight \(w\ge0\), partition it into \(N\) exact rational subcells.
On each subcell \(I=[u,v]\), evaluate the original physical supported
Fourier transform at its rational midpoint with an interval sine
enclosure, and subtract the valid whole-cell global derivative allowance
\(\|F'_z\|_\infty(v-u)/2\). If the resulting outward-rounded amplitude
lower is \(L_I\ge0\), then

\[
2\int_{u}^{v}w|F_z(\xi)|^2\,d\xi
\ge 2w(v-u)L_I^2.
\]

This is a lower integral of the *unchanged* cap and does not rely on
a point evaluation for an entire interval.

- Refine 256 existing [0,1] EF06 cells by 4 exactly.
- Refine the 121 existing original [1,4] cells by 16 exactly.
- Preserve all 788 high leaves with safe lower bound 0 (nonnegative).
- Preserve the full cap mass identity \(29.60374846875\).
- Compare the resulting exact-rational total to the separately verified
  EF08 original positive upper \(877811/10^6\).
- Report the sign without predetermining it.

**If positive:** \(\langle f,K_{\rm cap}f\rangle >
\langle f,A_ef\rangle\) is a counterexample to the *conservative*
operator domination \(K_{\rm cap}\preceq A_e\), **not** proof that
\(\langle f,K_{\rm true}f\rangle>\langle f,A_ef\rangle\).
Actual original \(K_{\rm true}\preceq K_{\rm cap}\) may have a much
smaller quadratic. Refine the cap or return to the direct original
signed two-vector/finite operator.

**If nonpositive:** only the current bounds remain inconclusive.
No assertion of method feasibility follows.

## Verification and custody

Script: `scripts/validate_rpb108_ef09_even_cap_lower_refinement.py`.
Workflow: `.github/workflows/rpb108-ef09-even-cap-lower.yml`.
Final-head exact-rational CI and governance replay pending.
EF08 whole-positive numerical bound is an explicit separately certified
premise, not recomputed by EF09; a valid joint conclusion requires
retention and independent audit of both exact-rational certificates.

**No full even-sector PSD, actual-zero global bridge, Lean original-form
attachment or RH proof is claimed.**
