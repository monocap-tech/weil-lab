#!/usr/bin/env python3
"""CP012: Exact countermodel to indexed numerical-row recovery from BatchSpec.

This does NOT question any original Zeta Lean zero-count or positivity theorem.
It shows that the PUBLIC BATCH INTERFACE (count + first left + last
right) does not determine the missing per-index numeric endpoints, EVEN IF
all slots are disjoint and contain a complete, simple, identical root roster.

Optional original upstream source contract check uses immutable git SHA-1
with real 2026 upstream Zeta BatchSpec/append declarations. No fabricated
Lean kernel certificate is emitted.
"""
from __future__ import annotations

import argparse
import hashlib
import json
from dataclasses import dataclass
from fractions import Fraction as F
from pathlib import Path

SOURCE_COMMIT = "c06b4e13d9c847e50a32c3d738271cbad62ae9f3"
BLOBS = {
    "Zeta/Zeros/Certificates/Basic.lean": "128e19e4bb056332b0fd71a8c107f4075cd8cd07",
    "Zeta/Zeros/Certificates/Fold.lean": "2596e253a8c8f94c47ce880500973775f2611d77",
    "Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean":
        "12848f56d0b62df858dcb89b708a858f4f7b28fb",
}
EXPECTED_BATCH_THEOREM = (
    "theorem batch : BatchSpec 200 149500 1000 474603 1000 := "
    "by build_batch_rs 0 200"
)


@dataclass(frozen=True)
class Interval:
    left: F
    right: F


def mock_public_batch_projection(intervals):
    """Exactly the three externally visible data of upstream BatchSpec."""
    assert intervals
    return {
        "length": len(intervals),
        "head_fst": intervals[0].left,
        "last_snd": intervals[-1].right,
    }


def check_complete_simple_slot_model(intervals, roots):
    """Pure rational abstract-model check; NOT a zeta-zero or Lean proof."""
    assert len(intervals) == len(roots)
    assert all(x.left < root < x.right for x, root in zip(intervals, roots))
    assert all(x.right <= y.left for x, y in zip(intervals, intervals[1:]))
    assert len(set(roots)) == len(roots)
    assert set(roots) == {F(1, 2), F(3, 2), F(5, 2)}
    return True


def countermodel():
    roots = [F(1, 2), F(3, 2), F(5, 2)]
    model_a = [
        Interval(F(0), F(1)),
        Interval(F(1), F(2)),
        Interval(F(2), F(3)),
    ]
    model_b = [
        Interval(F(0), F(9, 10)),
        Interval(F(13, 10), F(17, 10)),
        Interval(F(2), F(3)),
    ]
    assert check_complete_simple_slot_model(model_a, roots)
    assert check_complete_simple_slot_model(model_b, roots)
    assert mock_public_batch_projection(model_a) == mock_public_batch_projection(model_b)
    assert model_a[0].right != model_b[0].right
    assert model_a[1] != model_b[1]
    assert model_a[1].left != model_b[1].left
    assert len(roots) == 3  # Turing-like n=3 exact count, no other zeros
    # Negative control: even knowing ALL 3 true simple roots and the entire
    # root order, the exact certificate ENDPOINTS need not be unique.
    assert model_a != model_b

    # Distinct proposed indexed rows are equally compatible with the
    # identical public data; a claimed row binding cannot be recovered.
    print("CP012 EXACT FRACTION BATCHSPEC INDEXED-ROW NONIDENTIFIABILITY: PASS")
    print("both: length=3, first-left=0, last-right=3,")
    print("both: complete ordered distinct root roster 1/2,3/2,5/2")
    print("yet first interval right and second interval endpoints differ")
    print("This is a countermodel to a SOURCE-TO-ROW logical inference,")
    print("not a counterexample to zeta zero uniqueness or the upstream theorem.")


