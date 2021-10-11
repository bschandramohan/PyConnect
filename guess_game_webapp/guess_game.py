from flask import Flask
import random

app = Flask(__name__)


def generate_image_tag(fn):
    def operation(*args, **kwargs):
        result = fn(*args, **kwargs)
        if result is not None:
            if result == "Too Low":
                return f'<p>{result}</p> <iframe src="https://giphy.com/embed/wdh1SvEn0E06I" width="480" height="363" '\
                       f'frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a ' \
                       f'href="https://giphy.com/gifs/superman-funny-wdh1SvEn0E06I">via GIPHY</a></p> '
            elif result == "Too High":
                return f'<p>{result}</p> <iframe src="https://giphy.com/embed/t9l9L8qFKJfsFn2WLm" width="480" ' \
                       f'height="270" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a ' \
                       f'href="https://giphy.com/gifs/khalid-young-dumb-and-broke-t9l9L8qFKJfsFn2WLm">via ' \
                       f'GIPHY</a></p> '
            else:
                return f'<p>{result}</p> <iframe src="https://giphy.com/embed/Pnb5GTXdF54QxEaiLZ" width="480" ' \
                       f'height="480" frameBorder="0" class="giphy-embed" allowFullScreen></iframe><p><a ' \
                       'href="https://giphy.com/gifs/aspca-cat-kitten-got-it-Pnb5GTXdF54QxEaiLZ">via GIPHY</a></p> '

    return operation


@app.route("/")
def home():
    return "Welcome to the Guess Game. Guess the number by appending it at the end of the URL"


correct_number = random.randint(1, 10)


@app.route("/<int:number>")
@generate_image_tag
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
