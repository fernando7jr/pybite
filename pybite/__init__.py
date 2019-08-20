"""Chunk by chunk iteration made easier"""


def __map_same(x):
    return x


def __gen(iterable: iter, count: int, _map=None):
    buffer = []
    _len = 0
    if _map is None:
        _map = __map_same
    for item in iterable:
        if _len == count:
            yield buffer
            _len = 0
            buffer = []
        else:
            buffer.append(_map(item))
            _len += 1
    if _len > 0:
        yield buffer


def iterate_by(iterable: iter, chunk_size: int, map=None) -> iter:
    """
    Return a iterator of chunks for the iterable

    A new iterable is formed from the passed data and divided in chunks.
    Each chunk is generated on-demand and its size will be chunk_size or less
    in case there is not enough data to fill it.

    Parameters
    ----------
    iterable : iter
        Any iterable data e.g. list, tuple, dict, iter, ...
    chunk_size : int
        The size of each chunk
    map : callable optional, defaults None
        A map function for transform the data before dividing in chunks
    Returns
    -------
    iter
        New iterable for the chunked data
    Examples
    --------
    >>> iterate_by([1, 2, 3, 4, 5], 2)
    iter([[1, 2], [3, 4], [5])
    >>> iterate_by([1, 2, 3, 4, 5], 2, map=lambda x: x * 2)
    iter([[2, 4], [6, 8], [10])
    """
    return __gen(iterable, chunk_size, _map=map)
