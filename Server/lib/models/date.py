class Date:
    def __init__(self, id, date, activity_id):
        self.id = id
        self.date = date
        self.activity_id = activity_id
    
    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f"Date({self.id}, {self.date}, {self.activity_id})"