# spotify-album-cards

[![PyPI](https://img.shields.io/pypi/v/spotify-album-cards.svg)](https://pypi.org/project/spotify-album-cards/)
[![Changelog](https://img.shields.io/github/v/release/kevinschaul/spotify-album-cards?include_prereleases&label=changelog)](https://github.com/kevinschaul/spotify-album-cards/releases)
[![Tests](https://github.com/kevinschaul/spotify-album-cards/workflows/Test/badge.svg)](https://github.com/kevinschaul/spotify-album-cards/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/kevinschaul/spotify-album-cards/blob/master/LICENSE)

Create printable and scannable cards for albums on Spotify. Print these images, and scan them with your Spotify app to open up the album.

## Installation

Install this tool using `pip`:

    pip install spotify-album-cards

Create a Spotify app [here](https://developer.spotify.com/dashboard/). Set the redirect URI to be `http://127.0.0.1:9090`.

Create a `.env` file containing your Spotify app's Client ID, Client Secret and redirect URI as follows:

```
SPOTIFY_CLIENT_ID='your-spotify-client-id'
SPOTIFY_CLIENT_SECRET='your-spotify-client-secret'
SPOTIFY_REDIRECT_URI=http://127.0.0.1:9090
```

## Usage

`spotify-album-cards` provides two commands that are meant to be run in order.

### `get-albums`

Downloads all albums from your Spotify account, outputting a csv file.

Usage:

    spotify-album-cards get-albums -o albums.csv

Once downloaded, manually edit the resulting csv file to only include rows for albums that you would like to generate prints for.

### `generate-prints`

Generates images from an albums csv file. Currently creates images suitable for printing on 4x6 paper, with up to six albums per card.

Usage:

    spotify-album-cards generate-prints -i albums.csv -o prints

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd spotify-album-cards
    python -m venv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
