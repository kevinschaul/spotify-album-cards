from PIL import Image
from requests.api import get
from dotenv import load_dotenv
from io import BytesIO
from spotipy.oauth2 import SpotifyOAuth
import click
import csv
import math
import os
import requests
import spotipy

load_dotenv()

PPI = 300

def pluralize(n):
    """
    Returns "s" if n is not exactly 1
    """
    if n == 1:
        return ""
    else:
        return "s"

def get_spotipy_client():
    scope = "user-library-read"
    auth_manager = SpotifyOAuth(
        scope=scope,
        client_id=os.environ['SPOTIFY_CLIENT_ID'],
        client_secret=os.environ['SPOTIFY_CLIENT_SECRET'],
        redirect_uri=os.environ['SPOTIFY_REDIRECT_URI'],
    )
    return spotipy.Spotify(auth_manager=auth_manager)

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

        sp = get_spotipy_client()
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

    album_uris = []
    with open(input) as i:
        reader = csv.DictReader(i)
        for row in reader:
            album_uris.append(row['uri'])

    n_albums = len(album_uris)
    albums_per_print = 4
    n_prints = math.ceil(n_albums / albums_per_print)
    click.echo(f"Generating {n_prints} print{pluralize(n_prints)} from {n_albums} album{pluralize(n_albums)}")

    # Create output directory
    try:
        os.mkdir(output)
    except FileExistsError:
        pass

    for i in range(0, n_prints):
        start = i * albums_per_print
        stop = start + albums_per_print
        print(f"Generating print {i+1} of {n_prints}")
        image = generate_print(album_uris[start:stop])
        filepath = os.path.join(output, f"{i:04}.jpg")
        image.save(filepath)
        print(f"Saved to {filepath}")

def generate_print(uris):
    """
    Generate image data for printing up to four albums
    """
    width = 4*PPI
    height = 6*PPI
    composite = Image.new('RGB', (width, height), '#ffffff')
    for i in range(0, 4):
        if i < len(uris):
            x = round(width/2 * (i % 2))
            y = round(height/2 * math.floor(i / 2))
            image = generate_single_album(uris[i])
            composite.paste(image, (x, y))
    return composite

def generate_single_album(uri):
    """
    Generate image data for printing a single album, based on its uri
    """

    # Download the album artwork
    sp = get_spotipy_client()
    album = sp.album(uri)
    art_url = album['images'][0]['url']
    art_r = requests.get(art_url)
    art_image = Image.open(BytesIO(art_r.content))

    # Download the Spotify code image for this album
    # This url structure obtained from https://spotifycodes.com/
    code_url = f"https://scannables.scdn.co/uri/plain/jpeg/ffffff/black/640/{uri}"
    code_r = requests.get(code_url)
    code_image = Image.open(BytesIO(code_r.content))

    # Create a new image 2 in by 3 in
    width = 2*PPI
    height = 3*PPI
    print_image = Image.new('RGB', (width, height), '#ffffff')

    # Album art should take up the full width, and is always a square
    art_image_resized = art_image.resize((width, width))
    print_image.paste(art_image_resized, (0, 0))

    # Spotify code image should take up 1/4 in vertically
    code_image_resized = code_image.resize((
        round(code_image.size[0] * PPI/4 / code_image.size[1]),
        round(PPI/4)
    ))
    print_image.paste(code_image_resized, (
        round((width - code_image_resized.size[0]) / 2),
        round(2*PPI + (PPI - code_image_resized.size[1]) / 2))
    )

    return print_image
