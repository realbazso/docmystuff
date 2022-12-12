import click


@click.group()
@click.version_option()
def cli():
    "Create structured explanation document in Markdown for code folders using ChatGPT"


@cli.command(name="generate")
@click.argument(
    "INPUT_FOLDER",
)
@click.option(
    "-k",
    "--key",
    help="ChatGPT session key filename",
)
@click.option(
    "-o",
    "--output",
    help="Filename to output documentation to",
)
@click.option(
    "-l",
    "--language",
    help="Language to generate documentation in",
)
def first_command(ChatGPT_session_key, option):
    "Start document generation"
    click.echo("Here is some output")
