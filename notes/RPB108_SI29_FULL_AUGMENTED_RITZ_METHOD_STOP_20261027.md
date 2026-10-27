# Stop the canonical full-SI29 augmented Ritz/cap method

Base: PR #342 / 95ea0db2ac60bc0f3c5e220067a3f405afab5ffd.
Canonical obligation: W-ODD-NEG remains OPEN. Only its current next_action is
prepended with this conditional method stop; the historical action is preserved.
No active obligation, status, dependencies or acceptance condition is changed.
This is a scoped method stop,
not an original signed negative direction, a whole-operator proof or RH.

## Decision

The exact Astar Galerkin inverse with SOURCES J470 and TRIAL span(J470,F14)
cannot pass the cap-only necessary gate at any 0<theta<=97/100, for ANY
valid cap C>=Kminus. In particular, the inherited SM40/MG07 threshold is
below 97/100, so the canonical SI29-augmented Ritz/Young sufficient route
is stopped EVEN IF its strong residual penalty were zero.

There is no need to compute the full arch mixed block or 484D energy matrix
solely to decide this stopped method. Such calculations require a separate
justification under a changed criterion or trial. The full original signed
operator remains undecided. Thresholds above 97/100, other trial spaces,
other inverse approximations and the exact original signed Schur are not
ruled out. No new source-dimensional campaign follows automatically.

## A stronger complete negative action bound

Keep EXACTLY W=(I-P_J470)FC with the accepted original physical projection
and dyadic C. W is physically orthogonal to the whole original J470 and
W*W<=101/100 I. It is not endpoint-aligned or energy-projected.

For each of the original 107 SI10 clusters [a,b], center c, half-width r,
original order p, the first p Fourier Taylor coefficients of W vanish
EXACTLY: the corresponding odd polynomial sine/cosine generators belong
to J. The previous #334/#338 bounds computed the first omitted jet k=p
but paid everything thereafter with a generic remainder. This refinement
computes ALL 14 components at k=p,p+1,p+2 for EVERY cluster: 321 jets.

The magnitude of each scaled jet is the norm of

    v_k = (2*pi)^k/k! * < x^k trig_k(2*pi*c*x), W >,
    trig_k=sin for even k, cos for odd k.

The complex phase of the Fourier derivative has modulus one. The native
Gram helper integrates the FULL physical interval; there is no missing
Fourier or reflection factor. Every vector component is retained as a
4096-bit Arb ball. Exact dyadic box radii give a rational squared norm
upper; a dyadic square-root upper bounds its vector norm. With P=p+2,

    finite = sum_(k=p)^P r^k ||v_k||_upper,
    rem^2 = 2B*(101/100) * ((44/7)*B*r)^(2P+2)/((P+1)!)^2.

The real-frequency exponential Taylor remainder and Cauchy-Schwarz prove
this entire-interval remainder for arbitrary W coefficients together.
A rational Young parameter gives

    sup_(xi in cluster) ||What(xi)||^2
       <= (1+d)*finite^2 + (1+1/d)*rem^2 = L_j.

Reuse #338's original TWO-SIDED squared-height masses M2_j, which pay all
973 negative leaves and the full kappa shift for r_minus=(kappa-m)_+.
Then

    W* V* r_minus^2 V W <= beta2 I,
    beta2=sum M2_j L_j = 2.2417268773279946e-8... <9/400000000.

The physical compression V is an isometry, so Kminus^2<=V*r_minus^2 V,
NOT equality. Consequently ||Kminus W||^2<=beta2. The exact bound improves
the previous complete squared-action bound by a factor >397. No new
frequency integration or source normalization solve is performed.

Native validation includes an independent entire-power physical Gram
check of all three new first-cluster jets, pole and actual features.
An independent stdlib checker recomposes all 321 vector norms, all 107
remainders/Young payments, the squared action and both final ray margins.
The inherited native closed-form Gram/projection certificate remains a
dependency; arithmetic replay does not independently re-prove it.

## Eliminate the unknown energy correction without computing it

Let A=Astar and H=W*A W. The accepted actual energy Schur after eliminating
J is T_A>=h I, h=9/9091. Since T_A<=H, we also have H>=h I.
For either accepted original stopping ray f in J define the exact real

    q=H^-1 W*A f,   g=f-Wq.

This definition uses the finite form matrix; no computed q or full A inverse
is assumed. Form orthogonality gives W*A g=0 and

    A(g)=A(f)-q*Hq.

The negative action is NOT invariant under adding W. It is paid explicitly:

    Kminus(g)=Kminus(f)-2 Re q*W*Kminus f+q*W*Kminus Wq.

