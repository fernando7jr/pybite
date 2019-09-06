"""Open a file or return an io.StringIO if it is already open"""

def _open_file(file_stream, mode: str, encoding=None, **kwargs):
    """Open a file if it is a file_name otherwise return file_stream"""

    if type(file_stream) is str:
        return open(file_stream, mode, encoding=encoding, **kwargs)
    return file_stream
