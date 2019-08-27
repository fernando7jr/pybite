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

```
>>> iterate_by([1, 2, 3, 4, 5], 2)
iter([[1, 2], [3, 4], [5])
>>> iterate_by([1, 2, 3, 4, 5], 2, map=lambda x: x * 2)
iter([[2, 4], [6, 8], [10])
```

### 