Dropping the last NONNEGATIVE term and using ||W*Kminus f||<=sqrt(beta2)||f||
yields, with theta0=97/100 and s=||q||,

    Kminus(g)-theta0 A(g)
       >= gap_f -2 sqrt(beta2)||f|| s +theta0*h*s^2
       >= gap_f - beta2 ||f||^2/(theta0*h).

This completes the square; it does not require a tiny perturbation of a
nominal Schur matrix, a fixed forcing approximation or separate inverse
charges. It is why the illustrative 1% inverse target from #342 need not
be imposed to DECIDE THIS METHOD.

The accepted exact-rational 960-cell source stopping artifact gives gap_f
for f=12001*sin(2*pi*(37/64)x)+16384*sinh(x/2), and the distinct cap-selected
ray with coefficients (3013,4096). Both are genuine ORIGINAL J functions.
A positive exact sinh series proves sinh(B/2)<3/5, hence

    ||f||^2 <= 2B*(|alpha|+(3/5)|b|)^2.

No new low-frequency integration is needed. Exact complete graph margins:

| Original ray | Accepted gap lower | Whole 14D correction upper | Remaining strict lower (rounded down) |
|---|---:|---:|---:|
| Direct (12001,16384) | 1,286,120.156730... | 24,477.438477... | >1,261,642.718 |
| Cap-selected (3013,4096) | 85,059.302394... | 1,536.995925... | >83,522.306 |

The displayed correction values are upward decimal displays; exact
Fractions in the artifact carry acceptance. Only one strict ray is needed;
both pass. These are lower bounds for Kminus(g)-0.97*Astar(g), NOT for
Kminus(g)-Astar(g). They do not establish original signed negativity.

## Why this graph is precisely the augmented Galerkin image

Let V=span(J,W)=span(J,F). All fourteen normalized residual directions
are independent modulo J, and the original J Gram is invertible. Define
Z as the EXACT Astar Galerkin inverse for the ORIGINAL source synthesis J
in this full V. For every source coefficient y,

    <v,A Z y>=<v,J y> for every v in V.

Because W*J=0, ran(Z) is contained in {g in V: W*A g=0}. Conversely, for
our g=f-Wq in this latter space, choose y by

    (J*J)y = J*A g.

The finite physical J Gram is invertible, and the W test equation is zero
on both sides. Galerkin uniqueness therefore implies Z y=g. Also g is
NONZERO: f is a nonzero J vector and Wq is physically J-orthogonal.
Thus the unknown graph direction is genuinely in the exact full augmented
Galerkin image for a nonzero ORIGINAL source coefficient y.

For any C>=Kminus and 0<theta<=0.97, coercivity A(g)>0 implies

    <y,[theta Z*A Z-Z*C Z]y>
      =theta A(g)-C(g) <=0.97 A(g)-Kminus(g)<0.

The cap-only necessary matrix test fails. Adding a nonnegative residual
charge or multiplying C by 1+t cannot repair it. This is an existential
matrix witness with a quantitative uniform correction bound; the source
coefficient y need not be numerically constructed to prove failure.

An independent exact coupled 4D regression checks the graph/Galerkin image,
the completed-square bound, and an example where this theta-cap method
fails while A-K is strictly POSITIVE. This explicitly tests the scope.

## Custody, standing and critical-path consequence

Pinned native physical input: run 40417043904 / source
0e3321350980247f8cba46cdbb45b717e49ad213 / archive 12694539474, containing
matched original projection and full-frame JSONs. Pinned squared masses
and Schur input: run 40423854196 / source
fa7986b3fd83b8fd93014c886eb26943807e0202 / archive 12699072252. Pinned source
stopping rays: successful run 40194516892 / source
59b6449f11e7fae8791d8baf35cc049ad15826a5 / artifact 12599562140.
The focused workflow checks all run/source/artifact/archive/JSON hashes.
Native python-flint is pinned to 0.8.0 at 4096 bits. The bounded local full
calculation takes about 13 seconds. No expensive old integration is rerun.

Conditional analytic proof, native jet enclosures, exact arithmetic replay
and independent original Fourier/domain review have separate standing.
The original source-only stop did NOT already cover the enriched trial;
this new argument and complete negative action payment are necessary for
that extension. Historical source-only artifacts retain their old scope.

Reconcile: the canonical SI29-augmented Ritz/SM40-threshold sufficient method
is STOPPED, under the inherited domain assumptions. The active objective
W-ODD-NEG remains OPEN. Do not continue computing its arch block/14D response
solely for this stopped gate. The next justified strategy review concerns
the threshold loss versus the exact original signed Schur, or another
trial/method with a demonstrated benefit; it does not automatically add
source directions. Even/CC27/Weil/RH and independent domain review remain
OPEN. Draft/unmerged; no original positivity or negativity is claimed.
