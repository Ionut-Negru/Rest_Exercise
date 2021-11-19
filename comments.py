

class Comment:
    
    def __init__(self):
        self.id = None
        self.post_id = None
        self.name = None
        self.email = None
        self.body = None
        
    def get_data_from_json(self, json_text={}):
        self.id = json_text['id']
        self.post_id = json_text['post_id']
        self.name = json_text['name']
        self.email = json_text['email']
        self.body = json_text['body']
        return self
    
    def __repr__(self):
        return f'Id: {self.id}\nPost Id: {self.post_id}\nName: {self.name}\nEmail: {self.email}\nBody :{self.body}'
    
    def __str__(self):
        return self.__repr__()