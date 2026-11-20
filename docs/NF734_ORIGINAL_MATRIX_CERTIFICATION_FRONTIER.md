# NF734 — Original physical matrix certification frontier after index-one closure

## Accepted kernel custody recovered

NF733 has now completed its independent source-and-kernel custody audit,
**run [44782027897](https://github.com/monocap-tech/weil-lab/actions/runs/44782027897) SUCCESS**,
publishing the immutable permanent source-bound certificate artifact
**[14652498322](https://github.com/monocap-tech/weil-lab/actions/runs/44782027897/artifacts/14652498322)**.

The **original global** (not local-only) physical matrix index-one declarations
are accepted as two Lean universal theorems:

```lean
nf732OriginalHDRowOneAll :
  ∀ i : Fin 242,
    nf703OriginalCache.HDGate nf702OriginalInputs (1 : Fin 242) i = true

nf732OriginalAColumnOneAll :
  ∀ i : Fin 242,
    nf703OriginalCache.AGate nf702OriginalInputs i (1 : Fin 242) = true
```

Both passed with exactly
`[propext, Classical.choice, Quot.sound]`.
Their accepted source, eight genuine numerical source-specific quad objects,
and printed Lean axiom output were independently reauthenticated in NF733.

## Original matrix index-zero: the next incomplete but partially certified axis

Original **HD row zero** and original **A column zero** already have
independently accepted true global product gates for positions **0–23**:

| Original index-zero positions | Accepted source-bound Lean stage | Successful workflow | Immutable accepted source/audit artifact |
| --- | --- | --- | --- |
| 0–7 | NF708 | [44640227758](https://github.com/monocap-tech/weil-lab/actions/runs/44640227758) | 14589570565 |
| 8–15 | NF713 | [44649041852](https://github.com/monocap-tech/weil-lab/actions/runs/44649041852) | 14594190839 |
| 16–23 | NF715 third global frontier | [44669131044](https://github.com/monocap-tech/weil-lab/actions/runs/44669131044) | 14599683589 |

The accepted index-zero total is **24 HD + 24 A gate instances**,
in addition to the **242 HD + 242 A index-one instances**.

Thus the independently evidenced accepted total is
**532 original global matrix-product gate instances** as of the NF733
closure and before NF734's new kernel run. This is a gate count,
not a count of universal theorem declarations or of unique supporting
Lean lemmas.

The next original index-zero interval is **24–31**: eight HD row-zero
and eight A column-zero products, with **32 new declaration proof terms**
and the existing three shared NF704 projection identities. This
continues the *same* NF702 frozen input, NF703 full cache, NF681 local
dot bank and NF704 projection emitter. It does not substitute
a new rounded or synthetic matrix.

The NF734 driver requires all three accepted earlier source manifests and
axiom receipts, checks that the first **25 Lean source files**
(Common + Col000…Col023) are byte-for-byte identical to the accepted
third-stage bank, then generates Col024…Col031 and requests a new Lean
kernel audit of exactly 35 declarations. A generated source is **not**
a Lean-accepted proof.

## Exact remaining frontier before the new NF734 batch passes

| Product family | Accepted source-bound positions | Not yet closed by the cited custody |
| --- | --- | --- |
| Original HD row index 0 | 0–23 (24/242) | 24–241 (218 positions) |
| Original A column index 0 | 0–23 (24/242) | 24–241 (218 positions) |
| Original HD row index 1 | 0–241 (242/242) **universal Lean PASS** | None for this fixed row |
| Original A column index 1 | 0–241 (242/242) **universal Lean PASS** | None for this fixed column |
| Other original HD rows / A columns | Not established by this cited source chain | Requires separate evidence and acceptance |
| Original global vector gates | First 48/242 previously kernel accepted | 194 rows remain in that separately tracked frontier |
| Original physical full-payment rows | First 48/242 previously kernel accepted | 194 rows remain in that separately tracked frontier |

For original matrix-product gate instances, counting only the proved
index-zero and index-one portions yields **532/117128** possible
HD/A gate positions on two full 242×242 arrays. This count does **not**
assert that all other positions are false or unknowable; it records the
coverage supported by these explicitly authenticated certificates.

After a successful NF734 original index-zero kernel audit, the supported
covered index-zero sets would become 0–31 (32/242 each), bringing the
certified gate-instance count to **548**, leaving positions 32–241
(210 each) of index zero unclosed in this source chain.

## Why the next step is genuinely numerical

The existing NF681 source has a locally certified
242-coordinate original-product inventory for the first HD row and
first A column. The remaining task is **genuine global** attachment to
the original NF702 and NF703 frozen source/cache objects. The NF704
emitter produces claims of the form

```lean
nf703OriginalCache.HDGate nf702OriginalInputs 0 (i : Fin 242) = true
nf703OriginalCache.AGate nf702OriginalInputs (i : Fin 242) 0 = true
```

for each new `i` in 24–31. It is not enough to observe the locally
accepted dot-product receipts, or to have a Python source manifest. Each
actual global proposition must be kernel accepted under only the permitted
standard axioms.

## Certification boundaries

An **accepted universal index-one statement is not complete 242×242
matrix enclosure**. Other matrix indices, vector-payment gates,
full numerical enclosure custody, physical corrected-form transport,
global Weil positivity, and RH remain separate obligations. The
NF734 source preflight or a CI run merely submitted does not itself
expand certified matrix coverage.

The matrix-frontier inventory uses the actual NF708/NF713/NF715 and
NF733 artifact IDs. It does not claim an exhaustive search of all
possible unrelated historical Lean theorem names.
