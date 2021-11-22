import requests


class Rest:
    
    def __init__(self):
        self.api_url = 'https://gorest.co.in'
        self.token = '158796311887db56fd6e087542f27d1eacaae0ca13d102bd32526ab4041be815'
    
    def get_url_patch_string(self, option='', id=''):
        """
            @param option: the type of data entry
            @param id: the id of the entry
            @return: the url string for the patch operation
        """
        return f'{self.api_url}/public/v1/{option}/{id}?access-token={self.token};'
    
    def get_url_string(self, option=''):
        """
            @param option: the type of data entry
            @return: the url string for the get operation
        """
        return f'{self.api_url}/public/v1/{option}?access-token={self.token};'
    
    def get_url_post_string(self, option='', **kwargs):
        """
            @param option: the type of data entry
            @param kwargs: the keyword arguments of the field that will be included in the post url
            @return: the url string for the post operation
        """
        post_string = self.get_url_string(option)
        for i in kwargs:
            post_string = f'{post_string}{i}={kwargs[i]};'
        return post_string
    
    def get_meta_data(self, pagination = None):
        self.meta['total_entries'] = pagination['total']
        self.meta['total_pages'] = pagination['pages']
        self.meta['current_page'] = pagination['page']
        self.meta['entries_on_page'] = pagination['limit']
        self.meta['previous_page'] = pagination['links']['previous']
        self.meta['next_page'] = pagination['links']['next']
        
    def get_entries(self, option='', number_of_entries=1):
        """
            @param option: the type of data entry to be pulled(users, todos, etc)
            @param numer_of_entrie: the number of entries to be returned
            @return: list of entries
        """
        url = self.get_url_string(option)
        response = requests.get(url, verify=False)
        total_entries = self.get_data()
        
        while len(total_entries) < number_of_entries:
            next_page_url = self.meta.next_page
            response = requests.get(next_page_url, verify=False)
            total_entries = total_entries + self.data.get_data()
        
        return total_entries[0:number_of_entries]
    
    
    def get_number_of_entries(self):
        return self.meta['total_entries']
    
    def update_entry(self, option='', id=1, **kwargs):
        """
            @param option: the type of data entry to be updated (users,todos,etc)
            @param id: the id of the entry
            @param kwargs: the keyword arguments describe which fields will be updated
            example call update_entry('users', 2, gender=female)
        """
        url = self.get_url_patch_string(option, id)
        for i in kwargs:
            url = f'{url}{i}={kwargs[i]};'
        response = requests.patch(url, verify=False)
        if response.status_code == 200:
            print("Updated successfully")
            return response.json()['data']
        else:
            print("Something went wrong")


    def post_activity(self, id=1, activity='', **kwargs):
        """
            @param activity: the available activity : comments, posts, todos
            @param id: the id of the user if the activity is posts or todos. 
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
        else:
            print(f"Something went wrong. {response.status_code}\n{response.json()}")
