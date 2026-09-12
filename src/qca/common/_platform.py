from __future__ import annotations

import platform

from qca._version import __version__

# The spellings match the Go SDK's convention/requestconfig.go on purpose: the
# server aggregates SDK usage across languages, so the same machine has to land
# in the same bucket no matter which SDK called. platform.machine() and Go's
# runtime.GOARCH name the same architecture differently, hence the aliases.
_OS_NAMES = {
    "darwin": "MacOS",
    "windows": "Windows",
    "linux": "Linux",
    "ios": "iOS",
    "android": "Android",
    "freebsd": "FreeBSD",
    "openbsd": "OpenBSD",
}

_ARCH_NAMES = {
    "386": "x32",
    "i386": "x32",
    "i686": "x32",
    "x86": "x32",
    "amd64": "x64",
    "x86_64": "x64",
    "arm": "arm",
    "armv7l": "arm",
    "arm64": "arm64",
    "aarch64": "arm64",
}


def platform_headers() -> dict[str, str]:
    system = platform.system().lower()
    machine = platform.machine().lower()
    return {
        "X-Qoder-Lang": "python",
        "X-Qoder-Package-Version": __version__,
        "X-Qoder-OS": _OS_NAMES.get(system, f"Other:{system or 'unknown'}"),
        "X-Qoder-Arch": _ARCH_NAMES.get(machine, f"other:{machine or 'unknown'}"),
        "X-Qoder-Runtime": platform.python_implementation(),
        "X-Qoder-Runtime-Version": platform.python_version(),
    }
