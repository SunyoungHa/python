import json
from name import *

# Write a function: create_my_contact()  - The function create_my_contact() will assign
# the above name records to variable my_contact of dictionary data type.  The function
# create_my_contact() will return my_contact as the return value of the function.
# def main():
#     print('ok')
def create_my_contact():
    my_contact = {
        "01": {
            "firstName": "John",
            "lastName": "Smith",
            "DOB": "1/20/1991",
            "phoneNum": {"number": "510-600-5400",
                         "type": "cell"},
            "address": {
                "street": "100 main street",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94536"}
        },

        "02": {
            "firstName": "Ron",
            "lastName": "Robertson",
            "DOB": " 5/23/1991 ",
            "phoneNum": {"number": "987-654-3210",
                         "type": "cell"},
            "address": {
                "street": "100 main street",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94536"}
        },

        "03": {
            "firstName": "Paul",
            "lastName": "Washington",
            "DOB": " 5/23/1991 ",

            "phoneNum": {"number": "987-654-3210",
                         "type": "cell"},
            "address": {
                "street": "100 main street",
                "city": "Fremont",
                "state": "CA",
                "zipcode": "94536"}
        }

    }

    return my_contact


# Write a function:  save_json_file (fileName, contact_list)
# This function will output the dictionary contents in variable myContact to a JSON file
# fileName (MUST be JSON file format) which contains the records from myContact
# dictionary variable.  This function takes two parameters.  fileName – name of the JSON
# file to be created.  contact_list– contains my contact records stored in dictionary data
# type.  The variable contact_list is the return value of function create_my_contact().

def save_json_file(fileName, contact_list):
    json_object = json.dumps(contact_list, indent=4)
    print(json_object)

    with open(fileName, "w") as outfile:
        outfile.write(json_object)
    outfile.close()
    print(fileName, "created.")

    return json_object


# After you created the my_contact.json file, you need to open my_contact.json file and
# read the json file (the file must be JSON file format that you created) into a dictionary
# json_data. Write a function: find_my_contact_key(searchKey, my_contact).  This function will
# search the dictionary json_data with the key searchKey.  If the searchKey is in
# json_data, it will print out the found record.   For example, if search for ‘Ron’ using the
# function find_my_contact_key("Ron", json_data).  The function will print out the
# founded record, similar to the one below:

def find_my_contact_key(searchKey, my_contact):
    with open(my_contact, "r") as json_file:
        opened_data = json.load(json_file)

        found = False
        for p_id, p_info in opened_data.items():
            for key in p_info:
                if p_info[key] == searchKey:
                    print("****",  p_info[key], "found")
                    print("{:<10}".format("Name: "), p_info["firstName"],p_info["lastName"])
                    print("{:<10}".format("Birthday: "), p_info["DOB"])
                    print(p_info["phoneNum"]["type"],": ", p_info["phoneNum"]["number"])
                    print("address: ", p_info["address"])
                    found = True
        if not found:
            print("**** NOT Found: ", searchKey, "***\n")


if __name__ == '__main__':
    name = name("Sunyoung Ha", "lab6")
    print(name)

    data = create_my_contact()
    print(data)

    json_file = save_json_file("my_contact.json", data)
    # print(json_file)

    find = find_my_contact_key("John", 'my_contact.json')
    print(find)

    find = find_my_contact_key("Sunyoung", 'my_contact.json')
    print(find)
