"""Restore byte-exact gzip archives from the published UTF-8 transport files."""
import base64, gzip, hashlib
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1] / 'notes/data'

def restore():
    gram = 'RPB108_PRIME5_GRAM96_097_CERTIFICATE_20261007.json.gz'
    checkpoint = 'RPB108_PRIME5_GRAM96_097_COMPLETE_PANEL_CHECKPOINT_20261007.json.gz'
    items = [
        (gram, [gram + '.base64'], '712d2043aa52974306c77e6b4f86d61f57788b7b9da8e5e8cc0675ee5433ba28', '9d86c98ab7e9f10be43b25d33a1dc3b41709c220a8ec2cb310eb7023fae01793'),
        (checkpoint, [checkpoint + f'.part{i:02}.base64' for i in range(1, 4)], '4e694dd59fd4b7c75386d62eee2e4d1593d48167d69a062514db6c5c9cf12f55', 'fb28cc25a1de5d0a6fef527190d98c605783797b9023144d621f52e11aed43fb'),
    ]
    for name, parts, compressed_hash, decoded_hash in items:
        raw = b''.join(base64.b64decode((ROOT / part).read_text().strip(), validate=True) for part in parts)
        assert hashlib.sha256(raw).hexdigest() == compressed_hash
        assert hashlib.sha256(gzip.decompress(raw)).hexdigest() == decoded_hash
        target = ROOT / name
        if target.exists():
            assert target.read_bytes() == raw
        else:
            target.write_bytes(raw)
        print(name, 'verified')

if __name__ == '__main__':
    restore()
