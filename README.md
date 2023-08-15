# auto-commit-msg

### Automate Your Commit Messages Like Never Before!

`auto-commit-msg` is a powerful pre-commit hook that auto-generates commit messages using OpenAI's API. Elevate your Git workflow by ensuring consistent and intelligent commit logs in multiple languages. Experience a seamless and efficient development process while bearing a minimal cost for API usage.

### How to use auto-commit-msg with pre-commit

See [pre-commit](https://github.com/pre-commit/pre-commit) for instructions

Add this to your `.pre-commit-config.yaml:`

```yaml
repos:
  - repo: https://github.com/Daco2020/auto-commit-msg.git
    rev: v0.1.1
    hooks:
      - id: "auto-commit-msg"
```

### Required Environment Variables

OPENAI_API_KEY
>Please register your own OpenAI API key in the environment variables.

### Optional Environment Variables

OPENAI_MODEL
>Please specify the OpenAI model you wish to use. The default is "gpt-3.5-turbo".

COMMIT_LANGUAGE
>Set the desired language for the commit message. By default, it's set to English. Korean (ko), Japanese (jp), and Chinese (cn) are also supported.

COMMIT_CONVENTION
>Please specify the desired commit message convention. The default regular expression is as below:
```
DEFAULT_CONVENTION = (
    r'^((revert: ")?(feat|fix|docs|style|refactor|perf|test|ci|build|chore)'
    r"(\(.*\))?!?:\s.{1,50})"
)
```


## License

MIT