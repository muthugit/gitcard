from flask import Flask
from dataclasses import asdict
from src.use_cases.users.get_user.dto import GetUserRequest
from src.use_cases.users.get_user.use_case import GetUserUseCase


app = Flask(__name__)

@app.route("/<user>")
def get_user(user):
    dto = GetUserRequest(user)
    use_case = GetUserUseCase(dto)
    res = use_case.execute()
    return asdict(res.user)


if __name__ == "__main__":
    app.run(debug=True)