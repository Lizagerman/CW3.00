from utils import get_data

def test_get_data():
    assert get_data("file_for_test.json") == [{'date': '2023-06-30T02:08:58.425572'},
                                                {'date': '2018-03-23T10:45:06.972075'},
                                                {'date': '2019-04-04T23:20:05.206878', 'other': 'other for test'}]


