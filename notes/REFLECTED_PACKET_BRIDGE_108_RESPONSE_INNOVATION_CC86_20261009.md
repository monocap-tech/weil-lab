# CC86: conditional response innovation and finite-span stop rule

Parent: CC85 e00358705a56882ae3d223139da822969ecced33. Read-only Native Source: NF44 7bd6fbda5e156fbd009b6de0aeee6f41b1823c5c. No new producer packet is available. This result refines CC84's finite-span compression theorem into an exact selection and exhaustion rule.

## Paid finite-span setup

All formulas are real; transpose is denoted by *. Let A be the remaining high operator and Aj the NF44 six-source minorant. Assume the standing floor A >= (207/1000)I and the paid source/domain hypotheses supporting Aj. Set D=A-Aj >=0. For finite original high polynomials Y, put F=DY, G=Y*DY>0, B=G+F*Aj^-1F>0, and P=F*Aj^-1R. These are the complete signed quantities, not diagonal substitutes. Dependent defect columns must be removed before inversion.

Write the current retained lower certificate as K=[[E,r],[r*,c]], E>0 and s=c-r*E^-1r<0. Split P=(PE,p_last). Define M=B+PE E^-1PE*>0 and t=p_last-PE E^-1r. CC84 proves that the full batch condensed margin is s+theta, theta=t*M^-1t, and that a frozen paid combination with coefficients near M^-1t can attain a positive margin whenever theta>-s. This statement concerns the three retained coordinates in one parity.

## Exact conditional innovation

Let S be selected candidate indices, j a remaining candidate, H=M_SS, b=M_Sj, and u=t_S. Define

    delta = M_jj - b* H^-1 b > 0
    tau   = t_j - b* H^-1 u
    innovation(j | S) = tau^2 / delta.

For empty S the innovation is t_j^2/M_jj. Block inversion gives

    theta(S union {j}) = theta(S) + innovation(j | S).

Proof: eliminate the selected block in the quadratic t* M^-1 t. The remaining one-dimensional Schur block is delta and its transformed border is tau. Positivity of M makes delta positive. This is an identity, not a lower estimate. Repeating elimination telescopes to theta for the complete span in every order. Individual increments can depend on order; their total does not. No decreasing-increment claim is made.

Physical projection off the six NF44 polynomials remains necessary for the producer's custody, but it cannot replace this response conditioning. For example, M=[[2,1],[1,2]], t=(1,0) gives initial score 1/2 and a second innovation 1/6, even though the second raw response is zero. The full score is 2/3. Replacing M by its diagonal loses this response. The example is algebraic and does not claim that a particular original native polynomial realizes it.

## A reviewable scheduler and stop rule

1. Freeze a finite original polynomial candidate span and pay its full G, B, P and physical/domain errors. Physical normalization alone is insufficient.
2. Enclose M and t using the frozen NF44 K. Prove every denominator used in interval elimination positive. Maintain rigorous score bounds; unresolved signs require refinement.
3. Evaluate conditional innovations to prioritize candidates. Overlapping bounds do not certify which candidate is maximal; any fixed order remains valid. Do not sum unconditioned individual scores.
4. If a rigorous lower bound for the complete score exceeds an upper bound for -s, freeze a rational combination and replay the signed passing quadratic under the original source payments. A score crossing alone is not a native certificate.
5. If an upper score bound is at most a lower bound for -s, this entire paid candidate span is exhausted for this certificate. Equality cannot certify strict positivity. Change or enlarge the span, improve the minorant, or refine payments. This does not exclude positivity of the actual original form.

The span stop rule follows from CC84's maximization identity; the new innovation identity supplies a computation that accounts for correlations without double counting. This does not supply a rate or a universal sufficient number of source columns: for M=I and t=(0,...,0,2), every prefix before the last column scores zero, while the complete score is four. The delay is arbitrary. NF43/NF44 gains therefore cannot justify extrapolating termination or fixing a seventh-column success claim.

## Validation and frontier

The companion exact Fraction validator checks all six elimination orders for a correlated three-column metric, equality/strict crossing, a zero-raw-response positive innovation, and arbitrary-delay controls. It independently authenticates NF44's even and odd certificate hashes and recomputes their negative condensed intervals. It does not replay native integration, source production, or domain transport.

No paid candidate-span packet beyond NF44 is available, so no actual shell exhaustion or seventh source is certified here. The next producer packet can be checked against this criterion using NF44's updated witness and the full signed source metric. Both parity lower certificates remain indefinite. The standing floor and remaining-background transport are open attachments; the full simultaneous six-retained-direction sign, the other 106 retained directions, and collective coupling remain open. Highest certified whole aperture remains 21/20. No RH, F4, all-cap, Lean or whole-aperture closure is claimed.
