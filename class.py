class Student:
    School = "Glenmuir"

    def __init__(self):
        self.id = 0
        self.first_name = ""
        self.last_name = ""

    def __init__(self, id, fisrt_name, last_name):
        self.id = id
        self.first_name = fisrt_name
        self.last_name = last_name

    def id_update(self, new_id):
        self.id = new_id

    def first_name_update(self, ln):
        self.last_name = ln

    def last_name_update(self, fn):
        self.first_name = fn

    def print_info(self):
        print(self.id)
        print(self.first_name + " " + self.last_name)

    