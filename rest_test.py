import requests
from utils import *


class Rest:
    
    def __init__(self):
        self.api_url = 'https://gorest.co.in'
        self.token = '158796311887db56fd6e087542f27d1eacaae0ca13d102bd32526ab4041be815'
        self.data = DataWrapper()
    
    def get_url_patch_string(self, option='', id=''):
        return f'{self.api_url}/public/v1/{option}/{id}?access-token={self.token};'
    
    def get_url_string(self, option=''):
        return f'{self.api_url}/public/v1/{option}?access-token={self.token};'
    
    def get_url_post_string(self, option='', **kwargs):
        post_string = self.get_url_string(option)
        for i in kwargs:
            post_string = f'{post_string}{i}={kwargs[i]};'
        return post_string
        
    def get_data(self, option=''):
        aux = self.get_url_string(option)
        response = requests.get(aux, verify=False)
        return self.data.get_data(option, response.json())
    
    def get_entries(self, option='', number_of_entries=1):
        aux = self.get_url_string(option)
        response = requests.get(aux, verify=False)
        print(f'{aux}')
        total_entries = self.data.get_data(option, response.json())
        
        while len(total_entries) < number_of_entries:
            aux = self.data.next_page
            response = requests.get(aux, verify=False)
            total_entries = total_entries + self.data.get_data(option, response.json())
        
        return total_entries[0:number_of_entries]
    
    def get_number_of_users(self):
        self.get_data('users')
        return self.data.total_entries
            
    def post_entry(self, option='', **kwargs):
        if self.data.current_data == option:
            previous_number_of_users = self.get_number_of_users()
        else:
            self.get_data(option)
            previous_number_of_users = self.get_number_of_users()

        response = requests.post(self.get_url_post_string(option, **kwargs), verify=False)
        if response.status_code == 201:
            self.data.data.append(User().get_data_from_json(response.json()['data']))
            print(self.data.data[-1])
        else:
            print(response.json())  
        
        current_number_of_users = self.get_number_of_users()
        if current_number_of_users > previous_number_of_users:
            print("The number of users increased")
        else:
            print("Something went wrong. No new user in data")  

    def find_user_by_id(self, id=0):
        url = f'{self.get_url_string("string")}id={id}'
        response = requests.get(url, verify=False)
        return self.data.get_users(response.json())
    
    def find_users_by_status(self, status='active', number_of_users=1):
        url = f'{self.get_url_string("users")}status={status}'
        response = requests.get(url, verify=False)
        
    def find_users_with_middle_name(self, number_of_users=1):
        result = []
        while len(result) < number_of_users:
            users = self.get_data('users')
            for user in users:
                if len(user.name.split()) > 1:
                    result.append(user)
        return result[0:number_of_users]
        
    def get_to_dos_by_date(self, number_of_to_dos=1):
        todos = self.get_entries("todos", number_of_to_dos)
        return sorted(todos, key= lambda x: x.due_on)
    
    def update_entry(self, option='', id=1, **kwargs):
        url = self.get_url_patch_string(option, id)
        for i in kwargs:
            url = f'{url}{i}={kwargs[i]};'
        response = requests.patch(url, verify=False)
        if response.status_code == 200:
            print("Updated successfully")
        else:
            print("Something went wrong")

    def post_activity(self, id=1, activity='', **kwargs):
        """
            @param activity = the available activity : comments, posts, todos
            @param id = the id of the user if the activity is posts or todos. 
            If the activity is comments this is the id of the post
        """
        target = 'users'
        if activity == 'comments':
            target = 'posts'
        url = f'{self.api_url}/public/v1/{target}/{id}/{activity}?access-token={self.token};'
        for i in kwargs:
            url = f'{url}{i}={kwargs[i]};'
        print(url)
        response = requests.post(url, verify=False)
        if response.status_code == 201:
            print(f"Successfully added {activity}")
            print(response.json())
        else:
            print(f"Something went wrong. {response.status_code}\n{response.json()}")
""" Testing """

rest = Rest()
# rest.post_entry('users',email='sters_sts@example.com', name='ExampleName', gender='male', status='inactive')
# users = rest.find_users_with_middle_name(5)
# print(rest.find_user_by_id(120))
#users = rest.get_to_dos_by_date(20)
#for x in users:
#    print(x)
#    print('*' * 2)
#
#rest.update_entry('users', 18, email='test_example@meh.com')
#rest.post_activity(18, 'posts', body='Intr-o zi nu era lumina', title='O zi')
#rest.post_activity(18, 'todos', title='Exercitii', status='pending')
#rest.post_activity(1, 'comments', name='Marcel', email='example@testy.com', body='am adaugat un comment')
