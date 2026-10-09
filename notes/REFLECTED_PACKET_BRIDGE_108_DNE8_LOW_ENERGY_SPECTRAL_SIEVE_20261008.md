# RPB108 DNE8 — Native spectral sieve separates reflected packets from actual null candidates

Date: 2026-10-08 America/Los_Angeles. Parent: DNE7 `43c34826d5a2a187fd2ad40cf38e43b81d6e20ba`. Definitions: [DNE8 low-energy spectral sieve](../docs/TERMINOLOGY_RPB108_DNE8_SPECTRAL_SIEVE.md). Coupled CC54 and Aperture NF19 were recovered READ-ONLY; their heads are not moved or merged.

**Classification: new whole-domain cap-dependent heat-projector localization, explicit finite-rank bound, bounded reflected-Hankel compression and a quantified DNE7 packet-separation theorem. No RH, F4, first-contact exclusion, a=53/50 whole-domain sign or Lean claim.**

## 1. Actual positive-jump spectral target

DNE3's full original pole-free native form is

    H_a=J_a-kappa_a I,
    kappa_a=log(pi)-psi(1/4)+2sum_(log n<=2a) Lambda(n)/sqrt(n).

Here J_a is the physical selfadjoint nonnegative supported operator whose closed form contains the complete continuous j(d)=exp(-|d|/2)/(1-exp(-2|d|)) jump energy, all active actual prime-power translation conductances, BOTH orientations, and the support-exterior killing term. The original Q restores positive even and negative odd Hermitian pole moments separately.

A hypothetical original zero-moment contact h solves H_a h=0 and the appropriate moment constraint. Hence it obeys the genuine FULL supported operator equation

    J_a h=kappa_a h.                                        (1)

No such h is presumed to exist. This is the ONLY spectral condition used to distinguish true candidates from DNE7's unrestricted reflected test packets.

Let E_(a,Lambda)=1_[0,Lambda](J_a) for Lambda>=0. By supported compact resolvent it has finite rank. The next two estimates make that finiteness and the spatial anti-concentration effective without an old-source inverse-gap denominator.

## 2. Spectral-projector heat smoothing, with original constants

DNE5 established the killed native heat-kernel domination by the unrestricted positive Levy semigroup and the exact logarithmic symbol lower bound. In particular

    ||e^(-J_a)f||_infinity
          < exp(3) sqrt(2/e) ||f||_2.                       (2)

For any h in ran E_(a,Lambda), spectral calculus permits h=e^(-J_a)(e^(J_a)h), with

    ||e^(J_a)h||_2<=exp(Lambda)||h||_2.

Therefore on the ENTIRE low spectral range,

    ||h||_infinity < exp(Lambda+3) sqrt(2/e)||h||_2.       (3)

For every measurable E subset (-a,a) with length m, Cauchy-Schwarz and (3) give the operator localization

    ||1_E E_(a,Lambda)||_(2->2)^2
          <= m (2/e) exp(2Lambda+6).                      (4)

The bound is independent of the minimum old source gap and does not assume any source truncation, native eigenfunction regularity, RH, or actual positivity at a new cap. It is a true *spectral* estimate, unlike DNE7's high-frequency reflected packet construction.

## 3. Explicit finite-rank bound from the native killed heat trace

The unrestricted time-one heat kernel p_1 belongs to physical L2(R), with

    ||p_1||_2^2 < (2/e) exp(6) =2 exp(5),                 (5)

as in DNE5. The killed heat kernel K_a(1;x,y) is nonnegative and pointwise dominated by p_1(x-y). Thus the operator e^(-J_a) is Hilbert-Schmidt and

    Tr[e^(-2J_a)]
      =||e^(-J_a)||_HS^2
      <=int_I int_I p_1(x-y)^2 dxdy
      <=2a||p_1||_2^2
      <4a exp(5).                                        (6)

Every eigenvalue mu_j<=Lambda contributes at least exp(-2Lambda) to the trace. Consequently

    N_a(Lambda)=rank E_(a,Lambda)
       <4a exp(2Lambda+5).                               (7)

This is a cap-only EXPLICIT count of all possible actual native jump modes below a prescribed energy, independently of the canonical source deficiency or previous positive aperture.

At a=53/50, DNE5's inherited actual arithmetic bounds yield kappa_a<15, so

    N_a(kappa_a)<4a exp(35)<5*3^35.                       (8)

The number is hugely non-optimal and does NOT compute the true dimension or number of zero modes. It is a finite-rank reduction, not an evaluated source inverse.

## 4. Quantitative separation from the DNE7 negative packet subspaces

DNE7 showed that for any sufficiently small eps>0 the two positive-half reflected intervals

    J=(3log2/8-eps,3log2/8+eps),
    J'=(5log2/8-eps,5log2/8+eps)

carry infinite-dimensional, sign-definite negative/positive subspaces of the reflected parity-comparison Hankel form. Choose eps=10^(-22) and let S=J union J' union (-J) union (-J'), of measure exactly 8eps. The original strict support separation, prime-two-only reflected overlap, and bounded continuous archimedean Hankel contribution are strengthened by decreasing eps, so DNE7's native indefinite construction remains valid there.

For every h in ran E_(53/50,kappa),

    ||1_S h||_2^2/||h||_2^2
       <(8/10^22)*exp(36)
       <(8*3^36)/10^22
       <1/1000.                                         (9)

