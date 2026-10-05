# RPB108: null windows are isolated and counted by index growth

Base: research 326018b237ab9eafc72e8734d4b5bf960e4cefb4.

## Theorem for the actual full native family

Let n(a)=n_-(Q_a) and r(a)=dim ker Q_a. Both are finite at every fixed positive window. No positivity of Q_a is assumed.

For every b>a there is a self-adjoint I+compact remainder R_ab such that
\[
n(b)=n(a)+r(a)+n_-(R_{ab}),\qquad
r(b)=\dim\ker R_{ab}.
\tag{1}
\]
In particular n(b)>=n(a)+r(a).

If r(a)>0, some epsilon>0 satisfies
\[
\begin{array}{ll}
n(c)=n(a),\ r(c)=0,&a-\epsilon<c<a,\\
n(b)=n(a)+r(a),\ r(b)=0,&a<b<a+\epsilon.
\end{array}
\tag{2}
\]
Take epsilon<a. Thus every null window is isolated on both sides, even when its form is already indefinite.

The set of null windows is finite in every compact positive aperture interval. If u<v are non-null windows, then
\[
n(v)-n(u)=\sum_{u<t<v} r(t).
\tag{3}
\]
These statements do not determine whether the first positive endpoint exists.

## Terminology before use

**Null window:** a positive aperture t with nonzero full native weak-null space ker Q_t.

**Old invertible complement:** E=(ker Q_a)^perp in D_a, in the canonical logarithmic inner product. Its form operator is invertible, but need not be positive.

**Null-window index count:** equation (3), which counts multiplicities of the finitely many null windows between two non-null apertures.

**Local index budget:** the finite negative index at one fixed larger window. This is not a bound uniform over all apertures.

## Actual premises and custody

The actual forms restrict consistently under physical support inclusion D_a into D_b. They have bounded self-adjoint logarithmic Riesz operators I+compact. Physical dilation pulls them back to an operator-norm-continuous I+compact family A(t) on H=D_1, including prime activation thresholds.

The full native strict-enlargement theorem is unconditional: a nonzero vector supported in [-a,a] cannot be weak-null on D_b for b>a. Its proof uses actual translation covariance and fixed-window finite nullity, not background positivity.

Dilation is used only for comparing forms. Physical inclusion, when used below, retains the same original vector and its actual full analyses. The theorem does not substitute selected negative energy or infer a raw synthesis preimage.

## Signed-complement block elimination

Put K=ker Q_a, E=K^perp in D_a, and Z=D_a^perp in D_b. The old operator A_E on E is boundedly invertible. Indeed I+compact has an isolated finite-dimensional zero eigenspace; its restriction to the kernel complement has a spectral gap around zero. This is a bounded form inverse, not a physical operator-domain assertion. Its negative index is n(a).

The enlarged actual operator on E plus K plus Z is
\[
\begin{pmatrix}
A_E&0&V\\
0&0&B^*\\
V^*&B&C
\end{pmatrix}.
\]
Here B:K -> Z is injective: Bk=0 would make the unchanged old kernel vector weak-null on the enlarged domain, contrary to strict-enlargement rigidity.

Completing the square in E gives its old invertible form, plus
\[
\begin{pmatrix}0&B^*\\B&C_{\rm eff}\end{pmatrix},
\qquad C_{\rm eff}=C-V^*A_E^{-1}V.
\]
The algebra does not require A_E positive. The cross block V is compact and C is I+compact, so Ceff is I+compact.

Set F=Ran B, Z0=F^perp and D=B:K -> F. On K plus F the finite block
\[
W=\begin{pmatrix}0&D^*\\D&C_{11}\end{pmatrix}
\]
has inertia (r(a),r(a)), by the same explicit completion used in the positive-endpoint theorem. Its inverse is
\[
W^{-1}=\begin{pmatrix}
-D^{-1}C_{11}(D^*)^{-1}&D^{-1}\\
(D^*)^{-1}&0
\end{pmatrix}.
\]
The coupling from Z0 has the form Jz=(0,C12 z), hence J*W^(-1)J=0. Eliminating W leaves
\[
R_{ab}=P_{Z_0}C_{\rm eff}|_{Z_0},
\]
a self-adjoint I+compact operator. The resulting bounded invertible congruence is
\[
Q_b\sim Q_a|_E\oplus W\oplus R_{ab}.
\]
Negative index and nullity are invariant under congruence. This proves (1), including the case r(a)=0 with the empty finite block.

