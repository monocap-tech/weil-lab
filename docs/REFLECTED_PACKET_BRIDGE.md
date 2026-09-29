# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-35.

## Current standing

```math
oxed{
	extbf{RPB-50 — ONE NONZERO SCREW-CORE NEUTRAL DIRECTION COLLAPSES EVERY POSITIVE-LENGTH NEUTRAL PLATEAU; THE CORE-RESTRICTED NULL-EXTENSION INTERFACE IS DISCHARGED NEGATIVELY.}
}
```

RPB-49 proved that every nonzero screw-core endpoint null direction leaks under
every strict support enlargement:

```math
0
e uinker G_c
Longrightarrow
G_aJ_{c,a}u
e0
qquad
(a>c).
```

RPB-34 already showed that any such leakage produces a strict negative test
direction by the collar (2	imes2) argument.  Therefore

```math
oxed{
G_csucceq0,
quad
ker G_c
e0
Longrightarrow
G_a
otsucceq0
qquad
(a>c).
}
```

So an actual neutral edge cannot begin a positive-length nonnegative/neutral
right plateau.

Through the RPB-30 neutral-resolvent isomorphism and the RPB-32/33 screw-core
identification, the selected unit-gain eigenspace contains the nonzero core
subspace

```math
E_*^{m core}
=
J_*^{-1}
left(
D^{-1}(ker G_{c_*})
ight)

e{0}.
```

Every nonzero physical representative of this subspace fails strict
null-extension.  Thus the core-restricted form of
`AZ-FIN-WEIL-NULL-EXTENSION` is discharged negatively.

The full canonical mode-wise interface is not promoted closed here because the
remaining multiplicity defect

```math
delta_{m core}(c)
=
dimker A_c-dimker G_c
```

has not yet been proved to vanish.  Noncore Friedrichs zero modes, if they
exist, could still pose a mode-wise null-extension question; they cannot,
however, restore a nonnegative plateau because the already-existing core mode
forces right-side negativity.

## Next cursor

```text
RPB-51 / ZERO-EIGENSPACE MULTIPLICITY AND CORE-LIFT AUDIT
```

The next pass should test

```math
dimker A_c
stackrel{?}{=}
dimker G_c
```

at the actual neutral edge using Suzuki's generalized eigenvalue equivalence
with explicit multiplicity bookkeeping.  Equality would promote the
core-restricted negative null-extension result to the entire Friedrichs zero
eigenspace; failure would isolate the noncore zero-mode quotient as the final
irreducible residue.

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_50_20260928.md`.
