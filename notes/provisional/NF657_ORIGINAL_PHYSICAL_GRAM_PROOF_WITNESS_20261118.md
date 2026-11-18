# NF657 — actual physical Gram containment Lean PASS; compact rational positivity certificate

Status: **all 120 original 15-source physical H entry containments Lean PASS**. Quantified external finite-block positivity PASS. Final finite-block positive-definiteness theorem in Lean **OPEN**.

## 1. Recovered decisive compiler result

NF655 draft PR #680, repaired workflow run **44422031265**, job **135217176892**, completed SUCCESS on November 18, 2026. All stages passed: original archive pin/manifest and 73 accepted-input modules reused; the independent 106 original oscillator/pole-diagonal containments; the 14 cross entries after accepting the 14-row opposite-sign mixed moment theorem; all 120 original entry theorem axiom audits.

All printed named terminal proofs use only \`propext\`, \`Classical.choice\`, \`Quot.sound\`. Artifacts:
- \`nf655-local-gram-preflight\` ID **14480844197**, sha256 \`8724ba9cc99a3d7d5c2d872a2c04a15d1eb9783434b3f8f783cac5f6cbe242aa\`
- \`nf655-local-gram-kernel-logs\` ID **14482653638**, sha256 \`0dee7beaf397eb7c807d9ada5a5e1327ff0d2a2a352e1b3eca4311fc6a639941\`.

These are genuine original analytical \`neutralNF606PhysicalH\` containments, not only arithmetic data reconciliation or a constructed surrogate. NF655 fixes a \`Decidable\` elaboration problem by spelling out the rational widening gate. No main merge.

## 2. Two independent exact finite-block positivity witnesses

Original frozen NF631 widened entries artifact **14459025571**, ZIP sha256 \`e91a83cae117e98608aefa6849dac178e4ddb58dd1dffbfe37304ad248af9ed9\`, retained inner compressed bytes sha256 \`9e76e2dea4f46ed5fc3ff8875f804c186cd0cacb86c47295f0cd93d189b9f7e6\`. Historical original-entry hash \`43e81193739d18b699481384bf9c91f5d546a4398005f4c2925426985618bcde\`.

**Interval LDL witness.** Integer outward rounding at \(10^{160}\) produces 15 strictly positive pivot lower bounds; last \(4.942065270655478\times 10^{-46}\). Verified all 120 input enclosures, 15 pivot interval recursions, 105 lower factor interval recursions and 105 inverse-lower recursions by a *separate* exact-\(\mathbb Q\) validator. Exact integer inequality yields conservative \(10^{-60}\) coercivity. Generated local 177927-byte JSON witness SHA256 \`e3305c57c7688a1ec42159092ca67e1b385b0a196d95a15b5434068d40addcd6\`; available as session artifact, not yet committed to GitHub. The revised NF656 script can emit this witness with \`--witness\`.

**New, simpler fixed congruence witness.** Define the 15-by-15 **fixed rational**, unit lower-triangular \(K=k/10^{64}\). There is no square root or variable interval division in the proposed Lean gate. First enclose every original physical entry ball \(\langle m_{pq}/Q,r_{pq}/Q\rangle\) by symmetric rational \(\langle c_{pq}/S,e_{pq}/S\rangle\), where \(Q=10^{2600},S=10^{64}\), using 120 integer cross multiplication checks. Compute exact integer transformed centers and radius upper bounds:
\[
 C'_{ij}=\sum_{p,q}k_{ip}k_{jq}c_{pq},\qquad
 R'_{ij}=\sum_{p,q}|k_{ip}k_{jq}|e_{pq}.
\]
The transformed matrix \(K H_I K^\mathsf T\) has midpoint \(C'_{ij}/S^3\) and radius \(R'_{ij}/S^3\). Each of **15 exact integer** row margins
\[
 d_i=C'_{ii}-R'_{ii}-
       \sum_{j\neq i}(|C'_{ij}|+R'_{ij})
\]
is strictly positive. Put \(m=\min d_i\), \(N_K=\sum_{i,j}k_{ij}^2\). The final exact integer gate
\[
 \boxed{m\,10^{60}>S\,N_K}
\]
is strictly true. Then for every \(x\in\mathbb R^{15}\), if the physical matrix \(H_I\) is symmetric and inside the 120 original entry enclosures,
\[
  x^\mathsf T H_I x\ge 10^{-60}\|x\|_2^2.
\]
Proof: \(B=K H_I K^\mathsf T\). Strict diagonal dominance with positive diagonal gives \(y^\mathsf T B y\ge(m/S^3)\|y\|^2\) by \(2|ab|\le a^2+b^2\). Because \(K\) is unit lower triangular, it is invertible. Setting \(x=K^\mathsf T y\) and using \(\|K\|_F^2=N_K/S^2\) proves the bound.

Independent executed checks: all 120 original source interval inclusions, 225 exact transformed signed center/radius computations, all 15 margins, and final coercivity inequality. Zeroing an original radius or a margin was rejected. Quantizing both K and the H entry intervals at **64 digits** preserved a lower margin \(\approx4.94206527\times10^{-46}\) and external ratio \(\approx2.61550789801547\times10^{-59}\). The compact 34062-byte session witness has SHA256 \`f884548b04664516a9b508a1ca8ac41cc52ccf0295a959198bf528e561d1c39b\`.

## 3. Committed custody and remaining formal tasks

Committed to \`research/nf657-original-gram-proof-witness\`:
- Revised \`scripts/verify_nf656_original_physical_gram_interval_ldl.py\` emits complete outward-interval witness as an optional output.
- \`scripts/verify_nf657_original_gram_ldl_witness.py\` independently checks interval recursions and exact coercivity using rational fractions.
- \`scripts/emit_nf657_compact_congruence.py\` generates the shorter fixed rational witness from immutable NF631 source, using the original interval LDL only as an **untrusted preconditioner search**.
- \`scripts/verify_nf657_compact_congruence.py\` independently checks the **entire** shorter witness using direct signed integer four-index sums.
- \`WeilDefect/Arithmetic/ActualZetaOriginalPhysicalGramBlockSymmetry.lean\`: separate analytic physical H symmetry proof candidate, from the authentic NF607 pair dictionary; **Lean pending**.
- Manual-only \`nf657-original-gram-congruence.yml\` workflow: original NF631 pinned archive, independent validator, corruption tests, focused symmetry Lean build/axiom audit, artifact upload. **Not triggered** (no extra automatic CI fan-out).

To reproduce after acquiring original \`nf631-widened.zip\`:
\`\`\`sh
python scripts/emit_nf657_compact_congruence.py nf631-widened.zip nf657-compact.json
python scripts/verify_nf657_compact_congruence.py nf657-compact.json nf631-widened.zip
\`\`\`
A formal Lean theorem remains to be written/accepted for generic diagonal-dominance coercivity and this particular fixed rational certificate. The numerical inequalities are exact and independently checked, but that is not the same as Lean acceptance of the final block-positive theorem. The complete 242-dimensional physical system, original numerical solve custody, full signed Weil positivity and RH all remain open. Do not merge main or promote finite principal-block positivity to global statements.