Z and Z0 are logarithmic orthogonal complements, not asserted physical collar-support spaces. New block coordinates are not renamed as retained source vectors.

## Exact local crossing at an indefinite window

On the fixed dilated carrier write
\[
H=H_-\oplus K\oplus H_+
\]
for the negative, zero and positive spectral spaces of A(a). The negative space has dimension n(a), K has dimension r(a), and A(a) is uniformly strictly positive on H+.

For nearby t, norm continuity preserves strict negativity on H- and strict positivity on H+. Every nonpositive subspace of A(t) projects injectively to H- plus K; its dimension is therefore at most n(a)+r(a).

For b>a, equation (1) supplies n(b)>=n(a)+r(a). The preceding upper bound makes equality exact. A maximal negative subspace direct-sum ker A(b) is nonpositive, so the same bound forces r(b)=0.

For c<a sufficiently close, preserved old negative directions give n(c)>=n(a). Support inclusion gives n(c)<=n(a), hence equality. If r(c)>0, (1) applied to c<a would give n(a)>=n(c)+r(c), a contradiction. Thus r(c)=0. This proves (2).

The reduced R_ab is strictly coercive for b immediately to the right, since (1) now gives zero negative index and zero kernel for its I+compact form. This is a local derived property and does not restore a full-source contraction.

## Finitely many null windows on every compact interval

Fix 0<u<=v<w. For any finite ordered collection of null windows
u<=t1<...<tm<=v, repeated application of (1), together with support monotonicity, gives
\[
\sum_{j=1}^m r(t_j)\le n(w)-n(u).
\tag{4}
\]
Every summand is at least one; the right side is finite at the fixed window w. An infinite collection would contain finite subsets violating (4). Thus there are finitely many null windows in [u,v].

This argument uses only a fixed-window budget. It does not assume n(w) remains bounded as w tends to infinity and does not exclude infinitely many null windows escaping to infinity.

## Exact index count

At a non-null t, I+compact is boundedly invertible. Norm continuity preserves its positive and negative gaps, so n is locally constant there.

Between non-null endpoints u<v there are finitely many null windows. Equation (2) says that the index is n(t) immediately to the left of each such window and n(t)+r(t) immediately to the right. Summing these jumps proves (3).

A null vector never persists unchanged in a larger window. A later null vector is a new weak-null event with its own actual source custody, and each such event strictly increases the negative index. No oscillating or accumulating finite-aperture null branch is available.

## Remaining obstruction and validation

The first finite positive endpoint, if it exists, remains consistent with this entire theorem. Subsequent index growth is not a contradiction: only the index at each fixed aperture is known finite. Excluding all finite endpoints, or deriving an actual negative input, still needs independent information.

The theorem applies to the actual full native form. Selected-background variants require their own support consistency and rigidity; these are not supplied here. FULL TRANSPORT CLOSED is not claimed.

Analytic proof from the actual compact-form family and strict-enlargement rigidity; no new external input, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775. This theorem is not newly Lean formalized.

At 326018b, the full actual native family has a null-window index count without a global finite-index assumption. Write n(a)=negative index and r(a)=nullity. At any null window, including an indefinite one, eliminate the bounded invertible old kernel complement in the enlarged form. Strict-enlargement rigidity makes the kernel coupling injective; its finite block has inertia (r,r) and zero lower-right inverse block. Hence n(b)=n(a)+r(a)+n(R_ab) and r(b)=nullity(R_ab) for every b>a. Norm continuity gives n(b)=n(a)+r(a), r(b)=0 immediately to the right, and n(c)=n(a), r(c)=0 immediately to the left. Null windows are locally finite because each consumes its multiplicity from the finite negative-index budget of a fixed larger window. For invertible endpoints u<v, n(v)-n(u)=sum_{u<t<v} r(t). Thus later null modes are isolated index-increasing events, not arbitrary persistent or accumulating modes. This is actual full-form analysis with same-vector source custody, not selected-background transport, endpoint exclusion, a globally finite defect index or an RH conclusion. No new Lean/CI result; FULL TRANSPORT CLOSED remains open.
