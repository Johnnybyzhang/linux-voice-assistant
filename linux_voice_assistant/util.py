"""Utility methods."""

import platform
import uuid
from collections.abc import Callable
from typing import Optional


def get_mac() -> str:
    mac = uuid.getnode()
    mac_str = ":".join(f"{(mac >> i) & 0xff:02x}" for i in range(40, -1, -8))
    return mac_str


def call_all(*callables: Optional[Callable[[], None]]) -> None:
    for item in filter(None, callables):
        item()


def is_arm() -> bool:
    machine = platform.machine()
    return ("arm" in machine) or ("aarch" in machine)


def is_armhf() -> bool:
    """Check if running on 32-bit ARM (armhf/armv7l/armv6l)."""
    machine = platform.machine().lower()
    # Check for 32-bit ARM: armv6, armv7, armv8 (32-bit), but not aarch64
    return ("arm" in machine or machine.startswith("armhf")) and "aarch64" not in machine and "arm64" not in machine


def is_arm64() -> bool:
    """Check if running on 64-bit ARM (aarch64/arm64)."""
    machine = platform.machine().lower()
    return "aarch64" in machine or "arm64" in machine
