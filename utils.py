import requests


def open_and_read(file):
    """
    Opens a file and returns a list of the files lines.
    """
    try:
        with open(file, 'r') as fileData:
            return fileData.readlines()
    except IOError:
        print("Error: cant\'t find or read file")


def get_html_from(url):
    """
    Gets text response from request made to the 'url'.
    """
    try:
        response = requests.get(url)
        return response.text
    except requests.exceptions.RequestException as e:
        print('Could not make request because of: ', e)
