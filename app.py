#Thank you LazyDeveloper for helping developers in this journey !
#Must Subscribe On YouTube @LazyDeveloperr 

from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return '@n_k_bots'


if __name__ == "__main__":
    app.run()
