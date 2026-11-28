# NF618 Batch25 Boolean specialization repair

Predecessor: run 46096420464, production commit 93b4c78ee91fd6824156b95cba4214e2ef5d1fac, durable failure receipt 08afb4ea93508ec8cd7ea9e29900e51219bfb37a. All 14 power blocks built through exponent 159; 13 positive phase modules built, 13 negative phase modules failed at line 15, 89 reachable slot modules failed at line 38. No other Lean error classes in the retrieved log. The final audit did not run. No admission.

Root defect: generated proof used `if_true/if_false` (True/False propositions), not the actual Bool coercion proposition `b = true`. Specialize the high-phase theorem with explicit `if_pos (rfl : (true : Bool) = true)` or `if_neg (by decide : (false : Bool) ≠ true)`. Use a definitional `change` to the concrete frequency in the slot cache premise before applying phase identity. No numerical data, precision, theorem statement, slot count or axiom policy changed.

Bounded repair only; native result and independent admission outstanding. Do not repeat unchanged failure. The historical candidate's source fingerprint is not the new source fingerprint. Dependency reassembly and exact bank binding are reused from the successful G3 replay. No universal dispatch.

Governance observation: the initial four-row pilot covered a positive representative only, so it did not exercise the negative Boolean branch or this generated cache premise. Future production templates should include both signed branches and an actual bank-read attachment in the bounded preflight. The previous source and failure archive remain intact.
