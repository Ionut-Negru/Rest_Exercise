from rest_test import *

class Post(Rest):
    
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.posts = []
        
    def get_to_do_from_json(self, json_text={}):
        entry = {}
        entry['id'] = json_text['id']
        entry['user_id'] = json_text['user_id']
        entry['title'] = json_text['title']
        entry['body'] = json_text['body']
        return entry
    
    def get_post_string(self, entry={}):
        return f'Id: {entry["id"]}\nUser id: {entry["user_id"]}\nTitle: {entry["title"]}\nComment: {entry["body"]}'
    
    def parse_json(self, json=''):
        self.posts = []
        self.get_meta_data(json['meta']['pagination'])
        for user in json['data']:
            self.posts.append(self.get_to_do_from_json(user))
        return self.posts
    
    def get_data(self):
        self.posts.clear()
        aux = self.get_url_string('posts')
        response = requests.get(aux, verify=False)
        return self.parse_json(response.json())

        