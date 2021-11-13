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
    name="scanify",
    description="Create printable and scannable cards for albums on Spotify",
    long_description=get_long_description(),
    long_description_content_type="text/markdown",
    author="Kevin Schaul",
    url="https://github.com/kevinschaul/scanify",
    project_urls={
        "Issues": "https://github.com/kevinschaul/scanify/issues",
        "CI": "https://github.com/kevinschaul/scanify/actions",
        "Changelog": "https://github.com/kevinschaul/scanify/releases",
    },
    license="Apache License, Version 2.0",
    version=VERSION,
    packages=["scanify"],
    entry_points="""
        [console_scripts]
        scanify=scanify.cli:cli
    """,
    install_requires=["click"],
    extras_require={
        "test": ["pytest"]
    },
    python_requires=">=3.6",
)
