class Registration:
    def __init__(self, id, attendee_id, date_id):
        self.id = id
        self.attendee_id = attendee_id
        self.date_id = date_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Registration({self.id}, {self.attendee_id}, {self.date_id})"
    