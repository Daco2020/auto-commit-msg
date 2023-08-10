import subprocess

import openai

from config import (
    COMMIT_CONVENTION,
    CHUNK_SIZE,
    COMMIT_LANGUAGE,
    OPENAI_API_KEY,
    OPENAI_ENGINE,
)


openai.api_key = OPENAI_API_KEY


def main() -> None:
    diff = get_diff()
    commit_message = generate_commit_message(diff)
    print(commit_message)


def get_diff() -> str:
    cmd = ["git", "diff", "HEAD"]
    result = subprocess.run(cmd, capture_output=True, text=True)
    return result.stdout


def generate_commit_message(diff: str) -> str:
    response = openai.ChatCompletion.create(
        model=OPENAI_ENGINE,
        messages=build_messages(diff[:CHUNK_SIZE]),
        max_tokens=500,
        temperature=0.4,
        top_p=0.4,
    )
    return response.choices[0].message.content


def build_messages(diff: str) -> list:
    messages = [
        {
            "role": "user",
            "content": f"You are an expert in writing commit messages. Please review the modified code I'm providing, and answer with just the commit message title, following this regular expression: {COMMIT_CONVENTION}",
        },
        {
            "role": "assistant",
            "content": f"Yes, I understand. I will definitely answer with just the commit message title, following the format {COMMIT_CONVENTION}.",
        },
    ]

    if len(diff) > CHUNK_SIZE:
        summaries = [
            summarize_chunk(diff[i : i + CHUNK_SIZE])
            for i in range(0, len(diff), CHUNK_SIZE)
        ]
        combined_summary = " ".join(summaries)
        messages.append(
            {
                "role": "user",
                "content": f"Please write a commit message title based on the following summary:\n{combined_summary}, following the format {COMMIT_CONVENTION}.",
            }
        )
    else:
        answer_language = get_answer_language(COMMIT_LANGUAGE)
        messages.append(
            {
                "role": "user",
                "content": f"Below is the modified code. {diff}\n\n Please provide just the commit message title in {answer_language}, following the format {COMMIT_CONVENTION}.",
            }
        )

    return messages


def summarize_chunk(chunk: str) -> str:
    response = openai.ChatCompletion.create(
        model=OPENAI_ENGINE,
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


def get_answer_language(language: str) -> str:
    return {
        "en": "Please answer in English.",
        "ko": "영어로 답변해주세요.",
        "cn": "请用英语回答。",
        "jp": "英語でお答えください。",
    }.get(language, "Please answer in English.")


if __name__ == "__main__":
    main()
