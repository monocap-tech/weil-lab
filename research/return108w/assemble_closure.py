#!/usr/bin/env python3
"""Build the minimal literal bridge overlay, with fail-closed source custody."""
import hashlib, json, pathlib, re, subprocess
I = "f2e8ec89ae4bf8687a652b299b730d6d1baa43f7"
R = "d3067677cad7a0a583ef14b5466018dfad5f0afe"
ROOT = "WeilDefect/MasterReturn/LogCarrierBridge.lean"
def git(*args):
    return subprocess.check_output(["git", *args])
def inventory(ref):
    result = {}
    for row in git("ls-tree", "-r", "-z", ref).split(b"\0"):
        if not row: continue
        meta, path = row.split(b"\t", 1)
        mode, kind, sha = meta.decode().split()
        if kind == "blob": result[path.decode()] = (mode, sha)
    return result
def digest(data):
    return hashlib.sha1(b"blob " + str(len(data)).encode() + b"\0" + data).hexdigest()
trees = {"IV": inventory(I), "RECON": inventory(R)}
refs = {"IV": I, "RECON": R}
for p in ("lean-toolchain", "lakefile.toml"):
    assert trees["IV"][p] == trees["RECON"][p], p
    assert digest(pathlib.Path(p).read_bytes()) == trees["IV"][p][1], p
seen, manifest, external = set(), {}, set()
IV_ENTRY = "WeilDefect/Morphology/NeutralLogHilbertCarrier.lean"
assert git("rev-parse", "HEAD").decode().strip() == I
def visit(p, preferred):
    if (p, preferred) in seen: return
    seen.add((p, preferred))
    side = preferred
    if p not in trees[side]:
        raise SystemExit("MISSING PROJECT SOURCE IN " + side + ": " + p)
    # Only compare versions actually required by the selected import graph.
    a, b = trees["IV"].get(p), trees["RECON"].get(p)
    if p in manifest and manifest[p]["blob"] != trees[side][p][1]:
        raise SystemExit("DUAL-LINEAGE SOURCE CONFLICT: " + p + " " + str((a,b)))
    if side == "RECON" and a and a != b:
        raise SystemExit("RECON SOURCE WOULD OVERWRITE IV BASE: " + p)
    mode, sha = trees[side][p]
    assert mode == "100644", (p, mode)
    data = git("show", refs[side] + ":" + p)
    assert digest(data) == sha, p
    entry = manifest.setdefault(p, {"blob":sha,"origin":"IV" if a else "RECON","imports":[],"required_by":[]})
    if side not in entry["required_by"]: entry["required_by"].append(side)
    # Remove nested Lean block comments, preserving line boundaries.
    source = data.decode()
    clean = []
    depth = 0
    pos = 0
    while pos < len(source):
        if source.startswith("/-", pos):
            depth += 1; pos += 2
        elif depth and source.startswith("-/", pos):
            depth -= 1; pos += 2
        elif not depth and source.startswith("--", pos):
            end = source.find("\n", pos)
            pos = len(source) if end < 0 else end
        else:
            if not depth or source[pos] == "\n": clean.append(source[pos])
            pos += 1
    assert depth == 0, p
    for line in "".join(clean).splitlines():
        m = re.match(r"^\s*(?:(?:public|private|meta)\s+)*import\s+(.+?)\s*$", line)
        if not m: continue
        for module in m.group(1).split():
            if not re.fullmatch(r"[A-Za-z_][A-Za-z0-9_'.]*", module):
                raise SystemExit("UNPARSED IMPORT: " + p + ": " + line)
            target = module.replace(".", "/") + ".lean"
            if target in trees["IV"] or target in trees["RECON"] or module == "WeilDefect" or module.startswith("WeilDefect."):
                if target not in entry["imports"]: entry["imports"].append(target)
                visit(target, "IV" if p == ROOT and target == IV_ENTRY else side)
            else: external.add(module)
