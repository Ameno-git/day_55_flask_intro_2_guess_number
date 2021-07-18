from flask import Flask
import random

app = Flask(__name__)
number=random.randint(0,9)
print(number)
numb_list=[0,1,2,3,4,5,6,7,8,9]

@app.route("/")
def main_page():
    return "<h1 style='text-align: center'>Guess the number between 0 and 9</h1>" \
           "<h4 style='text-align: center'>adding  <u>/url/number</u>,  number in range [0:9]</h4>" \
           "<img scr='https://media.giphy.com/media/hvS1eKlR75hMr0l7VJ/giphy.gif'>"

@app.route("/url/<int:numb>")
def numbers(numb):
    if numb not in numb_list:
        return f"<h1>Number should be {numb_list}"
    elif numb>number:
        return f"<h3>Too high</h3>"
    elif numb<number:
        return f"<h3>Too low</h3>"
    else:
        return f"<h1 style='text-align: center'>YOU WON!!! number is '{number}'</h1>"



if __name__ == "__main__":
    app.run(debug=True)
