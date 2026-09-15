requests = []

def init_requests():
    global requests

def create_request(category, description,owner_name,owner_number, owner_area):
    return {
            "Id" : len(requests),
            "Status": 0,
            "Category": category,
            "Description" : description,
            "Owner_name" : owner_name,
            "Owner_number" : owner_number,
            "Owner_area" : owner_area,
            "Helper_name" : None,
            "Helper_number" : None
        }



def add_helper(id, name, number):
    requests[id]["Helper_name"] = name
    requests[id]["helper_number"] = number