visit(ROOT, "RECON")
# No source files are written until the entire selected closure passes.
for p, e in sorted(manifest.items()):
    dst = pathlib.Path(p)
    if e["origin"] == "IV":
        assert digest(dst.read_bytes()) == e["blob"], p
    else:
        assert not dst.exists(), p
        data = git("show", R + ":" + p)
        assert digest(data) == e["blob"], p
        dst.parent.mkdir(parents=True, exist_ok=True)
        dst.write_bytes(data)
    assert digest(dst.read_bytes()) == e["blob"], p
assert manifest[IV_ENTRY]["required_by"] == ["IV"]
assert manifest[ROOT]["blob"] == "2d45c6dac5353906a0daf2b9d500541be3be3e46"
neutral = "WeilDefect/Morphology/Neutral.lean"
assert manifest[neutral]["blob"] == "9c446407e5f9ecfada57d2dee5e1d85b7d8a5753"
assert manifest[neutral]["required_by"] == ["IV"]
result = {"IV":I,"RECON":R,"root":ROOT,"entries":manifest,"external_imports":sorted(external),"explicit_cross_edge":[ROOT,IV_ENTRY]}
pathlib.Path("return108w-closure.json").write_text(json.dumps(result, indent=2, sort_keys=True)+"\n")
print("Authenticated closure:", len(manifest), "modules;", sum(e["origin"]=="RECON" for e in manifest.values()), "overlay modules")
print("No differing shared path required by both lineages; IV morphology retained.")


