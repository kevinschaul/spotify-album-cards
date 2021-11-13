from dotenv import load_dotenv
from spotipy.oauth2 import SpotifyOAuth
import click
import csv
import os
import spotipy

load_dotenv()

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
    click.echo(f"Downloading your Spotify album data")

    n_written = 0
    with open(output, 'w') as f:
        writer = csv.writer(f)
        writer.writerow(['uri', 'artist', 'name'])

        scope = "user-library-read"
        auth_manager = SpotifyOAuth(
            scope=scope,
            client_id=os.environ['SPOTIFY_CLIENT_ID'],
            client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
            redirect_uri=os.environ['SPOTIFY_REDIRECT_URI'],
        )
        sp = spotipy.Spotify(auth_manager=auth_manager)

        albums = sp.current_user_saved_albums()
        while albums:
            for i, album in enumerate(albums['items']):
                writer.writerow([
                    album['album']['uri'],
                    album['album']['name'],
                    ', '.join([artist['name'] for artist in album['album']['artists']])
                ])
                n_written += 1
            if albums['next']:
                albums = sp.next(albums)
            else:
                albums = None
    click.echo(f"Wrote {n_written} rows to {output}")

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
