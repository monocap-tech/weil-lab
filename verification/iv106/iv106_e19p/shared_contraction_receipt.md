# IV106-E19P — shared 665-row integer contraction

Original C3 indicators, window [-11/10,11/10], width 11/3325.
All 665 targets; 665 interior step coefficients and 128 exterior step
coefficients per target, frozen at scale 10^12. Candidate generation uses
numerical Toeplitz/positive system solves; optimality is not assumed.

E19O's midpoint/sinc estimates are reused. At Q=16384, aliases m=-128..128,
s_m is the rational upper bound on sinc(u+m)^2 rounded upward at scale 2^20
(central alias 1; others u^2/(m+u)^2). Define three common weights:
A>=sum s_m*w_m, V>=sum s_m/w_m, C=sum s_m. The actual defect squared
is bounded pointwise by A|X|^2+V|Z|^2-2C Re(conj(Z)X).
A and V are rounded upward using interval logarithmic weights. This
quadratic remains nonnegative and represents a squared norm: use actual
alias amplitudes with s_m, plus the two nonnegative diagonal reserves.
Integer FFT of the three weights, normalized by Q and midpoint phase,
bounds real Toeplitz coefficients at scale 2^22 with error <=2 units.
Twiddle recurrence uses Machin pi, Taylor root enclosure, scale 2^60,
and e_next<=(2+R)e+20R+2/2^60; R=12Q/2^60. Final midpoint rotation adds
(1+R)e+20R+2/2^60. The real coefficient error includes output flooring.

Quantize candidate coefficients to scale P=2^18, with individual error
<1/P. For quantized x and q, l1 bounds <=1 and <=2 respectively.
Exact integer matrix products for the three Toeplitz contractions have
explicit int64 absolute-sum overflow checks. Add gram error times
(||x||_1+||q||_1)^2. The original frozen coefficients are restored via
triangle inequality: max A<20, max V<4, sqrt(h)<.06, so quantization
norm reserve <=.06*(5*26+2*29)/P. Discrete Parseval is exact since
index span <Q. Centering both coefficient sequences at target index
changes only a common phase of the defect and preserves its norm.
Use E19O's derivative estimate with the centered coefficient moment
norms, checked individually with rational square-root upper rounding.
Add derivative/(2Q) to midpoint norm. Tail uses exact jump sums as E19O.
All 665 rows passed independent rational coefficient/interval arithmetic.
The actual weighted logarithmic carrier admission and analytic
midpoint/jump/FFT derivations remain outside the strict native audit.

Max centered derivative=8360199/1250000=6.6881592.
Max tail=84213844211425151891573807/8652065625000000000000000000000 (row 28).
Max total squared upper=2501303731529070807584716102603981/72578786918400000000000000000000000000 (row 0).
Max rounded norm upper=1174109/200000000=.005870545. All below .005871.
These are individual row bounds, not a joint row-map norm bound or
terminal Schur certificate. E19O's smaller row-zero bound remains valid
conditional on the earlier analytic attachments.

Conversation artifact SHA256:
row_bank.npz e55b8992e769d09ee83fdd66a9d6a3cbaf592933f7d85d3ca0d8dd9a2e4d886e
row_bank_receipt.json e1f9bf1a11194227e726a9172705a637ff13ebb15afb11fedb5821c8853f8fd1
scale_rows.py e3a8a78081b66d32f8b7976059f8ddf4ae4e4ef25a8fd410f868e23509de1e40
certify_bank.py 814bb90590a546c67bce52659e612657a3e880754957c3aff2d8553391cc1f2a
bank_certificate.json 4c4940d86081e9a9d4e412fded7c57fcf5c85aa32824bbb933ab668835d683c4

The binaries and executable replays are delivered as conversation
artifacts; the repository note is a receipt, not an independent native
receipt. No proof of global Weil positivity is claimed.