The first strict inequality uses 2/e<1; the last is an EXACT INTEGER comparison (not floating-point sampling). Thus a low-energy h cannot be nonzero and fully supported in S. For odd h=O f (f is the positive-half restriction, without normalization), parity gives

    ||1_(J union J') f||_2^2 <(1/1000)||f||_2^2.       (10)

This quantitatively removes the very narrow arbitrary reflected packets used in DNE7 from the genuine null-eigenvector class. It does NOT say the full low-energy eigenspace has positive reflected Hankel sign: broad states and cross-region correlations are still unrestricted by (9).

## 5. The FULL reflected operator is bounded, with a rigorous spectral compression

Let B_a act on L2(0,a) with the exact DNE7 Hermitian reflected kernel

    B_a f(x)=int_0^a j(x+y)f(y)dy
       +sum_(ell_n<=2a)c_n 1_(0,a)(ell_n-x) f(ell_n-x).

The prime reflections are bounded selfadjoint partial involutions of operator norm at most 1. For t>0 the elementary inequality exp(-2t)<=1/(1+2t) gives

    j(t)<=1/(2t)+1.

For 0<x,y<a it follows that

    j(x+y)<=(1/2+2a)/(x+y).                             (11)

Carleman's Hilbert-kernel inequality, or Schur's test with weight x^(-1/2), shows the positive operator with kernel 1/(x+y) on L2(0,infinity) has norm pi. Therefore

    ||B_a|| <=pi(1/2+2a)+sum_n c_n.                      (12)

At a=53/50, CC37's exact coefficient sum S_a<12093/3740<4 and pi<22/7 give

    ||B_(53/50)|| <(22/7)(131/50)+4<13.                (13)

Let U_- be the unitary normalized odd extension from L2(0,a) to odd L2(-a,a), and E^-=U_-^*E_(a,Lambda)U_-. Then

    K_(a,Lambda)=E^- B_a E^-                            (14)

is a finite-rank selfadjoint compression with rank at most N_a(Lambda). Its actual entries require a genuine native J_a spectral basis; no such basis is evaluated here. In particular (12) is an absolute bound, not positivity.

On the DNE7 tiny support J union J', for any odd low-energy h=Of,

    |<1_(J union J') f,B_a 1_(J union J')f>|
       <=13 ||1_(J union J') f||²
       <13/1000 ||f||².                                 (15)

This is a fully quantitative bound on the *localized* comparison contribution. It neither bounds the cross terms between that support and its complement nor supplies a sign for the whole B_a.

## 6. Precise finite-dimensional first-contact test

DNE7's exact parity comparison for a real odd original zero-moment null h=O f reads

    H_a(O f)-H_a(E f)=4 <f,B_a f>,

where E f is even extension. If Q_a>=0 on the complete cap and H_a(O f)=0 with the original odd pole moment s(h)=0, original even positivity yields

    <f,B_a f> <=2 |int_0^a f(x)cosh(x/2)dx|².         (16)

The genuine candidate f also lies in the exact eigenspace

    F_a=U_-^* ker(J_a^- -kappa_a),                    (17)

which has finite dimension bounded by (7). Thus a sufficient *spectral-adapted sign discriminator* would be

    <f,(B_a-2|cosh(x/2)><cosh(x/2)|)f> >0            (18)

for every nonzero f in F_a satisfying the odd sinh-moment constraint. It would contradict (16) and exclude this specific odd moment-zero original contact. But (18) is NOT proved; merely writing this finite-dimensional matrix condition does not show RH and may be false in unrelated genuine crossing controls. If F_a is trivial, exclusion is immediate by other means.

DNE7's global infinite negative essential subspace in the REFLECTED comparison does not contradict a positive test (18) on some finite native eigenspace. Conversely, finite rank alone does not imply (18), and no sign is inferred from counting or (9).

## 7. Exact finite-contact falsifier: spectral confinement still permits an invisible higher null

Consider the rational symmetric two-site positive jump graph

    J=(1/100)[[1,-1],[-1,1]],

with eigenpairs (0,(1,1)) and (1/50,(1,-1)). Set kappa=1/50 and H=J-kappa I=-(1/100)[[1,1],[1,1]]. Give it a positive EVEN pole correction 2cc*, c=(1/10,1/10). Then

    Q=H+2cc*=(1/100)[[1,1],[1,1]] >=0.

The odd vector (1,-1) lies in ker J-kappa, has zero moment c, and remains an exact Q null. Meanwhile the reflected bounded test B=[[0,1],[1,0]] has negative expectation on that SAME low-energy vector, `<h,Bh>=-||h||²`. All operators are finite-rank, connected and positive-jump before the pole-free scalar shift. A positive ground state, old-gap-independent spectral projector and finite-dimensional reflected compression do not force (18).

This model is a structural falsifier, NOT an alternate arithmetic divisor or the unchanged original Weil identity.

## 8. Result and next DNE frontier

**Proved DNE8:** (3)-(4) low-J spectral-projector heat bounds; (6)-(8) explicit cap-only low-spectral rank; (9)-(10) quantitative DNE7 packet separation at a=53/50; (11)-(13) bounded entire reflected-Hankel operator; (14)-(17) exact finite-dimensional native spectral-compression gate and its narrowly localized error (15). Elementary exact control algebra and integer guards are provided in the linked validator.

**Still open:** spectrum/basis of the actual J_a at kappa; sign of (18); existence or absence of a zero moment H_a null; odd/even full original Q positivity at a=53/50; the CC original mixed E112/F112 Schur gate; all-cap first-contact exclusion, RH/F4/transport/Lean.

**DNE9 target:** construct or rigorously enclose the small actual low-J spectral projector or an equivalent resolvent on the source-constrained space, then evaluate (18) with complete original prime and archimedean reflected rows. A projected sign test must pay spectral approximation errors and retain the full odd pole moment. Avoid another universal reflection sign theorem, and do not treat the enormous abstract rank bound (8) as a practical finite algorithm.

The direct-null office remains independent of contemporaneous Coupled CC54 and Aperture NF19. DNE8 publication does not move their refs.
