from setuptools import setup
import os

VERSION = "0.1"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="docmystuff",
    description="Create structured explanation document in Markdown for code folders using ChatGPT",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Zsolt Balog",
    url="https://github.com/realbazso/docmystuff",
    project_urls={
        "Issues": "https://github.com/realbazso/docmystuff/issues",
        "CI": "https://github.com/realbazso/docmystuff/actions",
        "Changelog": "https://github.com/realbazso/docmystuff/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["docmystuff"],
    entry_points="""
        [console_scripts]
        docmystuff=docmystuff.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.7",
)
