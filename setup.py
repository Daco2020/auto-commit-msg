from setuptools import setup

setup(
    name="auto-commit-msg",
    py_modules=["main", "commit_msg_generator", "config"],
    entry_points={
        "console_scripts": ["auto-commit-msg=main:run"],
    },
    install_requires=["openai==0.27.8", 'subprocess32; python_version<"3.0"'],
)
