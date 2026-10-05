# RPB108: explicit finite certificates for the actual form

Base: research 43dc2f25dae7642253633d35eebdc7ea1a4cb3d1.

## Theorem

At each fixed actual aperture a, the canonical bounded native operator A is approximated in operator norm by explicit finite-rank perturbations of the identity, with a stated error tending to zero.

A finite strictly negative eigenvalue exceeding that error produces an actual negative vector on D_a. A finite positive lower bound exceeding the error certifies strict positivity on all D_a. The unresolved near-zero case is not silently classified as an endpoint.

The exact index and kernel also admit a finite-dimensional Schur reduction with a proved positive infinite-dimensional complement. This reduction derives the complement positivity from the approximation error, not from background positivity.

## Terminology before use

**Finite physical Fourier approximation:** J_TN below, obtained by low-frequency truncation and Taylor approximation of the physical Fourier kernel.

**Finite form certificate:** a spectral bound for A_TN together with its rigorous native operator-error bound.

**Exact finite Schur form:** the actual finite-dimensional form after eliminating the proved-positive high complement.

The finite-dimensional spaces consist of canonical form-domain vectors, not raw multiplicity copies. No physical spectral-domain assumption is made.

## Actual bounded correction

Let H=D_a with logarithmic inner product and J:H -> L2(R) its physical inclusion. Since w>=1, ||J||<=1. The actual mixed dictionary gives
\[
A=I+J^*C_aJ,
\tag{1}
\]
where C_a is a bounded self-adjoint physical L2 operator.

Its Fourier part is the actual archimedean-minus-logarithmic multiplier and finite native prime translations. Its pole part uses the two supported vectors
psi_plus/minus(x)=1_[-a,a](x) exp(plus/minus x/2).
The rank-two operator gives exactly the native cross moments on supported inputs. This defines a bounded extension on all physical L2, including the approximating outputs below.

With the established archimedean envelope C0,
\[
\|C_a\|\le c_a:=
C_0+2\sum_{\log n\le2a}\frac{\Lambda(n)}{\sqrt n}
+4ae^a.
\tag{2}
\]
The pole estimate follows from 2||psi_plus||||psi_minus||<=4ae^a. The prime cutoff includes equality thresholds. Every coefficient and normalization in (1) is actual native data.

## Explicit finite-rank approximation of physical inclusion

For T>0 and integer N>=0, define
\[
(B_{TN}h)(\xi)=1_{[-T,T]}(\xi)
\sum_{j=0}^N\frac{(-2\pi i\xi)^j}{j!}
\int_{-a}^a x^j h(x)\,dx,
\qquad
J_{TN}=\mathcal F^{-1}B_{TN}.
\tag{3}
\]
This has rank at most N+1. The moments are bounded functionals on H.

The omitted Fourier tail satisfies
\[
\|1_{|\xi|>T}\widehat h\|_2
\le\frac{\|h\|_H}{\sqrt{\log(e+T)}}.
\]
On the rectangle |x|<=a, |xi|<=T, exponential Taylor remainder is bounded by
\[
e^{2\pi aT}\frac{(2\pi aT)^{N+1}}{(N+1)!}.
\]
The rectangle's area is 4aT, so its kernel error has Hilbert-Schmidt norm at most sqrt(4aT) times this remainder. Plancherel and ||h||_2<=||h||_H give
\[
\|J-J_{TN}\|\le\eta_{TN}:=
\frac1{\sqrt{\log(e+T)}}+
\sqrt{4aT}e^{2\pi aT}
\frac{(2\pi aT)^{N+1}}{(N+1)!}.
\tag{4}
\]
Given any desired eta>0, first take T large enough for the first term to be below eta/2, then N large enough for the second to be below eta/2. No uncontrolled tail remains. The bound is deliberately coarse and does not assert practical computational cost.

J_TN h is a physical L2 approximation, generally not supported in [-a,a]. It is not itself promoted to an actual witness.

## Finite native operator and error

Define
\[
A_{TN}=I+J_{TN}^*C_aJ_{TN}.
\tag{5}
\]
Since ||J_TN||<=1+eta_TN, expansion of the difference in (1)-(5) gives
\[
\|A-A_{TN}\|\le
\epsilon_{TN}:=c_a\eta_{TN}(2+\eta_{TN}).
\tag{6}
\]
Thus the error can be made arbitrarily small.

Let E=Ran J_TN^*, a closed finite-dimensional subspace of H, and F=E^perp=ker J_TN. A_TN preserves E and equals I on F. It therefore reduces to a finite matrix B_TN=A_TN|E plus the identity.

The vectors spanning E are logarithmic Riesz representers of the finitely many moments in (3), or their linear combinations. They belong to D_a by construction. Exact finite Gram and native matrix entries must still be evaluated or rigorously enclosed for numerical use; the theorem does not pretend that the Riesz construction is already a numerical implementation.

## Rigorous sign certificates

