import requests
from functools import lru_cache
from src.config import CLIENT_ID, CLIENT_SECRET


class GithubProvider:
    def __init__(self):
        self.base_url: str = "https://api.github.com"
        self.header = {
            "Accept": "application/vnd.github+json",
            "X-GitHub-Api-Version": "2022-11-28"
        }

    @staticmethod
    @lru_cache(maxsize=16)
    def call_get(url):
        print(f"Calling API: {url}")
        r = requests.get(url, auth=(CLIENT_ID, CLIENT_SECRET))
        return r.json()
    
    def get_user_details(self, user_id):
        url = self.base_url + "/users/" + user_id
        return self.call_get(url)
    

if __name__ == "__main__":
    gh = GithubProvider()
    u = gh.get_user_details("muthugit")    
    print(u)
