#!/usr/bin/env python3
"""news-image-20261118: one image summing up Wednesday 18 November 2026.

A dense newspaper front page — masthead dated WEDNESDAY 18 NOVEMBER 2026,
three illustrated leads (Iran's drones hit the US air base in Kuwait; APEC
opens in Shenzhen with Xi greeting Trump; the COP31 draft splits talks over
a fossil-fuel phase-out), ten more illustrated stories, a world map with
twelve numbered pins, and twenty-six one-line briefs: 39 verified stories
from six continents in total. A DATE CHECK footer lists the big stories
deliberately left out because they were first reported on 17 November
(Kerch Bridge, Peltola's Alaska win, Nvidia's $115.8bn quarter, the Prague
train crash, Mongolia's president resigning, the US losing measles-free
status). Every story was reported on 18 November 2026 (Reuters, AP, ABC
News, Al Jazeera, OHCHR, BBC, The Guardian, Bloomberg, IMD, NASA and
others; see notes.md). All words are rendered in PIL so the spelling is
exact; the thirteen scene illustrations carry no text.

The program only copies the held image (news-v5.jpg, in this repository)
to /output/entry.png. It is deterministic: two runs write byte-identical
files, with no network and no randomness.

Run locally: `mkdir -p out && MAKEFUN_OUTPUT_DIR=out python3 main.py`
"""

import hashlib
import os
import sys

ART_FILE = "news-v5.jpg"
ART_SHA256 = "3f727d1c2790d79fe45e057e1a1126eb90f98982d431c4a59ed8ab1ea43fffdc"
MAX_BYTES = 1048576
MAX_DIMENSION = 1024
JPEG_MAGIC = b"\xff\xd8\xff"


def load_art():
    here = os.path.dirname(os.path.abspath(__file__))
    path = os.path.join(here, ART_FILE)
    with open(path, "rb") as handle:
        return handle.read()


def jpeg_dimensions(data):
    """Return (width, height) from the first SOF0/SOF2 marker, else None."""
    pos = 2
    end = len(data)
    while pos + 1 < end:
        if data[pos] != 0xFF:
            return None
        pos += 1
        while pos < end and data[pos] == 0xFF:
            pos += 1
        if pos >= end:
            return None
        marker = data[pos]
        pos += 1
        if marker == 0x01 or 0xD0 <= marker <= 0xD9:
            continue
        if pos + 2 > end:
            return None
        length = (data[pos] << 8) | data[pos + 1]
        if length < 2 or pos + length > end:
            return None
        if marker in (0xC0, 0xC2):
            if pos + 7 > end:
                return None
            height = (data[pos + 3] << 8) | data[pos + 4]
            width = (data[pos + 5] << 8) | data[pos + 6]
            return (width, height)
        if marker == 0xDA:
            return None
        pos += length
    return None


def check_art(data):
    if data[:3] != JPEG_MAGIC:
        return "held art is not a JPEG"
    if hashlib.sha256(data).hexdigest() != ART_SHA256:
        return "held art failed its integrity check"
    if len(data) > MAX_BYTES:
        return "held art exceeds the 1 MiB gate"
    dims = jpeg_dimensions(data)
    if dims is None:
        return "held art has no readable JPEG dimensions"
    if dims[0] > MAX_DIMENSION or dims[1] > MAX_DIMENSION:
        return "held art exceeds the 1024x1024 gate"
    return None


def main():
    data = load_art()
    problem = check_art(data)
    if problem is not None:
        sys.exit(problem)
    outdir = os.environ.get("MAKEFUN_OUTPUT_DIR") or "/output"
    os.makedirs(outdir, exist_ok=True)
    with open(os.path.join(outdir, "entry.png"), "wb") as handle:
        handle.write(data)


if __name__ == "__main__":
    main()
