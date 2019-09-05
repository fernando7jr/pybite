"""Open a file or return an io.StringIO if it is already open"""

def _open_file(file_stream, encoding=None):
    """Open a file if it is a file_name otherwise return file_stream"""

    if type(file_stream) is str:
        return open(file_stream, "r", encoding=encoding)
    return file_stream
