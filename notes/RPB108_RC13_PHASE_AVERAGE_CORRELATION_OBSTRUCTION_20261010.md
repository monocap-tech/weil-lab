# RPB108 RC13 — phase coverage does not preserve prime correlations

2026-10-10. Independent route consolidation.
Parent: ce459c992ca859f8a172d5e374f7edefcfd15333 (RC12).
Only research/rpb108-route-consolidation is written.

## Concrete transfer test and result

Test whether translating RC12's sparse positive chains through every phase
recovers positivity on a whole interval. The translations do recover physical
mass EXACTLY. They do not recover the original mixed arithmetic form.

Every translated chain mask misses the prime2 cross correlation. After
paying the complete within-packet localization errors, an ACTUAL smooth
test inside the already certified 1.06 anchor has

    Q(h)-F(h) < -3897/5000,                            (1)

where F is the phase average of the positive masked forms defined below.
Both archimedean and signed pole terms are included.

Thus nonnegative correction and exact-form recovery are false even with
continuous phase coverage. This does not disprove a relative-loss estimate
against the actual complete averaged energies. Q(h) is positive on this
test by the existing anchor, not an original negative vector.

## Definitions before use: a mass-preserving family of masks

Let L=log9. Fix a finite cap B and put

    N_B=ceil(2B/L)+2,
    0<epsilon<=1/(1000*9^(N_B-1)).

Choose a nonzero real nonnegative smooth L-periodic function g, supported
within radius epsilon of L times the integers. Such a function is obtained
by periodically repeating a smooth compact bump. Define

    G_0=integral_0^L g(s)^2 ds,
    G_1=integral_0^L g'(s)^2 ds,
    D=G_1/G_0,
    g_s(x)=g(x-s), 0<=s<L,
    F(h)=(1/G_0)integral_0^L Q(g_s h) ds.

D is a finite derivative ratio of the chosen mask, not a critical defect.
For smooth h supported in (-B,B), each g_s h is supported in at most N_B
consecutive radius-epsilon cells with spacing log9. It is an RC12 test
after an overall translation and, where necessary, padding with zero
packets. Its profile shapes and amplitudes are arbitrary.

The exact physical mass identity is

    (1/G_0)integral_0^L ||g_s h||_2^2 ds=||h||_2^2.

RC12 therefore gives a genuine whole-support lower bound on the AVERAGED
form:

    F(h)>=gamma||h||_2^2, gamma=627/16000.              (2)

The count bound follows because cell centers intersecting (-B,B) lie in
an interval of length 2B+2epsilon, with spacing L and 2epsilon<L.
Equation (2) uses RC12 without global pole-moment restrictions. It is not
yet a bound on Q(h).

## Exact correlation coefficient retained by the average

Define the real periodic autocorrelation

    a(d)=(1/G_0)integral_0^L g(z)g(z+d) dz,
    Delta(d)=1-a(d).

Then

    a(0)=1,
    Delta(d)=(1/(2G_0))integral_0^L [g(z+d)-g(z)]^2 dz>=0,
    Delta(d)<=D d^2/2,
    a(kL)=1 for integer k,
    a(d)=0 if dist(d,L times the integers)>2epsilon.  (3)

The last statement follows directly from the narrow supports. The derivative
bound uses the periodic translation estimate
||g(.+d)-g||_2<=|d|||g'||_2. In particular a(log2)=0:
log2 lies between .6 and .7, whereas L>2 and epsilon<=.001.

Polarizing the average shows that the continuous native kernel is multiplied
by a(x-y), and each prime atom by a(log n). Thus the prime2 coefficient of
F is ZERO; the coefficient in Q is -log2/sqrt2. At aligned displacements
9^k the average instead retains the coefficient exactly.

The complete original native kernel and atoms are those pinned through
RC7--RC12 to
notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482, read at
CC119 5df347d3808ac3282864a657b7380e0f54bf4daa:

    K_cont(d)=2cosh(d/2)-j(|d|),
    j(r)=exp(-r/2)/(1-exp(-2r)),
    c_n=Lambda(n)/sqrt(n).

The exact correction E(h)=Q(h)-F(h) is

    E_cont =
      integral integral conjugate(h(x))h(y)
          K_cont(x-y)Delta(x-y) dx dy,
    E_prime =
      -sum_n c_n integral conjugate(h(x))
          [h(x+log n)Delta(log n)+h(x-log n)Delta(log n)] dx,
    E=E_cont+E_prime.                                  (4)

The local archimedean renormalization cancels because a(0)=1. Near zero,
Delta(d)=O(d^2) pays the 1/|d| kernel singularity. Hence the identity is
well defined on smooth compact tests; it follows by cutoff cancellation
and dominated passage to the continuous phase average. No new rough-domain
extension is asserted.

