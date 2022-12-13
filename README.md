# docmystuff

[![PyPI](https://img.shields.io/pypi/v/docmystuff.svg)](https://pypi.org/project/docmystuff/)
[![Changelog](https://img.shields.io/github/v/release/realbazso/docmystuff?include_prereleases&label=changelog)](https://github.com/realbazso/docmystuff/releases)
[![Tests](https://github.com/realbazso/docmystuff/workflows/Test/badge.svg)](https://github.com/realbazso/docmystuff/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/realbazso/docmystuff/blob/master/LICENSE)

Create structured explanation document in Markdown for code folders using ChatGPT.

---
**NOTE**: 
Under development, not ready for use yet.

---

## Installation

Install this tool using `pip`:

    pip install docmystuff

### Obtain API key

The application is using OpenAI ChatGPT, which requires an API key. You can get one from <https://beta.openai.com/account/api-keys>. Put it into a file.

### Alternative solution: Obtaining the session token

Go to <https://chat.openai.com/chat> and log in or sign up.
Open the developer tools in your browser.
Go to the Application tab and open the Cookies section.
Copy the value for __Secure-next-auth.session-token and save it.
Once you have obtained a session token, you can configure the extension to use it as described in the previous section.
Credit: <https://github.com/mpociot/chatgpt-vscode#obtaining-the-session-token>

## Usage

For help, run:

    docmystuff --help

You can also use:

    python -m docmystuff --help

Example usage:

    docmystuff generate -k <your-key-file> -o <output-file> INPUT_FOLDER

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd docmystuff
    python -m venv venv
    source venv/bin/activate

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest

---

Credit for boilerplate: <https://github.com/simonw/click-app>

