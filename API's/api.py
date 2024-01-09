from flask import Flask

# Flask is Class

app = Flask(__name__)  # building a flask app object using __init__()


@app.post('/hello') # if any user sent get req to /hello resource run this function
def gett_hello(): # the return of this function will be the response of the code
    return 'world !'


app.run(port=8881) # run the application