import json
from utils import URL

with open("config.json", "r") as f:
    config = json.load(f)

WORKER_URL = URL(config["worker_url"])
