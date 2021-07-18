from flask import Flask

app = Flask(__name__)

def make_bold(func):
    def wrapper():
        return "<b>"+func()+"</b>"
    return wrapper

def make_emmphasis(func):
    def wrapper():
        return "<em>"+func()+"</em>"
    return wrapper

def make_underlined(func):
    def wrapper():
        return "<u>" + func() + "</u>"
    return wrapper


@app.route('/')
def hello_world():
    return '<h1>Hello, World!<h1>'

@app.route("/bye")
@make_bold
@make_underlined
@make_emmphasis
def bye():
    return "Bye"

@app.route("/<name>/<int:age>")
def myname(name,age):
    return f"HI, {name}! You are {age} old ;)"



if __name__ == "__main__":
    app.run(debug=True)