import os

# openai
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
CHUNK_SIZE = 5000

# language
COMMIT_LANGUAGE = os.environ.get("COMMIT_LANGUAGE", "en")

# convention
DEFAULT_CONVENTION = (
    r'^((revert: ")?(feat|fix|docs|style|refactor|perf|test|ci|build|chore)'
    r"(\(.*\))?!?:\s.{1,50})"
)
COMMIT_CONVENTION = os.environ.get("COMMIT_CONVENTION", DEFAULT_CONVENTION)

# prepare-commit-msg hook script that runs before commit
PREPARE_COMMIT_MSG = """#!/bin/bash
commit_msg_file=$1
commit_source=$2
commit_msg=$(cat $commit_msg_file)

if [ "$commit_source" == "message" ] || [ "$commit_source" == "template" ] || [ "$commit_source" == "merge" ] || [ "$commit_source" == "squash" ] || [ "$commit_source" == "commit" ]; then
    exit 0
fi

echo $(cat .git/temp_commit_msg) > $commit_msg_file
rm .git/temp_commit_msg
"""
