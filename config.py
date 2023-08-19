import os

# openai
OPENAI_API_KEY = os.environ.get("OPENAI_API_KEY")
OPENAI_MODEL = os.environ.get("OPENAI_MODEL", "gpt-3.5-turbo")
CHUNK_SIZE = 5000

# language
COMMIT_LANGUAGE = os.environ.get("COMMIT_LANGUAGE", "en")

# convention
COMMIT_CONVENTION = os.environ.get("COMMIT_CONVENTION", "")

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

echo -n > "$0"
"""

# These are contents used for the OpenAI API.
CONTENTS = {
    "en": {
        "code_diff": "Below is the modified code:\n",
        "instruction_request": "You are an expert in writing commit messages. Please review the modified code I'm providing, and answer with just the commit message title\n",
        "summarize_request": "Please summarize the following text in 3 lines:\n",
        "commit_msg_request": "Please write a commit message title based on the following summary:\n",
        "convention_request": f"following the format {COMMIT_CONVENTION}"
        if COMMIT_CONVENTION
        else "",
        "answer_language": "Please answer in English.\n",
    },
    "ko": {
        "code_diff": "아래는 수정된 코드입니다:\n",
        "instruction_request": "당신은 커밋 메시지 작성 전문가입니다. 제공하는 수정된 코드를 검토하고 커밋 메시지 제목만 답해주세요.\n",
        "summarize_request": "다음 텍스트를 3줄로 요약해주세요:\n",
        "commit_msg_request": "다음 요약을 기반으로 커밋 메시지 제목을 작성해주세요:\n",
        "convention_request": f"{COMMIT_CONVENTION} 형식에 맞춰 작성해주세요\n"
        if COMMIT_CONVENTION
        else "",
        "answer_language": "한국어로 답변해주세요.\n",
    },
    "cn": {
        "code_diff": "以下是修改后的代码:\n",
        "instruction_request": "你是编写提交信息的专家。请审查我提供的修改后的代码，并只回答提交消息的标题\n",
        "summarize_request": "请在3行内总结以下文本:\n",
        "commit_msg_request": "请根据以下摘要编写提交消息标题:\n",
        "convention_request": f"遵循{COMMIT_CONVENTION}格式\n" if COMMIT_CONVENTION else "",
        "answer_language": "请用中文回答。\n",
    },
    "jp": {
        "code_diff": "以下は修正されたコードです:\n",
        "instruction_request": "あなたはコミットメッセージの専門家です。提供する修正されたコードをレビューし、コミットメッセージのタイトルのみ回答してください。\n",
        "summarize_request": "以下のテキストを3行で要約してください:\n",
        "commit_msg_request": "以下の要約に基づいてコミットメッセージのタイトルを書いてください:\n",
        "convention_request": f"{COMMIT_CONVENTION}形式に従ってください\n"
        if COMMIT_CONVENTION
        else "",
        "answer_language": "日本語でお答えください。\n",
    },
}
DEFAULT_CONTENT = {
    "code_diff": "Below is the modified code:\n",
    "instruction_request": "You are an expert in writing commit messages. Please review the modified code I'm providing, and answer with just the commit message title",
    "summarize_request": "Please summarize the following text in 3 lines:\n",
    "commit_msg_request": "Please write a commit message title based on the following summary:\n",
    "convention_request": f"following the format {COMMIT_CONVENTION}"
    if COMMIT_CONVENTION
    else "",
    "answer_language": "Please answer in English.\n",
}
