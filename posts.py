from rest_test import *
from users import User


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
    
    def display_post(self, entry={}):
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

    def add_new_post(self, user_name='', title='', body=''):
        user = User().find_user_by_name(user_name)[0]
        self.post_activity(user['id'], 'posts' , title=title, body=body)
        
    def find_post_by_title(self, title=''):
        url = f'{self.get_url_string("posts")}title={title}'
        response = requests.get(url, verify=False)
        return self.parse_json(response.json())
    