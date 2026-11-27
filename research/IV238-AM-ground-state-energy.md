# IV238 — Original AM ground-state energy (delegated W02 continuation)

## Scope and dependencies

Owner ratified canonical-return@d4e482f2f616112dca11f6d8fd803a3dffb5a80c research/regroup-001/W02_CONTINUATION_AMENDMENT.md. Continue IV-AM only. Parent custody a718024dece88339096e0e1d4de301fd82a87c89; original verification source 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0 remains unchanged. Its original terminal run 45930758374 passed; prior raw-byte remote readback limitation remains recorded, not silently waived. This operation does not consume its integrated proof objects or rely on the terminal theorem. It uses the independently reproducible frozen cell data and original analytic dictionary. Claim tier: explicit analytical proof plus exact integer replay, not a new native Lean receipt.

Pinned source dependencies at 12da3689018ed2c6e7e3965f1386cb44f0f0f8a0:
- WeilDefect/Arithmetic/ActualZetaIV162AMOriginalPrimeCore.lean blob 27e13eeb38c1132be4be135412b05d63871ba68a: original literal finite form for supported Schwartz; 24 prime powers.
- WeilDefect/Arithmetic/ActualZetaIV157AMOriginalDictionary.lean blob b86530e112ccc54ce0a39a45e735e9422e67941d: original weights and signed shifts.
- WeilDefect/Arithmetic/ActualZetaIV156AMPhysicalForm.lean blob db4b1133ef9ab138c85b896ddf475a2103fb276d: positive coefficients and closed-window support endpoint.
- WeilDefect/Arithmetic/ActualZetaIV152AMPhysicalEnvelope.lean: floor/translation envelope, original positive coefficient caps.
- WeilDefect/Arithmetic/ActualZetaIV154AMSupport.lean blob 9a6278d8a699963d7e80d792a9bbe0b6166bdded: physical measurable step weight.
- custody/iv146-am/am_cells.json blob ba15f7c820fe5fd0a1a3ffb61f80554ef0659cb0, SHA256 2b149c79f469b594ce7c308e44c278da00e9e41fbd9da1436cad0b0dca9d294a; read from current custody parent. Original analytic source facts are used exactly as stated; no change to sign, support or normalization.

## Analytical identity

Let f be complex Schwartz, zero outside [-2,2], hence also at endpoints by continuity. Let J=[-2,2), H(x)=h[floor(4096(x+2))] on J, zero elsewhere, with h the frozen positive integer vector. Put g=f/H on J, zero elsewhere. Let S be the 24 prime powers from the original dictionary, a_n=Lambda(n)/sqrt(n)>0, s_n=log(n)>0. All integrals are Lebesgue on R unless specified. Define C=7979648/1000000, V(x)=sum_n a_n(H(x+s_n)+H(x-s_n))/H(x) on J, zero outside. Define E_-(f)=sum_n a_n integral H(x)H(x+s_n)|g(x+s_n)-g(x)|^2 dx and E_+(f) similarly with plus. Both nonnegative; all integrands bounded and compactly supported because H and g bounded and supported in J (minimum h>0). No smoothness of H or g is needed.

For each s=s_n, expansion of the square gives two diagonal terms and the cross term. The first diagonal integral is integral_J H(x+s)/H(x)|f(x)|^2 dx; the second becomes integral_J H(x-s)/H(x)|f(x)|^2 dx by y=x+s. The cross term is -2 Re integral f(x) conj(f(x+s)) dx for E_-, and +2 Re for E_+. The equality H(x)g(x)=f(x) holds everywhere, including zero extension. Translation invariance gives integral f(x)conj(f(x-s)) dx = conjugate(integral f(x)conj(f(x+s)) dx). The original literal dictionary therefore identifies P_2(f,f) with the real sum of these two signed shifts; no Hermiticity or reality assumption on f. Summing gives

    P_2(f,f) = integral_J V(x)|f(x)|^2 dx - E_-(f)
    -P_2(f,f) = integral_J V(x)|f(x)|^2 dx - E_+(f).

Equivalently the actual signed Weil prime contribution -P_2 is E_-(f) - integral_J V|f|^2. This is an exact analytic ground-state transform, not a new assertion of arithmetic positivity.

## Exact row residual

Define R_i=sum over the 48 frozen signed (j,u) pairs of u*max(h[i+j],h[i+j+1]), with zero extension. For x in cell i the floor-add lemma puts each translated coordinate in one of those two cells. Original coefficient caps are u/W, W=10^9. Nonnegative H gives V(x)<=r_i=R_i/(W h_i). Define delta_i=C-r_i. The attached exact BigInt replay checked all 16384 cells using the remote frozen input, not an estimated or sampled real integral. The function replay was executed in the connector's JS runtime; the committed standalone Node entry uses that identical function with additional input SHA256 assertion; the standalone wrapper itself was not separately run. All row slacks positive. Minimum weight 39499328; maximum 100000000. Maximum r_i=31581430071841747/3957747500000000 at cell 6572 (first occurrence). Minimum delta_i=1851038253/3957747500000000, about 4.677e-7. This scalar extremum was already in IV237, not a new numerical discovery. The new contribution is preserving the energy and spatial residual.

    C||f||^2 - P_2(f,f) >= E_-(f) + integral_J delta_cell(x)|f(x)|^2 dx
    C||f||^2 + P_2(f,f) >= E_+(f) + integral_J delta_cell(x)|f(x)|^2 dx.

In particular the signed prime contribution is bounded below by -r_max||f||^2+E_-(f). Retaining the spatial envelope is stronger than discarding it, and the plus/minus pair also yields |P_2| <= r_max||f||^2-min(E_-,E_+). The residual bounds concern the conservative envelope, not exact V or its spectrum. The 16 band minima in the JSON can supply a coarser spatial lower envelope without a new bank.

## Structural interface and limits

If a separately established original-normalization non-prime form B(f) satisfies B(f)+E_-(f)>=integral_J r_cell(x)|f(x)|^2 dx, the total B(f)-P_2(f,f) is nonnegative on this supported domain. This is a sufficient receiver criterion, not a proof of B's estimate, parity-specific Gamma transport, pole restoration, or structural Weil. No claim that E_- has an L2 spectral gap: internal translation energy alone need not supply uniform coercivity. Next investigate a legitimate original AM energy comparison (e.g. frequency-sensitive lower bounds on the weighted differences with the support boundary treated exactly); deliver interface only, no reassignment or adoption of another lineage. No new kernel proof or CI dispatched for this analytic report and exact executable audit; record-only commit skip ci, using previously observed isolated custody convention.

Four axes: mathematical identity analytically derived; exact row arithmetic replay PASS; new native formalization not attempted; source, replay and result committed on custody branch; program-level adoption remains scoped/local, not global. Existing terminal raw remote-byte readback caveat unchanged.
