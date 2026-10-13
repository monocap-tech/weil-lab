# RPB108: positive carrier equivalence and the exact unit-gain obstruction

Base: research 080a250ccf17adf2017248b7939bd1285b76cd5f.

## Minimal carrier theorem

Fix a>0. Let D_a be the canonical supported logarithmic Hilbert domain, now identified analytically with the full actual source graph and its Green closure. Write h_f for its physical vector, P=S_+ for normalized positive sampling, N for normalized full negative sampling, and B=S_B for any fixed selected-background projection of N.

The preceding actual logarithmic sampling theorem makes P,N,B bounded on D_a. The global actual positive-kernel theorem gives ker P={0}. The full-domain source/native identity and Gårding estimate give
\[
\|f\|_{D_a}^2
 \le\|Pf\|^2-\|Nf\|^2+K_a\|h_f\|_2^2
 \le\|Pf\|^2+K_a\|h_f\|_2^2
\tag{1}
\]
with finite nonnegative K_a. No background positivity is assumed.

Then:

1. There exists eta_a>0 with ||Pf||>=eta_a||f||_D for every f. Thus Ran P is closed.
2. The completion of D_a/ker P under ||[f]||_+=||Pf|| is canonically boundedly equivalent to D_a and the whole source graph. In fact ker P is zero and this norm is already complete on D_a.
3. The kernel inclusion ker P subset ker B holds. There is a unique bounded T:Ran P -> lp2 with B=TP.
4. T is a contraction exactly when ||Bf||<=||Pf|| for every f, equivalently B*B<=P*P on D_a. This inequality is still independent input; the theorem supplies bounded gain, not unit gain.
5. The raw synthesis quotient lp2/ker G, with its inherited quotient norm, is not boundedly equivalent through G to D_a. Its image is dense but proper. Completion in graph or positive energy, rather than the inherited quotient norm, yields D_a.

These statements identify exactly which carrier distinctions survive.

## Compactness of the physical embedding

Let J:D_a -> L2(R) send f to h_f. Since w(xi)=log(e+|xi|)>=1, this is bounded.

For R>0, the map
\[
h\longmapsto 1_{[-R,R]}(\xi)\int_{-a}^a h(x)e^{-2\pi i\xi x}\,dx
\]
is Hilbert-Schmidt from L2(-a,a) to L2(-R,R): its kernel has modulus one and squared integral 4aR. Extending the output by zero and applying inverse Fourier produces a compact map J_R:D_a -> L2(R).

For ||f||_D<=1, Plancherel gives
\[
\|(J-J_R)f\|_2^2
 =\int_{|\xi|>R}|\widehat h_f(\xi)|^2\,d\xi
 \le\frac1{\log(e+R)}.
\]
Hence J_R converges to J in operator norm. The physical embedding J is compact. This uses logarithmic growth of the weight and bounded physical support; it assumes no Sobolev regularity or operator-domain membership.

## Removing the compact remainder

Suppose P is not bounded below. Choose f_j with ||f_j||_D=1 and ||Pf_j||->0. By compactness of J, pass to a subsequence for which h_fj converges in physical L2.

Apply (1) to differences:
\[
\|f_j-f_k\|_D^2
 \le\|P(f_j-f_k)\|^2+K_a\|h_{f_j}-h_{f_k}\|_2^2
 \longrightarrow0.
\]
Completeness of D_a gives f_j->f in D_a. Continuity gives ||f||_D=1 and Pf=0, contradicting ker P={0}. Therefore eta_a>0 exists.

Injectivity here is the already proved actual critical-sampling rigidity: a compact-support entire transform vanishing at all actual critical-line ordinates vanishes identically, because documented simple-critical-zero density supplies more than O(T) distinct samples. No simplicity of all zeros or RH is assumed. This theorem inherits that external dependency.

The proof produces a nonconstructive fixed-window lower bound. It supplies neither a numerical eta_a nor uniform control as a varies or tends to infinity.

## Positive completion and factorization

Bounded sampling and the lower estimate give
\[
\eta_a\|f\|_D\le\|Pf\|\le\|P\|\,\|f\|_D.
\]
Thus the positive norm is equivalent to the canonical logarithmic norm. Its completion consists of the same vectors, with the same physical coordinate and source samples. This is stronger than mere algebraic positive observability.

If Pf_j is Cauchy, the lower bound makes f_j Cauchy in D_a; taking its limit proves Ran P is closed. P:D_a -> Ran P is a bounded isomorphism.

Define
\[
T(Pf)=Bf.
\]
The definition is well-defined by ker P subset ker B; here ker P=0. It is bounded with ||T||<=||B||/eta_a and is unique on Ran P. If a map on the entire positive coefficient Hilbert space is required, its canonical zero extension is T composed with the orthogonal projection onto the closed Ran P. This extension has the same norm and retains B=TP. No background positivity enters this construction.

The unit bound is exact:
\[
\|T\|\le1
\iff
\forall f,\ \|Bf\|\le\|Pf\|
\iff
B^*B\le P^*P.
\]
The adjoints here use the canonical D_a Hilbert inner product and the raw coefficient Hilbert inner product. Since B and P are bounded on this complete domain, the operator inequality is meaningful without a spectral unbounded-operator domain.