## Actual test, with within-packet errors paid

For the chosen finite D, choose tau>0 satisfying

    tau<=1/1000, D tau^2<=1/10000.

This is always possible. For example tau=1/[1000(D+1)] is sufficient,
using D/(D+1)^2<=1/4. Take a nonnegative even smooth profile phi supported
in (-tau,tau), with physical L2 norm one, and set b=log2,

    u(x)=phi(x+b/2), v(x)=phi(x-b/2), h=u+v.

The supports are disjoint, inside (-1.06,1.06), and ||h||_2^2=2.
Use B=1.06 for the phase frame. The inherited bound exp(53/25)<9 gives
2B/L<1 and hence N_B=3, so the stated epsilon choice is lawful.

Every cross distance between u and v lies in (.6-2tau,.7+2tau).
It is separated from all integer multiples of L by more than 2epsilon.
Thus a(x-y)=0 on the ENTIRE cross support product. In fact for every phase
s, g_s u and g_s v cannot both be nonzero, so

    F(u,v)=0,
    E(h)=E(u)+E(v)+2Q(u,v).                            (5)

The only original cross atom is prime2, with overlap exactly one and
coefficient -log2/sqrt2<-2/5. The reverse orientation and all other active
prime powers have zero overlap. On all cross distances, |K_cont|<5 as
in RC7--RC9. Since ||phi||_1^2<=2tau,

    2Q(u,v)<-4/5+20tau<=-39/50.                       (6)

This includes the full archimedean and signed pole cross interaction.

It remains to control E(u) and E(v); their internal masking errors are NOT
silently set to zero. There are no prime overlaps within a single packet,
because its diameter is <log2. At internal distance 0<r<=2tau,

    |K_cont(r)|<=3+1/r.

The pole kernel is <3. For r<=1/2, exp(2r)>=1+2r implies
j(r)<=1/(1-exp(-2r))<=(1+2r)/(2r)<=1/r.
Combining this with Delta(r)<=D r^2/2 and ||phi||_1^2<=2tau gives

    |E(u)|,|E(v)|
      <=D(12tau^3+2tau^2)
      <=3D tau^2
      <=3/10000.                                     (7)

All singular and continuous internal terms are paid. Equations (5)--(7)
prove

    E(h)<-39/50+6/10000=-3897/5000,

which is (1). The correction magnitude exceeds the available common
averaged guard gamma||h||_2^2=2gamma. The actual averaged local energies
can be much larger than that common guard; the test does not rule out
a sharper relative-energy bound.

## Why positive mixtures cannot recover the original form exactly

For this separated test pair, EVERY translated mask has zero mixed pairing.
Consequently no weighted mixture of these same masked forms can reproduce
the nonzero original mixed pairing Q(u,v). This applies even if its diagonal
physical-mass coverage is normalized by other weights.

The obstruction is missing correlations, not missing spatial coverage.
Uniform phase averaging makes that distinction explicit: it covers all
physical mass while retaining only the autocorrelation weights a(d).
Spatial translations do not supply the prime2 cross term that no individual
thin chain can see.

Equation (1) also disproves the stronger proposed sign E>=0 for this actual
averaging construction. It does not prove that every whole-domain gluing
strategy fails or that a relative bound is impossible.

## Concrete remaining transfer obligation

For each finite B, a sufficient whole-domain transfer would be

    E(h)>=-(1-nu_B)F(h), nu_B>0,

for all smooth h in the cap, with all atoms and signed continuous terms in
(4) retained. It would give Q(h)>=nu_B gamma||h||_2^2.
Neither the mass-frame identity nor positivity of each sparse-chain form
establishes that estimate.

A near-null version could instead supply the required decay for RC5.
The actual missing prime correlations and continuous correction must be
controlled against the actual local energies or by a new decomposition.
This step has not done so.

## Fresh validation and standing

scripts/validate_rpb108_rc13_phase_average_transfer.py passes 44 fresh exact
rational checks: cross-support and periodic-mask exclusions, original prime2
and continuous allowances, the internal-error budget, existence controls
for tau at finite derivative ratios, the -3897/5000 correction upper,
and comparison with the common averaged guard. Exponential bounds use
rational Taylor sums with geometric tail bounds. The continuous frame,
autocorrelation and functional identities are proved analytically above;
finite controls are not a proof by sampling.

The original whole 1.06 certificate remains unchanged and certifies this
h positively. RC12's sparse all-count theorem remains intact. No whole
aperture extension, original negative vector, relative-energy impossibility,
RH/F4 theorem or Lean closure is claimed. Other branches and historical
files remain unchanged.
