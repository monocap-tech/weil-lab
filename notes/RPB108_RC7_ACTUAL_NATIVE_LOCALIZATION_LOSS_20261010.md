# RPB108 RC7 — actual native localization loss

2026-10-10. Independent consolidation branch.
Parent: da91acbb0961369dbcc9831678253edea8c5ea4e (RC6).
Only this branch is written.

## Candidate and actual arithmetic result

Test the candidate: translate the completed a0=53/50 certificate onto local
pieces of a large supported function, then combine those positive local forms.

There is a complete signed localization identity, but its correction is not
automatically nonnegative. An explicit ACTUAL native smooth-packet computation
at separation log2 gives a correction strictly below -39/50, with all
archimedean, pole and active-prime terms retained. The packets fit inside the
already certified anchor. Their full Q is positive there; the result is a
negative localization correction, not a negative original Weil vector.

This replaces a generic structural example with an actual native arithmetic
test of the proposed gluing sign. It does not evaluate an actual critical
vector or establish failure of every possible quantitative gluing theorem.

## Definitions before use and inherited native attachment

Use real smooth localization functions chi_j, with

    sum_j chi_j(x)^2=1 on the support of h,

and each chi_j h supported in an interval of radius at most a0. There are
finitely many pieces on each fixed compact support. Translate each piece to
the anchor interval. The inherited full native form is stationary under
simultaneous physical translation: the Fourier multiplier and prime shifts
are stationary, and the two cross-paired pole factors cancel their translation
weights. Thus the anchor certificate applies to each translated piece.

Set

    Delta_chi(x,y)=1-sum_j chi_j(x)chi_j(y)
                  = (1/2)sum_j(chi_j(x)-chi_j(y))^2.

This nonnegative geometric factor is not a source critical defect.

The exact native mixed formula is inherited from the pinned CC27 report

    notes/REFLECTED_PACKET_BRIDGE_108_NATIVE_FLUX_CC27_20261008.md,
    blob e9a44661f94ee6750fc5ad1fbf7dc719fa3ba482,

read at CC119 5df347d3808ac3282864a657b7380e0f54bf4daa.
Its off-diagonal continuous kernel is

    K_cont(d)=2cosh(d/2)-j(|d|),
    j(r)=exp(-r/2)/(1-exp(-2r)), r>0,

and the prime atoms are -c_n at +/-log n, c_n=Lambda(n)/sqrt(n).
The formula includes all active prime powers, both shift orientations and
both signed pole moments.

## Complete signed localization identity

For smooth compact h,

    Q(h)=sum_j Q(chi_j h)+E_chi(h),                    (1)

where

    E_cont =
      integral integral conjugate(h(x))h(y)
          K_cont(x-y)Delta_chi(x,y) dx dy,

    E_prime =
      -sum_n c_n integral conjugate(h(x))
          [h(x+log n)Delta_chi(x,x+log n)
           +h(x-log n)Delta_chi(x,x-log n)] dx,

    E_chi=E_cont+E_prime.                             (2)

Take the real part where appropriate; the paired terms make the form real.
No prime or pole sign is replaced by an unsigned positive term.

The archimedean local renormalization cancels because sum chi_j^2=1.
Near the diagonal j(r)=O(1/r), while the smooth localization factor is
O(r^2). Consequently the remainder in (2) is integrable there. One may
derive it with a positive separation cutoff, cancel the local terms, and
remove the cutoff by this bound. This is an analytic localization identity
on smooth tests, not a newly proved rough-domain extension or Lean theorem.

The translated anchor gives

    sum_j Q(chi_j h)>=eta sum_j ||chi_j h||_2^2
                      =eta||h||_2^2,
    eta=1/10^37.                                     (3)

A valid global gluing rule must additionally lower-bound E_chi relative
to these complete local energies or otherwise pay the negative covariance.
The geometric nonnegativity of Delta_chi supplies no sign for E_chi.

## An actual prime2 loss with the continuous terms paid

Choose a nonnegative even smooth bump phi, supported in (-epsilon,epsilon)
and normalized in physical L2, with epsilon=1/1000. Set

    h_left(x)=phi(x+log2/2),
    h_right(x)=phi(x-log2/2),
    h=h_left+h_right.

