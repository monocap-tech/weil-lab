# CC95 — retained inverse-response rank budget

Definitions are additive; the original form/domain attachments and floor A>=kappa I, kappa=207/1000, remain hypotheses inherited from CC91–CC94.

**Full scalar-floor matrix.** For the eventual combined 56-column lifted family B=[V,W] per parity, define Q=B-star L_original B, R=P_F L_original B, Gamma=R-star R and S0=Q-Gamma/kappa. V is the current three-column NF37 packet and W is CC94's remaining 53-column lifted frame. S0 is a sufficient floor matrix; negative S0 does not imply a negative original-form vector.

**Current high response.** Let H be the existing eight even or seven odd paid high columns. Let QH=H-star A H, GH=(AH)-star AH, N=GH/kappa-QH, and D=R-star (A-kappa I)H. With the inherited attachments and certified N>0, the common inverse-response lower matrix has the form S=S0+kappa^-2 D N^-1 D-star. The packet rows of D are already certified; the remaining rows and full S0 are not. This expression describes a prospective completion using the same paid high columns, not an already computed full certificate.

**Correction kernel.** Delta=kappa^-2 D N^-1 D-star is positive semidefinite, rank at most n=8 or 7, and ker(Delta)=ker(D-star). On that kernel S=S0 exactly. Its dimension is at least 56-n: 48 even, 49 odd. S>0 requires S0 strictly positive there. Rank-n positive correction can remove at most n negative directions of S0.

**Additional response profiles.** The certified 3-by-n packet response Dv has rank three. For the eventual remaining rows Dw, consider Dw modulo the row span of Dv. The quotient response rank is at most n-3: five even, four odd. For a remaining coordinate vector c with Dw-star c in range(Dv-star), there is a unique packet coefficient a such that Dv-star a+Dw-star c=0. Thus (a,c) belongs to the correction kernel. At least 48/49 remaining coordinate dimensions admit such cancellation. These are mixed packet/remaining vectors, not necessarily the pure CC94 remaining vectors. Quotient response rank is not a post-Schur negative-index repair budget.

**Negative-index budget.** The actual current packet scalar-floor block has inertia (2 positive,1 negative,0 zero) in each parity. Therefore any full S0 has at least one negative direction per parity. If its negative index exceeds eight even or seven odd, the current response correction cannot make S positive. Its additional negative-index allowance beyond that already witnessed direction is at most seven even/six odd. The full negative index remains unknown.

Kernel positivity is necessary but insufficient: signed range and mixed terms still determine the final sign. These algebraic constraints are not a nonimplication from all original Weil identities, and they do not prove that the present high columns fail on the actual remaining complement.
