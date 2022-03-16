def read_database():
    return open("./database.txt", "r").read()


def save_to_database(fname, lname):
    try:
        db = open("./database.txt", "a")
        id = len(read_database().split("\n")) + 1
        db.write(f"\n{id},{fname},{lname}")
        db.close()
    except Exception as e:
        return False
    return True
