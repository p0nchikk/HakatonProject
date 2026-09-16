import database

requests = []

def init_requests():
    global requests

"""
    This function creates new request and saves it locally and in database
"""
def create_request(category, description,owner_name,owner_number, owner_area):
    request = {
            "Id" : database.get_requests_count(),
            "Category": category,
            "Description" : description,
            "Owner_name" : owner_name,
            "Owner_number" : owner_number,
            "Owner_area" : owner_area
        }
    requests.append(requests)
    database.save_new_request(request)
