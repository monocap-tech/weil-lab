# NF739 — Exact complex two-support Gram condition and the first three-support obstruction

**Canonical iteration:** NF739 · **Track:** Phase IV · **Stacked from:** [NF738 PR #763](https://github.com/monocap-tech/weil-lab/pull/763) · **Registry:** [Issue #761](https://github.com/monocap-tech/weil-lab/issues/761).

## 1. Recovered compiler status; do not relabel queued work as accepted

NF737's complete original numerical index-zero source job and NF738's actual original finite-collar complex-span proof source job were **still queued** at the most recent recovery. No new NF737 original numerical gate, no NF738 finite-span kernel theorem has been certified by those CI runs yet.

The separately accepted **actual original signed EF** two-generator complex collar span theorem from canonical NF736 (historical `nf735` source symbols) **did pass Lean** in successful job **136461473716** of [run 44786163030](https://github.com/monocap-tech/weil-lab/actions/runs/44786163030), with standard axiom receipt [14656510729](https://github.com/monocap-tech/weil-lab/actions/runs/44786163030/artifacts/14656510729). The simultaneous *pure* support-geometry job failed its initial `MeasureSpace ℝ` instance check and was repaired separately. The accepted original local theorem remains confined to the exact frozen two-collar support E and the literal NF598 `11/10` window.

## 2. Sharp Hermitian two-block condition

The canonical NF736 mathematical pilot presented a *real* 2×2 sufficient determinant test. NF739 makes the missing **complex, Hermitian** algebra completely explicit, without assuming any additional fact about the actual zeta Weil form.

Let the two diagonal energies be `a,b : ℝ` and the mixed coefficient be `p + iq`. Represent the arbitrary complex mixing coefficients as `u_r + i u_i` and `v_r + i v_i`. The exact realification of the Hermitian quadratic energy is

[
Q=a(u_r^2+u_i^2)
+2\bigl[p(u_r v_r+u_i v_i)+q(u_r v_i-u_i v_r)\bigr]
+b(v_r^2+v_i^2).
]

(The sign of the `q` term corresponds to the explicitly stated orientation `2Re((p+iq)u\overline v)`.)

If

[
a\ge0,\qquad b\ge0,\qquad p^2+q^2\le ab,
]

then `Q ≥ 0` for every arbitrary complex coefficient pair. Equivalently, the complex mixed coefficient must satisfy `|m|² ≤ ab`.

For `a>0`, the exact identity used for the source-independent Lean candidate is

[
aQ
=(a u_r+p v_r+q v_i)^2
+(a u_i+p v_i-q v_r)^2
+(ab-p^2-q^2)(v_r^2+v_i^2).
]

The `a=0` case forces `p=q=0` under the determinant hypothesis and leaves the nonnegative `b` diagonal. Thus the algebra handles even the degenerate diagonal case without division by zero or hidden strict positivity assumptions.

The new source `ActualZetaPhaseIVHermitianTwoBlockPSD.lean` contains two standalone Mathlib **Lean theorem candidates**: `neutralNF739HermitianTwoBlockPSD` and `neutralNF739HermitianTwoBlockExactSquares`. These are *pure algebra*: **no actual EF sesquilinear form, prime sum, archimedean or pole term has been identified with `p+iq`**.

## 3. Three-support obstruction: every pair can pass, yet the full span fails

Consider the **real symmetric 3×3** Gram matrix with diagonal `1` and every off-diagonal coefficient `-1`:

[
G=\begin{pmatrix}
1&-1&-1\\
-1&1&-1\\
-1&-1&1
\end{pmatrix}.
]

Its quadratic form is

[
T(x,y,z)=x^2+y^2+z^2-2(xy+xz+yz).
]

Every **complete two-coordinate principal restriction** is nonnegative:

[
T(x,y,0)=(x-y)^2\ge0,\quad
T(x,0,z)=(x-z)^2\ge0,\quad
T(0,y,z)=(y-z)^2\ge0.
]

But

[
oxed{T(1,1,1)=-3<0.}
]

The new source `ActualZetaPhaseIVThreeSupportObstruction.lean` formalizes all three pairwise PSD statements, exact negative value and existence of a negative full three-support vector. This is an **abstract three-dimensional counterexample**, not a negative instance of the actual Riemann zeta Weil form.

**Implication for Phase IV:** Even if one could prove the sharp Hermitian two-support Cauchy–Schwarz/determinant bound for every individual pair of support pieces, that alone would not establish positivity of arbitrary finite combinations. Positive semidefiniteness of all **2×2 principal submatrices** is not sufficient for a general 3×3 matrix. The next real Weil step would require *higher-order simultaneous Gram compatibility*, a structural factorization, or another argument that controls all finite mixed families—not only each pair separately.

## 4. Exact verification discipline

The CI workflow compiles the two new generic Mathlib modules **independently**. Each requires its own actual `.olean` and printed `#print axioms` output parsed by `scripts/nf739_phaseiv_gram_pilot_audit.py`, rejects `sorryAx` and nonstandard axioms, and emits two separate, source-SHA-bound accepted audit artifacts **only after the corresponding Lean job passes**.

No numerical zeta data are imported by these generic modules. Their eventual Lean acceptance must not be reported as a source-specific signed Weil positivity theorem.

## 5. Current Phase IV open contracts

1. Precisely define the **unwindowed centered mixed zeta-Weil pairing**, with source-checked orientation, involution, poles, gamma term, logarithmic prime powers and EF normalization. NF598's fixed `11/10` window cannot be discarded by notation.
2. Verify the pairing is Hermitian and sesquilinear on the intended global complex test class, and its diagonal equals the actual Weil criterion form in an appropriate common domain.
3. Establish genuine **arithmetic off-diagonal bounds** for the two-support pilot—not just the generic mathematical statement that such a bound would imply 2×2 PSD.
4. Extend beyond separate pairs to **every finite mixed-support Gram matrix**, in light of the explicit three-support countermodel; pass any dense-limit argument only in a topology with proved continuity.
5. Keep Phase III original matrix index-zero and remaining numerical enclosure custody separate. Neither Phase IV algebra nor accepted local E coercivity closes the original global Boolean gate bank.

**Global Weil positivity is OPEN. RH is NOT proved.**
