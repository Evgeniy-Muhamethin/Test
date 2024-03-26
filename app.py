from flask import Flask

app = Flask(__name__)


@app.route("/")
def page_index():
    return "Main page"


@app.route("/user/<uid>")
def profile(uid):
    print(uid)
    print(type(uid))
    return " "


@app.route("/profile/<uid>/")
def page_profile(uid):
    return f"<h1>Page profile user {uid}<h1>"


@app.route("/items/<uid>/")
def page_items(uid):
    return f"<h2>Page item {uid}<h2>"


@app.route("/feed/")
def page_feed():
    return "Feed user"


@app.route("/message/")
def page_message():
    return "Message user"


app.run()
