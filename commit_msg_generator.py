# commit_msg_generator.py

import openai

from config import (
    CHUNK_SIZE,
    COMMIT_CONVENTION,
    COMMIT_LANGUAGE,
    OPENAI_API_KEY,
    OPENAI_MODEL,
)


class CommitMessageGenerator:
    def __init__(
        self,
    ) -> None:
        openai.api_key = OPENAI_API_KEY
        self.model = OPENAI_MODEL
        self.commit_convention = COMMIT_CONVENTION
        self.commit_language = COMMIT_LANGUAGE
        self.chunk_size = CHUNK_SIZE

    def generate_commit_message(self, diff: str) -> str:
        """Generates a commit message based on the diff provided."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=self._build_messages(diff[: self.chunk_size]),
            max_tokens=500,
            temperature=0.4,
            top_p=0.4,
        )
        return response.choices[0].message.content

    def _build_messages(self, diff: str) -> list:
        """Builds a list of messages to send to the OpenAI API."""
        messages = [
            {
                "role": "user",
                "content": f"You are an expert in writing commit messages. Please review the modified code I'm providing, and answer with just the commit message title, following this regular expression: {self.commit_convention}",
            },
            {
                "role": "assistant",
                "content": f"Yes, I understand. I will definitely answer with just the commit message title, following the format {self.commit_convention}.",
            },
        ]

        if len(diff) > self.chunk_size:
            summaries = [
                self._summarize_chunk(diff[i : i + self.chunk_size])
                for i in range(0, len(diff), self.chunk_size)
            ]
            combined_summary = " ".join(summaries)
            messages.append(
                {
                    "role": "user",
                    "content": f"Please write a commit message title based on the following summary:\n{combined_summary}, following the format {self.commit_convention}.",
                }
            )
        else:
            answer_language = self._get_answer_language(self.commit_language)
            messages.append(
                {
                    "role": "user",
                    "content": f"Below is the modified code. {diff}\n\n Please provide just the commit message title in {answer_language}, following the format {self.commit_convention}.",
                }
            )

        return messages

    def _summarize_chunk(self, chunk: str) -> str:
        """Summarizes a chunk of code using the OpenAI API."""
        response = openai.ChatCompletion.create(
            model=self.model,
            messages=[
                {
                    "role": "user",
                    "content": f"Please summarize the following text in 3 lines:\n{chunk}",
                }
            ],
            max_tokens=500,
            temperature=0.4,
            top_p=0.4,
        )
        return response.choices[0].message.content

    def _get_answer_language(self, language: str) -> str:
        """Returns the language to use for the commit message answer."""
        return {
            "en": "Please answer in English.",
            "ko": "한국어로 답변해주세요.",
            "cn": "请用中文回答。",
            "jp": "日本語でお答えください。",
        }.get(language, "Please answer in English.")
