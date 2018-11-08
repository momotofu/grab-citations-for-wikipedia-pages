#!/usr/bin/env python

from utils import open_and_read, request_html_for
from bs4 import BeautifulSoup as bSoup
import cli.app

@cli.app.CommandLineApp
def main(app):
    # Store hyperlink sitations as key value pairs with the link
    # being the key.
    hyperlinksCitations = {}

    # Get hyperlinks from file and store in a list
    filename = app.params.filename
    hyperlinks = open_and_read(filename)

    # iterate through hyperLinks and retrieve citations
    for hyperlink in hyperlinks:
        mainPageSoup = bSoup(request_html_for(hyperlink), 'html.parser')

        # retrieve citation page hyperlink
        citationPageHyperlink = mainPageSoup.find(
            'a',
            title='Information on how to cite this page')['href']

        # retrieve citation page soup
        citationPageSoup = bSoup(
            request_html_for(citationPageHyperlink),
            'html.parse')

        # Map citation formats to hyperlinksCitations


main.add_param(
    "filename",
    help="A file of wikipedia page links separated by newlines")


if __name__ == '__main__':
    main.run()
