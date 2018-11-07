#!/usr/bin/env python

from utils import open_and_read
from bs4 import BeautifulSoup
import requests, cli.app

@cli.app.CommandLineApp
def main(app):
    filename = app.params.filename
    hyperLinks = open_and_read(filename)
    print(hyperLinks)

main.add_param(
    "filename",
    help="A file of wikipedia page links separated by newlines")


if __name__ == '__main__':
    main.run()
