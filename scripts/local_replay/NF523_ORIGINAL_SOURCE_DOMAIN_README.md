# NF523 local exact original-source graph-domain proof package

## Locally executed exact rational verification

```bash
python verify_nf523_original_endpoint_log_fractional_domain_exact.py \
  --nf494 NF494_original_H400_U400_source.json \
  --output nf523_primary_source_exact.json
python verify_nf523_independent_endpoint_and_moment_correction.py \
  --nf494 NF494_original_H400_U400_source.json \
  --primary nf523_primary_source_exact.json \
  --output nf523_independent_source_exact.json
```

Both ran locally and PASSED, with full immutable original NF494 SHA. The independent checker uses reverse Horner and automatic derivative rather than the primary forward absolute-sum calculation; its six-dimensional rational polynomial correction is a **control**, not a claim to have inverted the actual 242-dimensional weighted smoothing Gram.

The accompanying note supplies the complete original-source fractional-Sobolev theorem, construction of source moment-preserving smooth test approximants, and an exact finite-observation/non-domain countermodel. These mathematical arguments are not claimed to have been Lean-compiled. The actual full two-source zero graph norm/image and the signed original Weil form remain OPEN. No RH theorem.

NF522's three named original finite-selected physical NF404 sufficiency NO-GO results are retained unchanged and not transported across the source-domain boundary.