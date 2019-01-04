#!/usr/bin/env python
"""
The goals of this webcrawler application are as follows:
1. Fetch citation formats for each link supplied in a text file.
2. Neatly print citation formats and corresponding links (from supplied
text file) to a markdown file.

Helper request functions can be found in utils.py
"""

from utils import open_and_read, request_html_for
from utils import get_citation_format_from, format_citation_for
from bs4 import BeautifulSoup as bSoup
import cli.app


@cli.app.CommandLineApp
def main(app):
    """
    CommandLineApp which opens a supplied text file, and then crawls wikipedia
    until relavant citation formats are found. The citation formats and links
    are then printed to a markdown file.
    """

    base_url = 'https://en.wikipedia.org'
    # Store hyperlink sitations as key value pairs with the link
    # being the key.
    hyperlink_citations = {}
    citation_formats = app.params.citation_formats.split(' ')
    file_name = app.params.file_name

    # Get hyperlinks from file and store in a list
    hyperlinks = [x.strip() for x in open_and_read(file_name)]

    # iterate through hyperLinks and retrieve citations
    for hyperlink in hyperlinks:
        main_page_soup = bSoup(request_html_for(hyperlink), 'html.parser')

        # retrieve citation page hyperlink
        citation_page_hyperlink = base_url + main_page_soup.find(
            'a',
            title='Information on how to cite this page')['href'].strip()

        # retrieve citation page soup
        citation_page_soup = bSoup(
            request_html_for(citation_page_hyperlink),
            'html.parser')

        for citation_format in citation_formats:
            key = main_page_soup.title.text
            citation = get_citation_format_from(
                citation_page_soup,
                citation_format)
            if key not in hyperlink_citations:
                hyperlink_citations[key] = {
                    'hyperlink': hyperlink,
                    'citations': [citation]
                }
            else:
                hyperlink_citations[key]['citations'].append(citation)

    with open('citedLinks.md', 'w') as output_file:
        output_file.write('# Citations For Links')
        output_file.write('\n')
        output_file.write('\n')
        for key in hyperlink_citations:
            page_data = hyperlink_citations[key]
            output_file.write(
                format_citation_for(key, page_data, citation_formats))


main.add_param(
    'file_name',
    help='A file of wikipedia page links separated by newlines')
main.add_param(
    'citation_formats',
    help='A list of citation formats separated by commas.')


if __name__ == '__main__':
    main.run()
