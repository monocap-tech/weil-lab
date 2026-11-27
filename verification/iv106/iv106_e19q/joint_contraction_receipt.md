# IV106-E19Q joint cell-row error reserve

Authenticated E19P coefficient bank e55b8992e769d09ee83fdd66a9d6a3cbaf592933f7d85d3ca0d8dd9a2e4d886e.
All 665 row coordinates simultaneously, arbitrary complex coefficients.
Use h=11/3325, Q=16384, aliases -128..128, cutoff T=(257/2)/h.
For each bin take a whole-bin upper sinc^2 bound (central 1; otherwise
max |u|^2/min |m+u|^2), and interval log bounds. A,V,C constant on each
bin majorize the actual squared defect by A|X|²+V|Z|²-2C Re(conj(Z)X).
The majorant is PSD because it is a sum of weighted squared amplitudes
plus diagonal reserves. Integrate each trigonometric product exactly:
its DFT coefficient is multiplied by sinc(lag/Q), enclosed with rational
Taylor series and Machin pi. No joint derivative remainder needed.

Integer FFT scale 2^60, output Gram scale 2^30, entry error <=61 units
for each of the three weight matrices. Quantize frozen coefficients at
2^20, round intermediate Toeplitz products down by 2^14, and bound the
error by column absolute sums; exact int64 overflow checks. Symmetrize
the final matrix (store twice the symmetric part), use Gershgorin with
Python integer row sums. Bound coefficient restoration by exact Schur
norm inequalities, sqrt(h)<.06, max A<20, max V<4.

Tail: let JX and JQ be jump matrices including both endpoint jumps.
Periodic jump-polynomial Parseval and the Schur squared norms
ax=24628303069642413785469/100000000000000000000000,
aq=11784226917242618515783/2500000000000000000000
give joint tail <= 2*h/36 * [2*(11/L²+12/L)*ax+
2*(1/L²+1/L)/9*aq], L=257/2. Uses 9<w(T)<11 and monotone weighted
inverse-square integrands, sum bounded by first term plus integral.
This avoids multiplying individual tails by 665.

Gershgorin upper: 87985828070812221/479183000352220774400
Gram interval error: 275093309444679/368934881474191032320
Intermediate rounding: 25215113/180143985094819840
Quantization norm: 5906907/50000000000
Finite-band upper: 468960636836298049/2500000000000000000000
Tail: 636856137398970942186259669/63530881875000000000000000000000
Total: 12554249266547620967511044419/63530881875000000000000000000000 < 1/5000.
Norm upper: 14057333/1000000000. Trace of individual reserves ~0.02252374824,
114-fold larger squared reserve. This is conditional on the analytic
Fourier/step and integer FFT derivations and native carrier attachment.
No terminal positivity comparison or RH inference.

Local executed replay joint.py SHA256 a17002d1987640b3f0efab0c5591ece79c2b15efc9a21c6600ea051ea3e566f1
joint_certificate.json d61da378760ca11e21c7e828b46a717d810116d35dfc03d5ec325f1f6ddbb8c9
joint_matrix.npz 24e37cd533c5efbc554c926695fc89f64d39d60aee90cb6643c5aa3a69da23e7
ZIP replay bundle 8fdfe3275b99f0bd058a99abdfd00e9615a8dc976ca3b7a02763fcf53ee6b49d
The replay bundle is provided as a conversation artifact; this repository
receipt does not claim a repository-native audit of the binaries.
