import datetime


class ToDo:
    
    def __init__(self):
        self.id = None
        self.user_id = None
        self.title = None
        self.due_on = None
        self.status = None
        
    def get_data_from_json(self, json_text={}):
        self.id = json_text['id']
        self.user_id = json_text['user_id']
        self.title = json_text['title']
        self.due_on = datetime.datetime.strptime(json_text['due_on'],"%Y-%m-%dT%H:%M:%S.%f%z")
        self.status = json_text['status']
        return self
        
    def __repr__(self):
        return f'Id: {self.id}\nUser id: {self.user_id}\nTitle: {self.title}\nDue on: {self.due_on}\nStatus: {self.status}'
    
    def __str__(self):
        return self.__repr__()