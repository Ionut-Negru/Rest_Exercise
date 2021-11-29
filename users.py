from rest_test import *


class User(Rest):
    
    def __init__(self):
        super().__init__()
        self.meta = {}
        self.users = []
        
    def get_user_from_json(self, json_entry=[]):
        """
            Getting the user data from the json entry
            
            @return
            A dictionary with the user information
            
        """
        entry = {}
        entry['id'] = json_entry['id']
        entry['name'] = json_entry['name']
        entry['email'] = json_entry['email']
        entry['gender'] = json_entry['gender']
        entry['status'] = json_entry['status']
        return entry
    
    def parse_json(self, json=''):
        self.users = []
        self.get_meta_data(json['meta']['pagination'])
        for user in json['data']:
            self.users.append(self.get_user_from_json(user))
        return self.users
    
    def get_data(self):
        """
            Perform a GET for the users
            Extract the meta data from the response
            Extract the users data from the response
            @return
                A list of users, each user is represented by a dictionary
        """
        self.users.clear()
        aux = self.get_url_string('users')
        response = requests.get(aux, verify=False)
        return self.parse_json(response.json())
        
    def get_number_of_users(self, number_of_users=1):
        """
            Perform a GET for the users
            Extract the first N users
            @param number_of_users
                The number of users to be extracted
            @return
                A list of users, each user is represented by a dictionary, the length is specified by the param 
        """
        return self.get_entries('users', number_of_users)
        
    
    def display_user(self, entry={}):
        if entry != None:
            return f'Id: {entry["id"]}\nName: {entry["name"]}\nEmail: {entry["email"]}\nGender: {entry["gender"]}\nStatus: {entry["status"]}'
    
    
    def check_number_of_users_increased(func):
        
        def wrapper(*args, **kwargs):
            args[0].get_data()
            previous_number_of_users = args[0].get_number_of_entries()
            user = func(*args,**kwargs)
            args[0].get_data()
            current_number_of_users = args[0].get_number_of_entries()
            if previous_number_of_users < current_number_of_users:
                return user
            else:
                return None
        return wrapper
            
    @check_number_of_users_increased
    def add_new_user(self, name='', email='', gender='', status=''):
        if name == '':
            return 'Failed to add new user. Name was empty'
        if email == '':
            return 'Failed to add new user. Email was empty'
        if gender == '':
            return 'Failed to add new user. Gender was empty'
        if status == '':
            return 'Failed to add new user. Status was empty'
        
        url = self.get_url_string('users')
        payload = self.get_payload(name=name, email=email, gender=gender, status=status)
        response = requests.post(url, payload, verify=False)
        if response.status_code == 201:
            print("Adding new user successfully done.")
            return self.get_user_from_json(response.json()['data'])
        else:
            print("Failed adding a new user")
        
    def find_user_by_id(self, id=0):
        url = f'{self.get_url_string("users")}id={id}'
        response = requests.get(url, verify=False)
        return self.parse_json(response.json())
    
    def find_user_by_name(self, name=''):
        url = f'{self.get_url_string("users")}name={name}'
        response = requests.get(url, verify= False)
        return self.parse_json(response.json())
    
    def find_users_by_status(self, status='active', number_of_users=1):
        url = f'{self.get_url_string("users")}status={status}'
        result = []
        while len(result) < number_of_users:
            response = requests.get(url, verify=False)
            users = self.parse_json(response.json())
            for user in users:
                if user['status'] == status:
                    result.append(user)
            url = f'{self.meta["next_page"]};status={status}'
        self.users = result[0:number_of_users]
        return self.users

    def find_users_with_middle_name(self, number_of_users=1):
        result = []
        users = self.get_data()
        while len(result) < number_of_users:
            for user in users:
                if len(user['name'].split()) > 2:
                    result.append(user)
            url = f'{self.meta["next_page"]}'
            users = self.parse_json(requests.get(url, verify=False).json())
        self.users = result[0:number_of_users]
        return self.users
    
    def update_user(self, id=1, **kwargs):
        entry = self.update_entry('users', id, **kwargs)
        return self.get_user_from_json(entry)
        
    