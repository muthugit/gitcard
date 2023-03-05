from dataclasses import dataclass


@dataclass
class UserEntity:
    login: str
    id: str
    avatar_url: str
    name: str
    company: str
    location: str
    number_of_repos: int
    number_gists: int
    number_of_followers: int
    number_of_following: int
