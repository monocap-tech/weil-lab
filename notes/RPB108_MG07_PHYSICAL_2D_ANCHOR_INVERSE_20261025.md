# Complete-form physical anchor inverse bound

Let f=u+(4096/3013)s and g=u-s be the original physical basis in the
repaired signed 2D certificate. Let H be the 2x2 matrix of the COMPLETE
original signed form Q on this basis. This is the inverse of a finite
compression, not a compression of the global inverse.

## Exact bound from accepted GitHub evidence

Run 40260136876, source 8844685d3e72a3d38f943b084b6e5bc70ef3d09c,
artifact 12623752657 provides diagonal lower bounds a,d and the retained
cross absolute bound b, with the positive high-frequency form discarded
as PSD. Exact arithmetic gives

    a > 1/8000, d > 1/24,
    (a-1/8000)(d-1/24)-b^2 > 0.

The last reserve is approximately 3.5487117381478844e-8.
For any coefficient vector z, the retained form minus
(|z0|^2/8000+|z1|^2/24) is nonnegative, by the 2x2 determinant test.
Adding back the discarded positive high-frequency PSD form preserves this
bound. Thus

    H >= diag(1/8000,1/24),
    H^-1 <= diag(8000,24).

The source artifact is checked by successful run/source identity, archive
SHA-256 and exact JSON SHA-256. No frequency quadrature is repeated.

## Use in the remaining physical signed Schur

For r in the original form domain and L2-orthogonal to span(f,g), use
the COMPLETE original mixed functionals

    b(r) = (Q(f,r),Q(g,r)).

Completion of the finite square gives

    inf_(alpha,beta) Q(alpha f+beta g+r)
      = Q(r)-b(r)^* H^-1 b(r)
      >= Q(r)-8000|Q(f,r)|^2-24|Q(g,r)|^2.

Equivalently for the full mixed map C from the physical remainder,
C^* H^-1 C <= C^* diag(8000,24) C. This is a concrete bound on the
anchor inverse term in the complete physical Schur. It does not evaluate C
or prove positivity of the resulting remainder.

The previous isotropic inverse bound H^-1<=7100 I remains valid. The
new bound is a tradeoff: its first coefficient is 8000 instead of 7100,
while its second is 24 instead of 7100 (a factor 295.83 reduction).
Either valid bound can be used; the anisotropic penalty is smaller when
900|Q(f,r)|^2 < 7076|Q(g,r)|^2. No universal improvement is claimed.

The retained low-frequency cross estimate must NEVER replace the complete
mixed functionals Q(f,r),Q(g,r): the discarded positive high-frequency form
can have large mixed entries. Exact regression includes an arbitrary PSD
high-frequency model whose cross entries exceed the retained bound.

## Coordinate custody and unresolved obligations

These are PHYSICAL f,g coordinates. They are not SM34's Astar^-1 E0
energy-dual source coordinates. Neither this 2D result nor its inverse cap
can be inserted as a principal SM34 block without proving the coordinate
and operator transport. The exact physical completion-of-square argument
above is a separate valid use of the certificate.

The workflow also checks an adversarial algebra model: positive anchor and
positive diagonal remainder with an actual mixed term can have negative
Schur. Therefore this result does not imply positivity of any remaining
468 physical source directions or the infinite complement.

Inherited original Fourier, form-domain, support and pole assumptions
remain unchanged. Original complete mixed functionals, remaining signed
Schur, W-ODD-NEG, even/CC27, Weil and RH are OPEN.
