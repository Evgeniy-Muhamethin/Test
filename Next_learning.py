from flask import Flask

app = Flask(__name__)

@app.route("/")
def page_index():
    return "Main page"


app.run(host='0.0.0.0', port=8000)