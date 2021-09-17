import random

from flask import Flask

app = Flask(__name__)

correct_number = random.randint(1, 10)


@app.route("/")
def home():
    return "Welcome to the guessing game! Guess the number by appending it at the end of the URL"


@app.route("/<int:number>")
def guess_number(number):
    global correct_number  # Required when you have global variable being modified (not required while just read)
    if number < correct_number:
        return "Too Low"
    elif number > correct_number:
        return "Too High"
    else:
        correct_number = random.randint(1, 10)
        return "GOT IT!"


if __name__ == "__main__":
    app.run(debug=True)
