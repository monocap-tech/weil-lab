# RPB108 EF11 — actual original even signed Rayleigh, not the rejected conservative cap

**Obligation:** W-EVEN-FORM Priority 2. W-ODD-NEG remains canonical.

## Why the method changes

On the original physical supported cosine
\(f=\mathbf 1_{[-11/10,11/10]}\cos(2\pi(19/25)x)\),
EF10 verified a STRICT lower
\(\langle f,K_{\mathrm{cap},e}f\rangle>
0.879669083946\).
The independently certified original positive energy upper from EF08 is
\(\langle f,A_ef\rangle<0.877811\). Thus

\[
\langle f,(K_{\mathrm{cap},e}-A_e)f\rangle >
0.001858083946.
\]

This **rules out the sufficient domination method using this exact
conservative EF06/07 cap**. It does not show the actual negative
operator overwhelms the original positive one.

The new mathematically faithful object is

\[
Q_e(f)=2\int_0^\infty m(\xi)|\widehat f(\xi)|^2\,d\xi+
2|\langle f,\cosh(x/2)\rangle|^2.
\]

Indeed \(\max(m,\kappa)-(\kappa-m)_+=m\), pointwise.
The diagnostic no longer uses EF04/EF06 cap dominance.

## Exact outward enclosure

For each finite rational frequency cell \(I=[l,r]\), enclose
the actual **signed** multiplier
\([m_l,m_h]\) using monotone original archimedean
lower/upper, complete seven-prime rational phase interval, and
\(|p'|<69\) for the whole cell. Enclose the actual zero-extended
physical Fourier amplitude via exact center interval and
valid global/large-frequency Fourier derivative:
\([a_l,a_h]\subset[0,\infty)\). The interval multiplication
preserves the sign:

\[
2(r-l)\big[
m_l(a_l^2\text{ if }m_l\ge0\text{ else }a_h^2),
\quad
m_h(a_h^2\text{ if }m_h\ge0\text{ else }a_l^2)
\big].
\]

The union of **4096** exact [0,4] subcells and **3968**
exact [4,128] subcells covers all finite original signed frequencies.

For the infinite [128,∞) tail, original monotone
archimedean lower and the seven-prime \(2\sum w_n\) bound give
\(m(\xi)\ge L=\mathrm{arch}_{lo}(128)-TWOC\) for every
\(\xi\ge128\). The physical Fourier transform satisfies
\(|\hat f(\xi)|^2<1/(8\xi^2)\), so the entire reflected
signed tail is bounded below by
\(\min(0,L)/(4\cdot128)\).
The upper tail is EF08's fully signed original positive-operator
enclosure \(<0.040727\) (since \(m\le\max(m,\kappa)\)).
Add the original positive even pole **both sides**, with its
exact-rational overlap interval.

The validator reports a rigorously enclosed *single original signed
Rayleigh* interval without assuming its sign.

**Crucial:** even strictly positive Q on this vector proves nothing
about full even-sector PSD. Any apparent negative original Q would
require independent rederivation and scrutiny before being interpreted
as mathematical evidence against the RH criterion.

**Custody:** EF11 candidate follows EF10 source/merge reconciliation.
Focused GitHub Actions final-head exact rational and governance pending.
No full Weil theorem, RH, or Lean global attachment claim.
