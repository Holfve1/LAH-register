class Attendee:
    def __init__(self, id, first_name, last_name, suburb):
        self.id = id
        self.first_name = first_name
        self.last_name = last_name
        self.suburb = suburb

    def __eq__(self, other):
        return self.__dict__ == other.__dict__

    def __repr__(self):
        return f"Attendee({self.id}, {self.first_name}, {self.last_name}, {self.suburb})"