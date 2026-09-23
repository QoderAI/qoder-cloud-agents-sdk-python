#!/usr/bin/env python3
"""Rewrite a trusted local sdist with deterministic archive metadata."""

from __future__ import annotations

import argparse
import gzip
import os
import tarfile
import tempfile
from pathlib import Path


def normalize_sdist(archive: Path, epoch: int) -> None:
    with tempfile.TemporaryDirectory() as work:
        root = Path(work)
        with tarfile.open(archive, "r:gz") as source:
            source.extractall(root, filter="fully_trusted")

        output = archive.with_name(f".{archive.name}.tmp")
        with output.open("wb") as raw:
            with gzip.GzipFile(filename="", mode="wb", fileobj=raw, compresslevel=9, mtime=0) as compressed:
                with tarfile.open(fileobj=compressed, mode="w|", format=tarfile.PAX_FORMAT) as target:
                    for path in sorted(root.rglob("*"), key=lambda item: item.as_posix()):
                        info = target.gettarinfo(str(path), arcname=path.relative_to(root).as_posix())
                        info.uid = 0
                        info.gid = 0
                        info.uname = ""
                        info.gname = ""
                        info.mtime = epoch
                        if info.isfile():
                            with path.open("rb") as contents:
                                target.addfile(info, contents)
                        else:
                            target.addfile(info)
        os.replace(output, archive)


def main() -> None:
    parser = argparse.ArgumentParser()
    parser.add_argument("archive", type=Path)
    parser.add_argument("--epoch", type=int, required=True)
    args = parser.parse_args()
    normalize_sdist(args.archive, args.epoch)


if __name__ == "__main__":
    main()
