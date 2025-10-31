class Activity():

    def __init__(self, id, activity):
        self.id = id
        self.activity = activity

    def __eq__(self, other):
        return self.__dict__ == other.__dict__
    
    def __repr__(self):
        return f'Activity({self.id}, {self.activity})'