from setuptools import setup
import os

VERSION = "0.0.2"


def get_long_description():
    with open(
        os.path.join(os.path.dirname(os.path.abspath(__file__)), "README.md"),
        encoding="utf8",
    ) as fp:
        return fp.read()


setup(
    name="spotify-album-cards",
    description="Create printable and scannable cards for albums on Spotify",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Kevin Schaul",
    url="https://github.com/kevinschaul/spotify-album-cards",
    project_urls={
        "Issues": "https://github.com/kevinschaul/spotify-album-cards/issues",
        "CI": "https://github.com/kevinschaul/spotify-album-cards/actions",
        "Changelog": "https://github.com/kevinschaul/spotify-album-cards/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["spotify_album_cards"],
    entry_points="""
        [console_scripts]
        spotify-album-cards=spotify_album_cards.cli:cli
    """,
    install_requires=["click", "spotipy", "python-dotenv", "Pillow", "requests"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.6",
)
