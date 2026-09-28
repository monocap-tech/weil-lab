# Reflected-Packet Bridge

**Repository:** Weil-Lab  
**Branch:** `research/reflected-packet-bridge`  
**Standing:** experimental / not canonical promotion  
**Imported provenance source:** `monocap-tech/weil@research/reflected-packet-bridge` through RPB-34.

## Current standing

```math
\boxed{
\textbf{RPB-34 — THE SCREW-KERNEL DIAGONAL CROSSING FORM IS IDENTICALLY ZERO; THE RELEVANT OBJECT IS COLLAR LEAKAGE.}
}
```

For nested supports (0<c<a), zero extension (J_{c,a}) satisfies

```math
J_{c,a}^*G_aJ_{c,a}=G_c.
```

Hence for every (u\in\ker G_c),

```math
\langle G_aJ_{c,a}u,J_{c,a}u\rangle=0.
```

Define the collar leakage

```math
\mathcal L_{c,a}u:=G_aJ_{c,a}u.
```

Then

```math
\mathcal L_{c,a}u=0
\Longrightarrow
J_{c,a}u\in\ker G_a,
```

while

```math
\mathcal L_{c,a}u\ne0
\Longrightarrow
G_a\text{ has a negative direction}.
```

Immediate right negativity does not by itself force kernel leakage because compact positive-tail escape remains possible.

## Next cursor

```text
RPB-35 / SCREW-POTENTIAL COLLAR RIGIDITY OF ker G_{c_*}
```

The next pass should test whether a nonzero (u\in\ker G_{c_*}) can have

```math
F_u(x)=\int_{-c_*}^{c_*}g(x-y)u(y)\,dy
```

remain constant on any strict enlargement of ((-c_*,c_*)).

## Governance

The RPB line is a lab investigation. A committed pass may contain proved branch-local statements, imported results, scope/no-go statements, or open residue. Commit status is not canonical status. Promotion into the stable Weil theorem line requires a separate explicit audit.

Historical RPB notes are immutable. Later corrections are additive.

## Ledger

The full pass-by-pass record is stored in `notes/REFLECTED_PACKET_BRIDGE_0_20260928.md` through `notes/REFLECTED_PACKET_BRIDGE_34_20260928.md`.
