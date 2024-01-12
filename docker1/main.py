from flask import Flask

app = Flask(__name__)

users = [
    {"id": 1, "username": "hodi", "password": "123", "salary": 5000, "address": "123Main St", "active": True},
    {"id": 2, "username": "josh", "password": "456", "salary": 60000, "address": "456 Oak St","active": True}
    ]


@app.get('/hello')
def greet():
    return {"message":"hello"}

@app.get('/users')
def get_all_users():
    # active_users=[]
    # for user in users:
    #     if user['active']:
    #         active_users.append(user)
    # return active_users
 
    return [user for user in users if user['active']] # return all the active users

@app.get('/users/<int:user_id>') # all the get http requests with id as int will run this function
def get_user_by_id(user_id):
    for user in users: # run over all the users
        if user['id'] == user_id: # if the user id found return the user
            return user
    
    return{"error":"User not found"},404 # if the user_id doesnt exist return 404 status code 


app.run(use_reloader=True) # port 5000 host = localhost
