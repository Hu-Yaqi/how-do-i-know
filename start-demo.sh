#!/usr/bin/env bash
# Mac / Linux: runs the show from this folder without internet. Press Ctrl+C to stop.
cd "$(dirname "$0")" || exit 1
exec python3 serve.py "$@"