For background selection s, the equivalent scalar condition is
\[
Q_{{\rm bg},s}(f)
 =\|Pf\|^2-\|Bf\|^2
 =Q_{\rm native}(f)+\|N_{{\rm selected},s}f\|^2
 \ge0.
\]
This is precisely the still-needed actual WD-T10 domination. The positivity known for a<=0.8 supplies unit gain there; the present theorem supplies finite gain on every fixed a. Finite gain does not imply unit gain.

## Raw quotient versus energy completion

Let H_raw=lp2(actual divisor copies), and let G:H_raw -> D_a be actual whole Green synthesis followed by the canonical identification. The certified Green and gradient synthesis maps give a bounded map into supported H1_0. The elementary logarithmic bound by H1 energy and the newly proved source sampling estimate make G bounded into D_a and into the full graph.

Consequently ker G is closed. The Hilbert quotient
\[
Q_{\rm raw}=H_{\rm raw}/\ker G
\]
with its inherited quotient norm is complete, and G induces an injective bounded map G_bar:Q_raw -> D_a whose image is Ran G. Copy redundancy is lawfully removed by this quotient.

The image is dense by the proved full Green-graph density. It is proper because every raw Green synthesis has an L2 weak derivative, while D_a also contains nonzero interval step functions. For example
\[
h=1_{[-a/2,a/2]}
\]
is supported in [-a,a], and its Fourier transform is bounded near zero and O(1/|xi|) at infinity. Hence its logarithmic energy is finite. Its distributional derivative is a difference of two nonzero point masses, which is not represented by L2; thus h is not H1 and is outside Ran G.

Therefore Ran G is dense and nonclosed. If the inherited quotient norm and the transported D_a norm were equivalent on Q_raw, its completeness would force Ran G to be closed in D_a. This contradiction proves that the raw quotient topology is genuinely stronger. In particular, no bounded inverse to G_bar exists on its image, and G_bar is not onto the canonical carrier.

On Q_raw one can instead use the energy norm
\[
\|[v]\|_{\rm obs}=\|Gv\|_D,
\quad\hbox{or}\quad
\|[v]\|_+=\|PGv\|.
\]
These are norms because the quotient removes ker G and P is injective. They are equivalent by the positive lower bound. Their completions are canonically D_a, the full source graph, and Ran P with their respective equivalent norms.

The weaker completion may contain physical vectors with no raw lp2 synthesis preimage. Source custody survives because bounded analysis extends on the physical energy carrier; it does not require inventing new raw coefficients for such a vector.

Raw multiplicity remains in every energy sum. Quotienting synthesis redundancy neither discards multiplicity weights nor creates independent observations from identical copies.

## Exact obstruction and next work

The analytic carrier comparison and bounded factorization are now closed. The positive completion absorbs the canonical logarithmic/source carrier by an equivalence of norms, while the inherited raw synthesis quotient remains a different, stronger carrier with only a dense proper image. Its observation-energy completion recovers the canonical carrier.

The remaining WD-T10 obstruction is exactly unit domination, not a missing kernel inclusion, completion, closed positive range, or bounded factor constructor. To close it one must prove the actual selected-background quadratic nonnegative on this domain, or produce a lawful strict negative vector disproving that proposed contraction.

An actual WD-T38 instantiation can now use the canonical carrier directly. The historically retained abstract null identity still needs same-vector identification with its actual native form. No new nonzero null witness is constructed here. Enlarged-window weak-null persistence remains independent.

FULL TRANSPORT CLOSED and F4 entry remain open.

## Validation and cursor

Analytic proof using the previous logarithmic sampling/full graph theorem, actual positive injectivity and certified source/native Gårding identity. No new external result beyond those recorded dependencies. No Lean source/workflow changes or new CI claim. Existing certified code remains cb92c1b4dfca298cbc79d5b7d25598ea370236bf, Actions run 37236113125/job 111535430775.

At 080a250, full-domain source/native equality gives Elog<=||P||^2+K||h||^2 without positivity. The supported logarithmic embedding into physical L2 is compact by Fourier truncation, and the previously proved actual critical-sampling injectivity removes the compact remainder. Thus P is bounded below on every fixed window; its range is closed, and the positive-energy completion is canonically equivalent to the canonical logarithmic/full source carrier. Every selected B factors uniquely through P by a bounded map; the kernel inclusion is proved. The factor has norm<=1 exactly when B*B<=P*P, equivalently actual selected-background positivity, which remains independent and open outside the certified short-window scope. The inherited raw lp2/kerG quotient norm is genuinely different: actual raw synthesis has H1 range, while the logarithmic carrier contains step vectors, so its dense range is proper and the quotient norm cannot be equivalent to physical/positive energy. Completing that range in graph or positive norm yields the same canonical carrier. This closes the analytic carrier comparison and bounded factorization, not WD-T10 unit contraction, retained null attachment, or enlarged cancellation. Lean unchanged; FULL TRANSPORT CLOSED and F4 entry remain open.
