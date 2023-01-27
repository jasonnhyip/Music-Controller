# CLIENT_ID = "53f29f97e5824a83b1565ce36973ffad"
# CLIENT_SECRET = "3f274debf26147418040bca6270cac9f"
# REDIRECT_URI = "http://127.0.0.1:8000/spotify/redirect"

import environ

env = environ.Env()
environ.Env.read_env()

CLIENT_ID = env("CLIENT_ID")
CLIENT_SECRET = env("CLIENT_SECRET")
REDIRECT_URI = env("REDIRECT_URI")