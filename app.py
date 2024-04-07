from flask import Flask, request, render_template

app = Flask(__name__)


# @app.route("/")
# def hello():
#     user_data = {
#         "name":"Jill",
#         "number": "+7 123 456 78 90",
#         "age":"28",
#         "email":"jill@gmail.com",
#         "telegram":"jill_tellMe"
#     }
#     return render_template("hello.html",
#                            user = user_data)


# @app.route("/")
# def hello():
#     items = ["Python", "Java", "Kotlin", "Go"]
#     return render_template("hello.html",
#                            items=items)


@app.route("/")
def hello2():
    is_blocked = False
    return render_template("hello.html",
                           is_blocked=is_blocked)


@app.route("/1/")
def array_start():
    items = ["Python", "Java", "Kotlin", "Go"]
    return render_template("array_test.html",
                           items=items)


app.run()