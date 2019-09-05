from pybite import iterate_by


test_data = [
    chr(i)
    for i in range(ord("A"), ord("Z") + 1)
]


def test_iterate_by():
    result = list(iterate_by(test_data, 4))
    for i in range(0, 4):
        test_data_chunk = "".join(test_data[i*4:(i+1)*4])
        result_chunk = "".join(result[i])
        assert test_data_chunk == result_chunk


def test_iterate_by_with_header():
    header = "letter"
    result = list(iterate_by(test_data, 4, 
    persist_header=True, header=header))
    for i in range(0, 4):
        test_data_chunk = "".join([header] + test_data[i*4:(i+1)*4])
        result_chunk = "".join(result[i])
        assert test_data_chunk == result_chunk

    result = list(iterate_by([header] + test_data, 4, 
    persist_header=True))
    for i in range(0, 4):
        test_data_chunk = "".join([header] + test_data[i*4:(i+1)*4])
        result_chunk = "".join(result[i])
        assert test_data_chunk == result_chunk

