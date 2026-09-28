# Additive correction to GERM-72 — source-word custody

**Date:** 2026-09-28  
**Issued by:** GERM-73, one individual NF pass  
**Standing:** UNRATIFIED RESEARCH CORRECTION  
**Canonical theorem cursor:** SZ-CROSS-COLLAR-3, unchanged

## Determination

GERM-72's A3 and D3 source-word assignments are incorrect. Its resulting factor-40 cone certificate is not a certificate for the actual source recurrence. The two assignments and the factor-40 claim are withdrawn from current use. The original files remain historical records.

The GERM-72 interval itself is recovered by a new proof in [GERM-73](_recurrence73.md), with the correct words and a factor 5/2. GERM-73 then extends that repaired interval. This is not retrospective validation of the erroneous calculation.

## Exact error

In the GERM-71 second-section coordinate, put
```math
\zeta=\tau-\theta+\varepsilon.
```
An exterior-to-exterior third return still passes through the overlap. Its endpoint bits do not determine its intermediate bits.

The correct chronological words are:
```text
A3: 01-, 11+, 10+
D3: 01-, 11+, 11+, 10+
```
GERM-72 instead used:
```text
A3: 00-, 00+, 00+
D3: 00-, 00+, 00+, 00+
```

For example, choose `epsilon=gamma/2` and `v=3theta/4`. The second-section points are
```math
\tau-\theta+v,\quad v,\quad v+\theta,\quad v+2\theta.
```
Their exact overlap bits are `0,1,1,0`; hence the required word is `01-,11+,10+`. The analogous D3 witness is `v=alpha/2`, with bits `0,1,1,1,0`. GERM-73 certifies all these inequalities and their original-step lifts by exact affine tests, not sampled topology.

GERM-72's Q3 and P3 assignments survive this audit. Its matrix-product arithmetic was not the missing obligation: the unchecked ordinary-word source domains were.

## Consequences

The old chart `[[1,1],[3/5,1/5]]` sends the corrected J word to a matrix with positive first row and negative second row. Neither overall sign preserves its claimed same-sign cone. The factor 40 must not be reused.

The repaired three-word library uses chart `[[1,1],[1,3]]`, with certified common forward/backward factor 5/2. This re-establishes
```math
3h-\theta<e\le3h-\theta+\gamma.
```
The exact L72 expression remains correct. Its corrected decimal is `1.711168966534648195...`.

The physical observation on the fourth section is `W(h-beta+w)`, not an unqualified `W(alpha+w)` in the original low-head coordinate. The latter is valid only after explicitly defining the theta-section pullback. GERM-73 retains the physical translation.

## Audit limits

The GERM-72 wrapper was not used as an inherited certificate or claimed as newly replayed. GERM-73 recomputes physical matrices using the pinned GERM-71 source solver, verifies containment in its recorded boxes, and checks the actual source words before issuing replacement bounds.

The correction does not change GERM-71's standing, does not ratify any experimental result, and does not advance the canonical SZ theorem cursor.
