from posts import Post
from comments import Comment
from todos import ToDo
from users import User

def ex1():
    """
        GET pentru fiecare tip de date
        Metodele get_data returneaza o lista de dictionare ce contin tipurile de date
    """
    posts = Post().get_data()
    comments = Comment().get_data()
    to_dos = ToDo().get_data()
    users = User().get_data()
    
    # Printarea tipurilor de date
    for post in posts:
        print(Post().get_post_string(post)) 
        print('*'*20)
    for comment in comments:
        print(Comment().get_comment_string(comment))
        print('*'*20)
    for to_do in to_dos:
        print(ToDo().get_to_do_string(to_do))
        print('*'*20)
    for user in users:
        print(User().get_user_string(user))
        print('*'*20)
        
def ex2_and_ex3():
    """
        Adauga un nou user si afiseaza datele acestuia
        Un decorator al metodei get_user_string verifica daca numarul de user a crescut
    """
    users = User()
    new_user = users.add_new_user('Negru Ionut', 'example_email@test.com', 'male', 'active')
    print(User().get_user_string(new_user))
        
def ex4():
    """
        Gaseste id-ul unui user pe baza numelui
    """
    users = User()
    found_user = users.find_user_by_name('Negru Ionut')
    print(found_user[0]['id'])
    
def ex5():
    """
        Identifica primii 20 de useri
    """
    users = User()
    found_users = users.get_number_of_users(20)
    for user in found_users:
        print(users.get_user_string(user))
        print('*'*20)
    
def ex6():
    """
        Identifica primii 5 useri ce au un al doilea prenume
    """
    users = User()
    users_with_middle_name = users.find_users_with_middle_name(5)
    for user in users_with_middle_name:
        print(users.get_user_string(user))
        print('*'*20)


def ex8():
    """
        update user email
    """

    users = User()
    current_data = users.find_user_by_id(30)
    print(users.get_user_string(current_data[0]))
    users.update_user(30, email='ceva_random@execise.com')
    current_data = users.find_user_by_id(30)
    print(users.get_user_string(current_data[0]))
    
def ex9():
    """
        Obtine primele 20 todos ordonate by due date
    """
    todos = ToDo()
    sorted_to_dos = todos.get_sorted_to_dos(20,'due_on')
    for todo in sorted_to_dos:
        print(todos.get_to_do_string(todo))
        print('*'*20)
    
#ex1()
#ex2_and_ex3()
#ex4()
#ex5()
#ex6()

#ex8()
#ex9()