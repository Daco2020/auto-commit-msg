import os

# openai
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_ENGINE = os.environ.get("OPENAI_ENGINE", "gpt-3.5-turbo")
CHUNK_SIZE = 5000

# language
COMMIT_LANGUAGE = os.environ.get("COMMIT_LANGUAGE", "en")

# convention
DEFAULT_CONVENTION = (
    r'^((revert: ")?(feat|fix|docs|style|refactor|perf|test|ci|build|chore)'
    r"(\(.*\))?!?:\s.{1,50})"
)
COMMIT_CONVENTION = os.environ.get("COMMIT_CONVENTION", DEFAULT_CONVENTION)
