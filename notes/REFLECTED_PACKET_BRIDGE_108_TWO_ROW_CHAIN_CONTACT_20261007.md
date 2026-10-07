# RPB108: positivity does not collapse a two-vector comparison chain

Date: 2026-10-07 UTC. Recovered live head 3b8cd0e3b958cecdc62dd16322e266bfdab07ad9, including concurrent aperture custody.
Definitions: [two-row comparison chain contact](../docs/TERMINOLOGY_RPB108_TWO_ROW_CHAIN_CONTACT.md).
Category: endpoint exclusion / obstruction to positivity-only chain collapse.
Analytic control with an actual native background and TWO AUXILIARY observations; not an actual unshifted contact, not Lean-certified.

## Result and custody boundary

The exact actual-kernel chain theorem leaves open whether nonnegativity at first contact forces total kernel dimension one. Positivity and finite smooth observation morphology alone do not imply that conclusion. The following norm-continuous comparison aperture family has a genuine first contact at a0 with

    B_a0>=0, ker B_a0=span{h,g}, Dh=g,
    h in global H1 but not H2, g not H^(1/2).

The two vectors have opposite reflection parity. The rough endpoint quotient is one-dimensional and contains g; its regular kernel contains h. Both vectors solve the full mixed B-null equation, not just a diagonal cancellation equation.

Every actual native coefficient is retained in Q. The new negative rows are explicitly auxiliary smooth physical profiles. They are not divisor rows, do not satisfy the actual pair-translation dictionary, and are not identified with the lawful actual finite selection. The original actual Q_a0 remains strictly positive. Thus this is NOT a counterexample to actual unshifted endpoint exclusion or to the already proved critical derivative-promotion gate.

## 1. An odd actual forced inverse

Reuse the small-window conditions from the pinned actual rough-forced-inverse note:

    a0<=1/32, a0<=(1/4) exp(-2(|m0(0)|+2)).

The prime set is empty. The exact combined Euler/pole form on Omega=(-a0,a0) is

    Q(u)=integral V_a0 |u|^2
         +(1/2) integral_(Omega x Omega) J(|x-y|)|u(x)-u(y)|^2,
    J(s)=k(s)-2cosh(s/2), k(s)=exp(-s/2)/(1-exp(-2s)).

The retained proof gives V_a0>2, J>1 and canonical coercivity. In addition J is strictly decreasing on (0,2a0): k is strictly decreasing, whereas 2cosh(s/2) is increasing.

Choose real odd f in C_c^infinity(Omega), nonnegative and nonzero on the right half. Let g be the unique actual inverse Q(g,v)=<f,v>. Reflection and uniqueness make g odd. Restriction to x,y>0 gives exactly

    q_g(x)=V_odd(x)g(x)
           +integral_0^a0 J_odd(x,y)(g(x)-g(y))dy,
    J_odd(x,y)=J(|x-y|)-J(x+y)>0,
    V_odd(x)=V_a0(x)+2 integral_0^a0 J(x+y)dy>2.

This is an identity on odd vectors, not a replacement of the actual form. Its singularity at x=0 is incorporated into the positive potential. The odd sign indicator belongs to the logarithmic form domain; its finite jump has finite logarithmic energy. Lipschitz truncation on the right, followed by odd extension, is lawful for the displayed positive half-domain form. Negative-part comparison and comparison with the constant right-half profile give

    0<=g(x)<=||f||_infinity/2, 0<x<a0.

The full g is therefore bounded. Transfer to the external logarithmic Laplacian is exactly the pinned bounded-kernel transfer; its forcing is bounded. The accepted boundary upper theorem gives global continuity, zero boundary values, and |g(a0-v)|<=C/sqrt(log(1/v)). A nonzero positive interior patch W exists on the right.

For the matching LOWER bound choose a short outer interval I=(a0-delta,a0), separated from W and from 0. On I x W the continuous positive J_odd has a strictly positive minimum. Let beta be the external small-interval logarithmic torsion, supported in I. Extend it oddly when taking actual native action. On I its reflected contribution is smooth and bounded, and the retained logarithmic-kernel transfer shows q_odd,beta<=M for finite M. On I the action of the right-half indicator 1_W is

    q_odd,1_W(x)=-integral_W J_odd(x,y)dy<=-c_W<0.

Take lambda=(M+1)/c_W and b=beta+lambda 1_W on the half-window. Choose epsilon>0 with epsilon lambda below the positive patch height. Local half-domain comparison gives g>=epsilon beta on I. Hence

    c/sqrt(log(1/v))<=g(a0-v)<=C/sqrt(log(1/v))

