"""Vercel entry point for the read-only Backlot demonstration.

OpenMontage's production pipeline remains a local workload because it needs
FFmpeg, Remotion, long-running processes, and persistent project storage.
The hosted surface intentionally exposes only a bundled, immutable demo.
"""

from __future__ import annotations

import os
from pathlib import Path


REPO_ROOT = Path(__file__).resolve().parent.parent
os.environ.setdefault(
    "OPENMONTAGE_PROJECTS_DIR",
    str(REPO_ROOT / "vercel_demo_projects"),
)

from backlot.server import app  # noqa: E402,F401
