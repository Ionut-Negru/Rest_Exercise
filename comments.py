from rest_test import *
from users import User
from posts import Post


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
    
    def display_comment(self, entry={}):
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
    
    def add_new_comment(self, post_title='' ,body=''):
        post = Post().find_post_by_title(post_title)[0]
        user = User().find_user_by_id(post['user_id'])[0]
        self.post_activity(post['id'], 'comments', name=user['name'], email=user['email'], body=body)
    
    