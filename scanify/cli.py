import click


@click.group()
@click.version_option()
def cli():
    "Create printable and scannable cards for albums on Spotify"


@cli.command(name="get-albums")
@click.option(
    "-o",
    "--output",
    help="Output csv file",
    default="albums.csv",
    required=True,
)
def get_albums(output):
    "Downloads all albums from your Spotify account, outputting a csv file"
    click.echo(f"Here is some output {output}")

@cli.command(name="generate-prints")
@click.option(
    "-i",
    "--input",
    help="Input csv file",
    default="albums.csv",
    required=True,
)
@click.option(
    "-o",
    "--output",
    help="Output directory",
    default="prints",
    required=True,
)
def generate_prints(input, output):
    "Generates images from an albums csv file"
    click.echo(f"Input {input}, output {output}")
