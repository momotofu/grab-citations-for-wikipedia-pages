def open_and_read(file):
    """
    Opens a file and returns a list of the files lines.
    """
    with open(file, 'r') as fileData:
        return fileData.readlines()
