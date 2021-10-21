from sanic import Sanic
from sanic.response import json
from server import Server

server = Server()
app = Sanic("My Web Server")
token = None


# login and get token for the server
@app.route("/", methods=["GET"])
async def login(request):
    data = request.json
    user_name = data["user_name"]
    password = data["password"]
    if user_name and password:
        global token
        try:
            token = server.login(req_user_name=user_name, req_password=password)
        except Exception as e:
            return json({
                "error": str(e)
            })

    return json({
        "Welcome": user_name
    })


# Accept input data and return a normalized version of it
@app.route('/', methods=["POST"])
async def normalized(request):
    data = request.json
    req_token = data[2].get("authorization")
    if str(token) == str(req_token):
        return json({
            data[0]["name"]: data[0].get([key for key in list(data[0].keys()) if "Val" in key][0]),
            data[1]["name"]: data[1].get([key for key in list(data[1].keys()) if "Val" in key][0]),
        })
    return json({
        "error": "Login deny"
    })


# Debug
@app.route("/token")
def get_token(request):
    return json({
        "token": str(token)
    })


if __name__ == '__main__':
    app.run()
