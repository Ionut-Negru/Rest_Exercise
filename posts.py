

class Post:
    
    def __init__(self):
        self.id = None
        self.user_id = None
        self.title = None
        self.body = None
        
    def get_data_from_json_entry(self, json_text={}):
        self.id = json_text['id']
        self.user_id = json_text['user_id']
        self.title = json_text['title']
        self.body = json_text['body']
        return self
    
    def __repr__(self):
        return f'Id: {self.id}\nUser id: {self.user_id}\nTitle: {self.title}\nComment: {self.body}'
    
    def __str__(self):
        return self.__repr__()