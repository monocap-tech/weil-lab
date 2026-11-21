# PI009 — Direct Lean custody for finite-Gamma pilots; exact Fourier atom still open

**Independent PI### lane** based on PI008 #818 → PI007 #816 → PI006 #812 → PI005 #809 → PI004 #804 → PI003 #801 → PI002 #798 → PI001 #793. Registry #792. Does not modify NF### Phase III, IV### Phase IV, or CP### parallel investigations.

**Status at branch creation:** dedicated, source-aware Lean build+axiom audit workflow prepared; **no compiler receipt yet**. Original arithmetic/spectral dictionary at the classical level is unchanged. No global Weil positivity, RH/GRH, or validation of Masullo's operator trace.

## 1. Real audit finding: generic CI does not compile PI modules

At PI009's initial verification, the actual PI007 commit \`64939b1b382e92d9a8b7e140de08b21a5bad1a24\` had generic \`Lean\` Actions run **44856739800**, queued; PI008 commit \`4dec1583fb0f23797d211daf2121b9b91048e4d3\` had generic \`Lean\` run **44857500784**, queued. No successful compiler artifact or axiom audit from either was available.

More crucially, the genuine \`.github/workflows/lean.yml\` in the PI008 branch runs
\`lake build WeilDefect.Examples.WeakCriticalFallthrough\`
and checks for \`sorry\`/project axioms in source text. **It never directly imports or builds**:
- \`WeilDefect.Arithmetic.PI007FiniteGammaKernel\`
- \`WeilDefect.Arithmetic.PI008FiniteDigammaSymbol\`

The two PI modules are not included in \`WeilDefect.lean\` imports. Hence **even a PASS from the generic Lean job would not imply these two files had compiled**. PI009 corrects the custody path without changing the generic workflow or competing NF/IV proof modules.

## 2. New dedicated workflow: exact targets and strict receipts

\`.github/workflows/pi009-direct-lean-custody.yml\` triggers for PI source/audit changes. It runs:
1. Checkout and inspect source SHA/blob;
2. install exact pinned Lean and Mathlib v4.34.0 dependencies;
3. \`lake build WeilDefect.Arithmetic.PI007FiniteGammaKernel WeilDefect.Arithmetic.PI008FiniteDigammaSymbol\` (both exact target names);
4. require both nonempty \`.olean\` files;
5. direct \`lake env lean\` over each exact source, collecting the ten \`#print axioms\` records;
6. run \`scripts/pi009_strict_direct_lean_audit.py\`, rejecting missing or duplicated theorem records, nonstandard axioms, missing source/log/olean, malformed compilation status, and wrong mathlib pin. Its allowed axioms are only \`propext\`, \`Classical.choice\`, and \`Quot.sound\`.
7. Upload the source identities, compiler logs, axiom logs, receipt JSON, and physical \`.olean\` objects even if a later step fails.

**If any build or audit step fails, status is FAIL/OPEN.** A resulting PASS certifies **only** the ten elementary PI007/PI008 theorem candidates, not PI007/PI008's larger mathematical Gamma-to-real-place identities. This distinction prevents importing authority from a generic CI success.

No claim is made about earlier NF/IV compiler backlog clearing. PI009 adds an explicit narrow workflow but does not relabel queued run results as proofs.

## 3. The authentic next mathematical formalization obligation

Freeze the real atom Fourier theorem with the **actual source positive Fourier convention**. For all \(\alpha>0\) and \(r\in\mathbb R\):
\[
\boxed{
\int_{\mathbb R} e^{-\alpha|u|}e^{iru}\,du
=\frac{2\alpha}{\alpha^2+r^2}.
}
\tag{PI009-atom}
\]
Set \(\alpha=2n+1/2=2a_n\), \(a_n=n+1/4\); then
\[
\frac{2\alpha}{\alpha^2+r^2}
=\frac{a_n}{a_n^2+(r/2)^2},
\]
which is **exactly** the rational term in the original \(\Omega_N\) partial fractions.

The theorem requires an actual Lean complex-integral proof: split the real line into positive and negative half-lines, use the complex exponential integral for positive real part, justify integrability and the substitution, and algebraically reconcile the two reciprocal factors. The required identity is not supplied by merely writing a paper proof or by the existing upstream \`gammaR_bracket\` theorem.

After the atom is kernel accepted, PI010 must prove the finite-stage source equality
\[
\frac1{2\pi}\int \operatorname{paperFT}(h)(r)\Omega_N(r)\,dr
=(H_N-\gamma-\log\pi)h(0)
-\int h(u)K_N(u)\,du,
\]
with the correct \(2\pi\), integrability, and Fourier inversion hypotheses. Then formalize PI008's \(\frac3N+\frac{8r^2}{N^2}\) frequency error and PI007's physical \(\alpha_N\)-tail to take both limits in Lean.

Only the last source-bound stage should be attached to the actual IV011 \`neutralIV011OriginalMixedArch\` in a **separate PI companion based on an IV branch**, because the PI branch intentionally has no original IV011 module. A theorem importing an unavailable IV module from PI009 is invalid and must not be written as a compiler-accepted claim.

## 4. Source and scope preservation

- Actual upstream \`Zeta23.paperFT\` positive angular exponent: blob \`8024700cbfefb54d763b487afa84c03fef58a550\`.
- \`Zeta23.EF.gammaBracket\` literal digamma symbol: blob \`11119489556113fd419d7b6fb45ccbaa2e493e2a\`.
- \`Zeta23.DigammaSeries.hasSum_digamma_series\` source theorem: blob \`2c6cf90050c2e6d5cbef0745d0445e3a8d02394a\`.
- Weil-Lab IV011 actual arithmetic source: blob \`14d8f01ce34f764900eccc68399d7323b4f4a25c\` on PR #774.
- PI007 and PI008 mathematical preflights are **exact-rational external arithmetic**, not compiler evidence. Their analytical Fourier/Gamma assertions remain paper-level.
- Masullo's full trace and his excluded diagonal tests still need independent verification; PI006 proves why mixed tests alone cannot recover an absolute positivity margin.

**PI009 completion gate:** only state \`LEAN PASS\` for finite pilots after matching action conclusion, source SHA, nonempty \`.olean\`, and strict ten-theorem axiom receipt. Until then **compiler pending**. The real PI009 advance is removal of a misleading verification route; the Fourier-atom and Gamma transport theorems remain explicit falsifiable formal obligations.
