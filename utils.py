import json
from users import User
from posts import Post
from comments import Comment
from todos import ToDo

class DataWrapper:
    
    def __init__(self):
        self.current_data = None
        self.total_entries = None
        self.total_pages = None
        self.current_page = None
        self.entries_on_page = None
        self.previous_page = None
        self.next_page = None
    
    def get_meta_data(self,json_text={}):
        pagination = json_text['meta']['pagination']
        self.total_entries = pagination['total']
        self.total_pages = pagination['pages']
        self.current_page = pagination['page']
        self.entries_on_page = pagination['limit']
        self.previous_page = pagination['links']['previous']
        self.next_page = pagination['links']['next']
        
    def get_users(self, json_text={}):
        self.current_data = 'users'        
        self.get_meta_data(json_text)
        self.data = []
        for aux in json_text['data']:
            self.data.append(User().get_data_from_json(aux))
            
        return self.data
        
    def get_posts(self, json_text={}):
        self.current_data = 'posts'
        self.get_meta_data(json_text)
        self.data = []
        for aux in json_text['data']:
            self.data.append(Post().get_data_from_json(aux))
        
        return self.data
    
    def get_comments(self, json_text={}):
        self.current_data = 'comments'
        self.get_meta_data(json_text)
        self.data = []
        for aux in json_text['data']:
            self.data.append(Comment().get_data_from_json(aux))
        
        return self.data
            
    def get_todos(self, json_text={}):
        self.current_data = 'todos'
        self.get_meta_data(json_text)
        self.data = []
        for aux in json_text['data']:
            self.data.append(ToDo().get_data_from_json(aux))
        
        return self.data
    
    def get_data(self, option='', json_text=''):
        match option:
            case 'users':
                return self.get_users(json_text)
            case 'posts':
                return self.get_posts(json_text)
            case 'comments':
                return self.get_comments(json_text)
            case 'todos':
                return self.get_todos(json_text)
    