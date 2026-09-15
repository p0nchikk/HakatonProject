import pandas
import numpy as np

database = pandas.DataFrame()

def load_database_from_file():
    database = pandas.read_csv("database.csv")

"""
    This function gets request dictionary with its details
    and writes it to database file
"""
def save_new_request(request):
    new_request = {
        "Id": request["Id"],
        "Status": request["Status"],
        "Category": request["Category"],
        "Description": request["Description"],
        "Owner_number": request["Owner_number"],
        "Owner_name" : request["Owner_name"],
        "Owner_area": request["Owner_area"],
        "Helper_number": request["Helper_number"],
        "Helper_name": request["Helper_name"]
    }
    database.loc[len(database)] = new_request
    database.to_csv("database.csv", index=False)

"""
    This function gets owner number and returns array of requests of this number
"""
def get_user_requests(owner_number):
    requests = np.where(database['Owner_number'] == owner_number)
    return requests

"""
    This function gets the owner area and returns the array
    of requests from given area
"""
def get_requests_by_city(owner_area):
    requests = np.where(database['Owner_area'] == owner_area and database["Status"] == 'Published')
    return requests

"""
    This function gets the request id and its new status 
    and updated database
"""
def update_request_status(id, status):
    database.loc[id]["Status"] = status
    database.to_csv("database.csv", index=False)


# Status 0 - Published
# Status 1 - Helping
# Status 2 - Finished
