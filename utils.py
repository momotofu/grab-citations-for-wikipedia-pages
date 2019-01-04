import requests
"""
Support methods for main.py
"""


def open_and_read(file):
    """
    Opens a file and returns a list of the files lines.
    """

    assert isinstance(file, str)
    try:
        with open(file, 'r') as file_data:
            return file_data.readlines()

    except IOError as error:
        print("Error: cant\'t find or read file: ", error)


def request_html_for(url):
    """
    Gets text response from request made to the 'url'.
    """

    print('html requested for: ', url)
    try:
        response = requests.get(url)
        return response.text

    except requests.exceptions.RequestException as error:
        print('Could not make request because of: ', error)


def get_citation_format_from(soup, citation_format):
    """
    Returns a citation string with the given citation_format
    for the given soup
    """
    try:
        citation_header = soup.find(id=citation_format)
        if citation_header is None:
            raise Exception('MLA format doesn\'t match the html header id')
        else:
            return citation_header.parent.findNextSibling('p').text
    except Exception as error:
        print('Something went wrong while searching citationPageSoup Error: ',
              error)


def format_citation_for(title, page_data, citation_formats):
    """
    Takes a hyperlink string and a citation list; which are then
    formated into a readable string. That string is then written to
    the file provided.
    """

    citation_format_titles = [' '.join(x.split('_')).title() for x in citation_formats]
    formated_text = '#' * 3 + ' [' + ' '.join(title.split(' ')[:-2]) + ']'
    formated_text += '(' + page_data['hyperlink'] + ')' + '\n'

    for index, citation in enumerate(page_data['citations']):
        formated_text += '#' * 4 + ' ' + citation_format_titles[index] + '\n'
        formated_text += citation + '\n'

    formated_text += '\n'  # Add a single space between each citation
    return formated_text
