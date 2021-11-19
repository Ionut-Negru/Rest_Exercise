import json



class User:
    
    def __init__(self):
        self.id = None
        self.name = None
        self.email = None
        self.gender = None
        self.status = None
        
    def get_data_from_json(self, json_entry=[]):
        self.id = json_entry['id']
        self.name = json_entry['name']
        self.email = json_entry['email']
        self.gender = json_entry['gender']
        self.status = json_entry['status']
        return self
    
    def __repr__(self):
        return f'Id: {self.id}\nName: {self.name}\nEmail: {self.email}\nGender: {self.gender}\nStatus: {self.status}'
    
    def __str__(self):
        return self.__repr__()
    
    