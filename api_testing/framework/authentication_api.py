import json

import requests


class AuthenticationApi:
    base_url = "https://restful-booker.herokuapp.com"
    auth_api = base_url + "/auth/"

    def post_authentication(self, username, password, content_type="application/json"):
        return requests.post(self.auth_api, data=json.dumps({"password": password, "username": username}),
                             headers={"Content-Type": content_type})
