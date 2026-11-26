"""Reconstruct the pinned BK source archive from an authenticated local Git checkout.

No network, no implicit checkout changes, no unverified archive extraction.
This checks byte custody, not the numerical or mathematical comparison.
"""
import argparse
import hashlib
import io
import pathlib
import subprocess
import zipfile

COMMIT = "ea81fd040e51bf0ffbe8fdab3b5c6282cf293a0f"
DIR = "custody/T1D-archives/parts/CR-INT-T1D-BK-reproducibility.zip"
PARTS = (
    (780000, "55f2ec2142715ad65731694991017ece0565a06f"),
    (780000, "828a04b4235b67447896bdee3ac82f4111902732"),
    (780000, "9abdd8b9d20b85dac168804fcf666a80e68300bd"),
    (652441, "9c0583b9cb70bdeba27deedf9ec55d6037bd7476"),
)
SIZE = 2992441
SHA256 = "805fa6a91f0bdb9dbfffde06a9c8a774df744c0ef7b1df74690447e0454669ac"

def require(condition, message):
    if not condition:
        raise ValueError(message)

def reconstruct(repo):
    chunks = []
    for i, (size, sha) in enumerate(PARTS):
        path = f"{DIR}/part-{i:04d}.bin"
        data = subprocess.check_output(["git", "-C", str(repo), "show", f"{COMMIT}:{path}"])
        require(len(data) == size, f"part {i} size")
        blob = hashlib.sha1(f"blob {size}\0".encode()+data).hexdigest()
        require(blob == sha, f"part {i} Git identity")
        chunks.append(data)
    archive = b"".join(chunks)
    require(len(archive) == SIZE, "archive size")
    require(hashlib.sha256(archive).hexdigest() == SHA256, "archive SHA-256")
    with zipfile.ZipFile(io.BytesIO(archive)) as z:
        require(z.testzip() is None, "archive CRC")
        entries = z.namelist()
        require(len(entries) == len(set(entries)), "duplicate archive names")
    return archive, entries

def main():
    p = argparse.ArgumentParser(description=__doc__)
    p.add_argument("canonical_return_checkout", type=pathlib.Path)
    p.add_argument("output_zip", type=pathlib.Path)
    args = p.parse_args()
    archive, entries = reconstruct(args.canonical_return_checkout)
    with args.output_zip.open("xb") as f:
        f.write(archive)
    print("BK BYTE CUSTODY PASS", SHA256, SIZE)
    for entry in entries:
        print(entry)

if __name__ == "__main__":
    main()
