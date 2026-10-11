# RPB108 RC72 — fixed transfer allowance barrier and Young refinement

RC72 certifies a barrier for the source-residual estimate used in RC71: enlarging the nominal polynomial head cannot meet the inherited scalar source budget while paying the same full, unprojected physical source-transfer allowance. This is a restriction on an explicit class of upper estimates, not a lower bound on actual source leakage.

A finer exact rational Young-parameter search also improves the actual rank-38 residual upper factor for the existing 22 source inputs from 4323/512 to 4235/512, approximately 8.271484375. That is a further 8/393, approximately 2.0356%, tightening of the certified upper. The complete 38-input source map remains unevaluated.

## Defined estimate class

Write E_F for the physical transfer Gram upper from RC68. This encloses the error between the actual complete original physical source and the nominal source built from RC67's enriched 64-mode Riesz trials. It includes the correlated physical Riesz error, the complete parity operator norm, the nominal operator approximation error, and outward rounding.

The **fixed transfer allowance barrier** means the following. Consider upper matrices of the form

\[
B=\rho\big((1+t)W+(1+1/t)E_F\big)+D_{\mathrm{out}},
\quad W\succeq0,\quad D_{\mathrm{out}}\succeq0,\quad t>0,
\]

where rho=252/257, W is any certified nominal physical residual covariance upper, and D_out is a paid outward allowance. Separate positive parameters on the two parity blocks are permitted. Holding E_F fixed gives

\[
B\succeq\rho E_F.
\]

This remains true even if an enlarged head made W exactly zero. It therefore applies to any nominal head count within this estimate class. It does not apply to a method that directly bounds the projected transfer error, retains additional cancellation, changes the carrier norm, or replaces E_F with a sharper enclosure.

## Exact comparison witness

RC72 uses all 22 native coordinate inputs and all 22 exact physical Legendre inputs. The latter are represented by v=C^-1 e_n in the native Chebyshev coordinates. The strongest tested witness is the input with physical target P_20. Its exact physical squared norm is

\[
v^*P_{22}v=11/205.
\]

The certificate records its exact rational coefficients and its fixed allowance quadratic. Numerically,

\[
v^*E_Fv\approx0.0155396855297,\qquad
\frac{v^*E_Fv}{v^*P_{22}v}\approx0.289603230326.
\]

The actual canonical input Gram satisfies M_22 <= rho P_22. Hence, if one tries to prove B <= gamma M_22 using a majorant from this class, necessarily

\[
\gamma\ge\frac{v^*E_Fv}{v^*P_{22}v}.
\]

RC63's inherited scalar Schur source-budget ceiling is approximately 1.7084534755e-11. The witness exceeds this ceiling by approximately 16,951,192,085.9 times. The exact negative quadratic of gamma_ceiling rho P_22 - rho E_F is stored and independently replayed. Thus the comparison fails even against the certified upper bound for the unknown actual input Gram.

For this input alone, any replacement allowance in the same estimate class must be strictly below gamma_ceiling times 11/205, approximately 9.16731133e-13, to have a chance of meeting the strict budget. The present allowance would need a reduction by more than the factor above. This is a requirement on the allowance used by the method, not a proved lower bound or required reduction of the true Riesz error.

More than 99.9999% of this fixed allowance quadratic comes from the retained correlated Riesz-error enclosure component, rather than the tiny nominal operator approximation error. The exact component fraction is stored. This identifies a concrete estimate to sharpen or project; reducing the already small regular-kernel remainder alone cannot remove the present barrier.

## Refined actual rank-38 upper

The validator reuses RC71's paid physical polynomial residual at rank 38 and RC68's unchanged E_F. It tests an explicit finite grid of rational Young parameters and verifies every candidate by exact PSD comparison with RC67's actual 22-input canonical Gram lower bound. Final outward rounding is paid and the comparisons are checked again.

| Parity | Selected parameter | Certified relative upper |
|---|---:|---:|
| Even | 3 | 4235/512 |
| Odd | 9/4 | 2589/512 |

Therefore

\[
\Gamma_{38}^{(22\text{ inputs})}\le(4235/512)M_{22}.
\]

The selected upper matrix itself is checked to dominate rho E_F. A more carefully chosen scalar Young parameter improves the upper modestly, but cannot bypass the fixed-allowance barrier. The selected parameters are not claimed to be globally optimal.

## Independent replay

The physical transfer enclosure is reconstructed exactly from its hashed inputs. Generation multiplies parity norms entrywise; replay applies an independent diagonal congruence. Generation builds the physical trial Gram by matrix multiplication; replay reconstructs it by explicit mass-weighted sums.

Replay independently integrates each witness's physical polynomial norm from monomials, checks the Legendre conversion, reconstructs the witness allowance by congruence, and checks final Young comparisons in Legendre coordinates. The resulting certificate is reproduced exactly. No floating-point eigenvector or sampled positivity is used as proof evidence.

## Evidence boundary and next obligation

RC69 supplied actual complementary leakage lower witnesses for heads through 37. RC72 supplies a different result: a lower bound on the upper majorants in a defined method class. It proves no actual source-budget failure at 38 or 1250 features, no negative Weil direction, no actual Riesz-error lower bound, and no obstruction to aperture positivity. The inherited 1250-complement floor is not asserted as a floor for the 38-feature complement.

The next source estimate must either certify a correlated upper for the projected transfer error (I-Pi38)i*(F-F_nom), or construct a substantially sharper physical Riesz/source error enclosure. Merely adding nominal polynomial columns while retaining the full current E_F cannot certify the inherited scalar budget. The larger input-source covariance and enlarged Weil head floor remain separate open obligations.

RC72 adds its validator, certificate, and this report on the route-consolidation branch. Historical milestone artifacts remain unchanged. No Lean, RH, F4, or whole-aperture positivity conclusion is added.
