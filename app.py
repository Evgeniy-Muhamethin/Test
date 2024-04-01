from flask import Flask, request, render_template

app = Flask(__name__)


@app.route("/")
def page_index():

    page_content = """
    <h1>Look, it is my page</h1>
    <p>Pages is so much, but it is my page </p>
    <p>Frontend is my very like friend</p>
    """

    return page_content


app.run()