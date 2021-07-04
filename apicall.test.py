import unittest
from apicall import *

class getData(unittest.TestCase):

    def test_combine_req_string(self):
        filters = {'areatype': 'areaType=nation', 'areaname': 'areaName=england'}
        structure = {
            "date":"date",
            "areaName":"areaName",
            "newCasesByPublishDate": "newCasesByPublishDate",
            "newDeaths28DaysByPublishDate": "newDeaths28DaysByPublishDate"
        }
        expected_req = \
        f'https://api.coronavirus.data.gov.uk/v1/data?filters={filters["areatype"]};{filters["areaname"]}&structure={structure}'
        self.assertEqual(combine_req_string(filters, structure), expected_req)

    def test_make_request(self):
        test_url = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22newCasesByPublishDate%22:%20%22newCasesByPublishDate%22}'
        self.assertNotEqual(make_request(test_url), None)

    def test_parse_results(self):
        test_url = 'https://api.coronavirus.data.gov.uk/v1/data?filters=areaType=nation;areaName=england&structure={%22newCasesByPublishDate%22:%20%22newCasesByPublishDate%22}'
        test_response = make_request(test_url)
        self.assertEqual(type(parse_results(test_response)), dict)
    
    def test_result_display(self):
        pass

unittest.main()