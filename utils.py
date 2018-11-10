import requests


def open_and_read(file):
    """
    Opens a file and returns a list of the files lines.
    """
    assert type(file) == str
    print('file: ', file)
    try:
        with open(file, 'r') as fileData:
            return fileData.readlines()
    except IOError as e:
        print("Error: cant\'t find or read file: ", e)


def request_html_for(url):
    """
    Gets text response from request made to the 'url'.
    """
    print('html requested for: ', url)
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        print('Could not make request because of: ', e)


def get_citation_format_from(soup, citation_format):
    """
    Returns a citation string with the given citation_format
    for the given soup
    """
    try:
        return soup.find(id=citation_format).parent.findNextSibling('p').text
    except e:
        print('Something went wrong while searching citationPageSoup', e)
