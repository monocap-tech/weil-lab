# RPB108: prime-5 activation and actual 84-moment complement

Base: 8ef78e239b8eeae707865f38360cb638f5c0ab9d.
Definitions: docs/TERMINOLOGY_RPB108_PRIME5_84_081.md.

## Result and next obligation

At a=81/100, the actual supported form-domain complement orthogonal to physical Legendre degrees 0..83 has physical coercivity at least 51/100 and logarithmic coercivity at least 9/100. The bounds hold uniformly on [1/2,81/100]. This includes the newly active prime-5 term. The matching 84-coordinate native restriction, actual sources, complete residual Gram and corrected sign remain to be certified. The whole-domain positivity frontier remains a=4/5; the 84-moment complement cannot be paired with the old 52-coordinate finite restriction to infer positivity.

Dimension 84 is a sufficient choice for this complement calculation, not a claimed minimal dimension. No larger finite restriction or whole-domain calculation is reported as complete.

## Prime-5 threshold and actual panels

Rational enclosures prove 8/5<log(5)<81/50<log(7). Thus a=4/5 has no prime-5 overlap, while a=81/100 does. At the latter aperture the active prime powers are exactly 2,3,4,5. The coefficient for prime 5 is Lambda(5)=log(5), giving source amplitude log(5)/sqrt(5) and native correlation coefficient 2log(5)/sqrt(5). Prime 4 still uses Lambda(4)=log(2).

With ell_n=log(n)/(2a), the exact nine-panel geometry is:

| t interval | Active source translations |
| --- | --- |
| (0,1-ell_5) | +2,+3,+4,+5 |
| (1-ell_5,1-ell_4) | +2,+3,+4 |
| (1-ell_4,1-ell_3) | +2,+3 |
| (1-ell_3,ell_2) | +2 |
| (ell_2,1-ell_2) | +2,-2 |
| (1-ell_2,ell_3) | -2 |
| (ell_3,ell_4) | -2,-3 |
| (ell_4,ell_5) | -2,-3,-4 |
| (ell_5,1) | -2,-3,-4,-5 |

All endpoint ordering and interior translation controls pass. On the normalized constant coordinate, omitting prime 5 changes the native/source pairing by 2log(5)/sqrt(5)(1-log(5)/(2a)), rigorously above 0.009385425575221. Replacing Lambda(5) by log(2) changes it by more than 0.005343342792431. The omission, wrong-coefficient and edge-panel controls are rejected. This certifies actual activation geometry, not enclosures of the complete new sources.

## Joint prime-3/prime-5 operator bound

Put s3=log(3), s5=log(5), epsilon=2a-s5. Rational intervals prove 0<epsilon<min(s5-s3,2s3-s5), as well as 2a<2s3. Every prime-5 edge joins x and x+s5 for x in [0,epsilon]. The prime-3 edges at its endpoints add x+s3 and x+s5-s3. These four disjoint strips give the chain, in vertex order:

x+s3, x, x+s5, x+s5-s3.

The successive edge amplitudes are A3,A5,A3. Neither leaf admits another prime-3 or prime-5 edge: the certified gap inequalities put all such translates outside the support. All prime-5 edges have been included; the remaining components contain only single prime-3 edges or isolated vertices. Thus the operator decomposes into these four-point fibres and the remaining two-point fibres, without assuming rational dependence of log(3) and log(5).

The four-point weighted adjacency matrix has largest absolute eigenvalue J35=(A5+sqrt(A5^2+4A3^2))/2. Its positive symmetric eigenvector has end entries A3 and middle entries J35. The bipartite spectrum is symmetric. The certificate rounds J35 upward to 1.089148588713 and independently verifies positive exact rational LDL pivots for both J35 I+B and J35 I-B using outward amplitude bounds. A trial vector evaluated with lower actual amplitude bounds rejects a norm bound smaller by 10^-6. Entrywise domination by the nonnegative outward matrix bounds the actual chain norm. Since A3<=J35, the other components obey the same bound.

Combining this bound with the existing joint prime-2/4 norm J24 gives total prime loss at most J24+J35. Before prime-5 activation, the prime-3 operator alone is bounded by A3<=J35, so the same loss is valid uniformly on the aperture interval.

## Actual complement certificate

Retain the actual quarter-line archimedean high estimate m_0(t)>=log|t|-7/(216t^2), |t|>=1, and global floor m_0>-27/5. These are the previously established convergent Euler--Maclaurin and quarter-line minimum bounds. The existing exact 84-moment estimate rho84(T) and absolute pole bound p84 yield

c(T)-(27/5+c(T))rho84(T)-p84-J24-J35,

where c(T)=log(T)-7/(216T^2). At T=243/20 this exceeds 0.512861236961267 and hence 51/100. The inverse complement energy factor is 100/51. Independent logarithmic cutoff 19/2 yields a strictly positive high-symbol gap and logarithmic coercivity above 9/100. Monotonicity of the moment/pole bounds with support aperture and the uniform translation bounds establish the stated aperture interval.

## Validation and standing

Both certificates reproduce byte for byte. The independent exact four-by-four norm checks pass, and the too-small norm control fails on a verified actual trial vector. All nine activation panels and coefficient controls pass. No native or source constructor is expanded by this entry; previous matrix/source certificates are unchanged.

The next load-bearing task is the matching 84-coordinate native matrix and actual source construction at a=81/100, followed by the entire residual Gram and corrected sign. Finite restriction positivity alone will not close the whole domain. Lean, axioms and CI remain unchanged. Global endpoint exclusion, all-window domination, retained witness/null transport, F4 and FULL TRANSPORT CLOSED remain open.
