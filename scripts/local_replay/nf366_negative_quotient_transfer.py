#!/usr/bin/env python3
"""NF366: exact PR355 original four-quotient Gram replay; no native-Arb re-evaluation."""
import argparse
import hashlib
import io
import json
import os
import urllib.request
import zipfile
from fractions import Fraction

ZIP_SHA = "f7b64ceead7500fca389e3b994a208a6e8aae5be3270b750ab586e5ebe1fa1d0"
JSON_SHA = "d853e2ecf665b8bb3978ee203371c07f67d050b79e7427d6c673331fd1d60ab9"
ARTIFACT_ID = 12776684037

def dyad(pair):
    mantissa, exponent = int(pair[0]), int(pair[1])
    return Fraction(mantissa << exponent) if exponent >= 0 else Fraction(mantissa, 1 << (-exponent))

def fetch_archive(offline):
    if offline:
        with open(offline, "rb") as stream:
            return stream.read()
    token = os.environ.get("GITHUB_TOKEN")
    if not token:
        raise RuntimeError("Supply --offline PATH or GITHUB_TOKEN for GitHub Actions")
    url = (f"https://api.github.com/repos/monocap-tech/weil-lab/"
           f"actions/artifacts/{ARTIFACT_ID}/zip")
    request = urllib.request.Request(
        url,
        headers={
            "Authorization": "Bearer " + token,
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28",
            "User-Agent": "Weil-Lab-NF366-Custody",
        },
    )
    with urllib.request.urlopen(request, timeout=70) as stream:
        return stream.read()

def main():
    parser = argparse.ArgumentParser()
    parser.add_argument("--offline", default=None)
    args = parser.parse_args()
    blob = fetch_archive(args.offline)
    assert hashlib.sha256(blob).hexdigest() == ZIP_SHA, "PR355 ZIP mismatch"
    with zipfile.ZipFile(io.BytesIO(blob)) as archive:
        data = archive.read("original_exterior_scalar_floor_stop.json")
    assert hashlib.sha256(data).hexdigest() == JSON_SHA, "native JSON mismatch"
    obj = json.loads(data)
    gram = obj["physical_quotient_Gram_native"]
    assert obj["selected_rank"] == 242 and len(gram) == 4
    trace_upper = Fraction(0)
    for i in range(4):
        assert len(gram[i]) == 4
        mid = dyad(gram[i][i][0])
        radius = dyad(gram[i][i][1])
        assert radius >= 0 and mid >= radius
        trace_upper += mid + radius
    assert 0 < trace_upper < Fraction(1, 2**604)
    negative_squared_upper = 17**2 * trace_upper
    assert negative_squared_upper < Fraction(1, 10**179)
    print("PASS NF366: original archived 4x4 native quotient trace < 2^-604")
    print("PASS NF366: 17^2 * trace < 1e-179 (entire negative operator transfer)")
    print("trace approx", float(trace_upper))
    print("negative squared upper approx", float(negative_squared_upper))
    print("NOT full signed positivity / NOT original native Arb recomputation")

if __name__ == "__main__":
    main()
