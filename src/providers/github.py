import requests


class GithubProvider:
    def __init__(self):
        self.base_url: str = "https://api.github.com"
    
    def get_user_details(self, user_id):
        print("Getting user details")
        url = self.base_url + "/users/" + user_id
        r = requests.get(url)
        return r.json()
    

if __name__ == "__main__":
    gh = GithubProvider()
    u = gh.get_user_details("muthugit")    
    print(u)
