import pandas

data_frame = pandas.DataFrame()

def init_database():
    global data_frame
    data_frame = pandas.read_csv("database.csv", index_col=0)

"""
    This function gets request dictionary with its details
    and writes it to database file
"""
def save_new_request(request):
    # TODO: fix concat function
    new_request = {
        "Status": request["Status"],
        "Category": request["Category"],
        "Description": request["Description"],
        "Owner_number": request["Owner_number"],
        "Owner_name" : request["Owner_name"],
        "Owner_area": request["Owner_area"],
        "Helper_number": request["Helper_number"],
        "Helper_name": request["Helper_name"]
    }
    data_frame.loc[request["Id"]] = new_request
    data_frame.to_csv("database.csv", index=True)

"""
    This function gets owner number and returns dictionary 
    of requests of this number
"""
def get_user_requests(owner_number):
    requests = data_frame[data_frame['Owner_number'] == owner_number].to_dict()
    return requests

"""
    This function gets the owner area and returns dictionary
    of requests from given area
"""
def get_requests_by_area(owner_area):
    requests = data_frame[data_frame['Owner_area'] == owner_area and data_frame["Status"] == 'Published'].to_dict()
    return requests

"""
    This function gets the request id and its new status 
    and updated database
"""
def update_request_status(id, status):
    data_frame.loc[id-1]["Status"] = status
    data_frame.to_csv("database.csv", index=True)

