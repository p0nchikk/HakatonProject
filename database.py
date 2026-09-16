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
    requests_dict = data_frame.loc[data_frame['Owner_number'] == owner_number].to_dict()
    return get_list_of_dict(requests_dict)

"""
    This function gets the owner area and returns dictionary
    of requests from given area
"""
def get_requests_by_area(owner_area):
    requests_dict = data_frame.loc[(data_frame['Owner_area'] == owner_area) & (data_frame["Status"] == 'Published')].to_dict()
    return get_list_of_dict(requests_dict)

"""
    This function gets the owner area and the category
    and returns dictionary of requests from given area
"""
def get_requests_by_category_and_area(category, owner_area):
    requests_dict = data_frame.loc[(data_frame['Category'] == category) & (data_frame["Owner_area"] == owner_area)].to_dict()
    return get_list_of_dict(requests_dict)

"""
    This function gets the request id and its new status 
    and updated database
"""
def update_request_status(id, status):
    data_frame.loc[id, "Status"] = status
    data_frame.to_csv("database.csv", index=True)

"""
    This function sets helper's name and phone number
    to request by its id and updates request status to helping
"""
def set_helper_to_request(request_id, helper_name, helper_number):
    data_frame.loc[request_id, "Helper_name"] = helper_name
    data_frame.loc[request_id, "Helper_number"] = helper_number
    data_frame.to_csv("database.csv", index=True)
    update_request_status(request_id, 1)


def get_list_of_dict(dict):
    list = []
    for i in range(1, len(dict["Status"])+1):
        curr_request = {
            "Id": i,
            "Status": dict["Status"][i],
            "Category": dict["Category"][i],
            "Description": dict["Description"][i],
            "Owner_name": dict["Owner_name"][i],
            "Owner_number": dict["Owner_number"][i],
            "Owner_area": dict["Owner_area"][i],
            "Helper_name": dict["Helper_name"][i],
            "Helper_number": dict["Helper_number"][i]
        }
        list.append(curr_request)
    return list