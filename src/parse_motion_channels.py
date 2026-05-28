#!/usr/bin/env python3
import json
import sys
from pathlib import Path

def main():
    path = Path(__file__).resolve().parent.parent / "data" / "motion_channels.json"
    if len(sys.argv) > 1:
        path = Path(sys.argv[1])
    data = json.loads(path.read_text(encoding="utf-8-sig"))
    print("clip:", data.get("clip"), "fps:", data.get("fps"))
    for ch in data.get("channels", []):
        keys = ch.get("keys", [])
        ts = ", ".join(str(k.get("t")) for k in keys[:5])
        print(" ", ch.get("name"), "[" + ts + "]")

if __name__ == "__main__":
    main()