# RETURN108-X candidate: retain original W closure and append exact source.
# Authority: W02 continuation amendment d4e482f2f616112dca11f6d8fd803a3dffb5a80c.
# W was authenticated in canonical-return@55b2334d0a79fa9b3ab3b30d3f81a14802b1b89e.
X = "import WeilDefect.MasterReturn.LogCarrierBridge\n\n/-! RETURN108-X: quantitative continuous equivalence on the actual W carriers.\nGenerated deterministically by the W/X pinned closure assembler.\nNo signed-form, sampling, or support-natural assertion is included. -/\nnamespace WeilDefect.MasterReturn.LogCarrierContinuous\nopen MeasureTheory\nopen scoped FourierTransform\nopen WeilDefect.MasterRecon\nopen LogWeightComparison LogCarrierBridge\n\nnoncomputable def boundRI : ℝ := 1 + |cRI|\nnoncomputable def boundIR : ℝ := 1 + |cIR| / Real.log 2\n\ntheorem boundRI_nonneg : 0 ≤ boundRI := by\n  unfold boundRI\n  positivity\n\ntheorem boundIR_nonneg : 0 ≤ boundIR := by\n  unfold boundIR\n  have hlog : 0 < Real.log 2 := Real.log_pos (by norm_num)\n  positivity\n\ntheorem carrierEquiv_norm_sq_le (a : ℝ) (g : NeutralLogHilbertCarrier a) :\n    ‖carrierEquiv a g‖ ^ 2 ≤ boundRI * ‖g‖ ^ 2 := by\n  have hi := neutralLogPhysical_energy g.val\n  have hr := iv_energy_to_recon _ hi\n  rw [V08I.logCarrier_energy, carrierEquiv_physical, neutralLogHilbertCarrier_norm_sq]\n  calc\n    _ ≤ ∫ x, boundRI * (logarithmicFourierWeight x *\n      ‖(𝓕 (neutralLogPhysical g.val) : RealComplexL2) x‖ ^ 2) := by\n        apply integral_mono hr (hi.const_mul boundRI)\n        intro x\n        change V08I.logWeight x * (‖(𝓕 (neutralLogPhysical g.val) : RealComplexL2) x‖ ^ 2) ≤\n          boundRI * (logarithmicFourierWeight x * (‖(𝓕 (neutralLogPhysical g.val) : RealComplexL2) x‖ ^ 2))\n        rw [← mul_assoc]\n        exact mul_le_mul_of_nonneg_right (recon_le_scaled_iv x) (sq_nonneg _)\n    _ = _ := by rw [integral_const_mul]\n\ntheorem carrierEquiv_symm_norm_sq_le (a : ℝ) (g : V08I.logCarrier a) :\n    ‖(carrierEquiv a).symm g‖ ^ 2 ≤ boundIR * ‖g‖ ^ 2 := by\n  have hp : neutralLogPhysical ((carrierEquiv a).symm g).val =\n      V08I.physicalInclusion a g := toIV_physical a g\n  have hr := V08I.logCarrier_energy_integrable a g\n  have hi := recon_energy_to_iv _ hr\n  rw [neutralLogHilbertCarrier_norm_sq, hp, V08I.logCarrier_energy]\n  calc\n    _ ≤ ∫ x, boundIR * (V08I.logWeight x *\n      ‖(𝓕 (V08I.physicalInclusion a g) : V08I.FullL2) x‖ ^ 2) := by\n        apply integral_mono hi (hr.const_mul boundIR)\n        intro x\n        change logarithmicFourierWeight x * (‖(𝓕 (V08I.physicalInclusion a g) : V08I.FullL2) x‖ ^ 2) ≤\n          boundIR * (V08I.logWeight x * (‖(𝓕 (V08I.physicalInclusion a g) : V08I.FullL2) x‖ ^ 2))\n        rw [← mul_assoc]\n        exact mul_le_mul_of_nonneg_right (iv_le_scaled_recon x) (sq_nonneg _)\n    _ = _ := by rw [integral_const_mul]\n\nprivate theorem nonneg_le_of_pow_two_le {x y : ℝ} (hx : 0 ≤ x) (hy : 0 ≤ y)\n    (h : x ^ 2 ≤ y ^ 2) : x ≤ y := by\n  by_contra! hn\n  have hpos : 0 < (x-y)*(x+y) :=\n    mul_pos (sub_pos.mpr hn) (add_pos_of_pos_of_nonneg (lt_of_le_of_lt hy hn) hy)\n  nlinarith only [hpos, h]\n\ntheorem carrierEquiv_norm_le (a : ℝ) (g : NeutralLogHilbertCarrier a) :\n    ‖carrierEquiv a g‖ ≤ Real.sqrt boundRI * ‖g‖ := by\n  apply nonneg_le_of_pow_two_le (norm_nonneg _) (mul_nonneg (Real.sqrt_nonneg _) (norm_nonneg _))\n  rw [mul_pow, Real.sq_sqrt boundRI_nonneg]\n  exact carrierEquiv_norm_sq_le a g\n\ntheorem carrierEquiv_symm_norm_le (a : ℝ) (g : V08I.logCarrier a) :\n    ‖(carrierEquiv a).symm g‖ ≤ Real.sqrt boundIR * ‖g‖ := by\n  apply nonneg_le_of_pow_two_le (norm_nonneg _) (mul_nonneg (Real.sqrt_nonneg _) (norm_nonneg _))\n  rw [mul_pow, Real.sq_sqrt boundIR_nonneg]\n  exact carrierEquiv_symm_norm_sq_le a g\n\nnoncomputable def carrierContinuousEquiv (a : ℝ) :\n    NeutralLogHilbertCarrier a ≃L[ℂ] V08I.logCarrier a where\n  toLinearEquiv := carrierEquiv a\n  continuous_toFun :=\n    ((carrierEquiv a).toLinearMap.mkContinuous (Real.sqrt boundRI)\n      (carrierEquiv_norm_le a)).continuous\n  continuous_invFun :=\n    ((carrierEquiv a).symm.toLinearMap.mkContinuous (Real.sqrt boundIR)\n      (carrierEquiv_symm_norm_le a)).continuous\n\ntheorem carrierContinuousEquiv_physical (a : ℝ) (g : NeutralLogHilbertCarrier a) :\n    V08I.physicalInclusion a (carrierContinuousEquiv a g) = neutralLogPhysical g.val :=\n  carrierEquiv_physical a g\n\nend WeilDefect.MasterReturn.LogCarrierContinuous\n\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.boundRI_nonneg\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.boundIR_nonneg\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierEquiv_norm_sq_le\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierEquiv_symm_norm_sq_le\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierEquiv_norm_le\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierEquiv_symm_norm_le\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierContinuousEquiv\n#print axioms WeilDefect.MasterReturn.LogCarrierContinuous.carrierContinuousEquiv_physical\n"
x_path = pathlib.Path('WeilDefect/MasterReturn/LogCarrierContinuous.lean')
assert not x_path.exists(), x_path
x_path.write_bytes(X.encode('utf-8'))
print('RETURN108-X source SHA256:', hashlib.sha256(x_path.read_bytes()).hexdigest())

