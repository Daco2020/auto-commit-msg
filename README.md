# auto-commit-msg

![](https://i.imgur.com/IedULvJ.gif)
Automatically generate a commit message with just the `git commit` command, without `-m`. No more time wasted on crafting commit messages.
## Automate Your Commit Messages Like Never Before!

`auto-commit-msg` is a powerful pre-commit hook that auto-generates commit messages using OpenAI's API. Elevate your Git workflow by ensuring consistent and intelligent commit logs in multiple languages. Experience a seamless and efficient development process while bearing a minimal cost for API usage.

## How to use auto-commit-msg with pre-commit

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Add this to your `.pre-commit-config.yaml:`

```yaml
repos:
  - repo: https://github.com/Daco2020/auto-commit-msg.git
    rev: v0.1.2
    hooks:
      - id: "auto-commit-msg"
```

## Required Environment Variables

`OPENAI_API_KEY`  
Please register your own OpenAI API key in the environment variables.

## Optional Environment Variables

`OPENAI_MODEL`  
Please specify the OpenAI model you wish to use. The default is "gpt-3.5-turbo".

`COMMIT_LANGUAGE`  
Set the desired language for the commit message. By default, it's set to 'en'(English). 'ko'(Korean), 'jp'(Japanese), and 'cn'(Chinese) are also supported.

`COMMIT_CONVENTION`  
Please specify the desired commit message convention. If you do not provide one, the default will be left blank. 

The example is as below:  
```sh
# Example 1:
COMMIT_CONVENTION="^((revert: \")?(feat|fix|docs|style|refactor|perf|test|ci|build|chore)(\(.*\))?!!?:\s.{1,50})"

# Example 2:
COMMIT_CONVENTION="접두어로 feat, fix, docs, style, refactor, perf, test, ci, build, chore 중 하나를 사용하세요. (예시: feat: 로그인 기능 추가)"
```


## License

MIT

