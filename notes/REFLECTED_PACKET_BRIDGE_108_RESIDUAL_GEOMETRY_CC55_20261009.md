# RPB108 CC55 — Actual second-residual norm, phase angle and active-plane frame

Date 2026-10-09 UTC / 2026-10-08 Pacific. Recover Coupled CC54 `ec1d0caf1be0d817ba27d418bf1fedeb769f99d3` and read-only NF19 source head `38bf4791bd2a4ec4ecdc114e297c281d1b15c44c`. [Definitions](../docs/TERMINOLOGY_RPB108_RESIDUAL_GEOMETRY_CC55.md) precede load-bearing use. Historical wording, independent source branch and paused fronts preserved.

**New actual arithmetic target and result:** certify the TRUE second-mode residual norm rather than subtracting collective maxima. Original signed data give

\[
0.136<R_{\delta,e}<0.137,\qquad
0.112<R_{\delta,o}<0.113.
\tag{CC55.1}
\]

Together with authenticated CC53/NF19 bounds, the measured source-active plane has a positive A-relative LOWER frame eigenvalue between0.036 and0.039 even / between0.041 and0.044 odd. The measured two-column map nevertheless has a54-dimensional kernel per parity. This is a positive frame on a precisely specified actual source plane, not a frame on the full critical space.

## 1. NF19 recovery and exact replay

The immutable [NF19 report](https://github.com/monocap-tech/weil-lab/blob/38bf4791bd2a4ec4ecdc114e297c281d1b15c44c/notes/REFLECTED_PACKET_BRIDGE_108_SECOND_EXTERIOR_COLLECTIVE_NF19_20261009.md) certifies R2,e in(0.302,0.303) and R2,o in(0.275,0.276), with complete first-two corrected signs. It gives only residual norm lower bounds0.098/0.069 from R2-R1, and explicitly distinguishes them from the actual residual norm.

The NF19 raw archive was not available among the shared source files when checked. CC55 replays the published deterministic producer on the authenticated original E112 archive, reconstructing the SAME116 entries and checking uncompressed SHA256 `0a8f4ebd0778fa5c90209b3021d22791bdb0d9b73e0f19df608e04ed9ba2bcad`. This is a reproduction of NF19, not a new degree-expansion front. The existing first-boundary SHA is `da5fe692dc0d3a0820ccaf68217628776f08718661696dddad54012f4f3841ee`; E112 SHA is `f69019a895cd675e304989cbb8209c90f033264e0aef589d4b1aa3be09cf4c81`.

The published NF19 exact collective validator is replayed separately. Its four paid58-dimensional determinant tests are dependencies, not CC55's new tests. All original archimedean terms, six prime powers in both orientations, and both signed poles remain.

## 2. Actual residual and paid determinant criterion

Write d1=Q(phi1,phi1), c=Q(phi1,phi2), d2=Q(phi2,phi2). C-orthogonal elimination gives

\[
\psi=\phi_2-\frac{c}{d_1}\phi_1,
\quad d_\delta=d_2-\frac{c^2}{d_1}>3,
\quad b_\delta=b_2-\frac{c}{d_1}b_1.
\]
\[
G_2=G_1+T_2,\qquad
T_2(x)=\frac{|b_\delta(x)|^2}{d_\delta},\qquad
R_\delta=\frac{b_\delta^*A^{-1}b_\delta}{d_\delta}.
\tag{CC55.2}
\]

The [new exact certifier](../scripts/certify_native_residual_geometry_cc55.py) transforms original rational intervals outward, including c/d1 and its effect on every source coordinate and the high diagonal. It then rounds to grid10^-100 and pays the resulting full57-dimensional operator error. Bareiss integer elimination certifies center M(lower)+error I indefinite (56 positive leading minors, final negative) and center M(upper)-error I positive (all57 positive), where

\[
M(r)=\begin{pmatrix}rA&b_\delta\\b_\delta^*&d_\delta\end{pmatrix}.
\]

Four new exact paid tests prove (CC55.1). No numerical inverse or eigenvalue enters the proof. The result replaces NF19's coarse residual lower bound by a two-sided actual norm certificate.

## 3. Actual phase alignment in the low-energy metric

Let u1=A^{-1}b1/sqrt(d1), u_delta=A^{-1}b_delta/sqrt(d_delta), and sigma the squared cosine of their A-energy angle. The two positive rank-one response operators have traces R1 and R_delta. Their sum has largest eigenvalue R2, so its other nonzero eigenvalue is

\[
\lambda_-=R_1+R_\delta-R_2.
\tag{CC55.3}
\]

Their two-dimensional characteristic polynomial also gives

\[
\sigma=\frac{(R_2-R_1)(R_2-R_\delta)}{R_1R_\delta}.
\tag{CC55.4}
\]

Exact interval substitution of the authenticated strict brackets yields the following simplified outer bounds:

| Actual measured geometry | Even | Odd |
| --- | ---: | ---: |
| Squared A-energy cosine sigma | between0.57 and0.61 | between0.48 and0.51 |
| Lower nonzero frame eigenvalue lambda_minus | between0.036 and0.039 | between0.041 and0.044 |
| Residual norm on ker b1 | between0.053 and0.059 | between0.055 and0.059 |
| Source-active plane dimension | 2 | 2 |
| Full retained two-column kernel dimension | 54 | 54 |

The certificate records sharper rational angle and kernel-norm endpoints. Since0<sigma<1, the two actual source directions are independent and neither parallel nor A-orthogonal. Coherent overlap explains why the added residual norm is larger than R2-R1; taking the difference of maxima loses their shared direction information.

On the exact source-active plane S, G2>=lambda_minus A, giving a certified positive lower frame. On S's A-orthogonal complement, both measured sources vanish exactly. Thus the full retained lower frame constant is zero. The residual norm on ker b1 is R_delta(1-sigma); it is an attained SUPREMUM, not a lower frame on every first-mode-invisible vector.

## 4. What this does and does not resolve

CC54 proves first-source invisibility on actual near-critical retained spectral bands. CC55 proves that the second response is independent and reaches some first-source-invisible directions. It does not identify those maximizing directions with CC54's particular vectors, nor prove that the critical spectral subspace lies in S. The positive active-plane frame therefore cannot be promoted to a critical-space frame.

For a prescribed nonnegative defect form D, a measured lower frame G2>=cD would at least require D to annihilate the54-dimensional measured kernel. Current source certificates do not establish that alignment. The full source may supply the missing directions, so the measured kernel is not an arithmetic nonimplication theorem and not a full-high invisible Weil vector.

The remaining original high response is Gfull=G2+Trest. Full Schur sign still requires a source-aligned upper bound Trest<A-G2. The all-cap defect-relative lower frame question separately requires full-source geometry with the specified defect and aperture dependence. NF20's complete source/action or form-dual residual majorant is the next load-bearing data. Finite mode additions alone do not supply that estimate.

CC52's >1/5 compensated-tail pivot and its55-dimensional moment-constrained gate remain preserved. No carrier transfer is claimed. Whole supported original positivity remains21/20; target53/50 whole sign, full-critical frame, contact exclusion, RH/F4 and Lean remain open. [Exact certificate](data/RPB108_RESIDUAL_GEOMETRY_CC55_CERTIFICATE_20261009.json) and custody record the replay and scope; no GitHub Actions or Lean replay is claimed.
