from pybite import iterate_by


test_data = [
    chr(i)
    for i in range(ord("A"), ord("Z") + 1)
]


def test_iterate_by():
    iter_data = list(iterate_by(test_data, 4))
    for i in range(0, 4):
        test_data_chunk = "".join(test_data[i*4:(i+1)*4])
        iter_data_chunk = "".join(iter_data[i])
        assert test_data_chunk == iter_data_chunk
