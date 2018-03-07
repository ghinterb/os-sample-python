from flask import Flask
application = Flask(__name__)

@application.route("/")
def hello():
    return "Hello World! - My Name is Cyril Figgis<br/><img src='http://i.imgur.com/aypgP.jpg'/>"

if __name__ == "__main__":
    application.run()
