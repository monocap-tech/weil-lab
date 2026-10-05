# RPB108: rational certificate for one actual finite restriction

## Terminology and scope

A **rational enclosure** is an interval with rational endpoints proved to contain the stated real quantity. A **positive pivot certificate** is interval Schur elimination with every pivot lower endpoint strictly positive. It certifies positive definiteness of every symmetric matrix in the entry enclosures. It does not give an eigenvalue lower bound equal to the smallest pivot.

This chunk uses the actual native physical matrix identity established in `REFLECTED_PACKET_BRIDGE_108_EXACT_PHYSICAL_MATRIX_FORMULA_20261005.md`. It certifies the eight-dimensional restriction at aperture a=1/4. It assumes neither whole-domain positivity nor retained membership. No spectral operator-domain assertion is needed: the trial vectors belong to the logarithmic form carrier.

## Finite theorem

Let E be the complex span of P_n(x/a) times the indicator of [-a,a], for n=0,...,7 and a=1/4. The actual native Weil form Q is strictly positive on E minus zero.

The basis is unnormalized. Positive definiteness is preserved by the positive diagonal change to the physical orthonormal basis used in the earlier pilot. Raw divisor multiplicities in the actual form are unchanged.

## Exact entry construction

Write C_ij(t/2)=sum c_k t^k. The symmetrized physical correlation polynomial is constructed by exact rational integration of P_i(r)P_j(r-u) over u-1 <= r <= 1, multiplied by a and symmetrized; here u=2t. Its constant is delta_ij=2a/(2i+1) if i=j and zero otherwise. Opposite-parity entries vanish exactly.

No prime contributes: log 2 > 1/2 = 2a. This inequality is also checked with the rational logarithm enclosure. Each entry is

Q_ij = [-gamma-log pi-log(1-exp(-1))] delta_ij
       + integral from 0 to 1 of A_ij(t) B(t) dt
       + [(-1)^i+(-1)^j] M_i M_j,

where A_ij(t)=[exp(-t)delta_ij-exp(-t/4)C_ij(t/2)]/t,
B(t)=t/(1-exp(-t)), and M_i=integral from -a to a of P_i(x/a)exp(x/2) dx. The value at t=0 is removable. The pole term uses these same trial vectors.

## Rigorous error bounds

Use degree N=60 exponential Taylor polynomials and K=24 Bernoulli pairs for

B_K(t)=1+t/2+sum from k=1 to K of B_(2k)t^(2k)/(2k)!.

The Bernoulli identity |B_(2k)|/(2k)! = 2 zeta(2k)/(2pi)^(2k), together with zeta(2k)<2 and pi>3, gives, on [0,1],

|B-B_K| <= 4*6^(-2K-2)/(1-1/36), and |B_K|<2.

Put Csum=sum |c_k|. The exponential remainder, after dividing by t, obeys

|A-A_N| <= 3/(N+1)! * [delta_ij+Csum/4^(N+1)].

Indeed exp Taylor remainders are bounded by exp(1)t^(N+1)/(N+1)! and exp(1)<3. The exact cancellation at zero precedes division; the product with C is retained in full. Also

|A| <= (3/4)delta_ij + sum from k=1 onward of |c_k|.

Thus the integral enclosure radius is

2*3/(N+1)!*[delta_ij+Csum/4^(N+1)]
 + [(3/4)delta_ij+sum_(k>=1)|c_k|]*4*6^(-2K-2)/(1-1/36).

The polynomial integral itself is rational. The moment enclosure radius is
4a*sum |coefficients(P_i)| / [8^(N+1)(N+1)!], using exp(1/8)<2 and |r|<=1.

Constants are enclosed without floating arithmetic. Machin's identity pi=16 atan(1/5)-4 atan(1/239) uses alternating rational series with next-term bounds. Logarithms use the absolutely convergent atanh series after reduction to [1,2], with geometric tail bounds. Gamma uses the harmonic sum at n=100 and the six-term Euler--Maclaurin expansion; its remainder magnitude is at most |B_14|/(14*100^14). The latter bound follows from the signed remainder for the harmonic expansion, equivalently the alternating expansion of the positive Binet integral. Every interval operation rounds outward to the rational grid of step 10^(-50).

## Certificate and validation

`scripts/certify_native_legendre_small_window.py` runs with Python's standard library only. The eight exact rational pivot lower endpoints are recorded in `notes/data/RPB108_RATIONAL_FINITE_CERTIFICATE_20261005.json`. All are positive; their decimal displays are approximately

0.08032516, 0.10074755, 0.02659132, 0.08142060,
0.08552182, 0.08078255, 0.07536007, 0.07057590.

Inductively, a positive pivot and the enclosed Schur complement prove positive definiteness, completing the finite theorem. Maximum entry enclosure width is less than 9*10^(-30), checked rationally. Floating displays are not certificate inputs. A deliberately negative first diagonal is rejected. After diagonal normalization, the midpoint matrix agrees with the earlier physical pilot within 10^(-11); that comparison is a diagnostic, not part of the proof.

## Remaining interface

This theorem establishes the WD-T10 norm inequality only on this finite trial space, provided the previously established identity Q(f)=||S_+f||^2-||S_Bf||^2 is applied to the same f. It does not establish the inequality on D. It supplies no actual negative witness, exact null, signed endpoint-null Gaussian upper estimate, or exclusion of a finite positivity endpoint. The positive carrier and observation quotient remain distinct constructions until their stated range identification is justified; this computation introduces neither a new carrier nor a representation wrapper. FULL TRANSPORT CLOSED remains open. F4 entry cannot be inferred from a finite restriction certificate.

Lean source and the previous certified Lean checkpoint are unchanged; this is an analytic certificate with exact rational execution, not a new Lean proof.
