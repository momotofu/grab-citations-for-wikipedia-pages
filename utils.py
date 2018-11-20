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
        citation_header = soup.find(id=citation_format)
        if citation_header is None:
            raise Exception('MLA format doesn\'t match the html header id')
        else:
            return citation_header.parent.findNextSibling('p').text
    except Exception as e:
        print('Something went wrong while searching citationPageSoup Error: ', e)

def format_citation_for(title, hyperlink, citations, citation_formats):
    """
    Takes a hyperlink string and a citation list; which are then
    formated into a readable string. That string is then written to
    the file provided.
    """
    citation_format_titles = [' '.join(x.split('_')).title() for x in citation_formats]
    formated_text = '#' * 2 + ' ' + title + '\n'
    formated_text += hyperlink + '\n'
    # import pdb
    # pdb.set_trace()

    for index, citation  in enumerate(citations):
        formated_text += '#' * 4 + ' ' + citation_format_titles[index] + '\n'
        formated_text += citation + '\n'

    formated_text += '\n' # Add a single space between each citation
    return formated_text
