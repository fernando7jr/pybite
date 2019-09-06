"""Chunk by chunk iteration made easier"""


def __map_same(x):
    return x


def __gen(iterable: iter, count: int, _map=None, header=None):
    def _make_chunk():
        if header is not None:
            return [header]
        return []
    
    def _chunk_len():
        l = len(buffer)
        return l - 1 if header is not None else l

    buffer = _make_chunk()
    if _map is None:
        _map = __map_same
    for item in iterable:
        _len = _chunk_len()
        if _len == count:
            yield buffer
            buffer = _make_chunk()
        buffer.append(_map(item))
    if _chunk_len() > 0:
        yield buffer


def iterate_by(iterable: iter, chunk_size: int, map=None,
persist_header=False, header=None) -> iter:
    """
    Return a iterator of chunks for the iterable.

    A new iterable is formed from the passed data and divided in chunks.
    Each chunk is generated on-demand and its size will be chunk_size or less
    in case there is not enough data to fill it.
    In case persist_header is True, the size of each chunk will be increased by 1.

    Parameters
    ----------
    iterable : iter
        Any iterable data e.g. list, tuple, dict, iter, ...
    chunk_size : int
        The size of each chunk
    map : callable optional, defaults None
        A map function for transform the data before dividing in chunks
    persist_header : bool optional, defaults False
        Whether to persist a header on each chunk or not. 
        If persist_header is True and header is None, 
        the firt line will be read as the actual header.
    header : str optional, defaults None
        A header to be written at the start of each file.
        If persist_header is True and header is None, 
        the firt line will be read as the actual header.
    Returns
    -------
    iter
        New iterable for the chunked data
    Examples
    --------
    >>> iterate_by([1, 2, 3, 4, 5], 2)
    iter([1, 2], [3, 4], [5])
    >>> iterate_by([1, 2, 3, 4, 5], 2, map=lambda x: x * 2)
    iter([2, 4], [6, 8], [10])
    >>> iterate_by(["numbers", 1, 2, 3, 4, 5], 2, persist_header=True)
    iter(["numbers", 2, 4], ["numbers", 6, 8], ["numbers", 10])
    """
    if persist_header is True:
        if header is None:
            iterable = iter(iterable)
            header = iterable.__next__()
    return __gen(iterable, chunk_size, _map=map, header=header)
