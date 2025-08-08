import urllib
import urllib.parse
import urllib.request
import json
from fastapi import FastAPI, Request
from fastapi.responses import JSONResponse
import uvicorn
from authlib.integrations.requests_client import OAuth2Session

app = FastAPI()


@app.get("/authenticate")
async def authenticate(_: Request):
    client_id = 'wsc-59444845-e41a-4a21-a766-ae8bdbc27983'
    client_secret = '<secret>'
    authorization_url = 'https://auth.iam.dev.experience.hyland.com/idp/connect/authorize'
    callback_url = 'http://rdv-007679.hylandqa.net:8000/token'

    oauth = OAuth2Session(client_id, client_secret, redirect_uri=callback_url)

    auth_url, state = oauth.create_authorization_url(
        authorization_url,
        scope="hxp environment_authorization openid profile offline_access",
        prompt="login")

    return JSONResponse(
        content={
            "auth_url": auth_url
        }
    )


@app.get("/health")
async def health(_: Request):
    return JSONResponse(
        content={
            "message": "My man!",
        })


@app.get("/token")
async def token(request: Request):
    code = request.query_params["code"]
    auth_url = "https://auth.iam.dev.experience.hyland.com/idp/connect/token"
    body = {
        "grant_type": "authorization_code",
        "code": code,
        "redirect_uri": "http://rdv-007679.hylandqa.net:8000/token",
        "client_id": "wsc-59444845-e41a-4a21-a766-ae8bdbc27983",
        "client_secret": "<secret>"
    }

    headers = {
        'Content-Type': 'application/x-www-form-urlencoded'
    }

    encoded_data = urllib.parse.urlencode(body).encode("utf-8")

    request = urllib.request.Request(auth_url, data=encoded_data, headers=headers, method="POST")

    with urllib.request.urlopen(request) as response:
        response_data = json.loads(response.read().decode("utf-8"))
        return response_data.get("access_token")


if __name__ == "__main__":
    uvicorn.run("auth_server:app", host="RDV-007679.hylandqa.net", port=8000, reload=True)