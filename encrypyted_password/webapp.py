from init import app
import user_repository

user_repository.init()


@app.route("/")
def home():
    return "<b> Use /user/register/{username}/{password} to register and /user/login/{username}/{password} to login</b>"


@app.route("/user/register/<username>/<password>")
def register(username, password):
    if user_repository.store(username, password):
        return f"Authenticated User"
    else:
        return f"Invalid registration details"


@app.route("/user/login/<username>/<password>")
def login(username, password):
    if user_repository.is_user_login_correct(username, password):
        return f"Authenticated User"
    else:
        return f"Invalid login details"


if __name__ == "__main__":
    app.run(debug=True)
