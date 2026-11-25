# RPB108 LF85 — full-root validation and domain boundary

## Verified checkpoint

LF84 commit `42c6a56d50d9b40e757b8214dec07ddd162aad10` passed Lean workflow run `38196728241`, job `114643485286`:

- Check canonical certificate transport: success.
- Check complete root library: success.
- Reject unfinished trusted declarations: success.
- Overall job conclusion: success.

This supersedes LF66 as the latest confirmed full-root checkpoint on formalization/rpb108-certificate-transport. Mathlib remains pinned to 5ed2965256430c3649e86755f9576b54eca72435; the PR base remains research/rpb108-route-consolidation at 261e907ff6b8aed70a1319a86717286406ef7c4f. No branch retargeting or force update.

## Verified analytic coverage

The cumulative compiled chain now includes actual finite full-line time-action L1/L2 membership; Fourier transport and spectral cutoff convergence; ordinary/L2 Fourier representative attachment; actual physical-vector and pairing convergence; supported-test agreement with the endpoint candidate; explicit cap-compressed L2 vector equality; and almost-everywhere equality inside the cap. These source comparisons retain an explicit full weighted-product L2 domain premise.

A proved frequency-moment criterion supplies that domain premise from G and ξG in L2. The Schwartz trial theorem derives the criterion rather than assuming weighted-product membership. Cap-supported Schwartz trials equal their actual zero extensions, and their compression theorem consumes the derived domain witness. Cap bounds and Lipschitz constants remain explicit inputs to endpoint construction.

## Remaining boundary

| Trial or interface | Domain coverage |
| --- | --- |
| General bounded integrable trial with full weighted-product L2 premise | Conditional source attachment and convergence checked |
| Physical Schwartz trial | Weighted Fourier-domain membership derived and checked |
| Cap-supported physical Schwartz trial | Actual zero-extension domain and endpoint compression derived and checked |
| Arbitrary cap-Lipschitz trial with endpoint jumps | Full weighted-product domain membership still open |
| Complete canonical form domain | Form energy does not supply the stronger multiplier-domain premise |

The endpoint vector is a cap compression. The full-line spectral source retains exterior action; the proof does not set it to zero. The supported Schwartz result does not cover zero extensions with jumps merely by density or by form-energy membership.

## Next proof obligation

Derive a weighted L2 tail criterion compatible with 1/|ξ| Fourier decay, then establish that decay for the intended cap-Lipschitz or bounded-variation zero extensions, including boundary contributions. This should supply the logarithmic multiplier-domain premise without requiring the stronger first-frequency-moment condition. Source attachment can then consume the existing compiled interface.

LF85 is a documentation-only validation record; it introduces no Lean declarations or definitions and makes no aperture positivity, F4 closure or RH claim. The externally checked full-root SHA remains the LF84 SHA above.
