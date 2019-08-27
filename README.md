# PyBite

Chunk by chunk iteration made easier

## Installation

    pip install pybite

## Methods

### iterate_by

Return a iterator of chunks for the iterable

#### Parameters
    
**iterable**: *iter*

Any iterable data e.g. list, tuple, dict, iter, ...

**chunk_size**: *int*

The size of each chunk

**map**: *callable* optional, defaults *None*

A map function for transform the data before dividing in chunks

#### Returns

**iter**
    
New iterable for the chunked data

#### Examples

```python
>>> iterate_by([1, 2, 3, 4, 5], 2)
iter([[1, 2], [3, 4], [5])
>>> iterate_by([1, 2, 3, 4, 5], 2, map=lambda x: x * 2)
iter([[2, 4], [6, 8], [10])
```

### split_by_lines

Split a file into multiple files and store them in the output path.

The file is divided b lines into chunk files that later can be read individually
or joined back.

#### Parameters
    
**file_stream**: *str*, *io.StringIO*

A file path or io.StringIO instance to the file you want to split.

**output_path**: *str*

The path to the directory where the chunks will be stored.

**lines**: *int*

The quantity of lines on each chunk file. 
If included the header the total will be lines + 1.

**encoding**: *str* optional, defaults *None*

The input file encoding. 
The chunks will be saved using the same encoding.

**persist_header**: *bool* optional, defaults *False*

Whether to persist a header on each chunk or not. 
If persist_header is True and header is None, 
the firt line will be read as the actual header.

**header**: *str* optional, defaults *None*

A header to be written at the start of each file.
If persist_header is True and header is None, 
the firt line will be read as the actual header.

**chunk_name_format**: *str* optional, defaults *"04d"*

The format string for the chunk numbers in the output file names.

#### Returns

**list**
    
List of paths to the written files.

#### Examples

```python
with open("test.txt", "w", encoding="utf-8") as f:
    f.write("Symbols\nAyp\nBx\nCC\nDt")

>>> split_by_lines("test.txt", "out", 2, encoding="utf-8")
["out/test.chunk0000.txt", "out/test.chunk0001.txt", 
"out/test.chunk0002.txt"]
>>> split_by_lines("test.txt", "out", 2, encoding="utf-8", 
persist_header=True)
["out/test.chunk0000.txt", "out/test.chunk0001.txt"]
```

### join_file_chunks

Join chunk files into a single line stream.

Join the files created by split_by_lines into a iterable of
str lines and read ordered by name. 
Chunks not found will throw an error if ignore_missing_chunks is not False.

Avoid saving different files chunks into the same directory.

#### Parameters

**files_path**: *str*

The path to a directory containing the chunk files or a list of the path to the files.

**encoding**: *str* optional, defaults *None*

The input file encoding. 
The chunks will be saved using the same encoding.

**persisted_header**: *bool* optional, defaults *False*

Whether a header was persisted on each chunk or not. 
If persisted_header is True and header is None, 
the firt line of teh first file will be read as the actual header.

**header**: *str* optional, defaults *None*

A header to be read at the start of the first file.
If persisted_header is True and header is None, 
the firt line of teh first file will be read as the actual header.

**ignore_missing_chunks**: *bool* optional, defaults *"False*

Flag to ignore missing chunks.

#### Returns

**iter**
    
An iterable to the lines of the files (read in the order).

## Test

Test are handled by [PyTest](https://pypi.org/project/pytest/) and are included inside the folder `test`.

To run the test execute the command:
    
    pytest
