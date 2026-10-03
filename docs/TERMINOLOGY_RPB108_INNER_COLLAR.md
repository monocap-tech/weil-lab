# RPB-108: inner collar with a fixed prime cutoff

- **Physical support radius c:** the carrier is supported in [-c,c].
- **Cancellation radius a:** the open interval (-a,a) on which actual frozen source cancellation is required.
- **Auxiliary radius b:** any c < b < a used only to obtain a support gap for the archimedean kernel.
- **Fixed-cutoff collar function g_b:** the archimedean gap function at gap b-c, minus the full physical prime sum with cutoff a, plus the actual source pole.
- **Actual central cancellation:** vanishing of frozenWeilCompactAction on every compact Schwartz test supported in (-a,a). Endpoint nullity or a named scalar identity is not this witness.
- **Analytic reduction:** a written mathematical argument using certified identities. It is distinct from a new Lean theorem or an instantiated WD-T38 witness.

The prime cutoff stays a throughout the target action. Changing the auxiliary gap does not authorize changing that action. Spectral L2 membership is not a premise of this reduction.
