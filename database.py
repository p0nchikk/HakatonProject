import pandas

import consts

data_frame = pandas.DataFrame()

def init_database():
    global data_frame
    data_frame = pandas.read_csv("database.csv", index_col=0)

"""
    This function gets request dictionary with its details
    and writes it to database file
"""
def save_new_request(request):
    new_request = {
        "Id": get_requests_count(),
        "Status": consts.WAITING_STATUS,
        "Category": request["Category"],
        "Description": request["Description"],
        "Owner_number": request["Owner_number"],
        "Owner_name" : request["Owner_name"],
        "Owner_area": request["Owner_area"],
        "Helper_number": None,
        "Helper_name": None
    }
    data_frame.loc[new_request["Id"]] = new_request
    data_frame.to_csv("database.csv", index=True)

"""
    This function gets owner number and returns dictionary 
    of requests of this number
"""
def get_user_requests(owner_number):
    requests_dict = data_frame.loc[(data_frame['Owner_number'] == owner_number)].to_dict()
    return get_list_of_data_frame(requests_dict)

"""
    This function gets the owner area and returns dictionary
    of requests from given area
"""
def get_requests_by_area(owner_area):
    requests_df = data_frame.loc[(data_frame['Owner_area'] == owner_area) &
                                   (data_frame["Status"] == consts.WAITING_STATUS)]
    return get_list_of_data_frame(requests_df)

"""
    This function gets the owner area and the category
    and returns dictionary of requests from given area
"""
def get_requests_by_category_and_area(category, owner_area):
    requests_dict = data_frame.loc[(data_frame['Category'] == category) &
                                   (data_frame["Owner_area"] == owner_area) &
                                   (data_frame["Status"] == consts.WAITING_STATUS)]
    return get_list_of_data_frame(requests_dict)

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
    update_request_status(request_id, consts.HELPING_STATUS)

"""
    This function returns the amount of requests saved in database
"""
def get_requests_count():
    return len(data_frame.index)


def get_list_of_data_frame(df):
    list = []
    for index in range(len(df)):
        curr_request = {
            "Id": int(df.iloc[index]["Id"]),
            "Status": int(df.iloc[index]["Status"]),
            "Category": df.iloc[index]["Category"],
            "Description": df.iloc[index]["Description"],
            "Owner_name": df.iloc[index]["Owner_name"],
            "Owner_number": int(df.iloc[index]["Owner_number"]),
            "Owner_area": df.iloc[index]["Owner_area"]
        }
        list.append(curr_request)
    return list

init_database()
print(get_requests_by_area("Tel Aviv"))