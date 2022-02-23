import validation


def ask_person():
    person = {
        "name": "",
        "email": "",
        "person_id": "",
        "start_date": ""
    }
    while True:
        if person["name"] == "":
            person["name"] = input("Give name: ")
        if is_email((person["email"])):
            person["email"] = input("Give name: ")

        if is_email((person["person_id"])):
            person["person_id"] = input("Give person id: ")

        if is_date((person["start_date"])):
            person["start_date"] = input("Give name: ")

    return person
