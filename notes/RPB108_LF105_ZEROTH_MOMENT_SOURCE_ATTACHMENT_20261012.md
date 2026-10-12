# LF105 — zeroth moment source attachment

Recovers the concrete RC36 consumer data: eight physical Legendre moment targets, sixteen polynomial trial modes, B=11/10. The committed RC35 metric certificate has a 16-by-8 exact rational coefficient matrix. RC36's explicit `native_head_certified` and `aperture_extended` flags are false; no native feature certificate is inferred from this physical-moment approximation certificate.

Adds `neutralActualZetaLogRiesz_zerothMoment_error_of_cap_derivative`. The zeroth physical moment uses the existing actual column `neutralMomentColumnL2 a 0` and canonical adjoint source `neutralLogMomentSource a 0`. Their existing moment pairing theorems supply the whole-carrier source identity. LF104 supplies the trial domain and metric action identity. No independent whole-source hypothesis remains for this target. The physical trial/carrier identification remains explicit; RC35's specific polynomial trial has not yet been instantiated. At a=B=11/10 the target is the constant Legendre P0 cap column.

Next: import the actual rational polynomial trial and its carrier representative, prove physical identification, and extend moment-column attachment to the remaining seven targets. Then import checked residual/matrix data. This theorem alone supplies no numerical bound.

Validation: local structural and unfinished-declaration scans pass; Lean is unavailable locally. LF104 run 38215799148 had no job assigned; LF102 run 38212753549 passed targeted checks and was running the root build. LF101 (9db5a15e68056df9894ee08856b75d09fd9db8d7, run 38212344780) remains the latest full-root validated checkpoint. LF105 requires cumulative CI. No aperture positivity, F4 closure or RH is claimed.
