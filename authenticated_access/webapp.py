import user_repository

app = user_repository.dbFlask
MY_SECRET = "A VERY IMPORTANT SECRET"
user_repository.__init__()


@app.route("/")
def home():
    return "<h1>Register using /user/{username}/<{password} or login via login/{username}/{password}" \
           " to access the secret</h1> "


@app.route("/user/register/<username>/<password>")
def register(username, password):
    status = user_repository.store_user(username, password)
    if status:
        return f"Authenticated User, here is your secret: {MY_SECRET}"
    else:
        return "Invalid registration"


@app.route("/user/login/<username>/<password>")
def login(username, password):
    status = user_repository.is_user_login_correct(username, password)
    if status:
        return f"Authenticated User, here is your secret: {MY_SECRET}"
    else:
        return "Invalid user"


if __name__ == "__main__":
    app.run(debug=True)
