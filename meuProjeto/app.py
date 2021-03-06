from flask import Flask
app = Flask(__name__)

@app.route("/")
def hello():
    return "Hello World! My name is Flavia"

@app.route('/user/<username>')
def show_user_profile(username):
    # show the user profile for that user
    return 'User %s' % username    

if __name__ == "__main__":
    app.run()