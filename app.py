from flask import Flask
from dataclasses import asdict
from src.use_cases.users.get_user import (GetUserRequest, GetUserUseCase)


app = Flask(__name__, template_folder="src/providers/templates", static_folder="src/providers/templates/static")

@app.route("/favicon.ico")
def fav():
    return ""


@app.route("/<user>")
def get_user(user):
    dto = GetUserRequest(user)
    use_case = GetUserUseCase(dto)
    return use_case.render()
    # res = use_case.execute()
    # return asdict(res.user)


if __name__ == "__main__":
    app.run(debug=True)