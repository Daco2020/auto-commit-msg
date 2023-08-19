from typing import Any
import openai

from config import (
    CHUNK_SIZE,
    COMMIT_LANGUAGE,
    CONTENTS,
    DEFAULT_CONTENT,
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


class CommitMessageGenerator:
    def __init__(
        self,
    ) -> None:
        openai.api_key = OPENAI_API_KEY
        self.model = OPENAI_MODEL
        self.chunk_size = CHUNK_SIZE
        self.content = CONTENTS.get(COMMIT_LANGUAGE, DEFAULT_CONTENT)

    def generate_commit_message(self, diff: str) -> str:
        """Generates a commit message based on the diff provided."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self._build_messages(diff),
            max_tokens=500,
            temperature=0.5,
            top_p=0.5,
        )
        return response.choices[0].message.content

    def _build_messages(self, diff: str) -> list[dict[str, Any]]:
        """Builds a list of messages to send to the OpenAI API."""
        messages = [{"role": "system", "content": self.content["instruction_request"]}]

        if len(diff) > self.chunk_size:
            # If the diff is too large, summarize it in chunks
            combined_summary = self._get_combined_summary(diff)
            content = self.content["commit_msg_request"] + combined_summary
        else:
            # If the diff is too small, use it as is
            content = self.content["commit_msg_request"] + diff

        content += self.content["convention_request"] + self.content["answer_language"]
        messages.append({"role": "user", "content": content})

        return messages

    def _get_combined_summary(self, diff: str) -> str:
        """Gets a combined summary of the diff by summarizing chunks of the diff."""
        max_size = self.chunk_size * 5
        summaries = [
            self._summarize_chunk(diff[i : i + self.chunk_size])
            for i in range(0, len(diff[:max_size]), self.chunk_size)
        ]
        combined_summary = " ".join(summaries)
        return combined_summary

    def _summarize_chunk(self, chunk: str) -> str:
        """Summarizes a chunk of code using the OpenAI API."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {"role": "user", "content": self.content["summarize_request"] + chunk}
            ],
            max_tokens=500,
            temperature=0.5,
            top_p=0.5,
        )
        return response.choices[0].message.content