# RETURN108-Y: same authenticated W/X1 sources plus literal aperture inclusions.
Y = "import WeilDefect.MasterReturn.LogCarrierContinuous\n\n/-! RETURN108-Y: actual isometric aperture inclusions and naturality of the\ncontinuous carrier equivalence. No assertion about translation or signed forms. -/\nnamespace WeilDefect.MasterReturn.LogCarrierNatural\nopen MeasureTheory Set\nopen WeilDefect.MasterRecon\nopen LogCarrierContinuous\n\ntheorem iv_mem_of_le (a b : ℝ) (hab : a ≤ b) (g : NeutralLogHilbertCarrier a) :\n    g.val ∈ NeutralLogHilbertCarrier b := by\n  change neutralOutsideRestriction b (neutralLogPhysical g.val) = 0\n  apply (neutralOutsideRestriction_zero_iff b _).mpr\n  have hsub : Set.Icc (-a) a ⊆ Set.Icc (-b) b :=\n    Set.Icc_subset_Icc (neg_le_neg hab) hab\n  filter_upwards [neutralLogHilbertCarrier_supported g] with x hx\n  intro hout\n  exact hx (fun hin => hout (hsub hin))\n\ntheorem recon_mem_of_le (a b : ℝ) (hab : a ≤ b) (g : V08I.logCarrier a) :\n    g.val ∈ V08I.logCarrier b := by\n  change V08I.supportConstraint b (g : V08I.FullL2) = 0\n  apply Lp.ext\n  have hm := V08I.multiplier_ae (V08I.outsideMask b) (V08I.outsideMask_measurable b) 1\n    (V08I.outsideMask_bound b) (V08I.physicalMap (g : V08I.FullL2))\n  change (V08I.supportConstraint b (g : V08I.FullL2) : ℝ → ℂ) =ᵐ[volume]\n    fun x => V08I.outsideMask b x * V08I.physicalMap (g : V08I.FullL2) x at hm\n  have hsub : Set.Icc (-a) a ⊆ Set.Icc (-b) b :=\n    Set.Icc_subset_Icc (neg_le_neg hab) hab\n  filter_upwards [hm, V08I.physicalInclusion_support a g,\n    Lp.coeFn_zero ℂ 2 (volume : Measure ℝ)] with x hx hs h0\n  change V08I.supportConstraint b (g : V08I.FullL2) x = (0 : V08I.FullL2) x\n  change (0 : V08I.FullL2) x = 0 at h0\n  rw [hx, h0, V08I.outsideMask]\n  by_cases h : x ∈ Set.Icc (-b) b\n  · have hn : x ∉ (Set.Icc (-b) b)ᶜ := by simpa using h\n    rw [Set.indicator_of_notMem hn, zero_mul]\n  · have hz : V08I.physicalMap (g : V08I.FullL2) x = 0 :=\n      hs (fun hin => h (hsub hin))\n    rw [Set.indicator_of_mem (show x ∈ (Set.Icc (-b) b)ᶜ from h), hz, mul_zero]\n\nnoncomputable def ivInclLinear (a b : ℝ) (hab : a ≤ b) :\n    NeutralLogHilbertCarrier a →ₗ[ℂ] NeutralLogHilbertCarrier b where\n  toFun g := ⟨g.val, iv_mem_of_le a b hab g⟩\n  map_add' _ _ := Subtype.ext rfl\n  map_smul' _ _ := Subtype.ext rfl\n\nnoncomputable def reconInclLinear (a b : ℝ) (hab : a ≤ b) :\n    V08I.logCarrier a →ₗ[ℂ] V08I.logCarrier b where\n  toFun g := ⟨g.val, recon_mem_of_le a b hab g⟩\n  map_add' _ _ := Subtype.ext rfl\n  map_smul' _ _ := Subtype.ext rfl\n\nnoncomputable def ivIncl (a b : ℝ) (hab : a ≤ b) :\n    NeutralLogHilbertCarrier a →L[ℂ] NeutralLogHilbertCarrier b :=\n  (ivInclLinear a b hab).mkContinuous 1 (by\n    intro g\n    change ‖g‖ ≤ 1 * ‖g‖\n    simp)\n\nnoncomputable def reconIncl (a b : ℝ) (hab : a ≤ b) :\n    V08I.logCarrier a →L[ℂ] V08I.logCarrier b :=\n  (reconInclLinear a b hab).mkContinuous 1 (by\n    intro g\n    change ‖g‖ ≤ 1 * ‖g‖\n    simp)\n\ntheorem ivIncl_norm (a b : ℝ) (hab : a ≤ b) (g : NeutralLogHilbertCarrier a) :\n    ‖ivIncl a b hab g‖ = ‖g‖ := rfl\n\ntheorem reconIncl_norm (a b : ℝ) (hab : a ≤ b) (g : V08I.logCarrier a) :\n    ‖reconIncl a b hab g‖ = ‖g‖ := rfl\n\ntheorem ivIncl_physical (a b : ℝ) (hab : a ≤ b) (g : NeutralLogHilbertCarrier a) :\n    neutralLogPhysical (ivIncl a b hab g).val = neutralLogPhysical g.val := rfl\n\ntheorem reconIncl_physical (a b : ℝ) (hab : a ≤ b) (g : V08I.logCarrier a) :\n    V08I.physicalInclusion b (reconIncl a b hab g) =\n      V08I.physicalInclusion a g := rfl\n\ntheorem carrier_natural (a b : ℝ) (hab : a ≤ b) (g : NeutralLogHilbertCarrier a) :\n    carrierContinuousEquiv b (ivIncl a b hab g) =\n      reconIncl a b hab (carrierContinuousEquiv a g) := by\n  apply V08J.physicalInclusion_injective b\n  rw [carrierContinuousEquiv_physical, ivIncl_physical, reconIncl_physical,\n    carrierContinuousEquiv_physical]\n\ntheorem ivIncl_comp (a b c : ℝ) (hab : a ≤ b) (hbc : b ≤ c)\n    (g : NeutralLogHilbertCarrier a) :\n    ivIncl b c hbc (ivIncl a b hab g) = ivIncl a c (hab.trans hbc) g :=\n  Subtype.ext rfl\n\ntheorem reconIncl_comp (a b c : ℝ) (hab : a ≤ b) (hbc : b ≤ c)\n    (g : V08I.logCarrier a) :\n    reconIncl b c hbc (reconIncl a b hab g) = reconIncl a c (hab.trans hbc) g :=\n  Subtype.ext rfl\n\nend WeilDefect.MasterReturn.LogCarrierNatural\n\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.iv_mem_of_le\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.recon_mem_of_le\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.ivIncl\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.reconIncl\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.ivIncl_norm\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.reconIncl_norm\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.ivIncl_physical\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.reconIncl_physical\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.carrier_natural\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.ivIncl_comp\n#print axioms WeilDefect.MasterReturn.LogCarrierNatural.reconIncl_comp\n"
y_path = pathlib.Path('WeilDefect/MasterReturn/LogCarrierNatural.lean')
assert not y_path.exists(), y_path
y_path.write_bytes(Y.encode('utf-8'))
print('RETURN108-Y source SHA256:', hashlib.sha256(y_path.read_bytes()).hexdigest())
