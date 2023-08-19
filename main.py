#!/usr/bin/env python

import subprocess
import os

from config import PREPARE_COMMIT_MSG
from commit_msg_generator import CommitMessageGenerator


def run() -> None:
    """Run the auto-commit-msg script."""
    create_prepare_commit_msg()

    diff = get_diff()
    generator = CommitMessageGenerator()
    message = generator.generate_commit_message(diff)

    with open(".git/temp_commit_msg", "w") as file:
        file.write(message)


def create_prepare_commit_msg() -> None:
    """Create a prepare-commit-msg hook that will be run before commit."""
    with open(".git/hooks/prepare-commit-msg", "w") as file:
        file.write(PREPARE_COMMIT_MSG)
    os.chmod(".git/hooks/prepare-commit-msg", 0o755)


def get_diff() -> str:
    """Get the diff of the staged files."""
    cmd = ["git", "diff", "HEAD"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout
