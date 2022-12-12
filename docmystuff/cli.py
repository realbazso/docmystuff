import click


@click.group()
@click.version_option()
def cli():
    "Create structured explanation document in Markdown for code folders using ChatGPT"


@cli.command(name="generate")
@click.argument("input", type=click.Path(exists=True), required=True)
@click.option(
    "-k",
    "--key",
    type=click.File('rb'),
    help="ChatGPT session key filename",
)
@click.option(
    "-o",
    "--output",
    type=click.File('wb'),
    help="Filename to output documentation to",
)
@click.option(
    "-l",
    "--language",
    help="Language to generate documentation in",
)
def generate(key, output, language, input):
    "Start document generation"
    click.echo(f"Here is some output: {language}")
