# V10B55 native failure — evidence record
Run 45978018403 job 140434561216 source 181d0143ef8f3bda157686e9e732d55e0dc99b41; overall failure. V10B52b blob bba4ccf056254048f46e3dcba44a1f44ce1caacc. All six prior polynomial evaluation elaboration mismatches absent; single new error in polynomial_integrable addition case. Integrable.add hp hq produces pointwise Pi addition, while goal is explicit lambda; elaborated continuous ENorm instance expressions also differ in printed diagnostic. No complete module audit, no admission, sorryAx in failed declarations. The monomial_integrable axiom print alone does not meet module admission. Exact diagnostic:
2026-11-27T10:01:55.3203106Z error: WeilDefect/MasterRecon/V10B52b.lean:33:4: Type mismatch: After simplification, term
2026-11-27T10:01:55.3203702Z   Integrable.add hp hq
2026-11-27T10:01:55.3203973Z  has type
2026-11-27T10:01:55.3204533Z   @Integrable ℂ PseudoMetricSpace.toUniformSpace.toTopologicalSpace
2026-11-27T10:01:55.3205397Z     NormedAddCommGroup.toENormedAddCommMonoid.toContinuousENorm ℝ Real.measurableSpace
2026-11-27T10:01:55.3206687Z     ((fun x => ↑(eval x p) * ↑↑((physicalInclusion t) g) x) + fun x => ↑(eval x q) * ↑↑((physicalInclusion t) g) x)
2026-11-27T10:01:55.3207464Z     (supportMeasure t)
2026-11-27T10:01:55.3207707Z but is expected to have type
2026-11-27T10:01:55.3208316Z   @Integrable ℂ PseudoMetricSpace.toUniformSpace.toTopologicalSpace SeminormedAddGroup.toContinuousENorm ℝ
2026-11-27T10:01:55.3208870Z     Real.measurableSpace
2026-11-27T10:01:55.3209365Z     (fun x => ↑(eval x p) * ↑↑((physicalInclusion t) g) x + ↑(eval x q) * ↑↑((physicalInclusion t) g) x)
2026-11-27T10:01:55.3209809Z     (supportMeasure t)
2026-11-27T10:01:55.3224905Z info: WeilDefect/MasterRecon/V10B52b.lean:79:0: 'WeilDefect.MasterRecon.V10B52b.monomial_integrable' depends on axioms: [propext, Classical.choice, Quot.sound]
Full decoded native transcript preserved with source hashes, manifest, toolchain and diagnostics. Original artifact 15187564785 (7767 bytes, SHA256 cb35f4c01a6c422b26be286816d3e9ab524d1cb5191cbb8f4947410a7a953f3b) remains expiring; no claim of raw ZIP custody. V10B54 accepted head unchanged. New diagnostic permits a bounded explicit pointwise equality repair, not repetition of prior casts. No V10B19 or W consumption; no positivity promotion.
