# Weil-Lab NF448 — True original J8 endpoint: complete-source Taylor/Cauchy integration across the previously failed collar

**2026-11-01 PT. ACCEPTED for a rigorously signed original physical endpoint integral prefix \(I_B[0,1/10]\).** Remaining \(I_B[1/10,4B]\), the full source \(z(B)\) point, both true physical signed cells \(D_7,D_8\), the NF410/NF404 original scalar, W-ODD-NEG and RH are **OPEN**. Research draft [PR #469](https://github.com/monocap-tech/weil-lab/pull/469), stacked on NF447 PR #468. No merge to main.

## Previous cursor → current circle → next bold

**NF447 previous:** Paired original digamma and both image families formed the compact-support kernel at the true J8 endpoint \(x=B=11/10\). Original direct 1024-bit Acb integration on \([10^{-12},10^{-3}]\) returned **nan+nanj (METHOD STOP)**. An exact derivative-kernel identity and the original NF413 \(L^2\) plus NF445 4096-bit endpoint input yielded \(|I_B|<902\), while source-native known nonintegral contributions were computed near \(+0.8977981482264882\). None was a resolved numerical \(I_B\) or physical \(z(B)\).

**NF448 current:** **The original near-zero integral is no longer a numerical method stop**. Algebraically divide out the complete-source zero at \(t=0\) *before* any native integral, compute the full original 246-source Taylor coefficients with real Arb intervals at 4096 bits, integrate finite polynomial coefficients exactly, and pay a global Cauchy tail. Successfully extend the same source-preserving method through three nested physical apertures \(t\in[0,0.001]\), \(t\in[0,0.01]\), and \(t\in[0,0.1]\). Each has its own directly verified source envelope, analytic radius and overlapping shorter truncation. No independent real Gauss mesh or finite image shadow is substituted.

## The authentic original source and the true endpoint object

Let

\[
K(t)=\frac{e^{-t/4}}{1-e^{-t}},\qquad
I_B=\frac12\int_0^{4B}K(t)[u_4(B)-u_4(B-t/2)]\,dt,\quad B=11/10.
\]

The source \(u_4\) is **unchanged**: original NF407 242 selected + four critical exact dyadic coefficients (4096-bit original source ball), all 32 critical sine frequencies, 273 actual frequency/order groups and the original odd sinh mode. Source JSON SHA256
0a83cdb71c7d7d0b412f30564aff34fb560140300e02fe08b28302d940b2fcce;
original NF406 true seam SHA256
c2731e3bc422786a28cee7c058c1b41078e80935a6417ba1a149fba14c640675.
Independent original NF445 endpoint native-source JSON SHA256
51b8e0850c678085580940b3ab9afeff8277f446d4407c0200fb75754970db32, required byte-exact by CI before processing.

Define the **removable** functions

\[
L(t)=tK(t)=\frac{e^{-t/4}}{(1-e^{-t})/t},\quad L(0)=1,
\]

\[
G(t)=\frac{u_4(B)-u_4(B-t/2)}{t},\quad
G(0)=\frac{u_4'(B)}2.
\]

Then the true original object is exactly

\[
\boxed{I_B[0,h]=\frac12\int_0^h L(t)G(t)\,dt.}
\]

The **physical** source arguments \(B-t/2\) on \(0\le t\le h\le1/10\) lie inside \([-B,B]\). The finite entire-generator continuation is used on complex disks **only to prove an analytic Cauchy remainder**, not as a new physically active source outside support.

## Actual source-correlated native construction

For every original generator \(c\,y^k\sin(2\pi fy)\) (even \(k\)), respectively \(c\,y^k\cos(2\pi fy)\) (odd \(k\)), use the exact complex carrier \(2\operatorname{Re}(\alpha y^k e^{i\omega y})\) on real \(y\), where

\[
\alpha=-ic/2\text{ for sine},\quad
\alpha=c/2\text{ for cosine},\quad \omega=2\pi f.
\]

Expand \(y=B-t/2\) using the **original source coefficients** and exact polynomial binomial factors. At every Taylor degree, sum all 273 original frequency/order groups **before applying the final real interval charge**. The original sinh pole contributes the exact Taylor series of \(c_{\mathrm{pole}}\sinh(B/2-t/4)\). This is the same original finite odd-source mode, with no new pole or changed support.

Compute the \(L(t)\) Taylor coefficients by formal series division:

\[
\frac{1-e^{-t}}t
=\sum_{j\ge0}\frac{(-1)^j t^j}{(j+1)!},\qquad
e^{-t/4}=\sum_{j\ge0}\frac{(-t/4)^j}{j!}.
\]

For original-source \(u_4(B-t/2)=\sum_{r\ge0}u_rt^r\), the divided difference is \(G(t)=-\sum_{r\ge0}u_{r+1}t^r\). Integrate the resulting \(L(t)G(t)\) coefficients over \([0,h]\) with exact rational powers \(h^{n+1}/(n+1)\), using outward Arb intervals for each coefficient. The *entire complete source* remains one correlated series.

### Remainder proof — no numerical quadrature assumption

On a complex Cauchy circle \(|t|=R\), the original full generator coefficient and polynomial support bound is independently verified:

\[
\sum_{(f,k)} |c_{f,k}|(B+R/2)^k+|c_{\mathrm{pole}}|<10^{160},
\quad f<883,\quad k\le13.
\]

Using \(\pi<22/7\), \(e<11/4\) and \(E=\lceil(22/7)883R\rceil\), charge

\[
M_R=4\cdot10^{160}(11/4)^E
\]

for the complete-source entire analytic continuation on \(|t|=R\). The pole is included in this deliberately conservative envelope. This bounds the analytic coefficients of \(G(t)\).

On \(|t|\le1\), \(L(t)\) is analytic and \(|L(t)|<6\): the denominator \((1-e^{-t})/t\) differs from 1 by at most \(e-2\), giving modulus at least \(3-e>1/4\), and \(|e^{-t/4}|<3/2\).

For \(h<R<1\), let \(q=h/R\). If \(C_R>6/(1-R)\), the **absolute finite Taylor remainder** of degree \(N-1\) is strictly bounded by

\[
\boxed{
\left|I_B[0,h]-I_{N-1}\right|
<
\frac h2\frac{C_RM_R}{R}\frac{q^N}{1-q}.
}
\]

This exact rational tail is recorded in every source artifact, not estimated from the observed coefficient decay. Each original dyadic coefficient-radius uncertainty has a separate valid real-support derivative overcharge \(10^6 S_0\). Native Arb polynomial rounding is enclosed independently. Every panel also checks a shorter truncation \(N-16\) with its own tail and requires intersection of both outward intervals.

The first two disks have \(R=0.01,0.04\), for which \(C_R=7\) exceeds \(6/(1-R)\). The third disk has \(R=0.4\), for which \(6/(1-R)=10\): **NF448 explicitly uses \(C_R=12\)**, not the earlier narrow-disk constant 7. This change was committed and verified before accepting the largest panel.

## Accepted true original nested prefix certificates

| True compact \(t\)-aperture | Cauchy \(R\) | Native Taylor degree | Certified \(I_B[0,h]\) midpoint (approx) | Full interval width |
|---|---:|---:|---:|---:|
| \([0,0.001]\) | \(0.01\) | 239 | \(-2.8772090059190728157\times10^{-11}\) | \(7.778\times10^{-66}\) |
| \([0,0.01]\) | \(0.04\) | 459 | \(-3.0715889073188232814\times10^{-10}\) | \(1.690\times10^{-67}\) |
| \(\boxed{[0,0.1]}\) | \(0.4\) | 1299 | \(\boxed{-1.38432794090920285997\times10^{-7}}\) | \(\boxed{4.001\times10^{-107}}\) |

All full original continuous prefix intervals are **strictly negative**, as are the two non-overlapping differences obtained by rigorous interval subtraction:

\[
I_B[0.001,0.01]\approx-2.7838680067269159998\times10^{-10}<0,
\]

\[
I_B[0.01,0.1]\approx-1.3812563520018840367\times10^{-7}<0.
\]

Their sign is an original **partial endpoint-integral fact**, not a claim about the sign of the entire \(I_B\), \(z(B)\), or \(D_8\). The full source-Cauchy tail charged on \([0,0.1]\) is \(<2.108\times10^{-134}\). The final full interval width is dominated by native outward rational formatting, not the analytic tail.

Three original source-focused CI runs passed: [NF448 first [0,.001] #41398443555](https://github.com/monocap-tech/weil-lab/actions/runs/41398443555), [extended [0,.01] #41398925408](https://github.com/monocap-tech/weil-lab/actions/runs/41398925408), and [large [0,.1] corrected-convolution #41399207892](https://github.com/monocap-tech/weil-lab/actions/runs/41399207892). The three original signed JSON inner SHA256 digests and exact artifacts are preserved in the [NF448 source/custody index](../data/provisional/NF448_original_B_three_nested_Cauchy_prefixes_custody_index.json). The full *rational endpoint intervals* remain in the original GitHub Actions artifacts; their permanent raw-file repo archival is still due before Actions retention expiry.

## Remaining obligation graph and NF449

**NF448 accepted:** First complete continuous original near-zero integral that defeated NF447's Acb; extended true source-correlated Taylor/Cauchy from 0.001 to 0.01 to 0.1, with exact all-source and remainder charges. The **near-B small-t singularity is no longer the obstacle** to numerical endpoint integration.

**Still OPEN:** Complete endpoint \(I_B[0.1,4.4]\), original full physical \(z(B)\) numerical value, complete true original \(D_7,D_8\) source signed \(\int pz,\int z^2\), original principal global \(E_p\), NF410/NF404 whole signed scalar, exterior fourth J242 upper, W-ODD-NEG, even/whole Weil, operator-domain and RH. Six genuine original signed physical cells stay complete: J1,J2,J3 positive; J4,J5,J6 negative.

**Next bold — NF449:** For \([0.1,4.4]\) do not keep expanding one Taylor series about \(t=0\) to tens of thousands of terms. Build **local-center correlated Taylor/Cauchy panels** with exact source convolution and the regularized kernel, narrow certified complex disks, and an adaptive panel allocator. The source support and the NF404 principal/prime routing must remain unchanged, and all panels must provide independent error envelopes before aggregating \(I_B\). Only after a narrow full \(I_B\) interval may original physical J7/J8 signed moments be attempted.

No main merge.
