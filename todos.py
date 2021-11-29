import datetime
from rest_test import *
from users import User


class ToDo(Rest):
    
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.todos = []
        self.to_do_dict={
            'to_do_id': 'id',
            'user_id': 'user_id',
            'to_do_title': 'title',
            'deadline': 'due_on',
            'to_do_status': 'status'
            }
                
    def get_to_do_from_json(self, json_text={}):
        entry = {}
        entry['id'] = json_text['id']
        entry['user_id'] = json_text['user_id']
        entry['title'] = json_text['title']
        entry['due_on'] = datetime.datetime.strptime(json_text['due_on'],"%Y-%m-%dT%H:%M:%S.%f%z")
        entry['status'] = json_text['status']
        return entry
        
    def parse_json(self, json=''):
        self.todos = []
        self.get_meta_data(json['meta']['pagination'])
        for user in json['data']:
            self.todos.append(self.get_to_do_from_json(user))
        return self.todos
        
    def get_data(self):
        self.todos.clear()
        aux = self.get_url_string('todos')
        response = requests.get(aux, verify=False)
        return self.parse_json(response.json())
        
    def display_to_do(self, entry):
        return f'Id: {entry["id"]}\nUser id: {entry["user_id"]}\nTitle: {entry["title"]}\nDue on: {entry["due_on"].strftime("%d-%m-%Y, %H:%M:%S, %Z")}\nStatus: {entry["status"]}'
    
    def get_sorted_to_dos(self, number_of_to_dos=1, field_by_sort='', reversed=False):
        todos = self.get_entries("todos", number_of_to_dos)
        return sorted(todos, key= lambda x: x[self.to_do_dict[field_by_sort]], reverse = reversed)

    def add_new_to_do(self, user_name='', title='', due_date='', status='pending'):
        user = User().find_user_by_name(user_name)[0]
        self.post_activity(user['id'], 'todos', title=title, due_on=due_date, status=status)