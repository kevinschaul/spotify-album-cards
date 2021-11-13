# scanify

[![PyPI](https://img.shields.io/pypi/v/scanify.svg)](https://pypi.org/project/scanify/)
[![Changelog](https://img.shields.io/github/v/release/kevinschaul/scanify?include_prereleases&label=changelog)](https://github.com/kevinschaul/scanify/releases)
[![Tests](https://github.com/kevinschaul/scanify/workflows/Test/badge.svg)](https://github.com/kevinschaul/scanify/actions?query=workflow%3ATest)
[![License](https://img.shields.io/badge/license-Apache%202.0-blue.svg)](https://github.com/kevinschaul/scanify/blob/master/LICENSE)

Create printable and scannable cards for albums on Spotify. Print these images, and scan them with your Spotify app to open up the album.

## Installation

Install this tool using `pip`:

    pip install scanify

Create a Spotify app [here](https://developer.spotify.com/dashboard/). Set the redirect URI to be `http://127.0.0.1:9090`.

Create a `.env` file containing your Spotify app's Client ID, Client Secret and redirect URI as follows:

```
SPOTIFY_CLIENT_ID='your-spotify-client-id'
SPOTIFY_CLIENT_SECRET='your-spotify-client-secret'
SPOTIFY_REDIRECT_URI=http://127.0.0.1:9090
```

## Usage

`scanify` provides two commands that are meant to be run in order.

### `get-albums`

Downloads all albums from your Spotify account, outputting a csv file.

Usage:

    scanify get-albums -o albums.csv

Once downloaded, manually edit the resulting csv file to only include rows for albums that you would like to generate prints for.

### `generate-prints`

Generates images from an albums csv file. Currently creates images suitable for printing on 4x6 paper, with up to six albums per card.

Usage:

    scanify generate-prints -i albums.csv -o prints

## Development

To contribute to this tool, first checkout the code. Then create a new virtual environment:

    cd scanify
    python -m venv venv
    source venv/bin/activate

Or if you are using `pipenv`:

    pipenv shell

Now install the dependencies and test dependencies:

    pip install -e '.[test]'

To run the tests:

    pytest
