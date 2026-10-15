# RC311 — all-degree endpoint/diagonal contact identity on the canonical polynomial core

**Parent:** RC310, merged at \`55cb95ab5b3673129897870bcfe41b9c3e6ef998\`.  
**Claim scope:** all polynomial input degrees, both reflection parities, for the original logarithmic endpoint **suboperator**.  
**Status:** the independent frequency-domain identification of the *entire* canonical Weil form, positivity, signed inverse, Schur gate, Stage I, F4 and RH remain **OPEN**.

## 1. New mathematical result — the endpoint formula is not just a fitted matrix

RC309 bounded the infinite Legendre endpoint matrix with coefficients

\[
 E_{nd} =
 \begin{cases}
  \dfrac{2n+1}{|n-d|(n+d+1)},&
       n\ne d,\;n\equiv d \pmod 2,\\
  2(H_{2n}-H_n)+\dfrac1{2n+1},&n=d,\\
  0,&n\not\equiv d\pmod 2.
 \end{cases}
\]

RC311 establishes its identity, **for every finite Legendre polynomial input** and both parities, with the physical endpoint multiplier

\[
 W_B(x)=\log2-\tfrac12\log(1-(x/B)^2),
 \qquad -B<x<B.
\]

Namely, the exact Legendre expansion of \(W_BP_d\) has coefficient \(E_{nd}\) on \(P_n\), with the physical mass \(m_n=2B/(2n+1)\). Multiplication by the logarithmic endpoint is a densely defined form/source operation; this does not assert that \(W_B\) is a bounded ordinary physical \(L^2\) multiplier.

The proof does **not** extrapolate finitely many matrix entries. It uses the following identities valid for *all* integer degrees.

### Proof A: Legendre Sturm–Liouville determines the entire first column

Write \(t=x/B\). With \(W(t)=\log2-\frac12\log(1-t^2)\),

\[
 (1-t^2)W'(t)=t.
\]

The Legendre equation, integration by parts with vanishing logarithmic boundary product \((1-t^2)W(t)P_n'(t)\), \(P_n(\pm1)=(\pm1)^n\), and \(\int_{-1}^1P_n=0\) for \(n>0\), give

\[
 \int_{-1}^1W(t)P_n(t)\,dt
 =
 \begin{cases}
  2,&n=0,\\
  2/[n(n+1)],&n>0\text{ even},\\
  0,&n\text{ odd}.
 \end{cases}
\]

Thus the entire first Legendre column is exactly \(E_{n0}\).

### Proof B: algebraic commutation with coordinate multiplication

Let \(X\) denote multiplication by \(t\). Bonnet's recurrence is

\[
 tP_d=\frac{d+1}{2d+1}P_{d+1}
       +\frac d{2d+1}P_{d-1}.
\]

RC311 proves the all-index identity \(EX=XE\), **symbolically**, not by numerical sampling. In the separated case \(n>d+1\), the commutator is a rational function of symbolic \(n,d\) and reduces identically to zero. In the adjacent case \(n=d+1\), one needs precisely the diagonal harmonic recurrence

\[
 E_{d+1,d+1}-E_{dd}
 =
 \frac1{2d+1}+\frac1{2d+3}-\frac1{d+1}.
\]

The corresponding rational difference again vanishes identically. Opposite-parity cases and the diagonal case are trivial. The lower triangular entries follow by weighted symmetry \(m_nE_{nd}=m_dE_{dn}\), and \(X\) is symmetric in the same physical mass.

Since every Legendre \(P_d\) is a polynomial in \(X\) applied to \(P_0=1\),

\[
 E P_d=P_d(X)EP_0=P_d(X)WP_0=WP_d.
\]

This is the key **all-degree** result. The proof works on the full dense polynomial core, not merely on RC310's selected \(P_2,\dots,P_5\).

### Proof C: independent exact logarithmic moments

A second analytic integration identity gives

\[
 \int_{-1}^1t^{2j}W(t)\,dt
 =\frac{2H_{2j+2}-H_{j+1}}{2j+1};
 \qquad
 \int_{-1}^1t^{2j+1}W(t)\,dt=0.
\]

One obtains it by differentiating the beta integral (or equivalent elementary integration and harmonic recurrence), with the \(\log2\) terms cancelling exactly. RC311 uses these rational moments and monomial expansions of *both* Legendre factors to check an independent \(13\times13\) pairing table against the analytic all-degree \(E_{nd}\) formula. This numerical-domain regression is additional evidence; the universal proof is A+B.

## 2. Exact diagonal/contact bookkeeping

The actual original physical endpoint in RC231 is

\[
 h(t)=-\tfrac12\log(1-t^2)=W(t)-\log2.
\]

In RC46 the archimedean decomposition is

\[
 L_{\mathrm{arch}}=J+W+c_R I-K_{\mathrm{reg}},
\]

where \(J P_n=H_nP_n\), \(c_R=-\gamma-\log(2\pi R)\), and \(R=2B\).

The physical reference metric of RC121/RC231 is \(D_s=J+sI\), with

\[
 s=c_R+\log2+r,\qquad r=789/125.
\]

Consequently, **identically**

\[
 D_s+W-(\log2+r)I
 =J+W+c_R I,
\]

and also

\[
 D_s+h-rI=J+W+c_R I.
\]

The scalar \(\log2\) is therefore included **once and only once**. If a proposed formula used \(E-rI\) in place of \(E-(r+\log2)I\), it would introduce a nonzero erroneous contact shift of \(\log2 I\). The validator proves that mismatch symbolically and keeps the original rank-317 augmentation separate.

Combining the all-degree endpoint result with RC309's weighted-Schur bound identifies the bounded \(D^{-1}E\) extension uniquely with the endpoint form's \(D\)-Riesz extension **under the inherited actual metric form identification**. The ordinary multiplication \(W\) need not be bounded on \(L^2\).

## 3. What this does and does not certify

New and established in RC311:

- All-input-degree endpoint identity \(E_{nd}=[P_n](W_BP_d)\).
- Both parity sectors, including the diagonal harmonic coefficients.
- Exact \(\log2\) contact-term accounting and the \(c_R\), \(D_s\) scalar shift.
- Uniqueness of the bounded endpoint \(D\)-Riesz continuation from the dense polynomial core, conditional on RC309's bound and inherited metric.
- Independent \(13^2=169\) exact rational physical logarithmic-integral checks.

Still imported from earlier research rather than independently redemonstrated here:

- RC46's digamma/Plancherel and zero-extension derivation of the *whole* archimedean frequency-to-physical form.
- RC231's cancellation of the supported canonical Poisson remainder.
- The original physical seven-prime and signed-pole distributional source identities.
- Identification of the complete augmented model with the canonical Weil form on its correct common domain.

Those obligations cannot be replaced by checking more polynomial examples. Even after the full canonical identification, **boundedness alone is not positivity**; RC292's spectral lower bound, genuine signed inverse response and the remaining 314-dimensional Schur gate will still need separate proofs.

## RC312

Derive the complete RC46 digamma/Plancherel frequency-to-supported-form identity independently, including the \(r=0\) singular renormalization, boundary/contact terms and exact \(c_R\). Then verify RC231's cancellation of the bounded supported Poisson remainder at the form level, not merely at the matrix level, and reassemble the original canonical source. Only a fully audited identity permits canonical transfer.

## Reproduction

\`\`\`bash
python scripts/validate_rpb108_rc311_endpoint_core_identity.py --output certificates/rpb108_rc311_endpoint_core_identity.json
python scripts/validate_rpb108_rc311_endpoint_core_identity.py --output certificates/rpb108_rc311_endpoint_core_identity.json --replay
\`\`\`

The symbolic rational reductions and finite integral checks are computationally reproducible. The Sturm–Liouville and beta-integral steps are mathematical arguments supplied in this note, not Lean-formalized or independently peer-reviewed.
