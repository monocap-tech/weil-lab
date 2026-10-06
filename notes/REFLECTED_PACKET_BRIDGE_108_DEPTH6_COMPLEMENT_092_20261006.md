# RPB-108: fresh depth-six complement at aperture 23/25

The fixed aperture is a=23/25. The complete complement is the physical
L2-orthogonal complement of the normalized Legendre vectors of degrees
0 through 83 on [-a,a]. Its vectors have degrees at least 84. The symbol
c denotes a lower bound for the actual native quadratic form on that
complete complement, measured in squared physical L2 norm. The cutoff
T denotes the physical Fourier frequency used to split the mass bound.
The inverse factor beta is 1/c; it multiplies the residual source Gram
in the subsequent finite Schur estimate.

At T=137/10, the sixth finite Bessel iteration certifies
c=626973/1000000 and beta=1000000/626973. The unrounded lower bound is
approximately 0.6269739237255396; the bounded low-frequency mass is
approximately 0.001663181945827926. This improves the retained depth-three
bound 623/1000 at the same aperture. The complete logarithmic complement
bound remains 9/100. These are complement estimates only.

The fresh calculation repeats byte for byte. The independent validator
checks 21 polynomial recurrence comparisons, three quartic specializations,
all 48 integrated degree contributions and the complete infinite tail,
positive integration rates and Bessel positive-region membership, and
recomputes the archimedean/prime/pole balance at 100 digits. Four independent
finite Bessel-series controls verify the damping inequalities and reject
excessive exponents; four invalid iteration domains are rejected.

New 23/25 native and source constructors retain 84 physical basis vectors,
prime powers 2,3,4,5 (with Lambda(4)=log(2)), the actual nine-panel translation
order, and all earlier supported apertures. Their fresh error constants are
40 for exp(4a), 23/5 for the native kernel ceiling, and 9/4 for the source
alternating kernel ceiling. The obsolete exponential ceiling 39 fails at
this aperture. Exact support-order and alternating Bernoulli checks pass.
The historical quarter native certificate checksum is unchanged, and six
invalid constructor combinations are rejected.

The new full Gram constructor requires matching 23/25 native and source
certificates and binds its checkpoints to their hashes, its own constructor,
geometry, Hankel arithmetic and checkpoint codec. A 91/100 checkpoint cannot
be reused. It uses the established outward pairing-enclosure guard and
retains all mixed terms and the source-map approximation error.

The fresh native and source jobs are started; their completed certificates,
independent repetition, complete nine-panel Gram, and corrected Schur sign
remain the next frontier. This checkpoint makes no claim of whole-domain
positivity at 23/25. The certified whole-domain aperture remains 91/100.
Historical packet/source attachment, global endpoint exclusion, F-4 and
full transport remain open. Lean and workflows are unchanged.

## Certificate custody

- `notes/data/RPB108_PRIME5_DEPTH6_COMPLEMENT84_092_CERTIFICATE_20261006.json`
- `notes/data/RPB108_PRIME5_DEPTH6_COMPLEMENT_092_VALIDATION_20261006.json`
- `notes/data/RPB108_MATCHED_092_CONSTANTS_VALIDATION_20261006.json`
- `notes/data/RPB108_MATCHED_092_GUARDS_VALIDATION_20261006.json`

The complement SHA-256 is
`fb5455dc2d1f6bc271edfb37e88018a96679440a79ba479852b569d30d730e47`.
The independent recurrence proof follows the retained finite-induction
argument in `REFLECTED_PACKET_BRIDGE_108_ITERATED_DAMPING_20261006.md`;
it requires no infinite Bessel-series positivity assertion.
