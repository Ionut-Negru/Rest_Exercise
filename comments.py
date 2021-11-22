from rest_test import *

class Comment(Rest):
    
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.comments = []
        
    def get_comment_from_json(self, json_text={}):
        entry = {}
        entry['id'] = json_text['id']
        entry['post_id'] = json_text['post_id']
        entry['name'] = json_text['name']
        entry['email'] = json_text['email']
        entry['body'] = json_text['body']
        return entry
    
    def get_comment_string(self, entry={}):
        return f'Id: {entry["id"]}\nPost Id: {entry["post_id"]}\nName: {entry["name"]}\nEmail: {entry["email"]}\nBody :{entry["body"]}'
    
    def parse_json(self, json=''):
        self.comments = []
        self.get_meta_data(json['meta']['pagination'])
        for user in json['data']:
            self.comments.append(self.get_comment_from_json(user))
        return self.comments
    
    def get_data(self):
        self.comments.clear()
        aux = self.get_url_string('comments')
        response = requests.get(aux, verify=False)
        return self.parse_json(response.json())
    
    