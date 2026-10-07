# RPB108: the actual positive-source squared-height moment detects null regularity

Date: 2026-10-06 (America/Los_Angeles). Live source 47cf7b611ce74cc2eb1e1603336606f111041d97.
Definitions: [positive-source height moment](../docs/TERMINOLOGY_RPB108_POSITIVE_SOURCE_HEIGHT_MOMENT.md).
Analytic actual-source regularity equivalence; no new arithmetic moment bound or Lean certification.

## Direct actual arithmetic criterion

For any h in the actual canonical supported logarithmic domain D_c,
\[
\boxed{M_+(h)<\infty\quad\Longleftrightarrow\quad h'\in D_c.}
\tag{1}
\]
The derivative is that of the global physical zero extension. For an actual full-native null vector, automatic derivative promotion already proves h in H1 implies h' in D_c. Thus on K_c,
\[
\boxed{M_+(h)<\infty\quad\Longleftrightarrow\quad h\in H^1(\mathbb R).}
\tag{2}
\]
Only the complete positive squared-height source moment is needed; the base negative l2 source norm is already finite. Finite dimensionality of the unit-gain source space does not supply (1). This locates an exact regularity obligation in actual divisor coefficients rather than only in Fourier/boundary coordinates.

## Source convention and derivative coupling

Keep F_h(z)=integral h exp(i z x), z_q=theta_q+i beta_q and the existing normalized raw-coordinate p,n convention in the registry. Integration by parts for a global supported derivative gives F_(h')(z)=-iz F_h(z), hence
\[
p_q(h')=-i\theta_q p_q(h)-\beta_q n_q(h),\qquad
n_q(h')=-i\theta_q n_q(h)-\beta_q p_q(h).
\tag{3}
\]
All raw multiplicity copies and the source normalization are retained. The read Lean raw Green derivative theorem has exactly the -iz sign. Here the integration-by-parts identity is applied analytically to a canonical vector with global derivative membership, not asserted as a newly compiled Green theorem.

If h' belongs to D_c, both its complete source analyses are l2 by existing logarithmic sampling. Since beta is bounded and n(h) is already l2,
theta p(h)=i(p(h')+beta n(h)) is l2. This proves the reverse implication in (1). The negative squared-height moment is then finite too, by the second equation of (3). Its finiteness need not be assumed.

Changing the linear source convention flips n. It changes the beta-coupling signs, not any norm estimate or moment conclusion. No physical-L2 adjoint is substituted for a logarithmic adjoint.

## Converse through an enlarged support for translated tests

The converse cannot assume h' exists in L2 before proving it. Choose a fixed b>c and |t|<min(1,b-c). Let tau_t h(x)=h(x-t). The **test vector** changes; h itself remains the retained vector. Translations preserve whole-line logarithmic energy, and both translated supports fit [-b,b]. Set q_t=(tau_t h-h)/t in D_b.

Exact actual sampling gives
\[
\begin{pmatrix}p_q(\tau_t h)\\n_q(\tau_t h)\end{pmatrix}
=e^{i\theta_qt}
\begin{pmatrix}\cosh(\beta_qt)&\sinh(\beta_qt)\\
\sinh(\beta_qt)&\cosh(\beta_qt)\end{pmatrix}
\begin{pmatrix}p_q(h)\\n_q(h)\end{pmatrix}.
\tag{4}
\]
For |t|<=1 and |beta|<=1/2, elementary exponential/cosh/sinh bounds imply
\[
|p_q(q_t)|\le C\big((|\theta_q|+1)|p_q(h)|+|n_q(h)|\big)
\tag{5}
\]
with an absolute finite C. For example |e^(i theta t)-1|/|t|<=|theta|, cosh(beta t)<=exp(1/2), (cosh(beta t)-1)/|t| is bounded, and |sinh(beta t)|/|t|<=exp(1/2)/2. Therefore M_plus(h)<infinity makes ||P0 q_t|| uniformly bounded. No height-weighted negative moment is required in (5).

Apply the established actual positive lower bound **at the fixed enlarged support b**:
||P0 f||>=eta_b||f||_(D_b), eta_b>0.
The samples of q_t are precisely the same complete actual evaluations, with the support-independent source normalization. Hence q_t is uniformly bounded in D_b. This is the substantive use of complete actual positive observability; coefficient l2 membership by itself would not put an arbitrary prescribed sequence in Ran P0.

Take a weakly convergent subsequence in the Hilbert D_b. Physical inclusion is continuous, and q_t converges distributionally to -h'. The weak limit therefore represents -h' by a physical L2 vector with finite logarithmic energy. Its distributional support lies in [-c,c], so canonical support/domain custody puts it in D_c. This proves the forward implication of (1). It simultaneously establishes global H1 and zero endpoint traces as consequences.

No enlarged native null equation is used. q_t is only a lawful translated difference test on D_b. The original h's actual source and physical vector do not change. Dilation plays no role.

## Full contact-kernel arithmetic target

For a physical orthonormal basis e_j of the full finite K_c, define
\[
M_{+,K}=\sum_q\theta_q^2\sum_j|p_q(e_j)|^2.
\tag{6}
\]
This is basis independent under a unitary basis change. If it is finite, (2) puts all K_c in global H1. Automatic derivative promotion and the finite-dimensional derivative-chain obstruction then force K_c={0}.

Conversely, if a hypothetical K_c is nonzero, the existing regularity ceiling supplies a rough vector. At least one vector of every finite basis is rough, so (2) gives
\[
\boxed{M_{+,K}=+\infty\quad(K_c\ne\{0\}).}
\tag{7}
\]
Thus the smallest remaining arithmetic theorem on this route is finiteness of the **complete positive-source squared-height trace at every actual nonnegative candidate window**. Proving that theorem independently from the exact actual zero-null equation would exclude finite contact and close the global dichotomy. It is unproved; (6) is not an assumption hidden in a source record.

This criterion is equivalent to the existing full-kernel regularity gate, but now specifies the actual multiplicity-weighted divisor quantity to estimate. It does not show that the current branches already supply the required rate.

## Exact tail-rate target and failure of ordinary localization

Tonelli gives, with E_plus,K(T) from the registry,
\[
M_{+,K}=\int_0^\infty2T E_{+,K}(T)\,dT.
\tag{8}
\]
Indeed theta_q^2=integral_0^|theta_q| 2T dT. All terms are nonnegative. A sufficient independent tail estimate is E_plus,K(T)=O(T^(-2-epsilon)) for some epsilon>0; also O(T^(-2)log(T)^(-1-epsilon)) for large T suffices. The borderline O(T^(-2)) alone need not suffice.

Ordinary complete-source localization proves E_plus,K(T)->0 uniformly on finite K, as in the preceding source compression pass. It proves no weighted integral in (8). The ENERGY_TAIL_TEST derivative estimate consumes H1 Green custody and is not available on rough hypothetical K; even an unweighted small-tail assertion cannot supply the squared-height moment.

An exact sequence control uses p_j=(4/5)(3/5)^j, theta_j=(5/3)^j. Then ||p||^2=1 and all l2 tails decrease geometrically, but theta_j^2|p_j|^2=16/25 for every j, so the squared-height moment is infinite. A finite-support negative vector of norm one gives exact neutral norm balance without changing this fact. This is a coefficient/energy control, not an actual zero sequence, an actual sampled physical function or a native null vector. It rejects the inference from finite negative dimension, neutral norm balance and ordinary tails to a positive height moment.

Likewise the borderline tail E(T)=C/T^2 yields a logarithmically divergent integral in (8). The stronger logarithmic decay stated above is sufficient by the ordinary integral test.

## Remaining obligations and validation

Category: endpoint exclusion. This closes a lawful actual-source equivalence and gives a concrete arithmetic weighted-tail target. It does not prove moment finiteness, exclude a kernel, construct an actual negative vector or give same-vector enlarged null transport.

Prescribed packet attachment still requires named actual carrier/row/synthesis/adjoint identities. Source height moment finiteness for that named k would give its derivative-log membership once domain custody is attached, but one regular null vector need not fill a kernel of dimension greater than one. The full trace in (6) is the sufficient endpoint target.

Pinned read sources and repeated rational derivative/translation algebra and tail controls are in notes/data/RPB108_POSITIVE_SOURCE_HEIGHT_MOMENT_20261006.json. The weak-limit, observability and regularity proofs are analytic; controls do not certify them or an actual arithmetic bound. The positive-observability theorem retains its documented critical-zero-density external dependency, and logarithmic sampling retains its documented local-count dependency. No new external assumption, Lean file/build, axiom audit or CI result. Certified 19/20 positivity and newer 24/25 aperture inputs remain preserved. F4 and FULL TRANSPORT CLOSED remain open.