for all sufficiently small v>0. This is an actual forced-inverse lower bound, with q_g=f, not actual nullity. Its zero extension fails H^(1/2), by the divergent exterior cross integral integral |g(a0-v)|^2/v dv. Reflection gives the negative left edge. No new aperture decimal or numerical inverse is involved.

## 2. A regular physical primitive and its smooth forcing

Define h(x)=integral_(-a0)^x g(y)dy on Omega and zero outside. Oddness gives integral_Omega g=0, so both endpoint values of h are zero and its global distributional derivative is g. Thus h is even, belongs to global H1 and fails H2. It is nonzero; on the right edge h(x)=-integral_x^a0 g(y)dy<0.

The actual global convolution action commutes distributional differentiation. This includes the pole kernel 2cosh((x-y)/2); all statements are on compact physical test sets, so exponential growth at infinity causes no distributional problem. Therefore

    D q_h=q_g=f on Omega.

Let F(x)=integral_(-infinity)^x f(y)dy. Since f is odd, compact and has total integral zero, F is smooth, compact and even. There is a real constant c0 such that

    q_h=f_h:=F+c0 on Omega.

The constant is retained: zero endpoint values of h do NOT imply q_h has zero endpoint values. The global profile f_h is smooth and is constant outside supp F; it need not be in global physical L2, but its restriction to every finite window is a bounded L2 observation. The global H1 regularity also gives local L2 native action, so this distributional identity is a lawful mixed form equation.

Parity of Q gives Q(h,g)=0. Set alpha=Q(h)>0 and gamma=Q(g)>0. All pairings below use <u,v>=integral u conjugate(v), linear in the first slot.

## 3. Exact positive projection and two-dimensional mixed nullity

Fix the SAME global profiles f_h,f and constants alpha,gamma for every b>0. Define

    R_aux,b(v)=(<v,f_h>/sqrt(alpha),<v,f>/sqrt(gamma)),
    B_b(u,v)=Q_b(u,v)-<R_aux,b u,R_aux,b v>.

On the original window, Q(v,h)=<v,f_h> and Q(v,g)=<v,f>. Q-orthogonal projection onto span{h,g} yields the exact identity

    B_a0(v)=Q_a0(v-h Q(v,h)/alpha-g Q(v,g)/gamma)>=0.

Coercivity of Q proves ker B_a0=span{h,g}. In particular B_a0(h,v)=B_a0(g,v)=0 for EVERY canonical v. This is full comparison nullity; diagonal identities alone would not prove it.

The one lawful derivative step also respects the global comparison action on these particular vectors: q_B,h=q_h-f_h, q_B,g=q_g-f, and Df_h=f give Dq_B,h=q_B,g. This does not make B commute with differentiation on its whole domain, or supply the actual divisor pair-translation law. It avoids a control whose chain exists only as unrelated diagonal zeros.

The finite correction is bounded and compact on every supported canonical domain. The family is norm-continuous after the actual physical dilation identifications: the actual Q family is norm-continuous, and the dilated smooth observation profiles vary continuously in physical L2 on each compact aperture range. Dilation identifies coefficient spaces for continuity; it changes physical vectors and is not same-vector transport.

The scalar boundary trace morphology can also be retained here without invoking the actual-null theorem on a forced vector. Because f vanishes on a whole endpoint collar, its strip tests satisfy the same local homogeneous strip identity. The integrating-factor argument from the pinned trace note proves existence of the averaged trace of g. Its lower bound makes kappa_R(g)>0, and oddness gives kappa_L(g)=-kappa_R(g). H1 gives both traces of h zero. Thus the two-dimensional comparison kernel has exactly the balanced rank-one boundary Gram and a nonzero regular trace kernel. It is not necessary to import a pointwise normalized trace theorem.

## 4. A genuine comparison aperture first contact

For b<a0, B_b is the restriction of B_a0 to smaller physical support and is nonnegative. No nonzero element of span{h,g} can have that smaller support. Indeed near the right endpoint,

    |h(a0-v)|<=C v/sqrt(log(1/v)),
    g(a0-v)>=c/sqrt(log(1/v)),

so h/g tends to zero. A combination vanishing on an entire edge collar first has zero g coefficient, then zero h coefficient. Consequently B_b has zero kernel. Its canonical operator is I plus compact, since the actual native operator is and the added rows are finite rank; nonnegativity and zero kernel imply canonical coercivity.

For every b>a0 the UNCHANGED physical vector g remains supported and has B_b(g)=B_a0(g)=0, but it is not enlarged mixed null. In a sufficiently short right exterior collar f=0 and parity gives R_aux,h(g)=0 and R_aux,g(g)=sqrt(gamma). Hence its comparison residual there is exactly q_g.

