
#from utils import sort_data

def test_sort_data():
    micro_data =  [{
    "date": "2023-06-30T02:08:58.425572",
  },
  {
    "date": "2018-03-23T10:45:06.972075",
  },
  {
    "date": "2019-04-04T23:20:05.206878",
  }]

    assert sort_data(micro_data) ==  [{
    "date": "2023-06-30T02:08:58.425572",
  },
  {
    "date": "2019-04-04T23:20:05.206878",
  },
  {
    "date": "2018-03-23T10:45:06.972075",
  }]

