def combine_req_string(filters, structure):
    req_string = 'https://api.coronavirus.data.gov.uk/v1/data?filters='
    for filter in filters.values():
        req_string += filter + ';' #adds filters
    req_string = req_string[:-1] #removes last ;
    req_string += '&structure=' + str(structure) #adds structure
    return req_string

def make_request(request_url):
    pass

