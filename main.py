#!/usr/bin/env python

from utils import open_and_read, request_html_for
from utils import get_citation_format_from
from bs4 import BeautifulSoup as bSoup
import cli.app

@cli.app.CommandLineApp
def main(app):
    baseURL = 'https://en.wikipedia.org'
    # Store hyperlink sitations as key value pairs with the link
    # being the key.
    hyperlinksCitations = {}
    citationFormats = app.params.citationFormats.split(' ')
    filename = app.params.filename

    # Get hyperlinks from file and store in a list
    hyperlinks = [x.strip() for x in open_and_read(filename)]

    # iterate through hyperLinks and retrieve citations
    for hyperlink in hyperlinks:
        mainPageSoup = bSoup(request_html_for(hyperlink), 'html.parser')

        # retrieve citation page hyperlink
        citationPageHyperlink = baseURL + mainPageSoup.find(
            'a',
            title='Information on how to cite this page')['href'].strip()

        # retrieve citation page soup
        citationPageSoup = bSoup(
            request_html_for(citationPageHyperlink),
            'html.parser')

        for citation_format in citationFormats:
            key = mainPageSoup.title.text
            citation = get_citation_format_from(
                citationPageSoup,
                citation_format)
            if not key in hyperlinksCitations:
                hyperlinksCitations[key] = [citation]
            else:
                hyperlinksCitations[key].append(citation)

        # Map citation formats to hyperlinksCitations
    print('finished with: ', hyperlinksCitations)


main.add_param(
    'filename',
    help='A file of wikipedia page links separated by newlines')
main.add_param(
    'citationFormats',
    help='A list of citation formats separated by commas.')


if __name__ == '__main__':
    main.run()
