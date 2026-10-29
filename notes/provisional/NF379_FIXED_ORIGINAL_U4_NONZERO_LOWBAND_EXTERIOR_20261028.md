# NF379 — Fixed original u4 cannot have exactly zero lowband unfitted response

**2026-10-28 Pacific | Canonical W-ODD-NEG OPEN | ANALYTIC QUALITATIVE RESULT.** This is a bounded continuation of the Mittermeier sign-box comparison, not a theorem-level signed positivity conclusion. No external-method promotion, no original-domain closure, no new original source, and no claim that the NF375 numeric threshold has failed. Draft PR #361.

## Previous / current / next

**Previous cursor:** NF377 constructed 492 original physical odd annuli and a source-pinned native selector, but all last-checked native annulus runs were QUEUED and no specific index was accepted. NF378 proved finite sign-box values alone cannot provide a universal original lowband upper certificate even for images of the true lowband operator. This generic countermodel did not identify what happens to the FIXED original NF370 fourth trial.

**Current result:** On the **specific inherited NF370 original fourth source** u4, the accepted NF376 native signed-point certificate at real frequency xi=1/4 proves both m(1/4)>0 and the sine Fourier amplitude of u4 is strictly positive. Combined with entire continuation, this proves the actual lowband physical response cannot lie exactly in ANY finite-dimensional original selected-plus-fitted space J242+E4. Therefore its unfitted lowband norm is STRICTLY POSITIVE, qualitatively. This is a fact about the fixed u4, unlike the previous arbitrary-source dimensional counterexample.

**Next:** Quantify, with outward error, one true original signed pairing of this nonzero residual with a *certified specific annular diagnostic*; if its normalized dual exceeds the NF375 direction-four threshold 1.5e-13, STOP only that sufficient method. The qualitative statement below is not a substitute for this integral.

## Source-premise audit

SHA-pinned native original point certificate:
- `notes/data/provisional/NF376_native_original_fifth_quotient_signed_lowband.json` (Git blob `94b4825b63d72e8a8f07f8693359ad11043092c0`).
- Original rank SHA256 `9b9820a0163e5e8bf08dd1c2525c757ff67214b49a40cb093d00bc611c9ff9e2`; PR355 source SHA256 `abd37707d585dcd54b040f1ae865a7430a9c7cba85df31131661b2e72e560770`; NF369 fields SHA256 `3e73a12bbd70158a461d9722dc8fc499eee8d17baf0afc9090bac5d10165e7e8`.
- Its rational signed multiplier at xi=1/4 satisfies `507144821183/200000000000 <= m(1/4) <= 633931149017/250000000000`; the lower endpoint is STRICTLY POSITIVE.
- At the same xi, both outward integer endpoints of the actual original `u4` sine amplitude times 10^320 are strictly positive. This is a true original physical Fourier amplitude, not an arbitrarily postulated source, and was computed at 4096-bit native precision.
- The exact Fraction/integer premise assertions, including original Git blob and source SHA, are retained in `scripts/local_replay/nf379_fixed_u4_lowband_nonfit_premises.py`. This script has not been independently run through a new CI in this note; the reported positive interval was read and checked directly from the archived original native record.

## Lemma — fixed u4 lowband response lies outside original J242+E4

Let `I=(-B,B)`, `B=11/10`, `Lambda=2^20` and the inherited real-even continuous original signed multiplier m. Define the global bandlimited function

`G(z) = int_(-Lambda)^Lambda m(xi) hat(u4)(xi) exp(2pi i xi z) dxi`,

and its physical restriction `g4_low=G|I`. Since the band is compact, m is continuous and hat(u4) is continuous, G is an ENTIRE function of z and `G|R\in L2(R)` (Plancherel). Because both m(1/4) and hat(u4)(1/4) are nonzero, their product is nonzero on an open spectral interval; therefore `G\not\equiv0`.

Let `S=J242+span(E1,...,E4)`, with `E=QF`. Each generator of original J242 and original four PR355 F functions, restricted to I, is a finite exponential polynomial: finitely many `x^k sin(2pi c x)`, `x^k cos(2pi c x)` with real rational c, and `sinh(x/2)`. Consequently every element of S has an ENTIRE finite exponential-polynomial continuation `p(z)`. Every NONZERO such p has `p|R\not\in L2(R)` (the real exponentials grow in at least one direction; a nonzero finite real-frequency polynomial trigonometric sum has nondecaying mean-square growth). This non-L2 claim is an elementary finite-exponential-polynomial lemma, not an assumption of RH.

Suppose `g4_low\in S`. Then `G(x)=p(x)` for all x in the open interval I for some p in S. Entire identity uniqueness gives `G(z)=p(z)` for all complex z. But `G|R\in L2(R)`, while nonzero p is not. Hence p=0 and G=0, contradiction. Therefore

`g4_low \not\in S`.

Since S is finite-dimensional/closed in L2(I),

`|| (I-P_S)g4_low ||_(L2(I)) > 0`.

Thus, for the ACTUAL u4, the unfitted direction-four lowband residual is strictly nonzero even after removing original J242 and all four fitted E probes.

Additionally the complete continuum of odd physical sign-box tests is L2-dense in the odd carrier: there EXISTS some real t∈(0,B] with `<g4_low,(I-P_S)o_(2t)>!=0`. This does NOT imply that one of the preselected 492 annuli has a nonzero pairing (NF378 supplies the data-type obstruction), still less that its normalized pairing exceeds NF375 h4.

## Decision, exact remaining obligation

**PASS analytic qualitative:** fixed original u4 produces a nonzero bandlimited response outside every original finite-exponential-polynomial selected/fitted space, using *certified* inherited native nonzero values at xi=1/4 and the original function inventory.

**NOT certified:** any numerical lower `||(I-P_S)g4_low|| >= epsilon`, any 492-cell pairing, the strong signed lowband integral `I4(q;Lambda)`, NF375 h4 comparison, exact Suzuki-to-original full-frequency sign/pole matching, and complete infinite original exterior inverse. It is possible for a strictly nonzero residual to be *below* the stringent 1.5e-13 sufficient norm threshold.

**Promotion** still requires a genuinely quantitative, independently replayed original witness that changes the active acceptance/STOP test. **Closure** remains the entire original W-ODD-NEG O1/O2 form/infinite remainder conditions; even/whole/RH remain OPEN.

**Custody/stop:** Additive result and standard-library native-premise checker. Earlier 492-annulus original 4096-bit CI was still QUEUED at last retrieval, not silently promoted. No new branch or retyping of the canonical obligation.