No prime shift hits the original support in that collar. The right-edge part of the exact exterior Euler convolution, using k(t+v)>=c1/(t+v) for small t,v and the lower bound above, gives

    q_g(a0+t)<=-c2 sqrt(log(1/t))+O(1).

To see the growth directly, integrate v from t to a fixed small delta: integral_t^delta dv/[v sqrt(log(1/v))] grows like 2sqrt(log(1/t)). The negative left-half g is separated from this exterior point by a0 and contributes a bounded term; the pole is bounded on the collar. Therefore the residual is nonzero arbitrarily close to the edge.

Choose a smooth exterior test v supported within the enlarged window with B_b(g,v) nonzero. The exact trial

    B_b(g+s v)=2 Re(s B_b(v,g))+|s|^2 B_b(v)

is negative for some sufficiently small scalar s of the appropriate sign. This proves negativity for EVERY strict enlargement, not just a shifted eigenvalue model. The physical vector g is unchanged; only the allowed test support and restricted coefficient carrier enlarge. Zero diagonal form persists by support restriction, while enlarged full mixed nullity fails. No actual-zeta negative form is produced because B contains the two auxiliary negative rows.

## Failed implication and smallest actual theorem

The failed implication is

    nonnegative first contact + actual native background + finite smooth
    negative observations + balanced rank-one rough quotient
        -> total kernel dimension one / no regular null member.

The constructed control has total dimension two and regular null h with Dh=g in the same comparison kernel. It is stronger than a freely prescribed physical chain, because both vectors now obey an exact nonnegative mixed-null form at a genuine aperture first contact. It is weaker than the desired actual claim, because the two observations are not actual negative divisor rows. That gap is explicit and cannot be erased by calling them an existential finite selection.

The smallest actual endpoint theorem remains

    kappa_R vanishes on the WHOLE hypothetical unshifted actual contact K.

This implies global H1 for all K, lawful derivative invariance, and K=0 by the finite-dimensional compact-support derivative contradiction. A separate actual-arithmetic theorem dim K=1 would remove longer chains but would still leave one rough terminal vector with nonzero trace; it would not finish endpoint exclusion. The bound |beta_rho|<=3/8 remains accepted for actual divisor rows, and supplies no constraint on the added auxiliary profiles. No beta coordinates are assigned to them.

This obstruction belongs to endpoint exclusion. Historical retained attachment, same-vector enlarged FULL-native null transport and F4 are unchanged and open. Certified whole-domain actual positivity remains 973/1000; the concurrent complete 112-vector native/source work at 49/50 is preserved.

## Validation and source custody

The companion script checks exact rational nonorthogonal projection identities, their residual energy and kernel dimension, and rejects an incorrect diagonal-only normalization. These finite checks do not certify the analytic inverse, edge barrier, actual arithmetic contact or Lean. The odd-kernel transfer, primitive forcing including its constant, full mixed projection equation, and enlargement residual are the analytic proof above.

Pinned repository inputs:

- Actual rough forced inverse, notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_ROUGH_FORCED_INVERSE_20261007.md, blob 525ced5f03a8fc5dee543ada83d74a5fed8d74b0.
- Exact actual derivative chain, notes/REFLECTED_PACKET_BRIDGE_108_KERNEL_DERIVATIVE_CHAIN_20261007.md, blob e124b8a31a00df61908ce71cedd4ab7f83a14c76.
- Actual averaged endpoint trace, notes/REFLECTED_PACKET_BRIDGE_108_ACTUAL_ENDPOINT_TRACE_20261007.md, blob 1996d3fb3358965c5468481c31252f3dda440e69.
- External strip custody, notes/REFLECTED_PACKET_BRIDGE_108_EXTERNAL_SEVEN_EIGHTHS_CRITICAL_FLUX_20261007.md, blob c369d3760606d9e5b9ae0f4862156fd712e5be29.

External analytic input retained from the first pinned note: Hernandez-Santamaria, Lopez Rios and Saldana, arXiv:2401.18033v2 (3 July 2024), DOI 10.3934/dcds.2024084, Theorems 1.1, 1.2 and 5.2. The native odd-half transfer is proved here; it is not a quoted theorem of that paper. Accepted quasi-RH input retains OpenAI/math adc7f1241b42e322a6451854ab7e4c146bf78a and its recorded audit limitations. No local Lean build or axiom audit is claimed. RH, actual endpoint exclusion, F4 and FULL TRANSPORT CLOSED are not claimed.