Take epsilon=epsilon_TN<1.

If the finite block satisfies
\[
B_{TN}\ge gI_E,\qquad \min\{g,1\}>\epsilon,
\]
then
\[
A\ge(\min\{g,1\}-\epsilon)I_H>0.
\tag{7}
\]
This certifies strict positivity on the entire actual domain.

If e in E is a unit eigenvector with eigenvalue mu<-epsilon, then
\[
Q_a(e)=\langle e,Ae\rangle\le\mu+\epsilon<0.
\tag{8}
\]
The witness is e in the canonical D_a, with its actual unchanged P_a e and N_a e. No approximate physical output J_TN e is substituted for it. This supplies lawful input to the already proved fresh first-contact constructor if a finite negative certificate is obtained.

Every actually strictly coercive window eventually satisfies (7), because its positive gap dominates a sufficiently small epsilon. Every actual negative window eventually satisfies (8): a fixed negative Rayleigh value persists in A_TN for sufficiently small error, and all negative spectrum of A_TN lies in its finite block.

These are completeness statements for strict signs at a fixed window. No such sign has been computed in this note. An eigenvalue enclosure meeting zero does not prove an actual null vector or nonnegativity.

## Exact finite Schur reduction

Relative to E plus F write the actual A as
\[
A=\begin{pmatrix}B&V^*\\V&H_F\end{pmatrix}.
\]
By (6),
\[
H_F\ge(1-\epsilon)I_F,\quad
\|B-B_{TN}\|\le\epsilon,\quad
\|V\|\le\epsilon.
\]
The high complement is therefore positive and boundedly invertible. Define the exact finite Schur form
\[
S=B-V^*H_F^{-1}V.
\tag{9}
\]
Bounded completion gives
\[
n_-(A)=n_-(S),\qquad
\dim\ker A=\dim\ker S,
\]
and the explicit enclosure
\[
\|S-B_{TN}\|\le
\epsilon+\frac{\epsilon^2}{1-\epsilon}
=\frac{\epsilon}{1-\epsilon}.
\tag{10}
\]
For an exact kernel vector e of S, the corresponding actual vector is
\[
h=e-H_F^{-1}Ve\in E\oplus F\subset D_a.
\]
The inverse here is a derived bounded form inverse on F. It does not assume any physical unbounded-operator domain.

S is an exact mathematical finite reduction. Its entries contain the actual complement resolvent and are not automatically known from B_TN alone. Equation (10) provides a certified enclosure, not permission to identify a near-zero approximate eigenvalue with an exact kernel.

## Consequence for the research cursor

Actual negative input is no longer only an abstract supplied field: a rigorously evaluated finite negative certificate would construct a lawful canonical witness and activate the fresh first-contact route. Strict positive windows likewise admit finite certificates.

What remains independent is the sign information. The approximation theorem supplies neither an actual negative certificate nor an all-window positive gap. Its unresolved zero band retains precisely the endpoint question; shrinking an enclosure without a strict sign does not resolve that question.

The previous stable near-null observation theorem remains valid. This finite reduction adds explicit control of the infinite-dimensional complement without importing background positivity.

## Validation and cursor

Analytic estimates from the existing actual dictionary, Fourier tail bound and elementary Taylor remainder. No new external input, numerical eigenvalue calculation, implemented certified search, actual endpoint/negative claim, RH conclusion, Lean source/workflow change or CI claim. Certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 43dc2f2, the actual fixed-window form admits an explicit finite-rank certificate. Write A=I+J*C_a J, where J is physical inclusion and ||C_a||<=C0+2 sum_(log n<=2a) Lambda(n)/sqrt(n)+4a exp(a). Truncate physical Fourier observation to |xi|<=T and Taylor-expand exp(-2pi i x xi) through degree N. The resulting finite-rank J_TN has error eta<=1/sqrt(log(e+T))+sqrt(4aT)exp(2pi aT)(2pi aT)^(N+1)/(N+1)!. Thus A_TN=I+J_TN*C_a J_TN has error epsilon<=||C_a|| eta(2+eta), arbitrarily small by choosing T then N. On E=Ran J_TN*, A_TN is finite-dimensional and equals I on Eperp. For epsilon<1, the exact actual high complement is positive; its bounded Schur reduction S has the same index/nullity as A and ||S-A_TN|E||<=epsilon/(1-epsilon). A finite eigenvalue below -epsilon gives a lawful actual negative vector, while a finite lower bound above epsilon certifies strict positivity. Every actual strict negative or strictly coercive fixed window is eventually detected, but an error interval containing zero does not certify a kernel. Finite Gram/native entries and numerical enclosures have not been evaluated here; the theorem is an analytic certificate with explicit tail error, not an implemented search or actual sign result. Same-vector source custody remains on D_a, with no raw preimage or physical operator-domain assumption. No endpoint/RH conclusion or new Lean/CI result; FULL TRANSPORT CLOSED remains open.