def sha_git_blob(path):
    length = path.stat().st_size
    digest = hashlib.sha1(b"blob " + str(length).encode() + b"\0")
    with path.open("rb") as stream:
        for part in iter(lambda: stream.read(1 << 20), b""):
            digest.update(part)
    return digest.hexdigest()


def check_upstream_source(upstream_root, report_path):
    actual = {}
    for rel, expected in BLOBS.items():
        path = upstream_root / rel
        if not path.is_file():
            raise ValueError(f"Missing actual pinned upstream source {rel}")
        got = sha_git_blob(path)
        if got != expected:
            raise ValueError(f"Original upstream Git blob drift: {rel} {got} != {expected}")
        actual[rel] = path.read_text(encoding="utf-8")
    basic = actual["Zeta/Zeros/Certificates/Basic.lean"]
    fold = actual["Zeta/Zeros/Certificates/Fold.lean"]
    batch = actual["Zeta/Zeros/Certificates/RiemannSiegel/Batch0001.lean"]
    start = basic.find("abbrev BatchSpec (n an ad bn bd : ℕ) : Prop :=")
    end = basic.find("\nnamespace BatchSpec", start)
    if not (0 <= start < end):
        raise ValueError("Pinned upstream public BatchSpec type no longer locatable")
    statement = basic[start:end]
    for needle in (
        "∃ C : CertifiedZeroIntervals, C.intervals.length = n",
        "C.intervals.head?.map (·.fst) = some (Enclosure.sfrac false an ad)",
        "C.intervals.getLast?.map (·.snd) = some (Enclosure.sfrac false bn bd)",
    ):
        if needle not in statement:
            raise ValueError(f"Original public BatchSpec contract changed: {needle}")
    if ".get " in statement or ".getElem" in statement:
        raise ValueError("Original BatchSpec now names indexed source rows: re-audit no-go")
    for needle in (
        "theorem BatchSpec.append",
        "BatchSpec (n₁ + n₂) an ad en ed",
    ):
        if needle not in fold:
            raise ValueError("Original batch append source interface changed")
    if EXPECTED_BATCH_THEOREM not in batch:
        raise ValueError("Original first RS 200-row batch public theorem differs")
    countermodel()
    result = {
        "status": "PINNED_SOURCE_BATCHSPEC_ROW_OPACITY_CONFIRMED_NOT_LEAN",
        "source_commit": SOURCE_COMMIT,
        "original_git_blobs": BLOBS,
        "original_first_rs_public_batch_count": 200,
        "original_first_rs_public_first_left": "149500/1000",
        "original_first_rs_public_last_right": "474603/1000",
        "first_rs_source_row_right_endpoint_exposed": False,
        "required_additional_lean_statement":
            "SourceRowBinding certifiedZeroCount (Fin 52 ...) "
            "source_first_RS_left source_first_RS_right",
        "required_proof":
            "original compiled source-defined bundle/row index identification, "
            "NOT merely original source SHA, BatchSpec, batch length, "
            "Turing count or a separately certified new bracket",
        "kernel_receipt": None,
    }
    report_path.write_text(json.dumps(result, indent=2) + "\n", encoding="utf-8")
    print("CP012 EXACT SOURCE BATCHSPEC OPACITY AUDIT: PASS — NO ROW BINDING PROVED")


def main():
    p = argparse.ArgumentParser()
    p.add_argument("--self-test", action="store_true")
    p.add_argument("--upstream-source-root", type=Path)
    p.add_argument("--receipt", type=Path,
                   default=Path("cp012-source-row-interface-receipt.json"))
    args = p.parse_args()
    if args.self_test:
        countermodel()
    if args.upstream_source_root:
        try:
            check_upstream_source(args.upstream_source_root, args.receipt)
        except (OSError, ValueError, UnicodeError, AssertionError) as exc:
            raise SystemExit(f"NOT_READY: {exc}")
    if not args.self_test and not args.upstream_source_root:
        p.print_help()


if __name__ == "__main__":
    main()
