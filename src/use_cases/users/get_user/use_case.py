from . import GetUserRequest, GetUserResponse
from src.entities.user import UserEntity
from src.providers.github import GithubProvider
from flask import render_template



class GetUserUseCase:
    def __init__(self, req: GetUserRequest) -> None:
        self.req = req
        self.provider = GithubProvider()

    def execute(self):
        res = self.provider.get_user_details(self.req.user_id)
        return GetUserResponse(
            user=UserEntity(
                login=res["login"],
                id=res["id"],
                avatar_url=res["avatar_url"],
                location=res["location"], 
                number_gists=res["public_gists"],
                number_of_repos=res["public_repos"],
                number_of_followers=res["followers"],
                number_of_following=res["following"],
                name=res["name"],
                company=res["company"]
            )
        )
    
    def render(self):
        data = self.execute()
        return render_template("user/user_profile.html", user=data.user)
