"""Utilities for iterating files"""
from ._open import _open_file


def iterate_file_by_lines(file_stream, encoding=None, strip_end=False):
    """
    Return a iterator of file lines.

    Each line is read on-demand untill there is no more line to
    be read.

    Parameters
    ----------
    file_stream : str, io.StringIO
        A file path or io.StringIO instance to the file to be read.
    encoding : str optional, defaults None
        The input file encoding. 
        The chunks will be saved using the same encoding.
    strip_end : bool optional, defaults False
        Flag for strip the end of each line.
        Same as calling `line.rstrip()`.
    Returns
    -------
    iter
        A iterable for the file lines.
    Examples
    --------
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Symbols\nAyp\nBx\nCC\nDt")
    
    >>> iterate_file_by_lines("test.txt", encoding="utf-8")
    iter("Symbols\n", "Ayp\n", "Bx\n", "CC\n", "Dt")
    >>> iterate_file_by_lines("test.txt", encoding="utf-8", strip_end=True)
    iter("Symbols", "Ayp", "Bx", "CC", "Dt")
    """
    file_stream = _open_file(file_stream, "r", encoding=encoding)
    while True:
        line = file_stream.readline()
        if not line:
            break
        yield line if strip_end is False else line.rstrip()
    file_stream.close()
