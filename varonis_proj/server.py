import json
import jwt
from datetime import datetime, timedelta


class Server:
    def __init__(self):
        self.authorization_db = "user.json"
        self.jwt_key = "secret"
        self.jwt_algorithm = "HS256"

    def login(self, req_user_name, req_password):
        # Fetch user from storage
        file_name = self.authorization_db
        with open(file_name, "r") as user_file:
            data = json.load(user_file)
        db_user_name = data["user_name"]
        db_password = data["password"]
        # Validate user name and password
        if db_user_name != req_user_name or db_password != req_password:
            raise Exception("Wrong user name or password. Login deny")
        # Create token payload
        payload = {
            "user_name": req_user_name,
            "exp": datetime.utcnow() + timedelta(days=1),
            "admin": False
        }
        # Encode the payload with key and algorithm
        token = jwt.encode(payload=payload, key=self.jwt_key, algorithm=self.jwt_algorithm)
        # Return the token
        return token


# server = Server()
# username = "KFIR-AV"
# password = "123"
# T = server.login(req_user_name=username, req_password=password)
# print(jwt.decode(jwt=T, key="secret", algorithms='HS256'))