"""File spliting, separation and joining"""
import os
from .iterate import iterate_by


def __line_generator(f):
    while True:
        line = f.readline()
        if not line:
            break
        yield line


def __ensure_dir(path: str):
    os.makedirs(path, exist_ok=True)
    return os.path.relpath(path)


def __get_file_name(file_name: str, chunk: int, ext: str, chunk_format=None):
    if chunk_format is None:
        chunk_format = "{0:04d}"
    chunk_format = f"{{0:{chunk_format}}}"
    file_name = f"{file_name}.chunk{chunk_format}{ext}"
    return file_name.format(chunk)


def split_by_lines(
    file_stream, output_path: str, lines: int, 
    encoding=None, persist_header=False, header=None,
    chunk_name_format="04d") -> list:
    """
    Split a file into multiple files and store them in the output path.

    The file is divided b lines into chunk files that later can be read individually
    or joined back.

    Parameters
    ----------
    file_stream : str, io.StringIO
        A file path or io.StringIO instance to the file you want to split.
    output_path : str
        The path to the directory where the chunks will be stored.
    lines : int
        The quantity of lines on each chunk file. 
        If included the header the total will be lines + 1.
    encoding : str optional, defaults None
        The input file encoding. 
        The chunks will be saved using the same encoding.
    persist_header : bool optional, defaults False
        Whether to persist a header on each chunk or not. 
        If persist_header is True and header is None, 
        the firt line will be read as the actual header.
    header : str optional, defaults None
        A header to be written at the start of each file.
        If persist_header is True and header is None, 
        the firt line will be read as the actual header.
    chunk_name_format : str optional, defaults "04d"
        The format string for the chunk numbers in the output file names.
    Returns
    -------
    list
        List of paths to the written files.
    Examples
    --------
    with open("test.txt", "w", encoding="utf-8") as f:
        f.write("Symbols\nAyp\nBx\nCC\nDt")
    
    >>> split_by_lines("test.txt", "out", 2, encoding="utf-8")
    ["out/test.chunk0000.txt", "out/test.chunk0001.txt", 
    "out/test.chunk0002.txt"]
    >>> split_by_lines("test.txt", "out", 2, encoding="utf-8", 
    persist_header=True)
    ["out/test.chunk0000.txt", "out/test.chunk0001.txt"]
    """

    if type(file_stream) is str:
        file_stream = open(file_stream, "r", encoding=encoding)
    
    if persist_header is True and header is None:
        header = file_stream.readline()
    
    # Prepare the output_path for later
    output_path = __ensure_dir(output_path)
    output_base_name = os.path.split(file_stream.name)[1]
    output_base_name, output_base_ext = os.path.splitext(output_base_name)
    if output_base_ext:
        output_base_ext = "." + output_base_ext
    
    # Transform chunk_name_format into a format string
    chunk_name_format = f"{{0:{chunk_name_format}}}"
    
    chunk_id = 0
    chunk_files = []
    lines_gen = __line_generator(file_stream)
    for chunk in iterate_by(lines_gen, lines):
        # Generate the chunk_name
        chunk_name = __get_file_name(output_base_name, chunk_id, output_base_ext, 
        chunk_format=chunk_name_format)
        print(chunk_name, lines, chunk)

        # Join with the output_path and write the chunk
        output_file_name = os.path.join(output_path, chunk_name)
        output_stream = open(output_file_name, "w", encoding=encoding)
        if persist_header is True and header is not None:
            output_stream.write(header)
        output_stream.write("".join(chunk))
        output_stream.close()
        chunk_id += 1
        chunk_files.append(output_file_name)
    file_stream.close()
    return chunk_files
