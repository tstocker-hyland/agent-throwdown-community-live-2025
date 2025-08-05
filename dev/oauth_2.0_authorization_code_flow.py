import threading
import webbrowser
from flask import Flask, request
from authlib.integrations.requests_client import OAuth2Session

# OAuth configuration
client_id = 'your_client_id'
client_secret = 'your_client_secret'
authorization_endpoint = 'https://example.com/oauth/authorize'
token_endpoint = 'https://example.com/oauth/token'
redirect_uri = 'http://localhost:5000/callback'

# Flask app to catch redirect
app = Flask(__name__)
oauth = OAuth2Session(client_id, client_secret, redirect_uri=redirect_uri)
token_data = {}

@app.route("/callback")
def callback():
    code = request.args.get("code")
    token = oauth.fetch_token(token_endpoint, authorization_response=request.url)
    token_data.update(token)
    return "Login complete! You can close this window."

# Run Flask in thread
def run_flask():
    app.run(port=5000, debug=False)

threading.Thread(target=run_flask).start()

# Open browser to login
auth_url, state = oauth.create_authorization_url(authorization_endpoint)
webbrowser.open(auth_url)
