from setuptools import setup, find_packages

setup(
    name="auto-commit-msg",
    packages=find_packages(),
    install_requires=["openai", 'subprocess32; python_version<"3.0"'],
    entry_points={
        "console_scripts": [
            "auto-commit-msg=auto_commit_msg:main",
        ],
    },
)