Both packets lie strictly inside (-a0,a0), with disjoint supports.
Choose smooth localized pieces whose localization vectors are (1,0) on
the left packet and (0,1) on the right packet. The transitions lie in
the gap where h=0; localized products are exactly the two packets.
Thus Delta_chi=1 on cross pairs and zero on same-packet pairs, so

    E_chi(h)=2 Q(h_left,h_right).                     (4)

The prime2 contribution to the mixed pairing is EXACTLY

    -log2/sqrt2.

The other shift orientation in this mixed pairing has no overlap.
All other active prime powers have displacements at least log3>1, whereas
the packet separation is between .6 and .7 with a .002 tolerance.
Their overlaps vanish. Both orientations remain in the original form;
none is silently discarded.

Every cross distance lies between 1/2 and 1. For that entire range,

    2cosh(d/2)<3,
    j(d)<1/(1-exp(-1))<2,
    |K_cont(d)|<5.

Physical Cauchy--Schwarz gives ||phi||_1^2<=2epsilon. Therefore the
absolute continuous mixed pairing is at most 10epsilon. This pays the
ENTIRE archimedean and pole continuous interaction, not only its tail.

The fresh rational enclosures log2>3/5 and sqrt2<3/2 yield
log2/sqrt2>2/5. Hence

    E_chi(h)
      < -2*(2/5)+20epsilon
      = -39/50.                                     (5)

The physical mass of h is exactly 2. The magnitude of this certified
localization loss exceeds the available anchor-only margin 2eta by an
enormous factor. Bounding (1) using just (3) and an unsigned allowance
for the error cannot certify the whole form.

The individual local energies can be much larger than their common guard,
and the known anchor already certifies Q(h)>0. Formula (5) disproves the
nonnegative-correction premise; it does not disprove a sharper estimate
relative to the ACTUAL local energies. These are smooth noncritical tests.

## Long prime jumps survive every anchor-width localization

If every chi_j has support diameter at most 2a0, then for log n>2a0
no piece can contain both x and x+log n. Hence

    sum_j chi_j(x)chi_j(x+log n)=0,
    Delta_chi(x,x+log n)=1.

Every such prime-power interaction is entirely in the localization correction.
It is not controlled by a local anchor certificate merely by translating it.

Fresh rational exponential bounds give

    exp(53/25)<9<exp(11/5).

Thus log9>2a0 and prime power9 becomes active by cap 11/10.
Its coefficient is Lambda(9)/sqrt9=log3/3, not log9/3.
Two narrow nonnegative packets separated by log9 have exact prime9
cross contribution -2log3/3 to the diagonal form. Their continuous and
pole terms must still be retained before discussing the total sign.

This identifies a concrete mixed obligation for larger caps; it does not
replace old-active-prime forcing by a new-prime-only model. Prime2 already
causes (5) inside the anchor.

## Exit condition for this candidate

One possible sufficient quantitative gluing statement would be

    E_chi(h)>=-theta_B sum_j Q(chi_j h),
    theta_B<1,

for a lawful anchor-width partition and every supported h on each finite cap,
with the complete signed kernel and all long jumps included. It would give
Q(h)>0. No such inequality is proved here. It is a separate substantial
arithmetic estimate, not a consequence of localized positivity.

For the direct endpoint route, one can instead target the signed localization
correction restricted to genuine near-null vectors and prove the decay required
by RC5. The present tests do not constrain those vectors. Merely dropping
long jumps, using Delta_chi>=0 as a sign, or replacing the local energies
by their tiny common guard fails.

## Fresh validation and standing

scripts/validate_rpb108_rc7_localization_budget.py passes 23 new rational
checks: logarithm/exponential and square-root bounds, all packet support
separations, the continuous-kernel allowance, the -39/50 correction upper,
prime9 activation, and signed partition identities. The smooth-packet and
localization derivations are analytic arguments above, not proved by a
count of samples. No actual critical mode is evaluated.

Whole original positivity at 1.06 and RC5's canonical guard remain intact.
No negative original vector, arithmetic outward-decay estimate, new positive
aperture, RH/F4 theorem or Lean closure is claimed. Other refs and historical
files are untouched.
